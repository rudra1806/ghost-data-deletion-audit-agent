"""Gemini tool-using investigator for contested attributions.

The deterministic matcher resolves most resources outright.  When a resource
ties exactly on every evidence-based score between several cases (no
identifier on the record, same status fit, same job-phase fit), it records the
tie.  This agent then investigates each tie group with read-only tools and
proposes an assignment.  Its proposal is accepted only if it passes the same
structural checks the matcher enforces; otherwise the deterministic choice
stands.  Every tool call and decision is logged for the evaluation report.
"""
from __future__ import annotations

import json
from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple

from .data import Dataset, Identity, Request, system_for
from .evidence import EvidenceStore
from .llm import GeminiClient, function_calls
from .reasoner import WINDOW, Reasoner, in_phase

MAX_TURNS = 6

SYSTEM_PROMPT = """You are a deletion-audit investigator. A deterministic matcher must decide which
privacy-deletion case owns some records that carry no customer identifier. Records were
touched by the deletion worker inside several cases' activity windows, and the matcher's
evidence-based scores tie. Investigate with the tools, then call submit_decision exactly once.

Signals that matter (strongest first):
1. A deletion job's operations share the job's clock phase: the seconds offset between a
   case's account deletion and its follow-up operations falls in bands ~10s, ~21s, ~40s, ~52s
   (mod 60). get_case reports the phase check for each candidate.
2. A case already owning a record of the same system cannot take another.
3. Records whose state is evidenced before a case's audit time fit cases that otherwise
   verify as COMPLETE (the evidence exists to prove the final state).
4. Evidence listing order tends to follow subject order.
Assign each contested record to exactly one of its candidate cases. Be concise."""

TOOLS = [
    {"name": "get_case",
     "description": "Request metadata, resolved subject, records currently owned, and the phase check "
                    "of every contested record against this case's account deletion.",
     "parameters": {"type": "OBJECT", "properties": {"case_id": {"type": "STRING"}},
                    "required": ["case_id"]}},
    {"name": "get_resource",
     "description": "Deletion-worker events and evidence observations for one record.",
     "parameters": {"type": "OBJECT", "properties": {"resource_id": {"type": "STRING"}},
                    "required": ["resource_id"]}},
    {"name": "search_evidence",
     "description": "Find evidence lines containing a token (resource id, user id, email...).",
     "parameters": {"type": "OBJECT", "properties": {"token": {"type": "STRING"}},
                    "required": ["token"]}},
    {"name": "submit_decision",
     "description": "Final assignment of every contested record in this group.",
     "parameters": {"type": "OBJECT", "properties": {
         "assignments": {"type": "ARRAY", "items": {"type": "OBJECT", "properties": {
             "resource_id": {"type": "STRING"}, "case_id": {"type": "STRING"},
             "reason": {"type": "STRING"}}, "required": ["resource_id", "case_id", "reason"]}}},
         "required": ["assignments"]}},
]


class Investigator:
    def __init__(self, client: GeminiClient, reasoner: Reasoner, store: EvidenceStore, ds: Dataset):
        self.client = client
        self.r = reasoner
        self.store = store
        self.ds = ds

    # ------------------------------------------------------------------ tools
    def _worker_events(self, rid: str) -> List[dict]:
        return [{"activity_id": a.activity_id, "time": a.event_time.isoformat(), "type": a.event_type,
                 "result": a.reported_result}
                for a in self.r.events_by_resource.get(rid, []) if a.source_system == "deletion_worker"]

    def tool_get_case(self, case_id: str, ctx) -> dict:
        req, ident = ctx["cases"].get(case_id, (None, None))
        if req is None:
            return {"error": "unknown case"}
        owned = sorted(ctx["assigned"][case_id])
        acct_t = None
        for rid in owned:
            if rid.startswith("account_"):
                ts = [a.event_time for a in self.r.events_by_resource.get(rid, [])
                      if a.source_system == "deletion_worker" and abs(a.event_time - req.reported_at) <= WINDOW]
                acct_t = min(ts) if ts else None
        phase = {}
        for rid in ctx["group_resources"]:
            ts = [a.event_time for a in self.r.events_by_resource.get(rid, [])
                  if a.source_system == "deletion_worker"]
            if ts and acct_t:
                phase[rid] = {"seconds_after_account": int((ts[0] - acct_t).total_seconds()),
                              "in_phase": in_phase((ts[0] - acct_t).total_seconds())}
        return {"case_id": case_id, "subject": ident.user_id, "reported_status": req.reported_status,
                "requested_at": req.requested_at.isoformat(), "reported_at": req.reported_at.isoformat(),
                "audit_at": req.audit_at.isoformat(), "request_text": req.request_text[:300],
                "owned_records": owned, "provisional_status": ctx["provisional"].get(case_id),
                "contested_phase_check": phase}

    def tool_get_resource(self, rid: str, ctx) -> dict:
        obs = [{"evidence_id": o.evidence_id, "observed_at": o.observed_at.isoformat(),
                "present": o.present, "has_direct_identifiers": o.exposes_direct,
                "user_refs": sorted(o.user_refs), "source": o.source}
               for o in self.store.by_resource.get(rid, [])][:12]
        return {"resource_id": rid, "system": system_for(rid), "worker_events": self._worker_events(rid),
                "observations": obs, "grounded_owners": sorted(self.r.owners_of(rid))}

    def tool_search_evidence(self, token: str, ctx) -> dict:
        hits = []
        for file_id, text in sorted(self.store.texts.items()):
            for line in text.splitlines():
                if token and token.lower() in line.lower():
                    hits.append({"file_id": file_id, "line": line.strip()[:220]})
                    if len(hits) >= 10:
                        return {"hits": hits, "truncated": True}
        return {"hits": hits, "truncated": False}

    # ------------------------------------------------------------------ loop
    def review(self, cases: List[Tuple[Request, Identity]], assigned: Dict[str, Set[str]],
               case_filter: Optional[set] = None):
        log: List[dict] = []
        case_map = {req.case_id: (req, ident) for req, ident in cases}
        provisional = {req.case_id: self.r.build(req, ident, assigned[req.case_id]).status
                       for req, ident in cases}
        groups = self._groups(self.r.contested)
        for group in groups:
            members = {c for item in group for c in [item["chosen"], *item["rivals"]]}
            if case_filter and not (members & case_filter):
                continue
            ctx = {"cases": case_map, "assigned": assigned, "provisional": provisional,
                   "group_resources": [i["resource_id"] for i in group]}
            decision, transcript = self._investigate(group, ctx)
            accepted = self._apply(group, decision, assigned) if decision else False
            log.append({"group": group, "decision": decision, "accepted": accepted,
                        "tool_calls": transcript})
        return assigned, log

    @staticmethod
    def _groups(contested: List[dict]) -> List[List[dict]]:
        parent: Dict[str, str] = {}

        def find(x):
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for item in contested:
            for c in item["rivals"]:
                parent[find(c)] = find(item["chosen"])
        buckets: Dict[str, List[dict]] = defaultdict(list)
        for item in contested:
            buckets[find(item["chosen"])].append(item)
        return [buckets[k] for k in sorted(buckets)]

    def _investigate(self, group: List[dict], ctx) -> Tuple[Optional[list], List[dict]]:
        brief = [{"resource_id": i["resource_id"], "candidate_cases": sorted([i["chosen"], *i["rivals"]]),
                  "matcher_choice": i["chosen"]} for i in group]
        contents = [{"role": "user", "parts": [{"text":
                     "Contested records (each must go to one of its candidate cases):\n" +
                     json.dumps(brief, indent=1)}]}]
        transcript: List[dict] = []
        for _ in range(MAX_TURNS):
            try:
                data = self.client.generate(contents, "investigator_agent", system=SYSTEM_PROMPT,
                                            tools=TOOLS)
            except Exception as exc:
                transcript.append({"error": str(exc)[:200]})
                return None, transcript
            calls = function_calls(data)
            if not calls:
                return None, transcript
            contents.append(data["candidates"][0]["content"])
            responses = []
            for call in calls:
                name, args = call.get("name"), call.get("args", {}) or {}
                transcript.append({"tool": name, "args": args})
                if name == "submit_decision":
                    return args.get("assignments", []), transcript
                fn = {"get_case": lambda a: self.tool_get_case(a.get("case_id", ""), ctx),
                      "get_resource": lambda a: self.tool_get_resource(a.get("resource_id", ""), ctx),
                      "search_evidence": lambda a: self.tool_search_evidence(a.get("token", ""), ctx)}.get(name)
                result = fn(args) if fn else {"error": f"unknown tool {name}"}
                responses.append({"functionResponse": {"name": name, "response": {"result": result}}})
            contents.append({"role": "user", "parts": responses})
        return None, transcript

    def _apply(self, group: List[dict], decision: list, assigned: Dict[str, Set[str]]) -> bool:
        allowed = {i["resource_id"]: {i["chosen"], *i["rivals"]} for i in group}
        current = {i["resource_id"]: i["chosen"] for i in group}
        proposal = dict(current)
        for row in decision:
            rid, cid = row.get("resource_id"), row.get("case_id")
            if rid not in allowed or cid not in allowed[rid]:
                return False
            proposal[rid] = cid
        # Structural check: after the move no case holds two records of one system.
        trial = {c: set(v) for c, v in assigned.items()}
        for rid, cid in current.items():
            trial[cid].discard(rid)
        for rid, cid in proposal.items():
            system = system_for(rid)
            if any(system_for(x) == system for x in trial.get(cid, set())):
                return False
            trial.setdefault(cid, set()).add(rid)
        for cid, rids in trial.items():
            assigned[cid] = rids
        return True

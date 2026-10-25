"""End-to-end orchestration shared by main.py and the evaluation harness."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .data import EMAIL_RE, Dataset, Request, load_dataset, norm_email
from .evidence import EvidenceStore, Obs, load_evidence
from .intent import IntentClassifier, IntentVerdict
from .llm import GeminiClient
from .policy import Policy
from .reasoner import CasePlan, Reasoner
from .validate import validate_plan
from .vision import catalog_aliases, extract_images, vision_to_obs


@dataclass
class RunResult:
    plans: Dict[str, CasePlan]
    intents: Dict[str, IntentVerdict]
    client: GeminiClient
    store: EvidenceStore
    reasoner: Reasoner
    problems: Dict[str, List[str]] = field(default_factory=dict)
    agent_log: List[dict] = field(default_factory=list)


def alias_observations(store: EvidenceStore, aliases: Dict[str, str], ds: Dataset) -> List[Obs]:
    """Documents that mention a catalog alias (e.g. a statement number) show that resource."""
    out = []
    for file_id, text in store.texts.items():
        if not ds.manifest[file_id]["file_path"].endswith(".pdf"):
            continue
        low = text.lower()
        for alias, rid in aliases.items():
            if alias in low and rid not in store.by_resource:
                emails = {norm_email(e) for e in EMAIL_RE.findall(text)}
                refs = set(re.findall(r"\buser_\d+\b", text))
                from .data import parse_time, system_for
                captured = parse_time(ds.manifest[file_id]["captured_at"])
                out.append(Obs(file_id, captured, captured, system_for(rid) or "", rid, True,
                               direct_ids=emails, user_refs=refs, link_keys=emails | refs,
                               source="pdf:alias"))
    return out


def run(case_filter: Optional[set] = None, use_agent: bool = True,
        client: Optional[GeminiClient] = None, verbose: bool = False) -> RunResult:
    ds = load_dataset()
    client = client or GeminiClient()
    aliases = catalog_aliases(ds.activities)

    # 1. multimodal evidence: screenshots via Gemini vision, everything else parsed
    extractions = extract_images(client, ds.manifest)
    catalog_rids = {a.resource_id for a in ds.activities if a.event_type == "LINK_RESOURCE_IDENTITY"}
    store = load_evidence(ds.manifest, vision_to_obs(extractions, ds.manifest,
                                                     catalog_aliases(ds.activities, strict=False),
                                                     catalog_rids))
    for obs in alias_observations(store, aliases, ds):
        store.add(obs)

    # 2. intent: which requests actually authorize deletion
    all_requests: List[Request] = ds.sample_requests + ds.requests
    intents = IntentClassifier(client).classify([r.request_text for r in all_requests])

    # 3. deterministic reconstruction over the whole request population (windows
    #    are shared across cases, so attribution must see every deletion case)
    reasoner = Reasoner(ds, store, Policy(ds.rules))
    deletion_cases = []
    for req in all_requests:
        ident = reasoner.resolve(req)
        if intents[req.request_text].authorizes_deletion and ident is not None:
            deletion_cases.append((req, ident))
    assigned = reasoner.attribute(deletion_cases)

    agent_log: List[dict] = []
    if use_agent and client.available:
        from .investigator import Investigator
        inv = Investigator(client, reasoner, store, ds)
        assigned, agent_log = inv.review(deletion_cases, assigned, case_filter)

    plans: Dict[str, CasePlan] = {}
    problems: Dict[str, List[str]] = {}
    ident_of = {req.case_id: ident for req, ident in deletion_cases}
    for req in all_requests:
        if case_filter and req.case_id not in case_filter:
            continue
        if req.case_id not in ident_of:
            plans[req.case_id] = CasePlan(req.case_id, "NOT_APPLICABLE", [])
            continue
        plan = reasoner.build(req, ident_of[req.case_id], assigned[req.case_id])
        issues = validate_plan(plan, req, ds)
        if issues:
            problems[req.case_id] = issues
        plans[req.case_id] = plan
    return RunResult(plans, {r.case_id: intents[r.request_text] for r in all_requests},
                     client, store, reasoner, problems, agent_log)


def case_sort_key(case_id: str):
    m = re.search(r"(\d+)$", case_id)
    return (int(m.group(1)) if m else 0, case_id)


def steps_json(plan: CasePlan) -> str:
    return json.dumps(plan.steps, ensure_ascii=False, separators=(",", ":"))

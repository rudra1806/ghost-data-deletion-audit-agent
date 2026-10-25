"""Deterministic deletion-state reconstruction and step planning.

Pipeline per case:
  1. resolve the subject (current + historical identifiers)
  2. discover candidate resources (identifier links, catalog links, and the
     deletion worker's activity window around `reported_at`)
  3. attribute unlinked activity resources across cases that share a window
  4. reconstruct each resource's state at `audit_at`
  5. apply policy and emit ordered FINDING / REMEDIATION / VERIFICATION steps
"""
from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set, Tuple

from .data import Activity, Dataset, Identity, Request, norm_email, system_for
from .evidence import EvidenceStore, Obs, Scope
from .policy import OPERATION_ORDER, PHASE_OF, PHASE_ORDER, STATE_OF, Policy

WINDOW = timedelta(hours=2, minutes=30)
WORKER_EVENTS = {"DELETE_RECORD", "REDACT_RECORD", "ANONYMIZE_RECORD", "RETAIN_RECORD",
                 "DISABLE_DATA_FLOW", "BLOCK_RESTORE", "CHECK_DATA_FLOW", "CHECK_RESTORE_ACCESS"}
STATUS_RESULT_FIT = {
    "COMPLETE": {"SUCCESS": 2, "PARTIAL": 0, "FAILED": -1},
    "PARTIALLY_COMPLETE": {"PARTIAL": 2, "SUCCESS": 1, "FAILED": 0},
    "NOT_STARTED": {"FAILED": 2, "PARTIAL": 0, "SUCCESS": -1},
}
# Operations issued by one deletion job keep that job's clock phase: relative
# to the job's account deletion they land at these seconds-of-minute bands
# (measured on the sample cases; an unrelated event matches ~40% of the time).
PHASE_BANDS = [(8, 12), (19, 25), (38, 43), (49, 54)]


def in_phase(delta_seconds: float) -> bool:
    r = int(round(delta_seconds)) % 60
    return any(lo <= r <= hi for lo, hi in PHASE_BANDS)


CATALOG_RE = re.compile(r"linked (\S+) .*? to (\S+?@\S+?) and (user_\d+)|"
                        r"confirmed (\S+) .*? belongs only to (\S+?@\S+?) and (user_\d+)")


@dataclass
class ResourceState:
    resource_id: str
    system: str
    category: str
    action: str
    present: Optional[bool]
    exposes_direct: bool
    has_user_ref: bool
    flow_enabled: Optional[bool]
    restore_allowed: Optional[bool]
    evidence: Optional[str]              # citable evidence id for the state
    basis: str = ""                       # how the state was established (for tracing)


@dataclass
class CasePlan:
    case_id: str
    status: str
    steps: List[dict]
    user_id: Optional[str] = None
    resources: List[ResourceState] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


class Reasoner:
    def __init__(self, ds: Dataset, store: EvidenceStore, policy: Policy):
        self.ds = ds
        self.store = store
        self.policy = policy
        self.key_owner: Dict[str, Set[str]] = defaultdict(set)
        for ident in ds.identities.values():
            for key in ident.emails | ident.hashes | {ident.user_id}:
                self.key_owner[key].add(ident.user_id)
            for phone in ident.phones:
                if phone:
                    self.key_owner["phone:" + phone].add(ident.user_id)
        self.catalog: Dict[str, Set[str]] = defaultdict(set)   # resource -> users
        self.catalog_evidence: Dict[str, str] = {}
        for a in ds.activities:
            if a.event_type == "LINK_RESOURCE_IDENTITY":
                users = set(re.findall(r"\buser_\d+\b", a.details))
                for email in re.findall(r"[\w.+\-]+@[\w.\-]+\.\w+", a.details):
                    users |= self.key_owner.get(norm_email(email), set())
                self.catalog[a.resource_id] |= users
                self.catalog_evidence[a.resource_id] = a.activity_id
        self.owners: Dict[str, Set[str]] = {}
        self.contested: List[dict] = []
        self.offers: Dict[str, list] = {}
        self.events_by_resource: Dict[str, List[Activity]] = defaultdict(list)
        for a in ds.activities:
            self.events_by_resource[a.resource_id].append(a)
        self.worker_events: List[Activity] = [
            a for a in ds.activities
            if a.source_system == "deletion_worker" and a.event_type in WORKER_EVENTS]

    # ------------------------------------------------------------------ identity
    def resolve(self, req: Request) -> Optional[Identity]:
        uid = self.ds.email_index.get(norm_email(req.email))
        return self.ds.identities.get(uid) if uid else None

    # ------------------------------------------------------------------ ownership
    def owners_of(self, rid: str) -> Set[str]:
        """Subjects a resource is grounded to by identifiers anywhere in evidence."""
        if rid in self.owners:
            return self.owners[rid]
        owners: Set[str] = set(self.catalog.get(rid, set()))
        for o in self.store.by_resource.get(rid, []):
            for key in o.link_keys | o.direct_ids | o.user_refs:
                if key.startswith("name:"):
                    continue
                matched = self.key_owner.get(key)
                if matched:
                    owners |= matched
                elif "@" in key:
                    owners.add("unknown:" + key)   # identifier of someone not in the snapshot
        self.owners[rid] = owners
        return owners

    # ------------------------------------------------------------------ discovery
    def linked_resources(self, ident: Identity) -> Set[str]:
        found: Set[str] = set()
        for key in ident.keys():
            if key.startswith("name:"):
                continue
            found |= self.store.by_key.get(key, set())
        for rid, users in self.catalog.items():
            if ident.user_id in users:
                found.add(rid)
        return {r for r in found if ident.user_id in self.owners_of(r)}

    def window_events(self, req: Request) -> List[Activity]:
        lo, hi = req.reported_at - WINDOW, req.reported_at + WINDOW
        return [a for a in self.worker_events if lo <= a.event_time <= hi]

    def episode_bounds(self, cases: List[Tuple[Request, Identity]]) -> Dict[str, Tuple]:
        """Each request owns the evidence between the previous request's audit and its own.

        A subject can file several deletion requests months apart; a record
        observed before an earlier audit belongs to that earlier episode.
        """
        by_user: Dict[str, List[Request]] = defaultdict(list)
        for req, ident in cases:
            by_user[ident.user_id].append(req)
        bounds = {}
        for reqs in by_user.values():
            reqs.sort(key=lambda r: r.audit_at)
            prev = None
            for r in reqs:
                bounds[r.case_id] = (prev, r.audit_at)
                prev = r.audit_at
        return bounds

    def in_episode(self, rid: str, req: Request, bounds: Tuple) -> bool:
        lo, hi = bounds
        if any(abs(a.event_time - req.reported_at) <= WINDOW
               for a in self.events_by_resource.get(rid, [])):
            return True
        return any((lo is None or o.observed_at > lo) and o.observed_at <= hi
                   for o in self.store.by_resource.get(rid, []))

    def attribute(self, cases: List[Tuple[Request, Identity]]) -> Dict[str, Set[str]]:
        """Assign resources to cases.

        Linked resources (identifiers grounded in evidence) go to their
        subject's request for the matching episode.  Unlinked resources the
        deletion worker touched inside several cases' windows are contested and
        resolved per system, in activity-time order:
          * accounts: only cases still missing an account; the worker's
            reported result must fit the case's reported status;
          * other systems: only cases with no resource of that system yet;
          * a resource with citable state evidence prefers a case that would
            otherwise verify as COMPLETE (the evidence exists to prove it);
          * remaining ties follow subject order (lower user number first).
        """
        bounds = self.episode_bounds(cases)
        assigned: Dict[str, Set[str]] = defaultdict(set)
        req_of = {req.case_id: req for req, _ in cases}
        user_rank = {req.case_id: int(re.sub(r"\D", "", ident.user_id) or 0) for req, ident in cases}
        for req, ident in cases:
            linked = self.linked_resources(ident)
            assigned[req.case_id] |= {r for r in linked
                                      if self.in_episode(r, req, bounds[req.case_id])}

        provisional_complete = {}
        for req, ident in cases:
            plan = self.build(req, ident, assigned[req.case_id])
            provisional_complete[req.case_id] = plan.status == "COMPLETE"

        offers: Dict[str, List[Tuple[Activity, Request]]] = defaultdict(list)
        for req, ident in cases:
            for a in self.window_events(req):
                if self.owners_of(a.resource_id):
                    continue
                offers[a.resource_id].append((a, req))

        def has_system(case_id: str, system: str) -> bool:
            return any((system_for(r) or "") == system for r in assigned[case_id])

        def has_evidence(rid: str, req: Request) -> bool:
            return any(o.captured_at <= req.audit_at and o.observed_at <= req.audit_at
                       for o in self.store.by_resource.get(rid, []))

        position = {}
        for i, o in enumerate(self.store.observations):
            position.setdefault(o.resource_id, i)

        def worker_time(rid: str, req: Request) -> Optional[datetime]:
            ts = [a.event_time for a in self.events_by_resource.get(rid, [])
                  if a.source_system == "deletion_worker" and abs(a.event_time - req.reported_at) <= WINDOW]
            return min(ts) if ts else None

        def phase_ok(t_follow: datetime, t_account: datetime) -> bool:
            return in_phase((t_follow - t_account).total_seconds())

        # Pass 1 assigns accounts, pass 2 everything else (whose phase is
        # measured against the account the case ended up with).  Within a pass,
        # offers are scored and taken best-first (greedy global matching), so a
        # strong match cannot be stolen by a weaker one.
        self.contested = []
        taken: Set[str] = set()
        for stage in ("account", "other"):
            pairs = []
            for rid, cands in offers.items():
                system = system_for(rid) or ""
                if (system == "account_service") != (stage == "account"):
                    continue
                for a, q in cands:
                    linked_events = [t for t in (worker_time(r, q) for r in assigned[q.case_id]
                                                 if not r.startswith("account_")) if t]
                    if stage == "account":
                        # The worker deletes the primary profile about an hour before
                        # the workflow reports, and its result should match the claim.
                        offset = (a.event_time - q.reported_at).total_seconds() / 3600
                        timing = 1 if -1.4 <= offset <= -0.6 else 0
                        status = STATUS_RESULT_FIT.get(q.reported_status, {}).get(a.reported_result, 0)
                        phase = sum(phase_ok(t, a.event_time) for t in linked_events)
                        fit = (3 * status + timing, phase)
                    else:
                        acct = [worker_time(r, q) for r in assigned[q.case_id] if r.startswith("account_")]
                        acct = [t for t in acct if t]
                        phase = int(bool(acct) and phase_ok(a.event_time, acct[0]))
                        evidence = 1 if has_evidence(rid, q) == provisional_complete[q.case_id] else 0
                        fit = (phase, evidence)
                    order = position.get(rid, len(position) + a.event_time.timestamp())
                    pairs.append(((-fit[0], -fit[1]), order, user_rank[q.case_id], rid, q.case_id))
            pairs.sort()
            for negfit, _, _, rid, case_id in pairs:
                if rid in taken or has_system(case_id, system_for(rid) or ""):
                    continue
                # Exact ties on every evidence-based score are recorded: the pick
                # between them rests on ordering conventions only, so the
                # investigator agent may review it.
                rivals = sorted({c for nf, _, _, r, c in pairs
                                 if r == rid and nf == negfit and c != case_id
                                 and not has_system(c, system_for(rid) or "")})
                if rivals:
                    self.contested.append({"resource_id": rid, "chosen": case_id, "rivals": rivals})
                assigned[case_id].add(rid)
                taken.add(rid)
        self.offers = offers
        return assigned

    # ------------------------------------------------------------------ state
    def state_at(self, rid: str, req: Request) -> ResourceState:
        system = system_for(rid) or ""
        obs_all = self.store.by_resource.get(rid, [])
        if obs_all and obs_all[0].system:
            system = obs_all[0].system
        category = self.policy.category(system, obs_all)
        action = self.policy.required_action(category)
        usable = [o for o in obs_all if o.observed_at <= req.audit_at and
                  (o.present is not None or o.flow_enabled is not None or o.restore_allowed is not None)]
        usable.sort(key=lambda o: (o.observed_at, o.captured_at))
        st = ResourceState(rid, system, category, action, None, False, False, None, None, None)
        if usable:
            latest_time = usable[-1].observed_at
            latest = [o for o in usable if o.observed_at == latest_time]
            o = latest[-1]
            st.present = any(x.present for x in latest if x.present is not None) \
                if any(x.present is not None for x in latest) else None
            st.exposes_direct = any(x.exposes_direct for x in latest)
            st.has_user_ref = any(x.user_refs for x in latest)
            flows = [x for x in usable if x.flow_enabled is not None]
            if flows:
                st.flow_enabled = flows[-1].flow_enabled
            restores = [x for x in usable if x.restore_allowed is not None]
            if restores:
                st.restore_allowed = restores[-1].restore_allowed
            if st.present is None and (st.flow_enabled is not None or st.restore_allowed is not None):
                st.present = True
            st.evidence = self.cite(usable, req, st)
            st.basis = f"latest {o.source}@{o.evidence_id} {o.observed_at.isoformat()}"
            # A later complete listing of the system that omits the record
            # supersedes an older sighting ("old report said it still existed").
            scope = self.scope_absence(rid, system, req)
            replica_copy = any("replica" in x.source for x in latest)
            if scope and scope.observed_at > latest_time and st.present and not replica_copy and \
                    st.category not in ("DATA_FLOW", "BACKUP_ARCHIVE"):
                st.present = False
                st.exposes_direct = st.has_user_ref = False
                st.evidence = scope.evidence_id if scope.captured_at <= req.audit_at else None
                st.basis += f" | superseded by scope-absence {scope.evidence_id}"
            elif st.present is False and st.evidence is None and scope:
                st.evidence = scope.evidence_id
        else:
            scope = self.scope_absence(rid, system, req)
            if scope:
                st.present = False
                st.evidence = scope.evidence_id if scope.captured_at <= req.audit_at else None
                st.basis = f"scope-absence {scope.evidence_id}"
        return st

    def scope_absence(self, rid: str, system: str, req: Request) -> Optional[Scope]:
        best = None
        for sc in self.store.scopes:
            if sc.system != system or sc.observed_at > req.audit_at or sc.captured_at > req.audit_at:
                continue
            if rid in sc.resource_ids:
                continue
            if best is None or sc.observed_at > best.observed_at:
                best = sc
        return best

    def cite(self, usable: List[Obs], req: Request, st: ResourceState) -> Optional[str]:
        """Latest citable (captured <= audit_at) observation agreeing with the state."""
        for o in reversed(usable):
            if o.captured_at > req.audit_at:
                continue
            if st.flow_enabled is not None and o.flow_enabled is not None:
                if o.flow_enabled == st.flow_enabled:
                    return o.evidence_id
                continue
            if st.restore_allowed is not None and o.restore_allowed is not None:
                if o.restore_allowed == st.restore_allowed:
                    return o.evidence_id
                continue
            if o.present is not None and o.present == st.present:
                return o.evidence_id
        return None

    # ------------------------------------------------------------------ planning
    def plan_resource(self, st: ResourceState) -> Tuple[List[str], List[str], List[str]]:
        """(findings, remediations, verifications) operations for one resource."""
        f: List[str] = []
        r: List[str] = []
        v: List[str] = []
        act = st.action
        if st.category == "DATA_FLOW":
            if st.flow_enabled:
                f, r = ["REPORT_ACTIVE_DATA_FLOW"], ["DISABLE_DATA_FLOW"]
            v = ["VERIFY_DATA_FLOW_DISABLED"]
        elif st.category == "BACKUP_ARCHIVE":
            if st.restore_allowed:
                f, r = ["REPORT_RESTORE_RISK"], ["BLOCK_RESTORE"]
            v = ["VERIFY_RESTORE_BLOCKED"]
        elif act == "RETAIN":
            v = ["VERIFY_RECORD_PRESENT"]
        elif act == "DELETE":
            if st.present:
                f, r = ["REPORT_REMAINING_RECORD"], ["DELETE_RECORD"]
            v = ["VERIFY_RECORD_ABSENT"]
        elif act == "REDACT":
            if st.present is False:
                v = ["VERIFY_RECORD_ABSENT"]
            else:
                if st.present and st.exposes_direct:
                    f, r = ["REPORT_EXPOSED_PII"], ["REDACT_RECORD"]
                v = ["VERIFY_RECORD_REDACTED"]
        elif act == "ANONYMIZE":
            if st.present is False:
                v = ["VERIFY_RECORD_ABSENT"]
            else:
                if st.present and (st.exposes_direct or st.has_user_ref):
                    f, r = ["REPORT_EXPOSED_PII"], ["ANONYMIZE_RECORD"]
                v = ["VERIFY_RECORD_ANONYMIZED"]
        return f, r, v

    def build(self, req: Request, ident: Identity, resources: Set[str]) -> CasePlan:
        states = [self.state_at(rid, req) for rid in sorted(resources)]
        raw: List[Tuple[str, ResourceState]] = []
        for st in states:
            f, r, v = self.plan_resource(st)
            raw += [(op, st) for op in f + r + v]
        incomplete = any(PHASE_OF[op] == "FINDING" for op, _ in raw)
        status = "INCOMPLETE" if incomplete else "COMPLETE"
        raw.sort(key=lambda x: (PHASE_ORDER[PHASE_OF[x[0]]], OPERATION_ORDER.index(x[0]),
                                x[1].system, x[1].resource_id))
        steps = []
        for i, (op, st) in enumerate(raw, 1):
            phase = PHASE_OF[op]
            if phase == "FINDING" or (status == "COMPLETE" and phase == "VERIFICATION"):
                ev = st.evidence or ""
            else:
                ev = ""
            steps.append({"step_no": i, "phase": phase, "system_id": st.system,
                          "resource_id": st.resource_id, "operation": op,
                          "state": STATE_OF[op], "evidence_id": ev})
        return CasePlan(req.case_id, status, steps, ident.user_id, states)

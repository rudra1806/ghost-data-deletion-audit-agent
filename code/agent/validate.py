"""Output contract checks applied to every plan before it is written."""
from __future__ import annotations

from typing import List

from .data import Dataset, Request, parse_time
from .policy import OPERATION_ORDER, PHASE_OF, PHASE_ORDER, STATE_OF

REQUIRED_KEYS = {"step_no", "phase", "system_id", "resource_id", "operation", "state", "evidence_id"}


def validate_plan(plan, req: Request, ds: Dataset) -> List[str]:
    issues: List[str] = []
    if plan.status not in ("COMPLETE", "INCOMPLETE", "NOT_APPLICABLE"):
        issues.append(f"bad status {plan.status}")
    if plan.status == "NOT_APPLICABLE":
        if plan.steps:
            issues.append("NOT_APPLICABLE must have []")
        return issues
    if not plan.steps:
        issues.append("deletion case with no steps")
    prev = None
    for i, step in enumerate(plan.steps, 1):
        if set(step) != REQUIRED_KEYS:
            issues.append(f"step {i} keys {sorted(step)}")
        if step["step_no"] != i:
            issues.append(f"step numbering at {i}")
        op = step["operation"]
        if op not in PHASE_OF or PHASE_OF[op] != step["phase"] or STATE_OF[op] != step["state"]:
            issues.append(f"step {i} op/phase/state mismatch {op}")
            continue
        key = (PHASE_ORDER[step["phase"]], OPERATION_ORDER.index(op), step["system_id"],
               step["resource_id"])
        if prev and key < prev:
            issues.append(f"step {i} out of order")
        prev = key
        ev = step["evidence_id"]
        cite_required = step["phase"] == "FINDING" or plan.status == "COMPLETE"
        if cite_required and not ev:
            issues.append(f"step {i} {op} {step['resource_id']} missing evidence")
        if not cite_required and ev:
            issues.append(f"step {i} future step must not cite evidence")
        if ev.startswith("evidence_"):
            meta = ds.manifest.get(ev)
            if meta is None:
                issues.append(f"step {i} unknown evidence {ev}")
            elif parse_time(meta["captured_at"]) > req.audit_at:
                issues.append(f"step {i} cites {ev} captured after audit_at")
    if plan.status == "COMPLETE" and any(s["phase"] != "VERIFICATION" for s in plan.steps):
        issues.append("COMPLETE plan contains non-verification steps")
    if plan.status == "INCOMPLETE" and not any(s["phase"] == "FINDING" for s in plan.steps):
        issues.append("INCOMPLETE plan without findings")
    return issues

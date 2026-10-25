"""Evaluation harness.

    python3 code/evaluation/main.py            # score samples + custom cases, write report
    python3 code/evaluation/main.py --no-agent # deterministic-only ablation

Scores the agent on the 32 public samples (hidden-label proxy) and on custom
adversarial cases built by perturbing real requests, then writes
code/evaluation/evaluation_report.md (metrics + custom cases + the hand-kept
failure log in code/evaluation/notes.md).
"""
from __future__ import annotations

import argparse
import copy
import csv
import json
import sys
from collections import Counter
from dataclasses import replace
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agent.data import DATASET, REPO_ROOT, load_dataset  # noqa: E402
from agent.pipeline import case_sort_key, run  # noqa: E402

EVAL_DIR = Path(__file__).resolve().parent
FIELDS = ["phase", "system_id", "resource_id", "operation", "state", "evidence_id"]


def load_gold():
    gold = {}
    with open(DATASET / "sample_output.csv", newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            gold[row["case_id"]] = (row["deletion_status"], json.loads(row["steps_json"]))
    return gold


def key(step, fields=FIELDS):
    return tuple(step[f] for f in fields)


def score(plans, gold):
    m = Counter()
    per_case = []
    for cid, (gstatus, gsteps) in sorted(gold.items(), key=lambda kv: case_sort_key(kv[0])):
        plan = plans[cid]
        psteps = plan.steps
        m["cases"] += 1
        m["status_ok"] += plan.status == gstatus
        gk, pk = Counter(key(s) for s in gsteps), Counter(key(s) for s in psteps)
        tp = sum((gk & pk).values())
        m["tp"] += tp
        m["gold_steps"] += sum(gk.values())
        m["pred_steps"] += sum(pk.values())
        m["sequence_ok"] += [key(s) for s in psteps] == [key(s) for s in gsteps]
        m["sequence_ok_no_ev"] += [key(s, FIELDS[:-1]) for s in psteps] == [key(s, FIELDS[:-1]) for s in gsteps]
        # resource discovery
        gres = {(s["system_id"], s["resource_id"]) for s in gsteps}
        pres = {(s["system_id"], s["resource_id"]) for s in psteps}
        m["res_tp"] += len(gres & pres)
        m["res_gold"] += len(gres)
        m["res_pred"] += len(pres)
        # field-level accuracy on positionally aligned steps
        for i, g in enumerate(gsteps):
            p = psteps[i] if i < len(psteps) else None
            for f in FIELDS + ["step_no"]:
                m[f"field_total_{f}"] += 1
                m[f"field_ok_{f}"] += bool(p) and p.get(f) == g[f]
        # evidence: for steps matched ignoring evidence, is the citation right?
        g_noev = {key(s, FIELDS[:-1]): s["evidence_id"] for s in gsteps}
        for s in psteps:
            k = key(s, FIELDS[:-1])
            if k in g_noev:
                m["ev_total"] += 1
                m["ev_ok"] += s["evidence_id"] == g_noev[k]
        per_case.append((cid, gstatus, plan.status, tp, len(gsteps), len(psteps),
                         [key(s) for s in psteps] == [key(s) for s in gsteps]))
    return m, per_case


def changed_picks(agent_log) -> int:
    n = 0
    for g in agent_log:
        chosen = {i["resource_id"]: i["chosen"] for i in g["group"]}
        for row in g.get("decision") or []:
            if row.get("resource_id") in chosen and row.get("case_id") != chosen[row["resource_id"]]:
                n += 1
    return n


def pct(a, b):
    return f"{100.0 * a / b:.1f}%" if b else "n/a"


# --------------------------------------------------------------------------- custom cases

def custom_cases(ds, base_result):
    """Adversarial variants of real requests; expected outcomes stated up front."""
    from agent.intent import IntentClassifier
    from agent.reasoner import Reasoner
    from agent.policy import Policy

    reasoner = base_result.reasoner
    by_id = {r.case_id: r for r in ds.sample_requests}
    gold = load_gold()
    out = []

    def plan_for(req):
        ident = reasoner.resolve(req)
        verdict = IntentClassifier(base_result.client).classify([req.request_text])[req.request_text]
        if ident is None or not verdict.authorizes_deletion:
            return "NOT_APPLICABLE", [], verdict
        # reuse the attribution of the original case for its resources
        orig = base_result.plans.get(req.case_id.split("__")[0])
        resources = {s.resource_id for s in orig.resources} if orig else set()
        plan = reasoner.build(req, ident, resources)
        return plan.status, plan.steps, verdict

    # C1: negated request that mentions deletion words
    r = replace(by_id["case_01"], case_id="case_01__negated",
                request_text="I am NOT asking you to delete or close anything. Please just send me a copy "
                             "of the personal data on my account and keep the profile active.")
    st, steps, v = plan_for(r)
    out.append(("C1 negated deletion words", "case_01 with a copy-only request that says 'not delete'",
                "NOT_APPLICABLE, []", f"{st}, {len(steps)} steps (intent via {v.source})",
                st == "NOT_APPLICABLE" and not steps))

    # C2: request filed under the subject's historical e-mail address
    base = by_id["case_12"]
    ident = reasoner.resolve(base)
    current = next(e for e in ident.emails if e != base.email.lower())
    r = replace(base, case_id="case_12__alt_email", email=current)
    st, steps, v = plan_for(r)
    ok = st == gold["case_12"][0] and [key(s) for s in steps] == [key(s) for s in gold["case_12"][1]]
    out.append(("C2 identity via other address", f"case_12 re-filed with the subject's other address ({current})",
                f"same as gold: {gold['case_12'][0]}, {len(gold['case_12'][1])} steps",
                f"{st}, {len(steps)} steps", ok))

    # C3: time travel - audit before the export that proves deletion; the stale
    #     "account still ACTIVE" snapshot must then drive the answer
    base = by_id["case_26"]
    r = replace(base, case_id="case_26__early_audit", audit_at=base.audit_at - timedelta(days=5, hours=12))
    st, steps, v = plan_for(r)
    acct = [s for s in steps if s["resource_id"] == "account_5684"]
    ok = st == "INCOMPLETE" and any(s["operation"] == "REPORT_REMAINING_RECORD" for s in acct)
    out.append(("C3 audit-time cut-off", "case_26 audited on 2026-09-10 (before the 404 proof on 09-15)",
                "INCOMPLETE with REPORT_REMAINING_RECORD account_5684 (09-09 snapshot is latest evidence)",
                f"{st}; account steps {[s['operation'] for s in acct]}", ok))

    # C4: multilingual deletion request (German, not in the dataset)
    r = replace(by_id["case_02"], case_id="case_02__german",
                request_text="Bitte löschen Sie mein Kundenkonto und alle damit verbundenen personenbezogenen "
                             "Daten dauerhaft.")
    st, steps, v = plan_for(r)
    ok = st == gold["case_02"][0]
    out.append(("C4 unseen language", "case_02 with a German erasure request",
                f"deletion handled -> {gold['case_02'][0]}", f"{st} (intent via {v.source})", ok))

    # C5: replica ghost - the primary is clean but the failover replica still holds the profile
    base = by_id["case_05"]
    st, steps, v = plan_for(replace(base, case_id="case_05__replica"))
    ok = any(s["operation"] == "REPORT_REMAINING_RECORD" and s["resource_id"] == "account_005" for s in steps)
    out.append(("C5 replica drift ghost", "case_05: profile deleted from primary, alive in failover replica",
                "INCOMPLETE, REPORT_REMAINING_RECORD account_005 citing the replica snapshot",
                f"{st}; first step {steps[0]['operation'] if steps else '-'} {steps[0]['evidence_id'] if steps else ''}",
                ok))
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-agent", action="store_true")
    args = parser.parse_args()
    ds = load_dataset()
    gold = load_gold()
    result = run(use_agent=not args.no_agent)
    m, per_case = score(result.plans, gold)
    prec = m["tp"] / m["pred_steps"] if m["pred_steps"] else 0
    rec = m["tp"] / m["gold_steps"] if m["gold_steps"] else 0
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0
    customs = custom_cases(ds, result)

    notes = (EVAL_DIR / "notes.md").read_text(encoding="utf-8") if (EVAL_DIR / "notes.md").exists() else ""
    L = ["# Evaluation Report", "",
         "Generated by `python3 code/evaluation/main.py`"
         f"{' --no-agent' if args.no_agent else ''}. Labels come only from the public "
         "`dataset/sample_output.csv`; the 518 evaluation requests have no labels, so the samples are the "
         "accuracy proxy and the custom cases probe behaviours the samples do not isolate.", "",
         "## Sample-set accuracy (32 labelled cases)", "",
         "| Metric | Value |", "|---|---|",
         f"| Case-level status accuracy | {m['status_ok']}/{m['cases']} ({pct(m['status_ok'], m['cases'])}) |",
         f"| Step-level precision (exact step match, all 6 fields) | {m['tp']}/{m['pred_steps']} ({pct(m['tp'], m['pred_steps'])}) |",
         f"| Step-level recall | {m['tp']}/{m['gold_steps']} ({pct(m['tp'], m['gold_steps'])}) |",
         f"| Step-level F1 | {f1 * 100:.1f}% |",
         f"| Sequence accuracy (whole ordered steps_json identical) | {m['sequence_ok']}/{m['cases']} ({pct(m['sequence_ok'], m['cases'])}) |",
         f"| Sequence accuracy ignoring evidence ids | {m['sequence_ok_no_ev']}/{m['cases']} ({pct(m['sequence_ok_no_ev'], m['cases'])}) |",
         f"| Resource discovery precision | {m['res_tp']}/{m['res_pred']} ({pct(m['res_tp'], m['res_pred'])}) |",
         f"| Resource discovery recall | {m['res_tp']}/{m['res_gold']} ({pct(m['res_tp'], m['res_gold'])}) |",
         f"| Evidence citation accuracy (on otherwise-matching steps) | {m['ev_ok']}/{m['ev_total']} ({pct(m['ev_ok'], m['ev_total'])}) |",
         "", "### Field-level accuracy (position-aligned against gold)", "",
         "| Field | Accuracy |", "|---|---|"]
    for f in FIELDS + ["step_no"]:
        L.append(f"| {f} | {pct(m['field_ok_' + f], m['field_total_' + f])} |")
    L += ["", "### Per-case results", "", "| Case | Gold | Predicted | Matching steps | Gold steps | Pred steps | Exact sequence |",
          "|---|---|---|---|---|---|---|"]
    for cid, gs, ps, tp, ng, npred, ok in per_case:
        L.append(f"| {cid} | {gs} | {ps} | {tp} | {ng} | {npred} | {'yes' if ok else 'no'} |")
    L += ["", "## Custom evaluation cases (built by us)", "",
          "Each case perturbs a real request to isolate one behaviour; expectations were written before running.", "",
          "| Case | Scenario | Expected | Observed | Pass |", "|---|---|---|---|---|"]
    for name, scen, exp, obs, ok in customs:
        L.append(f"| {name} | {scen} | {exp} | {obs} | {'PASS' if ok else 'FAIL'} |")
    test_ids = {r.case_id for r in ds.requests}
    dist = Counter(result.plans[c].status for c in test_ids)
    L += ["", "## Evaluation-set sanity (518 unlabelled requests)", "",
          f"- Status distribution: {dict(dist)}",
          f"- Contract validation issues: {sum(len(v) for k, v in result.problems.items() if k in test_ids)}",
          f"- Contested attributions recorded by the matcher: {len(result.reasoner.contested)}",
          f"- Investigator groups reviewed: {len(result.agent_log)}; proposals accepted: "
          f"{sum(1 for g in result.agent_log if g['accepted'])}; proposals that changed the "
          f"matcher's pick: {changed_picks(result.agent_log)}",
          f"- Intent verdicts where Gemini and the rule cross-check disagree: "
          f"{sorted(c for c, v in result.intents.items() if v.disagreement)}", ""]
    L.append(notes)
    (EVAL_DIR / "evaluation_report.md").write_text("\n".join(L), encoding="utf-8")
    (EVAL_DIR / "agent_decisions.json").write_text(json.dumps(result.agent_log, indent=1, default=str),
                                                    encoding="utf-8")
    print("\n".join(L[:30]))
    print("custom:", [(c[0], c[4]) for c in customs])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

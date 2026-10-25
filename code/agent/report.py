"""Markdown reports generated from a run (usage + per-case trace)."""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone

from .data import REPO_ROOT

EVAL_DIR = REPO_ROOT / "code" / "evaluation"


def write_usage_report(result, n_requests: int, elapsed: float) -> None:
    summary = result.client.summary()
    lines = ["# Token Usage and Cost Report", "",
             f"Generated automatically by `code/main.py` at "
             f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} for the final full-dataset "
             f"run that produced `output.csv` ({n_requests} requests, wall time {elapsed:.0f}s; the "
             f"first live execution of the same pipeline took ~17 minutes because calls are throttled "
             f"to the free-tier per-minute limits, and reruns are served from the response cache).", "",
             "Provider: **Google Gemini API** (REST `generateContent`), free tier, so the actual spend "
             "was $0. The estimate below prices tokens at published list rates per 1M tokens; Gemini 3.x "
             "models are priced at the rate of their 2.5 class (Flash-Lite $0.10/$0.40, Flash "
             "$0.30/$2.50) as a stated proxy. Roles: vision = strongest Flash model allowed by the "
             "free tier, text (intent + investigator) = Flash-Lite with the larger daily quota; each has "
             "a fallback model if its quota is exhausted. `api_calls` are live requests in this run; "
             "`cache_hits` are identical prompts answered from `code/cache/llm/` (same tokens, no new "
             "spend). Token counts include both, so they describe the full workload of producing the "
             "output.", ""]
    if not summary:
        lines += ["No model calls were made in this run (offline mode).", ""]
    tot_calls = tot_in = tot_out = tot_api = 0
    tot_cost = 0.0
    lines += ["## Per-model totals", "",
              "| Model | Logical calls | Live API calls | Cache hits | Input tokens | Output tokens | "
              "Total tokens | Est. cost (USD) |",
              "|---|---|---|---|---|---|---|---|"]
    for model, s in summary.items():
        total = s["input_tokens"] + s["output_tokens"]
        lines.append(f"| {model} | {s['logical_calls']} | {s['api_calls']} | {s['cache_hits']} | "
                     f"{s['input_tokens']:,} | {s['output_tokens']:,} | {total:,} | "
                     f"${s['estimated_cost_usd']:.4f} |")
        tot_calls += s["logical_calls"]
        tot_api += s["api_calls"]
        tot_in += s["input_tokens"]
        tot_out += s["output_tokens"]
        tot_cost += s["estimated_cost_usd"]
    tot = tot_in + tot_out
    lines += [f"| **Overall** | **{tot_calls}** | **{tot_api}** | | **{tot_in:,}** | **{tot_out:,}** | "
              f"**{tot:,}** | **${tot_cost:.4f}** |", "",
              "## Per-request averages", "",
              f"- Requests processed: {n_requests}",
              f"- Average tokens per request: {tot / max(n_requests, 1):,.1f} "
              f"(input {tot_in / max(n_requests, 1):,.1f}, output {tot_out / max(n_requests, 1):,.1f})",
              f"- Estimated cost per request: ${tot_cost / max(n_requests, 1):.6f}",
              f"- Estimated total cost: ${tot_cost:.4f}", "",
              "## Calls by purpose", "",
              "| Model | Purpose | Calls |", "|---|---|---|"]
    for model, s in summary.items():
        for purpose, n in sorted(s["by_purpose"].items()):
            lines.append(f"| {model} | {purpose} | {n} |")
    lines += ["", "## Why the token bill is small", "",
              "- Request texts are deduplicated before classification and sent in batches of 20, so "
              "intent costs scale with distinct texts, not cases.",
              "- Each screenshot is transcribed once and cached; the deterministic reasoner consumes "
              "the structured transcription, never the image again.",
              "- Evidence parsing, identity resolution, state reconstruction, policy application and "
              "ordering are deterministic code with zero tokens.",
              "- The investigator agent is invoked only for cases whose attribution the deterministic "
              "matcher marks as contested.", ""]
    (EVAL_DIR / "usage_report.md").write_text("\n".join(lines), encoding="utf-8")


def write_run_trace(result, case_ids) -> None:
    lines = ["# Run trace", "",
             "Per-case audit trail from the last full run: resolved subject, intent verdict, and the "
             "state basis for every resource the plan touches.", ""]
    statuses = Counter(result.plans[c].status for c in case_ids)
    lines.append(f"Status distribution: {dict(statuses)}")
    lines.append("")
    from .pipeline import case_sort_key
    for cid in sorted(case_ids, key=case_sort_key):
        plan = result.plans[cid]
        intent = result.intents.get(cid)
        lines.append(f"## {cid} -> {plan.status} (subject {plan.user_id or '-'})")
        if intent:
            lines.append(f"- intent: {intent.request_type} via {intent.source}"
                         f"{' (rules disagree)' if intent.disagreement else ''}")
        for st in plan.resources:
            lines.append(f"- {st.system}/{st.resource_id} [{st.category}->{st.action}] present={st.present} "
                         f"direct={st.exposes_direct} ref={st.has_user_ref} flow={st.flow_enabled} "
                         f"restore={st.restore_allowed} ev={st.evidence} :: {st.basis}")
        if cid in result.problems:
            lines.append(f"- validation: {result.problems[cid]}")
        lines.append("")
    (EVAL_DIR / "run_trace.md").write_text("\n".join(lines), encoding="utf-8")

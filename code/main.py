"""Ghost Data Still Exists - deletion audit agent.

Usage (from the repository root):
    python3 code/main.py                 # full run -> ./output.csv
    python3 code/main.py --no-agent      # skip the Gemini investigator pass
    python3 code/main.py --offline       # no API calls (cached / rule fallbacks)

Writes:
    output.csv                              predictions for dataset/deletion_requests.csv
    code/evaluation/usage_report.md         token / cost summary of this run
    code/evaluation/run_trace.md            per-case audit trail (status, resources, basis)
"""
from __future__ import annotations

import argparse
import csv
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from agent.data import REPO_ROOT, read_csv  # noqa: E402
from agent.llm import GeminiClient  # noqa: E402
from agent.pipeline import case_sort_key, run, steps_json  # noqa: E402
from agent.report import write_run_trace, write_usage_report  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--no-agent", action="store_true", help="skip the Gemini investigator pass")
    parser.add_argument("--offline", action="store_true", help="never call the API")
    parser.add_argument("--output", default=str(REPO_ROOT / "output.csv"))
    args = parser.parse_args()

    started = time.time()
    client = GeminiClient()
    if args.offline:
        client.api_key = None
    if not client.available:
        print("[warn] GEMINI_API_KEY not set: using cached responses and rule fallbacks", file=sys.stderr)

    test_ids = {r["case_id"] for r in read_csv("deletion_requests.csv")}
    result = run(case_filter=None, use_agent=not args.no_agent, client=client)

    rows = []
    for case_id in sorted(test_ids, key=case_sort_key):
        plan = result.plans[case_id]
        rows.append({"case_id": case_id, "deletion_status": plan.status,
                     "steps_json": steps_json(plan)})
    with open(args.output, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["case_id", "deletion_status", "steps_json"])
        writer.writeheader()
        writer.writerows(rows)

    elapsed = time.time() - started
    problems = {k: v for k, v in result.problems.items() if k in test_ids}
    write_usage_report(result, n_requests=len(test_ids), elapsed=elapsed)
    write_run_trace(result, test_ids)

    counts = Counter(r["deletion_status"] for r in rows)
    print(f"wrote {len(rows)} rows to {args.output}: {dict(counts)}")
    print(f"validation issues: {sum(len(v) for v in problems.values())} in {len(problems)} cases")
    for case_id, issues in sorted(problems.items(), key=lambda kv: case_sort_key(kv[0]))[:15]:
        print(f"  {case_id}: {issues[:3]}")
    disagreements = [c for c, v in result.intents.items() if c in test_ids and v.disagreement]
    if disagreements:
        print(f"intent disagreements (gemini vs rules): {sorted(disagreements, key=case_sort_key)}")
    print(f"elapsed {elapsed:.1f}s; usage {result.client.summary()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Ghost Data Still Exists — Deletion Audit Agent

HackerRank Orchestrate, October 2026. For every request in `dataset/deletion_requests.csv`
the agent decides whether deletion was actually requested, reconstructs what every system
held at `audit_at`, applies `deletion_rules.csv`, and emits the ordered
FINDING → REMEDIATION → VERIFICATION plan in `output.csv`.

Challenge / submission: https://www.hackerrank.com/contests/hackerrank-orchestrate-october26/challenges/ghost-data-still-exists

## Run

Python 3.9+, no third-party packages except **PyMuPDF** (PDF text).

```bash
pip install pymupdf                      # if not already installed
echo "GEMINI_API_KEY=..." > .env         # repo root, never committed (see .gitignore)
python3 code/main.py                     # -> ./output.csv, code/evaluation/usage_report.md, run_trace.md
python3 code/evaluation/main.py          # -> code/evaluation/evaluation_report.md
```

Options: `--no-agent` (skip the investigator pass), `--offline` (no API calls; cached
responses and rule fallbacks). Models (free tier): vision `gemini-3.6-flash`
(`GEMINI_VISION_MODEL`), intent + investigator `gemini-3.5-flash-lite` (`GEMINI_TEXT_MODEL`),
each with a fallback model and a client-side per-minute throttle. Responses are cached in
`code/cache/` so reruns are deterministic and free; a fresh live run takes ~17 minutes
because of the free-tier rate limits.

## Architecture

```
 dataset/  ──► evidence.py  (SQL incl. replica tables, 5 JSON families, 7 log dialects joined
               by trace id, shift handover, PDFs)            ──► Observations + Scopes
 images    ──► vision.py    (Gemini vision transcribes admin screens to JSON; catalog aliases
               map rows to resource ids)                     ──► Observations
 requests  ──► intent.py    (Gemini, batched + deduped; multilingual rule cross-check)
                         │
                         ▼
             reasoner.py  (deterministic core)
               1. identity: current + historical emails, phones, hashes, user_id
               2. discovery: identifier links + data-catalog links, per request episode
               3. attribution: deletion-worker window (reported_at ± 2.5 h); unlinked records
                  matched globally on status fit, timing, evidence fit, job clock phase
               4. state at audit_at: latest observation by line time; citations only from files
                  captured ≤ audit_at; later full listings supersede primary (not replica) sightings
               5. policy.py: category → rule → findings / remediation / verification, sorted by
                  phase, operation order, system_id, resource_id
                         │
             investigator.py  Gemini function-calling agent (get_case, get_resource,
               search_evidence, submit_decision) reviews only exact ties; proposals pass the
               same structural validator or are rejected
                         │
             validate.py  contract checks on every row ──► output.csv
```

**Design principle: the model interprets, code decides.** Gemini does the three things that
need language or vision (intent in any language, reading screenshots, weighing tied
evidence). Everything that must be exact (dates, citations, policy, ordering, JSON
contract) is deterministic code that the LLM cannot override.

## Key decisions and trade-offs

- **Claims are not proof.** `reported_status` and activity `reported_result` are never used as
  state; they only help attribute an unlinked record to the right case.
- **Time discipline.** State uses the event time inside a file (a log exported after the
  audit can still show a lookup before it), but a step may only *cite* a file captured at or
  before `audit_at`.
- **Absence needs proof.** A record is absent if a lookup returned 404/NOT_FOUND or a
  complete listing of its system (inventory `snapshot_scope`, bundle collection) omits it.
- **Replica drift is the ghost.** A copy in a failover/regional/reporting replica keeps the
  record alive even after the primary is clean.
- **No fabrication.** Ids never seen in participant data are never invented, even where a
  naming pattern would guess right on the samples.
- **Cost.** Deterministic parsing means the LLM sees only distinct request texts, 11 images
  (once, cached) and a handful of tie groups. See `code/evaluation/usage_report.md`.

## Evaluation

`code/evaluation/evaluation_report.md` (generated): case status, step precision/recall/F1,
field-level and sequence accuracy on the 32 labelled samples, five custom adversarial cases,
and the failure → fix log. `code/evaluation/run_trace.md` explains every resource decision
for the 518 predictions.

## Layout

```
code/main.py                 entry point
code/agent/                  data, evidence, vision, intent, reasoner, policy, investigator,
                             llm (Gemini REST client), validate, report, pipeline
code/evaluation/main.py      evaluation harness
code/evaluation/*.md         evaluation_report, usage_report, run_trace, notes
code/cache/                  cached Gemini responses (safe to delete)
```

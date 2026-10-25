# AI Judge Interview Prep (not part of code.zip)

30-minute voice interview, camera on. It opens with: "Give me a quick 2-minute pitch of what you
built and the problem it solves." Then it probes architecture, problem understanding, trade-offs,
evaluation, and how you used AI. Speak in "I decided / I rejected / I measured".

## 2-minute pitch (read it aloud twice; ~280 words)

**Problem (20s).** Northstar's deletion workflow said "Complete" while personal data survived in
replicas, search indexes, support tickets, analytics, exports and backups, and sync jobs brought it
back. I built an audit agent that, for each of 518 requests, decides whether deletion was even
requested, reconstructs what every system held at the audit time, and outputs COMPLETE,
INCOMPLETE or NOT_APPLICABLE with an ordered, evidence-cited remediation and verification plan.

**Architecture (40s).** My core principle: *the model interprets, code decides.* Evidence comes in
five formats, so I normalise everything into one "observation" shape: which record, in which
system, at what time, present or absent, and with which identifiers. Gemini does the three things
that need language or vision: classifying request intent in any language, transcribing the admin
screenshots, and a tool-using investigator agent that reviews attributions where every
deterministic signal ties. Everything that must be exact is deterministic code the LLM can't
override: time cut-offs, which file may be cited, the deletion policy, step ordering and the JSON
contract.

**Evaluation (30s).** On the 32 labelled samples I get every status right and an exact step
sequence on 29. The other three reference ids that appear nowhere in the dataset, and I chose not
to fabricate them. I also wrote five adversarial cases (negated requests, historical emails,
audit-time cut-off, an unseen language, a replica ghost), and all five pass.

**Trade-offs (30s).** I don't trust the workflow's reported statuses or the activity results;
they're only used to attribute anonymous records to the right case. A record surviving only in a
failover replica still counts as remaining, because that's the ghost in the brief. And I
deliberately kept the LLM out of the policy path. That makes the system auditable and cheap: the
whole run costs fractions of a cent per request.

## Likely questions and crisp answers

**Why not let the LLM read everything and answer?** 94 files, 4,000 activity rows, strict ordering
and citation rules. An LLM would be slow, costly, and non-deterministic on exactly the parts graded
most strictly. I use it where it adds signal (language, vision, tie review) and validate its outputs.

**How do you resolve identity?** Current snapshot plus every historical email, phone and hash from
the audit log. 100 of the 518 requests use an old email. Matching is exact and case-insensitive,
because decoys like `g.silva76.jr@gmail.com` exist.

**How do you decide state at audit time?** I take the latest observation whose event time is at or
before `audit_at`. A log exported after the audit can still contain a lookup from before it. But a
step may only cite a file captured at or before the audit time. Absence needs proof: a 404 or
NOT_FOUND, or a complete listing of the system that omits the record.

**Hardest problem?** Deleted accounts and anonymized analytics carry no identifier. They're tied
to a case only by the deletion worker's activity within ±2.5h of `reported_at`, and many cases
report at the same minute. I built a global greedy matcher that scores four signals:
1. whether the worker's result fits the reported status;
2. deletion timing;
3. evidence fit (a record with proof goes to a case that will verify COMPLETE);
4. job clock phase.
For the last one: one deletion job's follow-up operations land at fixed seconds-of-minute offsets
after its own account deletion. That cut ambiguous ties from 129 to 53. The rest go to the Gemini
investigator, and its proposals must pass the same structural validator.

**Is the clock-phase signal overfitting?** It's measured on the samples and applied only as a
tie-breaker after the semantic signals. In real systems, operations issued by one job share that
job's scheduling cadence. I'd monitor it in production and drop it if it stopped holding.

**Policy decisions?** `deletion_rules.csv` is read at runtime. The category comes from system plus
record shape. A support attachment is deleted, while a conversation with shared context is
redacted. An analytics record with marketing opt-in is deleted as a marketing profile. A tombstone
keeps `user_id` and loses name, email, phone and hash. Backups and security logs are retained, but
restore is blocked and presence is verified.

**Ordering?** Findings, then remediation, then verification. Within a phase I follow the table's
operation order, then system and resource. Remediation disables flows and blocks restores before
deleting, so nothing gets recreated mid-fix.

**How did you use AI to build it?** Claude Code was the pair-programmer and every turn is in
log.txt. I directed the analysis myself: I reverse-engineered the evidence model from the samples,
rejected approaches that regressed (the legal-register inference, scope absence overriding replica
copies), and kept a failure→fix table in the evaluation report.

**What would you do with more time?** A labelled set beyond 32 samples, built by perturbing the
generator's patterns. Confidence scores per step. A production feedback loop where
re-verification after remediation becomes training data for the tie-breaker.

**Failure modes / limitations?** Residual tie attribution; categories for unseen record types;
model quotas (handled with throttling, fallbacks and caching); hidden-set ids that don't exist in
participant data.

## Numbers to remember

- 518 requests → 355 INCOMPLETE, 153 COMPLETE, 10 NOT_APPLICABLE; 0 contract violations
- Samples: 32/32 status, 29/32 exact sequence, step F1 99.2%, resource precision 100%, recall 97.3%,
  citation accuracy 100%
- Custom cases: 5/5 pass (negation, historical email, audit cut-off, German, replica ghost)
- Ties: 129 → 53 after job-phase signal; investigator reviewed 42 tie groups and agreed with the
  matcher in all of them (0 changed picks), which is good corroboration and also an honest limit
- Models: gemini-3.6-flash (vision, 11 calls), gemini-3.5-flash-lite (20 intent batches +
  119 investigator turns); 263,857 tokens, est. $0.13 total, $0.00025/request (free tier: $0 actual)
- A real bug I caught from the eval: Gemini first called "verify my account was deleted" a
  non-deletion request. That knocked 3 cases out and cascaded into 2 more wrong attributions.
  Fixed with an explicit prompt rule, and a regression check now reports any rule/LLM disagreement.
- Why vision is 3.6 not 3.8: 3.8 timed out twice in the smoke test; the fallback chain caught it.

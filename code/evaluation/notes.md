## Failures found and improvements made

Each row was found by running the harness against the 32 labelled samples (or by
sanity checks on the unlabelled 518), diagnosed from the run trace, and fixed in
code. The metric column is sample-set exact-sequence accuracy before -> after.

| # | Failure found | Root cause | Fix | Effect |
|---|---|---|---|---|
| 1 | First end-to-end run: 15/32 exact sequences | Anonymized analytics and redacted support rows were read from log lines that carry no `rows=` field, so their state was "unknown" and a scope snapshot wrongly declared them absent (case_03, case_18) | A completed read that returns a record body counts as presence | 15 -> 20 |
| 2 | Legal holds added to 6 samples that have none | Parser invented `legal_hold_<n>` ids from order numbers in the disputed-orders register PDF | Removed the derivation; only ids that appear in evidence are used | 20 -> 22 |
| 3 | `object_19` / `tombstone_17` attached to the September requests of user_07 / user_17 | Same subject filed earlier requests (Feb/Mar) and those artifacts belong to the earlier episode | Episode bounds: a request owns evidence observed after the previous request's audit and up to its own | 22 -> 24 |
| 4 | Wrong account picked when several cases report at the same minute (case_28/29, case_23, case_30 vs case_04) | Unlinked deleted accounts were handed out by subject order | Global greedy matching with a status fit (worker result vs reported claim), deletion timing fit, evidence fit (records with proof go to cases that will verify COMPLETE), then **job clock phase**: follow-up operations of one deletion job land at fixed seconds-of-minute bands after that job's account deletion | 24 -> 29; contested ties on the 518 set 129 -> 53 |
| 5 | case_126 family ("an old report says my account still exists") stayed INCOMPLETE | The newest explicit sighting was an older primary snapshot; a later full inventory omits the record | A later complete listing of the system supersedes an older sighting... | fixed family |
| 6 | ...which broke case_05 (replica ghost) | The failover replica is not covered by the primary inventory | ...except for sightings in replica copies (replica drift is exactly the ghost the brief describes) | 29 kept |
| 7 | Alias `user_17` substring-matched the legal register PDF and attached a tombstone to 6 subjects | Catalog aliases used verbatim for document search | Documents use only distinctive aliases (file names, statement numbers); exact screenshot labels may use reference aliases | 23 -> 29 in the pipeline run |
| 8 | Rule intent check rejected 18 genuine deletion requests ("eliminación", "remove any remaining copy", "the profile is gone") | Keyword lists cannot cover paraphrase, languages and negation | Gemini decides intent; rules stay only as a cross-check / offline fallback and every disagreement is reported | 0 disagreements left on rules after tightening |

### Known limitations

- Three sample steps reference ids that do not occur anywhere in the participant data
  (`account_004`, `audit_record_6645`, `audit_record_5569`). We deliberately do not
  fabricate ids from naming patterns, so these stay misses (the 3 non-exact samples).
- Remaining contested attributions (exact ties on every evidence signal) are resolved by the
  investigator agent when an API key is available, otherwise by evidence-listing order
  aligned with subject order. These are the most likely residual errors on the hidden set.
- Policy categories are inferred from system + record shape (attachment, contact index,
  marketing opt-in markers). A new record type with no such cue falls back to its
  system's default category.

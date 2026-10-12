# KOMODO concentration review, pending paths 1500-1999

This bounded batch is part of the unfinished all-record objective. The frozen
[plan](plan.json) covers 500 exact tracked normalized paths: 86 base accessions
and 414 strain/variant accessions. All 500 have [per-record results](records),
including 494 unchanged records. The six applied changes add 25
ingredient concentration entries and six separate identity-mapping entries,
twelve references and six curation events. They do not change quantities,
units, ingredient identities, stocks, variants, stable IDs or growth claims.
The [applied independent audit](diff-audit.json) verifies full-record inversion,
exact source snippets and unchanged formulation; readback and a zero-change
second apply also pass. All 23 checks in [validation.json](validation.json) are
terminal: eighteen pass, two are unavailable and three merge gates fail.
Unavailable or failed checks are not claimed as passes.

The [source captures](source-captures.json) pin 88 mapped endpoints, including
seven actual HTTP 404 responses affecting eight paths. All eight preliminary
candidate records and their complete API payloads are preserved in
[the context snapshot](inspected-candidate-context.json). The original DSMZ
recipe PDFs were independently retrieved, hashed and inspected for all eight;
their [cross-checks](original-source-crosschecks.json) retain extracted text and
source metadata. Copyright years are not invented publication years.

Two [source-pinned withholdings](withholdings.json) veto fifteen preliminary
endorsements for omitted stock/preparation stages. The final plan has 12,038
conflict rows and 16,978 unsupported rows. These include stock, source-only and
variant context, not just independent concentration facts. Its
[findings](preparation-findings.md) explain the exact unresolved scope, including
the separately inspected KOMODO 457_7098 variant page. Available variant sources
are not classified as absent merely because a base-recipe review cannot use them.
The [prior-cohort handoff](prior-cohort-handoff.json) identifies two earlier
DSMZ copies with fifteen existing entries requiring preparation-scope review;
no earlier plan or historical result is rewritten.

All four [baseline checks](baseline.json) pass, including strict validation of
15,910 records, representative schema validation, independent full-record
inversion and 165 focused pre-apply tests. Preview presentation is insertion-only:
910 lines added, no removed lines or replacement blocks. The
[independent preflight](preflight.json) confirms quantities and formulation are
unchanged. This does not imply every pre-existing field is correct.

Post-apply focused tests pass **246 on isolated Python 3.11** and **169 on
cached Python 3.13**, with no errors, failures or skips. Strict validation,
representative schema validation, IDs, variant links, prior medium/solution/
KOMODO readbacks and cumulative semantic diff pass. Product/reference checks
are unavailable because `oaklib` and `linkml-reference-validator` are missing.
These are local focused checks, not full-project-environment, full-suite or CI
passes. Exact-path coverage, Ruff, Black and `git diff --check` also pass.

The [actual-group retention audit](merge-retention.json) checks six records in
six current groups. All 25 complete ingredient evidence entries and all 25
amount/reference/snippet/field-scope matches survive. Five records retain all
checked provenance, but KOMODO 464 loses its complete mapping evidence,
bibliographic additions and curation event. These overlapping failures affect
one record and fail the gate despite retained ingredient quotations. The
authoritative normalized YAML retains every addition. Group membership alone
does not establish exact formulation equivalence, and no generated merge is
published to bypass the failure.

Global merge verification fails with 1,247 name conflicts and 3,287 fingerprint
issues. The [freshness comparison](merge-freshness.json) also fails: 6,320 tracked
outputs versus 6,493 temporary outputs, with 3,719 only tracked, 3,892 only fresh,
1,667 changed and 934 unchanged. All 6,493 identified groups were written;
the pipeline excludes 4,785 standalone solutions and skips 342 other inputs,
so this is not proof every normalized record participated. No tracked merged
output changed.

The edits remain local. No commit, PR, issue closure, merge or branch deletion
is claimed, and no generated merge is hand-edited or published.

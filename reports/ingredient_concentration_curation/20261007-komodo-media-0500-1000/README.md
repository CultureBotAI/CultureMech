# KOMODO concentration review, pending paths 500-999

This is another bounded batch within the unfinished all-record objective.
The frozen [plan](plan.json) covers 500 exact normalized paths, including 122
base accessions and 378 variant accessions. The independent
[post-apply audit](diff-audit.json) verifies 24 evidence-only edits: 141 ingredient
concentration entries, 24 separate identity-mapping entries, 48 references and
24 appended curation events. No quantity, unit, ingredient identity, stock,
variant, growth claim or prior history is changed. All 500 paths have
[per-record results](records), including 476 unchanged records. The
[preflight](preflight.json), guarded readback and zero-change rerun pass; the
first KOMODO batch also passes its source/hash/snippet readback unchanged.

All 27 preliminary candidates and complete source responses were inspected.
Three [source-pinned withholdings](withholdings.json) prevent endorsing
preparation/variant/pH conflicts in 111, 125 and 187. The
[preparation findings](preparation-findings.md) document the accepted scope,
unresolved ingredient details and nine unavailable endpoints affecting eleven
paths. Those source-access gaps are unchanged unsupported results, not invented
amount evidence. The [prior-cohort handoff](prior-cohort-followup.md) explicitly
reopens scientific preparation questions in three earlier DSMZ source records.

The [actual-group retention audit](merge-retention.json) fails for eight distinct
records; sixteen pass every checked field. Of 141 concentration claims, 131
retain the exact amount/reference/snippet/field-scope match and 120 retain the
full evidence entry. Three records lose amount quotes, five lose full entries,
and six each lose mapping evidence, references or curation events; these sets
overlap. All additions remain intact in authoritative normalized YAML. No
evidence is copied across unverified formulations to force this check to pass.

All three baseline and seventeen post-apply jobs in [validation.json](validation.json)
are terminal. The 910 focused tests pass with no errors, failures or skips.
Full strict validation passes all 15,910 normalized records; the representative
schema check, canonical IDs, guarded apply/readback/no-op, previous-batch
readback, independent full-record inversion, semantic diff, coverage and
`git diff --check` pass. Black and Ruff checks of the seven relevant Python
files also pass. Product and automated reference validation remain unavailable
because `oaklib` and `linkml-reference-validator` are missing.

Global merge verification fails with 1,247 name conflicts and 3,287 fingerprint
issues. [Freshness](merge-freshness.json) also fails: 6,320 tracked and 6,492 fresh
records, with 3,719 only tracked, 3,891 only fresh, 1,657 changed and 944 unchanged.
Together with the retention failure, these results prevent a publication-ready
claim. Validation uses isolated Python 3.11, not maintained Python 3.13 or CI;
the full repository suite was not rerun. No generated merged record is hand-edited
or published, and no commit, PR or merge is claimed for this batch.

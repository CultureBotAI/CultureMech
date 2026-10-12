# Hajjaj-Family Ingredient Curation

Applied locally to twenty exact normalized paths. This batch is not complete
scientific verification of these formulations or completion of the all-record
goal. The [plan](plan.json), [source ledger](source-review.json) and twenty
[per-record reports](records/) preserve exact before/after fields and evidence.

## Applied Changes

- 37 nutrient amounts restored to the primary paper's directly stated g/L units.
  No molecular-weight calculation or assumed final volume is used. This does
  not assert that the prior database conversions were numerically wrong.
- 90 primary chemical identifiers and 54 existing MIM links corrected to five
  independently verified hydrate identities; 137 ingredient labels corrected.
- 57 unsupported identity slots removed without invented replacements: twenty
  orthomolybdate mappings, eighteen copper mappings, eighteen glutamate mappings
  and one unsupported isoleucine stereochemical assignment.
- 535 scoped evidence entries, 150 bibliographic references, 243 ingredient
  context notes and twenty append-only curation events added. No permanent
  record IDs, organism claims, preparation, category/path or role claims changed.

The [primary paper](https://doi.org/10.1128/AEM.67.6.2596-2602.2001) supports the
eighteen explicitly source-linked records. MediaDB 330 and 331 receive only
their own database/SQL evidence and molybdate identity correction; no DOI or
unverified paper association is assigned to them. Source provenance includes
title, authors, available year, discovery mode, source type and access date.

The [independent source recheck](source-recheck.json) reparses all 243 database
rows from the hash-pinned official HTML and SQL export. Paper and ChEBI readings
are manual; there is no fabricated raw full-text capture or automatic-reference
pass. The [issue ledger](issues.md) retains unresolved source and identity gaps.

## Validation And Coverage

[Preview](preview.json): all eighty baseline/proposed schema and strict
commands, 254 adversarial tests, Ruff, Black and diff checks pass. The first
preview's concentration-only guard failure was fixed without changing unresolved
amount statuses; no recipe was written by the failed preview.

[Application](apply.json): twenty records changed, readback verified, and repeat
application is a no-op. The inventory proves that no other normalized path
changed. Fourteen regenerated indexes are semantically identical and are not
rewritten. All twenty formulations remain distinct and preserve the curated
content through runtime merging.

[Cumulative audit](cumulative-audit.json): **5,402 edited records, 37,914 new
evidence entries and 1,788 quantity corrections**. [Follow-up coverage](followup-coverage.json)
is **11,930 / 15,910**, with **3,980 outside coverage**. The 206 retained amounts
in this batch remain database assertions, not primary-verified final molarities.

All forty post-edit schema/strict commands and 382 regression tests pass.
The initial twenty reference commands abort on sandbox DNS without per-claim
results. The network-enabled rerun returns all twenty result sets: 316 snippets
and 130 titles pass; 219 snippets and twenty titles fail. Abstract-only article
fetches and generic SQL matching do not certify the independently inspected
full-text evidence.

Corpus strict, ID, product and MIM-index checks pass. Global merge verification
and freshness fail with 1,247 name conflicts, 3,287 fingerprint issues and 15,056
derivation differences. The [applied checkpoint](applied-checkpoint.json)
verifies all completed receipts, source captures, code and normalized-record
hashes. The fresh fast tier completes with **15,409 passed, sixteen skipped,
3,498 deselected and two dependency warnings** in 34:30. The
[terminal checkpoint](validation.json) pins the unchanged tested code and all
15,910 normalized-record hashes. This is not a full-suite pass, and the failed
reference and merge gates still prevent an all-gates claim. Nothing is committed,
merged or publication-ready. The full corpus objective remains active.

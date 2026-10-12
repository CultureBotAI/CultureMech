# DSMZ Albumin Preparations

Applied locally to DSMZ and KOMODO 403 and 751. This batch adds 114 evidence
entries, eight source references and four append-only curation events. It does
not add taxa-media associations or complete the all-record goal.

## Scientific Changes

- Restore the source-specific albumin preparations in all four records, removing
  only the three false LB constituents in each. Genuine tryptone and yeastolate
  in DSMZ 403 are preserved, along with existing chemical annotations.
- Reconstruct DSMZ 403's A-D preparation boundaries, including its separate
  900/200/143 ml water inputs, 100 ml CMRL product input and 86 ml inactivated
  rabbit serum. The source's alternative commercial products are alternatives,
  not additional ingredients. API-declared stock g/L values are retained only
  at stock scope, explicitly not independent final-volume measurements.
- Preserve the exact 50.05 g albumin fraction V batch input, Solution B's
  115 C/15 minute preparation and Solution A's 5 M NaOH titrant strength. No
  titrant dose is guessed. KOMODO 403's global pH 7.6 assertion is withdrawn;
  it is supported only for Solution A before the preparations are combined.
- Restore DSMZ 751's four stock doses: 15 ml hemin, 10 ml albumin, 5 ml glucose
  and 10 ml cysteine. Percentage bases remain unspecified, and the hemin
  solvent's 0.05 N is not converted to molarity. The cysteine is free base.
- Keep the three post-autoclave stocks separate from basal hemin. Move the
  liquid SC option into an evidence-backed inline variant, retaining all three
  changes together: omit corn-meal agar, KH2PO4 1.5 g and K2HPO4 0.5 g per batch.
  The solid base and existing reciprocal source-duplicate links are preserved.

The independent audit accounts for all 57 previous quantity fields, 62 source
rows and 187 field claims. It records 28 unsupported quantity withdrawals,
23 stock-scope rebases, four liquid-dose corrections, two water corrections,
23 new numeric fields and 35 relocated existing nodes. No final-medium volume
is inferred from water or summed liquid doses. Existing groundings, including
the corn-meal agar and legacy HEPES mappings, are not automatically recertified.

## Evidence And Validation

The two API responses and two original PDF binaries were refreshed and match
the inspected captures byte-for-byte. The PDFs were extracted with pypdf and
their page images inspected for table alignment, decimals and degree symbols.
Literal extracted snippets and source hashes are attached in YAML. Authors and
publication years remain unknown; the printed copyright year is not substituted.

All 126 dedicated reconstruction, mutation and write-guard tests pass. Baseline
and applied schema/strict, independent audit, readback and no-op checks pass.
The focused regression selection passes 459 tests; lint/format checks pass after
removing one unused loop variable. The initial lint failure remains in `final.json`
and the successful retry in `final-retry.json`. The fast tier passes 9,300 tests
(16 skipped). Strict schema and serial ID checks pass for all 15,910 normalized
records. Product validation passes with 91 warnings and 96,073 no-adapter skips;
chemical mappings are not comprehensively recertified. These checks use the
existing partial locked Python 3.13 environment, not a clean CI installation or
the complete test suite. All intended checks are terminal in the
[validation receipt](validation.json), including the failing gates below.

The DSMZ/KOMODO SC pair agrees exactly across eight formulation/evidence fields;
its reciprocal source-duplicate links are verified in
[`paired-formulations.json`](paired-formulations.json).

Variant links pass. Global merge verification still fails with 1,247 name
conflicts and 3,287 fingerprint issues. Freshness fails with 4,275 tracked-only,
8,732 fresh-only and 2,045 changed shared paths. Runtime routing produces 10,777
groups from 15,910 inputs; the four repaired targets retain their claims in
separate schema-valid groups. No tracked merged YAML was written. Five generated
metadata artifacts were refreshed, including the expected root-only hierarchy
count change from relocating two preserved HEPES annotations into stocks.

At the original batch validation, **58 of 122 checks passed**, while
60 PDF snippet checks and four PDF-title checks fail. The installed generic URL
fetcher cached binary PDF content as text instead of extracting the recipe.
The failed excerpts were manually verified against the exact captured text and
page images. This does not turn the automated failures into passes; see the
[local issue draft](issue-pdf-reference-extraction.md).

The subsequent [PDF validator repair](../20261008-recipe-pdf-validation/README.md)
now passes all 122 checks against these unchanged records. Its
[reference receipt](../20261008-recipe-pdf-validation/references-final.json) supersedes
only the earlier PDF-reference failures, not the still-failing global gates.
The original `validation.json` remains unchanged as the historical result.

All four targets already have canonical follow-up reports. `records/` contains
supplements using `- Follow-up target:`, not duplicate canonical `- Record:`
entries. Report presence is not evidence that all concentration claims are solved.
The all-record review, global merge/freshness failures and publication remain open.

## Artifacts

- `context.json`, `plan.json`: frozen baselines, source captures and exact decisions.
- `application.json`, `applied-audit.json`: actual writes, readback and full-field audit.
- `live.json`: refreshed hashes and the passing/failing automated reference results.
- `baseline.json`, `final.json`, `final-retry.json`, `post.json`, `fast.json`,
  `corpus.json`: individual check receipts, including retained initial failures.
- [`validation.json`](validation.json): consolidated terminal results and pinned
  artifact/code hashes; publication and all-record completion remain false.
- [`paired-formulations.json`](paired-formulations.json): exact SC formulation
  agreement and reciprocal source-duplicate link checks.
- `records/`, `adversarial-review.md`, `next-work.md`: decisions and remaining scope.

No GitHub issue, PR, commit, push, merge or branch deletion was performed in this batch.

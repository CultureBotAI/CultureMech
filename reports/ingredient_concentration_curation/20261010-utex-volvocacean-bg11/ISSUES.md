# Local Review Issues

These are local review dispositions, not GitHub issues. Publication operations
were previously denied and have not been retried.

## Resolved In This Batch

- P1: Both salt variants encoded a separately measured 1000 mL/L prepared BG-11
  dose, although the source stops base preparation at step one and adds salt
  before final makeup. Removed the unsupported dose, retained the base link,
  and documented the table/procedure distinction with source evidence.
- P1: Volvocacean omitted the requirement to prepare Waris without pH adjustment
  and omitted the subsequent autoclaving step. Restored the source-specific
  sequence without inventing pH, temperature or duration.
- P2: The records lacked concentration evidence and optional agar formulations.
  Added eight source-URL/snippet evidence entries and three separately scoped
  variants. Four supported structured quantities retain their values and units.
- P2: Existing NaCl notes implied exact mass/molar equivalence. They now identify
  the two printed quantities as source assertions, not a new exact conversion.
- P2: Adversarial review of the first proposal found a batch-generic history note
  incorrectly mentioning dose removal for Volvocacean, and an obsolete carried
  finding that agar was absent. The unapplied `plan.json` remains archived;
  `plan-v2.json` corrects both, with regression assertions. No prior history was
  rewritten.
- P3: Proposal construction initially stopped on an excerpt boundary and a
  dictionary-only update helper used for a list entry. Both stopped before
  normalized writes. The schema enum was corrected to
  `PHYSICAL_STATE_VARIANT`. The first integration preview then passed tests but
  failed Ruff; `preview.json` preserves that result. `preview-v2.json` includes
  the formatting/import/closure fixes and passes tests, Ruff and Black.

## Unresolved Scientific Scope

- P1: Each salt variant's agar procedure requires sterile sodium thiosulfate but
  gives no local dose. The linked base recipe has a dose, but formulation-specific
  inheritance has not been established. No number or zero was inserted.
- P2: The 0.36% source title says BG-11-1 while its linked base/table says BG-11.
  No nitrogen omission, permanent-identity change, rename or merger is inferred.
- Linked parent compositions, chemical/supplier mappings, salinity, ingredient
  roles, growth and general culture conditions are not certified by this batch.
  Optional agar additions are batch amounts, not measured final-volume claims.

## Validation And Publication

All three sandbox reference commands stopped on DNS failures before validation.
The separately authorized read-only fresh-network run passes all three commands
and eleven title/excerpt checks; see `references-live.json`. No reference
validator implementation, title or snippet was weakened to obtain that result.

Corpus strict schema, permanent IDs and product labels pass. Merge verification
and freshness fail; the fresh comparison reports 15,056 differences (2,045
changed, 4,275 tracked-only, 8,736 fresh-only). Equality with the preceding
checkpoint's counts is not proof of equal contents. Volvocacean also remains
excluded by the ingredient-based matcher before and after this curation; this
batch does not expand referenced parents to force a fingerprint.

Final results belong to `post.json`, `references.json`, `consumers.json`,
`corpus.json`, `cumulative.json`, and the terminal checkpoint. A passing
orchestration receipt does not imply all optional corpus/reference gates pass.
The broader strict UTEX parser remains uninstalled. Earlier full-suite runtime,
reference-title and merge-freshness issues remain tracked in the
[preceding checkpoint](../20261010-next-utex-applied/ISSUES.md). This batch does
not claim a new full-suite pass, installed-wheel change, browser screenshot,
complete scientific corpus review, or GitHub publication.

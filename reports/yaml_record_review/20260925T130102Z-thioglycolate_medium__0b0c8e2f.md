# YAML Record Review: thioglycolate_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thioglycolate_medium__0b0c8e2f.yaml
- Started UTC: 2026-09-25T13:01:50Z
- Finished UTC: 2026-09-25T13:02:14Z
- Verdict: needs curation

## Target

- Generated YAML for the TOGO M1607 Thioglycolate Medium import derived from NBRC_M807.
- The record was merged from `TOGO_M1607_Thioglycolate_Medium`.
- The checked sources were TOGO M1607 and the NBRC 807 medium page.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to TOGO M1607, a Thioglycolate Medium snapshot of NBRC_M807.
- The NBRC 807 page lists Thioglycolate Medium and pH 7.0 to 7.2.
- No conflicting duplicate merge was observed.

## Evidence

- NBRC 807 lists 15 g Hipolypepton, 5 g yeast extract, 5 g glucose, 2.5 g NaCl, 0.5 g L-cystine, 0.5 g sodium thioglycolate, 1 mg resazurin, 1 L distilled water, optional 15 g agar, and pH 7.0 to 7.2.
- TOGO M1607 preserves the same composition and pH range.
- `Hipolypepton` is a main NBRC ingredient rather than a nested solution.

## Completeness

- Most NBRC ingredients are present.
- `Hipolypepton` was migrated into an empty `solutions` entry named `Unknown solution`.
- The 1 mg resazurin source amount is stored as 1 g/L.
- The 1 L distilled-water row is stored as 1 g/L water.
- The NBRC pH range is missing.

## Findings

- TOGO volume and mass units were imported as g/L without conversion, producing a 1000-fold resazurin error and a false 1 g/L water concentration.
- `Hipolypepton` was removed from the ingredient list and converted to a structurally empty solution.
- The pH 7.0 to 7.2 range from both TOGO and NBRC is omitted.

## Recommended Edits

- Restore `Hipolypepton` as a 15 g/L main ingredient.
- Convert 1 mg resazurin to 0.001 g/L or preserve it as a 1 mg per liter source amount.
- Preserve 1 L distilled water as volume, not a g/L concentration.
- Add the pH 7.0 to 7.2 source range.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify TOGO L and mg units are converted rather than copied into `G_PER_L`.
- Confirm whether optional agar should be modeled as a solid variant or an optional ingredient.

## Additional Notes

- None found.

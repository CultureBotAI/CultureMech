# YAML Record Review: THERMOCLOSTRIDIUM A-G MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoclostridium_a_g_medium__441f8294.yaml
- Started UTC: 2026-09-25T11:52:30Z
- Finished UTC: 2026-09-25T11:55:05Z
- Verdict: needs curation

## Target

- Generated YAML for DSMZ Medium 326, THERMOCLOSTRIDIUM A-G MEDIUM.
- The record was merged from `clostridium_thermolacticum_medium`, `clostridium_thermolacticum_medium_replace_cellobiose_with_sucrose`, and `thermoclostridium_a_g_medium`.
- The checked sources were the normalized DSMZ 326 and KOMODO 326 records, MediaDive 326, and DSMZ Medium 326.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to DSMZ/MediaDive Medium 326.
- The KOMODO 326 records reference DSMZ Medium 326 through `mediadive.medium:326`.
- The `clostridium_thermolacticum_medium_replace_cellobiose_with_sucrose` child should be rechecked after stock handling is corrected because its name suggests a source-specific carbon-substrate variant.

## Evidence

- DSMZ 326 lists a main recipe with 1 ml Trace element solution SL-10, 1 ml Wolin's vitamin solution (10x), and 1000 ml Distilled water.
- Trace element solution SL-10 is a 1 L stock added at 1 ml/L.
- Wolin's vitamin solution (10x) is a 1 L stock added at 1 ml/L.
- DSMZ 326 gives pH 6.8-7.2 and an 80% N2 plus 20% CO2 anaerobic preparation.

## Completeness

- The 6.8-7.2 pH range is present.
- DSMZ preparation steps for the main recipe and Trace element solution SL-10 are present.
- The 1000 ml main water row is missing.
- Trace element solution SL-10 and Wolin's vitamin solution (10x) are flattened at undiluted stock strength.

## Findings

- Trace element solution SL-10 was expanded at full 1 L stock strength instead of as a 1 ml/L addition.
- Wolin's vitamin solution (10x) was expanded at full 1 L stock strength instead of as a 1 ml/L addition.
- Main-medium CoCl2 x 6 H2O was summed with a separate Trace element solution CoCl2 x 6 H2O row before source-scope dilution was applied.
- The 10 ml 25% HCl row from Trace element solution SL-10 was converted to a top-level 2.5 G_PER_L HCl ingredient.
- The 1000 ml main distilled-water row is missing.

## Recommended Edits

- Regenerate DSMZ 326 with Trace element solution SL-10 and Wolin's vitamin solution (10x) retained as stock additions, or expand them only after applying the 1 ml/L and 1 ml/L dilution factors.
- Keep duplicate ingredient names in separate recipe scopes until stock dilution is applied so CoCl2 x 6 H2O is not over-summed.
- Preserve 25% HCl as a Trace element solution volume rather than converting it to a top-level HCl mass concentration.
- Preserve the main 1000 ml distilled-water row.
- Recheck the KOMODO replacement child after regeneration and link it as a variant if the original source differs by carbon substrate.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that corrected DSMZ 326 no longer carries undiluted SL-10 or Wolin vitamin rows in the main ingredient list.

## Additional Notes

- None found.

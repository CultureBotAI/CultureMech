# YAML Record Review: thermosyntropha_medium__dc6c5aa3

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermosyntropha_medium__dc6c5aa3.yaml
- Started UTC: 2026-09-25T10:52:13Z
- Finished UTC: 2026-09-25T10:52:17Z
- Verdict: needs curation

## Target

- Generated YAML for DSMZ Medium 731, THERMOSYNTROPHA MEDIUM.
- The record was merged from `thermosyntropha_medium`.
- The main checked sources were DSMZ Medium 731 and MediaDive REST entry 731.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 after the startup line only and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The direct record is correctly identified as DSMZ Medium 731.
- pH 8.5 and the DSMZ anoxic preparation text are present.
- The record's duplicated NaCl and CaCl2 rows were already summed by data-quality cleanup, hiding the fact that part of each amount came from a 10 ml/L Modified Wolin's mineral solution stock.

## Evidence

- DSMZ/MediaDive 731 lists 1000 ml water plus 0.3 g K2HPO4, 0.3 g KCl, 0.5 g NaCl, 1 g NH4Cl, 0.3 g MgCl2 x 6 H2O, 0.05 g CaCl2 x 2 H2O, 10 ml Modified Wolin's mineral solution, 10 g yeast extract, 0.5 ml sodium resazurin solution, 3 g NaHCO3, 3 g Na2CO3, 1 ml Wolin's vitamin solution, 0.15 g L-Cysteine HCl x H2O, and 0.5 g Na2S x 9 H2O.
- Modified Wolin's mineral solution and Wolin's vitamin solution are DSMZ stock recipes, not final-medium top-level ingredients.
- A KOMODO DSMZ 731 duplicate exists as `THERMOSYNTROPHA_MEDIUM`.

## Completeness

- The generated record omits the 1000 ml distilled-water row.
- Modified Wolin's mineral solution is expanded at stock strength; 1 ml of Wolin's vitamin solution is also expanded as full stock vitamins.
- The direct DSMZ pH and main preparation step are retained.

## Findings

- The formula has blocking stock-solution flattening. The 10 ml/L Modified Wolin's mineral addition was expanded as full-strength stock rows and then summed into main NaCl and CaCl2, producing 1.49456 g/L NaCl and 0.149456 g/L CaCl2 where the DSMZ main recipe lists 0.5 g and 0.05 g plus a separate stock addition.
- The 1 ml/L Wolin's vitamin addition was expanded into gram-per-liter vitamin rows even though those rows are the stock solution recipe.
- The missing water row and KOMODO DSMZ 731 duplicate should be resolved together with the stock modeling fix.

## Recommended Edits

- Regenerate DSMZ 731 with Modified Wolin's mineral solution and Wolin's vitamin solution represented as 10 ml/L and 1 ml/L additions, or with correctly diluted stock expansions.
- Stop summing main-medium NaCl/CaCl2 with Modified Wolin stock NaCl/CaCl2 at the top level.
- Merge or retire the KOMODO DSMZ 731 duplicate after the direct DSMZ 731 record is repaired.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare the regenerated formula against the DSMZ 731 PDF and verify that only the main-medium rows remain top-level unless stock rows are explicitly diluted.

## Additional Notes

- None found.

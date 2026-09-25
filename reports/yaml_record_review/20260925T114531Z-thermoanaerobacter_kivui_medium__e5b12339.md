# YAML Record Review: THERMOANAEROBACTER KIVUI MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoanaerobacter_kivui_medium__e5b12339.yaml
- Started UTC: 2026-09-25T11:42:04Z
- Finished UTC: 2026-09-25T11:45:31Z
- Verdict: needs curation

## Target

- Generated YAML for DSMZ Medium 171, THERMOANAEROBACTER KIVUI MEDIUM.
- The record was merged from `acetogenium_medium` and `thermoanaerobacter_kivui_medium`.
- The checked sources were the normalized DSMZ 171 and KOMODO 171 records, MediaDive 171, and DSMZ Medium 171.

## Validation

- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to DSMZ/MediaDive Medium 171.
- The KOMODO 171 record references DSMZ Medium 171 through `mediadive.medium:171`.
- The DSMZ and KOMODO records are the same source formulation rather than separate recipes.

## Evidence

- DSMZ 171 lists a 1018 ml main recipe with 2 ml FeSO4 x 7 H2O solution at 0.1% w/v, 10 ml Modified Wolin's mineral solution, and 1000 ml distilled water.
- FeSO4 x 7 H2O solution is 1 g FeSO4 x 7 H2O in 1000 ml 0.1 N H2SO4, and DSMZ flags that ferrous sulfate solution as unstable and freshly prepared.
- Modified Wolin's mineral solution is a 1 L stock added at 10 ml/L.
- DSMZ 171 gives pH 6.5, an 80% H2 plus 20% CO2 anaerobic preparation, and a one bar overpressure instruction after inoculation.

## Completeness

- pH 6.5 is present.
- DSMZ preparation steps for the main recipe, Modified Wolin's mineral solution, and fresh ferrous sulfate solution are present.
- The main 1000 ml distilled-water row is missing.
- Modified Wolin's mineral solution and the FeSO4 solution are flattened at undiluted stock strength.

## Findings

- Modified Wolin's mineral solution was expanded at full 1 L stock strength instead of as a 10 ml/L addition.
- The FeSO4 x 7 H2O solution was expanded at full 1 L stock strength instead of as a 2 ml/L addition.
- The 1000 ml 0.1 N H2SO4 solvent inside the FeSO4 solution was converted to a nonsensical 1000 G_PER_L sulfuric acid ingredient row.
- Main-medium NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and FeSO4 x 7 H2O rows were summed with separate stock-solution rows before source-scope dilution was applied.
- The 1000 ml main distilled-water row is missing.

## Recommended Edits

- Regenerate DSMZ 171 with FeSO4 x 7 H2O solution and Modified Wolin's mineral solution retained as stock additions, or expand them only after applying the 2 ml/L and 10 ml/L dilution factors.
- Preserve 0.1 N H2SO4 as the solvent for FeSO4 x 7 H2O solution rather than converting its 1000 ml amount to 1000 G_PER_L.
- Keep duplicate ingredient names in separate recipe scopes until stock dilution is applied so NaCl, MgSO4, CaCl2, and FeSO4 are not over-summed.
- Preserve the main 1000 ml distilled-water row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that DSMZ 171 no longer carries a 1000 G_PER_L H2SO4 row or undiluted Modified Wolin mineral rows in the main ingredient list.

## Additional Notes

- None found.

# YAML Record Review: thiobacillus_prosperus_fo1_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiobacillus_prosperus_fo1_medium__447e2501.yaml
- Started UTC: 2026-09-25T12:58:31Z
- Finished UTC: 2026-09-25T12:58:55Z
- Verdict: needs curation

## Target

- Generated YAML for the direct JCM/MediaDive J1041 THIOBACILLUS PROSPERUS FO1 MEDIUM import.
- The record was merged from `thiobacillus_prosperus_fo1_medium`.
- The checked sources were MediaDive J1041 and the JCM 1041 medium page.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to JCM/MediaDive J1041, THIOBACILLUS PROSPERUS FO1 MEDIUM.
- The JCM 1041 page and MediaDive J1041 agree on the medium name and pH 6.0.
- No conflicting duplicate merge was observed.

## Evidence

- JCM J1041 uses 940 ml distilled water, 20 g NaCl, basal salts, and post-autoclave additions of 10 ml trace mineral solution and 50 ml FeSO4 x 7H2O solution.
- The J1041 trace mineral solution contains 1 L trace minerals from JCM 151 plus additional NiCl2 x 6 H2O and Na2SeO3 x 5 H2O.
- The FeSO4 stock contains 2 g FeSO4 x 7 H2O in 100 ml 0.1 N H2SO4 and should be prepared just before use.

## Completeness

- The JCM identity, pH 6.0 value, and first parent preparation step are present.
- The 10 ml trace mineral stock and 50 ml FeSO4 stock are flattened into top-level final ingredients.
- `NaCl` and `FeSO4 x 7 H2O` are summed across final and stock recipes.
- `H2SO4` is imported as 100 g/L even though the source row is 100 ml of 0.1 N H2SO4 inside the FeSO4 stock.

## Findings

- Final-medium ingredients are over-concentrated because trace and FeSO4 stock rows were expanded without retaining the 10 ml and 50 ml stock-addition volumes.
- The duplicate `NaCl` and `FeSO4 x 7 H2O` rows were summed across unrelated solution scopes.
- The FeSO4 stock's 0.1 N H2SO4 solvent was converted into a false final-medium 100 g/L H2SO4 ingredient.
- The 940 ml distilled-water row from JCM 1041 is omitted.

## Recommended Edits

- Model JCM 1041 with a parent basal solution plus 10 ml trace mineral solution and 50 ml FeSO4 solution.
- Remove cross-scope duplicate sums and recalculate only final concentrations that are actually needed.
- Keep the FeSO4 stock recipe and its just-before-use instruction as stock-solution metadata.
- Restore the 940 ml distilled-water row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Confirm the JCM 151 trace-minerals composition if it is expanded locally.
- Verify that JCM 1041 remains distinct from JCM 1084 because their pH and salt/stock formulas differ.

## Additional Notes

- None found.

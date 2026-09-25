# YAML Record Review: thiobacillus_prosperus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiobacillus_prosperus_medium__48108ae0.yaml
- Started UTC: 2026-09-25T12:58:56Z
- Finished UTC: 2026-09-25T12:59:20Z
- Verdict: needs curation

## Target

- Generated YAML for the direct JCM/MediaDive J1084 THIOBACILLUS PROSPERUS MEDIUM import.
- The record was merged from `thiobacillus_prosperus_medium`.
- The checked sources were MediaDive J1084 and the JCM 1084 medium page.

## Validation

- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to JCM/MediaDive J1084, THIOBACILLUS PROSPERUS MEDIUM.
- The JCM 1084 page and MediaDive J1084 agree on the medium name and pH 2.5.
- No conflicting duplicate merge was observed.

## Evidence

- JCM J1084 uses 940 ml distilled water, 0.5 g NaCl, basal salts, 2 mg NiCl2 x 6 H2O, 10 ml trace mineral solution, and a post-autoclave addition of 50 ml FeSO4 x 7H2O solution.
- The J1084 trace mineral solution contains 1 L trace minerals from JCM 151 plus additional NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O.
- The FeSO4 stock is 40 g FeSO4 x 7H2O in 0.1 N H2SO4 brought to 100 ml, filter-sterilized, and stored under N2.

## Completeness

- The JCM identity, pH 2.5 value, first parent preparation step, and FeSO4 stock preparation text are present.
- The 10 ml trace mineral stock is flattened into top-level final ingredients.
- `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, `NaCl`, and `NiCl2 x 6 H2O` are summed across basal and stock recipes.
- The 50 ml FeSO4 stock addition is not represented as an ingredient quantity.

## Findings

- Trace-mineral stock rows were expanded without applying the 10 ml stock-addition volume.
- Duplicate basal and trace-stock rows were summed across unrelated solution scopes.
- The high-concentration FeSO4 stock is described in preparation text but is missing from the ingredient table as a 50 ml post-autoclave addition.
- The 940 ml distilled-water row from JCM 1084 is omitted.

## Recommended Edits

- Model JCM 1084 with a parent basal solution plus 10 ml trace mineral solution and 50 ml FeSO4 solution.
- Remove cross-scope duplicate sums and retain basal 0.5 g NaCl and 2 mg NiCl2 x 6 H2O separately from trace stock ingredients.
- Add the FeSO4 stock amount and keep its N2 storage instruction attached to the stock.
- Restore the 940 ml distilled-water row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Confirm the JCM 151 trace-minerals composition if it is expanded locally.
- Verify that JCM 1084 remains distinct from JCM 1041 because their pH and salt/stock formulas differ.

## Additional Notes

- None found.

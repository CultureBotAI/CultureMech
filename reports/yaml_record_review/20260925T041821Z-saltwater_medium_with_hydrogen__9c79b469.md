# YAML Record Review: saltwater_medium_with_hydrogen__9c79b469

- Repository: CultureMech
- Record: data/merge_yaml/merged/saltwater_medium_with_hydrogen__9c79b469.yaml
- Started UTC: 2026-09-25T04:18:21Z
- Finished UTC: 2026-09-25T04:18:21Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:003114`, `saltwater_medium_with_hydrogen`, from `data/merge_yaml/merged/saltwater_medium_with_hydrogen__9c79b469.yaml`.

The record is a single-source direct MediaDive/JCM J772 import for `SALTWATER MEDIUM WITH HYDROGEN`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to JCM Medium J772.

No duplicate merge or synonym issue was found in the generated YAML.

## Evidence

JCM 772 lists a parent saltwater base with 20 g NaCl, 4 g Na2SO4, 3 g MgCl2 x 6H2O, 0.5 g KCl, 0.15 g CaCl2 x 2H2O, 0.25 g NH4Cl, 0.2 g KH2PO4, 1 mg Resazurin, and 1 L distilled water.

After cooling the autoclaved base, JCM 772 adds nine anaerobic stocks per liter: 1 ml Trace element solution from JCM 439, 1 ml Selenite-tungstate solution from JCM 431, 1 ml Vitamin solution from JCM 403, 1 ml Thiamine solution from JCM 403, 1 ml Vitamin B12 solution from JCM 403, 1 ml Riboflavin solution from JCM 462, 10 ml 1.0 M Sodium fumarate solution, 30 ml 8% NaHCO3 solution, and 8 ml 5% Na2S x 9H2O solution.

JCM 772 cools the base under an H2-CO2 4:1 gas stream, distributes and seals the medium under the same gas mixture, readjusts pH to 7.2-7.4 after stock addition, and pressurizes inoculated culture vessels to 200 kPa H2-CO2 4:1.

JCM 439 defines Trace element solution as a stock with 12.5 ml 25% HCl, 2.1 g FeSO4 x 7H2O, 30 mg H3BO3, 100 mg MnCl2 x 4H2O, 190 mg CoCl2 x 6H2O, 24 mg NiCl2 x 6H2O, 2 mg CuCl2 x 2H2O, 144 mg ZnSO4 x 7H2O, 36 mg Na2MoO4 x 2H2O, and 987 ml distilled water.

JCM 431 defines Selenite-tungstate solution as a stock with 0.4 g NaOH, 6 mg Na2SeO3 x 5H2O, 8 mg Na2WO4 x 2H2O, and 1 L distilled water.

JCM 403 and JCM 462 define the four vitamin stocks: Vitamin solution, Thiamine solution, Vitamin B12 solution, and Riboflavin solution.

## Completeness

The parent salt rows are present, but they were scaled down by the 54 ml of post-autoclave stock additions instead of preserving the JCM 772 per-liter base formula.

The distilled-water row is absent.

Trace element solution and Selenite-tungstate solution were flattened into parent ingredient rows at stock strength.

Vitamin solution, Thiamine solution, Vitamin B12 solution, and Riboflavin solution are present only as empty `Unknown solution` stubs.

The generated record has no structured Hydrogen gas or Carbon dioxide gas entries; H2-CO2 is preserved only as preparation prose.

## Findings

The generated direct MediaDive record converted a one-liter base plus nine anaerobic stock additions into a partially diluted flat recipe. For example, the 20 g/L NaCl source row became 18.9753 g/L and the 4 g/L Na2SO4 source row became 3.79507 g/L.

Three sterile stock additions were imported as final grams per liter: 10 ml 1.0 M Sodium fumarate solution became `Sodium fumarate` 10 g/L, 30 ml 8% NaHCO3 solution became `NaHCO3` 30 g/L, and 8 ml 5% Na2S x 9H2O solution became `Na2S x 9 H2O` 8 g/L.

JCM 439 and JCM 431 stock formulas were flattened into parent ingredients, so their acid, trace metal, NaOH, selenite, and tungstate concentrations are stock-strength rows in the finished medium.

The solution migrator left all four vitamin stocks as empty `Unknown solution` stubs with `G_PER_L` concentration values copied from their 1 ml/L aliquots.

## Recommended Edits

Repair the direct MediaDive J772 normalized source so it preserves the JCM 772 parent saltwater base as written and adds the nine anaerobic stocks as `ML_PER_L` solution aliquots.

Move JCM 439 Trace element solution and JCM 431 Selenite-tungstate solution components into nested stock scopes.

Expand Vitamin solution, Thiamine solution, Vitamin B12 solution, and Riboflavin solution from their JCM 403 and JCM 462 references instead of leaving empty `Unknown solution` stubs.

Add structured Hydrogen gas and Carbon dioxide gas ingredient entries with the 4:1 gas mixture and 200 kPa pressure details retained in `preparation_steps`.

Regenerate the merge layer after the normalized MediaDive J772 source is repaired.

## Follow-up Checks

Confirm the regenerated parent salt rows retain the exact JCM 772 base values: 20 g/L NaCl, 4 g/L Na2SO4, 3 g/L MgCl2 x 6H2O, 0.5 g/L KCl, 0.15 g/L CaCl2 x 2H2O, 0.25 g/L NH4Cl, 0.2 g/L KH2PO4, and 1 mg/L Resazurin.

Confirm the regenerated record has nine nonempty solution additions and no `Unknown solution` names.

Confirm no trace-element, selenite-tungstate, or vitamin stock component remains as a direct parent ingredient.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.

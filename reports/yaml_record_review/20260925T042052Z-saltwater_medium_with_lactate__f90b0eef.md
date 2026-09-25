# YAML Record Review: saltwater_medium_with_lactate__f90b0eef

- Repository: CultureMech
- Record: data/merge_yaml/merged/saltwater_medium_with_lactate__f90b0eef.yaml
- Started UTC: 2026-09-25T04:20:52Z
- Finished UTC: 2026-09-25T04:20:52Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002811`, `saltwater_medium_with_lactate`, from `data/merge_yaml/merged/saltwater_medium_with_lactate__f90b0eef.yaml`.

The record is the direct MediaDive/JCM J462 import for `SALTWATER MEDIUM WITH LACTATE`, with `saltwater_medium_with_acetate_and_ferric_citrate` / JCM J463 merged into it as a synonym.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The primary identity is correctly grounded to JCM Medium J462.

The synonym and `merged_from` link to `saltwater_medium_with_acetate_and_ferric_citrate` are not valid. JCM 463 derives from JCM 462, but it removes Na2S x 9H2O, uses 20 mM sodium acetate and 30 mM ferric citrate instead of sodium lactate, and reduces with L-cysteine HCl.

## Evidence

JCM 462 lists a parent medium with 20 g NaCl, 4 g Na2SO4, 3 g MgCl2 x 6H2O, 0.15 g CaCl2 x 2H2O, 0.75 g NH4Cl, 0.6 g KH2PO4, 0.09 g KBr, 0.5 g KCl, 2.5 g NaHCO3, 1 ml Trace element solution from JCM 439, 1 ml Vitamin solution from JCM 403, 1 ml Thiamine solution from JCM 403, 1 ml Vitamin B12 solution from JCM 403, 1 ml local Riboflavin stock, 1 ml Selenite-tungstate solution from JCM 431, 2.25 g Sodium lactate, 0.3 g Na2S x 9H2O, and 1 mg Resazurin.

JCM 462 dissolves the components except NaHCO3, the vitamin stocks, sodium lactate, and Na2S x 9H2O in 900 ml distilled water; cools under N2-CO2 4:1; autoclaves sealed Hungate tubes; separately autoclaves 0.2 M sodium lactate under N2; then adds one ninth volume of sodium lactate plus filter-sterilized 8% NaHCO3, Vitamin solution, Thiamine solution, and Vitamin B12 solution.

JCM 462 defines a local Riboflavin solution as 2.5 mg Riboflavin in 100 ml distilled water.

JCM 463 is a related derivative of JCM 462, but it is the acetate and ferric citrate medium, not another record for the lactate recipe.

## Completeness

The generated record carries all JCM 462 salts and stock contents in one flat parent `ingredients` list.

JCM 462 parent ingredients are wildly overconcentrated: for example, 20 g NaCl became 3333.33 g/L, 4 g Na2SO4 became 666.667 g/L, and 2.25 g Sodium lactate became 375 g/L.

Trace element solution, Vitamin solution, Thiamine solution, Vitamin B12 solution, local Riboflavin solution, and Selenite-tungstate solution are not represented as solution scopes.

Nitrogen gas and Carbon dioxide gas are absent as structured gas ingredients; the N2-CO2 4:1 headspace is present only as preparation prose.

The direct JCM 462 generated record is merged with JCM 463 even though JCM 463 intentionally changes the carbon source, reductant, and terminal electron acceptor chemistry.

## Findings

The direct MediaDive import expanded the JCM 462 local `Riboflavin (see below)` stock as a self-reference to all of JCM 462. That made the final parent concentrations nonsensical and stamped every ingredient with `Copied from referenced JCM Medium 462`.

The generated concentrations show reference-scope unit corruption. Parent base rows are hundreds of times too high, trace element and selenite-tungstate stock rows were copied directly into the final recipe, and the local Riboflavin stock became a direct `Riboflavin` 0.025 g/L final ingredient.

The JCM 403 Vitamin, Thiamine, and Vitamin B12 stocks were flattened into direct vitamin ingredient rows instead of three nested stock aliquots.

The merge with JCM 463 is a false duplicate merge. JCM 463 should remain a derivative variant of JCM 462 because acetate plus ferric citrate plus L-cysteine HCl is not the same recipe as lactate plus Na2S x 9H2O.

## Recommended Edits

Repair the direct MediaDive J462 normalized source by treating `Riboflavin (see below)` as a local stock table reference, not as a reference to the entire JCM 462 medium.

Model JCM 439 Trace element solution, JCM 403 Vitamin solution, JCM 403 Thiamine solution, JCM 403 Vitamin B12 solution, local Riboflavin solution, and JCM 431 Selenite-tungstate solution as solution scopes or stock aliquots.

Reject the J462 and J463 duplicate edge so regeneration no longer folds `saltwater_medium_with_acetate_and_ferric_citrate` into the lactate record.

Add structured Nitrogen gas and Carbon dioxide gas entries for the N2-CO2 4:1 headspace.

Regenerate the merge layer after the JCM 462 source repair and false-duplicate rejection.

## Follow-up Checks

Confirm the regenerated JCM 462 parent recipe has source-scale rows, including 20 g/L NaCl, 4 g/L Na2SO4, 2.5 g/L NaHCO3, 2.25 g/L Sodium lactate, 0.3 g/L Na2S x 9H2O, and 1 mg/L Resazurin.

Confirm the regenerated JCM 462 record has no `saltwater_medium_with_acetate_and_ferric_citrate` synonym and no JCM 463 `merged_from` source.

Confirm no regenerated ingredient carries `Copied from referenced JCM Medium 462`.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.

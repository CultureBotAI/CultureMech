# YAML Record Review: selenomonas_wg_medium__551ab349

- Repository: CultureMech
- Record: data/merge_yaml/merged/selenomonas_wg_medium__551ab349.yaml
- Started UTC: 2026-09-25T05:10:03Z
- Finished UTC: 2026-09-25T05:10:03Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:003051`, `selenomonas_wg_medium`, from `data/merge_yaml/merged/selenomonas_wg_medium__551ab349.yaml`.

The target record is a direct MediaDive/JCM Medium J705 import for `SELENOMONAS WG MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to JCM Medium J705.

It is a same-source duplicate of the generated TOGO M727 `SELENOMONAS_WG_MEDIUM` record, which also cites JCM GRMD 705.

No unrelated Selenomonas medium was treated as a duplicate.

## Evidence

JCM Medium 705 lists KH2PO4, K2HPO4, (NH4)2SO4, NaCl, MgSO4 x 7H2O, CaCl2 x 2H2O, Tryptone (BD-Difco), Yeast extract, Glucose, 10 ml VFA solution, 1 mg Resazurin, and 1 L Distilled water.

After the base is adjusted to pH 7.0, boiled, cooled under N2-CO2 4:1, distributed under the same gas, sealed, and autoclaved, JCM adds two sterile 5% reducing solutions per liter: 5 ml 5% L-Cysteine-HCl-H2O and 5 ml 5% Na2S-9H2O.

The VFA solution is a separate stock containing 1 ml Butyric acid, 1 ml iso-Valeric acid, 1 ml n-Valeric acid, and 100 ml Distilled water. The VFA stock is adjusted to pH 6.7 to 6.8 and stored tightly stoppered at 4C.

## Completeness

The generated record omits the main 1 L Distilled water row and the VFA stock water row.

The generated top-level `ph_value` is 6.8, which comes from the VFA solution adjustment; the top-level medium should carry the base-medium pH 7.0 adjustment.

The 10 ml VFA solution addition is flattened: its three 1 ml acid stock components are represented as 1 g/L final-medium ingredients.

The 5 ml/L additions of 5% L-Cysteine-HCl-H2O and 5% Na2S-9H2O are represented as 5 g/L final-medium ingredients instead of stock additions.

The N2-CO2 4:1 gas atmosphere is preserved only in preparation prose, not structured gas rows.

## Findings

The VFA solution boundary was lost during import.

Liquid VFA stock components were converted to `G_PER_L` parent ingredients.

The 5% reducing solution additions were flattened and overstate the final cysteine and sulfide amounts.

The generated top-level pH is sourced from the VFA stock, not the base medium.

The direct JCM J705 and TOGO M727 imports remain split into separate generated records for the same JCM recipe.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/selenomonas_wg_medium.yaml` so VFA solution is nested at 10 ml/L and contains Butyric acid, iso-Valeric acid, n-Valeric acid, and Distilled water in the JCM stock proportions.

Represent 5% L-Cysteine-HCl-H2O and 5% Na2S-9H2O as sterile stock additions at 5 ml/L instead of 5 g/L direct ingredients.

Restore the source water rows and set the top-level medium pH from the base pH 7.0 instruction rather than the VFA stock pH.

Merge or suppress the TOGO M727 same-source duplicate after the direct JCM and TOGO branches use matching stock boundaries.

Regenerate the merged YAML after the normalized JCM source is repaired.

## Follow-up Checks

Confirm the regenerated record no longer has Butyric acid, iso-Valeric acid, n-Valeric acid, 5% L-Cysteine-HCl-H2O, or 5% Na2S-9H2O as 1 to 5 g/L parent rows.

Confirm VFA solution has a 10 ml/L parent addition and a 100 ml Distilled water stock composition.

Confirm pH 7.0 is the top-level pH and pH 6.7 to 6.8 is scoped only to the VFA stock note.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.

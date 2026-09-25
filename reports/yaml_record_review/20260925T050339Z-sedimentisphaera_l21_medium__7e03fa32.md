# YAML Record Review: sedimentisphaera_l21_medium__7e03fa32

- Repository: CultureMech
- Record: data/merge_yaml/merged/sedimentisphaera_l21_medium__7e03fa32.yaml
- Started UTC: 2026-09-25T05:03:39Z
- Finished UTC: 2026-09-25T05:03:39Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002348`, `sedimentisphaera_l21_medium`, from `data/merge_yaml/merged/sedimentisphaera_l21_medium__7e03fa32.yaml`.

The target record is a single-source direct MediaDive/JCM J1177 import for `SEDIMENTISPHAERA L21 MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The target record is correctly grounded to JCM Medium J1177.

The generated merge layer also contains `data/merge_yaml/merged/SEDIMENTISPHAERA_L21_MEDIUM.yaml`, a TOGO M1261 import whose metadata identifies the same recipe as `JCM_M1177` from the same JCM GRMD 1177 URL. The two generated records are true duplicate source imports that did not merge.

## Evidence

JCM 1177 lists 120 g NaCl, 6 g MgCl2 x 6H2O, 1.5 g KCl, 1 g Na2SO4, 1 g NH4Cl, 0.4 g CaCl2 x 2H2O, 0.4 g K2HPO4, 10 ml Trace mineral solution from JCM 1084, 0.5 mg Resazurin, and 950 ml Distilled water in the base.

JCM 1177 then adds 10 ml 10% Glucose solution, 10 ml Trace vitamins from JCM 197, 30 ml 8% NaHCO3 solution, 10 ml 5% L-Cysteine HCl x H2O solution, and 10 ml 5% Na2S x 9H2O solution per liter.

JCM 1084 defines the JCM 1177 trace mineral solution by adding NiCl2 x 6H2O, Na2SeO3 x 5H2O, and sodium tungstate to JCM 151 Trace minerals.

## Completeness

The direct MediaDive/JCM target scales base salts and Resazurin below their source values.

The target represents the 10% Glucose, 8% NaHCO3, 5% L-Cysteine HCl x H2O, and 5% Na2S x 9H2O additions as 10 g/L, 30 g/L, 10 g/L, and 10 g/L parent rows.

The target flattens Trace mineral solution from JCM 1084 and Trace vitamins from JCM 197 into direct parent rows at stock strength.

The target omits the 950 ml Distilled water row.

The N2-CO2 atmosphere is present only in preparation prose, not as structured gas ingredients.

## Findings

The direct MediaDive import flattened all post-autoclave stock additions into final-medium ingredients.

The generated base rows are diluted by a calculated final volume rather than preserving the source masses.

The linked JCM 1084 and JCM 197 stocks lost their solution boundaries.

The TOGO M1261 duplicate is an unmerged copy of the same JCM 1177 recipe.

## Recommended Edits

Repair the direct MediaDive/JCM J1177 normalized source so the JCM 1084 Trace mineral solution, JCM 197 Trace vitamins, 10% Glucose solution, 8% NaHCO3 solution, 5% L-Cysteine HCl x H2O solution, and 5% Na2S x 9H2O solution remain solution-scoped with their source ml/L volumes.

Restore the source-scale base rows: 120 g/L NaCl, 6 g/L MgCl2 x 6H2O, 1.5 g/L KCl, 1 g/L Na2SO4, 1 g/L NH4Cl, 0.4 g/L CaCl2 x 2H2O, 0.4 g/L K2HPO4, 0.5 mg/L Resazurin, and 950 ml/L Distilled water.

Normalize the direct MediaDive/JCM J1177 and TOGO M1261 branches so the same-source imports merge.

Consider adding structured N2 and CO2 gas ingredients.

Regenerate the merge layer after the normalized sources are repaired.

## Follow-up Checks

Confirm the regenerated parent has no direct 10 g/L Glucose, 30 g/L NaHCO3, 10 g/L L-Cysteine HCl x H2O, or 10 g/L Na2S x 9H2O rows.

Confirm the regenerated parent has no direct stock-strength rows from JCM 1084 or JCM 197, such as 0.03 g/L NiCl2 x 6H2O or 0.002 g/L Biotin.

Confirm the regenerated merge layer has one JCM 1177 record, not both `sedimentisphaera_l21_medium__7e03fa32.yaml` and `SEDIMENTISPHAERA_L21_MEDIUM.yaml`.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.

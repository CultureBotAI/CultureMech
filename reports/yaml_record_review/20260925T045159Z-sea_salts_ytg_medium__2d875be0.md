# YAML Record Review: sea_salts_ytg_medium__2d875be0

- Repository: CultureMech
- Record: data/merge_yaml/merged/sea_salts_ytg_medium__2d875be0.yaml
- Started UTC: 2026-09-25T04:51:59Z
- Finished UTC: 2026-09-25T04:51:59Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002466`, `sea_salts_ytg_medium`, from `data/merge_yaml/merged/sea_salts_ytg_medium__2d875be0.yaml`.

The target record is a single-source direct MediaDive/JCM J1302 import for `SEA SALTS YTG MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The target record is correctly grounded to JCM Medium J1302.

The generated merge layer also contains `data/merge_yaml/merged/SEA_SALTS_YTG_MEDIUM.yaml`, a stale TOGO M1399 import for the same JCM_M1302 source. The normalized TOGO M1399 source has since been repaired to keep JCM 1302 stock additions in `solutions`.

## Evidence

JCM 1302 lists 0.5 g Yeast extract, 1 g Tryptone, 2.5 g Glucose, 30 g Sea salts, 1 ml Trace minerals from JCM 151, 1 ml 0.1% Na2SeO3 solution, 0.2 g L-Cysteine HCl x H2O, 0.5 mg Resazurin, and 1 L Distilled water.

JCM 1302 then instructs curators to autoclave under N2 and, after cooling, add 10 ml Trace vitamins from JCM 197 and 5 ml 1 M Sodium thiosulfate solution per liter.

JCM 151 defines the Trace minerals stock that includes Nitrilotriacetic acid, MgSO4 x 7H2O, MnSO4 x nH2O, NaCl, FeSO4 x 7H2O, CoSO4 x 7H2O, CaCl2 x 2H2O, ZnSO4 x 7H2O, CuSO4 x 5H2O, AlK(SO4)2, H3BO3, and Na2MoO4 x 2H2O.

JCM 197 defines the Trace vitamins stock that includes Biotin, Folic acid, Pyridoxine HCl, Thiamine HCl, Riboflavin, Nicotinic acid, Calcium pantothenate, Vitamin B12, p-Aminobenzoic acid, and Lipoic acid.

## Completeness

The direct MediaDive/JCM target scales the base Yeast extract, Tryptone, Glucose, Sea Salt, L-Cysteine HCl x H2O, and Resazurin rows down from source values by the later 16 ml of stock additions.

The target represents 1 ml/L 0.1% Na2SeO3 solution as a direct 1 g/L Na2SeO3 ingredient.

The target represents 5 ml/L 1 M Sodium thiosulfate solution as a direct 5 g/L Sodium thiosulfate ingredient.

The target flattens all JCM 151 Trace minerals and JCM 197 Trace vitamins components into the parent recipe at stock strength.

The target omits the 1 L Distilled water row and has no structured N2 gas ingredient.

The JCM 151 Trace minerals pH 6.5/7.0 preparation note is attached to the parent medium as a second preparation step.

## Findings

The importer flattened multiple JCM 1302 solution additions into parent ingredients instead of preserving them as stock scopes with 1 ml/L, 10 ml/L, and 5 ml/L addition volumes.

The generated base rows are all diluted by a calculated final volume of 1016 ml even though the JCM source reports them per liter of base medium.

Stock-strength trace mineral and vitamin rows make the target chemically unusable as a final-medium recipe.

The generated parent carries a trace-mineral-stock pH instruction unrelated to the parent JCM 1302 preparation.

The generated TOGO M1399 duplicate is stale relative to `data/normalized_yaml/bacterial/TOGO_M1399_Sea_Salts_YTG_Medium.yaml`, which has already been repaired to model these solution additions explicitly.

## Recommended Edits

Repair the direct MediaDive/JCM J1302 normalized source using the same solution-scoped structure already present in the repaired TOGO M1399 normalized source.

Restore the source-scale parent rows: 0.5 g/L Yeast extract, 1 g/L Tryptone, 2.5 g/L Glucose, 30 g/L Sea salts, 0.2 g/L L-Cysteine HCl x H2O, and 0.5 mg/L Resazurin.

Represent Trace minerals at 1 ml/L, 0.1% Na2SeO3 solution at 1 ml/L, Trace vitamins at 10 ml/L, and 1 M Sodium thiosulfate solution at 5 ml/L instead of flattening their contents into parent ingredients.

Restore the 1 L Distilled water row and consider adding structured N2 gas.

Regenerate the merge layer so the direct JCM J1302 branch can merge with the repaired TOGO M1399 source.

## Follow-up Checks

Confirm the regenerated parent record has no direct 1 g/L Na2SeO3 row and no direct 5 g/L Sodium thiosulfate row.

Confirm the regenerated parent record has no JCM 151 or JCM 197 stock-strength rows such as 1.5 g/L Nitrilotriacetic acid or 0.002 g/L Biotin.

Confirm the regenerated parent has no preparation step that starts with `Dissolve nitrilotriacetic acid`.

Confirm the stale `SEA_SALTS_YTG_MEDIUM.yaml` duplicate disappears or merges into a single generated JCM 1302 record.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.

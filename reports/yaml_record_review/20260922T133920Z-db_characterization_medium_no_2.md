# YAML Record Review: db_characterization_medium_no_2

- Repository: CultureMech
- Record: data/merge_yaml/merged/db_characterization_medium_no_2.yaml
- Started UTC: 2026-09-22T13:36:44Z
- Finished UTC: 2026-09-22T13:39:20Z
- Verdict: needs curation

## Target

Reviewed generated record `data/merge_yaml/merged/db_characterization_medium_no_2.yaml` with generated identifier `CultureMech:009974`, media term `TOGO:M578`, original name `DB Characterization Medium NO. 2`, category `bacterial`, and one merged source, `TOGO_M578_DB_Characterization_Medium_NO._2`.

## Validation

- LinkML open-schema validation: passed.
- Strict validation: passed with 0 error rows in `/private/tmp/db_characterization_medium_no_2.strict.tsv`.
- Reference validation: passed with 0 references checked.
- Term validation: passed.
- Embedded curation history: not checked; `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` blocks.

## Identity and Grounding

TOGO M578 is a faithful wrapper around JCM Medium 574, `DB CHARACTERIZATION MEDIUM NO. 2`: the TOGO API reports `original_media_id` `JCM_M574`, source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=574`, and pH `7.0 - 7.5`, matching the JCM page.

This generated record is source-equivalent to the local TOGO import but not to the older direct JCM/MediaDive record `data/normalized_yaml/bacterial/db_characterization_medium_no_2.yaml`. The exact gitignore-independent search for `M578`, `JCM_M574`, `GRMD=574`, and `db_characterization_medium_no_2` found the TOGO owner, this generated target, the separate direct JCM owner, downstream media that reference M578 stocks, and the sibling `DB Characterization Medium NO.2 With 1% Sea Salts` variant family.

## Evidence

JCM 574 defines a staged recipe. The first stage uses 833.0 ml MDS salt water, 1.0 ml FeCl2 solution, 1.0 ml trace element solution, 0.25 g peptone, and 0.05 g yeast extract, then brings the volume to 980 ml with distilled water. After autoclaving, it adds 5.0 ml 1 M NH4Cl, 2.0 ml potassium phosphate buffer, 3.0 ml vitamin solution, and 10.0 ml 1 M sodium pyruvate solution, and readjusts pH to 7.0 - 7.5 with sterile 10% Na2CO3 if needed.

The same source then defines reusable stocks. `MDS salt water` is made from 240.0 g NaCl, 30.0 g MgCl2 x 6 H2O, 35.0 g MgSO4 x 7 H2O, 7.0 g KCl, 5.0 ml 1 M CaCl2 solution, and water to 1.0 L, adjusted to pH 7.5 with 1 M Tris base. `Potassium phosphate buffer` is an 83.4:16.6 mix of 1 M K2HPO4 and 1 M KH2PO4 doubled with an equal volume of water. `Vitamin solution` is a 1 L stock containing milligram quantities of vitamins.

## Completeness

The generated record has the correct TOGO/JCM identity but not a faithful recipe graph. It mixes the final medium additions, three local stock definitions, and six unresolved solution references into one flat ingredient list with invalid `G_PER_L` units, leaves every solution composition empty, and drops all JCM preparation comments and pH metadata.

## Findings

1. **Milliliter final additions are imported as grams per liter.** The final recipe calls for 833 ml MDS salt water, 1 ml FeCl2 solution, 1 ml trace element solution, 5 ml 1 M NH4Cl, 2 ml potassium phosphate buffer, 3 ml vitamin solution, and 10 ml 1 M sodium pyruvate solution; the generated YAML stores the same numbers as `G_PER_L` ingredients or empty `solutions`.

2. **Stock solutions are flattened into media-level ingredients.** MDS salts, potassium phosphate buffer constituents, and vitamin solution constituents belong inside their stock definitions. In the generated record they appear as top-level ingredients, so stock concentrations such as 240 g/L NaCl or 3 mg/L biotin are represented as final medium concentrations.

3. **The vitamin stock has 1000-fold unit errors.** JCM lists biotin, folic acid, pyridoxine HCl, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid in mg for a 1 L vitamin stock. The generated record stores those numeric values as `G_PER_L`, e.g. 3 mg biotin becomes 3 g/L.

4. **pH and preparation semantics are missing.** The source pH is 7.0 - 7.5 and the JCM page carries instructions for bringing the first stage to 980 ml, autoclaving, adding filter-sterilized or autoclaved stocks, readjusting pH with sterile Na2CO3, washing agar, preparing MDS salt water, and preparing phosphate buffer. None of these steps are represented.

5. **Legacy MediaIngredientMech grounding remains.** `DL--Calcium pantothenate` still has `mediaingredientmech_term: MediaIngredientMech:000926` and no primary CHEBI term in the generated TOGO path.

## Recommended Edits

- Rebuild `TOGO_M578_DB_Characterization_Medium_NO._2.yaml` with the JCM 574 formula as a final 1 L medium plus structured child stocks rather than flattening all M578 tables into top-level ingredients.
- Represent milliliter additions as `ML_PER_L` final additions or as references to populated stock solutions, not `G_PER_L`.
- Convert vitamin-stock milligram rows to the correct stock concentrations, then keep the stock scoped under the 3 ml/L final vitamin-solution addition.
- Preserve the 7.0 - 7.5 final pH range and JCM preparation steps.
- Replace the remaining legacy `DL--Calcium pantothenate` MediaIngredientMech link with a CHEBI grounding or leave it ungrounded if the exact stereochemical form is not supported.

## Follow-up Checks

- After repair, compare the regenerated M578 output against both TOGO M578 and JCM GRMD 574.
- Re-run strict, reference, and term validation.
- Re-review the M578-dependent records, especially `5_salt_water_growth_medium`, `modified_growth_medium_with_23_total_salt_concentration`, and `db_characterization_medium_no_2_with_1_sea_salts`, to make sure they import only the intended MDS or full-medium stock portions.

## Additional Notes

The review used gitignore-independent `rg --no-ignore --hidden` searches for `M578`, `JCM_M574`, `GRMD=574`, and `db_characterization_medium_no_2`, so ignored files were included in the duplicate/source scan.

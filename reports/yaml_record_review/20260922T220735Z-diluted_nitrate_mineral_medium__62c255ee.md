# YAML Record Review: diluted_nitrate_mineral_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/diluted_nitrate_mineral_medium__62c255ee.yaml`
- Started UTC: 2026-09-22T22:06:21Z
- Finished UTC: 2026-09-22T22:07:35Z
- Verdict: needs curation

## Target

`CultureMech:007562` represents TOGO Medium M1046, `Diluted Nitrate Mineral Medium`, imported from the JCM Medium 992 agar-plate formulation. The generated record is a single-source merge from `data/normalized_yaml/bacterial/TOGO_M1046_Diluted_Nitrate_Mineral_Medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

A gitignore-independent `find` over `data/` found this TOGO M1046 agar record, a separate TOGO M1045 liquid record, the MediaDive/JCM J992 generated record, and related modified nitrate mineral salts media. TOGO M1046 should stay distinct from the liquid M1045 recipe, but it should be linked to the same JCM 992 source family.

## Evidence

- The live TOGO M1046 API lists 990 ml distilled water, 0.2 g MgSO4 x 7H2O, 0.03 g CaCl2 x 2H2O, 0.2 g KNO3, 15 g/l agar, 1 ml Modified SL--4 trace element solution, and 10 ml chelated iron solution, followed after autoclaving by 5 ml 0.2 M KH2PO4, 5 ml 0.2 M Na2HPO4, and 50% methane for agar plate cultures.
- The live JCM 992 page lists the same base ingredients, states that the two 0.2 M phosphate solutions are filter-sterilized additions after autoclaving and cooling to 60 C, and gives a target pH around 6.8.
- The live JCM 992 page defines Modified SL-4 trace element solution inline as 0.5 g EDTA-2Na, 0.2 g FeSO4 x 7H2O, 0.25 g CuSO4 x 5H2O, 100 ml SL-6 trace element solution, and 900 ml distilled water.
- JCM 992 links the chelated iron solution to JCM Medium 828, while the TOGO API carries the row as a reference to Medium M863; `find` found `TOGO_M863_Modified_NMS_Medium.yaml`, so that cross-reference needs resolution against the current JCM link.

## Completeness

The record is incomplete because all four stock or buffer additions were migrated into empty `Unknown solution` stubs and their milliliter additions became gram-per-liter values. The pH and post-autoclave preparation comments are also absent.

## Findings

- `Modified SL--4 trace element solution`, 1 ml, is an empty `Unknown solution` with `1 G_PER_L`.
- `Chelated iron solution`, 10 ml, is an empty `Unknown solution` with `10 G_PER_L`.
- The two 5 ml phosphate buffer additions are empty `Unknown solution` stubs with `5 G_PER_L`.
- The source pH value, 6.8, is absent.
- The autoclave, 60 C cooling, filter-sterilized phosphate addition, and 50% methane agar-plate cultivation instructions are absent.
- The Modified SL-4 child formula on the JCM 992 page is not represented under the 1 ml Modified SL-4 addition.
- The normalized TOGO source gained a methane CHEBI grounding in August, but the generated record is stale and still lacks that grounding.

## Recommended Edits

- Rebuild the M1046 record with the 990 ml base and four explicit milliliter additions: 1 ml Modified SL-4, 10 ml chelated iron, 5 ml 0.2 M KH2PO4, and 5 ml 0.2 M Na2HPO4.
- Nest the JCM 992 Modified SL-4 composition, including its 100 ml SL-6 cross-reference and 900 ml water, under the Modified SL-4 addition.
- Resolve the chelated iron target by comparing TOGO M863 with the current JCM Medium 828 link before expanding or linking that stock.
- Represent the 0.2 M phosphate additions as molar stocks or source-backed stock rows instead of gram-per-liter empty stubs.
- Preserve pH 6.8, 60 C cooling, filter-sterilized post-autoclave additions, and 50% methane agar-plate cultivation notes.
- Regenerate so the August methane grounding reaches the generated record.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no source milliliter row remains as a `G_PER_L` empty solution.
- Verify that M1046 stays distinct from M1045 while carrying an explicit relationship to the JCM 992 source family.
- Verify that the chelated iron cross-reference resolves to the intended JCM medium.

## Additional Notes

None found.

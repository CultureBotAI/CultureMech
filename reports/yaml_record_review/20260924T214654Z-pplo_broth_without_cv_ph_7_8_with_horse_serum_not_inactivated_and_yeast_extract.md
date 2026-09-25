# YAML Record Review: pplo_broth_without_cv_ph_7_8_with_horse_serum_not_inactivated_and_yeast_extract

- Repository: CultureMech
- Record: data/merge_yaml/merged/pplo_broth_without_cv_ph_7_8_with_horse_serum_not_inactivated_and_yeast_extract.yaml
- Started UTC: 2026-09-24T21:46:54Z
- Finished UTC: 2026-09-24T21:46:54Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:008814
- Name: pplo_broth_without_cv_ph_7_8_with_horse_serum_not_inactivated_and_yeast_extract
- Source import: TOGO M2226
- Primary external ID: TOGO:M2226
- Maintained input: data/normalized_yaml/bacterial/pplo_broth_without_cv_ph_7_8_with_horse_serum_not_inactivated_and_yeast_extract.yaml

This generated record represents TOGO M2226 / ATCC Medium 247, PPLO broth without CV at pH 7.8 with non-inactivated horse serum and yeast extract.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/pplo_broth_without_cv_ph_7_8_with_horse_serum_not_inactivated_and_yeast_extract.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

TOGO M2226 cites ATCC Medium 247. The ATCC PDF lists 21.0 g PPLO Broth w/o CV from BD catalog 255420, 200.0 ml Horse Serum (not inactivated), 100.0 ml Fresh Baker's Yeast Extract from GIBCO 18180, and 700.0 ml distilled water. It also identifies the PPLO Broth w/o CV component as pH 7.8 and instructs adding the horse serum and GIBCO 18180 aseptically to the sterile PPLO/water basal medium.

The generated record still reflects the stale TOGO volume import: 700 ml water, 200 ml horse serum, and 100 ml yeast extract are represented as 700, 200, and 100 G_PER_L. Its maintained normalized input already has a later `RESOLVED_TOGO_M2226_PPLO_HORSE_YEAST_SCORE15` repair that changed those rows to ML_PER_L, added pH 7.8, added source references, grounded horse serum and yeast extract, and added two preparation steps.

Exact ignored-file searches across `data/normalized_yaml` and `data/merge_yaml` for `TOGO:M2226`, `M2226`, the ATCC document token `AD2BC56A0BA94572A40803C02D24D35A`, and `pplo_broth_without_cv_ph_7_8_with_horse_serum_not_inactivated_and_yeast_extract` found one maintained normalized YAML and this generated merged record.

## Evidence

- ATCC Medium 247 lists 21.0 g PPLO Broth w/o CV, 200.0 ml Horse Serum (not inactivated), 100.0 ml Fresh Baker's Yeast Extract, and 700.0 ml Distilled water.
- ATCC Medium 247 names BD 255420 and pH 7.8 for the commercial PPLO Broth w/o CV component.
- ATCC Medium 247 says to add horse serum and GIBCO 18180 aseptically to a sterile basal medium containing PPLO broth and water.
- `data/normalized_yaml/bacterial/pplo_broth_without_cv_ph_7_8_with_horse_serum_not_inactivated_and_yeast_extract.yaml` already carries a September 2026 repair with those ATCC values, corrected units, and ATCC/TOGO references.

## Completeness

The generated record is stale relative to both ATCC Medium 247 and the repaired normalized input. It preserves the old ml-to-G_PER_L unit errors, omits pH 7.8, lacks ATCC references, uses broader ungrounded serum and yeast-extract rows, and lacks the two-step sterile basal plus aseptic-addition preparation.

## Findings

1. Major: ATCC volume rows are still represented as mass concentrations: 700 ml water as 700 G_PER_L, 200 ml horse serum as 200 G_PER_L, and 100 ml Fresh Baker's Yeast Extract as 100 G_PER_L.
2. Major: The generated record omits the source pH 7.8 that is already present in the repaired maintained input.
3. Major: The generated record is stale relative to `data/normalized_yaml/bacterial/pplo_broth_without_cv_ph_7_8_with_horse_serum_not_inactivated_and_yeast_extract.yaml`, which already corrected the volume units, added ATCC references, and added preparation steps.
4. Minor: Horse serum and yeast extract groundings from the repaired maintained input have not propagated into the generated record.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/pplo_broth_without_cv_ph_7_8_with_horse_serum_not_inactivated_and_yeast_extract.yaml` from the already-repaired normalized input.
- Confirm the regenerated record retains `ML_PER_L` for the water, horse-serum, and yeast-extract rows, pH 7.8, ATCC references, and the aseptic serum/yeast addition step.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Run exact ignored-file searches for `TOGO:M2226`, `AD2BC56A0BA94572A40803C02D24D35A`, and the long PPLO slug before adding any new M2226 record.
- Spot-check the regenerated page to ensure it renders 21.0 g PPLO Broth w/o CV, 200 ml horse serum, 100 ml Fresh Baker's Yeast Extract, and 700 ml distilled water.

## Additional Notes

None found.

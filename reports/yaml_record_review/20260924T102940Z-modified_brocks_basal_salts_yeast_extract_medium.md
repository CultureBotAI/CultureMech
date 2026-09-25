# YAML Record Review: Modified Brock's Basal Salts-Yeast Extract Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_medium.yaml
- Started UTC: 2026-09-24T10:29:40Z
- Finished UTC: 2026-09-24T10:29:40Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009937` |
| Name | `modified_brocks_basal_salts_yeast_extract_medium` |
| Original name | `Modified Brock's Basal Salts-Yeast Extract Medium` |
| Category | `bacterial` |
| Medium source | TOGO `M544`, mirrored from JCM `542` |
| Maintained owners | `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_medium.yaml`; `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_medeium_b.yaml` |
| Generated status | Incorrectly merged output from base JCM 542 and variant JCM 585 |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_medium.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_medium.yaml --out /private/tmp/modified_brocks_basal_salts_yeast_extract_medium.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_brocks_basal_salts_yeast_extract_medium.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The top-level identity points to JCM Medium 542 via TOGO `M544`, but the ingredient list was overwritten with the 0.5 g/L yeast concentration from JCM Medium 585 / TOGO `M590`. JCM 585 is a variant that says to prepare Medium 542 with 0.5 g/L final yeast extract and pH 3.0; it is not identical to base JCM 542, which uses 5 g/L yeast extract and pH 9.0.

Exact `find data/normalized_yaml -name ...` searches, which cover ignored files, found same-named bacterial and fungal normalized files. The generated `merged_from` paths resolve to the bacterial owners listed in the Target section, while same-basename fungal files are separate records and were not part of this generated merge.

## Evidence

TOGO `M544` and the live JCM `GRMD=542` page agree on the base Medium 542 formulation. TOGO `M590` and live JCM `GRMD=585` agree that variant B is a pH 3.0 derivative of Medium 542 with only 0.5 g/L final yeast extract.

| Source claim | Record representation | Review |
| --- | --- | --- |
| JCM 542 has 5 g yeast extract in 1 L final volume and pH 9.0. | The generated canonical M544 record has `0.5 G_PER_L` yeast extract and no pH. | Wrong concentration and missing pH. |
| JCM 585 is prepared from Medium 542 with 0.5 g/L final yeast extract and pH 3.0. | The generated record lists `modified_brocks_basal_salts_yeast_extract_medeium_b` as a variant child and synonym but merges its lower yeast concentration into the canonical base row. | Unsupported variant merge. |
| Both source media adjust pH and JCM 542 instructs autoclaving and removal of precipitate if necessary. | No `preparation_steps` are present. | Incomplete preparation import. |
| Na2MoO4 x 2 H2O, MnCl2 x 4 H2O, ZnSO4 x 7 H2O, CuCl2 x 2 H2O, FeCl3 x 6 H2O, CoSO4 x 7 H2O, VOSO4 x H2O, and Na2B4O7 x 10 H2O are milligram-per-liter rows. | Their numeric source milligram amounts were stored directly as `G_PER_L`, for example `FeCl3 x 6H2O` is `2 G_PER_L` instead of 2 mg/L. | Unsupported unit conversion. |
| The main recipe contains 1 L distilled water. | Water is represented as `1 G_PER_L`. | Unsupported water-volume conversion. |

## Completeness

The generated record is incomplete for JCM 542 because pH 9.0, the precipitate-removal instruction, the 5 g/L yeast concentration, and the correct milligram trace concentrations are absent. It is incomplete for JCM 585 because pH 3.0 and the variant relationship are only partially represented and the B variant is merged into the base record.

Empty target-organism and growth-evidence fields were not treated as defects. TOGO `M544`, TOGO `M590`, JCM 542, and JCM 585 are medium formulation pages, not growth-evidence pages.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| blocker | JCM Medium 542 and its JCM 585 concentration/pH variant were merged into one generated record. | The generated record has M544 identity but uses the variant B `0.5 G_PER_L` yeast-extract concentration; base M544/JCM 542 requires 5 g/L yeast extract and pH 9.0, while M590/JCM 585 requires 0.5 g/L and pH 3.0. | `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_medium.yaml`; `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_medeium_b.yaml`; merge logic. |
| major | Milligram trace ingredients were promoted to gram-per-liter rows. | JCM 542 lists the trace salts as mg amounts in 1 L, but the record stores the same numeric values as `G_PER_L`. | Both bacterial normalized owners; TOGO unit conversion. |
| major | pH values and preparation steps are missing. | M544/JCM 542 has pH 9.0 and an autoclave/precipitate-removal instruction; M590/JCM 585 has pH 3.0. The generated record has no `ph_value` or `preparation_steps`. | Both bacterial normalized owners; TOGO comments import. |
| major | The water row is modeled as grams per liter. | Source water is 1 L; the record stores `Distilled water` as `1 G_PER_L`. | Both bacterial normalized owners; TOGO water import. |

## Recommended Edits

1. Stop merging `modified_brocks_basal_salts_yeast_extract_medeium_b` into the base JCM 542 generated record; keep JCM 585 / TOGO M590 as a concentration and pH variant.
2. Restore JCM 542's 5 g/L yeast extract and pH 9.0 in `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_medium.yaml`.
3. Restore JCM 585's 0.5 g/L yeast extract and pH 3.0 in `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_medeium_b.yaml`.
4. Convert all source milligram trace rows to true grams-per-liter values.
5. Preserve 1 L distilled water as volume, not `1 G_PER_L`, and import the pH-adjustment plus precipitate-removal comments as preparation steps.
6. Regenerate `data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_medium.yaml` after the normalized owners and merge relationship are corrected.

## Follow-up Checks

1. Run focused open-schema, strict, reference, and term validators on both bacterial normalized owners.
2. Regenerate merge outputs and re-run the same validators on the base and B-variant generated records.
3. Manually compare the regenerated base record against TOGO `M544` and JCM `GRMD=542`, checking 5 g/L yeast extract, pH 9.0, milligram trace rows, and the autoclave/precipitate-removal step.
4. Manually compare the regenerated B variant against TOGO `M590` and JCM `GRMD=585`, checking 0.5 g/L yeast extract and pH 3.0.

## Additional Notes

The TOGO APIs for `M544` and `M590` still resolve. JCM `GRMD=542` and `GRMD=585` also both resolve and support the base-versus-variant split.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.

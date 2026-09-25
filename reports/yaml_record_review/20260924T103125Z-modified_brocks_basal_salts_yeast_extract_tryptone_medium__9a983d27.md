# YAML Record Review: Modified Brock's Basal Salts-Yeast Extract-Tryptone Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_tryptone_medium__9a983d27.yaml
- Started UTC: 2026-09-24T10:31:25Z
- Finished UTC: 2026-09-24T10:31:25Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_tryptone_medium__9a983d27.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:010261` |
| Name | `modified_brocks_basal_salts_yeast_extract_tryptone_medium` |
| Original name | `Modified Brock's Basal Salts-Yeast Extract-Tryptone Medium` |
| Category | `bacterial` |
| Medium source | TOGO `M846`, mirrored from JCM `812` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_tryptone_medium.yaml` |
| Generated status | Generated copy of a flattened TOGO/JCM normalized record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_tryptone_medium__9a983d27.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_tryptone_medium__9a983d27.yaml --out /private/tmp/modified_brocks_basal_salts_yeast_extract_tryptone_medium__9a983d27.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_brocks_basal_salts_yeast_extract_tryptone_medium__9a983d27.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_tryptone_medium__9a983d27.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_tryptone_medium__9a983d27.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The medium identity is coherent: `CultureMech:010261` and `TOGO:M846` identify the liquid TOGO mirror of JCM Medium 812, Modified Brock's Basal Salts-Yeast Extract-Tryptone Medium.

An exact `find data/normalized_yaml -name modified_brocks_basal_salts_yeast_extract_tryptone_medium.yaml` search, which covers ignored files, found same-named bacterial and fungal normalized files. The generated `merged_from` entry resolves to the bacterial maintained owner listed in the Target section.

## Evidence

TOGO `M846` and the live JCM `GRMD=812` page agree that the liquid JCM 812 formulation uses Medium No. 542 with 3 g/L final yeast extract, 3 g/L tryptone, and pH 7.0.

| Source claim | Record representation | Review |
| --- | --- | --- |
| JCM 812 uses Medium 542 with 3 g/L final yeast extract and 3 g/L tryptone. | Both rows are present at `3 G_PER_L`. | Supported. |
| JCM 812 adjusts pH to 7.0. | No `ph_value` is present. | Missing pH. |
| Medium 542's Na2MoO4 x 2 H2O, MnCl2 x 4 H2O, ZnSO4 x 7 H2O, CuCl2 x 2 H2O, FeCl3 x 6 H2O, CoSO4 x 7 H2O, VOSO4 x H2O, and Na2B4O7 x 10 H2O rows are milligram-per-liter rows inherited by JCM 812. | The numeric source milligram amounts were stored directly as `G_PER_L`, for example `MnCl2 x 4H2O` is `1.8 G_PER_L` instead of 1.8 mg/L. | Unsupported unit conversion. |
| Medium 542 has 1 L distilled water and an autoclave/precipitate-removal instruction inherited by JCM 812. | Water is `1 G_PER_L` and no `preparation_steps` are present. | Incomplete source representation. |

## Completeness

The generated record is incomplete because it drops pH 7.0 and inherited preparation text from the source comments. It also overstates trace salts by storing milligram amounts as grams per liter.

Empty target-organism and growth-evidence fields were not treated as defects. TOGO `M846` and JCM 812 are medium formulation pages, not growth-evidence pages.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Milligram trace ingredients were promoted to gram-per-liter rows. | JCM 812 inherits the Medium 542 trace rows as milligram amounts, but the record stores values such as `2 G_PER_L` FeCl3 x 6 H2O and `4.5 G_PER_L` Na2B4O7 x 10 H2O. | `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_tryptone_medium.yaml`; TOGO unit conversion. |
| major | pH 7.0 and preparation comments are missing. | TOGO carries the JCM 812 pH 7.0 comment and the inherited Medium 542 autoclave/precipitate-removal comment; the generated record has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_tryptone_medium.yaml`; TOGO comments import. |
| major | The water row is modeled as grams per liter. | Source water is 1 L; the record stores `Distilled water` as `1 G_PER_L`. | `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_tryptone_medium.yaml`; TOGO water import. |

## Recommended Edits

1. Convert the inherited source milligram trace rows in `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_tryptone_medium.yaml` to true grams-per-liter values.
2. Add pH 7.0 and preserve the source pH, autoclave, and precipitate-removal comments as structured preparation steps.
3. Preserve 1 L distilled water as volume, not `1 G_PER_L`.
4. Regenerate `data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_tryptone_medium__9a983d27.yaml` after the normalized owner is corrected.

## Follow-up Checks

1. Run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_tryptone_medium.yaml`.
2. Regenerate `data/merge_yaml/merged/modified_brocks_basal_salts_yeast_extract_tryptone_medium__9a983d27.yaml` and re-run the same validators on the generated record.
3. Manually compare the regenerated record against TOGO `M846` and JCM `GRMD=812`, checking pH 7.0, 3 g/L yeast extract, 3 g/L tryptone, inherited milligram salts, and inherited Medium 542 autoclaving instructions.

## Additional Notes

The TOGO API for `M846` and the JCM `GRMD=812` page still resolve.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.

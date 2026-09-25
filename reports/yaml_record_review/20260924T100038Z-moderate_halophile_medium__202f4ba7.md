# YAML Record Review: Moderate Halophile Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/moderate_halophile_medium__202f4ba7.yaml
- Started UTC: 2026-09-24T10:00:38Z
- Finished UTC: 2026-09-24T10:00:38Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/moderate_halophile_medium__202f4ba7.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:010005` |
| Name | `moderate_halophile_medium` |
| Original name | `Moderate Halophile Medium` |
| Category | `bacterial` |
| Physical state | `SOLID_AGAR` |
| Medium source | TOGO `M606`; original source JCM `JCM_M599-2` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M606_Moderate_Halophile_Medium.yaml` |
| Generated status | Generated merge output from one normalized TOGO record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/moderate_halophile_medium__202f4ba7.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/moderate_halophile_medium__202f4ba7.yaml --out /private/tmp/moderate_halophile_medium__202f4ba7.strict.tsv --workers 1 --quiet` | Passed; `/private/tmp/moderate_halophile_medium__202f4ba7.strict.tsv` contained only the header line, so no strict errors were reported. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/moderate_halophile_medium__202f4ba7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/moderate_halophile_medium__202f4ba7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent. `CultureMech:010005`, `TOGO:M606`, and the JCM `JCM_M599-2` provenance all identify the solid-agar Moderate Halophile Medium variant from JCM medium 599.

The inspected source supports `SOLID_AGAR`: TOGO and JCM both include the instruction to add 20.0 g/L agar for solid medium, and the generated record carries `agar` at `20 G_PER_L`.

Hydrated sulfate, chloride, bromide, bicarbonate, glucose, and agar ingredient groundings are plausible. Yeast extract and Proteose peptone No. 3 are undefined materials and are reasonably ungrounded.

## Evidence

TOGO `M606` and the live JCM `GRMD=599` page support the same formula:

| Source claim | Record representation | Review |
| --- | --- | --- |
| Add components to distilled water and bring volume to 1.0 L. | `Distilled water` is `1 G_PER_L`. | Unsupported unit: a final-volume instruction is not a 1 g/L water concentration. |
| Per 1 L: 9.6 g MgSO4 x 7H2O, 10 g yeast extract, 81 g NaCl, 0.36 g CaCl2 x 2H2O, 7 g MgCl2 x 6H2O, 2 g KCl, 0.06 g NaHCO3, 0.026 g NaBr, 1 g glucose, and 5 g Proteose peptone No. 3. | All 10 non-water base rows are present with matching numeric `G_PER_L` amounts. | Supported for a 1 L final volume. |
| For solid medium, add 20.0 g/L agar. | The record has `agar` `20 G_PER_L` and `physical_state: SOLID_AGAR`. | Supported. |
| Adjust pH to 7.0-7.2. | No field or preparation step records pH 7.0-7.2. | Incomplete. |
| Unless otherwise stated, JCM sterilizes media by autoclaving at 121 C for 15 min. | No autoclaving step is present. | Incomplete. |

## Completeness

The generated record has the full solid ingredient set from TOGO `M606`, including the agar that distinguishes `JCM_M599-2` from the liquid base recipe.

The pH range, final-volume water semantics, and JCM autoclave instruction are missing or malformed. Empty target-organism slots are not defects for this JCM recipe import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Distilled water is represented with the wrong unit. | TOGO and JCM say to bring the formula to 1.0 L with distilled water; the record stores `Distilled water` as `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M606_Moderate_Halophile_Medium.yaml`; TOGO volume-unit normalization. |
| major | The pH 7.0-7.2 range is missing. | TOGO `M606` exposes `"ph": "7.0-7.2"` and JCM 599 instructs users to adjust pH to 7.0-7.2; the record has no corresponding pH field or preparation step. | `data/normalized_yaml/bacterial/TOGO_M606_Moderate_Halophile_Medium.yaml`; TOGO pH import. |
| major | JCM sterilization conditions are missing. | The live JCM 599 page says to autoclave at 121 C for 15 min unless otherwise stated; the generated record has no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M606_Moderate_Halophile_Medium.yaml`; JCM/TOGO preparation import. |

## Recommended Edits

1. Correct the `Distilled water` representation in `data/normalized_yaml/bacterial/TOGO_M606_Moderate_Halophile_Medium.yaml` so the source final volume of 1.0 L is not encoded as `1 G_PER_L`.
2. Import the pH 7.0-7.2 and 121 C for 15 min autoclave instructions into scoped preparation fields.
3. Keep agar as a supported 20 g/L solidifying component for the `JCM_M599-2` solid variant.
4. Regenerate `data/merge_yaml/merged/moderate_halophile_medium__202f4ba7.yaml` from the corrected normalized source.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/TOGO_M606_Moderate_Halophile_Medium.yaml` and the regenerated merge output.
2. Manually compare the regenerated record against TOGO `M606` and JCM `GRMD=599`, checking every ingredient amount, the 20 g/L agar row, the final 1.0 L water instruction, pH 7.0-7.2, and the JCM autoclave condition.

## Additional Notes

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.

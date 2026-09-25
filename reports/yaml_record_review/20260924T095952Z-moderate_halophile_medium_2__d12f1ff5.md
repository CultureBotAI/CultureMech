# YAML Record Review: Moderate Halophile Medium 2

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/moderate_halophile_medium_2__d12f1ff5.yaml
- Started UTC: 2026-09-24T09:59:52Z
- Finished UTC: 2026-09-24T09:59:52Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/moderate_halophile_medium_2__d12f1ff5.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007847` |
| Name | `moderate_halophile_medium_2` |
| Original name | `Moderate Halophile Medium 2` |
| Category | `bacterial` |
| Physical state | `SOLID_AGAR` |
| Medium source | TOGO `M1311`; original source JCM `JCM_M1220-2` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M1311_Moderate_Halophile_Medium_2.yaml` |
| Generated status | Generated merge output from one normalized TOGO record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/moderate_halophile_medium_2__d12f1ff5.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/moderate_halophile_medium_2__d12f1ff5.yaml --out /private/tmp/moderate_halophile_medium_2__d12f1ff5.strict.tsv --workers 1 --quiet` | Passed; `/private/tmp/moderate_halophile_medium_2__d12f1ff5.strict.tsv` contained only the header line, so no strict errors were reported. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/moderate_halophile_medium_2__d12f1ff5.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/moderate_halophile_medium_2__d12f1ff5.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The generated record resolves to the TOGO `M1311` solid-agar variant of JCM medium `1220`, labeled `JCM_M1220-2` in TOGO. Its `SOLID_AGAR` state is supported because TOGO includes the JCM instruction to add agar at 20.0 g/L for solid medium, and the generated ingredient list contains a 20 g/L agar row.

The non-water ingredient groundings are coherent where exact compounds are groundable. Hydrate-sensitive salts such as MgSO4 x 7H2O, MgCl2 x 6H2O, and CaCl2 x 2H2O are grounded to the corresponding hydrate CHEBI terms. Yeast extract, malt extract, and peptone are undefined materials and are reasonably left without exact CHEBI terms.

The solvent row has the same unit defect as the liquid TOGO split: a source final volume of 1 L was converted into `1 G_PER_L` water.

## Evidence

TOGO `M1311` and the live JCM `GRMD=1220` page support the solid formulation:

| Source claim | Record representation | Review |
| --- | --- | --- |
| Add components to distilled water and bring volume to 1.0 L. | `Distilled water` is `1 G_PER_L`. | Unsupported unit: a final-volume instruction is not a 1 g/L water concentration. |
| Per 1 L: 9 g MgSO4 x 7H2O, 3 g yeast extract, 100 g NaCl, 0.2 g CaCl2 x 2H2O, 13 g MgCl2 x 6H2O, 1.3 g KCl, 0.05 g NaHCO3, 0.15 g NaBr, 10 g glucose, 3 g malt extract, and 5 g peptone. | All 11 non-water base rows are present with matching numeric `G_PER_L` amounts. | Supported for a 1 L final volume. |
| For solid medium, add 20.0 g/L agar. | The record has `agar` `20 G_PER_L` and `physical_state: SOLID_AGAR`. | Supported. |
| Adjust pH to 7.0-7.2. | No field or preparation step records pH 7.0-7.2. | Incomplete. |
| Unless otherwise stated, JCM sterilizes media by autoclaving at 121 C for 15 min. | No autoclaving step is present. | Incomplete. |

## Completeness

The solid formula has all 12 non-water rows from TOGO `M1311`, including the agar addition that distinguishes it from TOGO `M1310`.

The generated record is incomplete because it drops the pH 7.0-7.2 and JCM autoclaving instructions. The final-volume water row is also dimensionally wrong.

Empty target-organism fields were not treated as defects. The inspected JCM and TOGO source pages are medium recipes rather than organism-specific growth records.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Distilled water is represented with the wrong unit. | The source says to bring the formula to 1.0 L with distilled water; the record stores `Distilled water` as `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1311_Moderate_Halophile_Medium_2.yaml`; TOGO volume-unit normalization. |
| major | The pH 7.0-7.2 range is missing. | TOGO `M1311` retains the JCM comment `Adjust pH to 7.0-7.2`; no field or preparation step in the generated record captures it. | `data/normalized_yaml/bacterial/TOGO_M1311_Moderate_Halophile_Medium_2.yaml`; TOGO comment import. |
| major | JCM sterilization conditions are missing. | The live JCM 1220 page says to autoclave at 121 C for 15 min unless otherwise stated; the generated record has no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M1311_Moderate_Halophile_Medium_2.yaml`; JCM/TOGO preparation import. |

## Recommended Edits

1. Correct the `Distilled water` row in `data/normalized_yaml/bacterial/TOGO_M1311_Moderate_Halophile_Medium_2.yaml` so the source's 1.0 L final volume is represented as volume/final-volume context, not `1 G_PER_L`.
2. Import the pH 7.0-7.2 and 121 C for 15 min autoclave instructions into scoped preparation fields.
3. Keep agar as a supported 20 g/L solidifying component for this `SOLID_AGAR` variant.
4. Regenerate `data/merge_yaml/merged/moderate_halophile_medium_2__d12f1ff5.yaml` from the corrected normalized TOGO owner.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/TOGO_M1311_Moderate_Halophile_Medium_2.yaml` and the regenerated merge output.
2. Manually compare the regenerated record against TOGO `M1311` and JCM `GRMD=1220`, checking all base ingredient amounts, the 20 g/L agar row, the final 1.0 L water instruction, pH 7.0-7.2, and the JCM autoclave condition.

## Additional Notes

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.

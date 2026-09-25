# YAML Record Review: Modified M63 medium with glucose and 2.5 M NaCl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_m63_medium_with_glucose_and_2_5_m_nacl.yaml
- Started UTC: 2026-09-24T11:39:34Z
- Finished UTC: 2026-09-24T11:39:34Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_m63_medium_with_glucose_and_2_5_m_nacl.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:007428` |
| Name | `modified_m63_medium_with_glucose_and_2_5_m_nacl` |
| Source identity | `MEDIADB:7` |
| Category | `bacterial` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_m63_medium_with_glucose_and_2_5_m_nacl.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` by merging four MediaDB M63 salinity variants |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_m63_medium_with_glucose_and_2_5_m_nacl.yaml` reported `No issues found`. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_m63_medium_with_glucose_and_2_5_m_nacl.yaml --out /private/tmp/modified_m63_medium_with_glucose_and_2_5_m_nacl.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_m63_medium_with_glucose_and_2_5_m_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_m63_medium_with_glucose_and_2_5_m_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record is intended to denote MediaDB medium 7, "Modified M63 medium with glucose and 2.5 M NaCl". Its ID, slug, and `MEDIADB:7` source CURIE agree on that identity, but its ingredient list encodes the 0.6 M variant instead.

MediaDB 4, 5, 6, and 7 are distinct glucose M63 salt variants:

| MediaDB ID | Variant | Source NaCl |
|---|---|---|
| 4 | 0.6 M NaCl | 600.0 mM |
| 5 | 0.75 M NaCl | 750.0 mM |
| 6 | 1.5 M NaCl | 1500.0 mM |
| 7 | 2.5 M NaCl | 2500.0 mM |

The generated `MEDIADB:7` record carries `Sodium chloride` at 600.0 mM, which is the MediaDB 4 amount. The normalized MediaDB 7 source has the correct 2500.0 mM amount, so this wrong formula was introduced when `merge_recipes.py` collapsed the four salinity variants into one generated record and turned the other MediaDB records into synonyms.

## Evidence

The inspected MediaDB tab-delimited endpoints support each source formulation: medium 4 has 600.0 mM sodium chloride, medium 5 has 750.0 mM, medium 6 has 1500.0 mM, and medium 7 has 2500.0 mM. D-glucose, potassium hydroxide, potassium dibasic phosphate, magnesium sulfate, ferrous sulfate, and ammonium sulfate are unchanged across the four variants.

The inspected MediaDB pages for all four glucose media report seven compounds, two `Chromohalobacter salexigens` strains, one Rodriguez-moya et al. 2010 source, and two linked growth-data rows per medium. The two growth-data rows attached to MediaDB 7 are:

| MediaDB growth row | Organism | Growth rate | pH | Temperature |
|---|---|---|---|---|
| 7 | `Chromohalobacter salexigens` CHR61 | 0.061 1/h | 7.2 | 37.0 |
| 19 | `Chromohalobacter salexigens` CHR95 | 0.007 1/h | 7.2 | 37.0 |

The MediaDB pages inspected for MediaDB 7 did not describe pH adjustment, 0.22 um filter sterilization, or a preparation order, so the generic `ADJUST_PH` and `FILTER_STERILIZE` steps are unsupported.

## Completeness

The generated record is incomplete because it keeps one formula for four MediaDB formulations that differ in sodium chloride concentration.

Target-organism coverage is also incomplete. MediaDB 7 links two 2.5 M `Chromohalobacter salexigens` growth rows, but an exact gitignore-independent search over the generated YAML and all four normalized M63 glucose salinity-variant YAML sources found no `target_organisms`, `growth_rate`, MediaDB growth URL, or `Chromohalobacter` entry.

Empty optional narrative slots are not defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | Four distinct MediaDB glucose-salt variants were merged into one generated recipe with the wrong NaCl concentration for the asserted identity. | `MEDIADB:7` is the 2.5 M NaCl variant and its normalized source has 2500.0 mM sodium chloride, but the generated `MEDIADB:7` record has 600.0 mM NaCl from `MEDIADB:4` and treats `MEDIADB:4`, `MEDIADB:5`, and `MEDIADB:6` as synonyms. | Fix the variant-aware merge logic in `scripts/merge_recipes.py`, then regenerate `data/merge_yaml/merged/` so MediaDB 4, 5, 6, and 7 remain separate salinity variants. |
| major | The record contains unsupported generic preparation steps. | MediaDB 7 exposes the seven-compound formula, source, two organisms, and two growth-data rows, but no pH-adjustment instruction or 0.22 um filtration claim. | Remove or refine the generated `ADJUST_PH` and `FILTER_STERILIZE` steps in `data/normalized_yaml/bacterial/modified_m63_medium_with_glucose_and_2_5_m_nacl.yaml` and the sibling MediaDB M63 glucose normalized records, or in the MediaDB importer template if the placeholder is systemic. |
| major | The record omits two MediaDB growth rows for the 2.5 M glucose variant. | MediaDB 7 links growthdata 7 and 19; neither the generated record nor the four normalized M63 glucose salinity variants contain `target_organisms` or growth-rate entries. | Add strain-scoped target-organism entries to `data/normalized_yaml/bacterial/modified_m63_medium_with_glucose_and_2_5_m_nacl.yaml` once the salinity variants are no longer collapsed. |

## Recommended Edits

1. Change the merge fingerprint or variant handling so MediaDB 4, 5, 6, and 7 do not collapse; they differ in sodium chloride concentration and should remain linked only by `SALINITY_VARIANT` relationships.
2. Regenerate `data/merge_yaml/merged/` and confirm the MediaDB 7 generated recipe contains 2500.0 mM sodium chloride, not 600.0 mM.
3. Replace or remove the unsupported generic preparation steps on the four maintained M63 glucose salinity-variant sources.
4. Add `target_organisms` entries for MediaDB growthdata 7 and 19 to the maintained 2.5 M glucose normalized source.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on the regenerated MediaDB 7 YAML.
- Inspect the regenerated MediaDB 4, 5, 6, and 7 YAML files and confirm their NaCl values are 600.0, 750.0, 1500.0, and 2500.0 mM, respectively.
- Confirm `merged_from` no longer lists all four M63 glucose salinity variants in any single generated artifact.
- Re-open MediaDB growthdata 7 and 19 and confirm the target-organism rows remain scoped to the 2.5 M glucose variant before marking the growth annotations complete.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
- The exact gitignore-independent missing-growth search covered `data/merge_yaml/merged/modified_m63_medium_with_glucose_and_2_5_m_nacl.yaml` plus the normalized MediaDB 4, 5, 6, and 7 YAML files under `data/normalized_yaml/bacterial/`.

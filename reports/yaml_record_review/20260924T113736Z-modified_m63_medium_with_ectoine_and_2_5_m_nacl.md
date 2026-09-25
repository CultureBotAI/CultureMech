# YAML Record Review: Modified m63 medium with ectoine and 2.5 m nacl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_m63_medium_with_ectoine_and_2_5_m_nacl.yaml
- Started UTC: 2026-09-24T11:37:36Z
- Finished UTC: 2026-09-24T11:37:43Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_m63_medium_with_ectoine_and_2_5_m_nacl.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:007007` |
| Name | `modified_m63_medium_with_ectoine_and_2_5_m_nacl` |
| Source identity | `MEDIADB:11` |
| Category | `bacterial` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_m63_medium_with_ectoine_and_2_5_m_nacl.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` by merging four MediaDB M63 salinity variants |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_m63_medium_with_ectoine_and_2_5_m_nacl.yaml` reported `No issues found`. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_m63_medium_with_ectoine_and_2_5_m_nacl.yaml --out /private/tmp/modified_m63_medium_with_ectoine_and_2_5_m_nacl.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_m63_medium_with_ectoine_and_2_5_m_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_m63_medium_with_ectoine_and_2_5_m_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record is intended to denote MediaDB medium 11, "Modified m63 medium with ectoine and 2.5 m nacl". Its generated source CURIE and label agree with that identity, but its ingredient vector does not.

MediaDB 8, 9, 10, and 11 are four distinct salt variants with the same six non-NaCl ingredients and different sodium chloride concentrations:

| MediaDB ID | Variant | Source NaCl |
|---|---|---|
| 8 | 0.6 m nacl | 600.0 mM |
| 9 | 0.75 m nacl | 750.0 mM |
| 10 | 1.5 m nacl | 1500.0 mM |
| 11 | 2.5 m nacl | 2500.0 mM |

The generated `MEDIADB:11` record encodes `Sodium chloride` at 600.0 mM, which belongs to MediaDB 8, and lists the other MediaDB source identities as synonyms of the 2.5 M record. The four maintained normalized records still retain their distinct MediaDB IDs and NaCl concentrations; the identity defect is introduced by `merge_recipes.py` when it collapses salinity variants into one generated recipe.

## Evidence

The inspected MediaDB tab-delimited endpoints support each normalized source formula: medium 8 has 600.0 mM sodium chloride, medium 9 has 750.0 mM, medium 10 has 1500.0 mM, and medium 11 has 2500.0 mM. Ectoine, potassium hydroxide, potassium dibasic phosphate, magnesium sulfate, ferrous sulfate, and ammonium sulfate are unchanged across the four variants.

The inspected MediaDB pages for all four medium IDs report seven compounds, four `Chromohalobacter salexigens` strains, one Rodriguez-moya et al. 2010 source, and four linked growth-data rows per medium. The four growth-data rows attached to MediaDB 11 are:

| MediaDB growth row | Organism | Growth rate | pH | Temperature |
|---|---|---|---|---|
| 31 | `Chromohalobacter salexigens` CHR161 | 0.029 1/h | 7.2 | 37.0 |
| 39 | `Chromohalobacter salexigens` CHR183 | 0.016 1/h | 7.2 | 37.0 |
| 11 | `Chromohalobacter salexigens` CHR61 | 0.032 1/h | 7.2 | 37.0 |
| 23 | `Chromohalobacter salexigens` CHR95 | 0.02 1/h | 7.2 | 37.0 |

The MediaDB pages inspected for MediaDB 11 did not describe pH adjustment, 0.22 um filter sterilization, or a preparation order, so the generic `ADJUST_PH` and `FILTER_STERILIZE` steps are unsupported.

## Completeness

The generated record is incomplete because it lost the 0.75 M, 1.5 M, and 2.5 M formulae as records and kept the 0.6 M formula under the 2.5 M identity.

Target-organism coverage is also incomplete. MediaDB 11 links four 2.5 M `Chromohalobacter salexigens` growth rows, but an exact gitignore-independent search over the generated YAML and all four normalized M63 salinity-variant YAML sources found no `target_organisms`, `growth_rate`, MediaDB growth URL, or `Chromohalobacter` entry.

Empty optional narrative slots are not defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | Four distinct MediaDB salt variants were merged into one generated recipe with the wrong NaCl concentration for the asserted identity. | `MEDIADB:11` is the 2.5 M NaCl variant and its normalized source has 2500.0 mM sodium chloride, but the generated `MEDIADB:11` record has 600.0 mM NaCl from `MEDIADB:8` and treats `MEDIADB:8`, `MEDIADB:9`, and `MEDIADB:10` as synonyms. | Fix the variant-aware merge logic in `scripts/merge_recipes.py`, then regenerate `data/merge_yaml/merged/` so MediaDB 8, 9, 10, and 11 remain separate salinity variants. |
| major | The record contains unsupported generic preparation steps. | MediaDB 11 exposes the seven-compound formula, source, four organisms, and four growth-data rows, but no pH-adjustment instruction or 0.22 um filtration claim. | Remove or refine the generated `ADJUST_PH` and `FILTER_STERILIZE` steps in `data/normalized_yaml/bacterial/modified_m63_medium_with_ectoine_and_2_5_m_nacl.yaml` and the sibling MediaDB M63 normalized records, or in the MediaDB importer template if the placeholder is systemic. |
| major | The record omits four MediaDB growth rows for the 2.5 M variant. | MediaDB 11 links growthdata 31, 39, 11, and 23; neither the generated record nor the four normalized M63 salinity variants contain `target_organisms` or growth-rate entries. | Add strain-scoped target-organism entries to `data/normalized_yaml/bacterial/modified_m63_medium_with_ectoine_and_2_5_m_nacl.yaml` once the salinity variants are no longer collapsed. |

## Recommended Edits

1. Change the merge fingerprint or variant handling so MediaDB 8, 9, 10, and 11 do not collapse; they differ in sodium chloride concentration and should remain linked only by `SALINITY_VARIANT` relationships.
2. Regenerate `data/merge_yaml/merged/` and confirm the MediaDB 11 generated recipe contains 2500.0 mM sodium chloride, not 600.0 mM.
3. Replace or remove the unsupported generic preparation steps on the four maintained M63 salinity-variant sources.
4. Add `target_organisms` entries for MediaDB growthdata 31, 39, 11, and 23 to the maintained 2.5 M normalized source.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on the regenerated MediaDB 11 YAML.
- Inspect the regenerated MediaDB 8, 9, 10, and 11 YAML files and confirm their NaCl values are 600.0, 750.0, 1500.0, and 2500.0 mM, respectively.
- Confirm `merged_from` no longer lists all four M63 salinity variants in any single generated artifact.
- Re-open MediaDB growthdata 31, 39, 11, and 23 and confirm the target-organism rows remain scoped to the 2.5 M variant before marking the growth annotations complete.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
- The exact gitignore-independent missing-growth search covered `data/merge_yaml/merged/modified_m63_medium_with_ectoine_and_2_5_m_nacl.yaml` plus the normalized MediaDB 8, 9, 10, and 11 YAML files under `data/normalized_yaml/bacterial/`.

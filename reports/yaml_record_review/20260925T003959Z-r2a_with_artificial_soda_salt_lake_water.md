# YAML Record Review: R2A WITH ARTIFICIAL SODA-SALT LAKE WATER

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/r2a_with_artificial_soda_salt_lake_water.yaml
- Started UTC: 2026-09-25T00:39:59Z
- Finished UTC: 2026-09-25T00:40:38Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Generated record | data/merge_yaml/merged/r2a_with_artificial_soda_salt_lake_water.yaml |
| Maintained owner | data/normalized_yaml/bacterial/r2a_with_artificial_soda_salt_lake_water.yaml |
| Stable ID | CultureMech:001197 |
| Name | r2a_with_artificial_soda_salt_lake_water |
| Original name | R2A WITH ARTIFICIAL SODA-SALT LAKE WATER |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | SOLID_AGAR |
| pH | 9.0 |
| Source grounding | mediadive.medium:1719, DSMZ Medium 1719 |
| Merge fingerprint | 2809fd86be52e6000d923fd69e01067a3db4fbbf7a9e9a98a6b8eaaf76e9cbe1 |
| Merged from | r2a_with_artificial_soda_salt_lake_water |

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/r2a_with_artificial_soda_salt_lake_water.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/r2a_with_artificial_soda_salt_lake_water.yaml --out /private/tmp/r2a_with_artificial_soda_salt_lake_water.strict.tsv --workers 1 --quiet` | Passed. `/private/tmp/r2a_with_artificial_soda_salt_lake_water.strict.tsv` had one line, the header only, so 0 strict errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/r2a_with_artificial_soda_salt_lake_water.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused check reported 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/r2a_with_artificial_soda_salt_lake_water.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record correctly identifies DSMZ Medium 1719, R2A WITH ARTIFICIAL SODA-SALT LAKE WATER. Its nine soda-salt ingredients and pH 9.0 agree with the source identity.

The inherited R2A component is represented incorrectly. DSMZ 1719 says to add 3 g/L R2A, referring to Medium 830, but the generated CultureMech record inlines the full Medium 830 ingredient list at normal 1 L R2A concentrations, including 15 g/L agar and the Medium 830 pH 7.2 preparation note. Those full-strength rows do not belong in DSMZ 1719.

## Evidence

- Supported: DSMZ Medium 1719 and MediaDive medium 1719 list NaCl, Na2SO4, MgCl2 x 6 H2O, CaCl2 x 2 H2O, KCl, KBr, H3BO3, SrCl2 x 6 H2O, and NaF at the generated soda-salt concentrations.
- Supported: DSMZ Medium 1719 supports pH 9.0 and autoclaving the main solution before adding sterile sodium carbonate.
- Unsupported by omission: DSMZ Medium 1719 lists 900 ml distilled water in the main solution; the generated record has no water row.
- Unsupported by omission: DSMZ Medium 1719 adds 100 ml sterile Na2CO3 solution at 50 g/L; the generated record has the instruction text only and no sodium carbonate component or nested solution.
- Unsupported by flattening: DSMZ Medium 1719 adds 3 g/L R2A, not the full unscaled DSMZ Medium 830 ingredient list or the pH 7.2 DSMZ 830 preparation note.

## Completeness

The generated record is incomplete for DSMZ 1719 because the base solution make-up water and sodium carbonate supplement are missing as structured components. It is also over-complete in the wrong way because full DSMZ 830 base ingredients are flattened into the top-level medium rather than represented as a 3 g/L R2A addition.

The ignored-inclusive exact search for `mediadive.medium:1719`, `DSMZ_Medium1719`, and `DSMZ Medium: 1719` covered `data/normalized_yaml`, `data/merge_yaml`, `scripts`, and `src`. It found only this maintained owner/generated record and source-index rows for DSMZ 1719.

Empty optional fields are not otherwise defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The 900 ml main-solution water and 100 ml sterile sodium carbonate supplement are missing as components. | DSMZ 1719 lists 900 ml distilled water, then adds 100 ml sterile Na2CO3 solution at 50 g/L; the generated record has no water ingredient and no sodium carbonate ingredient or solution. | data/normalized_yaml/bacterial/r2a_with_artificial_soda_salt_lake_water.yaml |
| Major | DSMZ Medium 830 was flattened incorrectly. | The source says `Add 3 g / L R2A (M. 830)`; the generated record instead embeds normal full-strength DSMZ 830 yeast extract, peptone, casamino acids, glucose, starch, sodium pyruvate, K2HPO4, MgSO4 x 7 H2O, and agar rows. | data/normalized_yaml/bacterial/r2a_with_artificial_soda_salt_lake_water.yaml |
| Minor | A DSMZ 830 preparation step conflicts with the DSMZ 1719 pH 9.0 recipe. | The reviewed record has the correct pH 9.0 and also inherits the DSMZ 830 instruction about final pH 7.2, agar addition, and 121 C autoclaving. | data/normalized_yaml/bacterial/r2a_with_artificial_soda_salt_lake_water.yaml |

## Recommended Edits

1. Add the 900 ml distilled-water row to the maintained DSMZ 1719 owner.
2. Add the 100 ml sterile Na2CO3 50 g/L supplement as a nested or structured solution, with the aseptic-addition preparation step attached to that supplement.
3. Replace the flattened DSMZ 830 ingredient rows with a 3 g/L R2A addition or a parent/media solution link to `mediadive.medium:830`, whichever pattern the R2A repair pass establishes for powder-like source-medium additions.
4. Remove the inherited DSMZ 830 pH 7.2 preparation step from DSMZ 1719.
5. Regenerate merged YAML and indexes.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on the regenerated DSMZ 1719 record.
- Run an ignored-inclusive exact search for `mediadive.medium:1719` and `DSMZ_Medium1719` under `data/normalized_yaml` and `data/merge_yaml` to confirm no duplicate DSMZ 1719 owner was introduced.
- Inspect the regenerated recipe and verify that it contains the nine soda-salt rows, 900 ml water, the 3 g/L R2A addition, the 100 ml sodium carbonate supplement, autoclaving before sodium carbonate addition, and only pH 9.0.

## Additional Notes

None found.

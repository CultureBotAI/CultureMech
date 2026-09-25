# YAML Record Review: R2A MEDIUM (MICROAEROBIC)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/r2a_medium_microaerobic.yaml
- Started UTC: 2026-09-25T00:32:13Z
- Finished UTC: 2026-09-25T00:32:51Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Generated record | data/merge_yaml/merged/r2a_medium_microaerobic.yaml |
| Maintained owner | data/normalized_yaml/bacterial/r2a_medium_microaerobic.yaml |
| Stable ID | CultureMech:001988 |
| Name | r2a_medium_microaerobic |
| Original name | R2A MEDIUM (MICROAEROBIC) |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| pH range | 5.0-5.5 |
| Source grounding | mediadive.medium:830d, DSMZ Medium 830d |
| Merge fingerprint | 641806d242f78dbc8bd763be3de0945c2d60fdb144d61d4d092c69eacdec6cc7 |
| Merged from | r2a_medium_microaerobic |

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/r2a_medium_microaerobic.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/r2a_medium_microaerobic.yaml --out /private/tmp/r2a_medium_microaerobic.strict.tsv --workers 1 --quiet` | Passed. `/private/tmp/r2a_medium_microaerobic.strict.tsv` had one line, the header only, so 0 strict errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/r2a_medium_microaerobic.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused check reported 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/r2a_medium_microaerobic.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record denotes the right DSMZ source: Medium 830d, R2A MEDIUM (MICROAEROBIC). Its `LIQUID` state, pH range 5.0-5.5, lack of agar, and sparging/headspace protocol distinguish it correctly from the solid aerobic DSMZ 830 R2A base recipe.

The CHEBI groundings for glucose, starch, sodium pyruvate, K2HPO4, and MgSO4 x 7 H2O are appropriate. Yeast extract, BD Difco no. 3 proteose peptone, and casamino acids are undefined products and are correctly left without single-compound CHEBI mappings.

## Evidence

- Supported: DSMZ Medium 830d and MediaDive 830d list yeast extract, BD Difco no. 3 proteose peptone, casamino acids, glucose, soluble starch, Na-pyruvate, K2HPO4, and MgSO4 x 7 H2O at exactly the generated concentrations.
- Supported: DSMZ Medium 830d lists final volume 1000 ml, final pH 5.0-5.5, and 1000 ml distilled water; MediaDive likewise exposes a 1000 ml distilled-water row.
- Supported: the generated preparation steps preserve the two source instructions: sparge with 80% N2 / 20% CO2, fill and seal vials before autoclaving, adjust the autoclaved medium to pH 5.0-5.5 with sterile sodium carbonate stock, and add sterile air before inoculation for 5% O2 in the headspace.
- Unsupported by omission: the reviewed MediaRecipe omits the 1000 ml distilled-water ingredient even though the source and the generated `mediadive_1690_Main_sol_830d.yaml` solution both contain it.

## Completeness

The formula, pH, and gas-handling procedure are otherwise complete for DSMZ Medium 830d. The only material recipe gap is the missing 1000 ml final-volume water row.

An ignored-inclusive exact search for `mediadive.medium:830d` and `DSMZ_Medium830d` under `data/normalized_yaml`, `data/merge_yaml`, `scripts`, and `src` found only this medium owner/generated record, its source indexes, and the generated `mediadive_1690_Main_sol_830d.yaml` solution artifact. A looser bare `830d` search also matched unrelated merge-fingerprint strings and was not used for uniqueness.

Empty optional fields are not defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The MediaRecipe omits the final-volume water component from DSMZ 830d. | DSMZ Medium 830d and MediaDive 830d both list `Distilled water` at 1000 ml; `data/normalized_yaml/bacterial/r2a_medium_microaerobic.yaml` and its generated copy contain only the eight non-water solutes. | data/normalized_yaml/bacterial/r2a_medium_microaerobic.yaml |
| Minor | The standalone imported MediaDive solution represents water with an invalid percent-like concentration. | `data/normalized_yaml/bacterial/mediadive_1690_Main_sol_830d.yaml` preserves the same 1000 ml water source row but stores it as `1000 PERCENT_V_V`, so it cannot simply be linked until solution water units are normalized. | MediaDive solution import for mediadive.solution:1690 |

## Recommended Edits

1. Add the DSMZ 830d 1000 ml distilled-water component to `data/normalized_yaml/bacterial/r2a_medium_microaerobic.yaml` using the repository's standard final-volume representation.
2. Normalize the `mediadive_1690_Main_sol_830d.yaml` distilled-water row or leave that generated solution unlinked until MediaDive solution imports can represent 1000 ml final volume correctly.
3. Regenerate merged YAML and indexes so `data/merge_yaml/merged/r2a_medium_microaerobic.yaml` carries the water repair.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on the regenerated DSMZ 830d record.
- Run an ignored-inclusive exact search for `mediadive.medium:830d` and `DSMZ_Medium830d` under `data/normalized_yaml` and `data/merge_yaml` to confirm no duplicate 830d owner was introduced.
- Inspect the regenerated recipe and confirm that it has the eight DSMZ solutes, 1000 ml distilled water, pH 5.0-5.5, and both microaerobic gas-handling preparation steps.

## Additional Notes

None found.

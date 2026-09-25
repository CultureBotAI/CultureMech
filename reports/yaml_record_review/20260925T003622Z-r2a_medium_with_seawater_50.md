# YAML Record Review: R2A MEDIUM WITH SEAWATER 50%

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/r2a_medium_with_seawater_50.yaml
- Started UTC: 2026-09-25T00:36:22Z
- Finished UTC: 2026-09-25T00:36:57Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Generated record | data/merge_yaml/merged/r2a_medium_with_seawater_50.yaml |
| Maintained owner | data/normalized_yaml/bacterial/r2a_medium_with_seawater_50.yaml |
| Stable ID | CultureMech:000855 |
| Name | r2a_medium_with_seawater_50 |
| Original name | R2A MEDIUM WITH SEAWATER 50% |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | SOLID_AGAR |
| pH | 7.0 |
| Source grounding | mediadive.medium:1394, DSMZ Medium 1394 |
| Merge fingerprint | e7bb053875abc66a214d14a6ca8f7f95a064d404e3e733353ecedbc913cc49c6 |
| Merged from | r2a_medium_with_seawater_50 |

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/r2a_medium_with_seawater_50.yaml` | Passed; exited 0 with no diagnostics. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/r2a_medium_with_seawater_50.yaml --out /private/tmp/r2a_medium_with_seawater_50.strict.tsv --workers 1 --quiet` | Passed. `/private/tmp/r2a_medium_with_seawater_50.strict.tsv` had one line, the header only, so 0 strict errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/r2a_medium_with_seawater_50.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused check reported 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/r2a_medium_with_seawater_50.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record correctly points at DSMZ Medium 1394, R2A MEDIUM WITH SEAWATER 50%. Its base R2A ingredients, 1 mg/L FeSO4 addition, pH 7.0, and optional 20 g/L agar match the DSMZ and MediaDive source identity.

The final-volume liquid rows are not represented correctly. DSMZ and MediaDive list 500 ml seawater and 500 ml distilled water in the 1 L mineral-salts solution. The CultureMech record stores seawater as `500 G_PER_L` and omits distilled water entirely.

## Evidence

- Supported: DSMZ Medium 1394 and MediaDive medium 1394 list 0.5 g each yeast extract, Proteose Peptone (Difco no. 3), casamino acids, glucose, and soluble starch; 0.3 g each Na-pyruvate and K2HPO4; 0.05 g MgSO4 x 7 H2O; and 0.001 g FeSO4.
- Supported: DSMZ Medium 1394 and MediaDive medium 1394 support pH 7.0, sterilization by autoclaving, and optional solidification by adding 20.0 g/L agar.
- Unsupported by unit: DSMZ Medium 1394 lists seawater as 500 ml, not `500 G_PER_L`.
- Unsupported by omission: DSMZ Medium 1394 lists 500 ml distilled water, but the generated record has no distilled-water row.

## Completeness

The generated record is incomplete as a 50% seawater final-volume formula until it includes both 500 ml seawater and 500 ml distilled water. The optional agar row is present, but the source describes agar as a solidification option, so future curation should either mark the agar as optional in place or split the liquid and solid forms explicitly.

The ignored-inclusive exact search for `mediadive.medium:1394`, `DSMZ_Medium1394`, and `DSMZ Medium: 1394` covered `data/normalized_yaml`, `data/merge_yaml`, `scripts`, and `src`. It found only this maintained owner/generated record and source-index rows for DSMZ 1394.

Empty optional fields are not otherwise defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The final-volume liquid pair is incomplete and one unit is wrong. | DSMZ Medium 1394 lists 500 ml seawater and 500 ml distilled water; the generated record stores `Sea water` as `500 G_PER_L` and omits the 500 ml distilled-water row. | data/normalized_yaml/bacterial/r2a_medium_with_seawater_50.yaml |
| Minor | The record is typed as only solid agar even though agar is optional in the source. | DSMZ says the medium may be solidified by adding 20.0 g/L agar; the generated record includes agar and sets `physical_state: SOLID_AGAR`, with no liquid sibling or explicit optional marker beyond the note. | data/normalized_yaml/bacterial/r2a_medium_with_seawater_50.yaml |

## Recommended Edits

1. Represent the DSMZ 1394 liquid phase with 500 ml seawater and 500 ml distilled water using the repository's standard final-volume units.
2. Preserve agar as a 20 g/L optional solidifier or split this record into linked liquid and solid physical-state variants if optional agar is not expressible for one record.
3. Regenerate merged YAML and indexes so the reviewed DSMZ 1394 output carries the volume repair.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on the regenerated DSMZ 1394 record.
- Run an ignored-inclusive exact search for `mediadive.medium:1394` and `DSMZ_Medium1394` under `data/normalized_yaml` and `data/merge_yaml` to confirm no duplicate DSMZ 1394 owner was introduced.
- Inspect the regenerated recipe and verify that seawater and distilled water are both present at 500 ml, pH 7.0 is retained, and the agar row is represented as optional solidification or as a linked solid sibling.

## Additional Notes

None found.

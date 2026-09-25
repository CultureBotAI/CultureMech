# YAML Record Review: R2A + fumarate (anaerobic)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/r2a_fumarate_anaerobic__602bc886.yaml
- Started UTC: 2026-09-25T00:28:33Z
- Finished UTC: 2026-09-25T00:29:19Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Generated record | data/merge_yaml/merged/r2a_fumarate_anaerobic__602bc886.yaml |
| Maintained owner | data/normalized_yaml/bacterial/r2a_fumarate_anaerobic.yaml |
| Stable ID | CultureMech:009554 |
| Name | r2a_fumarate_anaerobic |
| Original name | R2A + fumarate (anaerobic) |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | SOLID_AGAR |
| Source grounding | TOGO:M3041, original NBRC_M1520-1 |
| Merge fingerprint | 602bc88678cc7bfd3d7b6c940693b79ea42572df53b4c3feabc72e881cea666d |
| Merged from | r2a_fumarate_anaerobic |

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/r2a_fumarate_anaerobic__602bc886.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/r2a_fumarate_anaerobic__602bc886.yaml --out /private/tmp/r2a_fumarate_anaerobic__602bc886.strict.tsv --workers 1 --quiet` | Passed. `/private/tmp/r2a_fumarate_anaerobic__602bc886.strict.tsv` had one line, the header only, so 0 strict errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/r2a_fumarate_anaerobic__602bc886.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused check reported 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/r2a_fumarate_anaerobic__602bc886.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record denotes the correct solid TOGO source projection: `TOGO:M3041`, R2A + fumarate (anaerobic), imported from `NBRC_M1520-1` on NBRC Medium 1520. The `SOLID_AGAR` physical state agrees with the inclusion of NBRC's 15 g agar-if-needed row.

The glucose, starch, sodium pyruvate, K2HPO4, MgSO4 x 7 H2O, and sodium fumarate groundings are chemically plausible. The Bacto yeast extract, proteose peptone, and casamino acids rows are undefined products and are correctly left without CHEBI terms.

## Evidence

- Supported: the live NBRC Medium 1520 page lists R2A + fumarate (anaerobic), the same dry R2A components, 1.4 g sodium fumarate, optional 15 g agar, 1 L distilled water, and pH 6-7.
- Supported: TOGO M3041 reports the same solid formula from `original_media_id` `NBRC_M1520-1` and includes the optional agar row as a 15 g component.
- Unsupported by unit: TOGO M3041 and the generated record convert NBRC 1 L distilled water into `1 G_PER_L`; the source gives a final-volume water row.
- Unsupported by omission: TOGO M3041 exposes pH 6-7 as a comment, but the generated record has no `ph_range`.

## Completeness

The formula includes all NBRC solid-formula ingredients, including the optional agar that differentiates M3041 from the liquid M3042 projection. It is still missing a correct volumetric water representation and the pH range.

The ignored-inclusive exact search for `TOGO:M3041`, `togomedium.org/medium/M3041`, `NBRC_M1520-1`, and `NO=1520` covered `data/normalized_yaml`, `data/merge_yaml`, `scripts`, and `src`. It found this TOGO M3041 owner and generated record, index entries for M3041, and the sibling `data/normalized_yaml/bacterial/TOGO_M3042_R2A_fumarate_anaerobic.yaml` liquid projection of the same NBRC 1520 recipe. The sibling is not an exact duplicate of M3041, but the two records should be linked as physical-state variants.

Empty optional fields are not otherwise defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Distilled water is represented with the wrong unit. | NBRC Medium 1520 and TOGO M3041 both list `Distilled water` as 1 L; the generated CultureMech ingredient is `1 G_PER_L`. | data/normalized_yaml/bacterial/r2a_fumarate_anaerobic.yaml |
| Major | The source pH range was lost. | NBRC gives pH 6-7 and TOGO M3041 keeps that text in comments; the generated record has no `ph_range` or preparation note that preserves it. | data/normalized_yaml/bacterial/r2a_fumarate_anaerobic.yaml |
| Minor | The solid M3041 and liquid M3042 records from NBRC 1520 are not linked as physical-state variants. | The exact NBRC URL search found `data/normalized_yaml/bacterial/TOGO_M3042_R2A_fumarate_anaerobic.yaml`, a TOGO M3042 record that removes the optional 15 g/L agar from the same NBRC 1520 composition. | TOGO M3041 and TOGO M3042 owner records |

## Recommended Edits

1. Correct the distilled-water concentration in `data/normalized_yaml/bacterial/r2a_fumarate_anaerobic.yaml` from `1 G_PER_L` to the repository's standard representation of 1 L per liter.
2. Add `ph_range: 6-7` from NBRC Medium 1520.
3. Add reciprocal physical-state variant metadata between the TOGO M3041 solid owner and the TOGO M3042 liquid owner, with the 15 g/L agar row documented as the differentiating ingredient.
4. Regenerate merged YAML and indexes so the reviewed generated record carries the maintained repair.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on the regenerated M3041 record.
- Run an ignored-inclusive exact search for `TOGO:M3041`, `NBRC_M1520-1`, and `NO=1520` under `data/normalized_yaml` and `data/merge_yaml` to confirm the repaired solid record and its M3042 sibling are intentionally related.
- Inspect the regenerated recipe and confirm that distilled water is volumetric, pH 6-7 is explicit, and the 15 g/L agar row remains the only formula difference from the M3042 liquid sibling.

## Additional Notes

The TOGO M3041 API reports a date-like `ph` metadata value even though its parsed comments include `pH 6-7`. Future curation should rely on the NBRC page and the TOGO comment string, not that malformed TOGO metadata field.

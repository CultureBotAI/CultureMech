# YAML Record Review: R2A + fumarate (anaerobic)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/r2a_fumarate_anaerobic.yaml
- Started UTC: 2026-09-25T00:26:30Z
- Finished UTC: 2026-09-25T00:27:34Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Generated record | data/merge_yaml/merged/r2a_fumarate_anaerobic.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M3042_R2A_fumarate_anaerobic.yaml |
| Stable ID | CultureMech:009555 |
| Name | r2a_fumarate_anaerobic |
| Original name | R2A + fumarate (anaerobic) |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| Source grounding | TOGO:M3042, original NBRC_M1520-2 |
| Merge fingerprint | c1f1d61bb0103e84f68cee0139a8311533add8d85e194d3562532208834f27c4 |
| Merged from | TOGO_M3042_R2A_fumarate_anaerobic |

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/r2a_fumarate_anaerobic.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/r2a_fumarate_anaerobic.yaml --out /private/tmp/r2a_fumarate_anaerobic.strict.tsv --workers 1 --quiet` | Passed. `/private/tmp/r2a_fumarate_anaerobic.strict.tsv` had one line, the header only, so 0 strict errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/r2a_fumarate_anaerobic.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused check reported 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/r2a_fumarate_anaerobic.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record denotes the right TOGO source and the right NBRC source variant: `TOGO:M3042`, R2A + fumarate (anaerobic), imported from `NBRC_M1520-2` on NBRC Medium 1520. The `LIQUID` physical state agrees with TOGO M3042 omitting the optional agar row from the NBRC page.

The chemical groundings for glucose, starch, sodium pyruvate, K2HPO4, MgSO4 x 7 H2O, sodium fumarate, CO2, and N2 are plausible. The undefined Bacto yeast extract, proteose peptone, and casamino acids products are correctly left ungrounded to CHEBI.

## Evidence

- Supported: the live NBRC Medium 1520 page lists R2A + fumarate (anaerobic), the same dry R2A components, 1.4 g sodium fumarate, 1 L distilled water, optional 15 g agar, pH 6-7, and an anaerobic liquid-medium instruction under an N2/CO2 atmosphere.
- Supported: TOGO M3042 reports the same formula without the optional 15 g agar row and keeps `original_media_id` as `NBRC_M1520-2` with the NBRC Medium 1520 URL.
- Unsupported by unit: TOGO M3042 and the generated record convert NBRC 1 L distilled water into `1 G_PER_L`; the source is a final-volume water row, not a gram-per-liter solute.
- Unsupported by omission: TOGO M3042 exposes pH 6-7 as a comment, but the generated record has no `ph_range`.
- Unsupported by omission: TOGO M3042 and NBRC both describe dispensing under N2/CO2, sealing with butyl rubber stoppers, and autoclaving at 121 C for 20 min; the generated record drops that preparation text and leaves N2 and CO2 as variable pseudo-ingredients.

## Completeness

The generated record is structurally valid but incomplete for culture use because it lacks both pH 6-7 and the anaerobic dispensing, sealing, and autoclaving instructions.

The ignored-inclusive exact search for `TOGO:M3042`, `togomedium.org/medium/M3042`, `NBRC_M1520-2`, and `NO=1520` covered `data/normalized_yaml`, `data/merge_yaml`, `scripts`, and `src`. It found this TOGO M3042 owner and generated record, index entries for M3042, and a separate `NBRC_M1520-1` / TOGO M3041 sibling that represents the same NBRC 1520 recipe with 15 g/L agar. The sibling is not an exact duplicate of M3042, but it should be linked as a physical-state variant once both rows are repaired.

Empty optional fields are not otherwise defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Distilled water is represented with the wrong unit. | NBRC Medium 1520 and TOGO M3042 both list `Distilled water` as 1 L; the generated CultureMech ingredient is `1 G_PER_L`. | data/normalized_yaml/bacterial/TOGO_M3042_R2A_fumarate_anaerobic.yaml |
| Major | The source pH range and anaerobic preparation instruction were lost. | NBRC gives pH 6-7 and says to dispense liquid medium under an N2/CO2 atmosphere, seal with butyl rubber stoppers, and autoclave at 121 C for 20 min; the generated record has no `ph_range` or `preparation_steps`. | data/normalized_yaml/bacterial/TOGO_M3042_R2A_fumarate_anaerobic.yaml |
| Minor | N2 and CO2 are modeled only as variable ingredients. | The gases are conditions in the NBRC preparation sentence rather than weighed formula rows, so the record should keep them in the anaerobic preparation step even if term-linked gas entries are retained as ancillary components. | data/normalized_yaml/bacterial/TOGO_M3042_R2A_fumarate_anaerobic.yaml |
| Minor | The liquid M3042 and solid M3041 records from NBRC 1520 are not linked as physical-state variants. | The exact NBRC URL search found `data/normalized_yaml/bacterial/r2a_fumarate_anaerobic.yaml`, a TOGO M3041 record that adds optional 15 g/L agar to the same NBRC 1520 composition. | TOGO M3041 and TOGO M3042 owner records |

## Recommended Edits

1. Correct the distilled-water concentration in `data/normalized_yaml/bacterial/TOGO_M3042_R2A_fumarate_anaerobic.yaml` from `1 G_PER_L` to the repository's standard representation of 1 L per liter.
2. Add `ph_range: 6-7` and preparation steps that preserve the NBRC anaerobic instruction: dispense under N2/CO2, seal with butyl rubber stoppers, and autoclave at 121 C for 20 min.
3. Move the N2/CO2 atmosphere semantics into the preparation text, or keep the gas entries only if their notes explain that they represent the gas phase rather than weighed ingredients.
4. Add reciprocal physical-state variant metadata between the TOGO M3042 liquid owner and the TOGO M3041 solid owner.
5. Regenerate merged YAML and indexes so the reviewed generated record carries the maintained repair.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on the regenerated M3042 record.
- Run an ignored-inclusive exact search for `TOGO:M3042`, `NBRC_M1520-2`, and `NO=1520` under `data/normalized_yaml` and `data/merge_yaml` to confirm the repaired liquid record and its M3041 sibling are intentionally related.
- Inspect the regenerated recipe and confirm that distilled water is volumetric, pH 6-7 is explicit, and the N2/CO2 butyl-stopper autoclave instruction is present.
- Inspect the M3041 sibling and confirm it differs from M3042 only by the optional 15 g/L agar physical-state variant.

## Additional Notes

The TOGO M3042 API currently reports a date-like `ph` metadata value even though its parsed comments include `pH 6-7`. Future curation should rely on the NBRC page and the TOGO comment string, not that malformed TOGO metadata field.

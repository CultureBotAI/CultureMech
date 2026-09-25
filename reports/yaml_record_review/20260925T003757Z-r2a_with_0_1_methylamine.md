# YAML Record Review: R2A with 0.1% methylamine

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/r2a_with_0_1_methylamine.yaml
- Started UTC: 2026-09-25T00:37:57Z
- Finished UTC: 2026-09-25T00:39:09Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Generated record | data/merge_yaml/merged/r2a_with_0_1_methylamine.yaml |
| Principal maintained owner | data/normalized_yaml/bacterial/r2a_with_0_1_methylamine.yaml |
| Stable ID | CultureMech:008687 |
| Name | r2a_with_0_1_methylamine |
| Original name | R2A with 0.1% methylamine |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | SOLID_AGAR |
| Source grounding | TOGO:M2097, original NBRC_M1410 |
| Merge fingerprint | 577bb7da9e4af1f9c10e7e800af1ba32bc6f06107a558f389f19af6058c4a009 |
| Merged from | 1_5_r2a_yeastextract, 5_r2a_medium, TOGO_M1646_R2A_Medium, r2a_medium_ph_6_0, r2a_with_0_1_methylamine |

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/r2a_with_0_1_methylamine.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/r2a_with_0_1_methylamine.yaml --out /private/tmp/r2a_with_0_1_methylamine.strict.tsv --workers 1 --quiet` | Passed. `/private/tmp/r2a_with_0_1_methylamine.strict.tsv` had one line, the header only, so 0 strict errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/r2a_with_0_1_methylamine.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused check reported 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/r2a_with_0_1_methylamine.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The generated record has the identity of TOGO M2097 / NBRC Medium 1410, but its formula was assembled from five distinct R2A-family inputs. It now mixes the 1/5 R2A ingredient concentrations from TOGO M3063, a 3 g/L yeast-extract concentration from `1_5_r2a_yeastextract`, the M2097 methylamine stock shell, and synonyms for 5x R2A, base R2A, and R2A pH 6.0.

The source identity is therefore wrong at the generated-record level. NBRC 1410 is full-strength R2A with 1 ml neutralized methylamine and pH unadjusted; the reviewed record no longer has full-strength MgSO4 x 7 H2O, K2HPO4, sodium pyruvate, glucose, soluble starch, proteose peptone, or casamino acids.

## Evidence

- Supported for the unmerged owner: NBRC 1410 and TOGO M2097 list full-strength R2A amounts, 1 L distilled water, 1 ml neutralized methylamine, optional 15 g agar, pH unadjusted, and a note to sterilize methylamine separately by filtration.
- Unsupported after merging: the generated record has 0.01 g/L MgSO4 x 7 H2O, 0.06 g/L K2HPO4, 0.06 g/L sodium pyruvate, 0.1 g/L glucose, and 0.1 g/L soluble starch, which come from the 1/5 R2A records rather than NBRC 1410.
- Unsupported after merging: the generated record has 3 g/L Bacto Yeast Extract, which comes from the distinct `1/5 R2A + yeastextract` formulation, not from NBRC 1410.
- Unsupported by omission: the methylamine supplement is stored as an empty `solutions` entry with `1 G_PER_L`; NBRC and TOGO list 1 ml `Methylamine*` in the formula and specify that it is neutralized and filter-sterilized separately.

## Completeness

The generated record is not complete for any of the five merged source recipes. Its source identity is M2097, but its base ingredient concentrations are from other records, and the other four source recipes are reduced to synonyms with their distinctive concentrations, pH condition, or formulation labels hidden.

The ignored-inclusive exact search for `TOGO:M2097`, `togomedium.org/medium/M2097`, `NBRC_M1410`, `NO=1410`, `TOGO:M3063`, `TOGO:M1940`, `TOGO:M1646`, and `TOGO:M1942` covered `data/normalized_yaml`, `data/merge_yaml`, `scripts`, and `src`. It found five separate maintained owners under `data/normalized_yaml/bacterial` and this one merged output that coalesced all five. That search included ignored files.

Empty optional fields are not otherwise defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | Five distinct R2A variants were falsely merged into one record with the M2097 identity. | The `merged_from` list combines 1/5 R2A + yeastextract, 5x R2A, base R2A, R2A pH 6.0, and R2A with 0.1% methylamine; these source owners have different TOGO IDs, NBRC originals, concentrations, pH conditions, or supplements. | merge fingerprinting for the five source owners |
| Blocker | The generated M2097 formula has the wrong base ingredient concentrations. | NBRC 1410 uses full-strength R2A values, but the generated record uses 1/5-strength values for MgSO4 x 7 H2O, K2HPO4, sodium pyruvate, glucose, soluble starch, proteose peptone, and casamino acids and the 3 g/L yeast extract from the distinct M3063 formulation. | data/normalized_yaml/bacterial/r2a_with_0_1_methylamine.yaml and merge generation |
| Major | The methylamine supplement is not represented as a real component with its preparation note. | TOGO M2097 and NBRC 1410 list 1 ml neutralized `Methylamine*` and the note `Neutralized. Sterilize separately by filtration.`; the maintained owner and generated record contain an empty `Methylamine*` solution at `1 G_PER_L`. | data/normalized_yaml/bacterial/r2a_with_0_1_methylamine.yaml |

## Recommended Edits

1. Change merge fingerprinting or add merge-blocking metadata so `1_5_r2a_yeastextract.yaml`, `5_r2a_medium.yaml`, `TOGO_M1646_R2A_Medium.yaml`, `r2a_medium_ph_6_0.yaml`, and `r2a_with_0_1_methylamine.yaml` generate distinct records.
2. Repair `data/normalized_yaml/bacterial/r2a_with_0_1_methylamine.yaml` so its 1 ml neutralized methylamine supplement is present at the main formula level or as a non-empty supplement and the separate filtration note is preserved.
3. Preserve the full-strength NBRC 1410 R2A base concentrations when regenerating M2097.
4. Re-evaluate the other four R2A owners as concentration, pH, source-duplicate, or supplement variants after they are split out of the false merged record.
5. Regenerate merged YAML and indexes.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on the regenerated M2097 record and the four re-split siblings.
- Run an ignored-inclusive exact search for `TOGO:M2097`, `TOGO:M3063`, `TOGO:M1940`, `TOGO:M1646`, and `TOGO:M1942` under `data/merge_yaml` to confirm they no longer collapse into one generated record.
- Manually inspect regenerated M2097 and verify full-strength R2A amounts, 1 L water, 1 ml neutralized methylamine, pH-unadjusted status, and the filter-sterilization note.

## Additional Notes

The owner `data/normalized_yaml/bacterial/r2a_medium_ph_6_0.yaml` is already marked as a possible source duplicate of `TOGO_M1646_R2A_Medium.yaml`; that local relationship is narrower than, and does not justify, merging in the 1/5, 5x, yeast-extract, or methylamine records.

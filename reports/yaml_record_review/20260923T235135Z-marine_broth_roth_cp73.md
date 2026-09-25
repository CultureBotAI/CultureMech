# YAML Record Review: marine_broth_roth_cp73

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_broth_roth_cp73.yaml
- Started UTC: 2026-09-23T23:50:37Z
- Finished UTC: 2026-09-23T23:51:55Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_broth_roth_cp73.yaml |
| Class | MediaRecipe |
| ID | CultureMech:015361 |
| Label | marine_broth_roth_cp73 |
| Source identity | mediadive.medium:514f, DSMZ Medium 514f, MARINE BROTH (ROTH CP73) |
| Generation state | Generated one-source merge under data/merge_yaml/merged; repair data/normalized_yaml/specialized/marine_broth_roth_cp73.yaml or the MediaDive importer rather than this file |

The generated record denotes DSMZ Medium 514f from MediaDive. Its major salts and pH range are correct, but the formulation is missing the 1000 ml distilled-water row.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_broth_roth_cp73.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_broth_roth_cp73.yaml --out /private/tmp/marine_broth_roth_cp73.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_broth_roth_cp73.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_broth_roth_cp73.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- MediaDive medium 514f identifies `MARINE BROTH (ROTH CP73)`, source DSMZ, pH range 7.4 to 7.8, and a link to `DSMZ_Medium514f.pdf`.
- The DSMZ 514f PDF reports `MARINE BROTH (ROTH CP73)` and the same base formulation.
- The generated CultureMech ID, name, MediaDive source accession, and DSMZ source agree.
- The salt groundings match the formulas named in DSMZ/MediaDive, including `Fe(III) citrate`, `MgCl2`, `CaCl2`, `NaF`, `(NH4)NO3`, and `Na2HPO4`.
- Peptone and Yeast extract remain ungrounded. Agar is grounded and present as a conditional addition.

## Evidence

- DSMZ and MediaDive support the listed peptone, yeast extract, ferric citrate, salts, and 15 g/L agar for solid media.
- The YAML omits `Distilled water` even though DSMZ and MediaDive both list 1000 ml.
- The source says to add 15.0 g/L agar for solid media. The record has `Agar` with a note `if required`, but the top-level `physical_state: SOLID_AGAR` implies the whole recipe is solid rather than broth with an agar option.
- The pH range is supported because DSMZ says final pH should be 7.6 +/- 0.2 at 25 C.
- The recommendation to use the Carl Roth medium for Marinomonas mediterranea DSM 23531 is preserved in the preparation step.

## Completeness

- The main DSMZ 514f recipe is materially incomplete until the 1000 ml distilled-water row is restored.
- No target organism or growth metric is asserted. DSMZ mentions Marinomonas mediterranea DSM 23531 only as context for using the Carl Roth formulation, not as a growth experiment.
- Exact gitignore-independent searches were run for `CultureMech:015361`, `marine_broth_roth_cp73`, `mediadive.medium:514f`, and `DSMZ Medium 514f` across the scoped specialized normalized YAML, target merged file, and MediaDive/specialized/recipe index files with `--no-ignore --hidden`; the maintained YAML owner found was data/normalized_yaml/specialized/marine_broth_roth_cp73.yaml.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_broth_roth_cp73.md' -print` search, which includes ignored files, found no pre-existing review report for this generated record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The DSMZ water row is missing. | DSMZ Medium 514f and MediaDive 514f list 1000 ml distilled water; the YAML has no Distilled water ingredient. | data/normalized_yaml/specialized/marine_broth_roth_cp73.yaml and the MediaDive importer |
| minor | The physical state overstates optional agar as required. | DSMZ says to add 15.0 g/L agar for solid media, but the record sets top-level `physical_state: SOLID_AGAR`. | data/normalized_yaml/specialized/marine_broth_roth_cp73.yaml |
| minor | Peptone and Yeast extract are ungrounded. | Both source rows are generic complex ingredients and have no `term` or `mediaingredientmech_chebi_term` blocks. | data/normalized_yaml/specialized/marine_broth_roth_cp73.yaml |

## Recommended Edits

1. Add the 1000 ml distilled-water ingredient to the normalized MediaDive 514f record.
2. Represent agar as an optional solidifying addition and avoid forcing the base liquid recipe to `SOLID_AGAR`.
3. Leave Peptone and Yeast extract explicitly unmapped or map them through the repository's accepted complex-ingredient vocabulary if exact terms exist.

## Follow-up Checks

- Compare the repaired normalized YAML row-by-row against the DSMZ 514f PDF and MediaDive 514f REST payload.
- Regenerate merged recipes and confirm the generated record contains 1000 ml distilled water.
- Run open schema, strict schema, reference, and term validation on the maintained specialized input and regenerated merge.

## Additional Notes

- DSMZ and MediaDive list `SrCl2`, `H3BO3`, `Na-silicate`, `NaF`, `(NH4)NO3`, and `Na2HPO4` as milligram weights, and the YAML's decimal g/L values are equivalent.

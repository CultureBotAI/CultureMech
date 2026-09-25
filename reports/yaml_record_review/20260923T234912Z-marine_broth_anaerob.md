# YAML Record Review: marine_broth_anaerob

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_broth_anaerob.yaml
- Started UTC: 2026-09-23T23:48:05Z
- Finished UTC: 2026-09-23T23:49:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_broth_anaerob.yaml |
| Class | MediaRecipe |
| ID | CultureMech:015360 |
| Label | marine_broth_anaerob |
| Source identity | mediadive.medium:514e, DSMZ Medium 514e, MARINE BROTH (ANAEROB) |
| Generation state | Generated one-source merge under data/merge_yaml/merged; repair data/normalized_yaml/specialized/marine_broth_anaerob.yaml or the MediaDive importer rather than this file |

The generated record denotes DSMZ Medium 514e from MediaDive. It is source-aligned on identity, pH range, major salts, reductants, and the anaerobic preparation text, but it omits water and loses source volume semantics for 0.1% stock additions.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_broth_anaerob.yaml` | Passed with exit 0 and no diagnostics |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_broth_anaerob.yaml --out /private/tmp/marine_broth_anaerob.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_broth_anaerob.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_broth_anaerob.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- MediaDive medium 514e identifies `MARINE BROTH (ANAEROB)`, source DSMZ, pH range 7.3 to 7.5, and a link to `DSMZ_Medium514e.pdf`.
- The DSMZ 514e PDF reports `MARINE BROTH (ANAEROB)` and the same final pH range.
- The generated CultureMech ID, name, MediaDive source accession, and DSMZ source agree.
- The salts, reductants, and resazurin groundings match the formulas named in DSMZ/MediaDive, including anhydrous `MgCl2`, `Na2SO4`, `KBr`, `NaF`, `(NH4)NO3`, `Na2HPO4`, `L-Cysteine HCl x H2O`, and `Na2S x 9 H2O`.
- Peptone, Yeast extract, and Sodium resazurin are not linked with `mediaingredientmech_chebi_term`; Sodium resazurin has only a generic `CHEBI:8806` Resazurin term.

## Evidence

- DSMZ and MediaDive support the listed peptone, yeast extract, salt, reductant, pH, and anaerobic sparging/autoclaving claims.
- The YAML omits `Distilled water` even though DSMZ and MediaDive both list 1000 ml.
- DSMZ and MediaDive represent NaF, `(NH4)NO3`, `Na2HPO4`, and Sodium resazurin as measured volumes of 0.1% w/v stock solutions. The YAML stores only computed final `G_PER_L` values and loses the required stock concentration and volume semantics.
- DSMZ specifies Peptone and Yeast extract as BD Bacto products; the YAML keeps only the generic ingredient names.
- DSMZ includes a DSM 15630-specific post-sterilization lactate supplement; the YAML does not represent that conditional variant or note.

## Completeness

- The main DSMZ 514e recipe is materially incomplete until the 1000 ml distilled-water row is restored.
- Stock concentration context is incomplete for every 0.1% w/v addition.
- No general target organism or growth metric is asserted; that is not a defect because the DSM 15630 lactate note is a conditional variant instruction, not a broad growth claim.
- Exact gitignore-independent searches were run for `CultureMech:015360`, `marine_broth_anaerob`, `mediadive.medium:514e`, `DSMZ Medium 514e`, and `176144cc6faf5f694eb68ef19fae93f652ab09ecc47d410d552fe18842066afb` across the scoped specialized normalized YAML, the target merged file, and MediaDive/specialized/recipe index files with `--no-ignore --hidden`; the maintained YAML owner found was data/normalized_yaml/specialized/marine_broth_anaerob.yaml.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_broth_anaerob.md' -print` search, which includes ignored files, found no pre-existing review report for this generated record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The DSMZ water row is missing. | DSMZ Medium 514e and MediaDive 514e list 1000 ml distilled water; the YAML has no Distilled water ingredient. | data/normalized_yaml/specialized/marine_broth_anaerob.yaml and the MediaDive importer |
| major | Four 0.1% w/v stock additions have been flattened to final g/L values. | DSMZ lists NaF, `(NH4)NO3`, `Na2HPO4`, and Sodium resazurin as ml additions from 0.1% w/v stocks; the YAML has only 0.0024, 0.0016, 0.008, and 0.0005 `G_PER_L` ingredient rows. | data/normalized_yaml/specialized/marine_broth_anaerob.yaml and the MediaDive importer |
| minor | BD Bacto peptone and yeast extract qualifiers were dropped. | DSMZ and MediaDive both attach `BD Bacto` to Peptone and Yeast extract; the YAML keeps only generic labels. | data/normalized_yaml/specialized/marine_broth_anaerob.yaml |
| minor | The DSM 15630 lactate supplement is missing. | DSMZ 514e instructs adding 2.5 g/L lactate after sterilization for DSM 15630; the YAML has no note or variant capturing that conditional use. | data/normalized_yaml/specialized/marine_broth_anaerob.yaml |

## Recommended Edits

1. Add the 1000 ml distilled-water ingredient to the normalized MediaDive 514e record.
2. Preserve the four 0.1% w/v stock additions as source-measured stock volumes or otherwise store both final concentration and stock preparation context.
3. Preserve the `BD Bacto` attributes on Peptone and Yeast extract.
4. Add a conditional note, variant, or discussion for the DSM 15630 lactate supplement.

## Follow-up Checks

- Compare the repaired normalized YAML row-by-row against the DSMZ 514e PDF and MediaDive 514e REST payload.
- Confirm the regenerated merge has distilled water and no longer loses 0.1% stock-addition context.
- Run open schema, strict schema, reference, and term validation on the maintained specialized input and regenerated merge.

## Additional Notes

- `SrCl2`, `H3BO3`, and `Na-silicate` are listed by DSMZ as milligram quantities. The YAML stores equivalent g/L decimal values; that is acceptable because these are weighed solids rather than measured stock additions.

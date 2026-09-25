# YAML Record Review: marine_broth_0_5_sodium_pyruvate

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_broth_0_5_sodium_pyruvate.yaml
- Started UTC: 2026-09-23T23:41:24Z
- Finished UTC: 2026-09-23T23:42:41Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_broth_0_5_sodium_pyruvate.yaml |
| Class | MediaRecipe |
| ID | CultureMech:008516 |
| Label | marine_broth_0_5_sodium_pyruvate |
| Source identity | TOGO:M1938, Marine Broth + 0.5% Sodium Pyruvate, original source NBRC_M1205 |
| Generation state | Generated merge under data/merge_yaml/merged; repair data/normalized_yaml/bacterial/marine_broth_0_5_sodium_pyruvate.yaml, data/normalized_yaml/bacterial/1_5_marine_broth_0_5_sodium_pyruvate.yaml, or merge_recipes.py rather than this file |

The generated record is intended to denote NBRC medium 1205, a full-strength Marine Broth 2216 recipe with sodium pyruvate. It has incorrectly merged NBRC medium 868, a distinct 1/5 Marine Broth + sodium pyruvate formulation that includes seawater and one-fifth the Marine Broth powder.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_broth_0_5_sodium_pyruvate.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_broth_0_5_sodium_pyruvate.yaml --out /private/tmp/marine_broth_0_5_sodium_pyruvate.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_broth_0_5_sodium_pyruvate.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_broth_0_5_sodium_pyruvate.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- TOGO M1938 and NBRC medium 1205 identify `Marine Broth + 0.5% Sodium Pyruvate`.
- NBRC 1205 lists 37.4 g Bacto Marine Broth 2216 (Difco), 5 g sodium pyruvate, 15 g agar if needed, 1 L distilled water, and `pH unadjusted`.
- TOGO M1665 and NBRC medium 868 identify `1/5 Marine Broth + 0.5% Sodium Pyruvate`, not the full-strength NBRC 1205 medium.
- NBRC 868 lists 7.5 g Bacto Marine Broth 2216, 5 g sodium pyruvate, 15 g agar if needed, 800 ml seawater, 200 ml distilled water, pH 7.6, and a note that the seawater is filtered aged seawater or Daigo's Artificial Seawater SP.
- The generated record carries TOGO:M1938/NBRC 1205 identity but has the 1/5 variant's 7.5 g Bacto Marine Broth value, 200 ml distilled-water value, false `1_5_marine_broth_0_5_sodium_pyruvate` synonym, and false `merged_from` entry.
- Sodium pyruvate is correctly grounded to `CHEBI:50144`. Water is correctly grounded to `CHEBI:15377`. The undefined commercial Bacto Marine Broth and optional agar rows have no exact ontology grounding in this record.

## Evidence

- The inspected NBRC 1205 page and TOGO M1938 API response support the full-strength composition of 37.4 g Bacto Marine Broth 2216, 5 g sodium pyruvate, 15 g optional agar, and 1 L distilled water.
- The generated record is not evidence-faithful for NBRC 1205 because its Bacto Marine Broth row is 7.5 g/L, its water row is 200 g/L, and its optional agar row is 750 g/L.
- The inspected NBRC 868 page supports 15 g optional agar in the 1/5 variant, while the TOGO M1665 API and normalized TOGO M1665 record have 750 g. The 750 g value is unsupported by the original NBRC page.
- The generated M1938 record omits NBRC 1205's `pH unadjusted` comment.
- The maintained TOGO import encodes water volumes as `G_PER_L` mass concentrations: the full-strength maintained M1938 record has 1 L distilled water stored as `1 G_PER_L`, and the 1/5 maintained M1665 record has 200 ml distilled water stored as `200 G_PER_L`.

## Completeness

- The full-strength NBRC 1205 record is a short complex-medium recipe. It has no expected nested stock-solution composition, strain growth assertion, or organism evidence in the inspected NBRC/TOGO source pages.
- Optional agar is not represented as optional: the source says `Agar (if needed)`, while the record sets `physical_state: SOLID_AGAR`.
- Exact gitignore-independent searches were run for `marine_broth_0_5_sodium_pyruvate`, `1_5_marine_broth_0_5_sodium_pyruvate`, `TOGO:M1938`, `TOGO:M1665`, `NBRC_M1205`, `NBRC_M868`, and `83c4dd814b263bcbc1555977ae637714ad03a870742573c355058b3f431cdf69` across the scoped normalized bacterial YAML, merged YAML, and TOGO/bacterial/recipe index files with `--no-ignore --hidden`; the relevant maintained owners found were the two bacterial TOGO records.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_broth_0_5_sodium_pyruvate.md' -print` search, which includes ignored files, found no pre-existing review report for this record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The generated NBRC 1205 record merged in the distinct 1/5 NBRC 868 medium and now publishes 1/5-strength values under the full-strength TOGO:M1938 identity. | NBRC 1205 has 37.4 g Bacto Marine Broth and 1 L distilled water; NBRC 868 has 7.5 g Bacto Marine Broth and 200 ml distilled water plus 800 ml seawater. The generated M1938 record lists 7.5 and 200 and carries `1_5_marine_broth_0_5_sodium_pyruvate` as a synonym. | data/normalized_yaml/bacterial/marine_broth_0_5_sodium_pyruvate.yaml, data/normalized_yaml/bacterial/1_5_marine_broth_0_5_sodium_pyruvate.yaml, and the duplicate fingerprint logic in `merge_recipes.py` |
| major | NBRC 868 optional agar was imported as 750 g/L instead of the 15 g in the original source. | The direct NBRC 868 page lists `Agar (if needed)` as 15 g. TOGO M1665 and the normalized M1665 record list 750 g and the generated M1938 record inherited that unsupported value. | data/normalized_yaml/bacterial/1_5_marine_broth_0_5_sodium_pyruvate.yaml and the NBRC-to-TOGO import normalization path |
| major | Distilled-water volume was encoded as a mass concentration. | NBRC 1205 lists 1 L distilled water, not 1 g/L; NBRC 868 lists 200 ml distilled water, not 200 g/L. Both maintained TOGO imports put those volume values under `G_PER_L`. | data/normalized_yaml/bacterial/marine_broth_0_5_sodium_pyruvate.yaml, data/normalized_yaml/bacterial/1_5_marine_broth_0_5_sodium_pyruvate.yaml, and the TOGO importer |
| minor | The optional-agar state is over-specified as a solid recipe. | NBRC 1205 and NBRC 868 both say `Agar (if needed)`, but the record encodes `physical_state: SOLID_AGAR` without an optional ingredient flag. | data/normalized_yaml/bacterial/marine_broth_0_5_sodium_pyruvate.yaml and data/normalized_yaml/bacterial/1_5_marine_broth_0_5_sodium_pyruvate.yaml |
| minor | The NBRC 1205 pH comment was dropped. | NBRC 1205 and TOGO M1938 include `pH unadjusted`; the maintained and merged M1938 YAML records do not represent it. | data/normalized_yaml/bacterial/marine_broth_0_5_sodium_pyruvate.yaml |

## Recommended Edits

1. Change duplicate detection so Marine Broth + 0.5% Sodium Pyruvate and 1/5 Marine Broth + 0.5% Sodium Pyruvate are not merged; regenerate `data/merge_yaml/merged/`.
2. Repair the 1/5 NBRC 868 import so optional agar is 15 g per recipe instead of 750 g/L.
3. Preserve source volume units for distilled water and seawater instead of encoding them as `G_PER_L`.
4. Represent optional agar as a conditional solidifying addition and avoid forcing the base broth-only recipe to `SOLID_AGAR`.
5. Preserve the NBRC 1205 `pH unadjusted` comment in a structured or note field.

## Follow-up Checks

- Rebuild merged recipes and confirm TOGO:M1938 has 37.4 g Bacto Marine Broth, 5 g sodium pyruvate, optional 15 g agar, and 1 L distilled water.
- Confirm TOGO:M1938 no longer lists `1_5_marine_broth_0_5_sodium_pyruvate` under `synonyms` or `merged_from`.
- Confirm the distinct TOGO:M1665 regenerated record has 7.5 g Bacto Marine Broth, 5 g sodium pyruvate, optional 15 g agar, 800 ml seawater, and 200 ml distilled water.
- Run open schema, strict schema, reference, and term validation on both maintained TOGO inputs and on the regenerated merged outputs.

## Additional Notes

- An earlier exploratory search for this review included a bare `CultureMech:` alternative and was too broad for ownership or absence claims. It was discarded; only the exact `--no-ignore --hidden` search in the Completeness section was used.
- Sodium pyruvate is correctly supported at 5 g in both NBRC 1205 and NBRC 868, so it is not part of the false-merge defect.

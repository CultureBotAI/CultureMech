# YAML Record Review: Petrotoga Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/petrotoga_medium__6eec3338.yaml
- Started UTC: 2026-09-24T20:41:05Z
- Finished UTC: 2026-09-24T20:41:05Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record path | `data/merge_yaml/merged/petrotoga_medium__6eec3338.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M295_Petrotoga_Medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009484` |
| Name | `petrotoga_medium` |
| Original name | `Petrotoga Medium` |
| Media term | `TOGO:M295` |
| Generated status | Generated merge output from `data/normalized_yaml/bacterial/TOGO_M295_Petrotoga_Medium.yaml` |

The target resolves to the TOGO M295 import of JCM Medium 300. An
ignored-inclusive search over `data`, `src`, and `scripts` for `TOGO:M295`,
`M295`, `JCM_M300`, `GRMD=300`, `CultureMech:009484`,
`JCM_J300_PETROTOGA_MEDIUM`, and `PETROTOGA_MEDIUM.yaml` found this TOGO record
and a separate direct JCM/MediaDive record for the same JCM 300 recipe in
`data/normalized_yaml/bacterial/JCM_J300_PETROTOGA_MEDIUM.yaml` and
`data/merge_yaml/merged/PETROTOGA_MEDIUM.yaml`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/petrotoga_medium__6eec3338.yaml` | Passed; no issues found. |
| Strict repository validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/petrotoga_medium__6eec3338.yaml --out /private/tmp/petrotoga_medium__6eec3338.strict.tsv --workers 1 --quiet` | Passed; the TSV had only its header line, so 0 errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/petrotoga_medium__6eec3338.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/petrotoga_medium__6eec3338.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run. | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in one generated YAML file. |

## Identity and Grounding

The identity is correct: live JCM Medium 300 and TOGO M295 both denote
PETROTOGA MEDIUM from JCM GRMD 300.

The top-level `composition_type: UNDEFINED` is too weak. JCM lists defined
salts, HEPES, maltose monohydrate, and undefined yeast extract, Bacto peptone,
and tryptone, so the recipe is semi-defined and complex rather than undefined.

The checked CHEBI groundings are compatible with the source ingredient labels.
No wrong chemical identity was found in this TOGO M295 record.

## Evidence

The JCM page for medium 300 supports the main formulation: 30.0 g NaCl, 0.5 g
MgCl2 x 6 H2O, 0.1 g CaCl2 x 2 H2O, 1.0 g NH4Cl, 0.2 g KCl, 2.6 g HEPES,
1.5 g Yeast extract (BD-Difco), 1.5 g Bacto peptone (BD-Difco), 1.5 g Tryptone
(BD-Difco), 0.3 g KH2PO4, 3.6 g maltose monohydrate, and 1.0 L distilled
water.

The TOGO import supports the same JCM_M300 original source and ingredient set.
The generated record carries the source water row, but imports it as `1`
`G_PER_L`; water is a 1 L preparation volume in JCM, not a 1 g/L solute.

The generated record drops the JCM pH and atmosphere instructions. JCM directs
the curator to adjust pH to 7.5 and fill the gas phase with N2. The direct
JCM/MediaDive sibling keeps that content in `ph_value: 7.5` and one
`preparation_steps` entry, but this TOGO-derived generated record has neither
field.

## Completeness

The generated record is missing pH 7.5 and the N2 gas-phase preparation step.

The direct JCM/MediaDive import for the same source recipe is emitted
separately as `data/merge_yaml/merged/PETROTOGA_MEDIUM.yaml`; the corpus
therefore has two generated records for one JCM 300 recipe.

No empty optional field was material to this review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | TOGO M295 remains split from the direct JCM/MediaDive Medium J300 owner instead of merging into the same source recipe. | The ignored-inclusive search over `data`, `src`, and `scripts` found both `TOGO:M295` with original source `JCM_M300` and a separate `mediadive.medium:J300` owner in `JCM_J300_PETROTOGA_MEDIUM.yaml`; both point to `GRMD=300`. | `data/normalized_yaml/bacterial/TOGO_M295_Petrotoga_Medium.yaml`, `data/normalized_yaml/bacterial/JCM_J300_PETROTOGA_MEDIUM.yaml`, and merge source-matching logic |
| Major | The TOGO-derived record omits the JCM pH and anaerobic gas-phase preparation text. | JCM says to adjust pH to 7.5 and fill the gas phase with N2; the generated TOGO record has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M295_Petrotoga_Medium.yaml` |
| Minor | The JCM water row is encoded as a gram-per-liter ingredient. | JCM lists `Distilled water` as 1.0 L, while the generated TOGO record stores it as `1` `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M295_Petrotoga_Medium.yaml` |
| Minor | The top-level composition type is too weak. | The source is an itemized recipe with both defined compounds and undefined complex peptone/extract ingredients, so `SEMI_DEFINED` is more accurate than `UNDEFINED`. | `data/normalized_yaml/bacterial/TOGO_M295_Petrotoga_Medium.yaml` and `data/normalized_yaml/bacterial/JCM_J300_PETROTOGA_MEDIUM.yaml` |

## Recommended Edits

1. Map TOGO M295/JCM_M300 to `mediadive.medium:J300` so the merge step emits
   one JCM 300 Petrotoga Medium record.
2. Preserve the union of source-supported fields when those owners are merged:
   keep the JCM pH 7.5 and N2 preparation text from the direct JCM import and
   the 1 L distilled water row from the TOGO/JCM source recipe.
3. Represent distilled water as a source volume rather than `1` g/L.
4. Change the final JCM 300 record's `composition_type` to `SEMI_DEFINED`.

## Follow-up Checks

1. Regenerate the merged YAML and rerun the open schema, strict, reference, and
   term validators on the regenerated JCM 300 output.
2. Manually compare the regenerated recipe with the JCM `GRMD=300` page and
   verify that the ingredient values, pH, N2 preparation instruction, and water
   volume are present.
3. Use an ignored-inclusive exact search for `TOGO:M295`, `JCM_M300`,
   `mediadive.medium:J300`, and `GRMD=300` under `data`, `src`, and `scripts`
   to verify that one exact JCM 300 source recipe does not create two generated
   records.

## Additional Notes

TOGO_M289_Cellulomonas_Fermentans_Medium cites `JCM_M295`; that is a different
JCM medium number and was not treated as a Petrotoga Medium duplicate.

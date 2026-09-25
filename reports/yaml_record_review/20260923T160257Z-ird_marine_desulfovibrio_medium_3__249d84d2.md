# YAML Record Review: IRD MARINE DESULFOVIBRIO MEDIUM-3

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ird_marine_desulfovibrio_medium_3__249d84d2.yaml
- Started UTC: 2026-09-23T16:02:00Z
- Finished UTC: 2026-09-23T16:02:57Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated record | `data/merge_yaml/merged/ird_marine_desulfovibrio_medium_3__249d84d2.yaml` |
| Stable ID | `CultureMech:015383` |
| Label | IRD MARINE DESULFOVIBRIO MEDIUM-3 |
| Source identity | MediaDive JCM J1117 |
| Source-owned record | `data/normalized_yaml/specialized/ird_marine_desulfovibrio_medium_3.yaml` |

This generated record copied the MediaDive J1116 parent composition and merged with the J1116 parent instead of preserving the J1117 high-salt variant. Future fixes belong in the specialized normalized owner, option-record expansion, and duplicate-merge logic.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ird_marine_desulfovibrio_medium_3__249d84d2.yaml` | Passed with `No issues found`. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ird_marine_desulfovibrio_medium_3__249d84d2.yaml --out /private/tmp/ird_marine_desulfovibrio_medium_3__249d84d2.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and zero error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ird_marine_desulfovibrio_medium_3__249d84d2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; this file received 0 configured reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ird_marine_desulfovibrio_medium_3__249d84d2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `pkg_resources` warning from `eutils`. |
| Embedded history | Not run | No documented focused validator checks embedded `MediaRecipe.curation_history`; `just validate-history` is scoped to standalone files under `history/`. |

## Identity and Grounding

- The `mediadive.medium:J1117` term and label match live MediaDive J1117.
- Live MediaDive J1117 and JCM 1117 both define IRD Marine Desulfovibrio Medium-3 as Medium 1116 with 60.0 g/L final NaCl.
- Gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found this MediaDive J1117 suffix plus a separate TOGO M1195 generated record for the same JCM 1117 source.

## Evidence

- Supported by MediaDive J1117 and JCM 1117: J1117 is an option-style recipe that changes the J1116 parent to 60.0 g/L final NaCl.
- Unsupported in the generated record: NaCl is `30.3337 G_PER_L`, copied from Medium 1116 before the J1117 60.0 g/L override was applied.
- Unsupported in the generated record: `parent_media.relationship` and `variant_relationship` call J1117 a `SOURCE_DUPLICATE`, but J1117 is a high-salt variant of J1116.
- Unsupported in the generated record: the copied J1116 trace-element stock was flattened into final ingredients at stock strength, and sodium lactate, bicarbonate, and sulfide stock additions are final `G_PER_L` ingredients.

## Completeness

- The record has no 60.0 g/L final NaCl row and therefore lacks the only J1117-specific formulation change.
- The J1116 parent preparation details and stock boundaries are not preserved after copying.
- Empty target-organism, literature-evidence, and discussion arrays are not defects for this option-style source recipe.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Blocker | The J1117 high-salt override was not applied. | MediaDive/JCM J1117 says to use Medium 1116 with 60.0 g/L final NaCl; the generated record still has copied-parent `30.3337 G_PER_L` NaCl. | `data/normalized_yaml/specialized/ird_marine_desulfovibrio_medium_3.yaml`; option-record expansion. |
| Major | J1117 is incorrectly modeled as a source duplicate of J1116. | The generated record sets `SOURCE_DUPLICATE` relationships and merges `ird_marine_desulfovibrio_medium_2` with `_3`, but the NaCl override makes J1117 a variant. | Variant classification and `merge_recipes.py`. |
| Major | J1116 parent stock boundaries were lost in the copied content. | The copied parent rows include final HCl/trace metals, bicarbonate, sodium lactate, and sulfide at stock strengths or ml amounts converted to `G_PER_L`. | MediaDive J1116 curation before J1117 expansion. |

## Recommended Edits

1. Expand J1117 from J1116 by copying the corrected parent and replacing the final NaCl concentration with 60.0 g/L.
2. Change the relationship between J1117 and J1116 from `SOURCE_DUPLICATE` to a variant or parent relationship that records the high-salt override.
3. Keep MediaDive J1117 and TOGO M1195 synchronized so both source records deduplicate into the same corrected high-salt Medium-3 output.

## Follow-up Checks

- Run open schema, strict, reference, and term validation on the corrected specialized owner and regenerated J1117 merged record.
- Re-run exact `mediadive.medium:J1117`, `TOGO:M1195`, and `GRMD=1117` searches with `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`.
- Manually verify that J1117 has 60.0 g/L NaCl and that J1116 remains at its lower NaCl concentration.

## Additional Notes

- The live MediaDive J1117 payload is option-style and contains only the instruction to use Medium 1116 with 60.0 g/L final NaCl.
- The exact source search used `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`.
- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -name '*ird_marine_desulfovibrio_medium_3__249d84d2*.md'` found no pre-existing report for this stem before this report was written.

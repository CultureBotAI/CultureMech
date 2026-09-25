# YAML Record Review: IRD MARINE CLOSTRIDIA MEDIUM-2

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ird_marine_clostridia_medium_2.yaml
- Started UTC: 2026-09-23T15:54:00Z
- Finished UTC: 2026-09-23T15:56:47Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated record | `data/merge_yaml/merged/ird_marine_clostridia_medium_2.yaml` |
| Stable ID | `CultureMech:015427` |
| Label | IRD MARINE CLOSTRIDIA MEDIUM-2 |
| Source identity | MediaDive JCM J938 |
| Source-owned record | `data/normalized_yaml/specialized/ird_marine_clostridia_medium_2.yaml` |

This is generated output from the MediaDive specialized owner after reference-resolution and merge steps. Future fixes belong in `data/normalized_yaml/specialized/ird_marine_clostridia_medium_2.yaml`, duplicate-merge logic, or the already-curated TOGO owner `data/normalized_yaml/bacterial/ird_marine_clostridia_medium_2.yaml`, followed by regeneration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ird_marine_clostridia_medium_2.yaml` | Passed with `No issues found`. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ird_marine_clostridia_medium_2.yaml --out /private/tmp/ird_marine_clostridia_medium_2.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and zero error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ird_marine_clostridia_medium_2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; this file received 0 configured reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ird_marine_clostridia_medium_2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `pkg_resources` warning from `eutils`. |
| Embedded history | Not run | No documented focused validator checks embedded `MediaRecipe.curation_history`; `just validate-history` is scoped to standalone files under `history/`. |

## Identity and Grounding

- The `mediadive.medium:J938` media term and label match the live MediaDive J938 payload and JCM GRMD 938 page.
- Live MediaDive J938 and JCM 938 both define IRD Marine Clostridia Medium-2 as JCM Medium 909 supplemented with 0.164 g/L sodium acetate and 2.0 g/L Trypticase peptone.
- Gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found a curated TOGO M984 owner in `data/normalized_yaml/bacterial/ird_marine_clostridia_medium_2.yaml`; the reviewed generated record still comes from the uncorrected MediaDive owner and is split from that curated TOGO representation.
- The reviewed generated record also merged the J938 supplemented child with `ird_marine_clostrida_medium`, `clostridium_lind_medium`, and `ird_fusibacter_medium`, even though those are the JCM 909 parent or parallel variants, not identical recipes.

## Evidence

- Supported by JCM 938, TOGO M984, and MediaDive J938: this record should carry the JCM 909 base plus 0.164 g/L sodium acetate and 2.0 g/L Trypticase peptone as JCM 938 supplements.
- Supported by the curated TOGO M984 owner: the JCM 909 base should include 940 ml water, base salts and yeast extract, nested JCM 151 trace minerals, 25 ml of 8% bicarbonate, 30 ml of 10% magnesium chloride, 5 ml of 1 M glucose, and 8 ml of 5% sulfide.
- Unsupported in the generated record: neither 0.164 g/L sodium acetate nor 2.0 g/L Trypticase peptone is present among the ingredients, so the record denotes JCM 909-like parent content rather than the JCM 938 supplemented child.
- Unsupported in the generated record: JCM 151 trace-mineral stock components are flattened into final ingredients, and trace-stock NaCl and calcium chloride have been summed with the final-medium NaCl and calcium chloride rows.
- Unsupported in the generated record: bicarbonate, magnesium chloride, glucose, and sulfide stock additions are modeled as final `G_PER_L` ingredients.

## Completeness

- The generated record is missing the two JCM 938-specific supplement rows that distinguish Medium 938 from its Medium 909 parent.
- The generated record has no `ph_value`; that is not itself a defect for JCM 938 because the live JCM 938 source delegates pH and preparation details to the parent JCM 909 recipe.
- The September 12 curated TOGO owner includes references, nested stocks, and sterilization detail that are absent from this MediaDive-based generated record.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Blocker | The generated record omits the ingredients that define JCM 938. | JCM 938 states that JCM Medium 909 is supplemented with 0.164 g/L sodium acetate and 2.0 g/L Trypticase peptone; the generated record contains neither supplement. | `data/normalized_yaml/specialized/ird_marine_clostridia_medium_2.yaml`; MediaDive option-C reference expansion. |
| Major | A supplemented child was merged into its parent and sibling media. | The generated `merged_from` lists `clostridium_lind_medium`, `ird_fusibacter_medium`, `ird_marine_clostrida_medium`, and `ird_marine_clostridia_medium_2`; JCM 938 should be related to but distinct from the JCM 909 parent because it adds two supplements. | `merge_recipes.py` duplicate logic and the specialized normalized owner. |
| Major | JCM 151 trace minerals were flattened at stock strength and then deduplicated against final rows. | The generated NaCl and CaCl2 rows explicitly merge final-medium and trace-minerals-stock values, and the rest of the trace-minerals recipe appears as final ingredients. | MediaDive reference-resolution and stock-boundary handling. |
| Major | Parent JCM 909 stock additions are modeled as final gram-per-liter ingredients. | JCM 909 uses 25 ml 8% bicarbonate, 30 ml 10% magnesium chloride, 5 ml 1 M glucose, and 8 ml 5% sulfide stocks; the generated record emits `25`, `30`, `5`, and `8 G_PER_L` rows. | MediaDive parent expansion and unit normalization. |
| Major | Corrected TOGO M984 content is not reflected in the generated product. | `data/normalized_yaml/bacterial/ird_marine_clostridia_medium_2.yaml` was repaired on 2026-09-12 with the JCM 938 supplements and nested JCM 909/JCM 151 stocks, but the generated record still follows the stale MediaDive fingerprint. | Regeneration and merge selection for TOGO M984/MediaDive J938. |

## Recommended Edits

1. Update `data/normalized_yaml/specialized/ird_marine_clostridia_medium_2.yaml` so JCM 938 keeps its 0.164 g/L sodium acetate and 2.0 g/L Trypticase peptone supplements when it expands the JCM 909 parent.
2. Preserve JCM 938 as a supplemented variant of JCM 909 instead of merging it as an identical recipe with JCM 909, J786, and J991.
3. Use the already-curated TOGO M984 owner as the reference shape for nested JCM 151 trace minerals and JCM 909 bicarbonate, magnesium chloride, glucose, and sulfide stock additions.
4. Regenerate merges so the corrected TOGO M984 and MediaDive J938 source identities deduplicate to one JCM 938 record, not one stale MediaDive record plus one stale TOGO-only suffix record.

## Follow-up Checks

- Run open schema, strict, reference, and term validation on the corrected MediaDive owner, the TOGO M984 owner, and regenerated JCM 938 merged output.
- Manually compare regenerated JCM 938 against the live JCM 938 text and verify that it contains both supplement rows.
- Re-run exact `mediadive.medium:J938`, `TOGO:M984`, and `GRMD=938` searches with `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged` to confirm that the stale split and false parent-child merge are gone.

## Additional Notes

- Live MediaDive J938 only carries the option-style instruction; it does not expose the expanded JCM 909 ingredients in the J938 payload.
- The exact source search used `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`.
- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -name '*ird_marine_clostridia_medium_2*.md'` found no pre-existing report for this stem before this report was written.

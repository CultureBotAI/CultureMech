# YAML Record Review: IRD Marine Clostridia Medium-2

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ird_marine_clostridia_medium_2__b29e94d3.yaml
- Started UTC: 2026-09-23T15:57:00Z
- Finished UTC: 2026-09-23T15:58:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated record | `data/merge_yaml/merged/ird_marine_clostridia_medium_2__b29e94d3.yaml` |
| Stable ID | `CultureMech:010411` |
| Label | IRD Marine Clostridia Medium-2 |
| Source identity | TOGO M984 / JCM 938 |
| Source-owned record | `data/normalized_yaml/bacterial/ird_marine_clostridia_medium_2.yaml` |

This generated output is stale relative to its maintained TOGO owner. The owner was repaired on 2026-09-12, but the generated suffix still shows the pre-repair two-row recipe plus an empty M953 cross-reference solution.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ird_marine_clostridia_medium_2__b29e94d3.yaml` | Passed with `No issues found`. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ird_marine_clostridia_medium_2__b29e94d3.yaml --out /private/tmp/ird_marine_clostridia_medium_2__b29e94d3.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and zero error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ird_marine_clostridia_medium_2__b29e94d3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; this file received 0 configured reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ird_marine_clostridia_medium_2__b29e94d3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `pkg_resources` warning from `eutils`. |
| Embedded history | Not run | No documented focused validator checks embedded `MediaRecipe.curation_history`; `just validate-history` is scoped to standalone files under `history/`. |

## Identity and Grounding

- The `TOGO:M984` term, label, and JCM GRMD 938 source identify IRD Marine Clostridia Medium-2.
- Live JCM 938 and TOGO M984 both define this medium as JCM Medium 909 supplemented with 0.164 g/L sodium acetate and 2.0 g/L Trypticase peptone.
- Gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found this TOGO M984 record split from the MediaDive J938 representation in `data/normalized_yaml/specialized/ird_marine_clostridia_medium_2.yaml` and the generated `data/merge_yaml/merged/ird_marine_clostridia_medium_2.yaml`.

## Evidence

- Supported by JCM 938 and TOGO M984: sodium acetate and Trypticase peptone are direct JCM 938 supplement rows, and the remaining formulation should come from the JCM 909 parent medium.
- Supported by the current maintained owner: the September 12 repair expanded the JCM 909 base, nested JCM 151 trace minerals, and represented 8% bicarbonate, 10% magnesium chloride, 1 M glucose, and 5% sulfide as quantified stock solutions.
- Unsupported in this generated record: the JCM 909 parent is only an empty `Unknown solution` with a `1 G_PER_L` concentration.

## Completeness

- This generated record lacks every JCM 909 base ingredient, nested stock solution, JCM 151 trace-minerals component, and preparation step now present in its maintained owner.
- The current maintained owner has source URLs for TOGO M984, JCM 938, TOGO M953, JCM 909, TOGO M142, and JCM 151; none are present in this stale generated suffix.
- Empty target-organism and literature-evidence arrays are not defects for this source recipe.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to its repaired owner. | `data/normalized_yaml/bacterial/ird_marine_clostridia_medium_2.yaml` now contains expanded JCM 909/JCM 151 content and a 2026-09-12 repair history entry; the generated suffix still contains only sodium acetate, Trypticase peptone, and an empty M953 placeholder from the pre-repair import. | Regenerate merges from `data/normalized_yaml/bacterial/ird_marine_clostridia_medium_2.yaml`. |
| Major | The JCM 909 parent remains an empty solution placeholder. | Live JCM 938 delegates the parent formula to JCM Medium 909, but the generated record leaves `IRD MARINE CLOSTRIDA MEDIUM (see Medium [M953])` with `composition: []` and `1 G_PER_L`. | Regeneration after the existing TOGO M984 repair; parent-reference expansion. |
| Major | The TOGO M984 and MediaDive J938 generated outputs are split. | Exact ignored-inclusive search found the TOGO record in this suffix and the MediaDive record in `ird_marine_clostridia_medium_2.yaml`, even though both represent JCM GRMD 938. | `merge_recipes.py` duplicate detection after MediaDive and TOGO owners are aligned. |

## Recommended Edits

1. Regenerate generated merges from the September 12 TOGO M984 owner so this suffix no longer reflects the pre-repair empty M953 placeholder.
2. Align `data/normalized_yaml/specialized/ird_marine_clostridia_medium_2.yaml` with the corrected TOGO M984 owner for JCM 938 expansion.
3. Deduplicate TOGO M984 with MediaDive J938 while keeping JCM 938 distinct from its JCM 909 parent.

## Follow-up Checks

- Run open schema, strict, reference, and term validation on regenerated JCM 938 output.
- Re-run exact `TOGO:M984`, `mediadive.medium:J938`, and `GRMD=938` searches with `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged` to confirm that the split stale suffix is gone.
- Manually verify the regenerated record against JCM 938 for the two supplement rows and against the repaired owner for the expanded JCM 909/JCM 151 stock structure.

## Additional Notes

- The exact source search used `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`.
- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -name '*ird_marine_clostridia_medium_2__b29e94d3*.md'` found no pre-existing report for this stem before this report was written.

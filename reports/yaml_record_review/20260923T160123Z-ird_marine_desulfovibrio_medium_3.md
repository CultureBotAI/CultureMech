# YAML Record Review: IRD Marine Desulfovibrio Medium-3

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ird_marine_desulfovibrio_medium_3.yaml
- Started UTC: 2026-09-23T15:59:00Z
- Finished UTC: 2026-09-23T16:01:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated record | `data/merge_yaml/merged/ird_marine_desulfovibrio_medium_3.yaml` |
| Stable ID | `CultureMech:007721` |
| Label | IRD Marine Desulfovibrio Medium-3 |
| Source identity | TOGO M1195 / JCM 1117 |
| Source-owned record | `data/normalized_yaml/bacterial/ird_marine_desulfovibrio_medium_3.yaml` |

This generated record merged TOGO M1195 with the lower-salt TOGO M1194 sibling. Future fixes belong in the two `data/normalized_yaml/bacterial/ird_marine_desulfovibrio_medium_*.yaml` owners and in duplicate-merge logic, not in the generated merge output.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ird_marine_desulfovibrio_medium_3.yaml` | Passed with `No issues found`. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ird_marine_desulfovibrio_medium_3.yaml --out /private/tmp/ird_marine_desulfovibrio_medium_3.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and zero error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ird_marine_desulfovibrio_medium_3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; this file received 0 configured reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ird_marine_desulfovibrio_medium_3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `pkg_resources` warning from `eutils`. |
| Embedded history | Not run | No documented focused validator checks embedded `MediaRecipe.curation_history`; `just validate-history` is scoped to standalone files under `history/`. |

## Identity and Grounding

- The `TOGO:M1195` term, JCM 1117 source URL, and label identify IRD Marine Desulfovibrio Medium-3.
- Live JCM 1117 and MediaDive J1117 define Medium-3 as Medium 1116 with 60.0 g/L final NaCl.
- Gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found this TOGO M1195 record, the lower-salt TOGO M1194 sibling that was merged into it, and a separate MediaDive J1117 generated suffix.

## Evidence

- Supported by TOGO M1195: the final recipe contains 920 ml distilled water, 60 g NaCl, yeast extract, calcium chloride, `KH2PO4`, `NH4Cl`, 1 mg resazurin, magnesium chloride, KCl, sodium sulfate, L-cysteine HCl hydrate, 1 ml trace element solution, 40 ml 5% bicarbonate, 20 ml 1 M sodium lactate, and 8 ml 5% sulfide.
- Supported by JCM 1117 and MediaDive J1117: Medium-3 is a high-salt variant of Medium 1116 with 60.0 g/L final NaCl.
- Unsupported in the generated record: NaCl is `30 G_PER_L`, inherited from the lower-salt Medium-2/M1194 sibling, so the generated formula is not M1195/JCM 1117.
- Unsupported in the generated record: N2 and carbon dioxide are final variable ingredients even though the source uses N2-CO2 and N2 as procedural gas atmospheres.
- Unsupported in the generated record: 20 ml of 1 M sodium lactate is modeled as a `20 G_PER_L` final ingredient.

## Completeness

- The trace element, 5% bicarbonate, and 5% sulfide stocks are empty `Unknown solution` rows with ml addition volumes stored as `G_PER_L`.
- The M1195 preparation comments are absent, including pH 7.0 adjustment, boiling, N2-CO2 cooling, anaerobic distribution, post-autoclave additions, and N2 storage of the sulfide stock.
- Empty target-organism, literature-evidence, and discussion arrays are not defects for this source recipe.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Blocker | The canonical generated record has the wrong NaCl concentration for JCM 1117. | TOGO M1195 and JCM 1117 specify 60 g/L final NaCl; the generated record merged M1195 with M1194 and retained `30 G_PER_L`. | `merge_recipes.py` duplicate logic and `data/normalized_yaml/bacterial/ird_marine_desulfovibrio_medium_3.yaml`. |
| Major | Medium-2 and Medium-3 were merged as duplicates even though the latter is the high-salt variant. | The generated `merged_from` contains both `ird_marine_desulfovibrio_medium_2` and `_3`, while JCM 1117 is explicitly Medium 1116 with 60.0 g/L final NaCl. | TOGO duplicate detection and variant modeling for M1194/M1195. |
| Major | Stock boundaries were lost. | TOGO M1195 lists 1 ml trace element solution, 40 ml 5% bicarbonate, and 8 ml 5% sulfide as solution additions; the generated record has three empty `Unknown solution` rows with `1`, `40`, and `8 G_PER_L`. | `data/normalized_yaml/bacterial/ird_marine_desulfovibrio_medium_3.yaml`; TOGO solution migration. |
| Major | Lactate and gas handling are represented as final reagents. | The source lists 20 ml 1 M sodium lactate and uses N2-CO2/N2 as atmospheres; the generated record stores `1 M Sodium lactate` as `20 G_PER_L` and gas rows as variable ingredients. | TOGO importer and solution migration. |
| Major | Preparation details are absent. | The generated record has no `preparation_steps`, but TOGO M1195 has two preparation comments covering pH 7.0, boiling, gas handling, autoclaving, post-autoclave additions, and final reduction. | TOGO comment import. |

## Recommended Edits

1. Split M1195/JCM 1117 from M1194/JCM 1116 and preserve 60 g/L final NaCl on Medium-3.
2. Model M1195's trace element, bicarbonate, lactate, and sulfide stocks as scoped volume additions instead of final `G_PER_L` rows.
3. Move N2-CO2 and N2 into preparation or atmosphere context, and import the pH 7.0 and anaerobic handling steps.
4. Align the MediaDive J1117 suffix with the corrected TOGO shape so both sources can deduplicate without collapsing the high-salt variant into Medium-2.

## Follow-up Checks

- Run open schema, strict, reference, and term validation on the corrected M1194 and M1195 owners and the regenerated merged records.
- Re-run exact `TOGO:M1195`, `TOGO:M1194`, `mediadive.medium:J1117`, and `GRMD=1117` searches with `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged` to confirm that the high-salt variant is no longer merged with Medium-2.
- Manually compare regenerated Medium-3 against JCM 1117 for the 60 g/L NaCl final amount and against TOGO M1195 for the complete anaerobic stock-addition sequence.

## Additional Notes

- The live MediaDive J1117 payload is an option-style record with only the instruction to use Medium 1116 at 60.0 g/L final NaCl.
- The exact source search used `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`.
- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -name '*ird_marine_desulfovibrio_medium_3*.md'` found no pre-existing report for this stem before this report was written.

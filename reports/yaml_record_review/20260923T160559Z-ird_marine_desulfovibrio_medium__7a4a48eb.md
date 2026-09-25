# YAML Record Review: IRD MARINE DESULFOVIBRIO MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ird_marine_desulfovibrio_medium__7a4a48eb.yaml
- Started UTC: 2026-09-23T16:03:00Z
- Finished UTC: 2026-09-23T16:05:59Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated record | `data/merge_yaml/merged/ird_marine_desulfovibrio_medium__7a4a48eb.yaml` |
| Stable ID | `CultureMech:015374` |
| Label | IRD MARINE DESULFOVIBRIO MEDIUM |
| Source identity | MediaDive JCM J1043 |
| Source-owned record | `data/normalized_yaml/specialized/ird_marine_desulfovibrio_medium.yaml` |

This generated record was produced from the MediaDive normalized owner only. Future fixes belong in `data/normalized_yaml/specialized/ird_marine_desulfovibrio_medium.yaml`, MediaDive stock import, and duplicate detection with TOGO M1108.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ird_marine_desulfovibrio_medium__7a4a48eb.yaml` | Passed with `No issues found`. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ird_marine_desulfovibrio_medium__7a4a48eb.yaml --out /private/tmp/ird_marine_desulfovibrio_medium__7a4a48eb.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and zero error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ird_marine_desulfovibrio_medium__7a4a48eb.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; this file received 0 configured reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ird_marine_desulfovibrio_medium__7a4a48eb.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `pkg_resources` warning from `eutils`. |
| Embedded history | Not run | No documented focused validator checks embedded `MediaRecipe.curation_history`; `just validate-history` is scoped to standalone files under `history/`. |

## Identity and Grounding

- The `mediadive.medium:J1043` term, source URL, pH 7.0, and label match live MediaDive J1043.
- Live JCM 1043 confirms the same visible formulation and post-autoclave additions.
- A gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found a second TOGO M1108 owner and generated output for the same GRMD 1043 source.

## Evidence

- Supported by MediaDive J1043 and JCM 1043: the 1009 ml main recipe contains 920 ml distilled water, 1 g `NH4Cl`, 0.3 g `KH2PO4`, 0.3 g `K2HPO4`, 25 g NaCl, 0.1 g KCl, 0.1 g calcium chloride dihydrate, 4 g sodium sulfate, 1 g BD-Difco yeast extract, 1 ml trace element solution, 0.5 g L-cysteine HCl hydrate, and 1 mg resazurin.
- Supported by MediaDive J1043 and JCM 1043: after autoclaving under N2-CO2, the medium receives 20 ml 1 M sodium lactate, 20 ml 15% magnesium chloride, and 40 ml 5% bicarbonate; prior to use it receives 8 ml 5% sulfide.
- Supported by MediaDive J1043: trace element solution is a separate 1000 ml stock containing 987 ml water, 12.5 ml 25% HCl, and the trace metal salts.
- Unsupported in the generated record: the trace-element stock is flattened into final HCl and metal-salt ingredients.
- Unsupported in the generated record: sodium lactate, magnesium chloride, bicarbonate, and sulfide stock additions are represented as `20`, `20`, `40`, and `8 G_PER_L` final ingredients.

## Completeness

- The 920 ml main water row and 987 ml trace-element water row are missing.
- The source pH 7.0 and two preparation comments are present.
- Empty target-organism, literature-evidence, and discussion arrays are not defects for this source recipe.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Trace element solution was flattened into final ingredients. | MediaDive J1043 has a 1 ml addition of solution 4186; the generated record lists HCl, FeSO4, H3BO3, MnCl2, CoCl2, NiCl2, CuCl2, ZnSO4, and Na2MoO4 as top-level ingredients at stock strength. | `data/normalized_yaml/specialized/ird_marine_desulfovibrio_medium.yaml`; MediaDive solution migration. |
| Major | Four post-autoclave stocks have wrong final units. | JCM/MediaDive list 20 ml 1 M sodium lactate, 20 ml 15% magnesium chloride, 40 ml 5% bicarbonate, and 8 ml 5% sulfide; the generated record stores those as `G_PER_L` ingredients. | `data/normalized_yaml/specialized/ird_marine_desulfovibrio_medium.yaml`; MediaDive unit normalization. |
| Major | Distilled-water rows were dropped. | MediaDive lists 920 ml water in the main recipe and 987 ml water in the trace-element stock; neither appears in the generated MediaDive record. | MediaDive water-row import logic. |
| Major | MediaDive J1043 and TOGO M1108 are unmerged duplicates. | Exact ignored-inclusive search found separate MediaDive and TOGO owners plus separate generated records for GRMD 1043. | Source-deduplication and `merge_recipes.py`, after both owners are corrected. |

## Recommended Edits

1. Re-nest MediaDive solution 4186 under the 1009 ml `Main sol. J1043` recipe as a 1 ml trace-element addition.
2. Restore the 920 ml final water row and 987 ml trace-element water row.
3. Preserve sodium lactate, magnesium chloride, bicarbonate, and sulfide as scoped stock-volume additions rather than final `G_PER_L` ingredients.
4. Align MediaDive J1043 with TOGO M1108 so both GRMD 1043 imports deduplicate after correction.

## Follow-up Checks

- Run open schema, strict, reference, and term validation on corrected J1043 normalized owners and regenerated merged output.
- Re-run exact `mediadive.medium:J1043`, `TOGO:M1108`, and `GRMD=1043` searches with `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`.
- Manually compare the regenerated main recipe against JCM 1043 and MediaDive solution 5103, and compare the trace-element stock against MediaDive solution 4186.

## Additional Notes

- The TOGO M1108 generated sibling has complementary importer damage: it preserves main water but lacks structured preparation, turns procedural gases into variable ingredients, and leaves trace element, bicarbonate, magnesium chloride, and sulfide as empty `Unknown solution` rows.
- The exact source search used `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`.
- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -name '*ird_marine_desulfovibrio_medium__7a4a48eb*.md'` found no pre-existing report for this stem before this report was written.

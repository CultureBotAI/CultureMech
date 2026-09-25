# YAML Record Review: IRD DESULFOCURVUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ird_desulfocurvus_medium__cacbbe37.yaml
- Started UTC: 2026-09-23T15:44:00Z
- Finished UTC: 2026-09-23T15:48:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated record | `data/merge_yaml/merged/ird_desulfocurvus_medium__cacbbe37.yaml` |
| Stable ID | `CultureMech:003301` |
| Label | IRD DESULFOCURVUS MEDIUM |
| Source identity | MediaDive JCM J953 |
| Source-owned record | `data/normalized_yaml/bacterial/ird_desulfocurvus_medium.yaml` |

This generated record was produced from the MediaDive normalized owner only. Future fixes belong in `data/normalized_yaml/bacterial/ird_desulfocurvus_medium.yaml`, MediaDive stock-solution import logic, or duplicate detection, followed by regeneration of the merged YAML.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ird_desulfocurvus_medium__cacbbe37.yaml` | Passed with `No issues found`. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ird_desulfocurvus_medium__cacbbe37.yaml --out /private/tmp/ird_desulfocurvus_medium__cacbbe37.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and zero error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ird_desulfocurvus_medium__cacbbe37.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; this file received 0 configured reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ird_desulfocurvus_medium__cacbbe37.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `pkg_resources` warning from `eutils`. |
| Embedded history | Not run | No documented focused validator checks embedded `MediaRecipe.curation_history`; `just validate-history` is scoped to standalone files under `history/`. |

## Identity and Grounding

- The `mediadive.medium:J953` term, source link, pH 7.2, and label match the live MediaDive REST record for J953.
- The live JCM GRMD 953 page resolves and confirms the same IRD Desulfocurvus visible formulation and stock-addition sequence.
- A gitignore-independent exact search over `data/normalized_yaml/bacterial` and `data/merge_yaml/merged` found the same JCM GRMD 953 source imported from TOGO as M1000 in `data/normalized_yaml/bacterial/TOGO_M1000_IRD_Desulfocurvus_Medium.yaml` and generated as `data/merge_yaml/merged/IRD_DESULFOCURVUS_MEDIUM.yaml`.

## Evidence

- Supported by MediaDive J953 and JCM 953: the main medium has a 1054 ml final volume and includes 1000 ml distilled water, 0.3 g `KH2PO4`, 0.3 g `K2HPO4`, 1 g `NH4Cl`, 2 g NaCl, 0.1 g KCl, 0.1 g calcium chloride dihydrate, 0.5 g magnesium chloride hexahydrate, 1 ml trace element solution, 1 g yeast extract, 3.16 g sodium thiosulfate pentahydrate, 0.5 g L-cysteine HCl hydrate, and 0.5 mg resazurin.
- Supported by MediaDive J953 and JCM 953: after autoclaving under N2-CO2, the recipe adds 25 ml 8% `NaHCO3` and 20 ml 1 M sodium lactate from anaerobic stocks, then adds 8 ml 5% `Na2S x 9H2O` before inoculation.
- Supported by MediaDive J953: trace element solution is a separate 1000 ml stock containing 12.5 ml 25% HCl, iron sulfate, boric acid, manganese chloride, cobalt chloride, nickel chloride, copper chloride, zinc sulfate, sodium molybdate, and 987 ml distilled water.
- Unsupported in the generated record: the trace-element stock is flattened into top-level final ingredients at stock concentration.
- Unsupported in the generated record: the 25 ml bicarbonate stock, 20 ml 1 M sodium lactate stock, and 8 ml sulfide stock are represented as `25`, `20`, and `8 G_PER_L` top-level ingredients.

## Completeness

- The 1000 ml final distilled-water row and 987 ml trace-element stock water row are absent.
- The source pH and preparation text are present and retain the two relevant anaerobic handling phases.
- Empty target-organism, literature-evidence, and discussion arrays are not defects for this imported source recipe.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Trace element solution was flattened into the final medium. | MediaDive J953 has a 1 ml addition of solution 4186; the generated record lists HCl, FeSO4, H3BO3, MnCl2, CoCl2, NiCl2, CuCl2, ZnSO4, and Na2MoO4 as top-level final ingredients at stock strength. | `data/normalized_yaml/bacterial/ird_desulfocurvus_medium.yaml`; MediaDive solution importer/migrator. |
| Major | Three anaerobic stock additions have wrong final units. | JCM/MediaDive list 25 ml of 8% bicarbonate, 20 ml of 1 M sodium lactate, and 8 ml of 5% sodium sulfide; the generated record stores those as `25`, `20`, and `8 G_PER_L`. | `data/normalized_yaml/bacterial/ird_desulfocurvus_medium.yaml`; MediaDive unit normalization. |
| Major | Distilled-water rows were dropped. | MediaDive lists 1000 ml water in the main 1054 ml medium and 987 ml water in trace element solution; neither row appears in the generated MediaDive record. | `data/normalized_yaml/bacterial/ird_desulfocurvus_medium.yaml`; MediaDive water-row import logic. |
| Major | The MediaDive J953 and TOGO M1000 records are unmerged duplicates. | Both owners use GRMD 953 for IRD Desulfocurvus Medium, but exact ignored-inclusive search found two normalized owners and two generated records. | Source-deduplication and `merge_recipes.py`, after both owners are corrected. |
| Minor | The JCM 439 trace-element relationship is not retained structurally. | JCM 953 links trace element solution to JCM medium 439 and MediaDive exposes the same stock as solution 4186; the generated record only has flattened stock components. | MediaDive stock-reference handling. |

## Recommended Edits

1. Re-nest MediaDive solution 4186 under the 1054 ml `Main sol. J953` recipe as a 1 ml trace-element addition.
2. Restore the 1000 ml final water row and 987 ml trace-element stock water row.
3. Preserve 25 ml 8% bicarbonate, 20 ml 1 M sodium lactate, and 8 ml 5% sulfide as anaerobic stock additions rather than final `G_PER_L` ingredients.
4. Keep pH 7.2, N2-CO2 autoclaving, and N2-CO2 vessel distribution as preparation or atmosphere context, not as reagent rows.
5. Correct the TOGO M1000 sibling, then merge or explicitly relate the two GRMD 953 imports.

## Follow-up Checks

- Run open schema, strict, reference, and term validation on the corrected MediaDive owner and regenerated merged record.
- Manually compare the regenerated main recipe against MediaDive J953 solution 4975 and the live JCM 953 table; compare the trace-element stock against MediaDive solution 4186.
- Re-run exact `mediadive.medium:J953`, `TOGO:M1000`, and `GRMD=953` searches with `rg --no-ignore --hidden` over `data/normalized_yaml/bacterial` and `data/merge_yaml/merged` to confirm duplicate handling.

## Additional Notes

- The TOGO M1000 generated sibling preserves the source's 1 L water row only as `1 G_PER_L`, turns N2 and carbon dioxide atmosphere text into variable ingredients, and leaves four stock additions as empty `Unknown solution` rows.
- The exact duplicate search used `rg --no-ignore --hidden` over `data/normalized_yaml/bacterial` and `data/merge_yaml/merged`.
- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -name '*ird_desulfocurvus_medium__cacbbe37*.md'` found no pre-existing report for this stem before this report was written.

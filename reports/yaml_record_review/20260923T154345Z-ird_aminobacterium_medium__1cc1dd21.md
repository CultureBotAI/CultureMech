# YAML Record Review: IRD AMINOBACTERIUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ird_aminobacterium_medium__1cc1dd21.yaml
- Started UTC: 2026-09-23T15:39:00Z
- Finished UTC: 2026-09-23T15:43:45Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated record | `data/merge_yaml/merged/ird_aminobacterium_medium__1cc1dd21.yaml` |
| Stable ID | `CultureMech:003338` |
| Label | IRD AMINOBACTERIUM MEDIUM |
| Source identity | MediaDive JCM J989 |
| Source-owned record | `data/normalized_yaml/bacterial/ird_aminobacterium_medium.yaml` |

This generated record was produced from the MediaDive normalized owner only. Future fixes belong in `data/normalized_yaml/bacterial/ird_aminobacterium_medium.yaml`, in the MediaDive importer or stock-solution migrator, or in duplicate detection, followed by regeneration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ird_aminobacterium_medium__1cc1dd21.yaml` | Passed. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ird_aminobacterium_medium__1cc1dd21.yaml --out /private/tmp/ird_aminobacterium_medium__1cc1dd21.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and zero error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ird_aminobacterium_medium__1cc1dd21.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with no reported failures. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ird_aminobacterium_medium__1cc1dd21.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `pkg_resources` warning from `eutils`. |
| Embedded history | Not run | No documented focused validator checks embedded `MediaRecipe.curation_history`; `just validate-history` is scoped to standalone files under `history/`. |

## Identity and Grounding

- The `mediadive.medium:J989` term, JCM source link, pH 7.2, and label match the live MediaDive REST record for J989.
- The live JCM GRMD 989 page resolves and confirms the same IRD Aminobacterium source recipe, including references to JCM 439 trace element solution and JCM 431 selenite-tungstate solution.
- A gitignore-independent exact search over `data/normalized_yaml/bacterial` and `data/merge_yaml/merged` found the same JCM GRMD 989 source imported from TOGO as M1042 in `data/normalized_yaml/bacterial/TOGO_M1042_IRD_Aminobacterium_Medium.yaml` and `data/merge_yaml/merged/IRD_AMINOBACTERIUM_MEDIUM.yaml`.

## Evidence

- Supported by MediaDive J989 and JCM 989: the 1002 ml main solution contains 945 ml distilled water, 1 g `NH4Cl`, 0.3 g `KH2PO4`, 0.3 g `K2HPO4`, 20 g NaCl, 0.1 g KCl, 0.1 g calcium chloride dihydrate, 1 g L-serine, 2 g BD-Difco yeast extract, 1 ml trace element solution, 1 ml selenite-tungstate solution, 0.5 g L-cysteine HCl hydrate, and 0.5 mg resazurin.
- Supported by MediaDive J989 and JCM 989: after boiling, cooling under N2-CO2, sealing, and autoclaving, the recipe adds 20 ml 15% `MgCl2 x 6H2O`, 25 ml 8% `NaHCO3`, and 10 ml 5% `Na2S x 9H2O` as stock solutions, then readjusts pH to 7.2 if necessary.
- Supported by MediaDive J989: the trace-element and selenite-tungstate stocks are separate 1000 ml solution recipes; the JCM page links to the same solution recipes as medium numbers 439 and 431.
- Unsupported in the generated record: the trace-element and selenite-tungstate stock contents are flattened as top-level ingredients at stock concentration, including HCl, iron sulfate, boric acid, manganese chloride, cobalt chloride, nickel chloride, copper chloride, zinc sulfate, sodium molybdate, NaOH, selenite, and tungstate.
- Unsupported in the generated record: the 20 ml magnesium chloride stock, 25 ml bicarbonate stock, and 10 ml sulfide stock are represented as `20`, `25`, and `10 G_PER_L` final ingredients.

## Completeness

- The 945 ml final distilled-water row, 987 ml trace-element water row, and 1000 ml selenite-tungstate water row are absent.
- The two source preparation comments are present and preserve pH 7.2, boiling, gas stream, autoclaving, anaerobic stock addition, and pH readjustment context.
- Empty target-organism, literature-evidence, and discussion arrays are not defects for this imported source recipe.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Trace-element and selenite-tungstate stock recipes were flattened into the final medium. | MediaDive J989 has final 1 ml additions of solution IDs 4186 and 4172, while the generated record exposes their HCl, metal-salt, NaOH, selenite, and tungstate components as top-level final ingredients. | `data/normalized_yaml/bacterial/ird_aminobacterium_medium.yaml`; MediaDive solution importer/migrator. |
| Major | Three post-autoclave stock additions have wrong final units. | JCM/MediaDive list 20 ml of 15% magnesium chloride, 25 ml of 8% bicarbonate, and 10 ml of 5% sodium sulfide; the generated record stores those as `20`, `25`, and `10 G_PER_L`. | `data/normalized_yaml/bacterial/ird_aminobacterium_medium.yaml`; MediaDive unit normalization. |
| Major | Scoped water rows were dropped. | MediaDive J989 lists 945 ml distilled water in the final medium plus 987 ml and 1000 ml water rows in the trace-element and selenite-tungstate stocks; no water row appears in the generated MediaDive record. | `data/normalized_yaml/bacterial/ird_aminobacterium_medium.yaml`; MediaDive water-row import logic. |
| Major | The MediaDive J989 and TOGO M1042 imports are unmerged duplicates. | Both owners use GRMD 989 for IRD Aminobacterium Medium, but exact ignored-inclusive search found two normalized owners and two generated records. | Source-deduplication and `merge_recipes.py`, after both owners are corrected. |
| Minor | MediaDive stock solution links are not retained structurally. | The source names trace element solution and selenite-tungstate solution as stock additions; the generated record neither nests MediaDive solution IDs 4186/4172 nor links the equivalent JCM 439/431 recipes. | MediaDive stock-reference handling. |

## Recommended Edits

1. Re-nest MediaDive solution IDs 4186 and 4172 under the 1002 ml `Main sol. J989` recipe instead of emitting their stock-strength ingredients as final ingredients.
2. Restore the 945 ml main water, 987 ml trace-element water, and 1000 ml selenite-tungstate water rows under their proper scopes.
3. Preserve 20 ml 15% magnesium chloride, 25 ml 8% bicarbonate, and 10 ml 5% sulfide as post-autoclave stock additions, not gram-per-liter final ingredients.
4. Keep the JCM/MediaDive pH 7.2 and anaerobic stock-addition preparation text attached to the final recipe.
5. Correct `data/normalized_yaml/bacterial/TOGO_M1042_IRD_Aminobacterium_Medium.yaml`, then let duplicate detection merge or intentionally cross-link the two GRMD 989 records.

## Follow-up Checks

- Run open schema, strict, reference, and term validation on the corrected MediaDive owner and regenerated merged record.
- Manually compare the regenerated main recipe against MediaDive J989 solution 5019 and the JCM 989 table, then compare stock recipes against MediaDive solutions 4186 and 4172.
- Re-run exact `mediadive.medium:J989`, `TOGO:M1042`, and `GRMD=989` searches with `rg --no-ignore --hidden` over `data/normalized_yaml/bacterial` and `data/merge_yaml/merged` to confirm duplicate handling.

## Additional Notes

- The TOGO M1042 generated sibling retains the 945 ml water row and JCM 439/431 cross-reference labels but lacks structured pH/preparation details, turns the N2-CO2 procedural gas mixture into variable ingredients, and leaves five stock additions as empty `Unknown solution` rows.
- The exact duplicate search used `rg --no-ignore --hidden` over `data/normalized_yaml/bacterial` and `data/merge_yaml/merged`.
- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -name '*ird_aminobacterium_medium__1cc1dd21*.md'` found no pre-existing report for this stem before this report was written.

# YAML Record Review: IRD ALKALIPHILUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ird_alkaliphilus_medium__f7529ed2.yaml
- Started UTC: 2026-09-23T15:33:00Z
- Finished UTC: 2026-09-23T15:38:36Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated record | `data/merge_yaml/merged/ird_alkaliphilus_medium__f7529ed2.yaml` |
| Stable ID | `CultureMech:003285` |
| Label | IRD ALKALIPHILUS MEDIUM |
| Source identity | MediaDive JCM J937 |
| Source-owned record | `data/normalized_yaml/bacterial/ird_alkaliphilus_medium.yaml` |

This generated record was produced from the MediaDive normalized owner only. Future fixes belong in `data/normalized_yaml/bacterial/ird_alkaliphilus_medium.yaml`, in MediaDive import/solution handling, or in duplicate-merge logic, followed by regeneration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ird_alkaliphilus_medium__f7529ed2.yaml` | Passed with `No issues found`. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ird_alkaliphilus_medium__f7529ed2.yaml --out /private/tmp/ird_alkaliphilus_medium__f7529ed2.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and zero error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ird_alkaliphilus_medium__f7529ed2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; this file received 0 configured reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ird_alkaliphilus_medium__f7529ed2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `pkg_resources` warning from `eutils`. |
| Embedded history | Not run | No documented focused validator checks embedded `MediaRecipe.curation_history`; `just validate-history` is scoped to standalone files under `history/`. |

## Identity and Grounding

- The `mediadive.medium:J937` term, JCM source, pH 8.5, and label match the live MediaDive REST record for J937.
- The live JCM GRMD 937 page resolves and confirms the same visible IRD Alkaliphilus recipe: a base medium, 75 ml 8% bicarbonate, 40 ml 0.025 M crotonic acid at pH 7.0, and 8 ml 5% sodium sulfide stock per liter.
- A gitignore-independent exact search over `data/normalized_yaml/bacterial` and `data/merge_yaml/merged` found a second maintained owner, `data/normalized_yaml/bacterial/TOGO_M983_IRD_Alkaliphilus_Medium.yaml`, and a second generated record, `data/merge_yaml/merged/IRD_ALKALIPHILUS_MEDIUM.yaml`, for the same JCM GRMD 937 source.

## Evidence

- Supported by MediaDive J937 and JCM 937: the main solution has a final volume of 1018 ml and includes 885 ml distilled water, 0.3 g `KH2PO4`, 0.3 g `K2HPO4`, 0.5 g `NH4Cl`, 5 g NaCl, 0.1 g KCl, 0.1 g calcium chloride dihydrate, 0.5 g magnesium chloride hexahydrate, 0.164 g sodium acetate, 10 ml trace minerals, 5 g yeast extract, 5 g BD-BBL Trypticase peptone, 0.5 g L-cysteine HCl hydrate, and 1 mg resazurin.
- Supported by MediaDive J937 and JCM 937: after autoclaving under N2-CO2, the medium receives 75 ml 8% `NaHCO3` and 40 ml 0.025 M crotonic acid, and 8 ml 5% `Na2S x 9 H2O` stock is added from an anaerobic stock before inoculation.
- Supported by MediaDive J937: trace minerals are a separate 1000 ml stock containing nitrilotriacetic acid, magnesium sulfate, manganese sulfate, NaCl, iron sulfate, cobalt sulfate, calcium chloride, zinc sulfate, copper sulfate, potassium aluminium sulfate, boric acid, sodium molybdate, and distilled water.
- Unsupported in the generated record: trace-mineral stock components are modeled as final ingredients at stock concentration, and the trace-stock NaCl and calcium chloride were merged with the final-medium NaCl and calcium chloride rows.
- Unsupported in the generated record: 75 ml 8% bicarbonate, 40 ml crotonic-acid stock, and 8 ml 5% sodium sulfide stock are modeled as `75`, `40`, and `8 G_PER_L` final ingredients.

## Completeness

- The generated record omits the 885 ml distilled-water row from the 1018 ml main solution and the 1000 ml water row from trace minerals.
- The MediaDive payload includes the 1000 ml trace-minerals stock recipe; the generated record has no nested stock or stock-level preparation scope.
- Empty target-organism, literature-evidence, and discussion arrays are not defects for this imported source recipe.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The 10 ml trace-minerals addition was flattened into final ingredients at stock strength. | MediaDive J937 exposes trace minerals as solution 3804, a 1000 ml stock; the generated record lists its nitrilotriacetic acid, MgSO4, MnSO4, FeSO4, CoSO4, ZnSO4, CuSO4, AlK(SO4)2, H3BO3, and Na2MoO4 rows as top-level ingredients. | `data/normalized_yaml/bacterial/ird_alkaliphilus_medium.yaml`; MediaDive solution importer/migrator. |
| Major | NaCl and calcium chloride were merged across unrelated recipe scopes. | The generated record reports merged NaCl `5.91159 G_PER_L` from `4.91159` and `1.0`, and merged calcium chloride `0.1982318 G_PER_L` from `0.0982318` and `0.1`; those source rows belong to the final medium and the undiluted trace-minerals stock, respectively. | Data-quality duplicate merging and MediaDive stock-boundary handling. |
| Major | Three stock additions have incorrect final units. | JCM/MediaDive list 75 ml of 8% bicarbonate, 40 ml of 0.025 M crotonic acid, and 8 ml of 5% sodium sulfide; the generated record stores them as `75`, `40`, and `8 G_PER_L`. | `data/normalized_yaml/bacterial/ird_alkaliphilus_medium.yaml`; MediaDive unit normalization. |
| Major | The TOGO and MediaDive imports for JCM 937 are unmerged duplicates. | TOGO M983 and MediaDive J937 share the same GRMD 937 source but exact ignored-inclusive search found two normalized owners and two generated records. | Source-deduplication and `merge_recipes.py`, after the two owners are corrected. |
| Minor | Water rows are missing from both the main recipe and the stock recipe. | The live MediaDive payload lists 885 ml distilled water in `Main sol. J937` and 1000 ml in `Trace minerals`, but the generated MediaDive record has no water ingredient. | `data/normalized_yaml/bacterial/ird_alkaliphilus_medium.yaml`; MediaDive water-row import logic. |

## Recommended Edits

1. Re-nest MediaDive solution 3804 as a trace-minerals stock used at 10 ml in `Main sol. J937`; keep stock-specific NaCl and calcium chloride separate from the final-medium rows.
2. Restore the 885 ml final water row and 1000 ml trace-minerals water row in their proper scopes.
3. Preserve the 75 ml bicarbonate, 40 ml crotonic-acid, and 8 ml sulfide stock additions as volume additions with their stated stock concentrations.
4. Re-compare the corrected MediaDive owner against JCM 937 for visible formulation and against MediaDive J937 for the trace-minerals stock that JCM only links.
5. Correct the paired TOGO M983 owner, then merge or explicitly relate the two generated JCM 937 records.

## Follow-up Checks

- Run open schema, strict, reference, and term validation on the corrected normalized owner and regenerated merged record.
- Manually compare the regenerated ingredient scopes against MediaDive J937 solution 4949 and trace-minerals solution 3804.
- Re-run exact `mediadive.medium:J937`, `TOGO:M983`, and `GRMD=937` searches with `rg --no-ignore --hidden` over `data/normalized_yaml/bacterial` and `data/merge_yaml/merged` to confirm that duplicate handling is resolved or documented.

## Additional Notes

- The TOGO M983 generated sibling has different importer damage: it keeps the base 885 ml water row but converts 1 mg resazurin to `1 G_PER_L`, turns N2 and N2-CO2 atmosphere text into variable gas ingredients, and leaves four stock additions as empty `Unknown solution` rows.
- The exact duplicate search used `rg --no-ignore --hidden` over `data/normalized_yaml/bacterial` and `data/merge_yaml/merged`.
- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -name '*ird_alkaliphilus_medium__f7529ed2*.md'` found no pre-existing report for this stem before this report was written.

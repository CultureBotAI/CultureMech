# YAML Record Review: marine_clostridium_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_clostridium_medium__7eae1fd6.yaml
- Started UTC: 2026-09-23T23:58:09Z
- Finished UTC: 2026-09-23T23:58:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_clostridium_medium__7eae1fd6.yaml |
| Class | MediaRecipe |
| ID | CultureMech:015390 |
| Label | marine_clostridium_medium |
| Source identity | mediadive.medium:J1187, JCM Medium 1187, MARINE CLOSTRIDIUM MEDIUM |
| Generation state | Generated one-source merge under data/merge_yaml/merged; repair data/normalized_yaml/specialized/marine_clostridium_medium.yaml or the MediaDive importer rather than this file |

The generated record denotes JCM Medium 1187 from MediaDive. The ID, label, pH, source accession, and JCM source agree, but stock solutions from MediaDive have been flattened into unsupported final-medium ingredient rows and the 1 L final distilled-water row is absent.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_clostridium_medium__7eae1fd6.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_clostridium_medium__7eae1fd6.yaml --out /private/tmp/marine_clostridium_medium__7eae1fd6.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_clostridium_medium__7eae1fd6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_clostridium_medium__7eae1fd6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- CultureMech:015390, `marine_clostridium_medium`, and `mediadive.medium:J1187` agree on JCM Medium 1187, `MARINE CLOSTRIDIUM MEDIUM`.
- MediaDive and the live JCM page agree on pH 7.5 and the main J1187 identity.
- The base salts, yeast extract, peptone, and resazurin mostly follow MediaDive's final-volume-normalized J1187 main solution; for example, 0.1 g KH2PO4 is divided by MediaDive's 1041 ml final volume to 0.0960615 g/L.
- The record misrepresents several source stock additions. NaHCO3, L-Cysteine HCl x H2O, and Na2S x 9 H2O are 25 ml, 6 ml, and 6 ml additions of 8%, 5%, and 5% solutions, not 25 g/L, 6 g/L, and 6 g/L final chemical rows.
- The trace vitamin and trace mineral components are ingredients of 2 ml/L and 1 ml/L stock additions, but the generated record publishes them as if they were direct final-medium additions.

## Evidence

- JCM Medium 1187 and MediaDive J1187 support KH2PO4, MgCl2 x 6 H2O, CaCl2 x 2 H2O, NH4Cl, NaCl, Yeast extract, Peptone, Resazurin, Trace vitamins solution, Trace mineral solution, Se/W solution, and the bicarbonate, cysteine, and sulfide solution additions.
- JCM and MediaDive both list 1 L or 1000 ml distilled water in the main solution; the generated YAML and its maintained specialized input omit that row.
- JCM says to add 25 ml 8% NaHCO3 solution, 6 ml 5% L-Cysteine x HCl x H2O solution, and 6 ml 5% Na2S x 9 H2O solution after cooling. The YAML stores those rows with `G_PER_L`, which makes the values 1000-fold concentration-scale ingredients rather than ml/L additions.
- MediaDive exposes the trace vitamin solution, trace mineral solution, and selenite-tungstate solution as stock solutions. The YAML includes the vitamin and mineral stock ingredients at their stock g/L values but does not show the 2 ml/L and 1 ml/L stock-addition rows themselves.
- The generated `Selenite-tungstate solution` entry keeps the stock identity but records its 1 ml/L amount as 1 g/L and points to an external MediaDive solution composition in prose instead of representing the 5543 recipe.
- The anaerobic preparation text matches JCM's main post-autoclave sequence at a coarse level but is compressed into one `AUTOCLAVE` step; it does not distinguish pH adjustment, boiling under N2-CO2, anaerobic dispensing, autoclaving, and post-cooling addition of autoclaved or filter-sterilized solutions.

## Completeness

- The main recipe is materially incomplete without the distilled-water row.
- The final formulation cannot be reconstructed correctly until the trace vitamin, trace mineral, Se/W, bicarbonate, cysteine, and sulfide rows are represented as solution additions with nested stock compositions or exact solution references.
- No target organism or growth metric is asserted. That is acceptable for this JCM formulation record.
- Exact gitignore-independent searches were run for `CultureMech:015390`, `marine_clostridium_medium`, `mediadive.medium:J1187`, `JCM Medium 1187`, and `7eae1fd6` across the scoped specialized normalized YAML directory, this target merged YAML, and the specialized and recipe index files with `--no-ignore --hidden`; the searches found the maintained input, generated target, and expected index entries.
- An exact `find data/merge_yaml/merged -maxdepth 1 -name 'marine_clostridium_medium*.yaml' -print` search, which includes ignored files, found only this generated target.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_clostridium_medium__7eae1fd6.md' -print` search, which includes ignored files, found no pre-existing review report for this generated record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Stock-solution compositions and final stock-addition volumes are flattened into unsupported final-medium ingredients. | MediaDive J1187 distinguishes the main solution, trace vitamin solution, trace mineral solution, and 1 ml Se/W addition; JCM lists bicarbonate, cysteine, and sulfide as 25 ml, 6 ml, and 6 ml solution additions, but the YAML publishes many stock-only rows directly and records those three ml additions as g/L ingredients. | data/normalized_yaml/specialized/marine_clostridium_medium.yaml and the MediaDive importer |
| major | The 1 L distilled-water main-solution row is missing. | JCM 1187 lists 1.0 L Distilled water, and MediaDive J1187 lists 1000 ml Distilled water in `Main sol. J1187`; the YAML has no final water ingredient. | data/normalized_yaml/specialized/marine_clostridium_medium.yaml and the MediaDive importer |
| minor | The multi-stage anaerobic preparation is compressed into one `AUTOCLAVE` step. | JCM requires pH adjustment, boiling and cooling under N2-CO2, distribution under the same gas mixture, sealing with butyl stoppers, autoclaving, and post-cooling anaerobic additions. | data/normalized_yaml/specialized/marine_clostridium_medium.yaml |

## Recommended Edits

1. Rework data/normalized_yaml/specialized/marine_clostridium_medium.yaml so main-solution final rows, stock additions, and nested stock compositions are separate.
2. Add the missing 1 L distilled-water row to the J1187 main solution.
3. Encode NaHCO3, L-Cysteine HCl x H2O, and Na2S x 9 H2O as 25, 6, and 6 ml/L stock-solution additions, not as g/L final ingredients.
4. Regenerate `data/merge_yaml/merged/` and verify the J1187 generated record no longer lists trace-vitamin or trace-mineral stock ingredients as top-level final-medium rows.

## Follow-up Checks

- Compare the repaired normalized YAML against the live JCM 1187 page and the MediaDive J1187 REST payload, including the final 1041 ml MediaDive normalization.
- Fetch MediaDive solution 5543 and verify the Se/W composition is represented consistently with the repaired stock model.
- Run open schema, strict schema, reference, and term validation on the maintained specialized input and regenerated merge.

## Additional Notes

- JCM 1187 and MediaDive J1187 agree on the source identity; the defect is a stock-boundary and amount-unit modeling problem, not a wrong-source problem.

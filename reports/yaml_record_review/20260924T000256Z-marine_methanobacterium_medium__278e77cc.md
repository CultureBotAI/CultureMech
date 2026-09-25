# YAML Record Review: marine_methanobacterium_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_methanobacterium_medium__278e77cc.yaml
- Started UTC: 2026-09-24T00:02:56Z
- Finished UTC: 2026-09-24T00:03:11Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_methanobacterium_medium__278e77cc.yaml |
| Class | MediaRecipe |
| ID | CultureMech:015389 |
| Label | marine_methanobacterium_medium |
| Source identity | mediadive.medium:J1186, JCM Medium 1186, MARINE METHANOBACTERIUM MEDIUM |
| Generation state | Generated one-source merge under data/merge_yaml/merged; repair data/normalized_yaml/specialized/marine_methanobacterium_medium.yaml or the MediaDive importer rather than this file |

The generated record denotes JCM Medium 1186 from MediaDive. Its source identity, pH, final-volume-normalized base salts, H2-CO2 handling, and pressure step agree with JCM and MediaDive, but it omits the 1000 ml main distilled-water row and flattens source stock recipes into the final-medium ingredient list.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_methanobacterium_medium__278e77cc.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_methanobacterium_medium__278e77cc.yaml --out /private/tmp/marine_methanobacterium_medium__278e77cc.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_methanobacterium_medium__278e77cc.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_methanobacterium_medium__278e77cc.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- CultureMech:015389, `marine_methanobacterium_medium`, and `mediadive.medium:J1186` agree on the intended source: JCM Medium 1186, `MARINE METHANOBACTERIUM MEDIUM`.
- MediaDive and the live JCM page agree on pH 7.5, the H2-CO2 atmosphere, and pressurizing inoculated vessels to 100 kPa.
- The base KH2PO4, MgCl2 x 6 H2O, CaCl2 x 2 H2O, NH4Cl, NaCl, Yeast extract, Sodium formate, Sodium acetate, and Resazurin rows match MediaDive's 1041 ml final-volume normalization.
- JCM and MediaDive model Trace vitamins, Trace mineral, and Se/W as ml/L stock additions; the YAML instead publishes the trace-vitamin and trace-mineral stock components at top level and records Se/W as a 1 g/L placeholder solution.
- NaHCO3, L-Cysteine HCl x H2O, and Na2S x 9 H2O are 25 ml, 6 ml, and 6 ml post-autoclave stock additions in JCM and MediaDive, not 25, 6, and 6 g/L final chemical rows.

## Evidence

- JCM Medium 1186 and MediaDive J1186 support the final-volume-normalized base amounts in the YAML.
- JCM 1186 and MediaDive `Main sol. J1186` both list Distilled water at 1000 ml; the generated YAML and the maintained specialized input omit that row.
- The YAML lists stock-only vitamin and trace-mineral ingredients as final-medium rows even though JCM adds 2 ml Trace vitamins solution, 1 ml Trace mineral solution, and 1 ml Se/W solution per liter.
- The generated `Selenite-tungstate solution` entry records 1 ml as 1 g/L and links `mediadive.solution:5543`; JCM 1186 specifically points to the Se/W solution in JCM Medium 852.
- The generated NaHCO3, L-Cysteine HCl x H2O, and Na2S x 9 H2O rows use `G_PER_L` where both inspected sources describe 8%, 5%, and 5% solution additions in ml.
- The two JCM preparation sentences are preserved, including anaerobic cooling and distribution under H2-CO2 and the 100 kPa pressure instruction.

## Completeness

- The final formula is materially incomplete until the 1000 ml distilled-water row is restored.
- The recipe is not executable at the right scope until trace vitamins, trace mineral, Se/W, bicarbonate, cysteine, and sulfide are represented as solution additions rather than flattened rows.
- The linked JCM 284 and 852 stock recipes are not nested. That is less urgent than preventing their stock ingredients from appearing at top level.
- No target organism or growth metric is asserted. That is acceptable for this JCM formulation record.
- Exact gitignore-independent searches were run for `CultureMech:015389`, `marine_methanobacterium_medium`, `mediadive.medium:J1186`, `JCM Medium 1186`, and the merge fingerprint prefix across the scoped specialized normalized YAML directory, this target merged YAML, and the specialized and recipe index files with `--no-ignore --hidden`; the searches found the maintained input, generated target, and expected index entries.
- An exact `find data/merge_yaml/merged -maxdepth 1 -name 'marine_methanobacterium_medium*.yaml' -print` search, which includes ignored files, found only this generated target.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_methanobacterium_medium__278e77cc.md' -print` search, which includes ignored files, found no pre-existing review report for this generated record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Trace-vitamin and trace-mineral stock compositions are flattened into final-medium ingredient rows. | JCM 1186 lists 2 ml Trace vitamins solution and 1 ml Trace mineral solution, while the YAML publishes their internal stock components as final g/L rows. | data/normalized_yaml/specialized/marine_methanobacterium_medium.yaml and the MediaDive importer |
| major | Post-autoclave ml/L solution additions are represented as g/L ingredients. | JCM and MediaDive list 25 ml 8% NaHCO3, 6 ml 5% L-Cysteine HCl x H2O, 6 ml 5% Na2S x 9 H2O, and 1 ml Se/W solution; the YAML stores those as 25, 6, 6, and 1 g/L rows or placeholder solutions. | data/normalized_yaml/specialized/marine_methanobacterium_medium.yaml and the MediaDive importer |
| major | The 1000 ml main water row is missing. | JCM 1186 and MediaDive J1186 both list Distilled water at 1.0 L or 1000 ml; the YAML has no water ingredient. | data/normalized_yaml/specialized/marine_methanobacterium_medium.yaml and the MediaDive importer |

## Recommended Edits

1. Rework data/normalized_yaml/specialized/marine_methanobacterium_medium.yaml so final main-solution ingredients and all stock additions have separate scopes.
2. Add the missing 1000 ml distilled-water row to the J1186 main solution.
3. Encode Trace vitamins, Trace mineral, Se/W, NaHCO3, L-Cysteine HCl x H2O, and Na2S x 9 H2O as ml/L solution additions instead of top-level g/L stock ingredients.
4. Regenerate `data/merge_yaml/merged/` and verify the J1186 generated record no longer publishes stock-only vitamin or trace-mineral rows at top level.

## Follow-up Checks

- Compare the repaired normalized YAML row-by-row against the live JCM Medium 1186 page and MediaDive J1186 REST payload.
- Re-check whether the generic `mediadive.solution:5543` is the right owner for JCM Medium 852's Se/W solution before preserving that link.
- Run open schema, strict schema, reference, and term validation on the maintained specialized input and regenerated merge.

## Additional Notes

- JCM Medium 1186 uses the same JCM 284 and 852 stock references as the adjacent JCM 1187 and JCM 1188 records, but the final base formula and H2-CO2 pressurization make it a separate recipe.

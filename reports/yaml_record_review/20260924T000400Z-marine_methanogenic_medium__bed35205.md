# YAML Record Review: marine_methanogenic_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_methanogenic_medium__bed35205.yaml
- Started UTC: 2026-09-24T00:04:00Z
- Finished UTC: 2026-09-24T00:04:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_methanogenic_medium__bed35205.yaml |
| Class | MediaRecipe |
| ID | CultureMech:000288 |
| Label | marine_methanogenic_medium |
| Source identity | mediadive.medium:J1106, JCM Medium 1106, MARINE METHANOGENIC MEDIUM |
| Generation state | Generated one-source merge under data/merge_yaml/merged; repair data/normalized_yaml/archaea/marine_methanogenic_medium.yaml or the MediaDive importer rather than this file |

The generated record denotes JCM Medium 1106 from MediaDive. It is distinct from the same-label TOGO M1183 import, and its final salts agree with JCM/MediaDive, but it omits the 930 ml main distilled-water row, drops the final trace-mineral and trace-vitamin stock-addition rows, and flattens internal stock components into the final-medium ingredient list.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_methanogenic_medium__bed35205.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_methanogenic_medium__bed35205.yaml --out /private/tmp/marine_methanogenic_medium__bed35205.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_methanogenic_medium__bed35205.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_methanogenic_medium__bed35205.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- CultureMech:000288, `marine_methanogenic_medium`, and `mediadive.medium:J1106` agree on the reviewed source: JCM Medium 1106, `MARINE METHANOGENIC MEDIUM`.
- The similarly named TOGO M1183 input has its own CultureMech ID, source accession, maintained path, and generated uppercase `MARINE_METHANOGENIC_MEDIUM.yaml` output; it is not the target of this review.
- JCM 1106 and MediaDive J1106 support the listed main-solution salts, Yeast extract, Resazurin, N2-CO2 autoclaving, and post-cooling anaerobic stock additions.
- NaCl, CaCl2 x 2 H2O, KCl, NH4Cl, MgCl2 x 6 H2O, K2HPO4, and Resazurin are grounded to terms matching the JCM formulas.
- NaHCO3, Na2S x 9 H2O, L-Cysteine HCl x H2O, NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and the vitamin rows are not direct final-medium g/L additions in JCM 1106.

## Evidence

- JCM Medium 1106 and MediaDive J1106 support the first eight top-level ingredient rows: 22 g NaCl, 0.14 g CaCl2 x 2 H2O, 0.34 g KCl, 0.5 g NH4Cl, 2.75 g MgCl2 x 6 H2O, 0.14 g K2HPO4, 0.2 g Yeast extract, and 1 mg Resazurin.
- JCM and MediaDive both list 930 ml distilled water in the main solution; the YAML omits this row.
- JCM lists 10 ml Trace mineral solution from Medium 1084 and 10 ml Trace vitamins from Medium 197. MediaDive models those as solution additions, but the YAML omits the final 10 ml rows and promotes only some internal stock components to top-level ingredients.
- JCM lists 30 ml 8% NaHCO3, 10 ml 5% Na2S x 9 H2O, and 10 ml 5% L-Cysteine HCl x H2O as post-autoclave additions; the YAML records them as 30, 10, and 10 g/L ingredients.
- The generated preparation step preserves the N2-CO2 autoclaving and post-cooling anaerobic-addition instruction.

## Completeness

- The recipe is materially incomplete without 930 ml distilled water.
- The Trace mineral and Trace vitamins final additions are missing as additions, and their stock-only nickel/selenium/tungsten and vitamin components are represented at the wrong scope.
- No target organism or growth metric is asserted. That is acceptable for this JCM formulation record.
- Exact gitignore-independent searches were run for `CultureMech:000288`, `marine_methanogenic_medium`, `mediadive.medium:J1106`, `JCM Medium 1106`, and the merge fingerprint across the scoped archaea normalized YAML directory, this target merged YAML, and the archaea and recipe index files with `--no-ignore --hidden`; the searches found the JCM J1106 target and a same-name TOGO M1183 sibling that was excluded by source identity.
- An exact `rg --no-ignore --hidden` search for `TOGO:M1183`, `M1183`, and `TOGO_M1183_Marine_Methanogenic_Medium` across generated merged YAML and that normalized sibling found a separate generated `MARINE_METHANOGENIC_MEDIUM.yaml` record for TOGO M1183.
- An exact `find data/merge_yaml/merged -maxdepth 1 -name 'marine_methanogenic_medium*.yaml' -print` search, which includes ignored files, found only this lower-case generated target; the case-sensitive find did not cover the same-label uppercase TOGO output.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_methanogenic_medium__bed35205.md' -print` search, which includes ignored files, found no pre-existing review report for this generated record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Stock-solution components are flattened into top-level final-medium ingredients. | JCM 1106 adds 10 ml Trace mineral and 10 ml Trace vitamins stocks, but the YAML publishes NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and ten vitamin stock components directly. | data/normalized_yaml/archaea/marine_methanogenic_medium.yaml and the MediaDive importer |
| major | Three post-autoclave ml/L stock additions are represented as g/L final ingredients. | JCM and MediaDive list 30 ml 8% NaHCO3, 10 ml 5% Na2S x 9 H2O, and 10 ml 5% L-Cysteine HCl x H2O; the YAML records 30, 10, and 10 g/L. | data/normalized_yaml/archaea/marine_methanogenic_medium.yaml and the MediaDive importer |
| major | The 930 ml main water row is missing. | JCM Medium 1106 and MediaDive `Main sol. J1106` both list Distilled water at 930 ml; the YAML has no water ingredient. | data/normalized_yaml/archaea/marine_methanogenic_medium.yaml and the MediaDive importer |

## Recommended Edits

1. Rework data/normalized_yaml/archaea/marine_methanogenic_medium.yaml so the J1106 main solution, Trace mineral stock, Trace vitamins stock, bicarbonate stock, sulfide stock, and cysteine stock are separate.
2. Add the missing 930 ml distilled-water row to the main solution.
3. Restore the 10 ml Trace mineral and 10 ml Trace vitamins additions and move stock-only NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and vitamin rows underneath the appropriate stock compositions.
4. Encode the NaHCO3, Na2S x 9 H2O, and L-Cysteine HCl x H2O additions as 30, 10, and 10 ml/L solution rows.
5. Regenerate `data/merge_yaml/merged/` and verify the J1106 output remains separate from the same-name TOGO M1183 output.

## Follow-up Checks

- Compare the repaired normalized YAML row-by-row against the live JCM Medium 1106 page and MediaDive J1106 REST payload.
- Re-run open schema, strict schema, reference, and term validation on the maintained archaea input and regenerated merge.
- Inspect the regenerated lower-case J1106 output and uppercase TOGO M1183 output to ensure both keep their own CultureMech IDs and source accessions.

## Additional Notes

- The same normalized `name` string for JCM J1106 and TOGO M1183 makes source identity checks mandatory for any future curation on `marine_methanogenic_medium`.

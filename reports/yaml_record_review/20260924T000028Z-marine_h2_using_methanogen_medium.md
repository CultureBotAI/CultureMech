# YAML Record Review: marine_h2_using_methanogen_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_h2_using_methanogen_medium.yaml
- Started UTC: 2026-09-24T00:00:28Z
- Finished UTC: 2026-09-24T00:01:05Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_h2_using_methanogen_medium.yaml |
| Class | MediaRecipe |
| ID | CultureMech:008267 |
| Label | marine_h2_using_methanogen_medium |
| Source identity | TOGO:M1705, NBRC Medium 911, Marine H2-using Methanogen Medium |
| Generation state | Generated one-source merge under data/merge_yaml/merged; repair data/normalized_yaml/archaea/marine_h2_using_methanogen_medium.yaml or the TOGO importer rather than this file |

The generated record denotes TOGO M1705/NBRC Medium 911. Its stable ID, source accession, and label agree, but the record flattens three stock recipes into the final-medium ingredient list, gives stock-addition volumes as g/L solution rows, and carries a stale generated sum of duplicated water rows.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_h2_using_methanogen_medium.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_h2_using_methanogen_medium.yaml --out /private/tmp/marine_h2_using_methanogen_medium.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_h2_using_methanogen_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_h2_using_methanogen_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- CultureMech:008267, `marine_h2_using_methanogen_medium`, and TOGO M1705 agree on the intended source identity: NBRC Medium 911, `Marine H2-using Methanogen Medium`.
- NBRC 911 lists the same main salts, yeast extract, acetate, carbonate, sulfide, cysteine, 1 L water, H2/CO2 gas handling, KP7 buffer, trace elements solution, and vitamin solution represented by the imported TOGO record.
- The main recipe adds 5 ml KP7 buffer, 2 ml Trace elements solution, and 2 ml Vitamin solution to the final medium. The generated `solutions` entries preserve those three names but record the amounts as 5, 2, and 2 g/L with empty placeholder compositions.
- KP7 buffer, Trace elements solution, and Vitamin solution are stock recipes. Their phosphate, trace-mineral, and vitamin rows should not be top-level final-medium ingredients.
- Gas entries for CO2, N2, and H2 are supported as procedural gases/headspace conditions, not as concentration-defined solutes.

## Evidence

- NBRC 911 supports the final-medium rows for MgCl2 x 6 H2O, CaCl2 x 2 H2O at 0.15 g, NH4Cl, Na2SO4, NaCl at 30 g, Bacto Yeast Extract, Sodium acetate, Resazurin at 1 mg, Na2CO3, Na2S x 9 H2O, Cysteine-HCl, and 1 L distilled water.
- The YAML merges source-identical component names across stock boundaries. Distilled water is summed to 4 g/L in the generated file, NaCl is summed to 31 g/L, and CaCl2 x 2 H2O is summed to 0.25 g/L because the main solution and nested stock solution rows share labels.
- The maintained input has already collapsed the four identical 1 L Distilled water rows back to one row, but it still leaves that row as 1 g/L rather than 1000 ml/L and still keeps NaCl and CaCl2 x 2 H2O summed across the trace stock and final recipe.
- KP7 buffer appears in NBRC as 5 ml, with KH2PO4 and K2HPO4 in a 1 L stock. The YAML records KP7 as a 5 g/L empty solution and also publishes KH2PO4 at 53 g/L and K2HPO4 at 106 g/L as final-medium rows.
- Trace elements solution appears in NBRC as 2 ml, with its own 1 L stock formula. The YAML records Trace elements as a 2 g/L solution and also publishes NTA, FeCl3 x 6 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnCl2, CuCl2 x 2 H2O, H3BO3, Na2MoO4 x 2 H2O, NaCl, NiCl2 x 6 H2O, Na2SeO4, Na2WO4, KAl(SO4)2 x 12 H2O, and NaOH stock rows at top level.
- Vitamin solution appears in NBRC as 2 ml, with milligram amounts per liter of stock. The YAML records Vitamin solution as a 2 g/L solution and publishes Biotin, Folic acid, Pyridoxine-HCl, Thiamine-HCl, Riboflavin, Nicotinic acid, Ca-pantothenate, p-Aminobenzoic acid, and Vitamin B12 as g/L final-medium rows.

## Completeness

- The final formulation cannot be followed correctly until final-medium rows, KP7 buffer, Trace elements solution, and Vitamin solution are represented as separate preparation scopes.
- The source gas-handling instructions are present only as prose in the NBRC/TOGO note and are not represented as ordered preparation steps in the YAML.
- No pH value is declared beyond NBRC's `pH unadjusted` comment, and no target organism or growth metric is asserted. Those absent optional slots are acceptable for this formulation-only source.
- Exact gitignore-independent searches were run for `CultureMech:008267`, `marine_h2_using_methanogen_medium`, `TOGO:M1705`, `NBRC_M911`, and the merge fingerprint across the exact normalized input, target merged YAML, and the archaea, TOGO, and recipe index files with `--no-ignore --hidden`; the searches found the maintained input, generated target, and expected index entries.
- An exact `find data/merge_yaml/merged -maxdepth 1 -name 'marine_h2_using_methanogen_medium*.yaml' -print` search, which includes ignored files, found only this generated target.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_h2_using_methanogen_medium.md' -print` search, which includes ignored files, found no pre-existing review report for this generated record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | KP7, trace-elements, and vitamin stock recipes are flattened into the final-medium ingredients. | NBRC 911 adds 5 ml KP7 buffer, 2 ml Trace elements solution, and 2 ml Vitamin solution, but the YAML publishes their stock phosphate, trace-metal, and vitamin components as direct g/L rows. | data/normalized_yaml/archaea/marine_h2_using_methanogen_medium.yaml and the TOGO importer |
| major | The three stock-addition amounts are represented with the wrong units. | NBRC lists KP7, Trace elements, and Vitamin solution as 5 ml, 2 ml, and 2 ml; the YAML stores those `solutions` as 5, 2, and 2 g/L. | data/normalized_yaml/archaea/marine_h2_using_methanogen_medium.yaml and the TOGO importer |
| major | Duplicate cleanup merged source rows across stock-solution boundaries. | NBRC has 30 g NaCl in the final recipe plus 1 g NaCl inside Trace elements, and 0.15 g CaCl2 x 2 H2O in the final recipe plus 0.1 g in Trace elements; the YAML sums those to 31 g/L and 0.25 g/L. | data/normalized_yaml/archaea/marine_h2_using_methanogen_medium.yaml and duplicate cleanup logic |
| minor | The generated water row is stale relative to a maintained duplicate repair. | The generated merge still has Distilled water at 4.0 g/L; the maintained input collapsed the four identical 1 L water rows on 2026-09-02, though it still uses the wrong `G_PER_L` unit. | data/merge_yaml generation after normalized repair |

## Recommended Edits

1. Rework data/normalized_yaml/archaea/marine_h2_using_methanogen_medium.yaml so final-medium ingredients, KP7 buffer, Trace elements solution, and Vitamin solution are separate scopes.
2. Change the KP7, Trace elements, and Vitamin solution additions to 5, 2, and 2 ml/L and move their formulas into nested `composition` entries or linked `SolutionRecipe` records.
3. Split stock-only NaCl and CaCl2 x 2 H2O from the final main rows so the final recipe returns to 30 g/L NaCl and 0.15 g/L CaCl2 x 2 H2O.
4. Regenerate `data/merge_yaml/merged/` and confirm the generated M1705 record no longer publishes KP7, trace, or vitamin stock components at top level.

## Follow-up Checks

- Compare the repaired normalized YAML row-by-row against NBRC Medium 911 and the TOGO M1705 source payload if that endpoint begins returning M1705 again.
- Re-run open schema, strict schema, reference, and term validation on the maintained archaea input and regenerated merge.
- Inspect the regenerated merge for the absence of stale duplicate notes on Distilled water, NaCl, and CaCl2 x 2 H2O.

## Additional Notes

- The TOGO public API returned an empty body for `M1705` during this review; NBRC Medium 911 was inspected directly and supports the relevant source formulation.
- An over-broad index search using a loose `TOGO:` token was discarded. The exact gitignore-independent source/ID search listed above was rerun and used for the report.

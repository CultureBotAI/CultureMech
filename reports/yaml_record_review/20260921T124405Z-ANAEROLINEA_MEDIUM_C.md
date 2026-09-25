# YAML Record Review: Anaerolinea Medium C

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROLINEA_MEDIUM_C.yaml
- Started UTC: 2026-09-21T12:42:20Z
- Finished UTC: 2026-09-21T12:44:05Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ANAEROLINEA_MEDIUM_C.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:007704` |
| Name | `anaerolinea_medium_c` |
| Source accession | `TOGO:M1179` |
| Source label | `Anaerolinea Medium C` |
| Generated status | Generated merge from `TOGO_M1179_Anaerolinea_Medium_C` |

The reviewed file is the generated merge for the TOGO import of JCM Medium 1103 / TOGO Medium 1179. Its maintained owner is `data/normalized_yaml/bacterial/TOGO_M1179_Anaerolinea_Medium_C.yaml`; the generated record adds only merge metadata to that normalized input.

The exact, gitignore-independent identity search used `rg --no-ignore --hidden` across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`, and `history` for `TOGO_M1179_Anaerolinea_Medium_C`, `Anaerolinea Medium C`, `ANAEROLINEA MEDIUM C`, `anaerolinea_medium_c`, `CultureMech:007704`, `TOGO:M1179`, `M1179`, `JCM_M1103`, and `GRMD=1103`. It found the maintained TOGO input, the reviewed generated merge, generated TOGO and recipe indexes, the adjacent MediaDive/JCM `data/normalized_yaml/bacterial/anaerolinea_medium_c.yaml` plus its generated merge, and unrelated JCM M1179 references in `M_MEDIUM`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROLINEA_MEDIUM_C.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROLINEA_MEDIUM_C.yaml --out /private/tmp/ANAEROLINEA_MEDIUM_C.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROLINEA_MEDIUM_C.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROLINEA_MEDIUM_C.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this checkout because project `uv` resolves with Python 3.13 and attempts to build `llvmlite==0.46.0`, whose setuptools build aborts with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project Python 3.11 commands above validate the generated record without building the project.

## Identity and Grounding

The generated record correctly identifies the TOGO M1179 import of JCM Medium 1103 by stable ID, source accession, label, category, and liquid complex-medium classification.

There is one source-version conflict. The TOGO M1179 API reports `original_media_id: JCM_M1103`, matches the generated `Solution A` and `Solution B` ingredient set, and points trace vitamins to Medium M190. The current JCM `GRMD=1103` page still serves the same ANAEROLINEA MEDIUM C recipe, but its Solution A table points trace vitamins to Medium 197.

Solution A, Solution B, Trace element solution SL-11, Selenite-tungstate solution, Trace vitamins, 5% sodium sulfide solution, and 5% L-cysteine solution are all source-supported solution boundaries. The generated record collapses most of their chemistry into direct medium ingredients and grounds the two local `Solution A` and `Solution B` rows to MediaDive solution IDs that are not present in the TOGO or JCM source.

The `CoCl2 x 6H2O` and `NiCl2 x 6H2O` ingredients are grounded to anhydrous cobalt dichloride and nickel dichloride rather than exact hydrated salts.

## Evidence

The generated record has no structured `references` or `source_data` block. I inspected the TOGO M1179 API payload and the direct JCM `GRMD=1103` HTML page.

Both sources support these recipe boundaries and amounts:

- Solution A: 900 ml distilled water, 0.15 g calcium chloride dihydrate, 0.14 g potassium dihydrogen phosphate, 0.54 g ammonium chloride, 1 mg resazurin, 0.2 g magnesium chloride hexahydrate, 2.5 g sodium bicarbonate, 2.3 g yeast extract, 1 ml Trace element solution SL-11, 0.5 ml Selenite-tungstate solution, 10 ml Trace vitamins, and N2-CO2 handling.
- Solution B: 100 ml distilled water, 2.2 g glucose, and an N2 atmosphere.
- Final assembly: 0.9 volume Solution A plus 0.1 volume Solution B, then 6 ml/L each of 5% sodium sulfide and 5% L-cysteine solutions.
- Trace element solution SL-11: 1 L distilled water with EDTA, FeCl2 x 4H2O, ZnCl2, MnCl2 x 4H2O, H3BO3, CoCl2 x 6H2O, CuCl2 x 2H2O, NiCl2 x 6H2O, and Na2MoO4 x 2H2O.

The current JCM page supports the ordered preparation conditions as source text: Solution A pH 6.5 before bicarbonate addition, boiling for 5-10 seconds, N2-CO2 cooling and dispensing, autoclaving and overnight standing, sterile anaerobic trace-vitamin addition, Solution B pH 7.0 plus filter sterilization, final anaerobic Solution B addition, reductant additions before inoculation, and pH 6.0 for Trace element solution SL-11.

## Completeness

The simple salts and carbon source are present, and the reviewed generated record has enough normalized ingredient labels to be recognizable.

The consequential gaps are:

- no `preparation_steps`;
- no Solution A pH 6.5, Solution B pH 7.0, or SL-11 pH 6.0 condition;
- no filter-sterilization condition for Solution B or trace vitamins;
- no final 0.9:0.1 Solution A/Solution B assembly instruction;
- no stock-solution composition for M1179-local Solution A, Solution B, or Trace element solution SL-11;
- no resolved stock-solution composition for Selenite-tungstate solution or Trace vitamins;
- no non-default names for any of the seven generated solution entries;
- no scoped gas rows for the N2-CO2 Solution A handling and N2 Solution B handling.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Source solution amounts are stored with mass concentration units. | TOGO M1179 and JCM 1103 add 900 ml Solution A, 100 ml Solution B, 1 ml SL-11, 0.5 ml Selenite-tungstate solution, 10 ml Trace vitamins, and 6 ml/L each of two 5% reductant solutions. The generated `solutions` rows store those amounts as `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1179_Anaerolinea_Medium_C.yaml` or the TOGO unit/solution importer |
| Major | M1179-local Solution A and Solution B are grounded to unrelated MediaDive solution IDs. | The source defines both stocks locally inside M1179/JCM 1103. The generated rows reference `mediadive.solution:5342` and `mediadive.solution:5343`, with notes pointing to `mediadive_5342_Solution_A.yaml` and `mediadive_5343_Solution_B.yaml`. | Same normalized TOGO M1179 owner or cross-source solution-linking importer |
| Major | Trace element solution SL-11 is flattened into direct ingredients. | The source adds 1 ml SL-11 to Solution A and separately defines a 1 L SL-11 stock. The generated record emits the SL-11 metal salts and EDTA as direct final-medium ingredients, with milligram stock rows inflated to gram-per-liter values such as `Na2MoO4 x 2H2O` at `36 G_PER_L` and `CuCl2 x 2H2O` at `2 G_PER_L`. | Same normalized TOGO M1179 owner or TOGO stock-solution importer |
| Major | Preparation and pH text was dropped. | The source includes Solution A, Solution B, final assembly, reductant-addition, and SL-11 pH instructions. The generated merge has no `preparation_steps`. | Same normalized TOGO M1179 owner or TOGO comment importer |
| Major | The Trace vitamins cross-reference disagrees with the current original JCM page. | The TOGO API and generated preferred term say Medium M190; the direct JCM `GRMD=1103` page says Medium No. 197. | Source refresh or manual reconciliation for `TOGO_M1179_Anaerolinea_Medium_C.yaml` |
| Minor | Water quantities from three sub-solutions were merged into one direct ingredient. | The source has 900 ml water in Solution A, 100 ml water in Solution B, and 1 L water in SL-11. The generated row is a direct `Distilled water` ingredient at `1001.0 G_PER_L`. | Same normalized TOGO M1179 owner after stock-solution repair |
| Minor | Hydrated cobalt and nickel salts are grounded to anhydrous terms. | The source lists `CoCl2 x 6H2O` and `NiCl2 x 6H2O`; the generated record stores `CHEBI:35696` cobalt dichloride and `CHEBI:34887` nickel dichloride. | Same normalized TOGO M1179 owner or ingredient grounding enrichment |
| Minor | Gas rows are duplicated and underspecified. | N2 and CO2 are part of the source preparation context for Solution A and Solution B, but the generated record emits direct `Carbon dioxide gas`, `Nitrogen gas`, and `N2` rows without those boundaries. | Same normalized TOGO M1179 owner or TOGO gas importer |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M1179_Anaerolinea_Medium_C.yaml` or the TOGO importer, preserve Solution A, Solution B, Trace element solution SL-11, Selenite-tungstate solution, Trace vitamins, and the two 5% reductant solutions as volume-based stock additions with their source labels.
2. Remove the `mediadive.solution:5342` and `mediadive.solution:5343` links from this TOGO record and represent M1179-local Solution A and Solution B explicitly.
3. Move the SL-11 EDTA and metal rows out of direct final-medium ingredients and into a structured SL-11 stock added to Solution A at 1 ml.
4. Import the JCM preparation comments as ordered steps, preserving the pH 6.5, pH 7.0, final 0.9:0.1 assembly, reductant addition, and SL-11 pH 6.0 scopes.
5. Reconcile whether the trace-vitamin reference should target Medium M190 from the TOGO payload or Medium 197 from the current JCM source.
6. Preserve the three water rows inside their source solution boundaries instead of merging them into direct final-medium `G_PER_L`.
7. Clear exact hydrated-salt groundings for `CoCl2 x 6H2O` and `NiCl2 x 6H2O` unless exact cobalt chloride hexahydrate and nickel chloride hexahydrate terms are available in the packaged ingredient index.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` on `data/normalized_yaml/bacterial/TOGO_M1179_Anaerolinea_Medium_C.yaml`.
2. If importer code changes, add or update focused tests for M1179 solution parsing, milligram preservation, pH/comment import, and JCM/TOGO cross-reference refresh.
3. Regenerate `data/merge_yaml/merged/ANAEROLINEA_MEDIUM_C.yaml` and verify that no SL-11 row appears as a direct final-medium ingredient.
4. Re-open the current JCM `GRMD=1103` page and prove that the regenerated trace-vitamin reference points to the reconciled source medium.

## Additional Notes

The adjacent MediaDive/JCM `data/normalized_yaml/bacterial/anaerolinea_medium_c.yaml` record already carries the direct JCM preparation text and is generated separately as `data/merge_yaml/merged/anaerolinea_medium_c__39713f85.yaml`. It remains a useful cross-check for pH and preparation support, but it is not the generated TOGO M1179 record reviewed here.

The direct JCM page fetched during review is an HTML source page for medium no. 1103, not a search snippet. The TOGO public `/medium/M1179` route is not enough for source review, so the TOGO-side comparison used `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1179`.

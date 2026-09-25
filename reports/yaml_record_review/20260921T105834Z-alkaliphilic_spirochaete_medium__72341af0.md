# YAML Record Review: alkaliphilic_spirochaete_medium__72341af0

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__72341af0.yaml`
- Started UTC: 2026-09-21T10:58:34Z
- Finished UTC: 2026-09-21T10:58:35Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:008545` |
| Generated path reviewed | `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__72341af0.yaml` |
| Maintained source path | `data/normalized_yaml/bacterial/TOGO_M1964_Alkaliphilic_spirochaete_medium.yaml` |
| Merge source | `TOGO_M1964_Alkaliphilic_spirochaete_medium` |
| Category | `bacterial` |
| Source accession | `TOGO:M1964`, original `NBRC_M1241` |
| Source label | `Alkaliphilic spirochaete medium` |
| Source inspected | `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1964` |

The reviewed file is a generated merge from one TOGO normalized record. Future curation should change `data/normalized_yaml/bacterial/TOGO_M1964_Alkaliphilic_spirochaete_medium.yaml` or the TOGO importer, then regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/alkaliphilic_spirochaete_medium__72341af0.yaml` | Passed with exit 0 and no issues emitted |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/alkaliphilic_spirochaete_medium__72341af0.yaml --out /private/tmp/alkaliphilic_spirochaete_medium__72341af0.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/alkaliphilic_spirochaete_medium__72341af0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/alkaliphilic_spirochaete_medium__72341af0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: this repository exposes `just validate-history` for standalone records under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record |

## Identity and Grounding

The source identity is consistent: the record is TOGO Medium `M1964`, named `Alkaliphilic spirochaete medium`, imported from original NBRC medium `1241`. The direct NBRC URL currently returns an NBRC error page, so the TOGO API payload was the inspected recoverable source for this review.

The target's solution identities are not consistent with TOGO M1964. TOGO lists three inline stock recipes:

| TOGO stock | TOGO addition to the main medium | Current `solutions` row |
|---|---:|---|
| `Vitamin solution*` | 10 ml | `mediadive.solution:6241` / `Vitamin solution`, `10 G_PER_L` |
| `Trace element solution**` | 2 ml | `mediadive.solution:6187` / `Trace element solution`, `2 G_PER_L` |
| `Bicarbonate solution***` | 200 ml | `mediadive.solution:29` / `Bicarbonate solution`, `200 G_PER_L` |

Those MediaDive stock records are not the same recipes as the TOGO/NBRC inline stocks. For example, TOGO M1964's bicarbonate stock has 75 g NaHCO3 and 50 g Na2CO3 per liter, while `mediadive_29_Bicarbonate_solution.yaml` has 30 g/L NaHCO3 only. The current CultureMech terms therefore point to near-name records that are chemically different.

Several exact ingredient groundings are weak or absent:

- `Yeast extract` is ungrounded.
- `CoCl2.6H2O` is grounded to anhydrous `CHEBI:35696` / `cobalt dichloride`.
- `NiCl2.6H2O` is grounded to anhydrous `CHEBI:34887` / `nickel dichloride`.
- `Ca-pantothenate` is grounded to `(R)-pantothenate`, not calcium pantothenate.

## Evidence

The TOGO API supports the top-level source identity, a pH of 9.7, 800 ml main-solution water, 10 g NaCl, 1 g NH4Cl, 0.2 g K2HPO4, 0.2 g KCl, 5 g sucrose, 0.003 g MgSO4.7H2O, 0.5 g yeast extract, a nitrogen atmosphere, a 1 g sulfide addition, and three stock additions: 10 ml vitamin solution, 2 ml trace element solution, and 200 ml bicarbonate solution.

The current record preserves many source tokens but not their containment:

| TOGO subsection | Source content | Current record state |
|---|---|---|
| Main solution | 800 ml water plus direct salts, yeast extract, sucrose, `N2`, 10 ml vitamin stock, 2 ml trace stock, and 200 ml bicarbonate stock | Stock components are duplicated as top-level ingredients; only placeholder `solutions` remain for the three stocks |
| Vitamin solution | 1 L water plus nine vitamins in mg amounts | The nine vitamins are direct ingredients with `G_PER_L` values, producing 1000-fold unit slips such as `Biotin` at `2 G_PER_L` instead of a 2 mg/L stock component |
| Trace element solution | 1 L water plus NaCl, CaCl2.2H2O, Na2MoO4.2H2O, H3BO3, MnCl2.4H2O, CoCl2.6H2O, NiCl2.6H2O, CuCl2.2H2O, ZnCl2, FeCl3.6H2O, KAl(SO4)2.12H2O, NTA, Na2WO4, Na2SeO4, and NaOH | The trace-stock components are direct ingredients; trace `NaCl` and water were merged with the main water and salt rows |
| Bicarbonate solution | 1 L water, 75 g NaHCO3, and 50 g Na2CO3 | Carbonate salts are direct ingredients, and the 200 ml stock addition is modeled as `200 G_PER_L` |
| Preparation comment | Mix without sulfide/vitamin/bicarbonate; dispense under nitrogen; seal with butyl rubber; autoclave; separately autoclave sulfide under N2; filter-sterilize vitamin and bicarbonate; aseptically and anaerobically add vitamin, bicarbonate, and sulfide before inoculation | No `preparation_steps` are present |

The local import diagnostics independently identify the water/salt merges and stock-strength unit slips:

| Diagnostic | Ingredient | Imported value | Source of concern |
|---|---:|---:|---|
| `data/import_tracking/reports/merged_duplicates.tsv` | `Distilled water` | `803.0 G_PER_L` | `800.0;1.0;1.0;1.0` |
| `data/import_tracking/reports/merged_duplicates.tsv` | `NaCl` | `11.0 G_PER_L` | `10.0;1.0` |
| `data/import_tracking/reports/concentration_plausibility.tsv` | nine vitamin rows | `0.1` to `10 G_PER_L` | vitamin stock mg values imported as grams |
| `data/import_tracking/reports/concentration_plausibility.tsv` | `FeCl3.6H2O` | `1.35 G_PER_L` | trace-element stock strength as a top-level ingredient |

## Completeness

Consequential gaps:

- `ph_value: 9.7` from TOGO `meta.ph` and the source comments is missing.
- All preparation text is missing.
- The three TOGO inline stock recipes are not modeled; the rows in `solutions` have wrong units and wrong `mediadive.solution` identities.
- Stock contents remain duplicated as top-level final-medium ingredients.
- Water and NaCl from different compartments were merged.
- No structured reference captures TOGO M1964 or NBRC M1241; they are only free-text notes.

Correctly empty or not inherently defective:

- `target_organisms` and `growth_metrics` are absent. The TOGO/NBRC formulation source does not establish a specific growth measurement.
- `discussion`, parent media, and variant links are absent; they are less important than the source transcription errors above.

A gitignore-independent search with `rg --no-ignore --hidden` and `find` covered `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for `TOGO_M1964_Alkaliphilic_spirochaete_medium`, `TOGO:M1964`, `NBRC_M1241`, the NBRC `NO=1241` URL, and the merge fingerprint `72341af0dd9a12b9524dabd4b7509c6c39146f0e3dcdbdc0f7a81fbb4134aaff`. It found this target, its normalized parent, registry/catalog/index references, and older import diagnostics; `find reports/yaml_record_review -name '*alkaliphilic_spirochaete_medium__72341af0.md' -print` found no prior review report for this exact stem.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The source pH was dropped. | TOGO M1964 has `meta.ph: 9.7` and a source comment `pH 9.7`; the YAML has no `ph_value`. | `data/normalized_yaml/bacterial/TOGO_M1964_Alkaliphilic_spirochaete_medium.yaml` or the TOGO importer |
| major | Inline stock recipes were flattened into final ingredients. | Vitamin, trace-element, and bicarbonate stock components appear as top-level rows alongside the main medium, even though TOGO M1964 adds only 10 ml, 2 ml, and 200 ml of those stocks. | `data/normalized_yaml/bacterial/TOGO_M1964_Alkaliphilic_spirochaete_medium.yaml` or the TOGO importer |
| major | Migrated solution descriptors carry wrong identities and units. | The three `solutions` rows use `G_PER_L` instead of ml additions and point to unrelated `mediadive.solution` records rather than TOGO M1964's inline stock definitions. | `data/normalized_yaml/bacterial/TOGO_M1964_Alkaliphilic_spirochaete_medium.yaml` and the solution migration rule |
| major | Preparation, atmosphere, and sterilization instructions are missing. | TOGO M1964 specifies mixing exceptions, N2 dispensing, butyl-rubber sealing, autoclaving at 121 C for 20 min, separate sulfide autoclaving under N2, filter sterilization of vitamin and bicarbonate solutions, and anaerobic aseptic addition before inoculation; `preparation_steps` is absent. | `data/normalized_yaml/bacterial/TOGO_M1964_Alkaliphilic_spirochaete_medium.yaml` or the TOGO importer |
| major | Duplicate cleanup summed ingredients from different containers. | Main-medium `NaCl` and trace-stock `NaCl` were merged as `11 G_PER_L`; main water, vitamin-stock water, trace-stock water, and bicarbonate-stock water were merged as `803 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1964_Alkaliphilic_spirochaete_medium.yaml` and the duplicate-merge cleanup rule |
| minor | Several exact ingredients are ungrounded or too broadly grounded. | `Yeast extract` has no term; CoCl2.6H2O and NiCl2.6H2O are grounded to anhydrous chlorides; Ca-pantothenate is grounded to a non-calcium pantothenate term. | `data/normalized_yaml/bacterial/TOGO_M1964_Alkaliphilic_spirochaete_medium.yaml` plus the packaged MediaIngredientMech label index for absent exact salts |
| minor | NBRC/TOGO provenance is free-text-only. | The source URL and original NBRC accession are embedded in `notes`; no structured source or reference row points to the TOGO API payload or original NBRC source. | `data/normalized_yaml/bacterial/TOGO_M1964_Alkaliphilic_spirochaete_medium.yaml` or import provenance mapping |

## Recommended Edits

1. Restore `ph_value: 9.7` from TOGO M1964.
2. Rebuild the normalized record from the TOGO component hierarchy:
   - Keep only main-solution components as root `ingredients`.
   - Put TOGO's `Vitamin solution*`, `Trace element solution**`, and `Bicarbonate solution***` in `solutions` with `10 ML_PER_L`, `2 ML_PER_L`, and `200 ML_PER_L`.
   - Move each stock's water and chemical rows into that stock's `composition`.
3. Remove `mediadive.solution:6241`, `mediadive.solution:6187`, and `mediadive.solution:29` from this TOGO record unless an inspected source establishes true cross-source equivalence.
4. Undo duplicate merges for `Distilled water` and `NaCl` by preserving source containers rather than summing rows from stock recipes.
5. Add preparation steps for nitrogen dispensing, butyl-rubber sealing, main-medium autoclaving, sulfide autoclaving under N2, vitamin/bicarbonate filter sterilization, and anaerobic aseptic post-autoclave additions.
6. Reground exact hydrated chlorides and calcium pantothenate only where exact verified identities exist; otherwise keep source labels explicit and unresolved.
7. Add structured TOGO M1964 and NBRC M1241 provenance.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/TOGO_M1964_Alkaliphilic_spirochaete_medium.yaml`.
- Rerun `just verify-merges` and inspect `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__72341af0.yaml`.
- Rerun `just validate-media-variant-links data/normalized_yaml/bacterial/TOGO_M1964_Alkaliphilic_spirochaete_medium.yaml` if variant links are added.
- Rerun `just validate-products` after regenerating derived pages.
- Manually compare the curated record against the TOGO M1964 JSON payload, especially the 10 ml vitamin, 2 ml trace, and 200 ml bicarbonate solution additions and the anaerobic preparation comment.
- Re-run the duplicate and concentration plausibility diagnostics, or equivalent focused scripts, to confirm `Distilled water`, `NaCl`, vitamin rows, and `FeCl3.6H2O` no longer flag this record.
- Re-run exact `rg --no-ignore --hidden` checks for `TOGO_M1964_Alkaliphilic_spirochaete_medium`, `TOGO:M1964`, and `NBRC_M1241` across `data`, `src`, `scripts`, `history`, and reports.

## Additional Notes

- The NBRC `NO=1241` URL embedded in the record returned an NBRC error page during this review; the TOGO API response still contained the imported NBRC formulation, original NBRC accession, and preparation comments.
- The generated merge has one parent, so the merge and normalized record currently have the same scientific content.
- `just validate-schema`, `just validate-strict`, and `just validate-terms` were not run directly because project `uv` currently tries to build `llvmlite==0.46.0` under Python 3.13 before reaching record validation. The equivalent no-project validator invocations above were used instead.

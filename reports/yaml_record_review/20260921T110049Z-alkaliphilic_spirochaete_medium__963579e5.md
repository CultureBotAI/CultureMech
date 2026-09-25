# YAML Record Review: alkaliphilic_spirochaete_medium__963579e5

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__963579e5.yaml`
- Started UTC: 2026-09-21T11:00:49Z
- Finished UTC: 2026-09-21T11:00:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:009316` |
| Generated path reviewed | `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__963579e5.yaml` |
| Maintained source path | `data/normalized_yaml/bacterial/TOGO_M2769_Alkaliphilic_Spirochaete_Medium.yaml` |
| Merge source | `TOGO_M2769_Alkaliphilic_Spirochaete_Medium` |
| Category | `bacterial` |
| Source accession | `TOGO:M2769` |
| Source label | `Alkaliphilic Spirochaete Medium` |
| Source documents inspected | TOGO M2769 API; `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium700.pdf`; `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf` |

The reviewed file is a generated merge from one TOGO normalized record. Future curation should change `data/normalized_yaml/bacterial/TOGO_M2769_Alkaliphilic_Spirochaete_Medium.yaml` or the TOGO importer and then regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/alkaliphilic_spirochaete_medium__963579e5.yaml` | Passed: `No issues found` |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/alkaliphilic_spirochaete_medium__963579e5.yaml --out /private/tmp/alkaliphilic_spirochaete_medium__963579e5.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/alkaliphilic_spirochaete_medium__963579e5.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/alkaliphilic_spirochaete_medium__963579e5.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: this repository exposes `just validate-history` for standalone records under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record |

## Identity and Grounding

The record identity is TOGO Medium `M2769`, `Alkaliphilic Spirochaete Medium`, derived from DSMZ Medium 700. This is distinct from the adjacent `alkaliphilic_spirochaete_medium__72341af0` merge, which is TOGO M1964 / NBRC M1241 with a bicarbonate stock.

DSMZ 700 uses two cross-referenced DSMZ Medium 141 stocks:

| DSMZ 700 stock addition | Source stock in DSMZ 141 | Current `solutions` row |
|---|---|---|
| 10 ml vitamin solution | Wolin's vitamin solution | `mediadive.solution:6241` / `Vitamin solution`, `10 G_PER_L` |
| 1 ml trace element solution | Modified Wolin's mineral solution | `mediadive.solution:6187` / `Trace element solution`, `1 G_PER_L` |

The migrated solution rows point to unrelated MediaDive stock records. `mediadive_6241_Vitamin_solution.yaml` is a three-component stock with different concentrations, and `mediadive_6187_Trace_element_solution.yaml` lacks most of Modified Wolin's mineral solution. Their names are near matches only.

Ingredient identity gaps:

- `Yeast extract` is ungrounded.
- `NiCl2 x 6 H2O` is grounded to anhydrous `CHEBI:34887` / `nickel dichloride`.
- The root `MgSO4 x 7 H2O` row has `term: CHEBI:31795` for magnesium sulfate heptahydrate but stale `mediaingredientmech_chebi_term: CHEBI:32599` for generic magnesium sulfate.

## Evidence

DSMZ Medium 700 supports the base medium: 10 g Na2CO3, 15 g NaHCO3, 10 g NaCl, 0.2 g K2HPO4, 1 g NH4Cl, 0.2 g KCl, 1 g Na2S x 9 H2O, 0.5 g yeast extract, 5 g sucrose, 10 ml vitamin solution from Medium 141, 1 ml trace element solution from Medium 141, and 1000 ml distilled water. It also supports anaerobic preparation under N2, pH 9.7 with 6N NaOH, autoclaving, and sterile-stock addition of neutralized sulfide, vitamins, and sucrose.

DSMZ Medium 141 supports the cross-referenced stock compositions:

| Source stock | DSMZ 141 content | Current record state |
|---|---|---|
| Wolin's vitamin solution | Ten vitamins or growth factors in mg per 1000 ml water | Nine matching vitamin rows and `D-Ca-pantothenate` are top-level final-medium ingredients at `G_PER_L`, e.g. `Biotin` is `2 G_PER_L` instead of 2 mg/L in a stock added at 10 ml/L |
| Modified Wolin's mineral solution | NTA, MgSO4, MnSO4, NaCl, FeSO4, CoSO4, CaCl2, ZnSO4, CuSO4, KAl(SO4)2, H3BO3, Na2MoO4, NiCl2, Na2SeO3, Na2WO4, 1000 ml water, and KOH pH adjustment | The trace stock contents are top-level ingredients; the 1 ml/L stock addition is modeled only as an unrelated `mediadive.solution:6187` row with `1 G_PER_L` |

The local diagnostics flag the stock-flattening artifacts:

| Diagnostic | Ingredient | Imported value | Source of concern |
|---|---:|---:|---|
| `data/import_tracking/reports/merged_duplicates.tsv` | `NaCl` | `11.0 G_PER_L` | base-medium `10.0` and trace-stock `1.0` summed |
| `data/import_tracking/reports/concentration_plausibility.tsv` | `Distilled water` | `1000.0 G_PER_L` | source volume modeled as concentration |
| `data/import_tracking/reports/concentration_plausibility.tsv` | nine vitamin rows | `0.1` to `10 G_PER_L` | DSMZ 141 vitamin mg values imported as grams |

The generated merge lags its source: `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__963579e5.yaml` still has `3000.0 G_PER_L` distilled water, while the maintained normalized file already collapsed the three identical 1000 ml water rows to one `1000.0` row on 2026-09-02.

## Completeness

Consequential gaps:

- `ph_value: 9.7` is absent even though DSMZ 700 states that target pH.
- No preparation step captures N2 handling, omission of bicarbonate/sulfide/sucrose/vitamin before autoclaving, boiling and cooling under nitrogen, pH adjustment with 6N NaOH, autoclaving, or sterile post-autoclave additions.
- DSMZ Medium 141 stocks are not modeled; their components remain top-level rows and the placeholder `solutions` rows point to unrelated MediaDive stocks with `G_PER_L` units.
- The source trace element solution's KOH pH-adjustment reagent is a top-level final-medium ingredient.
- TOGO M2769 / DSMZ 700 and DSMZ 141 provenance is present only in free-text `notes`.

Correctly empty or not inherently defective:

- `target_organisms`, `growth_metrics`, and literature `evidence` are absent. The DSMZ/TOGO recipe source does not itself prove a strain-specific growth outcome.
- `discussion`, quality flags, parents, and variants are absent; the direct formulation defects above are the urgent work.

A gitignore-independent search with `rg --no-ignore --hidden` and `find` covered `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for `TOGO_M2769_Alkaliphilic_Spirochaete_Medium`, `TOGO:M2769`, `DSMZ_Medium700`, and the merge fingerprint `963579e50eb6a37abd65ac493530d27942ccfaa6dee46c71649784766b502956`. It found this target, its normalized parent, registry/catalog/index references, a direct DSMZ 700 sibling record, and older import diagnostics; `find reports/yaml_record_review -name '*alkaliphilic_spirochaete_medium__963579e5.md' -print` found no prior review report for this exact stem.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated merge is stale relative to its normalized parent. | The merge still reports `Distilled water` as `3000.0 G_PER_L`; the normalized parent has the repaired single `1000.0` row and a `repair_merged_duplicates.py` history event from 2026-09-02. | `data/merge_yaml/merged/`, regenerated from `data/normalized_yaml/bacterial/TOGO_M2769_Alkaliphilic_Spirochaete_Medium.yaml` |
| major | The source pH and full anaerobic preparation protocol are missing. | DSMZ 700 adjusts to pH 9.7 with 6N NaOH and describes N2 preparation, autoclaving, and sterile-stock additions; the record has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M2769_Alkaliphilic_Spirochaete_Medium.yaml` or the TOGO importer |
| major | DSMZ 141 vitamin and trace stocks were flattened into final-medium ingredients. | The source adds 10 ml/L Wolin's vitamin solution and 1 ml/L Modified Wolin's mineral solution; those stock contents are direct `ingredients` rows in the YAML. | `data/normalized_yaml/bacterial/TOGO_M2769_Alkaliphilic_Spirochaete_Medium.yaml` or the TOGO importer |
| major | Solution references have wrong identities and units. | The `solutions` rows use `mediadive.solution:6241` and `mediadive.solution:6187` with `G_PER_L`, but DSMZ 700 references DSMZ Medium 141 stocks at 10 ml/L and 1 ml/L. | `data/normalized_yaml/bacterial/TOGO_M2769_Alkaliphilic_Spirochaete_Medium.yaml` and the solution migration rule |
| major | The cleanup layer summed `NaCl` across different containers. | The top-level `11.0 G_PER_L` NaCl row merges DSMZ 700's 10 g base NaCl with the DSMZ 141 trace stock's 1 g NaCl. | `data/normalized_yaml/bacterial/TOGO_M2769_Alkaliphilic_Spirochaete_Medium.yaml` and the duplicate-merge cleanup rule |
| minor | Ingredient grounding has stale or broad hydrated-salt links. | `Yeast extract` is ungrounded; `NiCl2 x 6 H2O` resolves to anhydrous nickel dichloride; the `MgSO4 x 7 H2O` primary term and MIM link disagree. | `data/normalized_yaml/bacterial/TOGO_M2769_Alkaliphilic_Spirochaete_Medium.yaml` plus the packaged MediaIngredientMech label index |
| minor | Source provenance is not structured. | TOGO M2769 and the DSMZ 700 PDF appear only in `notes`, and the DSMZ 141 stock provenance is only implied by imported stock contents. | `data/normalized_yaml/bacterial/TOGO_M2769_Alkaliphilic_Spirochaete_Medium.yaml` or import provenance mapping |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__963579e5.yaml` so the existing normalized water repair reaches the generated record.
2. Add `ph_value: 9.7` and model DSMZ 700's anaerobic preparation sequence: prepare under N2, omit Na2CO3, NaHCO3, Na2S, sucrose, and vitamins initially, boil/cool under nitrogen, add carbonate/bicarbonate, adjust with 6N NaOH, autoclave, then add neutralized Na2S, Wolin's vitamin solution, and sucrose from sterile stocks.
3. Replace the unrelated `mediadive.solution` links with DSMZ Medium 141 stock descriptors or local maintained `SolutionRecipe` records for Wolin's vitamin solution and Modified Wolin's mineral solution.
4. Move DSMZ 141 stock ingredients out of root `ingredients` and into those two stock compositions; keep only 10 ml/L and 1 ml/L additions on the root medium.
5. Undo the `NaCl` cross-container sum by keeping base NaCl and trace-stock NaCl separate.
6. Correct or de-ground stale exact-form links for `NiCl2 x 6 H2O`, `MgSO4 x 7 H2O`, and `Yeast extract` according to the packaged MediaIngredientMech index.
7. Add structured TOGO M2769, DSMZ 700, and DSMZ 141 provenance.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/TOGO_M2769_Alkaliphilic_Spirochaete_Medium.yaml`.
- Rerun `just verify-merges` and inspect `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__963579e5.yaml` to confirm the generated water row, root ingredients, and stock solution links match the normalized file.
- Rerun `just validate-products` after regenerating pages.
- Compare the curated normalized record against DSMZ Medium 700 and DSMZ Medium 141, especially the 10 ml Wolin vitamin stock, 1 ml Modified Wolin mineral stock, pH 9.7 adjustment, and anaerobic post-autoclave additions.
- Re-run the duplicate and concentration plausibility diagnostics, or equivalent focused scripts, to confirm this record no longer flags `NaCl`, vitamin rows, or root water.
- Re-run exact `rg --no-ignore --hidden` checks for `TOGO_M2769_Alkaliphilic_Spirochaete_Medium`, `TOGO:M2769`, and `DSMZ_Medium700` across `data`, `src`, `scripts`, `history`, and reports.

## Additional Notes

- `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__b7efab90.yaml` appears to be the direct DSMZ/MediaDive import of Medium 700 and should be reviewed separately when that sorted target is reached.
- `just validate-schema`, `just validate-strict`, and `just validate-terms` were not run directly because project `uv` currently tries to build `llvmlite==0.46.0` under Python 3.13 before reaching record validation. The equivalent no-project validator invocations above were used instead.

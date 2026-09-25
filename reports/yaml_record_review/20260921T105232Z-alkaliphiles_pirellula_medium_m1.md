# YAML Record Review: alkaliphiles_pirellula_medium_m1

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1.yaml`
- Started UTC: 2026-09-21T10:52:32Z
- Finished UTC: 2026-09-21T10:52:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:000904` |
| Generated path reviewed | `data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1.yaml` |
| Maintained source path | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1.yaml` |
| Merge source | `alkaliphiles_pirellula_medium_m1` |
| Category | `bacterial` |
| Source accession | `mediadive.medium:1441`, DSMZ Medium 1441 |
| Source label | `ALKALIPHILES PIRELLULA MEDIUM (M1)` |
| Source document inspected | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1441.pdf` |

The reviewed file is a generated merge record from one normalized MediaDive/DSMZ import. Future curation should change `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1.yaml`, then regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1.yaml` | Passed: `No issues found` |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1.yaml --out /private/tmp/alkaliphiles_pirellula_medium_m1.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: this repository exposes `just validate-history` for standalone records under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record |

## Identity and Grounding

The DSMZ identity matches: the record is DSMZ Medium 1441 / MediaDive `mediadive.medium:1441`, labeled `ALKALIPHILES PIRELLULA MEDIUM (M1)`, and the DSMZ PDF for Medium 1441 carries that same title.

This target is distinct from the adjacent DSMZ siblings already present in the corpus:

| Record | Source |
|---|---|
| `alkaliphiles_pirellula_medium_m1py` | DSMZ/MediaDive 1437, M1PY |
| `alkaliphiles_pirellula_medium_m1apy` | DSMZ/MediaDive 1439, M1aPY |
| `alkaliphiles_pirellula_medium_m1` | DSMZ/MediaDive 1441, M1 |

The top-level ingredient groundings are mostly plausible for the source tokens, but the record is not preserving the source formulation boundaries. Stock-solution components from the vitamin solution, Hutner's salts, and Metals 44 have been imported as if they were direct final-medium ingredients. That makes many otherwise-plausible CHEBI links support the wrong concentration and containment claim.

One exact-form grounding remains incomplete: `(NH4)6Mo7O24 x 4 H2O` is the DSMZ formula and the record retains that preferred term, but it grounds only to generic `CHEBI:91249` / `ammonium molybdate` and has no `mediaingredientmech_chebi_term`.

## Evidence

The inspected DSMZ PDF supports the overall source identity, pH 9.0, and the presence of the listed ingredients, but not their current flattened amounts. DSMZ 1441 is structured as:

| Source component | DSMZ amount and context | Current record state |
|---|---|---|
| Solution 1 base | CaCO3 5 g, Na2HPO4 x H2O 0.10 g, MgSO4 x 7H2O 0.50 g, Hutner's basal salts 20 ml, Gelrite 8 g, distilled water 930 ml | `CaCO3`, `Na2HPO4 x H2O`, and `Gelrite` are direct top-level rows scaled to non-source concentrations; the Hutner's stock boundary and 930 ml water are missing |
| Solution 2 | N-acetylglucosamine 2.0 g, Vitamin solution No. 6 10.0 ml, distilled water 40.0 ml | `N-Acetylglucosamine` is represented as `40 G_PER_L`; the vitamin stock boundary and 40 ml water are missing |
| Vitamin solution | Nine vitamins in 1000 ml distilled water, filter-sterilized | The nine vitamin stock concentrations are top-level ingredients instead of a 10 ml/L stock addition |
| Hutner's salts | NTA, MgSO4 x 7 H2O, CaCl2 x 2 H2O, ammonium molybdate tetrahydrate, FeSO4 x 7 H2O, 50 ml Metals 44, 950 ml distilled water | Hutner's stock concentrations are top-level ingredients instead of a 20 ml/L stock addition |
| Metals 44 | Na-EDTA, ZnSO4 x 7 H2O, FeSO4 x 7 H2O, MnSO4 x H2O, CuSO4 x 5 H2O, Co(NO3)2 x 6 H2O, Na2B4O7 x 10 H2O, 1000 ml distilled water | Metals 44 stock concentrations are top-level ingredients instead of a nested 50 ml/L Hutner's addition |

Two local import diagnostics independently flag the arithmetic problem in the maintained normalized file:

| Diagnostic | Ingredient | Imported value | Parts |
|---|---:|---:|---:|
| `data/import_tracking/reports/merged_duplicates.tsv` | `MgSO4 x 7 H2O` | `30.220833 G_PER_L` | `0.520833;29.7` |
| `data/import_tracking/reports/merged_duplicates.tsv` | `FeSO4 x 7 H2O` | `0.599 G_PER_L` | `0.099;0.5` |
| `data/import_tracking/reports/concentration_plausibility.tsv` | `ZnSO4 x 7 H2O` | `1.095 G_PER_L` | stock-solution magnitude trace salt |

The record has no PMID/DOI evidence blocks, no `sources` structure, and no target-organism growth claim. That absence avoids over-scoped growth evidence, but it leaves all source provenance as a free-text `notes` string.

## Completeness

Consequential gaps:

- The source's solution hierarchy is absent from `solutions`.
- All five DSMZ distilled-water rows are absent: Solution 1, Solution 2, Vitamin solution, Hutner's salts, and Metals 44.
- Addition volumes are absent: 20 ml Hutner's basal salts into Solution 1, 10 ml vitamin stock into Solution 2, and 50 ml Metals 44 into 1 L Hutner's salts.
- The preparation steps are detached from the solution records they prepare.
- The top-level `physical_state: LIQUID` is not supported by the DSMZ formula as imported because Solution 1 contains 8 g Gelrite.

Correctly empty or not inherently defective:

- `target_organisms` is absent. DSMZ 1441 is a source recipe, not a narrow primary growth experiment; the source PDF alone does not establish a strain-specific growth assertion.
- `evidence` is absent. No PMID or DOI citation is represented in the source import.
- `discussion`, quality flags, parent media, and variant links are absent. I did not find a concrete in-record conflict that those slots already try to represent.

A gitignore-independent search with `rg --no-ignore --hidden` and `find` covered `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for `DSMZ_Medium1441`, `ALKALIPHILES PIRELLULA`, `mediadive.medium:1441`, and `CultureMech:000904`. It found this target, its normalized parent, registry/catalog/index references, older import reports, and adjacent M1PY/M1aPY sibling records; `find reports/yaml_record_review -name '*alkaliphiles_pirellula_medium_m1.md' -print` found no prior review report for this exact stem.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | DSMZ stock-solution boundaries were flattened into one final ingredient list. | DSMZ 1441 has Solution 1, Solution 2, Vitamin solution, Hutner's salts, and nested Metals 44 blocks; the record has only direct top-level `ingredients` and no `solutions`. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1.yaml` or the MediaDive importer that produced it |
| major | Multiple stock concentrations and stock-local amounts are represented as final `G_PER_L` concentrations. | N-acetylglucosamine is `2.0 g` in the 50 ml Solution 2 addition, but the record says `40 G_PER_L`; ZnSO4 x 7 H2O is `1095 mg` in 1 L Metals 44, but the record says `1.095 G_PER_L` as a direct medium ingredient. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1.yaml` or the MediaDive importer |
| major | Duplicate chemicals from different formulation layers were arithmetically merged. | The record sums Solution 1 MgSO4 x 7H2O with Hutner's MgSO4 x 7H2O as `30.220833 G_PER_L`, and it sums Hutner's FeSO4 x 7 H2O with Metals 44 FeSO4 x 7 H2O as `0.599 G_PER_L`. Those are different containment contexts in the source. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1.yaml` and the duplicate-merge cleanup rule |
| major | Preparation steps lost their solution context and are not sufficient to reconstruct DSMZ 1441. | The record stores the Solution 1 autoclave step, the Solution 2 pH/filter step, vitamin filter sterilization, Hutner's pH adjustment, and Metals 44 EDTA/H2SO4 instruction as five top-level steps; it omits the explicit Hutner's, vitamin, and Metals 44 stock addition boundaries. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1.yaml` or normalized solution-modeling support |
| major | `physical_state: LIQUID` conflicts with the imported DSMZ formulation. | DSMZ 1441 includes 8 g Gellan gum Gelrite in Solution 1; a liquid formulation is not supported by the inspected PDF. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1.yaml` |
| minor | Source provenance is only a free-text note. | The source accession and PDF URL are embedded in `notes`; no structured `sources`, `references`, or evidence object captures the inspected DSMZ source. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1.yaml` or the DSMZ/MediaDive import transform |
| minor | Ammonium molybdate tetrahydrate is not grounded to an exact hydrated identity. | The row says `(NH4)6Mo7O24 x 4 H2O` but grounds only to generic `ammonium molybdate` and has no `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1.yaml` plus the packaged MediaIngredientMech label index if the exact salt is absent there |

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1.yaml` from DSMZ 1441 with explicit stock-solution structure:
   - Solution 1 as the base, with CaCO3, Na2HPO4 x H2O, MgSO4 x 7H2O, Gelrite, 930 ml distilled water, and 20 ml Hutner's basal salts.
   - Solution 2 as a filter-sterilized post-autoclave addition with N-acetylglucosamine, 40 ml distilled water, and 10 ml Vitamin solution No. 6.
   - Vitamin solution, Hutner's salts, and Metals 44 as maintained `SolutionRecipe` records or nested `SolutionDescriptor` blocks with their own water, concentrations, and preparation text.
2. Remove the duplicate-merge sums for `MgSO4 x 7 H2O` and `FeSO4 x 7 H2O`; keep their separate source positions instead of summing across stock layers.
3. Preserve stock addition volumes and final-medium arithmetic. Do not convert a stock concentration to a direct final-medium `G_PER_L` value unless the dilution is explicitly represented.
4. Replace the top-level preparation list with source-scoped preparation for each stock plus the final post-autoclave addition of filter-sterilized Solution 2 to Solution 1.
5. Correct `physical_state` from `LIQUID` to the source-supported state, or add an inspected source for a liquid M1 variant before keeping `LIQUID`.
6. Add structured DSMZ/MediaDive provenance so a curator can recover DSMZ Medium 1441 without parsing `notes`.
7. Resolve `(NH4)6Mo7O24 x 4 H2O` through the exact MediaIngredientMech/CHEBI hydrated identity if available; otherwise leave the exact source string ungrounded rather than grounding it only to a generic salt.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1.yaml` after curation.
- Rerun `just verify-merges` and inspect `data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1.yaml` to confirm the solution hierarchy survives regeneration.
- Rerun `just validate-products` after regenerating derived pages.
- Re-run `rg --no-ignore --hidden "alkaliphiles_pirellula_medium_m1|CultureMech:000904|mediadive.medium:1441" data reports` to confirm the maintained parent, generated merge, catalog, and indices agree.
- Manually compare the curated YAML with `DSMZ_Medium1441.pdf`, paying particular attention to 20 ml Hutner's, 10 ml vitamin stock, 50 ml Metals 44 inside Hutner's, water volumes, pH adjustments, filter sterilization, and Gelrite.
- Re-run duplicate and trace-salt plausibility scans, or the narrower scripts that emit `data/import_tracking/reports/merged_duplicates.tsv` and `data/import_tracking/reports/concentration_plausibility.tsv`, to ensure this record no longer flags `MgSO4 x 7 H2O`, `FeSO4 x 7 H2O`, or `ZnSO4 x 7 H2O`.

## Additional Notes

- The generated merge has one parent, so the reviewed merge and maintained normalized record currently have the same scientific content.
- The record validates structurally because the schema allows flat ingredient lists and free-text preparation steps. The failing behavior is the source-to-record transformation, not YAML shape.
- `just validate-schema`, `just validate-strict`, and `just validate-terms` were not run directly because project `uv` currently tries to build `llvmlite==0.46.0` under Python 3.13 before reaching record validation. The equivalent no-project validator invocations above were used instead.

# YAML Record Review: alkaliphiles_pirellula_medium_m1py

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1py.yaml`
- Started UTC: 2026-09-21T10:56:23Z
- Finished UTC: 2026-09-21T10:56:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:000899` |
| Generated path reviewed | `data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1py.yaml` |
| Maintained source path | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1py.yaml` |
| Merge source | `alkaliphiles_pirellula_medium_m1py` |
| Category | `bacterial` |
| Source accession | `mediadive.medium:1437`, DSMZ Medium 1437 |
| Source label | `ALKALIPHILES PIRELLULA MEDIUM (M1PY)` |
| Source documents inspected | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1437.pdf`; `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium590.pdf` |

The reviewed file is a generated merge record from one normalized MediaDive/DSMZ import. Future edits belong in `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1py.yaml` or the DSMZ/MediaDive import transform, followed by merge regeneration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1py.yaml` | Passed with exit 0 and no issues emitted |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1py.yaml --out /private/tmp/alkaliphiles_pirellula_medium_m1py.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1py.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1py.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: this repository exposes `just validate-history` for standalone records under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record |

## Identity and Grounding

The record's DSMZ/MediaDive source identity is correct: DSMZ Medium 1437 / MediaDive `mediadive.medium:1437`, labeled `ALKALIPHILES PIRELLULA MEDIUM (M1PY)`. It is separate from the neighboring M1aPY and M1 sibling recipes, which are DSMZ 1439 and DSMZ 1441.

The source identity does not carry through to containment. DSMZ 1437 has a base Solution 1, a filter-sterilized Solution 2, a vitamin stock, and a reference to Hutner's basal salts from DSMZ 590. The record contains a single list of 28 top-level ingredients, so several groundings that are correct as stock constituents are wrong as final-medium claims.

Ingredient grounding gaps:

- `Peptone`, `Yeast extract`, and `Ampicillin sodium salt` are ungrounded.
- `(NH4)6Mo7O24 x 4 H2O` is grounded only to generic `CHEBI:91249` / `ammonium molybdate` and has no `mediaingredientmech_chebi_term`.

## Evidence

DSMZ Medium 1437 supports the M1PY base and antibiotic-containing Solution 2. DSMZ Medium 590 supports the cross-referenced Hutner's salts and Metals 44 stock. The inspected sources do not support the flattened final list.

| Source component | DSMZ amount and context | Current record state |
|---|---|---|
| Solution 1 base | Peptone 0.25 g, yeast extract 0.25 g, CaCO3 5 g, Na2HPO4 x H2O 0.10 g, MgSO4 x 7H2O 0.50 g, 20 ml Hutner's basal salts, 9 g Gelrite, 930 ml distilled water | All non-water chemicals are direct top-level rows scaled to `G_PER_L`; 20 ml Hutner's salts and 930 ml water are absent |
| Solution 2 | N-acetylglucosamine 2.0 g, ampicillin sodium salt 0.2 g, cycloheximide 0.2 g, 10 ml vitamin solution, 40 ml distilled water | The three chemicals are direct top-level rows scaled against the 50 ml stock, yielding `40 G_PER_L` N-acetylglucosamine and `4 G_PER_L` for each inhibitor |
| Vitamin solution | Nine vitamins in 1000 ml distilled water, filter-sterilized | The nine vitamin stock concentrations are top-level ingredients instead of a 10 ml stock addition |
| Hutner's salts | NTA, MgSO4 x 7 H2O, CaCl2 x 2 H2O, ammonium molybdate tetrahydrate, FeSO4 x 7 H2O, 50 ml/L Metals 44, and 950 ml/L distilled water | DSMZ 590 Hutner's stock components are top-level M1PY ingredients |
| Metals 44 | Seven trace salts in 1 L distilled water | Metals 44 stock concentrations are top-level M1PY ingredients |

The repository's existing import diagnostics point to the same stock-flattening defects:

| Diagnostic | Ingredient | Imported value | Parts |
|---|---:|---:|---:|
| `data/import_tracking/reports/merged_duplicates.tsv` | `MgSO4 x 7 H2O` | `30.226316 G_PER_L` | `0.526316;29.7` |
| `data/import_tracking/reports/merged_duplicates.tsv` | `FeSO4 x 7 H2O` | `0.599 G_PER_L` | `0.099;0.5` |
| `data/import_tracking/reports/concentration_plausibility.tsv` | `ZnSO4 x 7 H2O` | `1.095 G_PER_L` | stock-solution magnitude trace salt |

The record has no literature evidence array and no target-organism growth claim to validate.

## Completeness

Consequential gaps:

- No `solutions` block represents 20 ml Hutner's salts, 10 ml vitamin stock, 50 ml/L Metals 44 inside Hutner's salts, or the filter-sterilized Solution 2 addition to Solution 1.
- Five distilled-water rows are absent: Solution 1, Solution 2, vitamin stock, Hutner's salts, and Metals 44.
- The preparation sequence is flattened. Hutner's and Metals 44 preparation from DSMZ 590 appears as top-level M1PY preparation, while Solution 2's antibiotic/vitamin addition is not modeled as a stock addition.
- `physical_state: LIQUID` conflicts with the 9 g Gelrite in DSMZ 1437 Solution 1.
- Source provenance is free text in `notes` and omits structured DSMZ 590 provenance.

Correctly empty or not inherently defective:

- `target_organisms`, `growth_metrics`, and `evidence` are absent. The DSMZ formulation page does not by itself support a strain-specific growth result.
- `discussion`, quality flags, parents, and variants are absent. Their absence is less important than the concrete formulation errors above.

A gitignore-independent search with `rg --no-ignore --hidden` and `find` covered `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for `alkaliphiles_pirellula_medium_m1py`, `ALKALIPHILES PIRELLULA MEDIUM (M1PY)`, `mediadive.medium:1437`, and `CultureMech:000899`. It found this target, its normalized parent, registry/catalog/index references, older import diagnostics, and no prior report for this exact stem.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | DSMZ solution boundaries were flattened into top-level final ingredients. | DSMZ 1437 separates Solution 1, Solution 2, a vitamin stock, and a 20 ml Hutner's stock addition from DSMZ 590; the YAML has no `solutions` and lists 28 direct ingredients. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1py.yaml` or the MediaDive importer |
| major | Solution 2 concentrations were imported as 50 ml stock concentrations rather than final-medium amounts. | N-acetylglucosamine, ampicillin sodium salt, and cycloheximide are 2.0 g, 0.2 g, and 0.2 g in Solution 2; the record reports `40`, `4`, and `4 G_PER_L` as if those were direct final concentrations. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1py.yaml` or the MediaDive importer |
| major | Hutner's salts and Metals 44 are expanded at stock strength and then partially summed with base rows. | `MgSO4 x 7 H2O` sums a Solution 1 part with a Hutner's part as `30.226316 G_PER_L`, and `FeSO4 x 7 H2O` sums Hutner's and Metals 44 parts as `0.599 G_PER_L`. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1py.yaml` and the duplicate-merge cleanup rule |
| major | Preparation steps lost source scoping. | DSMZ 590 stock-preparation steps are mixed into the M1PY top-level sequence, and the vitamin stock's filter sterilization is not attached to a stock recipe. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1py.yaml` |
| major | `physical_state: LIQUID` is unsupported by the inspected DSMZ 1437 formulation. | The base formulation contains 9 g Gellan gum Gelrite. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1py.yaml` |
| minor | Three direct source chemicals are ungrounded. | Peptone, yeast extract, and ampicillin sodium salt have no `term` or `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1py.yaml` |
| minor | Source provenance is not structured. | DSMZ 1437 is embedded only in `notes`; DSMZ 590 is only implied through imported Hutner's components. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1py.yaml` or import provenance mapping |

## Recommended Edits

1. Remodel `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1py.yaml` with Solution 1, filter-sterilized Solution 2, the vitamin stock, Hutner's salts, and the nested Metals 44 stock.
2. Link Hutner's salts to the maintained DSMZ 590 stock representation, such as `data/normalized_yaml/bacterial/hutners_salts_medium_590.yaml`, instead of duplicating and flattening its ingredients.
3. Keep M1PY's base MgSO4, Hutner's MgSO4, Hutner's FeSO4, and Metals 44 FeSO4 as distinct source-scoped rows; delete the duplicate-merge sums from this normalized record.
4. Restore the missing distilled-water rows and stock addition volumes.
5. Scope pH adjustment, autoclaving, filter sterilization, Hutner's preparation, and Metals 44 EDTA/H2SO4 instructions to their source solutions.
6. Correct `physical_state` unless a checked liquid M1PY variant exists and should be modeled separately.
7. Ground peptone, yeast extract, ampicillin sodium salt, and exact ammonium molybdate tetrahydrate only to verified MediaIngredientMech/CHEBI identities.
8. Add structured DSMZ Medium 1437 and DSMZ Medium 590 provenance.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1py.yaml`.
- Rerun `just verify-merges` and inspect `data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1py.yaml`.
- Rerun `just validate-products` after regenerating page outputs.
- Re-run exact `rg --no-ignore --hidden` checks for `CultureMech:000899`, `mediadive.medium:1437`, and `DSMZ_Medium1437` across `data`, `src`, `scripts`, `history`, and reports.
- Compare the curated record manually against `DSMZ_Medium1437.pdf` and `DSMZ_Medium590.pdf`, focusing on Solution 2's antibiotics, the vitamin stock, 20 ml Hutner's, 50 ml Metals 44, water volumes, and pH/sterilization sequence.
- Re-run the duplicate and concentration plausibility diagnostics, or equivalent focused scripts, to confirm this record no longer flags cross-stock `MgSO4 x 7 H2O`, `FeSO4 x 7 H2O`, or stock-strength `ZnSO4 x 7 H2O`.

## Additional Notes

- The generated merge has one parent, so the merge and normalized record currently have the same scientific content.
- DSMZ 1437 references Hutner's basal salts from Medium 590; the imported Hutner's and Metals 44 rows match the DSMZ 590 PDF but are in the wrong containment layer.
- `data/normalized_yaml/bacterial/hutners_salts_medium_590.yaml` already contains a curated nested Hutner's/Metals 44 stock derived from DSMZ Medium 590.
- `just validate-schema`, `just validate-strict`, and `just validate-terms` were not run directly because project `uv` currently tries to build `llvmlite==0.46.0` under Python 3.13 before reaching record validation. The equivalent no-project validator invocations above were used instead.

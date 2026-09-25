# YAML Record Review: alkaliphiles_pirellula_medium_m1apy

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1apy.yaml`
- Started UTC: 2026-09-21T10:54:53Z
- Finished UTC: 2026-09-21T10:54:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:000901` |
| Generated path reviewed | `data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1apy.yaml` |
| Maintained source path | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1apy.yaml` |
| Merge source | `alkaliphiles_pirellula_medium_m1apy` |
| Category | `bacterial` |
| Source accession | `mediadive.medium:1439`, DSMZ Medium 1439 |
| Source label | `ALKALIPHILES PIRELLULA MEDIUM (M1aPY)` |
| Source documents inspected | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1439.pdf`; `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium590.pdf` |

The reviewed file is a generated merge record from one normalized MediaDive/DSMZ import. Future edits belong in `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1apy.yaml` or in the DSMZ/MediaDive import rule that emitted it, followed by merge regeneration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1apy.yaml` | Passed: `No issues found` |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1apy.yaml --out /private/tmp/alkaliphiles_pirellula_medium_m1apy.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1apy.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1apy.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: this repository exposes `just validate-history` for standalone records under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record |

## Identity and Grounding

The generated record denotes the right source recipe: DSMZ Medium 1439 / MediaDive `mediadive.medium:1439`, `ALKALIPHILES PIRELLULA MEDIUM (M1aPY)`. The sibling M1 and M1PY recipes are present as separate DSMZ 1441 and DSMZ 1437 records, so this target is not an identity merge with its near neighbors.

The ingredient grounding is only partially meaningful because the record has lost the formulation tree. Peptone, yeast extract, CaCl2, Na2HPO4 x H2O, the first MgSO4 x 7H2O row, Gelrite, and N-acetylglucosamine are direct members of DSMZ 1439, but the vitamin rows are members of a vitamin stock, and NTA, CaCl2 x 2 H2O, ammonium molybdate, FeSO4, Na-EDTA, ZnSO4, MnSO4, CuSO4, Co(NO3)2, and Na2B4O7 are members of Hutner's salts or the nested Metals 44 stock from DSMZ Medium 590.

Two exact ingredient identities are still weak:

- `Peptone` and `Yeast extract` have no `term` or `mediaingredientmech_chebi_term`.
- `(NH4)6Mo7O24 x 4 H2O` is the DSMZ Medium 590 formula, but the row uses generic `CHEBI:91249` / `ammonium molybdate` and has no `mediaingredientmech_chebi_term`.

## Evidence

DSMZ Medium 1439 supports the main M1aPY formulation and DSMZ Medium 590 supports the cross-referenced Hutner's salts stock. Together they show that the current flat list is not a supported representation of the protocol.

| Source component | DSMZ amount and context | Current record state |
|---|---|---|
| Solution 1 base | Peptone 0.25 g, yeast extract 0.25 g, CaCl2 0.20 g, Na2HPO4 x H2O 0.10 g, MgSO4 x 7H2O 0.50 g, 20 ml Hutner's basal salts, 9 g Gelrite, 940 ml distilled water | All non-water chemicals are direct top-level rows scaled to `G_PER_L`; 20 ml Hutner's salts and 940 ml water are not represented |
| Solution 2 | N-acetylglucosamine 2.0 g, 10 ml vitamin solution, 40 ml distilled water | `N-Acetylglucosamine` is represented as `40 G_PER_L`; 10 ml vitamin solution and 40 ml water are not represented |
| Vitamin solution | Nine vitamins in 1000 ml distilled water, filter-sterilized | The nine vitamin stock concentrations are top-level ingredients instead of a 10 ml stock addition |
| Hutner's salts | 10 g/L NTA, 29.7 g/L MgSO4 x 7 H2O, 3.335 g/L CaCl2 x 2 H2O, 9.25 mg/L ammonium molybdate tetrahydrate, 99 mg/L FeSO4 x 7 H2O, 50 ml/L Metals 44, 950 ml/L distilled water | DSMZ 590 stock concentrations are imported as direct final-medium ingredients |
| Metals 44 | Seven trace salts in 1 L distilled water | Metals 44 stock concentrations are imported as direct final-medium ingredients |

Local import diagnostics flag the same maintained normalized file:

| Diagnostic | Ingredient | Imported value | Parts |
|---|---:|---:|---:|
| `data/import_tracking/reports/merged_duplicates.tsv` | `MgSO4 x 7 H2O` | `30.220833 G_PER_L` | `0.520833;29.7` |
| `data/import_tracking/reports/merged_duplicates.tsv` | `FeSO4 x 7 H2O` | `0.599 G_PER_L` | `0.099;0.5` |
| `data/import_tracking/reports/concentration_plausibility.tsv` | `ZnSO4 x 7 H2O` | `1.095 G_PER_L` | stock-solution magnitude trace salt |

No PMID/DOI evidence block or strain-specific growth evidence is present, so reference validation had no citation or snippet to check.

## Completeness

Consequential gaps:

- No `solutions` structure records the 20 ml Hutner's salts, 10 ml vitamin solution, or 50 ml/L Metals 44 stock nested inside Hutner's salts.
- Distilled water is missing from Solution 1, Solution 2, the vitamin solution, Hutner's salts, and Metals 44.
- Preparation steps are flattened and detached from their owning solution: final Solution 1 autoclaving, Solution 2 filter sterilization, vitamin-stock filtration, Hutner's pH adjustment, and Metals 44 precipitation handling all appear at one level.
- `physical_state: LIQUID` conflicts with the 9 g/L Gelrite solidifying agent in DSMZ 1439.
- Structured source provenance is incomplete; a curator must parse the `notes` string to recover DSMZ Medium 1439, and there is no structured link to DSMZ Medium 590 for Hutner's salts.

Correctly empty or not inherently defective:

- `target_organisms`, `growth_metrics`, and `evidence` are absent. The DSMZ recipe alone supports the formulation, not a narrow growth outcome.
- `discussion`, quality flags, parents, and variants are absent; the current record has no concrete preexisting discussion to review.

A gitignore-independent search with `rg --no-ignore --hidden` and `find` covered `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for `alkaliphiles_pirellula_medium_m1apy`, `ALKALIPHILES PIRELLULA MEDIUM (M1aPY)`, `mediadive.medium:1439`, and `CultureMech:000901`. It found this target, its normalized parent, registry/catalog/index references, older import reports, and no prior review report for this exact stem.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | M1aPY stock-solution and cross-reference boundaries were flattened into one ingredient array. | DSMZ 1439 uses Solution 1, Solution 2, and a vitamin solution; DSMZ 1439 also adds Hutner's basal salts from DSMZ 590, which itself nests Metals 44. The record has only direct `ingredients`. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1apy.yaml` or the MediaDive importer |
| major | Imported concentrations mix final-medium quantities with stock-local concentrations. | The record has `N-Acetylglucosamine` at `40 G_PER_L`, Hutner's NTA at `10 G_PER_L`, and Metals 44 ZnSO4 x 7 H2O at `1.095 G_PER_L`; those are solution-local values, not direct final-medium concentrations. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1apy.yaml` or the MediaDive importer |
| major | Duplicate salt rows from different formulation levels were summed. | `MgSO4 x 7 H2O` combines the Solution 1 and Hutner's rows as `30.220833 G_PER_L`; `FeSO4 x 7 H2O` combines the Hutner's and Metals 44 rows as `0.599 G_PER_L`. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1apy.yaml` and the duplicate-merge cleanup rule |
| major | Preparation instructions are scoped to the wrong thing. | Hutner's salts and Metals 44 preparation text from DSMZ 590 is stored as top-level M1aPY preparation, and the explicit addition of Solution 2 to Solution 1 after filter sterilization is not modeled as a relationship between stocks. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1apy.yaml` |
| major | The record marks the medium as liquid even though the DSMZ 1439 formula is Gelrite-containing. | DSMZ 1439 includes 9 g Gelrite in Solution 1; the record's `physical_state: LIQUID` is unsupported by the inspected source. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1apy.yaml` |
| minor | Direct base nutrients are not grounded. | The source has peptone and yeast extract in Solution 1; both rows currently have only `preferred_term` and concentration. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1apy.yaml` |
| minor | Source provenance is free text. | DSMZ 1439 is present only in `notes`, and the required DSMZ 590 Hutner's source is not represented structurally. | `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1apy.yaml` or import provenance mapping |

## Recommended Edits

1. Remodel `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1apy.yaml` around the source solution hierarchy: Solution 1 plus 20 ml Hutner's salts, post-autoclave Solution 2 plus 10 ml vitamin solution, and Metals 44 nested inside Hutner's salts.
2. Use an existing maintained Hutner's salts stock record such as `data/normalized_yaml/bacterial/hutners_salts_medium_590.yaml` or a dedicated `CultureMechTerm` link instead of duplicating DSMZ 590 stock components as top-level final ingredients.
3. Restore DSMZ amounts and units without summing across stock boundaries; keep Solution 1 `MgSO4 x 7H2O`, Hutner's `MgSO4 x 7 H2O`, Hutner's `FeSO4 x 7 H2O`, and Metals 44 `FeSO4 x 7 H2O` as distinct rows in their source containers.
4. Add missing distilled-water rows and the 20 ml, 10 ml, and 50 ml stock volumes.
5. Scope each preparation instruction to the relevant stock or final solution and preserve the filter-sterilized addition of Solution 2 to autoclaved Solution 1.
6. Correct `physical_state` unless an inspected liquid M1aPY source exists and is modeled as a separate variant.
7. Ground peptone, yeast extract, and the exact ammonium molybdate tetrahydrate form where the packaged MediaIngredientMech index supports them; otherwise leave exact unresolved source strings rather than forcing broader terms.
8. Move DSMZ Medium 1439 and DSMZ Medium 590 provenance out of the free-text-only `notes` path into structured references or source fields.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1apy.yaml`.
- Rerun `just verify-merges` and inspect `data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1apy.yaml` to confirm the generated merge keeps the nested solution structure.
- Rerun `just validate-products` after regenerating pages.
- Re-run exact `rg --no-ignore --hidden` checks for `CultureMech:000901`, `mediadive.medium:1439`, and `DSMZ_Medium1439` to confirm the normalized parent, generated merge, catalog, and indices agree.
- Compare the curated M1aPY record manually with `DSMZ_Medium1439.pdf` and `DSMZ_Medium590.pdf`, especially the Solution 1 base, 20 ml Hutner's salts, Solution 2, vitamin stock, Metals 44, water volumes, and pH/filter/autoclave steps.
- Re-run the duplicate and concentration plausibility reports, or equivalent focused scripts, to confirm `MgSO4 x 7 H2O`, `FeSO4 x 7 H2O`, and `ZnSO4 x 7 H2O` no longer report this record.

## Additional Notes

- The generated merge has one parent, and `data/merge_yaml/merged/alkaliphiles_pirellula_medium_m1apy.yaml` currently mirrors `data/normalized_yaml/bacterial/alkaliphiles_pirellula_medium_m1apy.yaml`.
- DSMZ 1439 references Hutner's basal salts from Medium 590 without spelling out that stock on the same page; the imported Hutner's and Metals 44 values match the Medium 590 PDF.
- `data/normalized_yaml/bacterial/hutners_salts_medium_590.yaml` already contains a curated nested Hutner's/Metals 44 representation of DSMZ Medium 590 that this record could reference instead of flattening.
- `just validate-schema`, `just validate-strict`, and `just validate-terms` were not run directly because project `uv` currently tries to build `llvmlite==0.46.0` under Python 3.13 before reaching record validation. The equivalent no-project validator invocations above were used instead.

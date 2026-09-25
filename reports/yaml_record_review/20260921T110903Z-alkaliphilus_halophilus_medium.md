# YAML Record Review: alkaliphilus_halophilus_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/alkaliphilus_halophilus_medium.yaml`
- Started UTC: 2026-09-21T11:07:58Z
- Finished UTC: 2026-09-21T11:09:05Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:004040` |
| Generated path reviewed | `data/merge_yaml/merged/alkaliphilus_halophilus_medium.yaml` |
| Maintained source path | `data/normalized_yaml/bacterial/alkaliphilus_halophilus_medium.yaml` |
| Merge source | `alkaliphilus_halophilus_medium` |
| Category | `bacterial` |
| Source accession | `komodo.medium:1290`, with copied DSMZ/MediaDive Medium 1290 formulation |
| Source label | KOMODO `ALKALIPHILUS HALOPHILUS medium`; DSMZ Medium 1290 `ALKALIPHILUS MEDIUM` |
| Source documents inspected | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf` |

The reviewed file is a generated merge from one normalized KOMODO record that has been enriched with the DSMZ Medium 1290 formulation. Future curation should change `data/normalized_yaml/bacterial/alkaliphilus_halophilus_medium.yaml`, the KOMODO/DSMZ enrichment path, or the stock-solution representation, then regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/alkaliphilus_halophilus_medium.yaml` | Passed: `No issues found` |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/alkaliphilus_halophilus_medium.yaml --out /private/tmp/alkaliphilus_halophilus_medium.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/alkaliphilus_halophilus_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/alkaliphilus_halophilus_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: this repository exposes `just validate-history` for standalone records under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record |

## Identity and Grounding

The source identity is a KOMODO-to-DSMZ duplicate: the YAML names `komodo.medium:1290` and `ALKALIPHILUS HALOPHILUS medium`, while its notes and ingredients point to DSMZ Medium 1290 / MediaDive 1290, `ALKALIPHILUS MEDIUM`. A direct DSMZ/MediaDive normalized sibling already exists at `data/normalized_yaml/bacterial/alkaliphilus_medium.yaml`.

DSMZ Medium 1290 is built from four terminal stocks:

| DSMZ component | Added amount |
|---|---:|
| Solution A | 950 ml |
| Solution B | 25 ml |
| Solution C | 1 ml |
| Solution D | 25 ml |

Solution A itself contains 10 ml Modified Wolin's mineral solution from Medium 141, and Solution C is a 10x Wolin vitamin solution from Medium 120. The generated record has no `solutions` rows and represents most stock contents as top-level final ingredients.

Ingredient identity gaps:

- `Yeast extract` and `Trypticase peptone` are ungrounded despite direct packaged MediaIngredientMech mappings.
- `NiCl2 x 6 H2O` is grounded to anhydrous `CHEBI:34887` / `nickel dichloride`, so the hexahydrate form is not preserved.
- `Calcium D-(+)-pantothenate` has a primary CHEBI term but no `mediaingredientmech_chebi_term`, despite a direct `CHEBI:31345` row in the packaged MediaIngredientMech label index.

## Evidence

DSMZ 1290 supports these stock-level amounts:

| Compartment | Source ingredient | Source amount | Current root value |
|---|---|---:|---:|
| Solution A | NaCl | 75 g / 950 ml A | `78.9474 G_PER_L`, then summed with stock NaCl to `79.9474 G_PER_L` |
| Solution A | MgSO4 x 7 H2O | 8.80 g / 950 ml A | `9.26316 G_PER_L`, then summed with stock MgSO4 to `12.26316 G_PER_L` |
| Solution A | Yeast extract | 10 g / 950 ml A | `10.5263 G_PER_L` |
| Solution A | Trypticase peptone | 10 g / 950 ml A | `10.5263 G_PER_L` |
| Solution B | D-Glucose | 2.50 g / 25 ml B | `100 G_PER_L` |
| Solution D | Na-thioglycolate | 0.50 g / 25 ml D | `20 G_PER_L` |
| Solution D | Na-ascorbate | 0.50 g / 25 ml D | `20 G_PER_L` |

The record stores Solution A, B, and D concentrations in their source container units. That makes the 25 ml B and D stocks about 40-fold too high for the completed medium, before accounting for the 1001 ml final volume.

The nested stocks were flattened as full-strength ingredients:

- Modified Wolin's mineral solution is added at 10 ml inside Solution A, but `Nitrilotriacetic acid`, `MnSO4 x H2O`, `FeSO4 x 7 H2O`, `CoSO4 x 7 H2O`, `CaCl2 x 2 H2O`, `ZnSO4 x 7 H2O`, `CuSO4 x 5 H2O`, `AlK(SO4)2 x 12 H2O`, `H3BO3`, `Na2MoO4 x 2 H2O`, `NiCl2 x 6 H2O`, `Na2SeO3 x 5 H2O`, and `Na2WO4 x 2 H2O` are top-level rows at stock strength.
- Wolin's vitamin solution (10x) is added as only 1 ml of Solution C, but all ten vitamin rows are top-level rows at 10x vitamin-stock strength.
- `NaCl` and `MgSO4 x 7 H2O` from Solution A were summed with their Modified Wolin stock rows even though those values belong to different containers.

DSMZ 1290's preparation protocol is absent from the YAML. The source dissolves Solution A, adjusts to pH 8.0 with 1 N NaOH, boils for 1 min, cools under 100% N2, dispenses under the same gas, autoclaves, adds filter-sterilized B, C, and D under 100% N2 before inoculation, and adjusts the completed medium to pH 8.0 with sterile anoxic 0.1 N HCl or 0.1 N NaOH if necessary.

## Completeness

Consequential gaps:

- No `solutions` block preserves Solutions A, B, C, D, Modified Wolin's mineral solution, or the 10x Wolin vitamin stock.
- No preparation step preserves the anaerobic Solution A boil/cool/dispense/autoclave sequence or the post-autoclave filter-sterilized additions.
- Root concentrations are the stock-container concentrations, not final-medium concentrations.
- `NaCl` and `MgSO4 x 7 H2O` were summed across Solution A and Modified Wolin's mineral solution.
- `NaOH` was extracted as a variable-concentration root ingredient from the pH note; the source also allows 0.1 N HCl or 0.1 N NaOH after completion, so pH adjustment should be procedural rather than a root ingredient.
- DSMZ, Medium 141, and Medium 120 provenance is only free text or implied by stock contents.

Correctly empty or not inherently defective:

- `target_organisms`, `growth_metrics`, and literature `evidence` are absent. The KOMODO/DSMZ source does not itself prove a strain-specific growth outcome.
- `parents`, `variants`, and `discussion` are absent; the direct formulation defects above are the urgent work.
- `ph_value: 8.0` and `physical_state: LIQUID` agree with DSMZ 1290.

A gitignore-independent search with `rg --no-ignore --hidden` and `find` covered `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for `alkaliphilus_halophilus_medium`, `CultureMech:004040`, `komodo.medium:1290`, `mediadive.medium:1290`, `DSMZ_Medium1290`, and the exact DSMZ sibling `alkaliphilus_medium`. It found this generated target, its KOMODO normalized parent, the direct DSMZ/MediaDive Medium 1290 sibling, generated/index/catalog entries, and historical validation/report rows. `find reports/yaml_record_review -name '*alkaliphilus_halophilus_medium.md'` found no prior report for this exact generated-record stem before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The DSMZ 1290 solution hierarchy has been flattened away. | DSMZ 1290 adds 950 ml Solution A, 25 ml Solution B, 1 ml Solution C, and 25 ml Solution D, with Modified Wolin's mineral solution nested under A; the record has only root `ingredients`. | `data/normalized_yaml/bacterial/alkaliphilus_halophilus_medium.yaml` or the DSMZ enrichment path |
| major | Stock-container concentrations are represented as final-medium concentrations. | Solution B contributes 2.50 g D-glucose in only 25 ml, but the record stores `100 G_PER_L`; Solution D contributes 0.50 g sodium thioglycolate and sodium ascorbate in 25 ml, but the record stores `20 G_PER_L` for each. | `data/normalized_yaml/bacterial/alkaliphilus_halophilus_medium.yaml` or the DSMZ enrichment path |
| major | The cleanup layer summed ingredients across different stock containers. | Solution A has 75 g NaCl and 8.80 g MgSO4 x 7 H2O, while Modified Wolin's mineral solution has 1 g/L NaCl and 3 g/L MgSO4 x 7 H2O; the record reports `79.9474` and `12.26316 G_PER_L` with duplicate-merge notes. | `data/normalized_yaml/bacterial/alkaliphilus_halophilus_medium.yaml` and the duplicate-merge cleanup rule |
| major | The DSMZ anaerobic preparation is missing. | The record has no `preparation_steps`, but DSMZ 1290 specifies Solution A pH adjustment, boiling, 100% N2 cooling and dispensing, autoclaving, filter sterilization of B/C/D, and anoxic post-autoclave addition. | `data/normalized_yaml/bacterial/alkaliphilus_halophilus_medium.yaml` |
| major | `NaOH` was imported as a root ingredient from a pH note. | DSMZ 1290 uses NaOH to adjust Solution A pH and allows HCl or NaOH to correct the complete medium; neither belongs as a variable-concentration medium component. | `data/normalized_yaml/bacterial/alkaliphilus_halophilus_medium.yaml` and the pH-buffer extraction rule |
| minor | Exact ingredient grounding is incomplete. | `Yeast extract` and `Trypticase peptone` are ungrounded despite MIM label-index hits; `NiCl2 x 6 H2O` resolves to anhydrous nickel dichloride; `Calcium D-(+)-pantothenate` lacks a `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/alkaliphilus_halophilus_medium.yaml` plus the packaged MediaIngredientMech label index |
| minor | Source provenance is not structured. | The normalized KOMODO record carries DSMZ Medium 1290, Medium 141, and Medium 120 only in notes or flattened stock rows; there are no structured references for the nested DSMZ stock sources. | `data/normalized_yaml/bacterial/alkaliphilus_halophilus_medium.yaml` or import provenance mapping |

## Recommended Edits

1. Re-curate `data/normalized_yaml/bacterial/alkaliphilus_halophilus_medium.yaml` from DSMZ Medium 1290 with `solutions` rows for Solution A, Solution B, Solution C, and Solution D at 950, 25, 1, and 25 ml.
2. Model Modified Wolin's mineral solution under Solution A at 10 ml and the Medium 120 10x Wolin vitamin stock under Solution C.
3. Move all stock-strength mineral and vitamin rows out of root `ingredients`.
4. Recompute or remove root ingredient concentrations so no Solution B, C, or D stock concentrations are treated as final-medium g/L values.
5. Undo `NaCl` and `MgSO4 x 7 H2O` cross-container sums.
6. Move `NaOH` into pH-adjustment preparation notes and include the optional final correction with sterile anoxic 0.1 N HCl or 0.1 N NaOH.
7. Add the DSMZ 1290 100% N2 preparation and post-autoclave B/C/D filtration and addition steps.
8. Ground `Yeast extract`, `Trypticase peptone`, `NiCl2 x 6 H2O`, and `Calcium D-(+)-pantothenate` with exact packaged MediaIngredientMech entries.
9. Add structured provenance for KOMODO 1290 plus DSMZ Medium 1290 and its Medium 141 / Medium 120 stock sources.
10. Regenerate `data/merge_yaml/merged/alkaliphilus_halophilus_medium.yaml`.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/alkaliphilus_halophilus_medium.yaml`.
- Rerun `just verify-merges` and inspect `data/merge_yaml/merged/alkaliphilus_halophilus_medium.yaml` to confirm the generated root record has stock `solutions` instead of full-strength nested rows.
- Rerun `just validate-references data/merge_yaml/merged/alkaliphilus_halophilus_medium.yaml` once structured DSMZ references are added.
- Rerun `just validate-products` after regenerating pages.
- Compare the regenerated record against DSMZ Medium 1290, especially Solution A/B/C/D amounts, Modified Wolin's mineral solution, Wolin's vitamin solution (10x), pH 8.0 handling, and 100% N2 preparation.
- Re-run exact `rg --no-ignore --hidden` checks for `CultureMech:004040`, `komodo.medium:1290`, `mediadive.medium:1290`, `DSMZ_Medium1290`, and `alkaliphilus_medium` across `data`, `src`, `scripts`, `history`, and reports.

## Additional Notes

- `data/normalized_yaml/bacterial/alkaliphilus_medium.yaml` is the direct DSMZ/MediaDive Medium 1290 sibling and appears to carry the same stock-flattening defects; review it separately when `data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml` is reached in sorted order.
- The search used to find prior reports included ignored files via `find`; there was no existing report with the exact `alkaliphilus_halophilus_medium` generated-record stem.
- `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` were not run directly because project `uv` currently tries to build `llvmlite==0.46.0` under Python 3.13 before reaching record validation. The equivalent no-project validator invocations above were used instead.

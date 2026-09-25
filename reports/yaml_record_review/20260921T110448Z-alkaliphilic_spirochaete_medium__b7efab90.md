# YAML Record Review: alkaliphilic_spirochaete_medium__b7efab90

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__b7efab90.yaml`
- Started UTC: 2026-09-21T11:02:22Z
- Finished UTC: 2026-09-21T11:04:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:001839` |
| Generated path reviewed | `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__b7efab90.yaml` |
| Maintained source path | `data/normalized_yaml/bacterial/alkaliphilic_spirochaete_medium.yaml` |
| Merge source | `alkaliphilic_spirochaete_medium` |
| Category | `bacterial` |
| Source accession | `mediadive.medium:700` |
| Source label | `ALKALIPHILIC SPIROCHAETE MEDIUM` / DSMZ Medium 700 |
| Related local stock records | `data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml`; `data/normalized_yaml/bacterial/mediadive_242_Wolin_s_vitamin_solution.yaml` |
| Source documents inspected | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium700.pdf`; `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf` |

The reviewed file is a generated merge from one normalized MediaDive import. Future curation should change `data/normalized_yaml/bacterial/alkaliphilic_spirochaete_medium.yaml`, the MediaDive importer, or the maintained MediaDive solution-linking inputs, then regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/alkaliphilic_spirochaete_medium__b7efab90.yaml` | Passed: `No issues found` |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/alkaliphilic_spirochaete_medium__b7efab90.yaml --out /private/tmp/alkaliphilic_spirochaete_medium__b7efab90.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/alkaliphilic_spirochaete_medium__b7efab90.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/alkaliphilic_spirochaete_medium__b7efab90.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: this repository exposes `just validate-history` for standalone records under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record |

## Identity and Grounding

The record identity is sound: `CultureMech:001839` is the direct MediaDive/DSMZ Medium 700 import for `ALKALIPHILIC SPIROCHAETE MEDIUM`, and the source accession `mediadive.medium:700` agrees with the cited DSMZ Medium 700 PDF.

DSMZ 700 uses two cross-referenced DSMZ Medium 141 stocks:

| DSMZ 700 stock addition | Matching local `SolutionRecipe` | Current record state |
|---|---|---|
| 10 ml vitamin solution | `CultureMech:011808`, `mediadive.solution:242`, Wolin's vitamin solution | No `solutions` row; stock composition rows are top-level final-medium ingredients |
| 1 ml trace element solution | `CultureMech:011798`, `mediadive.solution:241`, Modified Wolin's mineral solution | No `solutions` row; most stock composition rows are top-level final-medium ingredients |

The base ingredients, pH 9.7, and anaerobic/autoclave/post-addition preparation are carried from DSMZ 700, but the stock boundaries are not.

Ingredient identity gaps:

- `Yeast extract` is ungrounded even though the packaged MediaIngredientMech label index has a direct `FOODON:03315426` mapping.
- `NiCl2 x 6 H2O` is grounded to anhydrous `CHEBI:34887` / `nickel dichloride`, so the hexahydrate form is not preserved.
- `Calcium D-(+)-pantothenate` has a primary CHEBI term but no `mediaingredientmech_chebi_term`, despite a direct `CHEBI:31345` row in the packaged MediaIngredientMech label index.

## Evidence

DSMZ Medium 700 supports the base medium: 10 g Na2CO3, 15 g NaHCO3, 10 g NaCl, 0.2 g K2HPO4, 1 g NH4Cl, 0.2 g KCl, 1 g Na2S x 9 H2O, 0.5 g yeast extract, 5 g sucrose, 10 ml vitamin solution from Medium 141, 1 ml trace element solution from Medium 141, 1000 ml distilled water, and pH adjustment to 9.7. The root preparation steps also preserve the DSMZ 700 sequence: prepare under N2 while omitting carbonate, bicarbonate, sulfide, sucrose, and vitamins; boil and cool under nitrogen; add carbonate and bicarbonate; adjust with 6N NaOH; autoclave; add neutralized sulfide, vitamins, and sucrose from sterile stock solutions.

The two Medium 141 stocks are flattened instead of referenced:

| Stock | Source concentration | Stock addition to DSMZ 700 | Current root row |
|---|---:|---:|---:|
| Biotin in Wolin's vitamin solution | 0.002 g/L | 10 ml/L | `0.002 G_PER_L` |
| Folic acid in Wolin's vitamin solution | 0.002 g/L | 10 ml/L | `0.002 G_PER_L` |
| Pyridoxine hydrochloride in Wolin's vitamin solution | 0.01 g/L | 10 ml/L | `0.01 G_PER_L` |
| Nitrilotriacetic acid in Modified Wolin's mineral solution | 1.5 g/L | 1 ml/L | `1.5 G_PER_L` |
| MgSO4 x 7 H2O in Modified Wolin's mineral solution | 3 g/L | 1 ml/L | `3 G_PER_L` |
| NaCl in Modified Wolin's mineral solution | 1 g/L | 1 ml/L | folded into a root `11.0 G_PER_L` NaCl row |

The vitamin rows are stock-strength values that should be diluted 100-fold in the final medium if they are flattened at all. The trace rows are stock-strength values that should be diluted 1000-fold in the final medium if they are flattened at all.

The trace stock composition is also stale relative to the current local `mediadive.solution:241` record and the live DSMZ Medium 141 PDF:

| Ingredient | Local `mediadive.solution:241` | Current DSMZ 700 import |
|---|---:|---:|
| `NiCl2 x 6 H2O` | `0.03 G_PER_L` | `0.025 G_PER_L` |
| `Na2WO4 x 2 H2O` | `0.0004 G_PER_L` | absent |

## Completeness

Consequential gaps:

- The generated record has no `solutions` block for DSMZ 700's 10 ml/L Wolin vitamin stock or 1 ml/L Modified Wolin mineral stock.
- DSMZ Medium 141 stock constituents are top-level `ingredients` rows in stock concentrations rather than nested under the relevant stock recipes or linked through local `SolutionRecipe` records.
- `NaCl` from the base medium and `NaCl` from the trace stock were summed across different preparation containers.
- The generated root medium omits `Na2WO4 x 2 H2O`, which is present in the maintained local Modified Wolin stock and in the live DSMZ Medium 141 PDF.
- DSMZ and MediaDive provenance is present only in free-text `notes` plus the `media_term`; there are no structured source or retrieval fields for DSMZ 700 or DSMZ 141.

Correctly empty or not inherently defective:

- `target_organisms`, `growth_metrics`, and literature `evidence` are absent. The DSMZ recipe source does not itself prove a strain-specific growth outcome.
- `parents`, `variants`, `discussion`, and `data_quality_flags` are absent; the direct formulation defects above are the urgent work.

A gitignore-independent search with `rg --no-ignore --hidden` and `find` covered `data`, `src`, `scripts`, `pages`, `app`, and `reports/yaml_record_review` for `alkaliphilic_spirochaete_medium__b7efab90`, `CultureMech:001839`, `mediadive.medium:700`, `mediadive.solution:241`, `mediadive.solution:242`, and `DSMZ, ID: 700`. It found this generated target, its normalized MediaDive parent, the two maintained Wolin stock recipes, index entries, adjacent generated page rows, and a KOMODO sibling for DSMZ 700. `find reports/yaml_record_review -name '*alkaliphilic_spirochaete_medium__b7efab90.md'` found no prior report for this exact generated-record stem before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | DSMZ Medium 141 vitamin and trace stocks were flattened into final-medium ingredients. | DSMZ 700 adds 10 ml/L of vitamin stock and 1 ml/L of trace stock; the generated record places those stock components directly under root `ingredients` at stock concentrations. | `data/normalized_yaml/bacterial/alkaliphilic_spirochaete_medium.yaml` or the MediaDive importer |
| major | The record omits the `solutions` rows that would preserve the 10 ml/L and 1 ml/L stock additions. | Local `SolutionRecipe` records already exist for `mediadive.solution:241` and `mediadive.solution:242`, but the target has no `solutions:` key. | `data/normalized_yaml/bacterial/alkaliphilic_spirochaete_medium.yaml` or the MediaDive solution-linking rule |
| major | The cleanup layer summed `NaCl` across the base medium and the trace stock. | DSMZ 700 has 10 g base `NaCl`; Modified Wolin's mineral solution has 1 g/L `NaCl` before 1000-fold dilution; the record reports one `11.0 G_PER_L` row with `[Merged 2 duplicates: 10.0, 1.0]`. | `data/normalized_yaml/bacterial/alkaliphilic_spirochaete_medium.yaml` and the duplicate-merge cleanup rule |
| major | The inlined trace stock is stale relative to the maintained stock recipe. | `mediadive.solution:241` has `0.03 G_PER_L` `NiCl2 x 6 H2O` and `0.0004 G_PER_L` `Na2WO4 x 2 H2O`; the target has `0.025 G_PER_L` nickel chloride hexahydrate and no tungstate row. | `data/normalized_yaml/bacterial/alkaliphilic_spirochaete_medium.yaml`, `data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml`, or the MediaDive import snapshot |
| minor | Exact-form ingredient grounding is incomplete. | `Yeast extract` lacks a term despite a MIM label-index hit, `NiCl2 x 6 H2O` resolves to anhydrous nickel dichloride, and `Calcium D-(+)-pantothenate` lacks a `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/alkaliphilic_spirochaete_medium.yaml` plus the packaged MediaIngredientMech label index |
| minor | Source provenance is not structured. | The generated record preserves DSMZ import details only as `notes: 'Source: DSMZ | Link: ...'`, `media_term: mediadive.medium:700`, and a free-text curation-history note. | `data/normalized_yaml/bacterial/alkaliphilic_spirochaete_medium.yaml` or import provenance mapping |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/alkaliphilic_spirochaete_medium.yaml`, replace the flattened DSMZ Medium 141 vitamins and trace elements with two `solutions` entries: 10 ml/L Wolin's vitamin solution and 1 ml/L Modified Wolin's mineral solution.
2. Link those `solutions` entries to maintained `SolutionRecipe` records `mediadive.solution:242` and `mediadive.solution:241`, or create DSMZ-versioned stock records if MediaDive Medium 700 intentionally used an older Medium 141 stock snapshot.
3. Remove the top-level stock component rows for biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, lipoic acid, NTA, trace salts, and trace metals once the stock links own those compositions.
4. Undo the `NaCl` cross-container sum by keeping the 10 g/L base `NaCl` separate from the Modified Wolin mineral solution's stock `NaCl`.
5. Reconcile the trace-stock version mismatch: either update the Medium 700 record to the current `mediadive.solution:241` composition, including `Na2WO4 x 2 H2O`, or document and preserve the exact older stock source that had `0.025 G_PER_L` `NiCl2 x 6 H2O` and no tungstate.
6. Correct `Yeast extract`, `NiCl2 x 6 H2O`, and `Calcium D-(+)-pantothenate` grounding using exact packaged MediaIngredientMech entries.
7. Add structured provenance for the DSMZ 700 and DSMZ 141 documents or for the MediaDive records that supplied their formulations.
8. Regenerate `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__b7efab90.yaml` from the normalized record.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/alkaliphilic_spirochaete_medium.yaml`.
- Rerun `just verify-merges` and inspect `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__b7efab90.yaml` to confirm the generated root record has base ingredients plus two stock `solutions`, not stock-strength Wolin components as final ingredients.
- Rerun `just validate-references data/merge_yaml/merged/alkaliphilic_spirochaete_medium__b7efab90.yaml` once structured DSMZ and solution references are added.
- Rerun `just validate-products` after regenerating pages.
- Compare the regenerated record against DSMZ Medium 700 and the intended DSMZ Medium 141 or MediaDive stock snapshot, especially the 10 ml/L vitamin addition, 1 ml/L trace-element addition, pH 9.7, and anaerobic post-autoclave additions.
- Re-run exact `rg --no-ignore --hidden` checks for `CultureMech:001839`, `mediadive.medium:700`, `mediadive.solution:241`, and `mediadive.solution:242` across `data`, `src`, `scripts`, `pages`, `app`, and reports.

## Additional Notes

- The adjacent `data/merge_yaml/merged/alkaliphilic_spirochaete_medium__963579e5.yaml` target is a TOGO M2769 import of the same DSMZ Medium 700 recipe and has the same core stock-flattening issue through a different normalized parent.
- The search used to find prior reports included ignored files via `find`; there was no existing report with the exact `alkaliphilic_spirochaete_medium__b7efab90` generated-record stem.
- `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` were not run directly because project `uv` currently tries to build `llvmlite==0.46.0` under Python 3.13 before reaching record validation. The equivalent no-project validator invocations above were used instead.

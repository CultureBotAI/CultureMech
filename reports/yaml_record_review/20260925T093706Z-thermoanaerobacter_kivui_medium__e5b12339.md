# YAML Record Review: THERMOANAEROBACTER KIVUI MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoanaerobacter_kivui_medium__e5b12339.yaml`
- Started UTC: `2026-09-25T09:37:06Z`
- Finished UTC: `2026-09-25T09:38:18Z`
- Verdict: needs curation

## Target
Generated bacterial recipe `CultureMech:001198`, `thermoanaerobacter_kivui_medium`, with medium term `mediadive.medium:171` and label `THERMOANAEROBACTER KIVUI MEDIUM`.

It merges the MediaDive DSMZ 171 source `thermoanaerobacter_kivui_medium` with the KOMODO source duplicate `acetogenium_medium` on merge fingerprint `e5b123396312a6b1c53a95df77a87dac30a1d558647965ae7baf83ddfb34117b`.

## Validation
- LinkML schema validation: passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The MediaDive/KOMODO branch is correctly grounded to DSMZ Medium 171, `THERMOANAEROBACTER KIVUI MEDIUM`, and `komodo.medium:171` is a correct source-equivalent alias.

The same DSMZ 171 PDF is also represented by TOGO source `TOGO:M2747`, emitted separately as `data/merge_yaml/merged/THERMOANAEROBACTER_KIVUI_MEDIUM.yaml`.

Reviewed ingredient-level CHEBI terms on the MediaDive/KOMODO branch are internally consistent, including the heptahydrate, dodecahydrate, selenite pentahydrate, and tungstate dihydrate rows.

## Evidence
DSMZ Medium 171 and MediaDive medium 171 describe a main solution with direct phosphate, ammonium, chloride, magnesium, calcium, resazurin, cysteine, sulfide, and water ingredients plus 2 ml FeSO4 x 7 H2O solution and 10 ml Modified Wolin's mineral solution.

The generated record flattened Modified Wolin's mineral solution into the top-level final recipe. That injected its 1 L stock recipe as final concentrations, including `1.5 G_PER_L` nitrilotriacetic acid, `3 G_PER_L` MgSO4 x 7 H2O, `1 G_PER_L` NaCl, `0.1 G_PER_L` FeSO4 x 7 H2O, and the rest of the trace metals.

Stock rows were then merged with direct rows: `NaCl` became `1.442043 G_PER_L`, `MgSO4 x 7 H2O` became `3.0884086 G_PER_L`, `CaCl2 x 2 H2O` became `0.10589391000000001 G_PER_L`, and `FeSO4 x 7 H2O` became `1.1 G_PER_L`.

The FeSO4 x 7 H2O stock was also flattened separately. Its 0.1 N H2SO4 solvent became a top-level `H2SO4` row at `1000 G_PER_L`, although DSMZ only adds 2 ml of this acidified FeSO4 stock to the final medium.

## Completeness
The MediaDive/KOMODO branch preserves the DSMZ main anoxic H2/CO2 preparation instructions, post-inoculation H2/CO2 pressurization, the Modified Wolin pH adjustment step, and the unstable FeSO4-stock note.

The generated hierarchy is incomplete: those stock-specific steps now point to ingredients that have been collapsed into the final medium instead of to separate stock recipes.

## Findings
1. Needs curation: Modified Wolin's mineral solution was flattened into direct top-level ingredients at stock concentrations.
2. Needs curation: FeSO4 x 7 H2O solution was flattened into top-level `FeSO4 x 7 H2O` and `H2SO4` rows, including an impossible `1000 G_PER_L` final H2SO4 concentration.
3. Needs curation: duplicate stock and direct rows were merged for NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and FeSO4 x 7 H2O, corrupting final concentrations and hiding the solution boundaries.
4. Needs curation: TOGO M2747 remains an unmerged DSMZ 171 duplicate branch.

## Recommended Edits
1. Normalize the DSMZ 171 MediaDive, KOMODO, and TOGO source records, not the generated merge YAML, to retain 2 ml/L FeSO4 x 7 H2O solution and 10 ml/L Modified Wolin's mineral solution as nested stock additions.
2. Keep the FeSO4 stock's 0.1 N H2SO4 as the stock solvent/annotation rather than a direct `G_PER_L` ingredient.
3. Merge `mediadive.medium:171`, `komodo.medium:171`, and `TOGO:M2747` by exact DSMZ 171 source identity after the three import branches represent stocks consistently.
4. Regenerate generated YAML and confirm no final ingredient value is produced by summing a main-solution row with a stock-solution row.

## Follow-up Checks
After source normalization and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `mediadive.medium:171`, `komodo.medium:171`, `TOGO:M2747`, and `DSMZ_Medium171.pdf` and confirm that all DSMZ 171 data regenerates as one canonical record.

## Additional Notes
Exact duplicate-source searches included ignored files.

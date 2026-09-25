# YAML Record Review: THERMOANAEROMONAS medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoanaeromonas_medium__b7e31a5b.yaml`
- Started UTC: `2026-09-25T09:45:17Z`
- Finished UTC: `2026-09-25T09:46:47Z`
- Verdict: needs curation

## Target
Generated bacterial recipe `CultureMech:006920`, `thermoanaeromonas_medium`, with medium term `komodo.medium:963` and label `THERMOANAEROMONAS medium`.

It merges the KOMODO `komodo.medium:963` source with the matching MediaDive DSMZ Medium 963 source.

## Validation
- LinkML schema validation: passed; `linkml-validate` reported `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The branch is correctly identified as DSMZ Medium 963, `THERMOANAEROMONAS MEDIUM`; the KOMODO record explicitly records DSMZ Medium 963 provenance and was merged with the same MediaDive source identity.

Reviewed CHEBI terms are internally consistent for the direct medium rows and flattened stock rows, including Na3-EDTA, thiosulfate pentahydrate, selenite pentahydrate, and tungstate dihydrate.

No unmerged exact DSMZ 963 duplicate was found in an exact search over normalized and generated YAML with ignored files included.

## Evidence
DSMZ Medium 963 and MediaDive medium 963 define a main solution with K2HPO4, KH2PO4, Na3-EDTA, FeSO4 x 7 H2O, MgSO4 x 7 H2O, CaCl2 x 2 H2O, NaCl, NH4Cl, D-glucose, yeast extract, 10 ml Trace element solution, resazurin, NaHCO3, Na2S2O3 x 5 H2O, 1 ml Wolin's vitamin solution 10x, L-cysteine HCl x H2O, and water.

The generated record flattens the 10 ml Trace element solution into final top-level rows at stock recipe concentrations, including `Nitrilotriacetic acid` at `12.8 G_PER_L`, `FeCl2 x 4 H2O` at `1 G_PER_L`, and the rest of the trace salts.

Stock rows also merged with base rows: `CaCl2 x 2 H2O` is `0.1296736 G_PER_L` from direct `0.0296736` plus stock `0.1`, and `NaCl` is `1.197824 G_PER_L` from direct `0.197824` plus stock `1.0`.

The generated record flattens the 1 ml Wolin's vitamin solution 10x into final top-level rows at stock concentrations such as `Biotin` at `0.02 G_PER_L`, `Pyridoxine hydrochloride` at `0.1 G_PER_L`, and `Vitamin B12` at `0.001 G_PER_L`.

## Completeness
The DSMZ/MediaDive preparation step is missing from the generated KOMODO branch, including the N2/CO2 sparging, bicarbonate pH adjustment, anoxic autoclaving, filtered stock additions, and pH 6.5 final adjustment.

The DSM 26576 strain-specific pH 7.5 note from the DSMZ PDF is not represented.

## Findings
1. Needs curation: Trace element solution was flattened into top-level final ingredients and its CaCl2 and NaCl rows were merged with base rows.
2. Needs curation: Wolin's vitamin solution 10x was flattened into top-level final vitamin rows at stock concentrations.
3. Needs curation: DSMZ 963 preparation instructions and the DSM 26576 pH note are missing from the generated KOMODO branch.

## Recommended Edits
1. Normalize the KOMODO and MediaDive DSMZ 963 sources, not this generated merge file, so Trace element solution and Wolin's vitamin solution 10x remain 10 ml/L and 1 ml/L nested additions.
2. Preserve the DSMZ preparation step and DSM 26576 pH 7.5 note during the DSMZ 963 normalization.
3. Regenerate merge YAML and verify that stock CaCl2 and NaCl are no longer summed into the main-solution rows.

## Follow-up Checks
After source normalization and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `komodo.medium:963`, `mediadive.medium:963`, and `DSMZ_Medium963.pdf` and confirm that DSMZ 963 still regenerates as a single canonical output.

## Additional Notes
Exact duplicate-source searches included ignored files.

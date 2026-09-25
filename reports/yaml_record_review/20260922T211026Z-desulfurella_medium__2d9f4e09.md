# YAML Record Review: DESULFURELLA MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfurella_medium__2d9f4e09.yaml`
- Started UTC: 2026-09-22T21:10:26Z
- Finished UTC: 2026-09-22T21:10:26Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:001605` for `desulfurella_medium`, a MediaDive import of DSMZ Medium 480.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `mediadive.medium:480`, `DESULFURELLA MEDIUM`, with DSMZ provenance in `notes`.

A gitignore-independent Desulfurella lookup found the DSMZ 480 normalized source, a split TOGO M3130 companion for the same DSMZ Medium 480 page, and a distinct brackish-water Desulfurella variant.

## Evidence

MediaDive 480 represents the main recipe as a 1002 ml solution with NH4Cl, CaCl2 x 2 H2O, MgCl2 x 6 H2O, KCl, KH2PO4, 1 ml Trace element solution SL-10, yeast extract, 0.5 ml sodium resazurin at 0.1% w/v, sulfur, Na-acetate, NaHCO3, 1 ml Wolin's vitamin solution, DL-dithiothreitol, and 1000 ml distilled water.

Trace element solution SL-10 is a 1000 ml stock containing 10 ml 25% HCl, FeCl2 x 4 H2O, zinc, manganese, borate, cobalt, copper, nickel, molybdate, and 990 ml distilled water. Wolin's vitamin solution is a 1000 ml stock containing ten vitamin rows plus water.

## Completeness

The target preserves the DSMZ pH range and the main preparation text for sparging under 80% N2 and 20% CO2, heating in a boiling water bath on three successive days, and adding acetate, vitamins, dithiothreitol, and bicarbonate from sterile anoxic stocks.

The composition is incomplete because the 1 ml Trace element and 1 ml Wolin's vitamin additions are absent as `solutions`. Their stock constituents were flattened into top-level ingredient rows at stock concentrations, and the water rows for the main solution and both stocks are missing.

## Findings

- High: Trace element solution SL-10 was flattened. HCl, FeCl2 x 4 H2O, zinc, manganese, borate, cobalt, copper, nickel, and molybdate are listed at stock strengths instead of inside a 1 ml/L solution addition.
- High: Wolin's vitamin solution was flattened. Its biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid concentrations are stock concentrations rather than 1 ml/L final-medium contributions.
- Medium: The 1000 ml main distilled-water row, 990 ml Trace element stock water row, and 1000 ml Wolin's vitamin stock water row are absent.
- Low: The Trace element solution preparation instruction was appended as a top-level preparation step instead of being scoped to the Trace element stock recipe.
- Medium: The exact TOGO M3130 DSMZ 480 companion remains split from the MediaDive record and carries a 2990.0 G/L water row plus stock milligram rows promoted to G/L.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfurella_medium.yaml` so DSMZ 480 uses structured 1 ml additions for Trace element solution SL-10 and Wolin's vitamin solution.
- Move both stock recipes into subordinate `solutions` entries with their own water rows.
- Keep the main 1000 ml distilled-water row in the repaired main solution.
- Repair `data/normalized_yaml/bacterial/TOGO_M3130_Desulfurella_Medium.yaml` so it can reconcile with the curated DSMZ 480 import instead of generating as a split exact duplicate.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate merged YAML and confirm the repaired main recipe has Trace element and Wolin's vitamin source-volume additions rather than stock-strength top-level trace-metal and vitamin rows.
- Verify DSMZ Medium 480 is no longer split across the MediaDive and TOGO generated records unless they are deliberately retained as documented source duplicates.

## Additional Notes

None found.

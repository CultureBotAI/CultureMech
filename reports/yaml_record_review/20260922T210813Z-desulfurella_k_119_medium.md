# YAML Record Review: DESULFURELLA (K-119) MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfurella_k_119_medium.yaml`
- Started UTC: 2026-09-22T21:08:13Z
- Finished UTC: 2026-09-22T21:08:13Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:001608` for `desulfurella_k_119_medium`, a MediaDive import of DSMZ Medium 480c.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `mediadive.medium:480c`, `DESULFURELLA (K-119) MEDIUM`, with DSMZ provenance in `notes`.

A gitignore-independent exact filename lookup found only the DSMZ 480c normalized source for the K-119 filename. The generated record merges that source with five DSMZ 480-family KOMODO or MediaDive records, including a `thermoproteus_uzoniensis_medium` synonym from the archaeal category.

## Evidence

MediaDive 480c represents the main recipe as a 1002 ml solution with NH4Cl, CaCl2 x 2 H2O, MgCl2 x 6 H2O, KCl, KH2PO4, 1 ml Trace element solution SL-10, MOPS buffer, yeast extract, 0.5 ml sodium resazurin at 0.1% w/v, sulfur, Na-DL-lactate, Na2CO3, 1 ml Wolin's vitamin solution, sodium sulfide, and 1000 ml distilled water.

Trace element solution SL-10 is a 1000 ml stock containing 10 ml 25% HCl, FeCl2 x 4 H2O, zinc, manganese, borate, cobalt, copper, nickel, molybdate, and 990 ml distilled water. Wolin's vitamin solution is a 1000 ml stock containing ten vitamin rows plus water.

## Completeness

The target preserves the DSMZ pH range and the main preparation text for sparging under 80% N2 and 20% CO2, heating in a boiling water bath on three successive days, and adding lactate, vitamins, sulfide, and carbonate from sterile anoxic stocks.

The composition is incomplete because the 1 ml Trace element and 1 ml Wolin's vitamin additions are absent as `solutions`. Their stock constituents were flattened into top-level ingredient rows at stock concentrations, and the water rows for the main solution and both stocks are missing.

## Findings

- High: Trace element solution SL-10 was flattened. HCl, FeCl2 x 4 H2O, zinc, manganese, borate, cobalt, copper, nickel, and molybdate are listed at stock strengths instead of inside a 1 ml/L solution addition.
- High: Wolin's vitamin solution was flattened. Its biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid concentrations are stock concentrations rather than 1 ml/L final-medium contributions.
- Medium: The 1000 ml main distilled-water row, 990 ml Trace element stock water row, and 1000 ml Wolin's vitamin stock water row are absent.
- Low: The Trace element solution preparation instruction was appended as a top-level preparation step instead of being scoped to the Trace element stock recipe.
- Medium: Six DSMZ 480-family sources currently merge on the flattened ingredient signature; those relationships need to be rechecked after the repaired stock topology changes the merge fingerprint.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfurella_k_119_medium.yaml` so DSMZ 480c uses structured 1 ml additions for Trace element solution SL-10 and Wolin's vitamin solution.
- Move both stock recipes into subordinate `solutions` entries with their own water rows.
- Keep the main 1000 ml distilled-water row in the repaired main solution.
- Re-evaluate the five DSMZ 480-family sibling records that currently merge into this generated target after the DSMZ 480c topology is fixed.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate merged YAML and confirm the repaired main recipe has Trace element and Wolin's vitamin source-volume additions rather than stock-strength top-level trace-metal and vitamin rows.
- Verify each DSMZ 480-family source either merges as a deliberate source duplicate or remains a documented child of the repaired DSMZ 480c record.

## Additional Notes

None found.

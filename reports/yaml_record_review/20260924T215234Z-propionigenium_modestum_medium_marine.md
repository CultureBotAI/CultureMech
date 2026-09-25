# YAML Record Review: propionigenium_modestum_medium_marine

- Repository: CultureMech
- Record: data/merge_yaml/merged/propionigenium_modestum_medium_marine.yaml
- Started UTC: 2026-09-24T21:52:34Z
- Finished UTC: 2026-09-24T21:52:34Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:015351`, the generated liquid `PROPIONIGENIUM MODESTUM MEDIUM (MARINE)` record grounded to DSMZ/MediaDive Medium 293 and merged from `for_dsm_2376`, `propionigenium_modestum_medium`, `ven_chi2_medium`, and `propionigenium_modestum_medium_marine`.

## Validation

- LinkML validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `scripts/validate_strict.py` scanned one file and reported zero `ERROR` rows.
- Reference validation: Passed; `linkml-reference-validator` validated one file and reported zero reference checks.
- Term validation: Passed; `linkml-term-validator` exited 0.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The merge identity is plausible: MediaDive Medium 293 is `PROPIONIGENIUM MODESTUM MEDIUM (MARINE)`, and the three KOMODO aliases all point back to DSMZ/MediaDive 293 or 293a. An exact ignored YAML search for `mediadive.medium:293`, `DSMZ_Medium293`, `DSMZ, ID: 293`, and the four merged source names found this generated record, the four normalized inputs involved in the merge, and a few unrelated records that reference the same old DSMZ PDF URL in source history.

## Evidence

MediaDive REST for medium 293 reports a main 1001 ml solution containing 0.2 g KH2PO4, 0.25 g NH4Cl, 20 g NaCl, 3 g MgCl2 x 6 H2O, 0.5 g KCl, 0.15 g CaCl2 x 2 H2O, 1 ml Trace element solution SL-10, 0.5 ml 0.1% w/v sodium resazurin, 1.25 g Na2CO3, 3.25 g disodium succinate, 0.36 g Na2S x 9 H2O, and 1000 ml distilled water. The same payload defines SL-10 as a 1000 ml stock containing 10 ml 25% HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 990 ml water.

The generated record preserves the main dry-salt masses and the pH 7.2 to 7.5 range, but it imports SL-10 stock ingredients as if their stock-strength g/L values were full-strength final-medium ingredients.

## Completeness

The medium is missing the main 1000 ml distilled water addition, the 1 ml/L SL-10 addition, the 990 ml SL-10 stock water, and the SL-10 solution boundary. Its preparation text still describes adding carbonate, succinate, and sulfide from stock solutions, but the recipe has no carbonate, succinate, or sulfide stock-solution structures.

## Findings

- The 1 ml `Trace element solution SL-10` addition is absent from `ingredients` or `solutions`; instead, all SL-10 stock salts are flattened into the final medium at the stock's per-liter concentrations.
- `HCl` is listed as `2.5 G_PER_L`, but the source has 10 ml of 25% HCl inside the 1000 ml SL-10 stock.
- The main 1000 ml distilled water and the SL-10 stock's 990 ml distilled water are both omitted.
- The preparation step says carbonate, succinate, and sulfide are added from sterile anoxic stock solutions, but `Na2CO3`, disodium succinate, and `Na2S x 9 H2O` are modeled only as top-level dry ingredients.

## Recommended Edits

- Repair the normalized MediaDive and KOMODO Medium 293 records so the final recipe keeps the main salts in the main medium and has a `Trace element solution SL-10` addition at 1 ml/L with the DSMZ/MediaDive stock composition nested under it.
- Add distilled water rows for the main recipe and the SL-10 stock instead of dropping them during import.
- Move the 25% HCl aliquot into the SL-10 solution as a liquid addition rather than modeling it as pure `HCl`.
- Consider whether the carbonate, succinate, and sulfide additions should be modeled as named stock solutions or annotated as stock-added final solutes so the preparation instructions and ingredient graph agree.
- Regenerate `data/merge_yaml/merged` and verify that all four DSMZ 293 synonyms still coalesce into one canonical record.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merged record.
- Repeat an exact ignored search for `mediadive.medium:293` and the four merged source names to verify that the repaired source records still merge and that no stale DSMZ 293 branch remains.

## Additional Notes

None.

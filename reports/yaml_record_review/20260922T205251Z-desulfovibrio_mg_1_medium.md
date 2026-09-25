# YAML Record Review: DESULFOVIBRIO (MG-1) MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_mg_1_medium.yaml`
- Started UTC: 2026-09-22T20:52:51Z
- Finished UTC: 2026-09-22T20:53:04Z
- Verdict: pass with minor issues

## Target

Reviewed generated merged record `CultureMech:006106` for `desulfovibrio_mg_1_medium`, the KOMODO 615 import of DSMZ Medium 615.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `komodo.medium:615`, `DESULFOVIBRIO MG-1 medium`, and its notes state that KOMODO 615 came from DSMZ Medium 615.

A gitignore-independent exact lookup found only the KOMODO 615 import and the matching DSMZ 615 MediaDive normalized source. The generated merge correctly collapsed those same-category source duplicates and kept the `SOURCE_DUPLICATE` relationship from the KOMODO import to `data/normalized_yaml/bacterial/desulfovibrio_mg_1_medium.yaml`.

## Evidence

MediaDive 615 represents `DESULFOVIBRIO (MG-1) MEDIUM` as one 1004 ml solution at pH 7.5. Its non-water recipe rows are 1 g NH4Cl, 0.5 g KH2PO4, 4.5 g Na2SO4, 0.04 g CaCl2 x 2 H2O, 0.06 g MgSO4 x 7 H2O, 2 g glycerol, 1 g yeast extract, 0.6 g trisodium citrate x 2 H2O, 0.5 ml sodium resazurin at 0.1% w/v, 4 ml FeSO4 x 7 H2O at 0.1% w/v in 0.1 N H2SO4, and 0.1 g Na-thioglycolate in 1000 ml distilled water.

The generated record matches MediaDive final G/L values for all non-water ingredients and preserves the pH 7.5 anaerobic preparation text.

## Completeness

The substantive formula is complete: there are no separate stock recipes to nest under `solutions`, and the FeSO4 addition is present at the correct final concentration calculated from the 4 ml addition.

Two source details are absent. The target omits the 1000 ml distilled-water row, and the FeSO4 ingredient is no longer annotated as a 4 ml addition of a 0.1% w/v stock in 0.1 N H2SO4.

## Findings

- Medium: The 1000 ml distilled-water row from DSMZ 615 is absent.
- Low: The FeSO4 x 7 H2O row keeps the correct final amount but drops the source attribute that it is supplied as 4 ml of 0.1% w/v FeSO4 x 7 H2O in 0.1 N H2SO4.

## Recommended Edits

- Add the DSMZ 615 distilled-water row to `data/normalized_yaml/bacterial/desulfovibrio_mg_1_medium.yaml`.
- Preserve the FeSO4 source stock wording so the generated record still shows the source addition as 4 ml of 0.1% w/v FeSO4 x 7 H2O in 0.1 N H2SO4.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate merged YAML and confirm the KOMODO 615 and DSMZ 615 records still merge into one `SOURCE_DUPLICATE` output.
- Verify the regenerated recipe keeps the eleven non-water rows, the 1000 ml distilled-water row, pH 7.5, and the anaerobic preparation text.

## Additional Notes

None found.

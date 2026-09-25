# YAML Record Review: ectothiorhodospira_abdelmalekii_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ectothiorhodospira_abdelmalekii_medium__828e5ee6.yaml
- Started UTC: 2026-09-22T23:07:45Z
- Finished UTC: 2026-09-22T23:09:58Z
- Verdict: needs curation

## Target

Generated DSMZ/MediaDive medium 430 record `CultureMech:001539`, named `ectothiorhodospira_abdelmalekii_medium`, merged with a KOMODO source duplicate for DSMZ 430 modified for DSM 13718.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation against `scripts/validate_strict.py`: passed with 0 error rows.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the focused history validator targets standalone files under `history/`, not inline `MediaRecipe.curation_history` entries.

## Identity and Grounding

The DSMZ 430 identity and pH 8.5 are present. KOMODO 430_13718 is represented as a source duplicate, but the related TOGO/JCM copy of Ectothiorhodospira Abdelmalekii Medium is still split into `data/merge_yaml/merged/ectothiorhodospira_abdelmalekii_medium__8f51b444.yaml`; `find`, which includes ignored files, found both generated siblings.

Most leaf salts and vitamins are grounded. `NiCl2 x 6 H2O` should be rechecked because its source label is a hexahydrate while the ChEBI label is the anhydrous salt.

## Evidence

The DSMZ Medium 430 PDF defines a 1000 ml final medium with 0.80 g KH2PO4, 0.80 g NH4Cl, 0.05 g CaCl2 x 2 H2O, 0.10 g MgCl2 x 6 H2O, 120 g NaCl, 15 g Na2SO4, 1 g sodium acetate, 5 g Na2CO3 adjusted if required, 1 ml SLA trace-element solution, 10 g NaHCO3, 1 ml VA vitamin solution, and 5 ml 10% neutralized sulfide solution.

SLA is a separate 1 litre stock, VA is a separate 100 ml stock, and the sulfide solution is a separate 100 ml stock. MediaDive encodes those three stock volumes explicitly as solution amounts of 1 ml, 1 ml, and 5 ml in the final 1000 ml medium.

## Completeness

The top-level DSMZ salts are mostly complete and correctly scaled. The record loses the stock-solution boundaries: all SLA components, all VA components, and Na2S x 9 H2O from the 10% neutralized sulfide solution are rendered as direct final-medium ingredients at stock concentration. The final 1000 ml water basis is absent, which is acceptable only if every stock and added component is otherwise modeled explicitly.

The preparation sequence also flattens stock procedures into the final recipe. The SLA pH 2.0 to 3.0 adjustment and neutralized-sulfide anaerobic autoclave procedure appear as generic final-medium steps rather than as instructions for their respective stock solutions.

## Findings

- SLA trace elements are 1000-fold too concentrated in the final ingredient list: the final medium receives 1 ml SLA per litre, but the YAML records the full SLA stock g/L values.
- VA vitamins are 1000-fold too concentrated: the final medium receives 1 ml VA stock per litre, but the YAML records the VA stock values such as `Biotin 0.1 G_PER_L`.
- Neutralized sulfide is 200-fold too concentrated: the final medium receives 5 ml of a 100 g/L Na2S x 9 H2O stock per litre, while the YAML records `Na2S x 9 H2O 100 G_PER_L`.
- Stock-level pH adjustments and the neutralized-sulfide preparation procedure are flattened into the final preparation-step list.
- The JCM/TOGO copy of the same named medium remains a separate generated record with a different fingerprint, so source-equivalent variants have not been reconciled.
- Ectothiorhodospira abdelmalekii is present only in the medium name, not as structured target-organism metadata.

## Recommended Edits

- Preserve DSMZ 430 as nested Main, SLA, VA, and 10% neutralized sulfide solutions, or calculate final stock contributions through 1 ml/L and 5 ml/L addition rates.
- Keep the top-level DSMZ salts and pH 8.5 from the current record.
- Move the SLA pH and sulfide-bottle instructions onto their own stock recipes instead of treating them as final-medium steps.
- Recheck the nickel chloride hexahydrate grounding.
- Reconcile the DSMZ/KOMODO record with the TOGO/JCM Ectothiorhodospira Abdelmalekii record and preserve all stable source IDs on the canonical recipe.
- Add Ectothiorhodospira abdelmalekii or DSM 13718 as target metadata if supported by the source duplicate.

## Follow-up Checks

- Re-run open, strict, reference, and term validators after rebuilding.
- Compare the rebuilt record against the DSMZ Medium 430 PDF and MediaDive solution IDs 877, 690, 691, and 6471.
- Search with ignored files included for stale stock-strength values such as `Biotin 0.1 G_PER_L` and `Na2S x 9 H2O 100 G_PER_L` after regeneration.

## Additional Notes

The generated record has no explicit organism growth data to review.

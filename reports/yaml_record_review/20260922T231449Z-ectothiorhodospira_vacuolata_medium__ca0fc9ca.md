# YAML Record Review: ectothiorhodospira_vacuolata_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ectothiorhodospira_vacuolata_medium__ca0fc9ca.yaml
- Started UTC: 2026-09-22T23:12:18Z
- Finished UTC: 2026-09-22T23:14:49Z
- Verdict: needs curation

## Target

Generated DSMZ/MediaDive medium 431 record `CultureMech:001540`, named `ectothiorhodospira_vacuolata_medium`.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation against `scripts/validate_strict.py`: passed with 0 error rows.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the focused history validator targets standalone files under `history/`, not inline `MediaRecipe.curation_history` entries.

## Identity and Grounding

The DSMZ Medium 431 identity, title, pH 8.7, and source PDF URL are present. The target organism is only encoded in the recipe name and should be made structured target-organism metadata.

Most salts and vitamins are grounded. `NiCl2 x 6 H2O` should be rechecked because the source specifies a hexahydrate while the ChEBI label on `CHEBI:34887` is anhydrous nickel dichloride.

## Evidence

The DSMZ Medium 431 PDF lists a 1000 ml final medium containing 1.00 g KH2PO4, 0.50 g NH4Cl, 0.20 g MgCl2 x 6 H2O, 0.10 g CaCl2 x 2 H2O, 3.00 g NaHCO3, 30.00 g NaCl, 1 ml trace element solution SLA, 1 ml vitamin solution VA, 0.05 g Na2S x 9 H2O, 0.50 g Na2S2O3 x 5 H2O, 1.00 g Na-malate, and 1000 ml distilled water.

MediaDive DSMZ 431 encodes the same two stock additions as `Vitamin solution (VA)` solution 691 at 1 ml and `Trace element solution (SLA)` solution 690 at 1 ml in final solution 878.

## Completeness

The main salts, thiosulfate, malate, pH, and filter-sterilization instruction are present. The VA and SLA stock boundaries are lost: the seven vitamin rows and nine trace-element rows are rendered as direct final-medium ingredients at stock concentration rather than as 1 ml/L stock additions or as 1000-fold diluted final concentrations.

The SLA stock pH instruction is also flattened into the final preparation steps as a second pH adjustment to 2.0 to 3.0, which would be wrong for the pH 8.7 final medium.

## Findings

- VA vitamins are 1000-fold too concentrated because the final medium receives 1 ml VA per litre, but the record stores the VA stock g/L values directly.
- SLA trace elements are 1000-fold too concentrated for the same reason.
- The `Adjust pH to 2.0 - 3.0` step belongs to the SLA stock, not the final Ectothiorhodospira vacuolata medium.
- The 1000 ml distilled-water basis is omitted instead of being retained as final volume metadata.
- `NiCl2 x 6 H2O` is probably grounded to an anhydrous nickel chloride term.
- Ectothiorhodospira vacuolata is missing as structured target-organism metadata.

## Recommended Edits

- Preserve DSMZ 431 as nested Main, VA, and SLA solutions, or calculate final vitamin and trace-element contributions through the 1 ml/L stock dosages.
- Keep the final pH 8.7, direct main-ingredient masses, 0.05 g/L Na2S x 9 H2O, 0.50 g/L Na2S2O3 x 5 H2O, and 1.00 g/L Na-malate from the DSMZ source.
- Move the pH 2.0 to 3.0 adjustment onto the SLA stock recipe only.
- Recheck the nickel chloride hexahydrate grounding.
- Add Ectothiorhodospira vacuolata as target metadata if supported by DSMZ/JCM provenance.

## Follow-up Checks

- Re-run open, strict, reference, and term validators after rebuilding.
- Compare the rebuilt record against the DSMZ Medium 431 PDF and MediaDive solution IDs 878, 691, and 690.
- Search with ignored files included for stale DSMZ 431 stock-strength rows such as `Biotin 0.1 G_PER_L`, `FeCl2 x 4 H2O 1.8 G_PER_L`, and final-medium `Adjust pH to 2.0 - 3.0` after regeneration.

## Additional Notes

The generated record has no explicit organism growth data to review.

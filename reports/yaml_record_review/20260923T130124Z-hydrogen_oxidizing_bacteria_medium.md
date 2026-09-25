# YAML Record Review: Hydrogen-oxidizing bacteria medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/hydrogen_oxidizing_bacteria_medium.yaml
- Started UTC: 2026-09-23T12:59:57Z
- Finished UTC: 2026-09-23T13:01:24Z
- Verdict: needs curation

## Target

Reviewed the generated TOGO/NBRC branch for TOGO Medium M1727 and NBRC Medium 936, `Hydrogen-oxidizing bacteria medium`, at `data/merge_yaml/merged/hydrogen_oxidizing_bacteria_medium.yaml`. The maintained source is `data/normalized_yaml/bacterial/hydrogen_oxidizing_bacteria_medium.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hydrogen_oxidizing_bacteria_medium.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record's TOGO M1727 and NBRC 936 source links identify the intended NBRC hydrogen-oxidizing bacteria medium. The generated artifact is stale relative to a September 2026 duplicate-water repair in the maintained source, but the normalized source still preserves the older flattened stock and gas-atmosphere model.

## Evidence

NBRC 936 and TOGO M1727 list a final medium with 10 ml KP buffer, 0.75 g MgCl2 x 6 H2O, 0.15 g CaCl2 x 2 H2O, 0.54 g NH4Cl, 1.6 g Na2S2O3, 2 ml Trace elements solution, 2 ml Vitamin solution, 0.5 g Na2CO3, and 1 L distilled water. The source then separately defines KP buffer, Trace elements solution, and Vitamin solution stock recipes. It instructs mixing ingredients except KP buffer and vitamin solution, dispensing under an H2/CO2/O2 75/20/5 gas stream, sealing with butyl rubber stoppers, autoclaving KP buffer separately under N2, filter-sterilizing the vitamin solution, adding KP buffer and vitamin solution aseptically before inoculation, and pressurizing inoculated vessels to 150 kPa with H2/CO2/O2.

The generated record flattens all three stock recipes into top-level ingredients. It converts the 10 ml, 2 ml, and 2 ml stock additions into empty `G_PER_L` solutions; promotes the gas atmospheres and NaOH pH adjustment into variable ingredients; sums the final-medium 0.15 g CaCl2 x 2 H2O with the Trace elements solution 0.1 g CaCl2 x 2 H2O; and sums four separate 1 L water rows into a 4 `G_PER_L` water row.

## Completeness

The direct final-medium MgCl2 x 6 H2O, NH4Cl, Na2CO3, and Na2S2O3 amounts are present. The record is not complete enough to follow because KP buffer, Trace elements solution, and Vitamin solution are not usable as stocks, the gas and sterilization steps are missing, and the stock-strength vitamin and trace components are presented as if they were final-medium concentrations.

No `target_organisms`, growth metrics, or strain-specific growth evidence are asserted, so there are no over-scoped organism claims to review.

## Findings

- **major**: KP buffer, Trace elements solution, and Vitamin solution are flattened into top-level stock-strength ingredients instead of being represented as 10 ml, 2 ml, and 2 ml additions.
- **major**: Distilled water rows from the final medium and three stocks were summed into `4.0 G_PER_L` in the generated artifact; the current normalized source has collapsed the duplicate value to `1.0 G_PER_L` but still keeps the wrong mass unit.
- **major**: Final-medium CaCl2 x 2 H2O was summed with Trace elements solution CaCl2 x 2 H2O across stock boundaries.
- **major**: Gas atmospheres and the Trace elements NaOH pH adjustment are represented as variable-concentration ingredients.
- **major**: Mixing, gas dispensing, separate KP-buffer autoclaving under N2, vitamin filter sterilization, aseptic stock addition, and 150 kPa H2/CO2/O2 pressurization instructions are absent.
- **major**: Several exact hydrates are misgrounded or overgeneralized after flattening, including Na2S2O3 as a pentahydrate and chloride trace salts whose source rows specify hexahydrates.

## Recommended Edits

- In `data/normalized_yaml/bacterial/hydrogen_oxidizing_bacteria_medium.yaml`, rebuild the record from NBRC 936 with KP buffer, Trace elements solution, and Vitamin solution as nested stock additions at 10, 2, and 2 ml per liter.
- Keep stock components inside their stock recipes and stop merging same-named compounds across final-medium and stock boundaries.
- Convert all 1 L distilled-water rows to volume units in the relevant final-medium or stock context.
- Move H2, CO2, O2, N2, and NaOH out of top-level ingredients into gas-atmosphere and preparation notes.
- Restore the NBRC mixing, sterilization, aseptic-addition, and pressurization instructions, then regenerate the merged artifact.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Re-open TOGO M1727 and the NBRC 936 page to confirm the regenerated record preserves the three stock boundaries, gas handling, water volumes, and 150 kPa final pressurization.
- Run the repository's merge freshness audit after regenerating the TOGO/NBRC branch.

## Additional Notes

None.

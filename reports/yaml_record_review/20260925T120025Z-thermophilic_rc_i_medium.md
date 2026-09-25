# YAML Record Review: thermophilic_rc_i_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermophilic_rc_i_medium.yaml
- Started UTC: 2026-09-25T12:00:25Z
- Finished UTC: 2026-09-25T12:00:25Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:008425`, `thermophilic_rc_i_medium`, generated from TOGO Medium M1850 and ultimately sourced from NBRC Medium 1086.

## Validation

- LinkML schema: Passed; the command exited 0 with no diagnostics.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermophilic_rc_i_medium.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The medium is grounded to TOGO M1850, "Thermophilic RC-I medium", with NBRC Medium 1086 as the original source. The fetched NBRC page confirmed the main solution, Trace elements solution, Vitamin solution, gas instructions, and pH 7.0 text represented in the TOGO payload.

## Evidence

- NBRC M1086 lists the main 1 L recipe with KH2PO4 0.2 g, NH4Cl 0.1 g, MgCl2 x 6 H2O 0.4 g, CaCl2 x 2 H2O 0.1 g, NaCl 1 g, KCl 0.5 g, NaHCO3 2.52 g, Bacto Yeast Extract (Difco) 0.1 g, sodium acetate 0.1 g, Trace elements solution 2 ml, Vitamin solution 10 ml, resazurin 0.5 mg, cysteine-HCl 0.3 g, Na2S x 9H2O 0.3 g, and distilled water 1 L.
- NBRC M1086 defines a separate Trace elements solution in 1 L distilled water and a separate Vitamin solution in 1 L distilled water.
- NBRC M1086 autoclaves the base under H2/CO2, separately autoclaves cysteine-HCl and Na2S x 9H2O as 6% solutions under N2, aseptically adds filter-sterile vitamin solution and the reducing solutions, pressurizes inoculated bottles to 150 kPa with H2/CO2, and states pH 7.0.

## Completeness

The record includes the named main-solution, trace, and vitamin chemicals, but it flattens both nested stocks into direct top-level rows. It also merges all three 1 L water rows into one `Distilled water` 3.0 G_PER_L row and stores the 2 ml and 10 ml stock additions as G_PER_L solution concentrations.

## Findings

- `Distilled water` 3.0 G_PER_L is a merge artifact from the main recipe water, Trace elements solution water, and Vitamin solution water.
- `CaCl2 x 2 H2O` 0.118 G_PER_L merges the 0.1 g main-medium row with the 0.018 g Trace elements solution row, crossing stock boundaries.
- Trace elements are flattened at 1 L stock strength even though the source adds only 2 ml/L of that stock.
- Vitamin entries copy milligram stock masses into G_PER_L rows, for example `Biotin` 2 G_PER_L and `Vitamin B12` 0.01 G_PER_L from 2 mg/L and 0.01 mg/L stock rows.
- `Resazurin` 0.5 G_PER_L copies a 0.5 mg/L source row as grams per liter.
- The `solutions` entries record 2 ml and 10 ml additions as 2 and 10 G_PER_L and call both stocks `Unknown solution`.

## Recommended Edits

- Rebuild the recipe with a main solution, Trace elements solution, and Vitamin solution, preserving 2 ml/L and 10 ml/L stock additions.
- Reverse the duplicate merges for distilled water and CaCl2 x 2 H2O so each row remains scoped to its source solution.
- Fix mg-to-G_PER_L conversions for resazurin and all Vitamin solution rows.
- Add preparation steps from NBRC M1086, including H2/CO2 autoclaving, 6% cysteine-HCl and Na2S x 9H2O reducing solutions under N2, filter-sterile vitamin addition, and 150 kPa H2/CO2 pressurization.

## Follow-up Checks

- Inspect `data/normalized_yaml/bacterial/NBRC_1091.yaml`, which the exact source search showed also references NBRC Medium 1086, before deduplicating NBRC-derived Thermophilic RC-I content.
- Check whether H2/CO2 pressure belongs in structured gas fields or in preparation text.

## Additional Notes

No target-organism evidence was reviewed. The narrowed exact source search included ignored and hidden files and found the current TOGO M1850 record, its normalized source, and NBRC_1091 references to the same NBRC Medium 1086.

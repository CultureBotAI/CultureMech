# YAML Record Review: ectothiorhodospira_abdelmalekii_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ectothiorhodospira_abdelmalekii_medium__8f51b444.yaml
- Started UTC: 2026-09-22T23:10:34Z
- Finished UTC: 2026-09-22T23:11:53Z
- Verdict: needs curation

## Target

Generated TOGO M3030 record `CultureMech:009542`, named `ectothiorhodospira_abdelmalekii_medium`, with JCM_M1387 as the original source.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation against `scripts/validate_strict.py`: passed with 0 error rows.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the focused history validator targets standalone files under `history/`, not inline `MediaRecipe.curation_history` entries.

## Identity and Grounding

The Togo M3030 and JCM 1387 identities are visible in `media_term` and `notes`. The record duplicates DSMZ/MediaDive Medium 430 in `data/merge_yaml/merged/ectothiorhodospira_abdelmalekii_medium__828e5ee6.yaml`, but the two imports diverged enough to avoid merging.

The simple salts are grounded correctly. N2 is grounded as dinitrogen, but it is not a final solute in JCM 1387; it is the anaerobic gas used while filling tubes.

## Evidence

JCM 1387 lists 0.80 g KH2PO4, 0.05 g CaCl2 x 2 H2O, 0.80 g NH4Cl, 0.10 g MgCl2 x 6 H2O, 120 g NaCl, 15 g Na2SO4, 10 g NaHCO3, 5 g Na2CO3, 1 ml trace element solution SLA, 0.50 g Na2S x 9 H2O, 1 g sodium acetate, and 1000 ml distilled water. It instructs the curator to adjust pH to 8.5, bubble with nitrogen, fill tubes under nitrogen, autoclave, and after sterilization add 1 ml/L filter-sterilized VA vitamin solution plus an appropriate amount of sterilized Na2S x 9 H2O solution.

The generated record instead contains `Distilled water 1100.0 G_PER_L`, `Na2S x 9 H2O 10.5 G_PER_L`, a variable N2 ingredient, and three empty `solutions` entries whose concentrations do not preserve millilitre stock doses.

## Completeness

The main mineral recipe is partially present, but all preparation instructions are absent. The SLA, VA, and sulfide stock references were migrated into empty `solutions` with default `Unknown solution` names. The 1 ml SLA and 1 ml/L VA additions are stored as `1 G_PER_L`, and the final 0.50 g Na2S x 9 H2O row has been summed with the 10 g stock recipe.

## Findings

- Distilled water was imported as `1100.0 G_PER_L` after summing 1000 ml final water with 100 ml water from the Na2S x 9 H2O stock recipe.
- Na2S x 9 H2O was inflated to `10.5 G_PER_L` after merging the direct 0.5 g final-medium addition with the 10 g/100 ml sulfide stock row.
- The required 1 ml trace-element stock and 1 ml/L VA stock are empty solutions with `G_PER_L` placeholder concentrations.
- N2 is modeled as a variable-concentration ingredient instead of a gas phase used during tube filling.
- All source preparation instructions are missing, including pH 8.5 adjustment, nitrogen bubbling, filling under nitrogen, autoclaving, and post-sterilization vitamin/sulfide addition.
- The equivalent DSMZ 430 import remains a separate generated record rather than a structured additional source for one canonical medium.

## Recommended Edits

- Preserve JCM 1387 stock references as millilitre additions rather than converting them to gram-per-litre placeholder solutions.
- Keep Na2S x 9 H2O final-medium and stock-solution rows separate.
- Store N2 as an anaerobic gas-phase preparation condition, not a soluble ingredient.
- Restore JCM's pH, nitrogen, autoclave, and post-sterilization stock-addition instructions.
- Reconcile the Togo/JCM and DSMZ/KOMODO imports and keep TOGO:M3030, JCM_M1387, and DSMZ 430 provenance on the canonical recipe when their differences have been normalized.

## Follow-up Checks

- Re-run open, strict, reference, and term validators after rebuilding.
- Compare the rebuilt record against JCM 1387, Togo M3030, and DSMZ Medium 430.
- Search with ignored files included for stale `1100.0`, `10.5`, `Unknown solution`, and variable `N2` artifacts after regeneration.

## Additional Notes

The generated record has no explicit organism growth data to review.

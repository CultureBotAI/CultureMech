# YAML Record Review: denitrovibrio_medium__bc5acd4f

- Repository: CultureMech
- Record: `data/merge_yaml/merged/denitrovibrio_medium__bc5acd4f.yaml`
- Started UTC: 2026-09-22T17:17:18Z
- Finished UTC: 2026-09-22T17:17:18Z
- Verdict: needs curation

## Target

Generated bacterial `denitrovibrio_medium` record for TOGO M2167, linked to NBRC Medium 1550.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to TOGO M2167 and keeps the NBRC Medium 1550 URL in `notes`. Live NBRC Medium 1550 matched the TOGO M2167 ingredient set, including Trace element solution SL-10*, Vitamin solution**, N2/CO2 preparation, and pH 6.8-7.2.

This is a different Denitrovibrio formula from DSMZ Medium 881: NBRC uses an FeCl3-containing trace stock with Na2SeO4 and Na2WO4 and adds 10 ml vitamin stock; DSMZ 881 uses an FeCl2 SL-10 stock, a separate selenite-tungstate solution, and 1 ml seven-vitamin stock. The fingerprint should therefore remain separate from the DSMZ/KOMODO 881 duplicate family.

The complex/undefined classification is not supported because NBRC Medium 1550 is a defined chemical medium.

## Evidence

The generated record flattened both inline NBRC stock formulas as final direct ingredients but also left empty `solutions` placeholders for `Trace element solution SL-10*` and `Vitamin solution**`.

Three source water rows were summed into one top-level row as `3.0 G_PER_L`, reflecting the 1 L main-solution water, 1 L Trace element solution water, and 1 L Vitamin solution water.

Milligram stock rows were imported as gram-per-liter final concentrations. Examples include 36 mg Na2MoO4 x 2 H2O as `36 G_PER_L`, 6 mg H3BO3 as `6 G_PER_L`, 100 mg MnCl2 x 4 H2O as `100 G_PER_L`, 4 mg Na2WO4 as `4 G_PER_L`, 2 mg Biotin as `2 G_PER_L`, 10 mg Pyridoxine-HCl as `10 G_PER_L`, and 0.1 mg Cyanocobalamin as `0.1 G_PER_L`.

The NBRC source lists 0.5 mg Resazurin in the main solution. The generated ingredient stores it as `0.5 G_PER_L`, a 1000-fold unit error.

The generated stock placeholders have `mediadive.solution:4178` and `mediadive.solution:6241` links. Those generic MediaDive solution records are not adequate grounding for the NBRC inline stock formulas: the NBRC trace stock uses 35% HCl, FeCl3 x 6H2O, Na2WO4, Na2SeO4, and NiCl2 x 2H2O, and the NBRC vitamin stock has 10 inline vitamin components.

The source preparation says to autoclave under an 80/20 N2/CO2 atmosphere, sterilize fumarate and sulfide under N2, add filter-sterile vitamin and carbonate solutions before inoculation, and adjust pH to 6.8-7.2. The generated record has no `preparation_steps`; `Carbon dioxide gas`, `Nitrogen gas`, and `NaOH` are represented as ingredients with variable concentrations.

## Completeness

NBRC provides complete formulas for the main medium, Trace element solution SL-10*, and Vitamin solution**, but the generated `solutions` entries have empty compositions and do not retain the stock-specific component boundaries.

The record also lacks the autoclaving, gas-atmosphere, filter-sterile addition, and final pH-adjustment instructions required to make the medium as published.

## Findings

- Needs curation: the record should be defined/defined, not complex/undefined.
- Needs curation: complete NBRC trace and vitamin stocks are flattened into top-level ingredients and replaced with empty solution placeholders.
- Needs curation: milligram stock quantities and 0.5 mg Resazurin are emitted as `G_PER_L`.
- Needs curation: stock-internal water is merged into top-level final-medium water.
- Needs curation: generic MediaDive stock links do not faithfully identify the NBRC-specific trace and vitamin formulas.
- Needs curation: N2, CO2, and NaOH pH adjustment are modeled as ingredients instead of preparation conditions.
- Needs curation: the hydrated cobalt and nickel chloride rows are grounded to anhydrous CHEBI terms and should be rechecked.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M2167_Denitrovibrio_Medium.yaml` from NBRC Medium 1550 before regenerating this merged record.
- Keep TOGO M2167 separate from the DSMZ Medium 881 Denitrovibrio family because the formulas are not source duplicates.
- Change `medium_type` and `composition_type` to `DEFINED`.
- Nest the NBRC Trace element solution SL-10* and Vitamin solution** formulas under `solutions` with 1 ml/L and 10 ml/L additions.
- Remove stock-internal trace metals, vitamins, HCl, stock water, N2, CO2, and NaOH from top-level `ingredients`.
- Correct the Resazurin and milligram stock quantities.
- Preserve the NBRC N2/CO2 autoclaving and pH 6.8-7.2 adjustment as preparation or condition data.
- Recheck hydrated cobalt and nickel chloride groundings.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after repair.
- Compare the regenerated stock compositions against the live NBRC 1550 table.
- Confirm `Trace element solution SL-10*` and `Vitamin solution**` are populated from the NBRC inline formulas rather than MediaDive stand-ins.
- Confirm no milligram stock quantity remains as a whole-number `G_PER_L` final ingredient.

## Additional Notes

TOGO M2167 and NBRC Medium 1550 were both reachable during review.

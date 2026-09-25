# YAML Record Review: Microaerobic sulfur-oxidizing bacteria medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/microaerobic_sulfur_oxidizing_bacteria_medium.yaml`
- Started UTC: 2026-09-24T06:16:10Z
- Finished UTC: 2026-09-24T06:16:10Z
- Verdict: needs curation

## Target

- Reviewed merged record `data/merge_yaml/merged/microaerobic_sulfur_oxidizing_bacteria_medium.yaml`.
- Editable normalized source: `data/normalized_yaml/bacterial/microaerobic_sulfur_oxidizing_bacteria_medium.yaml`.
- TOGO medium: `TOGO:M1729`, Microaerobic sulfur-oxidizing bacteria medium.
- Original source: NBRC medium 938.

## Validation

- LinkML open-schema validation: passed; `No issues found`.
- Strict validation: passed with 0 errors; `validate_strict.py` scanned 1 file and produced only the TSV header.
- Reference validation: passed; 1 file, 0 checks.
- Term validation: passed.
- Embedded history: Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The recipe identity is coherent: TOGO `M1729`, NBRC `NO=938`, and the generated YAML all name Microaerobic sulfur-oxidizing bacteria medium.
- `CoCl2 x 6H2O` and `NiCl2 x 6H2O` are grounded only to generic cobalt dichloride and nickel dichloride rather than exact hexahydrate terms.
- `Ca-pantothenate` is grounded to `(R)-pantothenate`, losing the source's calcium salt form.
- `Oxygen gas` remains ungrounded even though the source gas phase is specified.

## Evidence

- NBRC and TOGO list a 1 L main medium with 5 ml KP buffer, 2 ml trace elements solution, 2 ml vitamin solution, MgCl2 x 6H2O 3.05 g, CaCl2 x 2H2O 0.15 g, ammonium sulfate 0.66 g, NaCl 30 g, sodium thiosulfate pentahydrate 5 g, sodium nitrate 0.85 g, sodium bicarbonate 2.52 g, and water to 1 L.
- The KP buffer is a separate 1 L stock containing KH2PO4 119 g, K2HPO4 21 g, and water, and it is autoclaved under N2.
- The trace-elements solution is a separate 1 L stock containing NTA, FeCl3 x 6H2O, MnCl2 x 4H2O, CoCl2 x 6H2O, CaCl2 x 2H2O, ZnCl2, CuCl2 x 2H2O, H3BO3, Na2MoO4 x 2H2O, NaCl, NiCl2 x 6H2O, Na2SeO4, Na2WO4, and water.
- The trace-elements instructions say to dissolve NTA first, adjust to pH 6.5 with NaOH, then add other minerals, with final pH 7.0.
- The vitamin solution is a separate 1 L stock whose vitamin amounts are in milligrams, not grams.
- The final-medium instructions say to mix ingredients except KP buffer and vitamin solution, dispense under N2/CO2/O2 75/20/5, seal with butyl rubber stoppers, separately autoclave KP buffer under N2, filter-sterilize vitamin solution, add KP buffer and vitamin solution aseptically before inoculation, and pressurize inoculated vessels to 150 kPa with N2/CO2/O2 75/20/5.

## Completeness

- The three source stocks are absent as real nested solutions. `KP buffer*`, `Trace elements solution**`, and `Vitamin solution***` survive only as empty `Unknown solution` placeholders with gram-per-liter concentrations.
- All stock ingredients have been promoted to final-medium ingredients at stock concentrations.
- Final-medium and stock-preparation instructions are absent from the YAML.
- The generated water row is stale: it still publishes `4.0` g/L water from four merged 1 L stock waters even though the editable source has a September repair collapsing this to one 1 L placeholder.

## Findings

- The final additions `5 ml KP buffer`, `2 ml Trace elements solution`, and `2 ml Vitamin solution` were transformed into empty 5, 2, and 2 g/L solution placeholders.
- KP buffer ingredients are listed as final ingredients at 119 g/L KH2PO4 and 21 g/L K2HPO4 instead of nested under a 5 ml/L stock addition.
- Trace-elements ingredients are listed as final ingredients at full stock strength. The duplicate NaCl and CaCl2 x 2H2O rows from that stock were summed into the final NaCl and CaCl2 rows, yielding 31 g/L NaCl and 0.25 g/L CaCl2 x 2H2O instead of preserving 30 g/L and 0.15 g/L in the main medium plus nested stock contents.
- Vitamin-stock rows were imported as grams per liter although the source amounts are milligrams per liter; because the stock itself is only used at 2 ml/L, the published vitamin concentrations are inflated by a much larger factor.
- `N2` from the KP buffer stock is promoted to a final-medium gas row, duplicating the final `Nitrogen gas` row.
- The main anaerobic workflow, KP-buffer N2 autoclaving, vitamin filtration, and trace-elements NTA/pH instructions are missing.
- The generated merge is stale relative to the normalized source for the repaired water row, but the normalized source still carries the main stock-flattening defects.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/microaerobic_sulfur_oxidizing_bacteria_medium.yaml`.
- Rebuild KP buffer, Trace elements solution, and Vitamin solution as nested solutions added to the final medium by volume.
- Move KH2PO4 and K2HPO4 into KP buffer.
- Move NTA, Fe, Mn, Co, Ca, Zn, Cu, B, Mo, NaCl, Ni, Se, W, and NaOH into the trace-elements solution.
- Move all vitamin rows into the vitamin stock and preserve their `mg` source units or the correct converted g/L stock concentrations.
- Restore preparation notes for pH unadjusted main medium, N2/CO2/O2 75/20/5 dispensing and 150 kPa pressurization, KP buffer sterilization under N2, vitamin filtration, and trace-elements pH adjustment.
- Correct generic or salt-form groundings for CoCl2 x 6H2O, NiCl2 x 6H2O, Ca-pantothenate, and Oxygen gas where exact terms are available.
- Regenerate `data/merge_yaml/merged/microaerobic_sulfur_oxidizing_bacteria_medium.yaml` after the normalized source is fixed.

## Follow-up Checks

- Re-run focused open-schema, strict, reference, and term validators for `data/merge_yaml/merged/microaerobic_sulfur_oxidizing_bacteria_medium.yaml`.
- Verify the final medium keeps NBRC's 5 ml, 2 ml, and 2 ml stock additions instead of 5, 2, and 2 g/L solution placeholders.
- Verify final NaCl is 30 g/L and final CaCl2 x 2H2O is 0.15 g/L, with the additional NaCl and CaCl2 x 2H2O rows scoped only to the trace-elements stock.
- Verify vitamin-stock quantities are milligram-scale and are not listed as final gram-per-liter additions.
- Verify the source gas phase N2/CO2/O2 75/20/5 and 150 kPa pressurization are represented.

## Additional Notes

- Empty optional fields were not treated as defects.

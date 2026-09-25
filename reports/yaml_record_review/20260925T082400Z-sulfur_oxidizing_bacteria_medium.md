# YAML Record Review: Sulfur-oxidizing Bacteria Medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfur_oxidizing_bacteria_medium.yaml` (`CultureMech:008255`)
- Started UTC: `2026-09-25T08:24:00Z`
- Finished UTC: `2026-09-25T08:24:00Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfur_oxidizing_bacteria_medium.yaml` |
| Normalized source | `data/normalized_yaml/bacterial/TOGO_M1695_Sulfur-oxidizing_bacteria_Medium.yaml` |
| CultureMech ID | `CultureMech:008255` |
| Media term | `TOGO:M1695` |
| Original source | TOGO Medium M1695, NBRC Medium 901, Sulfur-oxidizing bacteria Medium |
| Merge fingerprint | `352b542798edbc0dcac5dbb3e76d8e8f4f6830a61fd466ba3f86af0b64ca0996` |
| Merged from | `TOGO_M1695_Sulfur-oxidizing_bacteria_Medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected `CultureMech:008255` identifier, `TOGO:M1695` source term, NBRC 901 provenance, and merge fingerprint. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:008255`, `TOGO:M1695`, `TOGO_M1695_Sulfur-oxidizing_bacteria_Medium.yaml`, and the merge fingerprint found the M1695 normalized source and this generated merge as the only direct recipe records, with the expected normalized indexes also referencing the same ID and source term.

Several main-solution salts are plausibly grounded, and Bacto Yeast Extract is correctly left ungrounded. The stock hierarchy is not grounded: KP buffer, Trace element solution, and Vitamin solution remain listed as separate `solutions` while their internal stock ingredients were also flattened into top-level final-medium ingredients at stock concentrations. `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` are grounded to generic cobalt dichloride and nickel dichloride terms, respectively, despite hydrate-specific source strings.

## Evidence

NBRC 901 and TOGO M1695 list the completed main solution as 10 ml KP buffer, 0.75 g MgCl2 x 6 H2O, 0.15 g CaCl2 x 2 H2O, 0.54 g NH4Cl, 3.2 g Na2S2O3, 0.1 g Bacto Yeast Extract, 2 ml Trace element solution, 2 ml Vitamin solution, 0.5 g Na2CO3, and 1 L distilled water.

The source preparation says to mix ingredients except KP buffer and vitamin solution, dispense under N2/CO2/O2 at 75/20/5, separately autoclave KP buffer under N2, filter-sterilize the vitamin solution, aseptically add KP buffer and vitamin solution before inoculation, and pressurize inoculated vessels to 150 kPa with N2/CO2/O2.

NBRC 901 defines KP buffer as 119 g KH2PO4 plus 21 g K2HPO4 per 1 L stock; Trace elements solution as NTA, FeCl3 x 6 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnCl2, CuCl2 x 2 H2O, H3BO3, Na2MoO4 x 2 H2O, NaCl, NiCl2 x 6 H2O, Na2SeO4, Na2WO4, and KAl(SO4)2 x 12 H2O per 1 L stock; and Vitamin solution as milligram-scale biotin, folic acid, pyridoxine-HCl, thiamine-HCl, riboflavin, nicotinic acid, Ca-pantothenate, p-aminobenzoic acid, and Vitamin B12 per 1 L stock.

The generated YAML stores KP buffer as `10 G_PER_L`, Trace element solution as `2 G_PER_L`, Vitamin solution as `2 G_PER_L`, flattens all stock ingredients as top-level `G_PER_L` rows, and carries the gas names as variable top-level ingredients. Merge generation then summed four scoped distilled-water rows to `4.0 G_PER_L`, even though the normalized M1695 source had already repaired the duplicate-water value to `1.0`.

## Completeness

The generated record is incomplete because it lacks the source's preparation steps, stock-scope preparation notes, 150 kPa gas-pressurization instruction, and distinct 1 L water scopes. It is also over-complete as a final-medium representation because KP-buffer, trace-element, and vitamin stock internals are duplicated at top level instead of scoped to the 10 ml/L and 2 ml/L stock additions.

`target_organisms` is absent. The TOGO and NBRC recipe metadata reviewed here do not assert growth observations, so no growth target was inferred.

## Findings

- KP buffer, Trace element solution, and Vitamin solution are represented with `G_PER_L` concentrations instead of the source's 10 ml/L, 2 ml/L, and 2 ml/L additions.
- KP-buffer ingredients are flattened into the final medium at 119 g/L KH2PO4 and 21 g/L K2HPO4 stock strength.
- Trace-element ingredients are flattened into the final medium at per-liter stock strength rather than the final 2 ml/L dilution.
- Vitamin ingredients are flattened into the final medium with milligram source amounts imported as grams per liter, then are not scoped to the final 2 ml/L vitamin-stock dilution.
- The final 0.15 g/L CaCl2 x 2 H2O row and the trace-stock 0.1 g/L CaCl2 x 2 H2O row are merged into a single 0.25 g/L final ingredient.
- Distinct main, KP-buffer, trace-element, and vitamin water rows are merged into one `4.0 G_PER_L` distilled-water row in the generated merge.
- The source preparation steps are missing.
- N2, CO2, and O2 gas handling was imported as variable top-level ingredients instead of the source N2/CO2/O2 atmosphere and pressurization instructions.
- `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` lost hydrate-specific grounding.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M1695_Sulfur-oxidizing_bacteria_Medium.yaml` or the TOGO nested-stock import, then regenerate `data/merge_yaml/merged/sulfur_oxidizing_bacteria_medium.yaml`.
- Keep KP buffer, Trace element solution, and Vitamin solution as nested 1 L stocks added to the final medium at 10 ml/L, 2 ml/L, and 2 ml/L.
- Preserve source-scoped water rows and CaCl2 x 2 H2O rows instead of summing them across final and stock scopes.
- Convert the source gas mixture into preparation instructions or atmosphere metadata instead of variable final ingredients.
- Add the source preparation text for separate KP-buffer autoclaving, vitamin filtration, and 150 kPa pressurization.
- Correct hydrate-specific groundings for CoCl2 x 6 H2O and NiCl2 x 6 H2O if exact terms are available.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:008255`, `TOGO:M1695`, `352b542798edbc0dcac5dbb3e76d8e8f4f6830a61fd466ba3f86af0b64ca0996`, and `TOGO_M1695_Sulfur-oxidizing_bacteria_Medium.yaml`.
- Recompare the regenerated M1695 recipe against both TOGO and NBRC to make sure the three nested stock recipes are scoped under the correct main-solution additions.
- Confirm M1695 remains separate from the sibling M1683 Sulfur-oxidizing bacteria medium record.

## Additional Notes

Empty optional fields that are unrelated to source identity, stock hierarchy, and source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the TOGO import, normalized M1695 source, and merge generation for nested stocks.

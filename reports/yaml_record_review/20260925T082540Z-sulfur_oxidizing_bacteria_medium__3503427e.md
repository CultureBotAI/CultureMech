# YAML Record Review: Sulfur-oxidizing Bacteria Medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfur_oxidizing_bacteria_medium__3503427e.yaml` (`CultureMech:008242`)
- Started UTC: `2026-09-25T08:25:40Z`
- Finished UTC: `2026-09-25T08:25:40Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfur_oxidizing_bacteria_medium__3503427e.yaml` |
| Normalized source | `data/normalized_yaml/bacterial/sulfur_oxidizing_bacteria_medium.yaml` |
| CultureMech ID | `CultureMech:008242` |
| Media term | `TOGO:M1683` |
| Original source | TOGO Medium M1683, NBRC Medium 888, Sulfur-oxidizing bacteria medium |
| Merge fingerprint | `3503427ecf788884252bc07b427ecc0440c3438dff7e387911b23c2e2c55174a` |
| Merged from | `sulfur_oxidizing_bacteria_medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected `CultureMech:008242` identifier, `TOGO:M1683` source term, NBRC 888 provenance, and merge fingerprint. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:008242`, `TOGO:M1683`, the merge fingerprint, and `source: sulfur_oxidizing_bacteria_medium.yaml` found the normalized M1683 source and this generated merge as the only direct recipe records, with the expected normalized indexes also referencing the same ID and source term.

Several main-solution salts are plausibly grounded, but the stock hierarchy is not grounded. KP buffer, Trace elements solution, and Vitamin solution remain listed as separate `solutions` while their internal stock ingredients were also flattened into top-level final-medium ingredients at stock concentrations. `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` are grounded to generic cobalt dichloride and nickel dichloride terms, respectively, despite hydrate-specific source strings.

## Evidence

NBRC 888 and TOGO M1683 list the completed main solution as 5 ml KP buffer, 3.05 g MgCl2 x 6 H2O, 0.15 g CaCl2 x 2 H2O, 0.66 g ammonium sulfate, 30 g NaCl, 5 g Na2S2O3 x 5 H2O, 2 ml Trace elements solution, 2 ml Vitamin solution, 2.52 g NaHCO3, and 1 L distilled water, with the pH unadjusted.

The source preparation says to mix ingredients except KP buffer and vitamin solution, dispense under N2/CO2/O2 at 60/20/20, separately autoclave KP buffer under N2, filter-sterilize the vitamin solution, aseptically add KP buffer and vitamin solution before inoculation, and pressurize inoculated vessels to 150 kPa with the same N2/CO2/O2 mixture.

NBRC 888 defines KP buffer as 119 g KH2PO4 plus 21 g K2HPO4 per 1 L stock; Trace elements solution as NTA, FeCl3 x 6 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnCl2, CuCl2 x 2 H2O, H3BO3, Na2MoO4 x 2 H2O, NaCl, NiCl2 x 6 H2O, Na2SeO4, and Na2WO4 per 1 L stock; and Vitamin solution as milligram-scale biotin, folic acid, pyridoxine-HCl, thiamine-HCl, riboflavin, nicotinic acid, Ca-pantothenate, p-aminobenzoic acid, and Vitamin B12 per 1 L stock.

The generated YAML stores KP buffer as `5 G_PER_L`, Trace elements solution as `2 G_PER_L`, Vitamin solution as `2 G_PER_L`, flattens all stock ingredients as top-level `G_PER_L` rows, and carries the gas names as variable top-level ingredients. Merge generation then summed four scoped distilled-water rows to `4.0 G_PER_L`, even though the normalized M1683 source had already repaired the duplicate-water value to `1.0`.

## Completeness

The generated record is incomplete because it lacks the source's preparation steps, pH-unadjusted note, stock-scope preparation notes, 150 kPa gas-pressurization instruction, and distinct 1 L water scopes. It is also over-complete as a final-medium representation because KP-buffer, trace-element, and vitamin stock internals are duplicated at top level instead of scoped to the 5 ml/L and 2 ml/L stock additions.

`target_organisms` is absent. The TOGO and NBRC recipe metadata reviewed here do not assert growth observations, so no growth target was inferred.

## Findings

- KP buffer, Trace elements solution, and Vitamin solution are represented with `G_PER_L` concentrations instead of the source's 5 ml/L, 2 ml/L, and 2 ml/L additions.
- KP-buffer ingredients are flattened into the final medium at 119 g/L KH2PO4 and 21 g/L K2HPO4 stock strength.
- Trace-element ingredients are flattened into the final medium at per-liter stock strength rather than the final 2 ml/L dilution.
- Vitamin ingredients are flattened into the final medium with milligram source amounts imported as grams per liter, then are not scoped to the final 2 ml/L vitamin-stock dilution.
- The final 30 g/L NaCl row and the trace-stock 1 g/L NaCl row are merged into a single 31 g/L final ingredient.
- The final 0.15 g/L CaCl2 x 2 H2O row and the trace-stock 0.1 g/L CaCl2 x 2 H2O row are merged into a single 0.25 g/L final ingredient.
- Distinct main, KP-buffer, trace-element, and vitamin water rows are merged into one `4.0 G_PER_L` distilled-water row in the generated merge.
- The source preparation steps and pH-unadjusted note are missing.
- N2, CO2, and O2 gas handling was imported as variable top-level ingredients instead of the source N2/CO2/O2 atmosphere and pressurization instructions.
- `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` lost hydrate-specific grounding.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/sulfur_oxidizing_bacteria_medium.yaml` or the TOGO nested-stock import, then regenerate `data/merge_yaml/merged/sulfur_oxidizing_bacteria_medium__3503427e.yaml`.
- Keep KP buffer, Trace elements solution, and Vitamin solution as nested 1 L stocks added to the final medium at 5 ml/L, 2 ml/L, and 2 ml/L.
- Preserve source-scoped water, NaCl, and CaCl2 x 2 H2O rows instead of summing them across final and stock scopes.
- Convert the source gas mixture into preparation instructions or atmosphere metadata instead of variable final ingredients.
- Add the source preparation text for separate KP-buffer autoclaving, vitamin filtration, and 150 kPa pressurization.
- Correct hydrate-specific groundings for CoCl2 x 6 H2O and NiCl2 x 6 H2O if exact terms are available.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:008242`, `TOGO:M1683`, `3503427ecf788884252bc07b427ecc0440c3438dff7e387911b23c2e2c55174a`, and `source: sulfur_oxidizing_bacteria_medium.yaml`.
- Recompare the regenerated M1683 recipe against both TOGO and NBRC to make sure the three nested stock recipes are scoped under the correct main-solution additions.
- Confirm M1683 remains separate from the sibling M1695 Sulfur-oxidizing bacteria Medium record.

## Additional Notes

Empty optional fields that are unrelated to source identity, stock hierarchy, and source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the TOGO import, normalized M1683 source, and merge generation for nested stocks.

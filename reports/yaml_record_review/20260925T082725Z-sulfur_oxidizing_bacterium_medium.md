# YAML Record Review: Sulfur-oxidizing Bacterium Medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfur_oxidizing_bacterium_medium.yaml` (`CultureMech:008706`)
- Started UTC: `2026-09-25T08:27:25Z`
- Finished UTC: `2026-09-25T08:27:25Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfur_oxidizing_bacterium_medium.yaml` |
| Normalized source | `data/normalized_yaml/bacterial/sulfur_oxidizing_bacterium_medium.yaml` |
| CultureMech ID | `CultureMech:008706` |
| Media term | `TOGO:M2113` |
| Original source | TOGO Medium M2113, NBRC Medium 1437, Sulfur-oxidizing bacterium medium |
| Merge fingerprint | `edc4b40df685857e9944c74bfb2df9854c1cf3186e6061c6e01528eabed8ef0a` |
| Merged from | `sulfur_oxidizing_bacterium_medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` exited 0 with no diagnostics for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected `CultureMech:008706` identifier, `TOGO:M2113` source term, NBRC 1437 provenance, and merge fingerprint. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:008706`, `TOGO:M2113`, the merge fingerprint, and `sulfur_oxidizing_bacterium_medium.yaml` found this normalized source and generated merge as the only direct recipe records, with the expected normalized indexes also referencing the same ID and source term.

Several main-solution salts are plausibly grounded, but all five stock additions from NBRC 1437 were flattened into top-level ingredients at stock strength. `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` are grounded to generic cobalt dichloride and nickel dichloride terms, respectively, despite hydrate-specific source strings.

## Evidence

NBRC 1437 and TOGO M2113 list the completed main solution as 0.5 g MgSO4 x 7 H2O, 0.1 g CaCl2 x 2 H2O, 0.1 g NH4Cl, 0.1 g KH2PO4, 0.1 g KCl, 0.85 g NaNO3, 0.16 g sodium acetate, 1 ml Trace element mixture, 1 ml Selenite-tungstate solution, 30 ml Bicarbonate solution, 1 ml Vitamin solution, 20 ml Thiosulfate solution, and 930 ml distilled water at pH 7.0-7.2.

The source preparation says to mix all ingredients except the bicarbonate, vitamin, and thiosulfate solutions, dispense under N2/CO2 at 80/20, seal with butyl rubber stoppers, autoclave at 121C for 20 min, and then aseptically and anaerobically add the omitted solutions with sterile syringes.

NBRC 1437 defines a Trace element mixture containing 12.5 ml 25% HCl, milligram-scale FeSO4 x 7 H2O, H3BO3, MnCl2 x 4 H2O, CoCl2 x 6 H2O, NiCl2 x 6 H2O, CuCl2 x 2 H2O, ZnSO4 x 7 H2O, and Na2MoO4 x 2 H2O in 987 ml water; a 1 L Selenite-tungstate solution with 0.4 g NaOH plus 6 mg Na2SeO3 x 5 H2O and 8 mg Na2WO4 x 2 H2O; a 100 ml 1.0 M Bicarbonate solution with 8.4 g NaHCO3; a 100 ml vitamin solution in sodium phosphate buffer; and a 100 ml 1.0 M Thiosulfate solution with 24.8 g Na2S2O3 x 5 H2O.

The generated YAML stores Trace element mixture, Selenite-tungstate solution, Bicarbonate solution, Vitamin solution, and Thiosulfate solution as `G_PER_L` additions, flattens their ingredients as top-level final-medium rows, converts stock milligrams and milliliters directly to `G_PER_L` values, and carries source gases as variable top-level ingredients. It also sums the main-solution 930 ml water row plus the 987 ml, 1 L, 100 ml, and 100 ml stock-water rows into one `2118.0 G_PER_L` distilled-water row.

## Completeness

The generated record is incomplete because it lacks the source's preparation steps, final pH 7.0-7.2 value, stock-scope preparation notes, and distinct water scopes. It is also over-complete as a final-medium representation because trace-element, selenite-tungstate, bicarbonate, vitamin, and thiosulfate stock internals are duplicated at top level instead of scoped to the 1 ml, 1 ml, 30 ml, 1 ml, and 20 ml stock additions.

`target_organisms` is absent. The TOGO and NBRC recipe metadata reviewed here do not assert growth observations, so no growth target was inferred.

## Findings

- Trace element mixture, Selenite-tungstate solution, Bicarbonate solution, Vitamin solution, and Thiosulfate solution are represented with `G_PER_L` concentrations instead of the source's 1 ml/L, 1 ml/L, 30 ml/L, 1 ml/L, and 20 ml/L additions.
- Trace-element ingredients are flattened into the final medium at stock amount values; milligram-scale values such as 2100 mg FeSO4 x 7 H2O are represented as 2100 g/L.
- The 12.5 ml HCl trace-mixture addition is represented as 12.5 g/L.
- Selenite-tungstate, vitamin, and thiosulfate stock ingredients are flattened into top-level final-medium rows instead of nested under their stocks.
- Sodium phosphate buffer from the 100 ml vitamin stock is represented as a 100 g/L final-medium ingredient.
- The distinct main, trace-mixture, selenite-tungstate, bicarbonate, and thiosulfate water rows are merged into one `2118.0 G_PER_L` distilled-water row.
- The source preparation steps and final pH 7.0-7.2 are missing.
- N2 and CO2 gas handling was imported as variable top-level ingredients instead of the source N2/CO2 atmosphere and bicarbonate stock instructions.
- `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` lost hydrate-specific grounding.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/sulfur_oxidizing_bacterium_medium.yaml` or the TOGO nested-stock import, then regenerate `data/merge_yaml/merged/sulfur_oxidizing_bacterium_medium.yaml`.
- Keep all five stock recipes nested and attach them to the final medium at the source 1 ml/L, 1 ml/L, 30 ml/L, 1 ml/L, and 20 ml/L additions.
- Preserve stock-specific water rows and milligram units instead of converting them to final `G_PER_L` rows.
- Convert the source gas mixture into preparation instructions or atmosphere metadata instead of variable final ingredients.
- Add final pH 7.0-7.2 plus the source preparation text for the main solution, CO2-saturated bicarbonate stock, filter-sterilized vitamin stock, and N2-stored thiosulfate stock.
- Correct hydrate-specific groundings for CoCl2 x 6 H2O and NiCl2 x 6 H2O if exact terms are available.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:008706`, `TOGO:M2113`, `edc4b40df685857e9944c74bfb2df9854c1cf3186e6061c6e01528eabed8ef0a`, and `sulfur_oxidizing_bacterium_medium.yaml`.
- Recompare the regenerated M2113 recipe against both TOGO and NBRC to make sure all five nested stock recipes are scoped under the correct main-solution additions.

## Additional Notes

Empty optional fields that are unrelated to source identity, stock hierarchy, and source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the TOGO import, normalized M2113 source, and merge generation for nested stocks.

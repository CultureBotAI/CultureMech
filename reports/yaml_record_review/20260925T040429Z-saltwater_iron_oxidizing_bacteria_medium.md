# YAML Record Review: saltwater_iron_oxidizing_bacteria_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/saltwater_iron_oxidizing_bacteria_medium.yaml
- Started UTC: 2026-09-25T04:04:29Z
- Finished UTC: 2026-09-25T04:04:29Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:010043`, `saltwater_iron_oxidizing_bacteria_medium`, from `data/merge_yaml/merged/saltwater_iron_oxidizing_bacteria_medium.yaml`.

The record is a single-source TOGO M642 import with JCM_M629 listed as TOGO's original source.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to TOGO M642 and the live JCM 629 page for `SALTWATER IRON-OXIDIZING BACTERIA MEDIUM`.

JCM 629 derives from JCM 628 by using the listed artificial saltwater in place of Modified Wolfe's mineral solution. The generated record does not preserve the JCM 628 two-layer structure used by that substitution.

## Evidence

TOGO M642 and the referenced JCM 628 base formula define a two-layer gradient medium: a bottom layer made from 50 ml FeS solution, 50 ml artificial saltwater, and 1 g agarose, plus a top layer made from 100 ml artificial saltwater, 1 ml trace mineral solution, 0.195 g MES, 0.042 g NaHCO3, 0.15 g agarose, and gas headspace manipulations.

JCM 629 lists the artificial saltwater stock as 27.5 g NaCl, 5.38 g MgCl2 x 6 H2O, 6.78 g MgSO4 x 7 H2O, 0.72 g KCl, 0.2 g NaHCO3, 1.4 g CaCl2 x 2 H2O, 1 g NH4Cl, 0.05 g KH2PO4, and 1 L distilled water.

The JCM 628 preparation instructions autoclave both layer solutions, pour 0.75 ml bottom layer into each 10 ml vial, let it solidify for at least 30 min, cool the top layer to 35 - 40C, add 1 ml trace vitamins, adjust pH to 6.1 - 6.4 with sterile CO2, overlay 3.75 ml top layer, solidify it for 3 hr to overnight, inoculate just above the bottom layer, seal with butyl rubber stoppers, and replace the gas phase with N2-CO2-O2 8:1:1.

## Completeness

The artificial saltwater salts are present.

The bottom layer, top layer, FeS solution, trace mineral solution, trace vitamin addition, artificial-saltwater aliquots, pH steps, vial overlay volumes, and gas headspace steps are not represented with valid layer or stock boundaries.

## Findings

Layer volumes were converted into parent ingredients. `Bottom layer` and `Top layer` appear as 100 and 101 g/L ingredients even though they are solution scopes, not solutes.

The bottom-layer 50 ml artificial-saltwater aliquot and top-layer 100 ml artificial-saltwater aliquot were summed into a single `150 G_PER_L` artificial-saltwater row, losing which layer gets each aliquot.

`Agarose` was summed across the bottom and top layers as 1.15 g/L, and `NaHCO3` was summed across the top layer and the artificial-saltwater stock as `0.24200000000000002 G_PER_L`.

The FeS solution and trace mineral solution references are represented as empty `Unknown solution` records with `50 G_PER_L` and `1 G_PER_L` concentrations, even though the source rows are 50 ml and 1 ml aliquots.

The trace-vitamin addition from the JCM 628 preparation instructions is missing entirely.

All layer-pouring, cooling, pH, inoculation, sealing, and N2-CO2-O2 headspace instructions are missing from the generated record.

## Recommended Edits

Model the bottom layer, top layer, FeS solution, artificial saltwater, trace mineral solution, and trace vitamin addition as distinct scopes with the source milliliter aliquots kept on the correct layer.

Do not merge same-named ingredients across the top layer, bottom layer, and artificial-saltwater stock.

Carry the JCM 628 preparation instructions through the JCM 629 substitution so the generated record preserves the 0.75 ml bottom-layer and 3.75 ml top-layer vial assembly.

## Follow-up Checks

After regeneration, confirm `Bottom layer`, `Top layer`, `Artificial saltwater`, `FeS solution`, and `Trace mineral solution` no longer appear as gram-per-liter parent ingredients.

Confirm the generated record includes the top-layer 1 ml trace-vitamin addition and the 6.1 - 6.4 pH adjustment by sterile CO2 gas.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.

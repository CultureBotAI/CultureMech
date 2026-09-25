# YAML Record Review: saltwater_iron_oxidizing_bacteria_medium_ii__846706e5

- Repository: CultureMech
- Record: data/merge_yaml/merged/saltwater_iron_oxidizing_bacteria_medium_ii__846706e5.yaml
- Started UTC: 2026-09-25T04:11:44Z
- Finished UTC: 2026-09-25T04:11:44Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002248`, `saltwater_iron_oxidizing_bacteria_medium_ii`, from `data/merge_yaml/merged/saltwater_iron_oxidizing_bacteria_medium_ii__846706e5.yaml`.

The record is the direct MediaDive/JCM J1068 import for `SALTWATER IRON-OXIDIZING BACTERIA MEDIUM-II`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to JCM Medium J1068.

It is the same JCM 1068 medium as TOGO M1137, but it was not deduplicated with the TOGO record because the direct MediaDive path flattened the JCM stock references into parent ingredients instead of retaining solution scopes.

## Evidence

JCM 1068 lists 1 L Artificial saltwater from JCM 629 and 10 ml Wolfe's mineral solution from JCM 265, then adds 10 ml Trace vitamins from JCM 197, 12.5 ml 8% NaHCO3 solution, and 10 ml freshly prepared 0.2 M FeCl2 solution after autoclaving.

JCM 1068 instructs the curator to replace the gas phase with N2-CO2-O2 at 80:20:3 v/v/v and pressurize to 200 kPa.

JCM 629 defines Artificial saltwater as a salt stock with 27.5 g NaCl, 5.38 g MgCl2 x 6H2O, 6.78 g MgSO4 x 7H2O, 0.72 g KCl, 0.2 g NaHCO3, 1.4 g CaCl2 x 2H2O, 1.0 g NH4Cl, and 0.05 g KH2PO4 per liter.

JCM 265 defines Wolfe's mineral solution as Trace minerals from JCM 151 plus 0.02 g NiCl2 x 6H2O, 0.001 g Na2SeO3, and 0.01 g Na2WO4 x 2H2O per liter.

JCM 197 defines Trace vitamins as a 1 L stock with milligram-per-liter vitamin concentrations, including 2 mg/L Biotin, 2 mg/L Folic acid, 10 mg/L Pyridoxine HCl, 5 mg/L Thiamine HCl, 5 mg/L Riboflavin, and 0.1 mg/L Vitamin B12.

## Completeness

The generated direct record has artificial-saltwater salts, Wolfe's mineral solution components, JCM 151 trace-mineral components, and JCM 197 trace-vitamin components.

Those rows all sit in the parent `ingredients` list instead of inside Artificial saltwater, Wolfe's mineral solution, or Trace vitamins solution scopes.

The generated record has no structured Carbon dioxide gas, Nitrogen gas, or Oxygen gas ingredient entries; it preserves the N2-CO2-O2 headspace only as preparation prose.

The generated `preparation_steps` include one Wolfe's-mineral-stock pH instruction as though it applied to the finished JCM 1068 medium.

## Findings

The direct MediaDive record incorrectly flattens all referenced stock contents into the final recipe. Trace vitamins and Wolfe's mineral additives are recorded at stock strength even though JCM 1068 adds only 10 ml/L of each stock.

The `data-quality-cleanup-v1.0` duplicate merger summed unlike quantities after flattening. `NaHCO3` is 12.7 g/L because the 12.5 ml 8% NaHCO3 stock addition was added to the 0.2 g/L artificial-saltwater NaHCO3 row, and `NaCl`, `MgSO4 x 7 H2O`, and `CaCl2 x 2 H2O` likewise carry duplicate-merge notes instead of source-equivalent concentrations.

The 10 ml freshly prepared 0.2 M FeCl2 stock was converted to a direct `FeCl2` row at 10 g/L, losing both the molar stock concentration and the post-autoclave filter-sterilized addition.

The record is a duplicate split from TOGO M1137 / JCM 1068. These two imports should collapse only after both represent Artificial saltwater, Wolfe's mineral solution, 8% NaHCO3 solution, 0.2 M FeCl2 solution, Trace vitamins, and the 80:20:3 gas phase with equivalent structure.

## Recommended Edits

Repair the direct MediaDive J1068 normalized source so JCM 1068 contains five top-level solution aliquots rather than one flattened ingredient list.

Represent JCM 197 vitamins and JCM 265 Wolfe's mineral additives at stock scope, not as final parent medium ingredients.

Move the Wolfe's-mineral pH adjustment into Wolfe's mineral stock preparation notes so it is not applied to the final JCM 1068 recipe.

After repairing the direct MediaDive source, regenerate the merge layer and confirm the MediaDive/JCM J1068 and TOGO M1137 paths converge with equivalent solution semantics.

## Follow-up Checks

Confirm the regenerated record has no duplicate-merge notes on `NaHCO3`, `NaCl`, `MgSO4 x 7 H2O`, or `CaCl2 x 2 H2O`.

Confirm the regenerated parent record has structured Carbon dioxide gas, Nitrogen gas, and Oxygen gas entries with the 80:20:3 200 kPa headspace retained in `preparation_steps`.

Confirm no JCM 197 vitamin row remains as a direct final-medium ingredient at stock strength.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.

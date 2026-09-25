# YAML Record Review: saltwater_iron_oxidizing_bacteria_medium_ii

- Repository: CultureMech
- Record: data/merge_yaml/merged/saltwater_iron_oxidizing_bacteria_medium_ii.yaml
- Started UTC: 2026-09-25T04:08:36Z
- Finished UTC: 2026-09-25T04:08:36Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007659`, `saltwater_iron_oxidizing_bacteria_medium_ii`, from `data/merge_yaml/merged/saltwater_iron_oxidizing_bacteria_medium_ii.yaml`.

The record is the generated canonical record for TOGO M1137 / JCM Medium 1068, `SALTWATER IRON-OXIDIZING BACTERIA MEDIUM-II`, with `freshwater_thiosulfate_oxidizing_bacteria_medium` / TOGO M3016 merged into it as a synonym.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The primary identity is correctly grounded to TOGO M1137 / JCM Medium 1068.

The synonym and `merged_from` link to `freshwater_thiosulfate_oxidizing_bacteria_medium` are not valid. TOGO M1137 is the saltwater JCM 1068 iron-oxidizing medium, while TOGO M3016 is the JCM 1347 freshwater thiosulfate-oxidizing medium.

The TOGO M1137 normalized source has already been repaired by `repair_togo_m1137_score15.py`, but the generated merge layer is still the older flattened form with empty solution stubs.

## Evidence

TOGO M1137 / JCM 1068 lists 1 L Artificial saltwater from Medium M642 / JCM 629 and 10 ml Wolfe's mineral solution from Medium M257 / JCM 265, then adds 10 ml Trace vitamins from Medium M190 / JCM 197, 12.5 ml 8% NaHCO3 solution, and 10 ml freshly prepared 0.2 M FeCl2 solution after autoclaving.

JCM 1068 instructs the curator to replace the gas phase with N2-CO2-O2 at 80:20:3 v/v/v and pressurize to 200 kPa.

TOGO M3016 / JCM 1347 is materially different: it uses 1 L Modified Wolfe's solution from Medium M641, 10 ml Trace minerals from Medium M142, 1 M NaHCO3, 1 M MES, 1 M Na2S2O3 x 5H2O, Trace vitamins, pH 6.0-6.5, and an N2-CO2-O2 gas phase at 79:20:1.

## Completeness

The generated record preserves Carbon dioxide gas, Nitrogen gas, and Oxygen gas as parent ingredients.

The generated `solutions` entries for Artificial saltwater, Wolfe's mineral solution, 8% NaHCO3 solution, 0.2 M FeCl2 solution, and Trace vitamins are empty `Unknown solution` stubs.

All five solution aliquots use `G_PER_L` values copied from TOGO volumes, so 1 L, 10 ml, and 12.5 ml additions were converted to `1`, `10`, and `12.5` g/L values instead of volumetric aliquots.

The generated record has no preparation steps for sealing the tubes, autoclaving before filter-sterilized additions, adding the FeCl2 stock freshly, or pressurizing the N2-CO2-O2 headspace to 200 kPa.

Oxygen gas is missing its CHEBI dioxygen grounding.

## Findings

The generated merge record is stale relative to `data/normalized_yaml/bacterial/TOGO_M1137_Saltwater_Iron-Oxidizing_Bacteria_Medium-II.yaml`, which already contains repaired Artificial saltwater, Wolfe's mineral solution, 8% NaHCO3 solution, 0.2 M FeCl2 solution, and Trace vitamins solution scopes.

The recipe merger falsely collapsed TOGO M1137 with `freshwater_thiosulfate_oxidizing_bacteria_medium`; M3016 belongs to a different JCM medium with different stock references, different sterile additions, a different pH, and a different gas mixture.

The solution migrator defects in the generated file make the recipe quantitatively unusable: the five structured medium references and stock solutions have empty compositions, generic `Unknown solution` names, and gram-per-liter concentrations that originated as liter or milliliter additions.

The generated record also lost the repaired `preparation_steps`, source-specific notes, expanded stock references, `data_quality_flags`, and source URL list that are now present in the normalized TOGO M1137 record.

## Recommended Edits

Regenerate `saltwater_iron_oxidizing_bacteria_medium_ii.yaml` from the repaired TOGO M1137 normalized source instead of editing the generated YAML by hand.

Reject the M1137 and M3016 duplicate edge before regeneration so the saltwater iron-oxidizer record no longer lists the freshwater thiosulfate medium as a synonym or `merged_from` source.

Carry `ML_PER_L` aliquots, stock concentrations, nonempty stock compositions, the N2-CO2-O2 80:20:3 200 kPa headspace instruction, and Oxygen gas CHEBI grounding from the repaired normalized source into the generated record.

## Follow-up Checks

After regeneration, confirm `saltwater_iron_oxidizing_bacteria_medium_ii` has no TOGO M3016 synonym, no `freshwater_thiosulfate_oxidizing_bacteria_medium` `merged_from` value, and no trace of the M3016-only 79:20:1 gas mixture.

Confirm the regenerated M1137 record has exactly five solution scopes with nonempty compositions or single-solute stock definitions: Artificial saltwater, Wolfe's mineral solution, 8% NaHCO3 solution, 0.2 M FeCl2 solution, and Trace vitamins.

Confirm any regenerated direct MediaDive/JCM 1068 copy and the TOGO M1137 copy converge into one JCM 1068 recipe only after they both carry equivalent solution semantics.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.

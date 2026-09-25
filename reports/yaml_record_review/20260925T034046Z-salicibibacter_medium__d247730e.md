# YAML Record Review: salicibibacter_medium__d247730e

- Repository: CultureMech
- Record: data/merge_yaml/merged/salicibibacter_medium__d247730e.yaml
- Started UTC: 2026-09-25T03:40:46Z
- Finished UTC: 2026-09-25T03:40:46Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002419`, `salicibibacter_medium`, from `data/merge_yaml/merged/salicibibacter_medium__d247730e.yaml`.

The generated record uses JCM Medium J1253 / `mediadive.medium:J1253` as the canonical source and lists `jcm_medium_no_167` / JCM Medium J167 as a duplicate synonym in `merged_from`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The canonical identity is grounded to the correct JCM 1253 page for `SALICIBIBACTER MEDIUM`.

JCM 167 is not an alternate name for JCM 1253. The JCM 1253 formulation references Medium No. 167 only as the source of a 1 ml/L trace element solution, while JCM 167 is a separate base formulation with a different NaCl amount, direct 5 g/L Na2CO3, a 9.0-9.5 final pH, and its own SL-6 trace element stock.

The duplicate-merge fingerprint is therefore a false positive: the generated record should not put `jcm_medium_no_167` in `synonyms` or `merged_from`.

## Evidence

The JCM 1253 source lists 1 g KH2PO4, 1 g KCl, 1 g NH4Cl, 0.24 g MgSO4 x 7 H2O, 0.17 g CaSO4 x 2 H2O, 1 ml trace element solution from Medium No. 167, 140 g NaCl, 1 g sodium glutamate, 5 g yeast extract, 5 g Casamino acids, and 20 g agar per liter, then says to add 5 ml of an autoclaved 10% w/v Na2CO3 solution and check a final pH of 7.5-8.0.

The JCM 167 source lists a related but different medium with 200 g NaCl and 5 g Na2CO3 in the main recipe, a 9.0-9.5 final pH, and the SL-6 trace element solution stock. Its terminal "Adjust pH to 3.6" instruction applies to the SL-6 stock, not to the complete JCM 1253 medium.

## Completeness

The JCM 1253 main-solution ingredient set is present, but two concentration rows were taken from JCM 167 rather than JCM 1253 and the generated record does not model the 1 ml/L trace-solution aliquot or the 5 ml 10% Na2CO3 stock aliquot.

The SL-6 trace element stock recipe from JCM 167 is partially present as direct ingredient rows. Its 1 L distilled water row and pH 3.6 preparation step are not kept in an explicit stock-solution scope.

## Findings

JCM 167 was merged as a duplicate of JCM 1253 even though JCM 1253 only links to JCM 167 for a trace element solution. This creates an invalid synonym and prevents JCM 167 from remaining available as its own recipe.

The canonical JCM 1253 formula inherited JCM 167's `NaCl` amount. The generated record has 200 g/L NaCl; JCM 1253 specifies 140 g/L.

The Na2CO3 handling is off by scope and amount. JCM 1253 specifies 5 ml of a 10% w/v Na2CO3 solution added after autoclaving, equivalent to 0.5 g/L Na2CO3 in the final liter; the generated record has a direct 5 g/L Na2CO3 row.

The SL-6 trace element stock from JCM 167 has been flattened into the JCM 1253 parent at stock concentrations. JCM 1253 adds only 1 ml/L of that stock, so the generated direct metal rows are about 1000x too concentrated for the final medium.

`NiCl2 x 6 H2O` is grounded to `CHEBI:34887` / `nickel dichloride`, which does not capture the hexahydrate used in the JCM 167 SL-6 stock formula.

## Recommended Edits

Remove the `jcm_medium_no_167` / `salicibibacter_medium` duplicate merge by repairing the normalized inputs or the merge-fingerprint logic, then regenerate the merged YAML.

Keep JCM 1253 as `SALICIBIBACTER MEDIUM` with 140 g/L NaCl, 1 ml/L of the JCM 167 trace element solution stock, and the 5 ml/L 10% w/v Na2CO3 post-autoclave aliquot.

Keep JCM 167 as its own medium. Model its SL-6 trace element solution as a stock with the listed 1 L distilled water row and pH 3.6 adjustment so that those stock concentrations and prep instructions cannot be attached to the JCM 1253 parent medium.

Reground `NiCl2 x 6 H2O` to a hydrate-specific CHEBI term if one is available in the repository's CHEBI snapshot; otherwise leave the mapping absent with the hydrated label intact rather than grounding it to an anhydrous nickel chloride term.

## Follow-up Checks

Regenerate `data/merge_yaml/merged/salicibibacter_medium__d247730e.yaml` from the normalized YAML after repairing JCM 1253, and confirm `merged_from` no longer contains `jcm_medium_no_167`.

Run open schema, strict, reference, and term validation against the regenerated JCM 1253 record and the split JCM 167 record.

Check for other media that link to JCM 167 as a trace element source to make sure the merge logic treats stock references as references instead of duplicate recipe evidence.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.

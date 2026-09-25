# YAML Record Review: MICROAEROPHILIC LUTIBACTER MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/microaerophilic_lutibacter_medium__7e7d58f1.yaml`
- Started UTC: 2026-09-24T06:17:29Z
- Finished UTC: 2026-09-24T06:17:29Z
- Verdict: needs curation

## Target

- Reviewed merged record `data/merge_yaml/merged/microaerophilic_lutibacter_medium__7e7d58f1.yaml`.
- Editable normalized source: `data/normalized_yaml/bacterial/microaerophilic_lutibacter_medium.yaml`.
- MediaDive medium: `mediadive.medium:J1069`, MICROAEROPHILIC LUTIBACTER MEDIUM.
- JCM source: Medium 1069.

## Validation

- LinkML open-schema validation: passed; `No issues found`.
- Strict validation: passed with 0 errors; `validate_strict.py` scanned 1 file and produced only the TSV header.
- Reference validation: passed; 1 file, 0 checks.
- Term validation: passed.
- Embedded history: Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The recipe identity is coherent: the JCM 1069 page and MediaDive `J1069` both name MICROAEROPHILIC LUTIBACTER MEDIUM.
- The JCM recipe links to Artificial saltwater, Wolfe's mineral solution, and Trace vitamins sub-recipes. MediaDive preserves those as solution records, but the YAML loses all solution boundaries.
- `NiCl2 x 6 H2O` is grounded only to generic nickel dichloride.
- `ph_value: 6.2` captures the lower bound of the JCM pH adjustment but loses the upper bound, 6.5.

## Evidence

- The JCM source defines the final medium as 1 L Artificial saltwater, 1.95 g MES, 1 ml Wolfe's mineral solution, 10 ml Trace vitamins, and 2 g Tryptone.
- The JCM final preparation says to mix components, adjust pH to 6.2 to 6.5, distribute into culture vessels, replace the gas phase with N2-CO2-O2 90:10:2, seal with butyl rubber stoppers, and autoclave.
- MediaDive expands Artificial saltwater into a 1 L stock containing NaCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, KCl, NaHCO3, CaCl2 x 2 H2O, NH4Cl, KH2PO4, and water.
- MediaDive expands Wolfe's mineral solution as 1 L Trace minerals plus NiCl2 x 6 H2O, Na2SeO3, and Na2WO4 x 2 H2O.
- MediaDive expands Trace minerals into a 1 L stock containing NTA, MgSO4 x 7 H2O, MnSO4 x n H2O, NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2, H3BO3, Na2MoO4 x 2 H2O, and water.
- MediaDive expands Trace vitamins into a 1 L stock added at 10 ml/L-equivalent in the final medium.

## Completeness

- The generated recipe is missing Artificial saltwater, Wolfe's mineral solution, Trace minerals, and Trace vitamins as nested solutions.
- Main-medium salts from Artificial saltwater are indistinguishable from trace-mineral salts from Wolfe's mineral solution after duplicate merging.
- The final gas replacement and trace-minerals pH adjustment instructions are present.

## Findings

- The final medium has been flattened from solution additions into 31 top-level ingredients. It no longer states that the final medium uses 1 L Artificial saltwater, 1 ml Wolfe's mineral solution, and 10 ml Trace vitamins.
- `NaCl`, `MgSO4 x 7 H2O`, and `CaCl2 x 2 H2O` were summed across Artificial saltwater and the nested Trace minerals stock, yielding 28.5, 9.78, and 1.5 g/L instead of preserving the two source contexts.
- Wolfe's mineral components are listed as final ingredients at stock concentration even though Wolfe's mineral solution is only a 1 ml addition to the final medium.
- Trace vitamins are listed as final ingredients at stock concentration even though the Trace vitamins stock is only a 10 ml addition to the final medium.
- The trace-minerals preparation step is present but now appears as a top-level medium step rather than a step attached to the Trace minerals stock.
- The normalized source has the same flattened structure, so this is not only a stale generated merge.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/microaerophilic_lutibacter_medium.yaml`.
- Restore the final recipe as Artificial saltwater plus MES, Wolfe's mineral solution, Trace vitamins, and Tryptone.
- Nest Artificial saltwater, Wolfe's mineral solution, Trace minerals, and Trace vitamins so their components are scoped to the correct stocks.
- Keep the trace-minerals pH 6.5 to final pH 7.0 preparation step on the Trace minerals stock, not the final medium.
- Restore the final pH range 6.2 to 6.5.
- Re-ground `NiCl2 x 6 H2O` to an exact hexahydrate term if one is available.
- Regenerate `data/merge_yaml/merged/microaerophilic_lutibacter_medium__7e7d58f1.yaml` after the normalized source is fixed.

## Follow-up Checks

- Re-run focused open-schema, strict, reference, and term validators for `data/merge_yaml/merged/microaerophilic_lutibacter_medium__7e7d58f1.yaml`.
- Verify final NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O are no longer summed with Trace minerals stock rows.
- Verify vitamins are nested under a Trace vitamins stock used at 10 ml per final recipe, not listed as final stock-strength top-level ingredients.
- Verify the final N2-CO2-O2 gas-replacement instruction remains attached to the final medium.

## Additional Notes

- Empty optional fields were not treated as defects.

# YAML Record Review: sporomusa_medium_2

- Repository: CultureMech
- Record: data/merge_yaml/merged/sporomusa_medium_2.yaml
- Started UTC: 2026-09-25T06:52:41Z
- Finished UTC: 2026-09-25T06:55:00Z
- Verdict: pass with minor issues

## Target

Reviewed the generated record for JCM Medium J1425, `SPOROMUSA MEDIUM-2`, assigned `CultureMech:015862`.

## Validation

- LinkML validation: Passed; no issues found.
- Strict validation: Passed; the TSV contained only the header, with 0 error rows.
- LinkML reference validation: Passed; 0 reference checks were run and all passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record is a direct JCM GRMD import for `jcm.grmd:1425`. The live JCM page resolves GRMD 1425 to `SPOROMUSA MEDIUM-2`, matching the generated `original_name` and `media_term` identity.

The ingredient groundings are partial but appropriate for the resolved salts, water, and resazurin rows. JCM stock-solution rows such as FeCl2 solution, trace element solution, Se/W solution, trace vitamins, 8 percent NaHCO3 solution, 0.1 percent FeSO4 x 7 H2O solution, and 0.1 M Dithiothreitol solution remain solution-level rows rather than expanded solutes.

## Evidence

The generated target preserves JCM's two base solutions: Solution A contains 860 ml water, 0.5 g NH4Cl, 0.5 g MgSO4 x 7 H2O, 0.25 g CaCl2 x 2 H2O, 2.25 g NaCl, 1 ml FeCl2 stock, 1 ml trace-element stock, 1 ml Se/W stock, 2 ml 0.1 percent FeSO4 stock, 2 g yeast extract, 2 g Casitone, and 0.5 mg resazurin; Solution B contains 100 ml water, 0.35 g K2HPO4, and 0.23 g KH2PO4.

The post-autoclave additions also match the JCM source: 10 ml trace vitamins and 30 ml 8 percent NaHCO3 after combining Solutions A and B, followed by 10 ml 0.1 M Dithiothreitol per liter prior to inoculation. The generated preparation steps retain JCM's N2 autoclaving, H2-CO2 80:20 dispensing atmosphere, butyl-rubber stopper sealing, and pH 7.0 adjustment instruction.

## Completeness

The direct JCM formulation is preserved at the level exposed on the GRMD 1425 page, including milliliter and milligram units. MediaDive's REST API returned `DataNotFound` for `J1425`, so no MediaDive structured mirror was available for this JCM-only medium.

Chemical completeness is limited because the JCM cross-reference stocks are not expanded. The record tells consumers to add 1 ml FeCl2 solution, 1 ml trace element solution, 1 ml Se/W solution, and 10 ml trace vitamins, but it does not inline their recipes from the referenced JCM medium pages.

## Findings

- Low: Cross-referenced JCM stock solutions remain unexpanded and mostly ungrounded. FeCl2 solution and trace element solution point to JCM Medium 187, Se/W solution points to JCM Medium 317, and trace vitamins point to JCM Medium 197 on the source page.
- Low: Percentage and molar stock additions are retained as solution names and `ML_PER_L` rows. This is source-faithful, but 0.1 percent FeSO4 x 7 H2O, 8 percent NaHCO3, and 0.1 M Dithiothreitol are not converted to final solute concentrations.

## Recommended Edits

- Keep `data/merge_yaml/merged/sporomusa_medium_2.yaml` generated from `data/normalized_yaml/bacterial/JCM_J1425_SPOROMUSA_MEDIUM_2.yaml`; do not edit the generated file by hand.
- Add a JCM stock-expansion pass that can follow Medium 187, Medium 317, and Medium 197 references and attach resolvable stock compositions to the normalized JCM record while preserving the original milliliter aliquot evidence.
- Where a source row embeds a simple concentration, add derived final-solute amounts for the 0.1 percent FeSO4 x 7 H2O, 8 percent NaHCO3, and 0.1 M Dithiothreitol stocks or explicitly mark them as unresolved stock additions.

## Follow-up Checks

- After any stock expansion, confirm that the original JCM aliquot rows remain traceable so the direct GRMD recipe can still be audited against the source page.

## Additional Notes

None found

# YAML Record Review: hydrogen_using_marine_methanogen_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium.yaml
- Started UTC: 2026-09-23T13:08:32Z
- Finished UTC: 2026-09-23T13:10:37Z
- Verdict: needs curation

## Target

- Reviewed generated record: `data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:008683`
- Name: `hydrogen_using_marine_methanogen_medium`
- Source identity: TOGO Medium M2092 from NBRC Medium 1403, `Hydrogen-using marine methanogen medium`
- Maintained input: `data/normalized_yaml/archaea/TOGO_M2092_Hydrogen-using_marine_methanogen_medium.yaml`
- Merge state: generated from one normalized source, `TOGO_M2092_Hydrogen-using_marine_methanogen_medium`

## Validation

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium.yaml`: passed.
- `python scripts/validate_strict.py data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium.yaml --out /private/tmp/hydrogen_using_marine_methanogen_medium.strict.tsv --workers 1 --quiet`: passed with 0 error rows.
- `linkml-reference-validator validate data data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`: passed; 0 reference checks.
- `linkml-term-validator validate-data data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`: exited 0.
- Embedded history: Not checked; the repository exposes `just validate-history` for standalone `history/` entries, not for `MediaRecipe.curation_history` embedded in a merged YAML file.

## Identity and Grounding

- The generated record correctly identifies TOGO M2092 / NBRC Medium 1403 rather than the separate same-named TOGO M2010 / NBRC Medium 1298 record.
- The TOGO API and live NBRC Medium 1403 page agree on the main medium identity, the three named subcomponents, and the preparation text.
- The generated `Trace elements solution**` and `Vitamin solution***` rows are grounded to unrelated MediaDive solution IDs:
  - `mediadive.solution:6129` in `data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml` contains ZnSO4, MnCl2, MoO3, CuSO4, and cobalt nitrate, not the NBRC 1403 NTA/FeCl3/CoCl2/CaCl2/ZnCl2/NiCl2 trace recipe.
  - `mediadive.solution:6241` in `data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml` contains only cyanocobalamin, thiamine, biotin, and water, not the nine-component NBRC 1403 vitamin recipe.
- Several hydrated salts are grounded too broadly after enrichment. In particular, hydrated `CoCl2` and `NiCl2` source rows are grounded to generic cobalt dichloride and nickel dichloride terms rather than hydrate-specific terms.

## Evidence

- TOGO M2092 and NBRC Medium 1403 support a 1 L main solution with 30 g NaCl, 0.15 g calcium chloride dihydrate, 0.3 g NH4Cl, 0.75 g magnesium chloride hexahydrate, 0.2 g Bacto Yeast Extract, 0.14 g coenzyme M, 1 mg resazurin, 5 ml KP buffer, 2 ml trace elements solution, 2 ml vitamin solution, and variable H2, CO2, and N2 gas.
- The source defines KP buffer as a separate 1 L stock with 119 g KH2PO4 and 21 g K2HPO4, autoclaved under N2.
- The source defines a separate 1 L trace elements solution with NaCl, calcium chloride dihydrate, sodium molybdate dihydrate, boric acid, manganese chloride tetrahydrate, cobalt chloride hexahydrate, nickel chloride hexahydrate, copper chloride dihydrate, zinc chloride, iron chloride hexahydrate, potassium aluminum sulfate dodecahydrate, NTA, sodium tungstate, sodium selenate, and NaOH for pH adjustment.
- The source defines a separate 1 L vitamin solution with nine mg-scale ingredients: biotin, p-aminobenzoic acid, thiamine-HCl, calcium pantothenate, pyridoxine-HCl, folic acid, vitamin B12, riboflavin, and nicotinic acid.
- The source preparation says to leave pH unadjusted in the main medium, exclude KP buffer, vitamin solution, Na2CO3, cysteine-HCl, and sodium sulfide nonahydrate from the initial mix, dispense under H2/CO2, separately autoclave KP buffer and the 5 percent cysteine and sulfide solutions under N2, filter-sterilize the vitamin and 10 percent Na2CO3 solutions, add the late solutions aseptically and anaerobically before inoculation, and pressurize inoculated vessels to 150 kPa with H2/CO2.

## Completeness

- Consequentially incomplete: the generated canonical record has no `preparation_steps`, so the anaerobic dispense, separate sterilization, filter sterilization, late additions, and 150 kPa H2/CO2 pressurization are absent.
- Consequentially incomplete: the three subcomponent additions are retained only as `solutions` with `G_PER_L` concentrations, empty `composition` lists, and `Unknown solution` names; the actual 5 ml, 2 ml, and 2 ml addition volumes are no longer represented as volumes.
- Consequentially incomplete: the subcomponent contents are also flattened as top-level ingredient rows at their stock concentrations, which overstates every KP, trace, and vitamin stock ingredient in the final medium.
- Empty optional organism and growth-evidence slots are acceptable; NBRC 1403 is a source recipe, not a strain growth assay.
- Bounded searches:
  - `find data/raw/togo data/raw/nbrc -maxdepth 3 -type f -print`, which includes ignored files, found only `data/raw/togo/README.md` and `data/raw/nbrc/README.md`.
  - `rg --no-ignore --hidden -n -F 'Hydrogen-using marine methanogen medium' data/raw/togo data/raw/nbrc` found no raw TOGO or NBRC payload in this checkout, so the live TOGO API and NBRC page were used as the inspected sources.

## Findings

### Blockers

None found.

### Major

| Finding | Evidence | Maintained owner |
|---|---|---|
| Three stock solutions are duplicated into the main ingredient list at stock strength. | The source main solution adds 5 ml KP buffer, 2 ml trace elements solution, and 2 ml vitamin solution. The generated record has those solution rows but also promotes 119 g/L KH2PO4, 21 g/L K2HPO4, all trace stock salts, and all vitamin stock entries into top-level final-medium ingredients. | `data/normalized_yaml/archaea/TOGO_M2092_Hydrogen-using_marine_methanogen_medium.yaml`; the TOGO importer or solution migration that should preserve subcomponent boundaries. |
| Milligram vitamin and indicator quantities are represented as grams per liter. | NBRC/TOGO list resazurin as 1 mg in the main medium and the vitamin stock as 0.01 to 10 mg per liter; the generated record uses `G_PER_L` for resazurin and each vitamin value. `data/import_tracking/reports/concentration_plausibility.tsv` already flags 8 vitamin/indicator unit slips for `CultureMech:008683`. | TOGO quantity normalization for M2092 and the vitamin subcomponent importer. |
| Duplicate ingredients were summed across final and stock boundaries. | The source has 30 g NaCl in the main solution plus 1 g NaCl in the trace stock, and 0.15 g calcium chloride dihydrate in the main solution plus 0.1 g in the trace stock. The generated record has 31.0 and 0.25 g/L rows; `data/import_tracking/reports/merged_duplicates.tsv` flags both as `DIFFERING_PARTS`. | `data/normalized_yaml/archaea/TOGO_M2092_Hydrogen-using_marine_methanogen_medium.yaml` and duplicate cleanup for source-derived repeated labels. |
| Source preparation was dropped. | NBRC/TOGO give essential anaerobic and sterilization procedure for H2/CO2 dispense, late additions, N2-autoclaved reducing stocks, filter-sterilized vitamin and carbonate stocks, and 150 kPa H2/CO2 pressurization. The generated record has no `preparation_steps`. | TOGO M2092 normalized record and importer support for TOGO `comments`. |
| Solution CURIEs are wrong for the two named NBRC subcomponents. | `mediadive.solution:6129` and `mediadive.solution:6241` resolve to unrelated local MediaDive solution records with different compositions. The NBRC stocks are local M2092 subcomponents, not those MediaDive recipes. | `data/normalized_yaml/archaea/TOGO_M2092_Hydrogen-using_marine_methanogen_medium.yaml` solution migration. |
| Hydrated salts and calcium pantothenate are grounded too broadly or to the conjugate base. | The source specifies cobalt chloride hexahydrate, nickel chloride hexahydrate, and calcium pantothenate. The generated record grounds them to cobalt dichloride, nickel dichloride, and `(R)-pantothenate`, respectively. | CHEBI enrichment and MediaIngredientMech refresh for the TOGO M2092 normalized input. |

### Minor

None found.

## Recommended Edits

1. In `data/normalized_yaml/archaea/TOGO_M2092_Hydrogen-using_marine_methanogen_medium.yaml`, preserve `KP buffer*`, `Trace elements solution**`, and `Vitamin solution***` as medium-specific stock additions with the source 5 ml, 2 ml, and 2 ml volumes.
2. Remove stock-only components from the top-level final-medium `ingredients`; keep them inside maintained local solution records or nested solution composition.
3. Keep the source units for resazurin and vitamin-stock ingredients as milligrams, and do not convert the numeric values to `G_PER_L` without a `0.001` factor.
4. Split the main NaCl and calcium chloride rows from their trace-stock rows instead of summing them.
5. Convert the TOGO/NBRC comments into ordered `preparation_steps`, including anaerobic H2/CO2 dispense, N2 autoclaving, filter sterilization, late additions, the trace-stock NaOH adjustment, and final H2/CO2 pressurization.
6. Remove the unrelated `mediadive.solution:6129` and `mediadive.solution:6241` terms from NBRC 1403 solution references unless a source-specific crosswalk verifies equivalence.
7. Re-ground cobalt chloride hexahydrate, nickel chloride hexahydrate, and calcium pantothenate to terms that preserve the source chemical forms.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation on the normalized TOGO M2092 record and the regenerated merged record.
- Re-run the concentration-plausibility audit for `CultureMech:008683`; the resazurin, vitamin, and trace-stock alerts should disappear once mg quantities and stock boundaries are represented correctly.
- Re-run the duplicate-ingredient audit; M2092 should no longer sum 30 g main-medium NaCl with 1 g trace-stock NaCl or 0.15 g main-medium calcium chloride with 0.1 g trace-stock calcium chloride.
- Manually compare regenerated M2092 against both the TOGO API JSON and the NBRC Medium 1403 page to ensure every source paragraph remains assigned either to the main recipe or the intended local stock recipe.

## Additional Notes

- TOGO M2092 and TOGO M2010 share the same source label but are different NBRC source media. M2092 includes coenzyme M and points to NBRC Medium 1403; M2010 points to NBRC Medium 1298 and is represented by `data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium__931ca534.yaml`.
- The generated M2092 record still has `mediaingredientmech_term` on `Cysteine-HCl`; the term validator did not reject it, so this is low priority compared with the stock-boundary and unit defects.

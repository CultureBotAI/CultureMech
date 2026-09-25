# YAML Record Review: hydrogen_using_marine_methanogen_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium__931ca534.yaml
- Started UTC: 2026-09-23T13:12:00Z
- Finished UTC: 2026-09-23T13:12:41Z
- Verdict: needs curation

## Target

- Reviewed generated record: `data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium__931ca534.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:008597`
- Name: `hydrogen_using_marine_methanogen_medium`
- Source identity: TOGO Medium M2010 from NBRC Medium 1298, `Hydrogen-using marine methanogen medium`
- Maintained input: `data/normalized_yaml/archaea/hydrogen_using_marine_methanogen_medium.yaml`
- Merge state: generated from one normalized source, `hydrogen_using_marine_methanogen_medium`

## Validation

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium__931ca534.yaml`: passed.
- `python scripts/validate_strict.py data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium__931ca534.yaml --out /private/tmp/hydrogen_using_marine_methanogen_medium__931ca534.strict.tsv --workers 1 --quiet`: passed with 0 error rows.
- `linkml-reference-validator validate data data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium__931ca534.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`: passed; 0 reference checks.
- `linkml-term-validator validate-data data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium__931ca534.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`: passed after the expected `eutils` deprecation warning.
- Embedded history: Not checked; the repository exposes `just validate-history` for standalone `history/` entries, not for `MediaRecipe.curation_history` embedded in a merged YAML file.

## Identity and Grounding

- The generated record correctly identifies TOGO M2010 / NBRC Medium 1298, not same-named TOGO M2092 / NBRC Medium 1403.
- The source identity and stable ID agree across `media_term`, source notes, the normalized input, and the generated filename suffix.
- The TOGO API and live NBRC Medium 1298 page agree on the medium identity, three named subcomponents, and preparation text.
- The generated `Trace elements solution**` and `Vitamin solution***` rows are grounded to unrelated MediaDive solution IDs:
  - `mediadive.solution:6129` in `data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml` has a different zinc sulfate, manganese chloride, molybdenum trioxide, copper sulfate, and cobalt nitrate formula.
  - `mediadive.solution:6241` in `data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml` has only cyanocobalamin, thiamine, biotin, and water rather than NBRC 1298's nine vitamin components.
- Several ingredient groundings are broader than the source chemical forms: hydrated cobalt chloride and hydrated nickel chloride are grounded as generic chlorides, and calcium pantothenate is grounded as `(R)-pantothenate`.

## Evidence

- TOGO M2010 and NBRC Medium 1298 support a 1 L main solution with 30 g NaCl, 0.15 g calcium chloride dihydrate, 0.3 g NH4Cl, 0.75 g magnesium chloride hexahydrate, 0.2 g Bacto Yeast Extract, 1 mg resazurin, 5 ml KP buffer, 2 ml trace elements solution, 2 ml vitamin solution, and variable H2, CO2, and N2 gas.
- The source defines KP buffer as a separate 1 L stock with 119 g KH2PO4 and 21 g K2HPO4.
- The source defines a separate 1 L trace elements solution with NaCl, calcium chloride dihydrate, sodium molybdate dihydrate, boric acid, manganese chloride tetrahydrate, cobalt chloride hexahydrate, nickel chloride hexahydrate, copper chloride dihydrate, zinc chloride, iron chloride hexahydrate, potassium aluminum sulfate dodecahydrate, NTA, sodium tungstate, sodium selenate, and NaOH for pH adjustment.
- The source defines a separate 1 L vitamin solution with nine mg-scale ingredients: biotin, p-aminobenzoic acid, thiamine-HCl, calcium pantothenate, pyridoxine-HCl, folic acid, vitamin B12, riboflavin, and nicotinic acid.
- The source preparation leaves the main pH unadjusted, excludes KP buffer, vitamin solution, Na2CO3, cysteine-HCl, and sodium sulfide nonahydrate from the initial mix, dispenses under H2/CO2, separately autoclaves KP buffer plus 5 percent cysteine and sulfide stocks under N2, filter-sterilizes vitamin and 10 percent Na2CO3 solutions, adds late solutions aseptically and anaerobically before inoculation, and pressurizes inoculated vessels to 150 kPa with H2/CO2.

## Completeness

- Consequentially incomplete: the generated record has no `preparation_steps`; the H2/CO2 dispense, separate N2 autoclaving, filter sterilization, anaerobic late additions, and final 150 kPa pressurization are absent.
- Consequentially incomplete: the 5 ml KP buffer, 2 ml trace elements solution, and 2 ml vitamin solution additions survive only as empty `G_PER_L` solution rows named `Unknown solution`.
- Consequentially incomplete: stock compositions are flattened as direct top-level ingredients, so KP buffer, trace-solution, and vitamin-solution ingredient strengths are no longer scoped to their own 1 L stock recipes.
- Empty optional target-organism and growth-evidence slots are acceptable because NBRC 1298 is a medium recipe rather than a primary growth assay.
- Bounded searches:
  - `find data/raw/togo data/raw/nbrc -maxdepth 3 -type f -print`, which includes ignored files, found only `data/raw/togo/README.md` and `data/raw/nbrc/README.md`.
  - `rg --no-ignore --hidden -n -F 'Hydrogen-using marine methanogen medium' data/raw/togo data/raw/nbrc` found no raw TOGO or NBRC payload in this checkout, so the live TOGO API and NBRC page were used as the inspected sources.

## Findings

### Blockers

None found.

### Major

| Finding | Evidence | Maintained owner |
|---|---|---|
| Stock-solution ingredients are flattened into the main medium at stock strength. | NBRC/TOGO add 5 ml KP buffer, 2 ml trace elements solution, and 2 ml vitamin solution to the main solution. The generated record also lists KH2PO4, K2HPO4, all trace-solution salts, and all vitamin-solution ingredients as if they were direct final-medium rows. | `data/normalized_yaml/archaea/hydrogen_using_marine_methanogen_medium.yaml`; TOGO import and solution migration. |
| Source milligrams are represented as grams per liter. | NBRC/TOGO list 1 mg resazurin in the main solution and nine mg-scale vitamin rows in the vitamin stock. The generated record writes those numeric values as `G_PER_L`; `data/import_tracking/reports/concentration_plausibility.tsv` flags 8 vitamin/indicator unit slips for `CultureMech:008597`. | TOGO quantity normalization for M2010 and vitamin subcomponent import. |
| Repeated labels are summed across main and trace-stock boundaries. | The source has 30 g main-medium NaCl plus 1 g trace-stock NaCl, and 0.15 g main-medium calcium chloride plus 0.1 g trace-stock calcium chloride. The generated record sums these into 31.0 and 0.25 g/L; `data/import_tracking/reports/merged_duplicates.tsv` flags both rows as `DIFFERING_PARTS`. | `data/normalized_yaml/archaea/hydrogen_using_marine_methanogen_medium.yaml` and duplicate cleanup. |
| Source preparation is missing. | The NBRC/TOGO comments specify initial mixing exclusions, H2/CO2 dispense, N2 autoclaving, filter-sterilized late solutions, aseptic anaerobic additions, and 150 kPa H2/CO2 pressurization, none of which appear in the generated record. | TOGO M2010 normalized record and importer support for TOGO comments. |
| MediaDive solution links point to unrelated stock recipes. | `mediadive.solution:6129` and `mediadive.solution:6241` resolve locally to MediaDive recipes that do not match the NBRC trace and vitamin formulations. | Solution migration for `data/normalized_yaml/archaea/hydrogen_using_marine_methanogen_medium.yaml`. |
| Hydrate and salt groundings lose exact source identity. | NBRC 1298 specifies cobalt chloride hexahydrate, nickel chloride hexahydrate, and calcium pantothenate; the generated record grounds those labels to generic cobalt dichloride, generic nickel dichloride, and the pantothenate anion. | CHEBI enrichment and MediaIngredientMech refresh for the TOGO M2010 normalized input. |

### Minor

None found.

## Recommended Edits

1. Preserve `KP buffer*`, `Trace elements solution**`, and `Vitamin solution***` as NBRC 1298 local stock recipes and carry the main-source 5 ml, 2 ml, and 2 ml stock addition volumes.
2. Remove KP, trace, and vitamin stock-only ingredients from the top-level final-medium ingredient list.
3. Convert mg quantities with the correct 0.001 factor or preserve them as milligram quantities instead of turning 1 mg, 2 mg, 5 mg, and 10 mg values into the same numeric values in `G_PER_L`.
4. Keep the source's repeated NaCl and calcium chloride labels in their main-solution versus trace-stock contexts so duplicate cleanup cannot sum them.
5. Translate the TOGO comment paragraphs into ordered `preparation_steps` for anaerobic dispensing, separate sterilization, filtration, late additions, trace-stock pH handling, and pressurization.
6. Remove unrelated `mediadive.solution:6129` and `mediadive.solution:6241` CURIEs from these local NBRC stock-solution rows.
7. Re-ground cobalt chloride hexahydrate, nickel chloride hexahydrate, and calcium pantothenate without dropping hydrates or cations.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation on the corrected TOGO M2010 normalized input and the regenerated `data/merge_yaml/merged/hydrogen_using_marine_methanogen_medium__931ca534.yaml`.
- Re-run concentration-plausibility and duplicate-ingredient audits for `CultureMech:008597`; the 8 unit-slip rows and the two `DIFFERING_PARTS` rows should disappear.
- Re-run merge generation and verify M2010 remains separate from M2092 because the former lacks the coenzyme M row that is present in NBRC 1403.
- Manually compare the regenerated M2010 record against both the TOGO API JSON and NBRC Medium 1298.

## Additional Notes

- This same source-formulation family appears in M2092/NBRC 1403, but M2010/NBRC 1298 is a distinct record and should not be merged with it.
- The remaining legacy `mediaingredientmech_term` on `Cysteine-HCl` is not a validator failure and is lower priority than the stock-solution and unit handling defects.

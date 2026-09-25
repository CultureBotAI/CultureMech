# YAML Record Review: hydrogen_using_marine_sulfate_reducer_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogen_using_marine_sulfate_reducer_medium.yaml
- Started UTC: 2026-09-23T13:13:54Z
- Finished UTC: 2026-09-23T13:14:58Z
- Verdict: needs curation

## Target

- Reviewed generated record: `data/merge_yaml/merged/hydrogen_using_marine_sulfate_reducer_medium.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:008598`
- Name: `hydrogen_using_marine_sulfate_reducer_medium`
- Source identity: TOGO Medium M2011 from NBRC Medium 1299, `Hydrogen-using marine sulfate-reducer medium`
- Maintained input: `data/normalized_yaml/bacterial/hydrogen_using_marine_sulfate_reducer_medium.yaml`
- Merge state: generated from one normalized source, `hydrogen_using_marine_sulfate_reducer_medium`

## Validation

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogen_using_marine_sulfate_reducer_medium.yaml`: passed.
- `python scripts/validate_strict.py data/merge_yaml/merged/hydrogen_using_marine_sulfate_reducer_medium.yaml --out /private/tmp/hydrogen_using_marine_sulfate_reducer_medium.strict.tsv --workers 1 --quiet`: passed with 0 error rows.
- `linkml-reference-validator validate data data/merge_yaml/merged/hydrogen_using_marine_sulfate_reducer_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`: passed; 0 reference checks.
- `linkml-term-validator validate-data data/merge_yaml/merged/hydrogen_using_marine_sulfate_reducer_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`: passed after the expected `eutils` deprecation warning.
- Embedded history: Not checked; the repository exposes `just validate-history` for standalone `history/` entries, not for `MediaRecipe.curation_history` embedded in a merged YAML file.

## Identity and Grounding

- The generated record correctly identifies TOGO M2011 / NBRC Medium 1299.
- The TOGO API and live NBRC Medium 1299 page agree on the sulfate-reducer identity, source accession, sulfate/thiosulfate main-medium additions, three named stock additions, and preparation text.
- The generated `Trace elements solution**` and `Vitamin solution***` rows are grounded to unrelated MediaDive solution IDs:
  - `mediadive.solution:6129` points to a different Trace elements solution with zinc sulfate, manganese chloride, molybdenum trioxide, copper sulfate, and cobalt nitrate.
  - `mediadive.solution:6241` points to a different Vitamin solution with cyanocobalamin, thiamine, biotin, and water only.
- Hydrated cobalt chloride and hydrated nickel chloride are grounded to generic cobalt dichloride and nickel dichloride; calcium pantothenate is grounded to the pantothenate anion.

## Evidence

- TOGO M2011 and NBRC Medium 1299 support a 1 L main solution with 30 g NaCl, 0.15 g calcium chloride dihydrate, 0.3 g NH4Cl, 0.75 g magnesium chloride hexahydrate, 1.4 g Na2SO4, 2.5 g sodium thiosulfate pentahydrate, 0.2 g Bacto Yeast Extract, 0.14 g coenzyme M, 1 mg resazurin, 5 ml KP buffer, 2 ml trace elements solution, 2 ml vitamin solution, and variable H2, CO2, and N2 gas.
- The source defines KP buffer as a separate 1 L stock with 119 g KH2PO4 and 21 g K2HPO4.
- The source defines a separate 1 L trace elements solution with NaCl, calcium chloride dihydrate, sodium molybdate dihydrate, boric acid, manganese chloride tetrahydrate, cobalt chloride hexahydrate, nickel chloride hexahydrate, copper chloride dihydrate, zinc chloride, iron chloride hexahydrate, potassium aluminum sulfate dodecahydrate, NTA, sodium tungstate, sodium selenate, and NaOH for pH adjustment.
- The source defines a separate 1 L vitamin solution with nine mg-scale ingredients: biotin, p-aminobenzoic acid, thiamine-HCl, calcium pantothenate, pyridoxine-HCl, folic acid, vitamin B12, riboflavin, and nicotinic acid.
- The source preparation leaves the main pH unadjusted, excludes KP buffer, vitamin solution, Na2CO3, cysteine-HCl, and sodium sulfide nonahydrate from the initial mix, dispenses under H2/CO2, separately autoclaves KP buffer plus 5 percent cysteine and sulfide stocks under N2, filter-sterilizes vitamin and 10 percent Na2CO3 solutions, adds late solutions aseptically and anaerobically before inoculation, and pressurizes inoculated vessels to 150 kPa with H2/CO2.

## Completeness

- Consequentially incomplete: `preparation_steps` are absent even though the source has required anaerobic dispense, separate sterilization, filter-sterilization, late-addition, trace-solution pH, and final pressurization instructions.
- Consequentially incomplete: KP buffer, trace elements solution, and vitamin solution are preserved only as empty `G_PER_L` solution stubs, not as 5 ml, 2 ml, and 2 ml source additions.
- Consequentially incomplete: the KP, trace, and vitamin stock ingredients are also flattened into the top-level final-medium ingredients at stock strength.
- Empty optional target-organism and growth-evidence slots are acceptable for an imported NBRC recipe.
- Bounded searches:
  - `find data/raw/togo data/raw/nbrc -maxdepth 3 -type f -print`, which includes ignored files, found only `data/raw/togo/README.md` and `data/raw/nbrc/README.md`.
  - `rg --no-ignore --hidden -n -F 'Hydrogen-using marine sulfate-reducer medium' data/raw/togo data/raw/nbrc` found no raw TOGO or NBRC payload in this checkout, so the live TOGO API and NBRC page were used as the inspected sources.

## Findings

### Blockers

None found.

### Major

| Finding | Evidence | Maintained owner |
|---|---|---|
| Stock-solution rows are duplicated into the top-level medium at stock strength. | NBRC/TOGO add 5 ml KP buffer, 2 ml trace elements solution, and 2 ml vitamin solution to the main recipe. The generated record also includes all KP, trace, and vitamin stock components as direct final-medium ingredients. | `data/normalized_yaml/bacterial/hydrogen_using_marine_sulfate_reducer_medium.yaml`; TOGO import and solution migration. |
| Milligram quantities became gram-per-liter quantities. | The source lists 1 mg resazurin and mg-scale vitamin rows; the generated record writes the same numeric values as `G_PER_L`. `data/import_tracking/reports/concentration_plausibility.tsv` flags 8 vitamin/indicator unit slips for `CultureMech:008598`. | TOGO quantity normalization for M2011 and vitamin subcomponent import. |
| Duplicate cleanup summed main-medium and trace-stock labels. | The source has 30 g NaCl in the main medium and 1 g in the trace stock, plus 0.15 g calcium chloride in the main medium and 0.1 g in the trace stock. The generated record has unsupported 31.0 and 0.25 g/L rows, both flagged in `data/import_tracking/reports/merged_duplicates.tsv`. | The TOGO M2011 normalized record and duplicate cleanup. |
| Source preparation was omitted. | Essential H2/CO2 dispensing, N2 autoclaving, late anaerobic additions, filter sterilization, and pressurization instructions from NBRC/TOGO are not represented. | TOGO comment import for `data/normalized_yaml/bacterial/hydrogen_using_marine_sulfate_reducer_medium.yaml`. |
| Solution CURIEs point to wrong MediaDive records. | The generated NBRC local trace and vitamin rows are linked to `mediadive.solution:6129` and `mediadive.solution:6241`, whose inspected local compositions are different. | Solution migration for the TOGO M2011 normalized record. |
| Several ingredient groundings lose exact chemical form. | Source cobalt chloride hexahydrate, nickel chloride hexahydrate, and calcium pantothenate are grounded as generic cobalt dichloride, generic nickel dichloride, and `(R)-pantothenate`. | CHEBI enrichment and MediaIngredientMech refresh for TOGO M2011. |

### Minor

None found.

## Recommended Edits

1. Preserve NBRC 1299 `KP buffer*`, `Trace elements solution**`, and `Vitamin solution***` as local stock recipes added at 5 ml, 2 ml, and 2 ml.
2. Move KP, trace, and vitamin stock ingredients out of final-medium `ingredients` and into their intended stock-solution scopes.
3. Keep resazurin and vitamin values in mg or convert them with a `0.001` factor before using grams.
4. Stop summing NaCl and calcium chloride across final and trace-stock boundaries.
5. Import TOGO/NBRC comment paragraphs into ordered preparation steps for initial mixing, anaerobic dispensing, separate N2 autoclaving, filter sterilization, late addition, trace-stock pH adjustment, and H2/CO2 pressurization.
6. Remove the unrelated MediaDive solution CURIEs unless a source-specific crosswalk proves equivalence.
7. Re-ground cobalt chloride hexahydrate, nickel chloride hexahydrate, and calcium pantothenate to exact source forms.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation on the corrected normalized record and the regenerated merged M2011 record.
- Re-run the concentration-plausibility audit for `CultureMech:008598`; the resazurin and vitamin unit-slip rows should be gone.
- Re-run the duplicate-ingredient audit; M2011 should no longer sum main-medium NaCl or calcium chloride with trace-stock rows.
- Manually compare regenerated M2011 with the live TOGO M2011 JSON and NBRC Medium 1299 page, especially the sulfate and thiosulfate rows that distinguish it from the same formulation family.

## Additional Notes

- The source-specific sulfate, thiosulfate, and coenzyme M rows are supported as main-medium ingredients; the curation issue is the treatment of the three reusable-looking but source-local stocks.
- The remaining legacy `mediaingredientmech_term` on `Cysteine-HCl` is lower priority than the unsupported stock flattening, unit conversion, and solution-link defects.

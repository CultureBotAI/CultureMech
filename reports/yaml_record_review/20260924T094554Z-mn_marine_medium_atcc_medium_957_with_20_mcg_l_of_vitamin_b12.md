# YAML Record Review: mn_marine_medium_atcc_medium_957_with_20_mcg_l_of_vitamin_b12

- Repository: CultureMech
- Record: data/merge_yaml/merged/mn_marine_medium_atcc_medium_957_with_20_mcg_l_of_vitamin_b12.yaml
- Started UTC: 2026-09-24T09:44:58Z
- Finished UTC: 2026-09-24T09:45:54Z
- Verdict: needs curation

## Target

Generated bacterial recipe for `CultureMech:009056`, `mn_marine_medium_atcc_medium_957_with_20_mcg_l_of_vitamin_b12`, from `TOGO:M2482`.

The TOGO record points to an ATCC PDF for `MN Marine medium (ATCC Medium 957) with 20 mcg/L of vitamin B12`.

## Validation

Open LinkML validation passed with `No issues found`.

Strict schema-layer validation passed with 0 error rows; `/private/tmp/mn_marine_medium_atcc_medium_957_with_20_mcg_l_of_vitamin_b12.strict.tsv` contained only the header line.

Reference validation passed, but performed 0 checks.

Term validation passed. The run emitted the expected `eutils` / `pkg_resources` deprecation warning before `Validation passed`.

Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries inside generated YAML.

## Identity and Grounding

The medium identity is correct: TOGO `M2482` imports the ATCC PDF recipe named `MN Marine medium (ATCC Medium 957) with 20 mcg/L of vitamin B12`.

Most hydrate-aware salt groundings are chemically plausible, including magnesium sulfate heptahydrate, calcium chloride dihydrate, sodium molybdate dihydrate, manganese chloride tetrahydrate, zinc sulfate heptahydrate, copper sulfate pentahydrate, and cobalt nitrate hexahydrate.

`K2HPO4 x 3 H2O` is grounded only as generic dipotassium hydrogen phosphate, so the phosphate hydrate form is not preserved in the ontology link.

## Evidence

TOGO `M2482` preserves the ATCC PDF as two recipe blocks: a 1 L ATCC Medium 957 base and a separate 1 L `Trace Metals A-5` stock.

The ATCC PDF confirms the base recipe: 0.04 g `MgSO4 x 7H2O`, 0.02 g `CaCl2 x 2H2O`, 0.75 g `NaNO3`, 0.02 g `K2HPO4 x 3H2O`, 3.0 mg citric acid, 3.0 mg ferric ammonium citrate, 0.5 mg EDTA, 0.02 g `Na2CO3`, 1.0 ml `Trace Metals A-5`, 10.0 g Noble agar if needed, 250.0 ml distilled water, and 750.0 ml seawater.

The same ATCC PDF gives the stock recipe for 1 L `Trace Metals A-5`: 2.86 g `H3BO3`, 1.81 g `MnCl2 x 4H2O`, 0.222 g `ZnSO4 x 7H2O`, 0.039 g `Na2MoO4 x 2H2O`, 0.079 g `CuSO4 x 5H2O`, 49.4 mg `Co(NO3)2 x 6H2O`, and 1.0 L distilled water.

The PDF also says that ATCC Medium 957 receives 20 mcg/L vitamin B12 and is adjusted after autoclaving to pH 8.5 with KOH.

## Completeness

The generated YAML includes the base inorganic and organic additions, seawater, distilled water, KOH, agar, and the trace-metal stock rows, but it flattens `Trace Metals A-5` into the top-level ingredient list.

The 20 mcg/L vitamin B12 addition named by the source is absent.

The source pH 8.5 and post-autoclave pH-adjustment instruction are absent from generated structured fields.

No target organism, incubation temperature, atmosphere, or growth evidence is present in TOGO M2482 or the ATCC PDF, so those absences are not defects for this source-only import.

## Findings

1. Needs curation: milligram rows in ATCC Medium 957 were converted to grams per liter without scaling. Ferric ammonium citrate and citric acid are each 3.0 mg in the 1 L base recipe, but both are stored as `3 G_PER_L`; EDTA is 0.5 mg and is stored as `0.5 G_PER_L`.

2. Needs curation: `Trace Metals A-5` was flattened without the 1 ml/L dilution. The stock contains gram-per-liter boric acid, manganese, zinc, molybdate, and copper rows, but only 1 ml of that stock is added to the final liter, so those final concentrations should be 1000 times lower than the stock concentrations if flattened.

3. Needs curation: the cobalt nitrate stock row has a second unit error. `Co(NO3)2 x 6H2O` is 49.4 mg in the 1 L stock, but is stored as `49.4 G_PER_L` in the final medium, making it 1,000,000 times too high relative to a 1 ml stock addition.

4. Needs curation: the 20 mcg/L vitamin B12 supplement named in the source medium is missing entirely.

5. Needs curation: the generated record collapses 250 ml final-medium distilled water with 1 L trace-metal-stock water into `251.0 G_PER_L`, losing both the volume unit and the stock hierarchy.

6. Minor: pH 8.5 and the instruction to adjust pH after autoclaving with KOH are missing, and KOH is represented as a variable ingredient rather than only as a pH-adjustment reagent.

## Recommended Edits

Re-curate `data/normalized_yaml/bacterial/mn_marine_medium_atcc_medium_957_with_20_mcg_l_of_vitamin_b12.yaml`, or fix the TOGO importer, so `Trace Metals A-5` is represented as a local nested stock added at 1 ml per liter.

Keep source milligram units for citric acid, ferric ammonium citrate, EDTA, and stock cobalt nitrate; if the representation requires final concentrations, explicitly scale the 1 ml stock addition.

Add the 20 mcg/L vitamin B12 supplement as an ingredient.

Preserve pH 8.5 and the post-autoclave KOH adjustment instruction.

Revisit the `K2HPO4 x 3H2O` ontology link; if no hydrate-specific CHEBI term is available, leave the source hydrate explicit rather than implying an anhydrous salt.

## Follow-up Checks

Re-run open LinkML, strict, reference, and term validation after any normalized-record edits.

Manually compare the regenerated YAML to the ATCC PDF text, because every milligram row and every nested-stock row has a high-risk unit conversion.

Check other ATCC/TOGO records with `Trace Metals A-5` cross-references for the same stock-flattening and cobalt milligram-to-gram error.

## Additional Notes

No GitHub issues or PR comments were created by this record review.

Exact source-record searches used `find` or `rg --no-ignore --hidden`, so ignored files were included.

# YAML Record Review: Clostridium (GV) Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_gv_medium.yaml`
- Started UTC: `2026-09-22T09:14:45Z`
- Finished UTC: `2026-09-22T09:15:28Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:009051` for TOGO Medium `M2475`, generated from `data/normalized_yaml/bacterial/TOGO_M2475_Clostridium_GV_Medium.yaml` on merge fingerprint `0aee3891e8cb39da36c12c3d66f9025aa7cbc3e068f5d16ea615faa46d8ce4be`.

The stated source is DSMZ Medium 500, `CLOSTRIDIUM (GV) MEDIUM`, via `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium500.pdf`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no rows in `/private/tmp/clostridium_gv_medium.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The record identity is recognizable as a TOGO import of DSMZ Medium 500, but it is not a faithful standalone CultureMech record yet. The same DSMZ 500 source is represented in the direct MediaDive/KOMODO branch `data/merge_yaml/merged/clostridium_gv_medium__dbc14635.yaml`, so the corrected record should either merge into that branch or be split into explicit DSMZ 500 variants rather than remaining a second generic `clostridium_gv_medium` recipe.

Most hydrate groundings on the base formula are chemically specific, but `NiCl2 x 6 H2O` is still grounded to generic `CHEBI:34887` / nickel dichloride even though the source and preferred term identify the hexahydrate. The Vitamin solution entry also names a generic `Vitamin solution` and points to `mediadive.solution:6241`, while the DSMZ source specifies `Wolin's vitamin solution (10x)`.

## Evidence

The TOGO API confirms that `M2475` is `Clostridium (GV) Medium`, has pH `7.0 - 7.2`, and cites the DSMZ Medium 500 PDF as its source. Its JSON also preserves DSMZ's stock structure: a one-liter base receives 0.5 ml Na-resazurin, 2 ml FeSO4, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, and a vitamin-solution aliquot; the trace, selenite-tungstate, and vitamin formulas are separate subcomponents.

The DSMZ PDF confirms the base medium plus three separate stock formulas. The base recipe contains 1000 ml distilled water, 5 g D-glucose, 0.5 ml 0.1% sodium resazurin, 2 ml 0.1% FeSO4 in 0.1 N H2SO4, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, and 1 ml Wolin's vitamin solution (10x). The PDF's variant notes replace glucose with 2 g/l sodium crotonate for DSM 5704, replace glucose with 6 g/l trisodium citrate for DSM 6222, adjust complete-medium pH to 6.5-6.7 for DSM 9179, and reduce glucose to 2 g/l for DSM 9187 and DSM 10612.

## Completeness

This record is missing several structured source facts:

- `ph_range` should capture 7.0-7.2 from TOGO and DSMZ.
- The anoxic preparation is absent: dissolve the starting ingredients except bicarbonate, magnesium sulfate, calcium chloride, glucose, vitamins, cysteine, and sulfide; sparge with 80% N2 / 20% CO2 for 30-45 min; add bicarbonate; adjust to pH 7.0; dispense under 80% N2 / 20% CO2; autoclave; then add sterile anoxic MgSO4, CaCl2, glucose, cysteine, and sulfide stocks plus filter-sterilized vitamins.
- DSMZ 5704, 6222, 9179, 9187, and 10612 variant instructions are absent as structured media variants.
- The stock recipes are flattened into parent `ingredients` instead of being kept as `solutions[*].composition`.

## Findings

- The 1000 ml base water, 990 ml Trace element solution SL-10 water, 1000 ml Selenite-tungstate water, and 1000 ml Wolin vitamin water were merged into one parent `Distilled water` row at `3990.0 G_PER_L`. These are different solutions and must not be summed into the final medium.
- Trace element stock internals were copied into the parent ingredient list with milligram values converted to grams per liter. Examples include `ZnCl2` at `70 G_PER_L`, `MnCl2 x 4 H2O` at `100 G_PER_L`, `CoCl2 x 6 H2O` at `190 G_PER_L`, and `NiCl2 x 6 H2O` at `24 G_PER_L`, while DSMZ lists 70 mg, 100 mg, 190 mg, and 24 mg in a one-liter stock that is dosed at only 1 ml/l of final medium.
- Selenite-tungstate internals have the same defect: `Na2SeO3 x 5 H2O` and `Na2WO4 x 2 H2O` are stored as `3` and `4 G_PER_L` parent ingredients instead of 3 mg and 4 mg per liter of a stock used at 1 ml/l.
- Vitamin stock internals were flattened from Wolin's vitamin solution into parent gram-per-liter nutrients. `Biotin 2 G_PER_L`, `p-Aminobenzoic acid 5 G_PER_L`, `Thiamine-HCl 5 G_PER_L`, `Pyridoxine-HCl 10 G_PER_L`, and related rows represent stock mg/l values shifted by three orders of magnitude.
- The migrated `solutions` array has empty compositions and stores source milliliter aliquots as `G_PER_L` values, including `Na-resazurin solution (0.1% w/v)` at `0.5 G_PER_L`, `FeSO4 x 7H2O solution` at `2 G_PER_L`, `Trace element solution SL-10` at `1 G_PER_L`, `Selenite-tungstate solution` at `1 G_PER_L`, and `Vitamin solution` at `10 G_PER_L`.
- `D-Glucose` is stored as `2 G_PER_L` in a generic DSMZ 500 record. DSMZ Medium 500's base recipe uses 5 g/l glucose, and 2 g/l glucose is only a strain-specific variant for DSM 9187 and DSM 10612.
- The parent formula includes `N2` and `Carbon dioxide gas` as variable-concentration ingredients rather than representing the 80% N2 / 20% CO2 dispensing atmosphere and the 100% N2 stock-atmosphere instructions as preparation conditions.
- `high_metal: true` appears to be an artifact of copying concentrated trace-metal stock internals into the final medium.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/TOGO_M2475_Clostridium_GV_Medium.yaml` or the TOGO stock import logic, then regenerate; `data/merge_yaml/merged/clostridium_gv_medium.yaml` is derived.
- Preserve DSMZ Medium 500 as a base formula with 5 g/l D-glucose and separate solution aliquots for resazurin, FeSO4, Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution.
- Move Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution internals into `solutions[*].composition` using their true stock units.
- Store source milliliter additions as volume aliquots rather than as grams per liter.
- Add structured pH and anaerobic preparation fields from the DSMZ PDF.
- Model the DSMZ strain-specific modifications as media variants instead of overwriting the base glucose amount.
- Re-ground `NiCl2 x 6 H2O` to a nickel chloride hexahydrate term.
- Re-run the merge and confirm that the corrected TOGO and direct DSMZ/KOMODO branches no longer produce two generic `clostridium_gv_medium` generated records unless they intentionally represent separate named variants.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Compare the regenerated formula against the DSMZ Medium 500 PDF to ensure only 1000 ml base water remains in the parent recipe and that each stock recipe has its own stock water.
- Confirm no trace-element, selenite-tungstate, or vitamin stock internal is present as a final parent ingredient unless it has been correctly diluted through its aliquot.
- Confirm the glucose 2 g/l case is attached only to DSM 9187 / DSM 10612 variant metadata.
- Confirm `high_metal` is unset after stock internals are no longer flattened into the parent formula.

## Additional Notes

Empty optional fields are not defects. The critical issue is that the TOGO import collapsed nested stock context into a flat parent formula, so downstream consumers would read concentrated stock recipes as final medium ingredients.

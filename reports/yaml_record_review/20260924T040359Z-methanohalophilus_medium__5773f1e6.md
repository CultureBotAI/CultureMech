# YAML Record Review: methanohalophilus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanohalophilus_medium__5773f1e6.yaml
- Started UTC: 2026-09-24T04:03:59Z
- Finished UTC: 2026-09-24T04:08:22Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:008606` / `methanohalophilus_medium`, produced from one normalized NBRC-via-TOGO import:

- `data/normalized_yaml/archaea/TOGO_M2019_Methanohalophilus_Medium.yaml`
- `merged_from`: `TOGO_M2019_Methanohalophilus_Medium`
- `merge_fingerprint`: `5773f1e681ffcde43d804b002a33009051b2fb8c180c5106ed90d1e8e3a25394`
- Upstream identity: TOGO Medium `M2019`, original source `NBRC_M1308`

## Validation

- LinkML open validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 error rows in `/private/tmp/methanohalophilus_medium__5773f1e6.strict.tsv`.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The generated record keeps the expected CultureMech identifier, TOGO `M2019` medium term, NBRC `M1308` source note, and single-source merge fingerprint. NBRC `NO=1308` is still retrievable and matches the TOGO `M2019` component structure.

The normalized owner has the same post-merge duplicate-water repair seen in adjacent NBRC imports: its three identical 1 L water rows have been collapsed to one `1.0` row, while the generated merge still has the stale `3.0` sum. The owner still needs stock reconstruction, solution-reference cleanup, and cross-scope duplicate repair before the generated merge is refreshed.

## Evidence

- NBRC `M1308` lists a 1 L main solution with 0.136 g `KH2PO4`, 0.54 g `NH4Cl`, 3.05 g `MgCl2 x 6 H2O`, 0.147 g `CaCl2 x 2 H2O`, 20 g NaCl, 1.2 g trimethylamine-HCl, 2.52 g `NaHCO3`, 2 ml Vitamin solution, 1 ml Trace element solution, 1 mg resazurin, 0.5 g cysteine-HCl, 0.5 g `Na2S x 9 H2O`, and 1 L distilled water.
- The NBRC Vitamin solution is a 1 L stock with biotin, folic acid, pyridoxine-HCl, thiamine-HCl, riboflavin, nicotinic acid, calcium pantothenate, p-aminobenzoic acid, vitamin B12, and distilled water.
- The NBRC Trace element solution is a 1 L stock with nitrilotriacetic acid, `FeCl3 x 6 H2O`, `MnCl2 x 4 H2O`, `CoCl2 x 6 H2O`, `CaCl2 x 2 H2O`, `ZnCl2`, `CuCl2 x 2 H2O`, `H3BO3`, `Na2MoO4 x 2 H2O`, NaCl, `NiCl2 x 6 H2O`, `Na2SeO4`, `Na2WO4`, distilled water, and NaOH used to set stock pH.
- NBRC instructs autoclaving the base without vitamin solution, cysteine-HCl, or `Na2S x 9H2O` under 80/20 `N2`/`CO2`; separately autoclaving 5% cysteine-HCl and 5% sodium-sulfide solutions under `N2`; filter-sterilizing the vitamin solution; and adding vitamin, cysteine-HCl, and `Na2S x 9H2O` prior to inoculation.
- MediaDive solution `6187`, which the YAML names as the trace-element stock, is an EDTA/Fe/Mn/Zn/Co/Mo formulation and lacks the NBRC stock's NTA, sodium chloride, calcium, copper, nickel, selenate, and tungstate rows.

## Completeness

The main NBRC salt and reducing rows are present. The generated record cannot reconstruct the source medium because the 2 ml vitamin and 1 ml trace-element stock additions are empty placeholders while their source stock components were flattened into final ingredient rows, diluted stock rows were summed with main rows, and the anaerobic/filter-sterile preparation workflow was not preserved.

## Findings

- The trace-element placeholder points to the wrong external stock. NBRC `M1308` defines a local NTA-based stock that includes calcium chloride, copper chloride, nickel chloride, selenate, and tungstate, but the YAML links `Trace element solution**` to generic MediaDive solution `6187`.
- The vitamin placeholder repeats the same wrong generic mapping as neighboring NBRC imports: `Vitamin solution*` points to MediaDive `6241`, whose three-component 100 ml recipe does not match the embedded 1 L NBRC vitamin recipe.
- Stock contents were flattened and mis-scaled into final medium. The YAML stores 10 mg pyridoxine-HCl as `10 G_PER_L`, 0.01 mg vitamin B12 as `0.01 G_PER_L`, and the trace stock's NTA and ferric chloride as direct final-medium rows even though only 1 ml of the trace stock is added.
- Duplicate cleanup crossed stock boundaries. Main NaCl 20 g and trace-stock NaCl 1 g were summed into `21.0 G_PER_L`, and main `CaCl2 x 2 H2O` 0.147 g was summed with trace-stock 0.1 g to form `0.247 G_PER_L`.
- The generated water row is stale and dimensionally wrong: three independent 1 L solvent rows were summed into `3.0 G_PER_L`; the owner now collapses the duplicate row, but still represents a source liter as a gram-per-liter amount.
- `CoCl2 x 6H2O` is grounded to anhydrous `CHEBI:35696`, and `Cysteine-HCl` still carries the legacy `mediaingredientmech_term` field instead of a CHEBI-keyed link.
- Preparation semantics are absent. The source's 80/20 `N2`/`CO2` base autoclave, 5% cysteine-HCl and 5% sulfide stocks under `N2`, filter-sterile vitamin solution, prior-to-inoculation additions, and trace-stock pH order are not represented.

## Recommended Edits

- Replace the incorrect MediaDive `6241` and `6187` links with local structured NBRC `Vitamin solution` and `Trace element solution` definitions from NBRC `M1308` / TOGO `M2019`.
- Preserve the source main-formula invocations as 2 ml/L Vitamin solution and 1 ml/L Trace element solution.
- Keep stock ingredients scoped to their stock solutions, or compute final concentrations by applying the 2 ml/L and 1 ml/L dilutions without deleting the stock hierarchy.
- Keep main, vitamin-stock, and trace-stock water separate; do not sum NaCl or calcium chloride across main and trace formulas.
- Correct cobalt chloride hexahydrate and cysteine-HCl link fields.
- Reattach the NBRC anaerobic/autoclave/filter-sterile preparation instructions to the normalized recipe.
- Regenerate `data/merge_yaml/merged/methanohalophilus_medium__5773f1e6.yaml` from the curated normalized owner.

## Follow-up Checks

- Re-run open, strict, reference, and term validation after regeneration.
- Compare the regenerated record against NBRC `M1308` and TOGO `M2019`, confirming that `Na2WO4` and `Na2SeO4` remain inside the local trace stock.
- Verify that no generic MediaDive solution cross-reference remains unless it is formula-identical to the NBRC stock.

## Additional Notes

None found

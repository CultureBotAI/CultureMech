# YAML Record Review: methanohalobium_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanohalobium_medium__eb221141.yaml
- Started UTC: 2026-09-24T04:01:36Z
- Finished UTC: 2026-09-24T04:05:40Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:008486` / `methanohalobium_medium`, produced from one normalized NBRC-via-TOGO import:

- `data/normalized_yaml/archaea/TOGO_M1909_Methanohalobium_medium.yaml`
- `merged_from`: `TOGO_M1909_Methanohalobium_medium`
- `merge_fingerprint`: `eb2211419dd3ba19cf0f60e1972138db01bdee0a53b6d88dcf131910d6bed0c5`
- Upstream identity: TOGO Medium `M1909`, original source `NBRC_M1169`

## Validation

- LinkML open validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 error rows in `/private/tmp/methanohalobium_medium__eb221141.strict.tsv`.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The generated record keeps the expected CultureMech identifier, TOGO `M1909` medium term, NBRC `M1169` source note, and single-source merge fingerprint. Its source page is still retrievable from NBRC medium detail page `NO=1169` and agrees with the TOGO `M1909` payload.

The normalized owner has one repair that is absent from the generated merge: `Distilled water` was collapsed back from three duplicate `1.0` values to one `1.0` value on 2026-09-02. The owner still has the wrong gram-per-liter water unit, the summed NaCl and calcium chloride duplicate rows, flattened vitamin and trace stocks, and empty solution stubs, so it needs more curation before this generated file is refreshed.

## Evidence

- NBRC `M1169` lists a 1 L main solution with 0.33 g `NH4Cl`, 0.33 g `KH2PO4`, 0.33 g KCl, 0.33 g `CaCl2 x 2 H2O`, 0.33 g `MgCl2 x 6 H2O`, 4 g `MgSO4 x 7 H2O`, 250 g NaCl, 0.142 g Coenzyme M, 0.5 g Bacto Yeast Extract (Difco), 10 ml Vitamin solution, 1 ml Trace elements solution, 5 g trimethylamine-HCl, 1 mg resazurin, 5 g `NaHCO3`, 0.5 g `Na2S x 9 H2O`, and 1 L distilled water.
- The NBRC Vitamin solution is a local 1 L stock with biotin, folic acid, pyridoxine-HCl, thiamine-HCl, riboflavin, nicotinic acid, calcium pantothenate, p-aminobenzoic acid, vitamin B12, and distilled water.
- The NBRC Trace elements solution is a local 1 L stock with nitrilotriacetic acid, `FeCl3 x 6 H2O`, `MnCl2 x 4 H2O`, `CoCl2 x 6 H2O`, `CaCl2 x 2 H2O`, `ZnCl2`, `CuCl2 x 2 H2O`, `H3BO3`, `Na2MoO4 x 2 H2O`, NaCl, `NiCl2 x 6 H2O`, distilled water, and NaOH used to set the stock pH.
- NBRC instructs autoclaving the base without vitamin solution, trimethylamine-HCl, `NaHCO3`, or `Na2S x 9H2O` under an 80/20 `N2`/`CO2` atmosphere; separately autoclaving a 5% sulfide solution under `N2`; adding filter-sterile vitamin, 50% trimethylamine-HCl, 5% `NaHCO3`, and sulfide prior to inoculation; and adjusting final pH to 7.4 with filter-sterile 5% `Na2CO3`.
- MediaDive solutions `6241` and `6129`, which are named in the YAML placeholders, do not match these NBRC stock formulas: `6241` contains only cyanocobalamine, thiamine HCl, biotin, and 100 ml water, while `6129` is a five-component sulfate/nitrate trace solution.

## Completeness

The main NBRC salts and organic nutrients are present. The record is not complete enough to use because two NBRC-local stock formulas have been flattened into the main ingredient list, three solution additions are empty `Unknown solution` records, two duplicate stock components were summed with main components, and all preparation instructions were dropped.

## Findings

- The two named stock additions point to the wrong formulas. `Vitamin solution*` points to `mediadive.solution:6241`, and `Trace elements solution**` points to `mediadive.solution:6129`; neither MediaDive stock matches the formulas embedded in NBRC `M1169`, so following the YAML notes would reconstruct the wrong medium.
- Stock ingredients were flattened into final ingredients with the wrong units and dilution. The 1 ml/L trace stock and 10 ml/L vitamin stock should be represented as stock additions; instead, the YAML stores NBRC stock recipe amounts such as 10 mg pyridoxine-HCl as `10 G_PER_L`, 0.01 mg vitamin B12 as `0.01 G_PER_L`, and 12.8 g nitrilotriacetic acid as `12.8 G_PER_L` in the final medium.
- Cleanup merged components across formula scopes. The generated record stores NaCl as `251.0 G_PER_L` from a 250 g main-medium row plus a 1 g trace-stock row, and `CaCl2 x 2 H2O` as `0.43000000000000005 G_PER_L` from a 0.33 g main row plus a 0.1 g trace-stock row.
- The generated merge is stale after a normalized-source repair. `data/normalized_yaml/archaea/TOGO_M1909_Methanohalobium_medium.yaml` now collapses the three 1 L water rows to one row, but `data/merge_yaml/merged/methanohalobium_medium__eb221141.yaml` still has `3.0 G_PER_L` water from the old duplicate sum.
- The `Na2CO3 solution` placeholder is empty and volume-free. NBRC specifies a filter-sterile 5% `Na2CO3` solution only for pH adjustment, with approximately 0.5 g/L final `Na2CO3`; the generated record has an `Unknown solution` with `VARIABLE` concentration and no preparation context.
- The `CoCl2 x 6H2O` ingredient is grounded to `CHEBI:35696` cobalt dichloride instead of a hexahydrate term and is missing a `mediaingredientmech_chebi_term`, unlike its neighboring stock salts.
- The anaerobic handling instructions were discarded. The NBRC formula differentiates 80/20 `N2`/`CO2` base autoclaving, 5% sulfide under `N2`, filter-sterile vitamin/trimethylamine/bicarbonate additions, final carbonate pH adjustment, and trace-stock pH preparation; none of that is present in the YAML.

## Recommended Edits

- Replace the incorrect MediaDive `6241` and `6129` links with local structured NBRC `Vitamin solution` and `Trace elements solution` blocks from TOGO/NBRC `M1909`.
- Restore main-formula stock additions as 10 ml/L Vitamin solution, 1 ml/L Trace elements solution, filter-sterile 50% trimethylamine-HCl, filter-sterile 5% `NaHCO3`, separately autoclaved 5% `Na2S x 9H2O`, and pH-adjusting 5% `Na2CO3`.
- Remove top-level rows that came from vitamin and trace stock components, or retain them only as dilution-derived final concentrations clearly generated from the structured stocks.
- Preserve main-medium, vitamin-stock, and trace-stock water in separate scopes and prevent duplicate cleanup from summing NaCl or calcium chloride across those scopes.
- Correct `CoCl2 x 6H2O` grounding to cobalt chloride hexahydrate and restore the `mediaingredientmech_chebi_term`.
- Reattach the NBRC preparation paragraph and the trace-elements pH note to the normalized record.
- Regenerate `data/merge_yaml/merged/methanohalobium_medium__eb221141.yaml` from the curated normalized owner.

## Follow-up Checks

- Re-run open, strict, reference, and term validation after regeneration.
- Compare the regenerated record against NBRC `M1169` and TOGO `M1909`, confirming that the 10 ml vitamin addition, 1 ml trace addition, and pH-only carbonate adjustment have the correct scopes.
- Verify that no MediaDive solution cross-reference remains unless it points to a stock with the same formula as the embedded NBRC stock.

## Additional Notes

None found

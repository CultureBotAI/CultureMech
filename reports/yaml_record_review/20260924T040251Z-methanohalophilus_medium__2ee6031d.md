# YAML Record Review: methanohalophilus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanohalophilus_medium__2ee6031d.yaml
- Started UTC: 2026-09-24T04:02:51Z
- Finished UTC: 2026-09-24T04:07:04Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:008488` / `methanohalophilus_medium`, produced from one normalized NBRC-via-TOGO import:

- `data/normalized_yaml/archaea/TOGO_M1910_Methanohalophilus_medium.yaml`
- `merged_from`: `TOGO_M1910_Methanohalophilus_medium`
- `merge_fingerprint`: `2ee6031dc69c35391d02410b93616bb30d6d5a14fcacd1daf0b60119ca6e4b1b`
- Upstream identity: TOGO Medium `M1910`, original source `NBRC_M1170`

## Validation

- LinkML open validation: Passed; printed `No issues found`.
- Strict validation: Passed with 0 error rows in `/private/tmp/methanohalophilus_medium__2ee6031d.strict.tsv`.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The generated record keeps the expected CultureMech identifier, TOGO `M1910` medium term, NBRC `M1170` source note, and single-source merge fingerprint. The NBRC `NO=1170` page is still retrievable and matches the TOGO `M1910` component structure.

The normalized owner has a post-merge duplicate repair that is absent from the generated file: `Distilled water` has been reduced from `3.0` to `1.0` after the three identical water rows were collapsed. The owner still retains the wrong water unit, cross-scope NaCl and calcium chloride sums, flattened stock components, incorrect MediaDive solution links, and ontology grounding errors.

## Evidence

- NBRC `M1170` lists 0.33 g each of `NH4Cl`, `KH2PO4`, KCl, `CaCl2 x 2 H2O`, and `MgCl2 x 6 H2O`; 0.01 g `K2SO4`; 70 g NaCl; 10 ml Vitamin solution; 10 ml Trace elements solution; 0.05 g Bacto Yeast Extract (Difco); 5 g methylamine-HCl; 1 mg resazurin; 5 g `NaHCO3`; 0.3 g cysteine-HCl; 0.15 g `Na2S x 9 H2O`; and 1 L distilled water.
- The NBRC Vitamin solution is a 1 L stock with biotin, folic acid, pyridoxine-HCl, thiamine-HCl, riboflavin, nicotinic acid, calcium pantothenate, p-aminobenzoic acid, vitamin B12, and distilled water.
- The NBRC Trace elements solution is a 1 L stock with nitrilotriacetic acid, `FeCl3 x 6 H2O`, `MnCl2 x 4 H2O`, `CoCl2 x 6 H2O`, `CaCl2 x 2 H2O`, `ZnCl2`, `CuCl2 x 2 H2O`, `H3BO3`, `Na2MoO4 x 2 H2O`, NaCl, `NiCl2 x 6 H2O`, distilled water, and NaOH used to set the stock pH.
- NBRC instructs autoclaving the base without vitamin solution, `NaHCO3`, cysteine-HCl, or `Na2S x 9 H2O` under 80/20 `N2`/`CO2`; separately autoclaving 3% cysteine-HCl and 1.5% sodium-sulfide solutions under `N2`; adding filter-sterile vitamin and 5% `NaHCO3` before inoculation; and ending at approximately pH 7.2.
- The generic MediaDive `Vitamin solution` `6241` and `Trace elements solution` `6129` records named by the placeholders do not match the embedded NBRC stocks.

## Completeness

The main NBRC salts, methylamine substrate, yeast extract, and reducing-agent masses are present. The record is not complete enough for reconstruction because the vitamin and trace stocks are both flattened and replaced with empty `Unknown solution` placeholders, stock components are indistinguishable from final main-medium ingredients, and all NBRC preparation instructions were lost.

## Findings

- The two stock placeholders point to wrong external solution records. `Vitamin solution*` is linked to MediaDive `6241`, and `Trace elements solution**` is linked to MediaDive `6129`; both formulas differ from the vitamin and trace recipes embedded in NBRC `M1170`.
- Vitamin-stock amounts were converted from milligrams in a 1 L stock to gram-per-liter final-medium rows. Examples include 10 mg pyridoxine-HCl stored as `10 G_PER_L`, 5 mg thiamine-HCl stored as `5 G_PER_L`, and 0.01 mg vitamin B12 stored as `0.01 G_PER_L`.
- Trace-stock amounts were flattened into the final ingredient list and then partially merged with main-medium ingredients. The generated record sums main NaCl 70 g with trace-stock NaCl 1 g as `71.0 G_PER_L`, and main `CaCl2 x 2 H2O` 0.33 g with trace-stock `CaCl2 x 2 H2O` 0.1 g as `0.43000000000000005 G_PER_L`.
- The generated water row is stale and dimensionally wrong. It still stores `3.0 G_PER_L` from three separate 1 L solvent rows; the normalized owner now collapses this to one row, but that row still stores a source liter as a gram-per-liter concentration.
- The source methylamine-HCl row is grounded as `CHEBI:64700` trimethylamine hydrochloride, a different methylamine salt.
- `CoCl2 x 6H2O` is grounded to `CHEBI:35696` cobalt dichloride instead of a hexahydrate term, and `Cysteine-HCl` still carries a legacy `mediaingredientmech_term` even though the record history says legacy links were migrated.
- Anaerobic preparation semantics are missing: the 80/20 `N2`/`CO2` base autoclave, 3% cysteine-HCl under `N2`, 1.5% sulfide under `N2`, filter-sterile vitamin and 5% bicarbonate additions, trace-stock pH workflow, and final pH 7.2 are all absent from the generated YAML.

## Recommended Edits

- Replace the incorrect MediaDive `6241` and `6129` links with local structured NBRC `Vitamin solution` and `Trace elements solution` definitions from NBRC `M1170` / TOGO `M1910`.
- Preserve the main-formula stock invocations as 10 ml/L Vitamin solution and 10 ml/L Trace elements solution instead of flattening their child ingredients into the main list.
- Keep vitamin-stock water, trace-stock water, and main-medium water scoped separately; prevent duplicate cleanup from summing NaCl or calcium chloride across those scopes.
- Correct the methylamine-HCl, cobalt chloride hexahydrate, and cysteine-HCl ontology/link fields.
- Reattach the NBRC preparation paragraph, including the filter-sterile 5% bicarbonate addition, 3% cysteine-HCl and 1.5% sulfide solutions, anaerobic gas atmospheres, and approximate pH 7.2.
- Regenerate `data/merge_yaml/merged/methanohalophilus_medium__2ee6031d.yaml` from the curated normalized owner.

## Follow-up Checks

- Re-run open, strict, reference, and term validation after regeneration.
- Compare the regenerated record against NBRC `M1170` and TOGO `M1910`, confirming that both 10 ml stock additions have the correct local stock formulas.
- Confirm that no generic MediaDive solution cross-reference remains unless it is formula-identical to the NBRC stock.

## Additional Notes

None found

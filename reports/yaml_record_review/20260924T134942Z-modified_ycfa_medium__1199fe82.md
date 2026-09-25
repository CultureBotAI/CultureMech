# YAML Record Review: modified_ycfa_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_ycfa_medium__1199fe82.yaml
- Started UTC: 2026-09-24T13:49:06Z
- Finished UTC: 2026-09-24T13:49:42Z
- Verdict: needs curation

## Target

Reviewed merged generated record `CultureMech:009545`, `modified_ycfa_medium`, a liquid undefined bacterial recipe imported from TOGO `M3033` / JCM `M1407`.

## Validation

The generated record passed the focused open schema validator; it exited 0 with no diagnostics.

Strict validation passed with 0 errors. The TSV output contained only its header row.

Reference validation passed. The checker executed 0 reference checks for this record.

Term validation passed. The validator emitted the known `eutils` / `pkg_resources` warning before reporting success.

Embedded `curation_history` entries were not checked: `just validate-history` validates standalone `history/` content, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The TOGO identity is correct. TOGO `M3033` resolves to `Modified YCFA Medium`, original media id `JCM_M1407`, JCM `GRMD=1407`, and pH 8.0.

The external source is a derivative recipe. Live JCM medium 1407 says to use JCM medium 1130, `YCFA MEDIUM`, and adjust pH to 8.0. TOGO `M1210` is the corresponding import of JCM `M1130`.

The six generated solution rows are only cross-reference placeholders for M1210 stocks. Each has `composition: []`, `name: Unknown solution`, and a gram-per-liter unit for a milliliter dose. The record also flattens every M1210 stock component into the final ingredient list, so the cross-reference boundary is not preserved.

Several groundings need repair. `L-Cysteine-HCl-H2O` has no structured term; the `n--Valeric acid`, `iso--Valeric acid`, and `iso--Butyric acid` rows still use deprecated `mediaingredientmech_term` values; `Pyridoxine-HCl` and `Thiamine-HCl` have primary CHEBI terms but lack `mediaingredientmech_chebi_term` links.

## Evidence

The live JCM 1407 page names the source `MODIFIED YCFA MEDIUM`, references medium 1130, and states `Adjust pH to 8.0`.

The live JCM 1130 page defines the YCFA base: 10 g tryptone, 2.5 g yeast extract, 4 g NaHCO3, 2 g glucose, 2 g maltose, 2 g cellobiose, 1 g L-Cysteine-HCl-H2O, 150 ml Mineral solution I, 150 ml Mineral solution II, 1 mg resazurin, 6.2 ml VFA mix, 10 ml Hemin solution, 1 ml Vitamin solution I, and 660 ml distilled water. It adjusts pH to 7.45, then adds 1 ml filter-sterilized Vitamin solution II after autoclaving.

JCM 1130 also defines the inherited stocks. Mineral solution I is 3 g K2HPO4 in 1 L water. Mineral solution II is 3 g KH2PO4, 6 g ammonium sulfate, 6 g NaCl, 0.6 g MgSO4 x 7 H2O, and 0.6 g CaCl2 x 2 H2O in 1 L water. VFA mix contains 17 ml acetic acid, 6 ml propionic acid, 1 ml n-valeric acid, 1 ml iso-valeric acid, 1 ml iso-butyric acid, and 26 ml 10 N NaOH. Hemin solution contains 0.28 g KOH, 25 ml ethanol, 0.1 g hemin, and enough water to reach 100 ml. Vitamin solution I contains Biotin, Vitamin B12, p-Aminobenzoic acid, Folic acid, and Pyridoxine-HCl in 500 ml water; Vitamin solution II contains Thiamine-HCl and Riboflavin in 500 ml water.

The TOGO `M3033` API expands the JCM 1130 base into the Modified YCFA source with the same six stock doses and stock compositions, adds comments to adjust pH to 8.0, and preserves the after-autoclave filter-sterilized 1 ml Vitamin solution II instruction.

## Completeness

The generated top-level recipe is structurally incomplete. It has the six stock additions, but their doses are incorrectly encoded as `G_PER_L` values, and their compositions are empty.

The generated final ingredient list is over-complete in the wrong scope. Mineral solution I, Mineral solution II, VFA mix, Hemin solution, and both vitamin stocks should be nested inherited stocks, but their ingredients were promoted to top-level final-medium ingredients at stock recipe concentrations.

The generated `Distilled water` value is not meaningful because it sums the 660 ml main water, both 1 L mineral-stock solvents, 100 ml hemin-stock solvent, and both 500 ml vitamin-stock solvents into `1762.0 G_PER_L`.

## Findings

1. The six inherited M1210 stock additions are represented as empty `Unknown solution` placeholders with `G_PER_L` units. Their source doses are 150 ml, 150 ml, 6.2 ml, 10 ml, 1 ml, and 1 ml.

2. All inherited stock ingredients were flattened into final-medium ingredients at stock concentrations, including mineral salts, VFA acids, 10 N NaOH, KOH, ethanol, hemin, and vitamins.

3. Stock and main solvent volumes were summed into `Distilled water: 1762.0 G_PER_L`, which mixes milliliters and liters from unrelated scopes.

4. `Resazurin` is 1 mg in JCM/TOGO, but the generated record serializes it as `1 G_PER_L`.

5. The pH 8.0 modification from JCM 1407 is not modeled, and neither is the post-autoclave addition of filter-sterilized Vitamin solution II inherited from JCM 1130.

6. Branched VFA components and L-Cysteine-HCl-H2O need grounding cleanup: the VFA rows still carry legacy MediaIngredientMech ids, and the cysteine monohydrate has no structured ontology term.

## Recommended Edits

Represent `modified_ycfa_medium` as a derivative of YCFA medium M1210 / JCM 1130 with pH changed to 8.0, preserving the live JCM 1407 source note.

Replace the six empty solution placeholders with structured stock references or nested local copies of Mineral solution I, Mineral solution II, VFA mix, Hemin solution, Vitamin solution I, and Vitamin solution II from M1210.

Keep stock-only ingredients inside those stock definitions and record only the six milliliter stock doses in the final recipe.

Correct main-recipe quantities that were converted from milligram or milliliter source rows, especially `Resazurin`, all VFA liquids, Hemin solution solvent rows, and vitamin stock milligram rows.

Add preparation metadata for final pH 8.0 and the post-autoclave filter-sterilized Vitamin solution II addition.

Ground `L-Cysteine-HCl-H2O`, migrate VFA legacy MediaIngredientMech ids to CHEBI keying, and add missing CHEBI-keyed links for `Pyridoxine-HCl` and `Thiamine-HCl`.

## Follow-up Checks

After editing `data/normalized_yaml/bacterial/modified_ycfa_medium.yaml` or the TOGO derivative merge logic, regenerate the merged YAML and rerun open schema, strict, reference, and term validation.

Recompare the generated record against live JCM `GRMD=1407`, live JCM `GRMD=1130`, TOGO `M3033`, and TOGO `M1210`: the only semantic change from YCFA should be final pH 8.0.

Check `YCFA_MEDIUM.yaml` from TOGO `M1210` and the JCM-derived YCFA with mannitol record for the same stock-flattening pattern before changing shared import logic.

## Additional Notes

An exact, ignored-file-inclusive search for `TOGO:M3033`, `M3033`, `JCM_M1407`, and `GRMD=1407` under `data/normalized_yaml` and `data/merge_yaml/merged` found only this normalized owner and this generated merge record for JCM 1407.

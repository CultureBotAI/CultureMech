# YAML Record Review: mdm_modified_dehority_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/mdm_modified_dehority_medium.yaml
- Started UTC: 2026-09-24T01:01:27Z
- Finished UTC: 2026-09-24T01:02:22Z
- Verdict: needs curation

## Target

Reviewed generated merged record `data/merge_yaml/merged/mdm_modified_dehority_medium.yaml` for DSMZ/MediaDive medium 1668. Exact `find` over `data/normalized_yaml` with ignored files included located one normalized owner: `data/normalized_yaml/bacterial/mdm_modified_dehority_medium.yaml`.

Exact `mediadive.medium:1668` searches over the generated record, the owner, and normalized indexes included ignored files and found only this record family and the matching bacterial/recipe index entries.

## Validation

- Open LinkML validation against `src/culturemech/schema/culturemech.yaml` as `MediaRecipe`: passed with `No issues found`.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows; the strict TSV had a header only.
- LinkML reference validation: passed; 0 reference checks were emitted for this file.
- LinkML term validation with labels and `conf/oak_config.yaml`: passed.
- Embedded `curation_history`: Not checked. The repository `just validate-history` target validates standalone `history/` files rather than embedded generated-record history blocks.

## Identity and Grounding

`media_term.term.id` is `mediadive.medium:1668`, matching live MediaDive REST and rendered pages for `MDM (modified dehority medium)`. The final pH 6.8 and the anaerobic main-medium instruction were preserved.

## Evidence

MediaDive 1668 defines a 500 ml main solution with Yeast extract, Tryptone, 250 ml of `Stock A: Salt solution 2x (50 ml stock per 100 ml medium)`, 2.5 ml of `Stock B: Salt solution 200x (0,5 ml stock per 100 ml medium)`, water, and 1 g/L L-Cysteine HCl. The target instead stores every Stock A and Stock B row at the stock recipe concentration:

- Stock A rows are two-fold too high: the stock is added at 250 ml per 500 ml, so `K2HPO4`, `NaHCO3`, `NaCl`, `NH4Cl`, `CaCl2`, `MgCl2`, and `FeSO4 x 7 H2O` need a 0.5 factor.
- Stock B rows are 200-fold too high: the stock is added at 2.5 ml per 500 ml, so `MgCl2 x 2 H2O`, `ZnCl2`, `CoCl2`, `Na2 MoO4 x 2 H2O`, `Na2SeO3`, `NiCl2 x 6 H2O`, and `Na2WO4 x 2 H2O` need a 0.005 factor.

The record also flattens multiple non-main solutions as direct final-medium ingredients without a final addition volume in the REST main recipe. The `Vitamin solution` rows are present at their 1000 ml stock concentrations, the `Cellobiose (10%)` stock contributes 100 g/L cellobiose, `CM-Mix (only for DSM 104697)` contributes D-Glucose, Cellobiose, Maltose, and Starch, and `Vitamin K1 solution (only for DSM 104697)` contributes Ethanol and Vitamin K1. This produced a single `Cellobiose` row of 101.0 g/L with the note `[Merged 2 duplicates: 100.0, 1.0]`.

## Completeness

The target has the main solution, stock recipes, auxiliary solutions, and DSM 104697-only solutions collapsed into one flat 33-row ingredient list. That shape loses solution boundaries, solution addition volumes, and strain-specific qualifiers from the MediaDive source. Water-only rows are intentionally absent from CultureMech, but the remaining solutes cannot be interpreted as final per-liter concentrations until the referenced stocks are scaled and the unreferenced or conditional solutions are removed or represented conditionally.

`L-Cysteine HCl` still carries a legacy `mediaingredientmech_term` instead of a migrated `mediaingredientmech_chebi_term`, and `NiCl2 x 6 H2O` is grounded to an anhydrous nickel dichloride term.

## Findings

1. `needs curation` - Stock A salts are present at 2x their final concentrations because `K2HPO4`, `NaHCO3`, `NaCl`, `NH4Cl`, `CaCl2`, `MgCl2`, and `FeSO4 x 7 H2O` were not multiplied by the 250 ml / 500 ml stock-addition ratio.
2. `needs curation` - Stock B trace salts are present at 200x their final concentrations because `MgCl2 x 2 H2O`, `ZnCl2`, `CoCl2`, `Na2 MoO4 x 2 H2O`, `Na2SeO3`, `NiCl2 x 6 H2O`, and `Na2WO4 x 2 H2O` were not multiplied by the 2.5 ml / 500 ml stock-addition ratio.
3. `needs curation` - Auxiliary stock and DSM 104697-only solutions were flattened into the base medium as final ingredients, yielding unsupported final rows such as 101.0 g/L `Cellobiose`, 4 g/L `D-Glucose`, 19 g/L `Ethanol`, and 0.1 g/L `Vitamin K1`.
4. `minor` - `L-Cysteine HCl` and `NiCl2 x 6 H2O` need enrichment cleanup after the quantitative stock flattening is fixed.

## Recommended Edits

Rebuild the normalized DSMZ 1668 record with explicit stock-solution boundaries or with final concentrations computed from each main-solution stock volume. Stock A must be multiplied by 0.5; Stock B must be multiplied by 0.005. Do not flatten the vitamin, cellobiose, CM-Mix, or Vitamin K1 solution stock concentrations into the unconditional base medium unless the source provides a final addition volume and condition.

After the recipe is corrected, rerun duplicate-row cleanup so unrelated `Cellobiose` contexts are not arithmetically merged, then rerun MediaIngredientMech/CHEBI enrichment for `L-Cysteine HCl` and `NiCl2 x 6 H2O`.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validators on the regenerated merged record.
- Confirm Stock A and Stock B values are scaled by 0.5 and 0.005, respectively.
- Confirm the regenerated base medium no longer has `Cellobiose: 101.0 G_PER_L`, unconditional `D-Glucose`, unconditional `Ethanol`, or unconditional `Vitamin K1` rows.
- Re-check `mediadive.medium:1668` in normalized source indexes with ignored files included.

## Additional Notes

The MediaDive REST response for medium 1668 was sufficient to verify the main solution, stock A/B addition volumes, auxiliary solution names, and DSM 104697-only qualifiers; the rendered page agreed on the MDM identity and final pH.

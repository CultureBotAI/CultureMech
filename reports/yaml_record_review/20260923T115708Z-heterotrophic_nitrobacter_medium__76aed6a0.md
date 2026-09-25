# YAML Record Review: HETEROTROPHIC NITROBACTER MEDIUM
- Repository: CultureMech
- Record: data/merge_yaml/merged/heterotrophic_nitrobacter_medium__76aed6a0.yaml
- Started UTC: 2026-09-23T11:56:18Z
- Finished UTC: 2026-09-23T11:57:08Z
- Verdict: needs curation

## Target

Reviewed the generated direct DSMZ branch for DSMZ Medium 756, `HETEROTROPHIC NITROBACTER MEDIUM`, at `data/merge_yaml/merged/heterotrophic_nitrobacter_medium__76aed6a0.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/heterotrophic_nitrobacter_medium__76aed6a0.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `mediadive.medium:756` and has the DSMZ Medium 756 title and pH 7.4. Its identity is correct; the curation defects are in the structured composition of DSMZ's stock solutions.

## Evidence

DSMZ Medium 756 lists 1.50 g yeast extract, 1.50 g peptone, 0.55 g sodium pyruvate, 1 ml Trace element solution, 100 ml Stock solution, and 899 ml distilled water in the main medium. The Stock solution is a separate one-liter recipe containing 0.07 g CaCO3, 5.00 g NaCl, 0.50 g magnesium sulfate heptahydrate, and 1.50 g KH2PO4. The Trace element solution is a separate one-liter recipe containing milligram amounts of manganese, boric acid, zinc, molybdate, iron, and copper salts.

The generated record flattens the Stock solution and Trace element solution contents into top-level ingredients at their source stock strengths. It also omits the 899 ml final-medium water and the water rows for both stock recipes.

## Completeness

The main carbon and nitrogen ingredients and pH-adjustment text are present. The record is incomplete for the stock-solution boundaries, solvent volumes, and final concentrations of every ingredient that entered through a stock addition.

## Findings

- The 100 ml Stock solution addition was flattened at full stock strength; CaCO3, NaCl, MgSO4 x 7 H2O, and KH2PO4 should either remain nested or be diluted 10-fold in the final medium.
- The 1 ml Trace element solution addition was flattened at full stock strength; all six trace rows should either remain nested or be diluted 1000-fold in the final medium.
- The 899 ml distilled-water row in the main solution is missing.
- Distilled water is missing from the Stock solution and Trace element solution recipes.
- NaOH/KOH pH adjustment is present only as preparation prose and is not linked to reagent choices.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/heterotrophic_nitrobacter_medium.yaml` to preserve DSMZ 756's Stock solution and Trace element solution as scoped solutions.
- Restore the 899 ml main-medium water and the water rows in both stocks.
- Either keep stock ingredients nested or convert them to final concentrations after applying the 100 ml/L and 1 ml/L addition volumes.
- Keep pH 7.4 adjustment with NaOH or KOH as an ordered preparation step.

## Follow-up Checks

- Re-run merge generation and the four focused validators after the normalized source is corrected.
- Confirm no regenerated top-level ingredient retains the full-strength trace-solution values such as `0.0973 G_PER_L` ferrous sulfate heptahydrate.

## Additional Notes

None.

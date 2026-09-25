# YAML Record Review: HELIOBACILLUS MOBILIS MEDIUM (modified van Niel's medium)
- Repository: CultureMech
- Record: data/merge_yaml/merged/heliobacillus_mobilis_medium_modified_van_niels_medium.yaml
- Started UTC: 2026-09-23T11:50:56Z
- Finished UTC: 2026-09-23T11:51:34Z
- Verdict: needs curation

## Target

Reviewed the generated source-duplicate merge for DSMZ Medium 537, `HELIOBACILLUS MOBILIS MEDIUM (modified van Niel's medium)`, at `data/merge_yaml/merged/heliobacillus_mobilis_medium_modified_van_niels_medium.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/heliobacillus_mobilis_medium_modified_van_niels_medium.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The generated record merges the direct DSMZ 537 branch with the KOMODO Medium 537 branch and retains the DSMZ `mediadive.medium:537` media term. The two source records are true mirrors of DSMZ Medium 537, but the normalized parents have inherited the same stock-flattened composition.

## Evidence

MediaDive 537 and the DSMZ PDF list 0.100 g MgSO4, 2.000 mg EDTA, 10.000 g yeast extract, and 885.000 ml distilled water in the main medium. After pH adjustment, boiling, dispensing under nitrogen, and autoclaving, the source aseptically adds 1 ml Trace element solution A, 10 ml Trace element solution B, 5 ml of a `4 g in 100 ml H2O` K2HPO4 stock, and 100 ml of a `1.1 g in 100 ml H2O` sodium-pyruvate stock. Trace element solution A is a separate one-liter stock, and Trace element solution B is a separate 100 ml stock.

The generated record omits the 885 ml main-medium water, flattens every Trace element solution A and B stock ingredient at stock strength, and represents the K2HPO4 and sodium-pyruvate stock volumes as `5 G_PER_L` and `100 G_PER_L`.

## Completeness

The record has the DSMZ title, pH, major base ingredients, and a paraphrase of the preparation block. It loses the distinction between final medium and stock solutions, omits all water from the main medium and the two trace-element stocks, and does not preserve that K2HPO4 and sodium pyruvate are filter-sterilized stock additions after autoclaving.

## Findings

- The 885 ml distilled-water row in the final medium is missing.
- Trace element solution A is added at 1 ml/L, but its boric acid, manganese, zinc, molybdate, copper, and cobalt rows are present at 1000x their stock concentrations rather than at their final dilutions.
- Trace element solution B is added at 10 ml/L, but ferric ammonium citrate and calcium chloride are imported as the stock's 2 g/L and 3 g/L rather than the final 0.02 g/L and 0.03 g/L.
- K2HPO4 is imported as `5 G_PER_L`; the source adds 5 ml of a 4 g/100 ml stock, or 0.2 g/L final.
- Sodium pyruvate is imported as `100 G_PER_L`; the source adds 100 ml of a 1.1 g/100 ml stock, or 1.1 g/L final.
- The preparation step is a single `FILTER_STERILIZE` action covering pH adjustment, boiling, nitrogen dispensing, autoclaving, cooling, and filter-sterilized additions.

## Recommended Edits

- Curate the DSMZ 537 normalized parent and the KOMODO mirror so stock solutions remain nested or are converted to final concentrations after applying the 1 ml/L and 10 ml/L addition volumes.
- Restore distilled water in the main medium and in both trace-element stock recipes.
- Convert the K2HPO4 and sodium-pyruvate stock additions to final medium amounts instead of treating their volumes as grams per liter.
- Split preparation into ordered pH adjustment, boiling, nitrogen dispensing, autoclaving, cooling, and aseptic filter-sterilized stock-addition steps.

## Follow-up Checks

- Re-run merge generation and verify the DSMZ and KOMODO mirrors still collapse to one source-duplicate record after the source records are corrected.
- Confirm the regenerated final recipe no longer contains the full-strength Trace element solution A or B stock rows as top-level ingredient concentrations.

## Additional Notes

None.

# YAML Record Review: planctomyces_medium__9f041a1b

- Repository: CultureMech
- Record: data/merge_yaml/merged/planctomyces_medium__9f041a1b.yaml
- Started UTC: 2026-09-24T21:27:04Z
- Finished UTC: 2026-09-24T21:27:04Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:001133
- Name: planctomyces_medium
- Source import: planctomyces_medium
- Primary external ID: mediadive.medium:1651
- Maintained input: data/normalized_yaml/bacterial/planctomyces_medium.yaml

This generated record represents DSMZ Medium 1651, PLANCTOMYCES MEDIUM.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/planctomyces_medium__9f041a1b.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct DSMZ Medium 1651 identity. Exact ignored-file searches across `data` for `mediadive.medium:1651`, `DSMZ_Medium1651`, and the `planctomyces_medium` slug found this normalized recipe and generated merge, plus a separate same-label DSMZ Medium 622 recipe; DSMZ 622 is a different liquid Planctomyces medium and is not an equivalent duplicate of DSMZ 1651.

The base DSMZ 1651 ingredients are recognizable, and several stock-internal ingredient groundings are individually plausible. The source hierarchy is not preserved: MediaDive and the DSMZ PDF define a main solution with 20 ml mineral salts solution, 1 ml trace element solution, 250 ml artificial sea water, and 5 ml double-concentrated vitamin solution, while the generated record places those stocks' internal ingredients directly in the final medium table.

## Evidence

- DSMZ Medium 1651 lists 0.25 g Bacto peptone, 0.25 g Bacto yeast extract, 2.38 g HEPES, 20 ml mineral salt solution, 1 ml trace element solution, 250 ml artificial sea water, 15 g Bacto agar, and 730 ml double-distilled water in the autoclaved base.
- The source then adds 8 ml of 10% N-acetylglucosamine stock and 5 ml double-concentrated vitamin solution from Medium 621 after cooling to 60 C.
- DSMZ Medium 1651 separately defines 1 L artificial sea water, mineral salts solution, Metals 44, trace element solution, and vitamin solution recipes.
- The source nests 50 ml Metals 44 inside 1 L mineral salts solution, then adds only 20 ml of that mineral salts solution to the final medium.

## Completeness

The generated record is incomplete as a source-faithful DSMZ 1651 representation:

- Artificial sea water is a 250 ml stock addition, but all artificial-sea-water salts are top-level ingredients at stock concentrations.
- Mineral salts solution is a 20 ml stock addition, but nitrilotriacetic acid, MgSO4 x 7 H2O, CaCl2 x 2 H2O, Na2MoO7O4 x 2 H2O, FeSO4 x 7 H2O, and nested Metals 44 rows are top-level ingredients at stock concentrations.
- Trace element solution is a 1 ml stock addition, but its internals are top-level ingredients at stock concentrations.
- Double-concentrated vitamin solution is a 5 ml stock addition, but its internals are top-level ingredients at stock concentrations.
- H3BO3, FeSO4 x 7 H2O, MnSO4 x H2O, CuSO4 x 5 H2O, and Co(NO3)2 x 6 H2O were summed across distinct stock boundaries.
- `Double distilled water` was summed across several stock and final-medium water rows and represented as 3730 G_PER_L.

## Findings

1. Major: Stock recipes from DSMZ 1651 were flattened into the final medium. The MediaDive and PDF sources require 20 ml mineral salts solution, 1 ml trace element solution, 250 ml artificial sea water, and 5 ml vitamin solution additions; future repair belongs in `data/normalized_yaml/bacterial/planctomyces_medium.yaml` or the MediaDive importer.
2. Major: Several salts from different stocks were merged by label instead of kept in their source stock context. `H3BO3`, `FeSO4 x 7 H2O`, `MnSO4 x H2O`, `CuSO4 x 5 H2O`, and `Co(NO3)2 x 6 H2O` each combine separate source rows; future repair belongs in the source-preserving normalization layer.
3. Major: Final concentrations are inflated by missing stock dilution factors. Trace element internals are 1000-fold high, artificial-sea-water internals are 4-fold high, vitamin stock internals are 200-fold high, and Metals 44 internals omit both the 50 ml per liter mineral-salts dilution and the 20 ml final-medium addition.

## Recommended Edits

- Rebuild DSMZ 1651 in `data/normalized_yaml/bacterial/planctomyces_medium.yaml` with separate solution records or source-preserving nested stock additions for mineral salts solution, Metals 44, trace element solution, artificial sea water, and vitamin solution.
- Preserve the source volumes: 20 ml mineral salts, 50 ml Metals 44 inside 1 L mineral salts, 1 ml trace elements, 250 ml artificial sea water, 8 ml 10% N-acetylglucosamine, and 5 ml double-concentrated vitamin solution.
- Recalculate final concentrations only after stock hierarchy is preserved so stock-internal rows are not summed into top-level grams per liter.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run an exact ignored-file search for `mediadive.medium:1651` and `DSMZ_Medium1651` with ignored files included before adding any new DSMZ 1651 source import.
- Spot-check the rendered DSMZ 1651 page to ensure artificial sea water, mineral salts, Metals 44, trace elements, and vitamin solution render as stock additions rather than as final base ingredients.

## Additional Notes

None found.

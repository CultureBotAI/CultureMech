# YAML Record Review: pfennigs_medium_iii

- Repository: CultureMech
- Record: data/merge_yaml/merged/pfennigs_medium_iii.yaml
- Started UTC: 2026-09-24T21:01:38Z
- Finished UTC: 2026-09-24T21:01:38Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:001229
- Name: pfennigs_medium_iii
- Source import: pfennigs_medium_iii
- Primary external ID: mediadive.medium:1761
- Source URL: DSMZ_Medium1761.pdf

This generated record represents DSMZ Medium 1761, PFENNIG'S MEDIUM III.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/pfennigs_medium_iii.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The medium identity is correct for DSMZ Medium 1761, and exact ignored-file searches across `data` found only the normalized MediaDive source and this merged record for `mediadive.medium:1761` / `DSMZ_Medium1761`.

Ingredient grounding is mostly populated and locally consistent, but the generated row structure is not source-faithful. The DSMZ recipe is assembled from Solution A, B, C, D, E, F, G, Trace element solution SL-12 B, and a separate neutralized sulfide feeding solution. The generated record flattens those stocks into one final `ingredients` list and stores many stock concentrations as final medium concentrations.

## Evidence

- The rendered DSMZ Medium 1761 PDF defines Solution A-G and Trace element solution SL-12 B separately.
- The source final-assembly instructions add 50 ml of mixed Solution C/D/E to each 100 ml bottle of Solution A, then add 2.6 ml Solution B, 0.1 ml Solution F, and 1 ml Solution G before use.
- The source neutralized sulfide solution is a separate feed for DSM 11081 at 0.5-1 ml per 100 ml approximately every 3 days.
- The source says the final assembled medium is adjusted with filter-sterilized 1 M Na2CO3 to pH 7.1-7.3.

## Completeness

The record is complete enough to identify the medium and many stock ingredients, but it is not complete as a curated final recipe. The named solution hierarchy and feed-solution boundary are missing from structured ingredients, so generated concentrations such as CaCl2 x 2 H2O 0.543478 G_PER_L and NaHCO3 30 G_PER_L are stock-solution values, not final-medium values.

Other missing or distorted details:

- Solution B Na2S x 9 H2O at 14.8148 G_PER_L and neutralized sulfide Na2S x 9 H2O at 30 G_PER_L were merged into a single 44.8148 G_PER_L final row.
- Trace element solution SL-12 B rows are direct stock concentrations; they have not been converted through the 1 ml Solution E aliquot and 25 ml Solution E stock.
- Solution G ammonium acetate and magnesium acetate are 2.5 g per 100 ml stock values, not 25 G_PER_L final-medium values.
- Resazurin is supplied as 0.5 ml of a 0.1% stock solution for Solution D, but the generated row stores it as 0.005 G_PER_L without preserving that source context.
- The top-level `ph_value` is 6.0 even though the assembled medium is finally adjusted to pH 7.1-7.3; the pH 6.0 instruction belongs near the SL-12 B stock context.

## Findings

1. The stock hierarchy was flattened. Solution A-G and SL-12 B should be represented as stocks or nested preparation components, not as peer final-medium ingredients.
2. Stock concentrations were treated as final concentrations for the main medium, which overstates most salts, vitamins, acetate salts, and trace metals.
3. The neutralized sulfide feeding solution was merged into the same Na2S x 9 H2O ingredient as Solution B, creating a chemically impossible 44.8148 G_PER_L final row.
4. The final pH is wrong at the recipe level. The generated `ph_value: 6.0` does not capture the final DSMZ 1761 pH 7.1-7.3 after Na2CO3 adjustment.
5. Volume additions for 50 ml mixed Solution C/D/E, 2.6 ml Solution B, 0.1 ml Solution F, and 1 ml Solution G are only present in prose, so they cannot be used for unit-aware final concentration derivation.

## Recommended Edits

- Rebuild DSMZ 1761 from the primary PDF with Solution A-G, SL-12 B, and neutralized sulfide feed preserved as distinct source components.
- Convert the named solution aliquots into final concentrations only after preserving stock volumes, stock concentrations, and final assembly volume.
- Keep the neutralized sulfide feed separate from Solution B and from the base medium.
- Set the final assembled medium pH to 7.1-7.3; keep the pH 6.0 adjustment with SL-12 B if the schema can represent per-solution pH.
- Preserve CO2 and N2 bubbling as preparation steps or atmosphere metadata, not ingredients.
- Regenerate the merged YAML from the corrected normalized source.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Re-render the generated DSMZ 1761 page and verify that named stocks, aliquots, final pH, and neutralized sulfide feeding instructions are not collapsed into the base ingredient table.
- Repeat an exact ignored-file search for `mediadive.medium:1761` and `DSMZ_Medium1761` to confirm that no second normalized DSMZ 1761 import was introduced.

## Additional Notes

None found.

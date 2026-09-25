# YAML Record Review: ferriphaselus_es_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ferriphaselus_es_medium.yaml
- Started UTC: 2026-09-23T02:51:50Z
- Finished UTC: 2026-09-23T02:52:39Z
- Verdict: needs curation

## Target

CultureMech:000727 is the generated merged record for DSMZ Medium 1267, `FERRIPHASELUS (ES) MEDIUM`.

DSMZ 1267 is a layered defined agarose medium built from 901 ml Solution A, 1 ml Solution B, and 100 ml Solution C. Solution A contains the basal salts, 1 ml Modified Wolin's mineral solution, MES, NaHCO3, agarose, and water. Solution B contains 1 ml 10x Wolin's vitamin solution. Solution C contains 100 ml ferrous sulfide sludge.

## Validation

- LinkML open-schema validation: pass; `linkml-validate` reported `No issues found`.
- Strict schema validation: pass; `scripts/validate_strict.py` exited 0 and the TSV contained only the header row.
- Reference validation: pass; the reference validator scanned the file and reported 0 checks.
- Term validation: pass; `linkml-term-validator` exited 0 and reported `Validation passed`.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded history entries in generated MediaRecipe YAML.

## Identity and Grounding

The CultureMech identifier, normalized name, DSMZ Medium 1267 identity, defined/solid typing, and pH range match the intended source medium.

Most simple ingredient strings have plausible CHEBI groundings, but the generated ingredient list should not be interpreted as final solute concentrations because it has flattened DSMZ stock solutions at their own full recipe concentrations.

## Evidence

The DSMZ PDF and the MediaDive REST payload agree on the high-level recipe: main solution 1267 is 901 ml Solution A, 1 ml Solution B, and 100 ml Solution C. The generated YAML instead expands Solution A's 1 ml Modified Wolin's mineral stock, Solution B's 1 ml 10x vitamin stock, and Solution C's 100 ml ferrous sulfide sludge as top-level gram-per-liter ingredients.

That expansion overstates the stock contents. The full 1 L Modified Wolin's mineral formula is merged into the top-level record even though only 1 ml of that stock is used in Solution A; this produces merged rows such as MgSO4 x 7 H2O `0.221976 + 3.0` and CaCl2 x 2 H2O `0.110988 + 0.1`. The 1 L Wolin's vitamin formula is likewise copied directly as 0.02 to 0.1 g/L vitamin ingredients despite Solution B containing only 1 ml of a 10x stock. The 100 ml ferrous sulfide sludge recipe is copied as 154 g/L FeSO4 x 7 H2O and 123 g/L Na2S x 9 H2O and the FeSO4 row is then merged with the 0.1 g/L mineral-stock row into `154.1`.

The generated preparation steps preserve the DSMZ bottom-layer, top-layer, inoculation, Solution B filtration, Modified Wolin's mineral, and ferrous-sulfide-sludge instructions.

## Completeness

The generated record is not composition-complete for DSMZ 1267 because it loses the nested Solution A, B, and C boundaries that make the recipe meaningful.

The record includes the components of referenced stocks, but at stock concentrations instead of the smaller amounts contributed to the final medium or layer.

## Findings

1. The 1 ml Modified Wolin's mineral addition is flattened at full 1 L stock concentration, then merged with basal Solution A salts.
2. The 1 ml Solution B vitamin stock is flattened at full 10x stock concentration, making every vitamin row a stock recipe concentration rather than a final-medium contribution.
3. The 100 ml ferrous sulfide sludge stock is flattened as if 154 g/L FeSO4 x 7 H2O and 123 g/L Na2S x 9 H2O were final medium ingredients, even though those values describe the sludge stock preparation.
4. The generated ingredient list cannot distinguish which ingredients belong only to the top agarose layer, only to the FeS bottom layer, or to reusable stock solutions.

## Recommended Edits

1. Recurate DSMZ 1267 with Solution A, Solution B, Solution C, Modified Wolin's mineral solution, Wolin's vitamin solution, and ferrous sulfide sludge preserved as nested stocks.
2. Avoid merging duplicate salts across basal recipes, mineral stocks, and FeS sludge unless the values are first normalized to the actual same final layer.
3. If nested stocks cannot be represented, scale every expanded stock ingredient by its real volume contribution and keep layer-specific notes for top-layer and bottom-layer ingredients.

## Follow-up Checks

- Re-run open-schema, strict-schema, reference, and term validation after recurating the nested stock graph.
- Confirm `FeSO4 x 7 H2O` no longer appears as a merged `154.1` g/L top-level ingredient.
- Confirm the recipe still records pH 6.1 to 6.4 and DSMZ Medium 1267.

## Additional Notes

The DSMZ Medium 1267 PDF was fetched and rendered to text with `mutool`; its solution hierarchy matches the MediaDive REST payload used for this review.

# YAML Record Review: carboxydocella_manganica_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CARBOXYDOCELLA_MANGANICA_MEDIUM.yaml
- Started UTC: 2026-09-22T03:46:55Z
- Finished UTC: 2026-09-22T03:46:55Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:001641`, `carboxydocella_manganica_medium`, class `MediaRecipe`.
- Merge lineage: one source recipe, `carboxydocella_manganica_medium`, on fingerprint `8e1c9f33116c3fc83ff4877fdafdb58600e449218b0e1f0bfb71966da815ac7a`.
- Maintained owner: `data/normalized_yaml/bacterial/carboxydocella_manganica_medium.yaml`.
- Claimed source identity: DSMZ/MediaDive Medium 507b.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation exited successfully for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The generated merge and normalized owner are materially identical: the merge only appends its `MERGED_RECIPES` event, `merge_fingerprint`, and `merged_from`.
- The record denotes DSMZ/MediaDive Medium 507b, `CARBOXYDOCELLA MANGANICA MEDIUM`. The DSMZ PDF and MediaDive JSON agree on pH 6.5, five base salts, 10 ml Trace element solution SL-4, carbonate, pyruvate, yeast extract, 1 ml 10x Wolin vitamin solution, 1000 ml distilled water, and the anaerobic preparation text.
- The generated owner correctly uses MediaDive's 1011 ml final-volume normalization for the directly weighed main-solution salts, carbonate, pyruvate, and yeast extract.
- Most simple ingredient groundings are source-compatible. `NiCl2 x 6 H2O` is grounded to generic nickel dichloride instead of the exact packaged `CHEBI:53542` answer for the hexahydrate label, and `Calcium D-(+)-pantothenate` is missing the CHEBI-keyed MediaIngredientMech mirror carried by other grounded rows.

## Evidence

- MediaDive's Medium 507b JSON represents the main recipe as `Main sol. 507b` with 1011 ml final volume: 1000 ml water plus 10 ml Trace element solution SL-4 plus 1 ml Wolin's vitamin solution (10x).
- DSMZ and MediaDive both keep Trace element solution SL-4 as a 1000 ml stock recipe, added at 10 ml in Medium 507b. The active `data/normalized_yaml/bacterial/mediadive_20_Trace_element_solution_SL-4.yaml` import also preserves that SL-4 stock and its EDTA/pH instruction.
- DSMZ and MediaDive both keep Wolin's vitamin solution (10x) as a 1000 ml stock recipe, added at 1 ml in Medium 507b. The active `data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml` import also preserves that stock solution.
- DSMZ lists `Distilled water 1000 ml` in all three places: the main 507b recipe, the SL-4 stock, and the 10x Wolin stock.

## Completeness

- The generated record is missing the main-medium `Distilled water` row.
- The generated record flattens full-strength SL-4 and Wolin stock components directly into the main `ingredients` list. The final medium receives only 10 ml of SL-4 and 1 ml of 10x Wolin stock in 1011 ml total volume, so these generated stock components are about 101-fold or 1011-fold too concentrated as final medium rows.
- The generated record does not link to the active `mediadive.solution:20` SL-4 solution or `mediadive.solution:5980` Wolin solution; both standalone solution imports also store their 1000 ml water rows as `1000 PERCENT_V_V` instead of `1000 ML_PER_L`.
- Target organisms, evidence, variants, and references are empty. The inspected DSMZ/MediaDive source is sufficient for composition and preparation, but this record has not tried to curate strain-specific growth claims.

## Findings

- Major: Trace element solution SL-4 was flattened incorrectly. The source adds 10 ml of SL-4 stock to a 1011 ml final medium, but the generated medium stores the full-strength SL-4 stock recipe as main-medium g/L concentrations.
- Major: Wolin's vitamin solution (10x) was flattened incorrectly. The source adds 1 ml of the 10x stock to a 1011 ml final medium, but the generated medium stores the full-strength vitamin stock recipe as main-medium g/L concentrations.
- Major: the generated record omits the required 1000 ml distilled-water component from the main solution, and the active standalone SL-4 and Wolin imports both preserve their own water rows with a pseudo-percent unit.
- Minor: `NiCl2 x 6 H2O` needs a hexahydrate-specific primary CHEBI grounding.
- Minor: `Calcium D-(+)-pantothenate` has a correct primary CHEBI term but is missing a `mediaingredientmech_chebi_term` mirror.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/carboxydocella_manganica_medium.yaml`, `data/normalized_yaml/bacterial/mediadive_20_Trace_element_solution_SL-4.yaml`, and `data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml`, not the generated merge.
- Add `Distilled water` at `1000 ML_PER_L` to the main medium and repair both standalone stock solutions so their water rows use `ML_PER_L`.
- Represent Trace element solution SL-4 as a 10 ml stock-solution addition and Wolin's vitamin solution (10x) as a 1 ml stock-solution addition instead of flattening their full-strength components into the main medium.
- Preserve the SL-4 stock pH-7.0 preparation instruction on the stock solution, not as a second top-level preparation step on the main medium.
- Reground `NiCl2 x 6 H2O` to `CHEBI:53542`.
- Add the missing CHEBI-keyed MediaIngredientMech mirror for `Calcium D-(+)-pantothenate`.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the maintained medium owner and both stock-solution owners.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/CARBOXYDOCELLA_MANGANICA_MEDIUM.yaml`.
- Inspect the regenerated merge to confirm it has main-medium water, 10 ml/L SL-4 and 1 ml/L Wolin stock additions, no full-strength stock components in the main ingredient list, hydrate-specific nickel grounding, and the intended pantothenate mirror.
- Re-check the DSMZ Medium 507b PDF and MediaDive Medium 507b JSON export to confirm the maintained medium and stock solutions still match all source rows and instructions.

## Additional Notes

- `rg --no-ignore --hidden -l` for `CultureMech:001641`, `mediadive.medium:507b`, `CARBOXYDOCELLA_MANGANICA_MEDIUM`, and `carboxydocella_manganica_medium` included ignored and hidden files; it found one active normalized owner, one generated merge, generated indexes/catalogs, archived validation reports, the semi-defined composition audit, concentration plausibility output, and unrelated downstream app/report artifacts, but no second active normalized owner for `mediadive.medium:507b`.
- The formula is legitimately semi-defined because the source includes 0.20 g/L yeast extract; `data/import_tracking/reports/composition_type_semi_defined.tsv` has already promoted this owner to `SEMI_DEFINED`.

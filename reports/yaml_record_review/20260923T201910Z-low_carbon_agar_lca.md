# YAML Record Review: Low Carbon Agar-LCA

- Repository: CultureMech
- Record: `data/merge_yaml/merged/low_carbon_agar_lca.yaml`
- Started UTC: `2026-09-23T20:17:54Z`
- Finished UTC: `2026-09-23T20:19:10Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:001251`
- `name`: `low_carbon_agar_lca`
- `original_name`: `Low Carbon Agar-LCA`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `media_term`: `mediadive.medium:1818`
- `merge_fingerprint`: `a3da8dae2e1d15e2455b8851e9828d41ad79f0f34fd7a0f848e3151d706ba730`
- `merged_from`: `low_carbon_agar_lca`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/low_carbon_agar_lca.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:001251`, `mediadive.medium:1818`, `Source: DSMZ, ID: 1818`, `low_carbon_agar_lca`, and the merge fingerprint found one maintained owner, `data/normalized_yaml/bacterial/low_carbon_agar_lca.yaml`, plus this generated record. No duplicate generated recipe or archived conflicting owner was found in the checked paths.
- The generated record merges exactly one owner on the recorded fingerprint and preserves DSMZ / MediaDive medium ID 1818.
- MediaDive REST and HTML both identify Medium 1818 as `Low Carbon Agar-LCA`, source DSMZ, complex medium, and a 500 ml `Main sol. 1818`.
- `Mg(SO4) x 7 H2O` and `Yeast extract` are not CHEBI-grounded in either the maintained owner or the generated record. They are still explicit source-name rows, so this review did not treat them as identity errors.
- `NaNO3` carries a correct `CHEBI:63005` term but still has a legacy `mediaingredientmech_term: MediaIngredientMech:000171` field instead of a `mediaingredientmech_chebi_term` field.

## Evidence

- MediaDive REST Medium 1818 returns medium ID `1818`, name `Low Carbon Agar-LCA`, `complex_medium: yes`, source `DSMZ`, and one solution, `Main sol. 1818`, with volume `500` ml.
- MediaDive REST Solution 6328 gives eight recipe rows for that 500 ml solution: 0.5 g `D(+)-Glucose`, 0.5 g `KH2PO4`, 0.1 g `Mg(SO4) x 7 H2O`, 0.1 g `KCl`, 1 g `NaNO3`, 0.1 g `Yeast extract`, 9 g `Agar`, and 500 ml `Distilled water`.
- The generated record keeps the seven non-water ingredient rows in source order and omits `Distilled water`.
- The generated record stores each non-water source mass as the same numeric value in `G_PER_L`; because the MediaDive solution volume is 500 ml, those same numeric values are not the actual grams-per-liter values for the source solution.
- The MediaDive page reports `Final pH: n.d.`, `Medium type: Complex medium`, and no associated strains for Medium 1818.
- The solution endpoint reports no preparation steps and no equipment for Solution 6328, so the generated record is correctly empty for source-specific preparation steps.

## Completeness

- Ingredient identities and ordering match the non-water MediaDive rows.
- Ingredient amounts do not match MediaDive when interpreted through the generated `G_PER_L` units: the source rows are grams in 500 ml, not grams per liter.
- The `Distilled water` 500 ml row is present in MediaDive and absent from the generated record.
- No pH value, preparation steps, equipment, or associated strains were found in the checked MediaDive REST and HTML views.

## Findings

1. MediaDive masses were imported as grams per liter without accounting for the 500 ml solution volume.
   - Evidence: MediaDive Solution 6328 has `volume: 500` and source rows like 0.5 g `D(+)-Glucose` and 9 g `Agar`; the generated record stores `D(+)-Glucose` as 0.5 `G_PER_L` and `Agar` as 9 `G_PER_L` instead of converting the 500 ml recipe to 1 g/L glucose and 18 g/L agar or preserving the original 500 ml solution boundary.
   - Impact: every non-water concentration is half the DSMZ formula if consumers read the unit literally.

2. The 500 ml `Distilled water` row is omitted.
   - Evidence: both MediaDive Medium 1818 and Solution 6328 include recipe order 9, `Distilled water`, amount 500, unit `ml`; the generated YAML has no water or final-volume row.
   - Impact: the generated record loses the source final-volume boundary needed to interpret the source mass rows.

3. `NaNO3` still carries a deprecated `mediaingredientmech_term` link.
   - Evidence: the generated and maintained `NaNO3` ingredient rows have `term: CHEBI:63005` but retain `mediaingredientmech_term: MediaIngredientMech:000171`; the June 2026 curation event notes that the legacy `MediaIngredientMech:NNNNNN` ID scheme was deprecated.
   - Impact: this one row missed the CHEBI-keyed enrichment shape used by the other migrated rows.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/low_carbon_agar_lca.yaml` or the MediaDive importer so source masses from a 500 ml MediaDive solution are either preserved with their original solution volume or converted to the correct `G_PER_L` values before merge.
2. Preserve the `Distilled water` 500 ml final-volume row from MediaDive Solution 6328 when representing this recipe.
3. Replace the `NaNO3` `mediaingredientmech_term` object with the CHEBI-keyed enrichment shape used by the other CHEBI-grounded rows.
4. Regenerate `data/merge_yaml/merged/low_carbon_agar_lca.yaml` from the corrected owner and rerun downstream generated outputs.

## Follow-up Checks

- Re-fetch MediaDive Medium 1818 and Solution 6328 and verify that all corrected ingredient quantities retain the 500 ml boundary or convert exactly to the expected grams per liter.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Re-run any MediaIngredientMech migration/enrichment checks after replacing the legacy `NaNO3` link.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.

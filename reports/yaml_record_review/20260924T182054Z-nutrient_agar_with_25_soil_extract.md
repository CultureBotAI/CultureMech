# YAML Record Review: nutrient_agar_with_25_soil_extract

- Repository: CultureMech
- Record: data/merge_yaml/merged/nutrient_agar_with_25_soil_extract.yaml
- Started UTC: 2026-09-24T18:20:54Z
- Finished UTC: 2026-09-24T18:20:54Z
- Verdict: needs curation

## Target

- `id`: `CultureMech:010373`
- `name`: `nutrient_agar_with_25_soil_extract`
- `original_name`: `Nutrient Agar With 25% Soil Extract`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `media_term`: `TOGO:M94`, `Nutrient Agar With 25% Soil Extract`
- `merged_from`: `TOGO_M94_Nutrient_Agar_With_25_Soil_Extract`

## Validation

- LinkML validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with 0 ERROR rows; `/private/tmp/nutrient_agar_with_25_soil_extract.strict.tsv` was header-only.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The generated record is the TOGO Medium M94 import of JCM Medium 102, `NUTRIENT AGAR WITH 25% SOIL EXTRACT`. TOGO M94 and the live JCM page both list the final liter as 5.0 g Peptone, 3.0 g Beef extract, 250.0 ml Soil extract, 15.0 g Agar, and 750.0 ml Tap water, adjusted to pH 7.0. The Soil extract stock is prepared separately from 400 g air-dried garden soil in 1.0 L tap water.

An ignored-inclusive exact search found the intended TOGO M94 source, the direct JCM J102 maintained source, the generated TOGO M94 record under review, and an older generated `nutrient_agar__990be6d3` merge that incorrectly absorbed the direct JCM J102 record.

## Evidence

The maintained `data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml` has been repaired: it keeps 250.0 ml/L Soil extract as a nested solution in the final medium, keeps the stock's 400 g/L air-dried garden soil and 1.0 L tap water inside that solution, records pH 7.0 and the soil-stock autoclave/sedimentation/centrifugation steps, and cites both TOGO M94 and JCM Medium 102.

The generated record is stale. It flattens `Soil extract (see below)` to a 250 g/L final ingredient, flattens the stock's 400 g/L air-dried garden soil into the final ingredient list, merges 750 ml of final tap water with 1.0 L stock tap water into `751.0 G_PER_L`, and omits pH 7.0, preparation steps, references, and data-quality flags.

## Completeness

The review checked the generated TOGO M94 record, its repaired maintained normalized source, the direct JCM J102 normalized source, TOGO Medium M94, the live JCM 102 page, schema validation, strict validation, reference validation, term validation, and an ignored-inclusive exact search for JCM 102 and the soil-extract slug.

## Findings

1. The generated ingredient structure is wrong. JCM 102 uses a 250 ml Soil extract aliquot in the final liter and a separate stock made from 400 g soil plus 1.0 L tap water. The generated record flattens the stock soil and stock water into the final medium and turns both milliliter quantities into gram-per-liter rows.
2. The generated record is stale relative to the repaired TOGO M94 normalized source. It lacks the repaired `solutions` entry, source annotations, preparation steps, pH 7.0, `ingredients_curated` / `has_unmapped_ingredients` flags, FoodOn/MICRO mappings for Beef extract and Peptone, and TOGO/JCM references.
3. The direct JCM J102 normalized source is also malformed and was absorbed into the unrelated `nutrient_agar__990be6d3` generated record. It should be repaired to match the TOGO M94 mirror or removed as a stale duplicate before the duplicate graph is regenerated.

## Recommended Edits

- Regenerate this record from the repaired `TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml` so the 250 ml Soil extract row remains a solution and the 400 g soil plus 1.0 L stock tap water stay inside that solution.
- Preserve pH 7.0, soil-extract preparation steps, TOGO/JCM references, source annotations, and data-quality flags in the generated YAML.
- Repair the direct JCM J102 source in `data/normalized_yaml/bacterial/nutrient_agar_with_25_soil_extract.yaml` and reconcile it with TOGO M94 as the same JCM recipe instead of allowing it to merge with unsupplemented Nutrient Agar.

## Follow-up Checks

- Re-run generation and confirm `nutrient_agar_with_25_soil_extract` contains no 250 g/L soil-extract ingredient, no 400 g/L final soil ingredient, and no 751.0 g/L tap-water row.
- Confirm the direct JCM J102 record no longer appears in the generated `nutrient_agar` duplicate cluster.
- Re-run schema, strict, reference, and term validation against the regenerated YAML.

## Additional Notes

None found.

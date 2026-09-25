# YAML Record Review: nutrient_broth_nb_ii

- Repository: CultureMech
- Record: data/merge_yaml/merged/nutrient_broth_nb_ii.yaml
- Started UTC: 2026-09-24T18:31:32Z
- Finished UTC: 2026-09-24T18:31:32Z
- Verdict: needs curation

## Target

- `id`: `CultureMech:009430`
- `name`: `nutrient_broth_nb_ii`
- `original_name`: `Nutrient broth (NB II)`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `TOGO:M2894`, `Nutrient broth (NB II)`
- `merged_from`: `nutrient_broth_nb_ii`

## Validation

- LinkML validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with 0 ERROR rows; `/private/tmp/nutrient_broth_nb_ii.strict.tsv` was header-only.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The generated record is TOGO Medium M2894 `Nutrient broth (NB II)`. TOGO lists the NB II liquid formulation as 3.5 g/L Peptone from casein, 2.5 g/L Peptone from meat, 2.5 g/L Peptone from gelatine, 1.5 g/L Yeast extract, and 5 g/L NaCl, grown at 30 C.

An ignored-inclusive exact search for TOGO M2894 and `nutrient_broth_nb_ii` found only the expected maintained source, the generated singleton record, and source/catalog/index references to that same source.

## Evidence

The generated record preserves the five non-water source ingredients and their concentrations. The maintained `data/normalized_yaml/bacterial/nutrient_broth_nb_ii.yaml` has already been repaired to add row-level source annotations, a 1.0 L Distilled water row, a 30 C temperature value, a FoodOn mapping for Yeast extract, a FoodOn mapping for Peptone from casein, data-quality flags, and the TOGO M2894 reference.

The generated record is stale. It includes Distilled water but stores it as `1 G_PER_L`, and it lacks the repaired 30 C temperature, source annotations, FoodOn mappings, `ingredients_curated` / `has_unmapped_ingredients` flags, and source reference.

## Completeness

The review checked the generated record, the repaired maintained normalized source, TOGO Medium M2894, schema validation, strict validation, reference validation, term validation, and an ignored-inclusive exact search for the TOGO identifier and slug.

## Findings

1. The generated water row has the wrong unit. TOGO M2894 records a per-liter formulation, and the repaired source stores Distilled water as 1.0 L; the generated record stores `1 G_PER_L`.
2. The generated record is stale relative to the repaired source. It lacks temperature 30 C, source annotations, Yeast extract and Peptone from casein mappings, `ingredients_curated` / `has_unmapped_ingredients` flags, and the TOGO M2894 reference.

## Recommended Edits

- Regenerate this singleton from `data/normalized_yaml/bacterial/nutrient_broth_nb_ii.yaml` so the Distilled water row uses 1.0 L and the temperature, source annotations, source reference, curation flags, and repaired mappings are preserved.
- Keep Peptone from meat and Peptone from gelatine intentionally unmapped unless source-specific meat and gelatin hydrolysate ontology terms are added.

## Follow-up Checks

- Re-run generation and confirm the generated record has no 1 g/L Distilled water row.
- Re-run schema, strict, reference, and term validation against the regenerated YAML.

## Additional Notes

None found.

# YAML Record Review: nutrient_broth_nb_difco

- Repository: CultureMech
- Record: data/merge_yaml/merged/nutrient_broth_nb_difco.yaml
- Started UTC: 2026-09-24T18:30:29Z
- Finished UTC: 2026-09-24T18:30:29Z
- Verdict: needs curation

## Target

- `id`: `CultureMech:008787`
- `name`: `nutrient_broth_nb_difco`
- `original_name`: `Nutrient broth (NB) (Difco)`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `TOGO:M2194`, `Nutrient broth (NB) (Difco)`
- `merged_from`: `nutrient_broth_nb_difco`

## Validation

- LinkML validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with 0 ERROR rows; `/private/tmp/nutrient_broth_nb_difco.strict.tsv` was header-only.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The generated record is TOGO Medium M2194 `Nutrient broth (NB) (Difco)`. TOGO lists 8 g Nutrient broth (NB) from Difco in 1 L Distilled water at pH 6.8 +/- 0.2; its source comment says strains of Dickeya dadantii 3937 were cultivated at 30 C in nutrient broth, King's B medium, or minimal medium A.

An ignored-inclusive exact search for TOGO M2194 and `nutrient_broth_nb_difco` found only the expected maintained source, the generated singleton record, unresolved-commercial-product bookkeeping for the same source, and source/catalog/index references to that same source.

## Evidence

The maintained `data/normalized_yaml/bacterial/nutrient_broth_nb_difco.yaml` has already been repaired. It keeps 8 g/L Nutrient broth (NB) from Difco intentionally unmapped, corrects Distilled water to 1000 ml/L, records pH range 6.6 to 7.0, records the 30 C culture temperature, adds MIX steps, adds data-quality flags, and cites TOGO M2194.

The generated record is stale. It has the correct 8 g/L Difco Nutrient broth row, but it stores the 1 L Distilled water row as `1 G_PER_L`, lacks the pH range and 30 C temperature, and omits the repaired source annotations, preparation steps, data-quality flags, and source reference.

## Completeness

The review checked the generated record, the repaired maintained normalized source, TOGO Medium M2194, schema validation, strict validation, reference validation, term validation, and an ignored-inclusive exact search for the TOGO identifier and slug.

## Findings

1. The generated water row has the wrong unit. TOGO M2194 lists 1 L Distilled water, and the repaired source records 1000 ml/L; the generated record stores `1 G_PER_L`.
2. The generated record is stale relative to the repaired source. It lacks the source pH range, 30 C cultivation temperature, source annotations, preparation steps, `ingredients_curated` / `has_unmapped_ingredients` flags, and the TOGO M2194 reference.

## Recommended Edits

- Regenerate this singleton from `data/normalized_yaml/bacterial/nutrient_broth_nb_difco.yaml` so the Distilled water row uses 1000 ml/L and the pH range, temperature, source annotations, preparation steps, curation flags, and reference are preserved.
- Continue to leave the commercial Nutrient broth (NB) (Difco) row unmapped unless a product-level ontology term is intentionally added.

## Follow-up Checks

- Re-run generation and confirm the generated record has no 1 g/L Distilled water row.
- Re-run schema, strict, reference, and term validation against the regenerated YAML.

## Additional Notes

None found.

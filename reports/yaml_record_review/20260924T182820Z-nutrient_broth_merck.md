# YAML Record Review: nutrient_broth_merck

- Repository: CultureMech
- Record: data/merge_yaml/merged/nutrient_broth_merck.yaml
- Started UTC: 2026-09-24T18:28:20Z
- Finished UTC: 2026-09-24T18:28:20Z
- Verdict: pass with minor issues

## Target

- `id`: `CultureMech:009448`
- `name`: `nutrient_broth_merck`
- `original_name`: `Nutrient broth (Merck)`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `TOGO:M2911`, `Nutrient broth (Merck)`
- `merged_from`: `nutrient_broth_merck`

## Validation

- LinkML validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with 0 ERROR rows; `/private/tmp/nutrient_broth_merck.strict.tsv` was header-only.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The generated record is TOGO Medium M2911 `Nutrient broth (Merck)`. TOGO M2911 lists two components, 5 g/L Peptone from meat and 3 g/L Meat extract, and notes that Salmonella isolates were inoculated into nutrient broth from Merck and incubated at 37 C for 18 h.

An ignored-inclusive exact search for TOGO M2911 and `nutrient_broth_merck` found only the expected maintained source, the generated singleton record, and source/catalog/index references to that same source.

## Evidence

The generated singleton preserves both source ingredient rows and both concentrations exactly: 5 g/L Peptone from meat and 3 g/L Meat extract.

The maintained `data/normalized_yaml/bacterial/nutrient_broth_merck.yaml` has minor repair metadata that has not reached the generated artifact yet. It adds row-level `source` and `notes`, a note that the isolate incubation in the TOGO comment was at 37 C for 18 h, `temperature_value: 37.0`, `ingredients_curated` / `has_unmapped_ingredients`, and a TOGO M2911 reference.

## Completeness

The review checked the generated record, the repaired maintained normalized source, TOGO Medium M2911, schema validation, strict validation, reference validation, term validation, and an ignored-inclusive exact search for the TOGO identifier and slug.

## Findings

1. The generated record is mildly stale relative to the repaired source. It lacks `temperature_value: 37.0`, row-level source annotations, data-quality flags, and the TOGO M2911 reference.

## Recommended Edits

- Regenerate this singleton from `data/normalized_yaml/bacterial/nutrient_broth_merck.yaml` so the repaired temperature, source annotations, curation flags, and source reference are preserved.

## Follow-up Checks

- Re-run generation and confirm the two generated ingredient rows remain 5 g/L Peptone from meat and 3 g/L Meat extract.
- Re-run schema, strict, reference, and term validation against the regenerated YAML.

## Additional Notes

None found.

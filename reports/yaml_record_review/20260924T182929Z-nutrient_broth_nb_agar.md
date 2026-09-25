# YAML Record Review: nutrient_broth_nb_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/nutrient_broth_nb_agar.yaml
- Started UTC: 2026-09-24T18:29:29Z
- Finished UTC: 2026-09-24T18:29:29Z
- Verdict: needs curation

## Target

- `id`: `CultureMech:009085`
- `name`: `nutrient_broth_nb_agar`
- `original_name`: `Nutrient broth (NB) agar`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `media_term`: `TOGO:M2513`, `Nutrient broth (NB) agar`
- `merged_from`: `nutrient_broth_nb_agar`

## Validation

- LinkML validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with 0 ERROR rows; `/private/tmp/nutrient_broth_nb_agar.strict.tsv` was header-only.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The generated record is TOGO Medium M2513 `Nutrient broth (NB) agar`. The source comment states that the agar medium has 3 g beef extract, 5 g peptone, and 15 g agar per liter for maintenance of the ORFRC strain. A second source comment describes Rahnella sp. Y9602 incubation at 25 C in an anoxic chamber under 1% H2, 5% CO2, and 94% N2.

An ignored-inclusive exact search for TOGO M2513 and `nutrient_broth_nb_agar` found only the expected maintained source, the generated singleton record, and source/catalog/index references to that same source.

## Evidence

The generated record and the maintained `data/normalized_yaml/bacterial/nutrient_broth_nb_agar.yaml` still match. Both include the four medium components plus three variable-concentration gas rows for carbon dioxide, nitrogen, and hydrogen.

The TOGO M2513 source text separates those concepts: beef extract, peptone, agar, and water are the medium formulation; H2, CO2, N2, and 25 C are incubation atmosphere and temperature conditions. The source gives exact atmosphere percentages, but the generated ingredient rows lose those percentages and retain the gases only as variable recipe components.

## Completeness

The review checked the generated record, the maintained normalized source, TOGO Medium M2513, schema validation, strict validation, reference validation, term validation, and an ignored-inclusive exact search for the TOGO identifier and slug.

## Findings

1. The generated record treats incubation gases as ingredients. `Carbon dioxide gas`, `Nitrogen gas`, and `Hydrogen gas` should not be variable medium components; they come from an anoxic headspace of 1% H2, 5% CO2, and 94% N2 for Rahnella sp. Y9602 incubation.
2. The generated water row has the wrong unit. TOGO M2513 lists the recipe per liter, but the record stores Distilled water as `1 G_PER_L` instead of 1 L.
3. The 25 C incubation condition and the exact anoxic gas percentages are absent. The current gas ingredient rows discard the percentages that would be needed to capture the culture condition faithfully.

## Recommended Edits

- Remove H2, CO2, and N2 from `ingredients` in `data/normalized_yaml/bacterial/nutrient_broth_nb_agar.yaml`; capture the 1% H2 / 5% CO2 / 94% N2 anoxic atmosphere in notes or an incubation-condition field if the schema has one.
- Correct Distilled water to 1.0 L, keep 3.0 g/L Beef extract, 5.0 g/L Peptone, and 15.0 g/L Agar as the medium formulation, and record the 25 C incubation temperature outside the ingredient list.
- Add a TOGO M2513 reference, row-level source annotations, curation flags, and a repair history entry before regenerating this YAML.

## Follow-up Checks

- Re-run generation and confirm no gas appears as a top-level medium ingredient for TOGO M2513.
- Confirm the regenerated record has no 1 g/L water row.
- Re-run schema, strict, reference, and term validation against the regenerated YAML.

## Additional Notes

None found.

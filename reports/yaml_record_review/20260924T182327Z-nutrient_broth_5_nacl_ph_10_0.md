# YAML Record Review: nutrient_broth_5_nacl_ph_10_0

- Repository: CultureMech
- Record: data/merge_yaml/merged/nutrient_broth_5_nacl_ph_10_0.yaml
- Started UTC: 2026-09-24T18:23:27Z
- Finished UTC: 2026-09-24T18:23:27Z
- Verdict: needs curation

## Target

- `id`: `CultureMech:008325`
- `name`: `nutrient_broth_5_nacl_ph_10_0`
- `original_name`: `Nutrient Broth + 5% NaCl (pH 10.0)`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `media_term`: `TOGO:M1760`, `Nutrient Broth + 5% NaCl (pH 10.0)`
- `merged_from`: `nutrient_broth_5_nacl_ph_10_0`

## Validation

- LinkML validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with 0 ERROR rows; `/private/tmp/nutrient_broth_5_nacl_ph_10_0.strict.tsv` was header-only.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The generated record is TOGO Medium M1760, an import of NBRC Medium 972. TOGO and NBRC agree that the medium contains 13 g Nutrient Broth (OXOID), 50 g NaCl, 15 g Agar if needed, and 900 ml Distilled water in the main base, plus 100 ml of a sodium-sesquicarbonate stock made from 4.2 g NaHCO3, 5.3 g anhydrous Na2CO3, and 100 ml Distilled water. The stock is sterilized separately and added to the other autoclaved ingredients; final pH is about 10.0.

An ignored-inclusive exact search for TOGO M1760, NBRC 972, and `nutrient_broth_5_nacl_ph_10_0` found only the expected maintained source, the generated singleton record, and source/catalog/index references to that same record.

## Evidence

The maintained `data/normalized_yaml/bacterial/nutrient_broth_5_nacl_ph_10_0.yaml` has already been repaired. It keeps the final per-liter concentrations for Nutrient Broth, NaCl, NaHCO3, Na2CO3, optional Agar, and Distilled water; models total water as 1000.0 ml/L; records final pH 10.0; maps sodium carbonate to `CHEBI:29377`; preserves the separate 100 ml sodium-sesquicarbonate-stock handling as preparation and sterilization metadata; and cites TOGO M1760 plus NBRC 972.

The generated record is still stale. It has the correct non-water final ingredient amounts, but it keeps the 100 ml stock as an empty `Unknown solution`, flattens 900 ml base water plus 100 ml stock water to `1000.0 G_PER_L`, drops final pH 10.0, lacks the sodium-carbonate CHEBI mapping, and omits the repaired preparation steps, sterilization note, source annotations, references, and data-quality flags.

## Completeness

The review checked the generated record, the repaired maintained normalized source, TOGO Medium M1760, the live NBRC Medium 972 page, schema validation, strict validation, reference validation, term validation, and an ignored-inclusive exact search for the TOGO/NBRC identifiers and slug.

## Findings

1. The generated water row has the wrong unit. NBRC 972 contributes 900 ml base water plus 100 ml stock water per final liter, and the repaired source records 1000.0 ml/L; the generated record stores that total as `1000.0 G_PER_L`.
2. The generated `solutions` entry is a stale migration artifact. The NBRC sodium-sesquicarbonate stock is represented by the NaHCO3 and Na2CO3 final concentrations plus separate-stock preparation metadata in the repaired record; the generated `Sodium-sesquicarbonate solution*` row has `composition: []`, `100 G_PER_L`, and `name: Unknown solution`.
3. The generated record is stale relative to the repaired source. It lacks pH 10.0, the Na2CO3 `CHEBI:29377` mapping, source annotations, preparation steps, a sterilization note, `ingredients_curated` / `has_unmapped_ingredients` flags, and TOGO/NBRC references.

## Recommended Edits

- Regenerate the merged record from the repaired normalized source so Distilled water is 1000.0 ml/L and the empty sodium-sesquicarbonate `Unknown solution` is removed.
- Preserve pH 10.0, the Na2CO3 CHEBI mapping, separate-stock preparation steps, source annotations, data-quality flags, and TOGO/NBRC references.
- Confirm generation no longer emits a solution row when a stock has been intentionally reduced to final per-liter ingredient concentrations plus preparation metadata.

## Follow-up Checks

- Re-run generation and confirm the record has no 1000.0 g/L water row and no empty sodium-sesquicarbonate solution.
- Confirm the regenerated record still keeps final NaHCO3 at 4.2 g/L and Na2CO3 at 5.3 g/L.
- Re-run schema, strict, reference, and term validation against the regenerated YAML.

## Additional Notes

None found.

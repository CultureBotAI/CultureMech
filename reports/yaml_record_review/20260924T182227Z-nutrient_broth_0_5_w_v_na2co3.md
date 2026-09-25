# YAML Record Review: nutrient_broth_0_5_w_v_na2co3

- Repository: CultureMech
- Record: data/merge_yaml/merged/nutrient_broth_0_5_w_v_na2co3.yaml
- Started UTC: 2026-09-24T18:22:27Z
- Finished UTC: 2026-09-24T18:22:27Z
- Verdict: needs curation

## Target

- `id`: `CultureMech:008239`
- `name`: `nutrient_broth_0_5_w_v_na2co3`
- `original_name`: `Nutrient Broth + 0.5%(w/v) Na2CO3`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `media_term`: `TOGO:M1680`, `Nutrient Broth + 0.5%(w/v) Na2CO3`
- `merged_from`: `nutrient_broth_0_5_w_v_na2co3`

## Validation

- LinkML validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with 0 ERROR rows; `/private/tmp/nutrient_broth_0_5_w_v_na2co3.strict.tsv` was header-only.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The generated record is TOGO Medium M1680, an import of NBRC Medium 885. TOGO and NBRC agree on the rows for 8 g Bacto Nutrient Broth (Difco), 5 g Na2CO3, 15 g Agar if needed, and 1 L Distilled water, with a source note that Na2CO3 is sterilized separately by autoclaving and added to the other ingredients; final pH is about 10.5.

An ignored-inclusive exact search for TOGO M1680, NBRC 885, and `nutrient_broth_0_5_w_v_na2co3` found only the expected maintained source, the generated singleton record, and source/catalog/index references to that same record.

## Evidence

The maintained `data/normalized_yaml/bacterial/nutrient_broth_0_5_w_v_na2co3.yaml` has already been repaired. It keeps Bacto Nutrient Broth, Na2CO3, optional Agar, and Distilled water as final ingredients; records Distilled water as 1000.0 ml/L; maps Na2CO3 to `CHEBI:29377`; preserves final pH 10.5; models separate carbonate autoclaving as preparation and sterilization metadata; and cites TOGO M1680 plus NBRC 885.

The generated record is still stale. It leaves Distilled water as 1 g/L, moves Na2CO3 into an empty `Unknown solution`, drops the sodium-carbonate ontology mapping, drops final pH 10.5, and lacks the repaired preparation steps, sterilization note, references, source annotations, and data-quality flags.

## Completeness

The review checked the generated record, the repaired maintained normalized source, TOGO Medium M1680, the live NBRC Medium 885 page, schema validation, strict validation, reference validation, term validation, and an ignored-inclusive exact search for the TOGO/NBRC identifiers and slug.

## Findings

1. The generated ingredient structure is wrong. NBRC 885 lists Na2CO3 as a 5 g/L ingredient with separate sterilization, but the generated record moves it to `solutions` with an empty `composition` and `name: Unknown solution`.
2. The generated water quantity is wrong. The source lists 1 L Distilled water per liter, and the repaired maintained record stores 1000.0 ml/L; the generated record stores `1 G_PER_L`.
3. The generated record is stale relative to the repaired source. It lacks pH 10.5, the Na2CO3 `CHEBI:29377` mapping, source annotations, preparation steps, a sterilization note, `ingredients_curated` / `has_unmapped_ingredients` flags, and TOGO/NBRC references.

## Recommended Edits

- Regenerate the merged record from the repaired normalized source so Na2CO3 is a final 5.0 g/L ingredient and Distilled water is 1000.0 ml/L.
- Preserve pH 10.5, the separate Na2CO3 sterilization preparation step, the CHEBI mapping for sodium carbonate, source annotations, data-quality flags, and TOGO/NBRC references.
- Confirm the generation pipeline no longer converts separately sterilized ingredients into empty `Unknown solution` entries.

## Follow-up Checks

- Re-run generation and confirm `solutions` is absent or no longer contains an empty Na2CO3 stock for this medium.
- Confirm the regenerated record has no `1 G_PER_L` Distilled water row.
- Re-run schema, strict, reference, and term validation against the regenerated YAML.

## Additional Notes

None found.

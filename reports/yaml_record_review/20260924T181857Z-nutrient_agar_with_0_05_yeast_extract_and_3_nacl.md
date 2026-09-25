# YAML Record Review: nutrient_agar_with_0_05_yeast_extract_and_3_nacl

- Repository: CultureMech
- Record: data/merge_yaml/merged/nutrient_agar_with_0_05_yeast_extract_and_3_nacl.yaml
- Started UTC: 2026-09-24T18:18:57Z
- Finished UTC: 2026-09-24T18:18:57Z
- Verdict: needs curation

## Target

- `id`: `CultureMech:007712`
- `name`: `nutrient_agar_with_0_05_yeast_extract_and_3_nacl`
- `original_name`: `Nutrient Agar With 0.05% Yeast Extract And 3% NaCl`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `media_term`: `TOGO:M1186`, `Nutrient Agar With 0.05% Yeast Extract And 3% NaCl`
- `merged_from`: `nutrient_agar_with_0_05_yeast_extract_and_3_nacl`

## Validation

- LinkML validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with 0 ERROR rows; `/private/tmp/nutrient_agar_with_0_05_yeast_extract_and_3_nacl.strict.tsv` was header-only.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The generated bacterial record is the TOGO Medium M1186 import of JCM Medium 1109. TOGO reports original source `JCM_M1109` with JCM `GRMD=1109`; both TOGO and the live JCM page list Nutrient agar, see JCM Medium 74, at 1.0 L; Yeast extract (BD-Difco) at 0.5 g; and NaCl at 30.0 g.

An ignored-inclusive exact search found this bacterial TOGO M1186 source, a fungal direct JCM 1109 record with the same slug, the generated fungal hash-suffixed output for that direct JCM record, and unrelated records that merely mention M1186 as an NBRC or JCM source identifier in other namespaces.

## Evidence

The maintained bacterial source in `data/normalized_yaml/bacterial/nutrient_agar_with_0_05_yeast_extract_and_3_nacl.yaml` has already been repaired to model JCM 1109 as a supplemented variant of `data/normalized_yaml/bacterial/JCM_J74_NUTRIENT_AGAR.yaml`: it keeps 30.0 g/L NaCl and 0.5 g/L Yeast extract (BD-Difco) as added ingredients, records `Nutrient agar (JCM Medium 74)` as a 1.0 L solution, links the parent JCM 74 source, and keeps TOGO/JCM references plus data-quality flags.

The generated record still has the stale migrated representation. It stores the JCM 74 nested medium as `Nutrient agar (see Medium [M65])`, gives it `unit: G_PER_L` instead of `unit: L`, names the solution `Unknown solution`, and omits the maintained parent-media relationship, variant modification, references, data-quality flags, source annotations, and FoodOn yeast-extract mapping.

## Completeness

The review checked the generated bacterial record, its maintained normalized source, the category-colliding fungal JCM 1109 source, TOGO Medium M1186, the live JCM 1109 page, schema validation, strict validation, reference validation, term validation, and an ignored-inclusive exact search for the relevant TOGO and JCM identifiers.

## Findings

1. The generated nested-medium quantity is wrong. JCM 1109 and TOGO M1186 use 1.0 L Nutrient agar from JCM Medium 74, but the generated `solutions` row encodes the same nested medium as `1 G_PER_L` with an `Unknown solution` name and a stale TOGO `M65` cross-reference.
2. The generated record is stale relative to the repaired normalized bacterial source. The generated YAML lacks the repaired parent link to JCM 74, supplemented-variant metadata, source annotations, FoodOn yeast-extract mapping, data-quality flags, and TOGO/JCM references.
3. A same-source JCM 1109 import remains under `data/normalized_yaml/fungal/nutrient_agar_with_0_05_yeast_extract_and_3_nacl.yaml` and generated as `nutrient_agar_with_0_05_yeast_extract_and_3_nacl__c7db8d34.yaml`. That fungal source is malformed and currently prevents a clean same-source reconciliation of TOGO M1186 with the direct JCM 1109 import.

## Recommended Edits

- Regenerate this merged record from the repaired normalized bacterial source so the nested Nutrient agar component is represented as `1.0 L` of JCM Medium 74 instead of `1 G_PER_L`.
- Preserve the repaired parent `SUPPLEMENTED_VARIANT` link to `JCM_J74_NUTRIENT_AGAR`, variant-modification text, source annotations, FoodOn yeast-extract mapping, `has_unmapped_ingredients` flag for the nested Nutrient agar solution, and TOGO/JCM references.
- Repair or retire the fungal direct JCM 1109 duplicate so the same JCM recipe is not represented as both a repaired bacterial TOGO source and a malformed fungal MediaDive source.

## Follow-up Checks

- Re-run generation and confirm the bacterial generated record has a 1.0 L JCM 74 solution rather than a 1 g/L unknown solution.
- Confirm no direct JCM 1109 duplicate remains outside the intended duplicate cluster.
- Re-run schema, strict, reference, and term validation against the regenerated YAML.

## Additional Notes

None found.

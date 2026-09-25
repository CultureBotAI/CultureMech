# YAML Record Review: nutrient_agar_with_0_05_yeast_extract_and_3_nacl__c7db8d34

- Repository: CultureMech
- Record: data/merge_yaml/merged/nutrient_agar_with_0_05_yeast_extract_and_3_nacl__c7db8d34.yaml
- Started UTC: 2026-09-24T18:19:52Z
- Finished UTC: 2026-09-24T18:19:52Z
- Verdict: needs curation

## Target

- `id`: `CultureMech:010490`
- `name`: `nutrient_agar_with_0_05_yeast_extract_and_3_nacl`
- `original_name`: `NUTRIENT AGAR WITH 0.05% YEAST EXTRACT AND 3% NaCl`
- `category`: `fungal`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `media_term`: `mediadive.medium:J1109`, `NUTRIENT AGAR WITH 0.05% YEAST EXTRACT AND 3% NaCl`
- `merged_from`: `nutrient_agar_with_0_05_yeast_extract_and_3_nacl`

## Validation

- LinkML validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with 0 ERROR rows; `/private/tmp/nutrient_agar_with_0_05_yeast_extract_and_3_nacl__c7db8d34.strict.tsv` was header-only.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The generated fungal record is a direct JCM Medium 1109 import. The checked JCM page lists `NUTRIENT AGAR WITH 0.05% YEAST EXTRACT AND 3% NaCl` with three rows: 1.0 L Nutrient agar from JCM Medium 74, 0.5 g Yeast extract (BD-Difco), and 30.0 g NaCl.

An ignored-inclusive exact search for TOGO M1186 and JCM 1109 identifiers found this fungal direct JCM source, the generated fungal hash-suffixed record, and a repaired bacterial TOGO M1186 import that mirrors the same JCM 1109 source. No additional direct JCM 1109 maintained source was found.

## Evidence

The generated record matches its maintained fungal source and is a singleton merge, so the error is upstream of the merge output. Both generated and maintained YAML encode JCM Medium 1109 as 1000 g/L `Agar`, 0.5 g/L Yeast extract, and 30 g/L NaCl.

The live JCM source does not list a 1000 g/L agar ingredient. It lists 1.0 L of pre-made Nutrient agar from JCM Medium 74 as the base medium, plus 0.5 g Yeast extract and 30.0 g NaCl. The repaired bacterial TOGO M1186 source already uses that interpretation.

## Completeness

The review checked the generated fungal record, its maintained normalized source, the repaired bacterial TOGO mirror, the live JCM 1109 page, the TOGO M1186 export that mirrors JCM 1109, schema validation, strict validation, reference validation, term validation, and an ignored-inclusive exact search for TOGO M1186 and JCM 1109 identifiers.

## Findings

1. The recipe is chemically wrong. It has `Agar` at 1000 g/L, but JCM 1109 requires 1.0 L of Nutrient agar from JCM Medium 74. That is a nested base-medium reference, not pure agar.
2. The direct JCM 1109 source is split from the repaired TOGO M1186 mirror of the same JCM page. Once the JCM source is repaired, those two records should either merge as source duplicates or be linked by explicit duplicate metadata rather than remaining as category-separated singleton outputs.
3. The generated record lacks evidence and repair metadata. It has no references to the JCM page, no parent link to JCM 74, no variant-modification text, no source annotations on the ingredient rows, no data-quality flags, and no FoodOn mapping for the yeast extract row.

## Recommended Edits

- Repair `data/normalized_yaml/fungal/nutrient_agar_with_0_05_yeast_extract_and_3_nacl.yaml` by replacing the 1000 g/L `Agar` row with a 1.0 L `Nutrient agar (JCM Medium 74)` solution or nested-media row.
- Carry over the source-grounded interpretation already present in the repaired bacterial TOGO M1186 source: 0.5 g/L Yeast extract (BD-Difco), 30.0 g/L NaCl, JCM 74 as the parent medium, and TOGO/JCM evidence URLs.
- Reconcile the repaired direct JCM 1109 record with the TOGO M1186 mirror so the same JCM recipe no longer produces two generated outputs with the same slug.

## Follow-up Checks

- Re-run generation and confirm no `nutrient_agar_with_0_05_yeast_extract_and_3_nacl` generated record contains `Agar` at 1000 g/L.
- Confirm the direct JCM 1109 source and TOGO M1186 mirror are no longer category-separated singleton outputs for the same recipe.
- Re-run schema, strict, reference, and term validation against the regenerated YAML.

## Additional Notes

None found.

# YAML Record Review: nutrient_agar_oxoid_cm3_with_phosphate

- Repository: CultureMech
- Record: data/merge_yaml/merged/nutrient_agar_oxoid_cm3_with_phosphate.yaml
- Started UTC: 2026-09-24T18:17:23Z
- Finished UTC: 2026-09-24T18:17:23Z
- Verdict: needs curation

## Target

- `id`: `CultureMech:006094`
- `name`: `nutrient_agar_oxoid_cm3_with_phosphate`
- `original_name`: `NUTRIENT AGAR (OXOID CM3) WITH PHOSPHATE`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `ph_value`: `6.8`
- `media_term`: `komodo.medium:605a`, `NUTRIENT AGAR (OXOID CM3) WITH PHOSPHATE`
- `merged_from`: `KOMODO_605_NUTRIENT_AGAR_OXOID_CM3`, `KOMODO_605a_NUTRIENT_AGAR_OXOID_CM3_WITH_PHOSPHATE`, `nutrient_agar_oxoid_cm3_with_phosphate`

## Validation

- LinkML validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with 0 ERROR rows; `/private/tmp/nutrient_agar_oxoid_cm3_with_phosphate.strict.tsv` was header-only.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The generated record is grounded as KOMODO Medium 605a / DSMZ Medium 605a, a phosphate-supplemented variant of DSMZ Medium 605. MediaDive 605a lists `NUTRIENT AGAR (OXOID CM3) WITH PHOSPHATE`, final pH 6.8, a recipe that starts with 1000 ml of Main sol. 605, and additions of 0.45 g/L KH2PO4 plus 2.39 g/L Na2HPO4 x 12 H2O.

An ignored-inclusive exact search found the expected maintained direct DSMZ 605a record, the expected maintained KOMODO 605a source duplicate, base-605 records that mention 605a as their supplemented variant, and this generated 605a record. No separate third maintained 605a source was present.

## Evidence

The maintained `data/normalized_yaml/bacterial/nutrient_agar_oxoid_cm3_with_phosphate.yaml` and `data/normalized_yaml/bacterial/KOMODO_605a_NUTRIENT_AGAR_OXOID_CM3_WITH_PHOSPHATE.yaml` have already been repaired: both include the 605a phosphate salts, the five DSMZ 605 base solids, the 1.0 L distilled-water row from DSMZ 605, DSMZ PDF references for 605a and 605, `ingredients_curated` / `has_ontology_mappings`, and a dodecahydrate-specific `CHEBI:91259` mapping for `Na2HPO4 x 12 H2O`.

The generated record retains the correct pH and the correct seven non-water ingredients, but it lacks the distilled-water row, ingredient source annotations, preparation step, data-quality flags, references, and the corrected dodecahydrate mapping from the repaired maintained sources.

## Completeness

The review checked the generated merged record, the two intended maintained 605a sources, the erroneous normalized KOMODO 605 source that was merged into this 605a record, DSMZ/MediaDive REST content for Medium 605a, schema validation, strict validation, reference validation, term validation, and an ignored-inclusive exact search for DSMZ/KOMODO 605a identifiers.

## Findings

1. The duplicate cluster is contaminated by base Medium 605. `merged_from` includes `KOMODO_605_NUTRIENT_AGAR_OXOID_CM3`, and `synonyms` exposes `komodo.medium:605` / `nutrient_agar_oxoid_cm3` on the phosphate record. That source says KOMODO/DSMZ Medium 605 in its identifier, term, and notes, but its ingredients are the 605a phosphate fingerprint. It should not merge into a 605a phosphate record until it is corrected to the base DSMZ 605 formulation or otherwise split from the 605a fingerprint.
2. The generated record is stale relative to both repaired 605a maintained sources. It lost the 1.0 L distilled-water ingredient, DSMZ PDF references, data-quality flags, source annotations, and the 605a preparation statement, and it still maps `Na2HPO4 x 12 H2O` only to an anhydrous disodium hydrogenphosphate term instead of the repaired dodecahydrate term.
3. The merged record kept child relationship metadata after collapsing that child with its parent duplicate. It uses KOMODO `CultureMech:006094` as the generated ID while `parent_media` still points to direct DSMZ `CultureMech:001733` with `SOURCE_DUPLICATE`, even though `nutrient_agar_oxoid_cm3_with_phosphate` is already one of the merged sources.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/KOMODO_605_NUTRIENT_AGAR_OXOID_CM3.yaml` so KOMODO Medium 605 carries the base DSMZ 605 ingredients instead of the 605a phosphate salts, or otherwise remove it from the 605a duplicate cluster.
- Regenerate the merged record so only the direct DSMZ 605a record and KOMODO 605a source duplicate collapse into `nutrient_agar_oxoid_cm3_with_phosphate`.
- Preserve the repaired 1.0 L distilled-water row, `CHEBI:91259` dodecahydrate mapping, DSMZ source annotations, preparation step, data-quality flags, references, and parent link to the base DSMZ 605 record in the regenerated artifact.
- Teach the merge step to drop `parent_media` links that point at records already collapsed into the same `merged_from` cluster.

## Follow-up Checks

- Re-run generation after repairing the normalized sources and confirm `KOMODO_605_NUTRIENT_AGAR_OXOID_CM3` no longer appears in the generated 605a `merged_from`.
- Confirm `nutrient_agar_oxoid_cm3` and `nutrient_agar_oxoid_cm3_with_phosphate` remain separate generated records linked by `SUPPLEMENTED_VARIANT`.
- Re-run schema, strict, reference, and term validation against the regenerated 605a YAML.

## Additional Notes

None found.

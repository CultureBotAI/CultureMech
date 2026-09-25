# YAML Record Review: 948_oxoid_nutrient_broth_with_additonal_salt

- Repository: CultureMech
- Record: data/merge_yaml/merged/948_oxoid_nutrient_broth_with_additonal_salt.yaml
- Started UTC: 2026-09-21T07:50:17Z
- Finished UTC: 2026-09-21T07:51:16Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/948_oxoid_nutrient_broth_with_additonal_salt.yaml`.
- Stable identifier: `CultureMech:001029`.
- Source identity asserted by the record: DSMZ / MediaDive `1551`, `948 (OXOID NUTRIENT BROTH) WITH ADDITONAL SALT`.
- The generated record was merged from one owner, `948_oxoid_nutrient_broth_with_additonal_salt.yaml`, on fingerprint `47538ebe26315ed774aced6f4c02f53dc8f2ce74ecd2562e11f81260f9c87f34`.
- Current authoritative owner: `data/normalized_yaml/bacterial/948_oxoid_nutrient_broth_with_additonal_salt.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/948_oxoid_nutrient_broth_with_additonal_salt.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/948_oxoid_nutrient_broth_with_additonal_salt.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/948_oxoid_nutrient_broth_with_additonal_salt.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/948_oxoid_nutrient_broth_with_additonal_salt.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- The DSMZ / MediaDive identity is coherent: `mediadive.medium:1551` identifies the same DSMZ medium 1551 recipe in the generated target, the normalized owner, and BacMedia text.
- A gitignore-independent exact search with a digit boundary for `mediadive.medium:1551` found only one active normalized owner and its generated merge.
- The current normalized owner has already been repaired with structured `Nutrient broth (Oxoid)` provenance, a DSMZ Medium 1551 reference, and a pH value of 7.2.
- The generated record is stale relative to that current owner.

## Evidence

- DSMZ / BacMedia lists 13 g `Nutrient broth (Oxoid)`, 17.5 g NaCl, and 1000 ml distilled water for the DSMZ 1551 main solution.
- The same source discloses the Oxoid nutrient broth composition as 1 g Lab-Lemco beef extract, 2 g yeast extract, 5 g peptone, 5 g NaCl, and 1000 ml distilled water, and states pH 7.2.
- The normalized owner preserves the top-level 13 g/L Oxoid product row, the 17.5 g/L supplemental NaCl row, a 1000 ml/L distilled water row, and separate 1 g/L, 2 g/L, 5 g/L, and 5 g/L rows for the disclosed Oxoid subcomposition.
- The generated target has only the disclosed Oxoid subcomposition rows and one merged 22.5 g/L NaCl row.

## Completeness

- The generated target loses the explicit 13 g/L `Nutrient broth (Oxoid)` product row from DSMZ.
- The generated target loses the 1000 ml distilled water row.
- The generated target collapses supplemental NaCl and Oxoid-internal NaCl into one row, so downstream consumers cannot tell that 17.5 g/L is added outside the commercial product and 5 g/L comes from the product.

## Findings

- BLOCKER: `data/merge_yaml/merged/948_oxoid_nutrient_broth_with_additonal_salt.yaml` is stale and no longer matches the repaired normalized owner.
- BLOCKER: the generated target has incorrect source structure: 13 g/L Nutrient Broth (Oxoid) plus 17.5 g/L added NaCl is represented as an expanded product composition with a single 22.5 g/L NaCl row.
- BLOCKER: the generated target omits the 1 L distilled-water row now present in the normalized owner and in the DSMZ source.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/948_oxoid_nutrient_broth_with_additonal_salt.yaml` from the repaired `data/normalized_yaml/bacterial/948_oxoid_nutrient_broth_with_additonal_salt.yaml`; do not edit the generated YAML directly.
- Preserve both layers of the DSMZ source: the final medium made from 13 g/L Oxoid Nutrient Broth and 17.5 g/L added NaCl, and the disclosed Oxoid product composition.
- Keep the supplemental 17.5 g/L NaCl row separate from the Oxoid-internal 5 g/L NaCl row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merge artifact.
- Re-run an exact `mediadive.medium:1551` source search with a digit boundary; DSMZ Medium 1551 should still have exactly one active generated record.
- Confirm that the generated page shows 13 g/L Nutrient Broth (Oxoid), 17.5 g/L added NaCl, 1000 ml/L distilled water, and pH 7.2.

## Additional Notes

- The `kg_microbe_match: mediadive.medium:74` value appears on many unrelated records and is not useful as a deduplication key for this medium.

# YAML Record Review: nutrient_broth_with_10_horse_serum

- Repository: CultureMech
- Record: `data/merge_yaml/merged/nutrient_broth_with_10_horse_serum.yaml`
- Started UTC: 2026-09-24T18:33:33Z
- Finished UTC: 2026-09-24T18:34:34Z
- Verdict: needs curation

## Target

Generated bacterial record `CultureMech:004809`, `nutrient_broth_with_10_horse_serum`, merging `KOMODO_302_NUTRIENT_BROTH_WITH_10_HORSE_SERUM` with the direct DSMZ/MediaDive 302 record.

## Validation

Open LinkML validation passed with `No issues found`.

Strict validation passed; `/private/tmp/nutrient_broth_with_10_horse_serum.strict.tsv` contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: the history validator operates over standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The KOMODO and direct DSMZ parents are correctly recognized as source duplicates. The KOMODO record explicitly cites DSMZ Medium 302, the direct parent is `mediadive.medium:302`, the local ingredient and pH signatures match, and an existing source-duplicate audit also records this pair as `SOURCE_DUPLICATE`.

An exact ignored-inclusive, hidden-inclusive search for `KOMODO_302_NUTRIENT_BROTH_WITH_10_HORSE_SERUM`, `komodo.medium:302`, `mediadive.medium:302`, `DSMZ Medium 302`, `nutrient_broth_with_10_horse_serum`, and `NUTRIENT BROTH WITH 10% HORSE SERUM` found only the expected normalized KOMODO and MediaDive parents, this generated merge, source indexes, deep-research metadata, and the archived source-duplicate audit row.

## Evidence

MediaDive 302 is DSMZ `NUTRIENT BROTH WITH 10% HORSE SERUM`, pH 7.0, with Peptone 5 g, Meat extract 3 g, Agar 15 g if necessary, Distilled water 1000 ml, and a sterile Horse serum addition of 100 ml to autoclaved medium.

The generated record preserves Peptone 5 g/L, Meat extract 3 g/L, Agar 15 g/L if necessary, and pH 7.0, so the duplicate merge is based on the intended formula.

MediaDive 12 is DSMZ `SOIL EXTRACT MEDIUM`, pH 6.8-7.0, with air-dried garden soil, tap water, and agar; it is unrelated to the horse-serum DSMZ Medium 302 recipe.

## Completeness

The generated record inherited the source omission of Distilled water, the wrong mass unit for Horse serum, and the false `kg_microbe_match`. It also dropped DSMZ preparation details from the direct parent that describe pH adjustment and adding Horse serum to autoclaved medium.

The KOMODO normalized parent is mildly ahead of the generated merge for local ontology terms on `Peptone` and `Horse serum`, but the underlying source formula still needs unit and water repair before regeneration.

## Findings

Needs curation:

- `Horse serum` is encoded as `100 G_PER_L`; MediaDive 302 lists `100 ml` sterile Horse serum.
- The ingredient list is missing `1000 ML_PER_L` Distilled water from DSMZ Medium 302.
- `kg_microbe_match: mediadive.medium:12` points to DSMZ Soil Extract Medium, not DSMZ Medium 302.
- The generated YAML is stale relative to both parents for direct DSMZ preparation steps and relative to the KOMODO parent for exact local `Peptone` and `Horse serum` ontology grounding.

## Recommended Edits

Repair both normalized parents before merge regeneration:

- Add `Distilled water` at `1000 ML_PER_L`.
- Change `Horse serum` to `100 ML_PER_L`.
- Remove or recompute `kg_microbe_match: mediadive.medium:12`.
- Preserve the DSMZ pH-adjustment and sterile-addition preparation details in the canonical generated record.
- Keep the KOMODO parent as a `SOURCE_DUPLICATE` of the direct `mediadive.medium:302` parent.

Regenerate `data/merge_yaml/merged/nutrient_broth_with_10_horse_serum.yaml` from the repaired normalized records instead of hand-editing the generated artifact.

## Follow-up Checks

After repair, rerun open schema, strict, reference, and term validation for this generated YAML. Also confirm no regenerated `NUTRIENT BROTH WITH 10% HORSE SERUM` record contains `mediadive.medium:12`, confirm the formula includes both the 1000 ml/L water and 100 ml/L Horse serum rows, and confirm the preparation text still distinguishes autoclaved base medium from the sterile serum addition.

## Additional Notes

None found.

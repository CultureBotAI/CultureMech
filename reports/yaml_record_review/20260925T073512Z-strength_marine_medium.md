# YAML Record Review: 1/2 Strength Marine Medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/strength_marine_medium.yaml
- Started UTC: 2026-09-25T07:35:12Z
- Finished UTC: 2026-09-25T07:35:12Z
- Verdict: needs curation

## Target
Reviewed generated record `CultureMech:008842` / `strength_marine_medium` from `data/merge_yaml/merged/strength_marine_medium.yaml`.

The generated record has one source, `TOGO:M2255`, which cites ATCC Medium 2515 1/2 Strength Marine Medium.

## Validation
- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed for 1 file with 0 total error rows.
- Reference validation: Passed for 1 file with 0 link checks and all validations passing.
- Term validation: Passed.
- Embedded curation history validation: Not checked; the standalone history validator does not target `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding
The TOGO source identity is preserved in the generated YAML: `TOGO:M2255`, `CultureMech:008842`, and the ATCC source URL all point to the intended ATCC 2515 medium.

The generated record is stale relative to `data/normalized_yaml/bacterial/strength_marine_medium.yaml`. The normalized source has a 2026-09-12 curation entry that corrected the TOGO M2255 import, removed a false `kg_microbe_match` to DSMZ Soil Extract Medium, and linked this recipe to Marine Broth 2216 as a half-strength concentration variant; none of that post-August curation is present in the generated merged YAML.

## Evidence
The ATCC PDF for Medium 2515 lists 18.7 g Marine Broth 2216 from BD 279110, 15.0 g agar if needed, and 1000.0 ml DI Water.

TOGO M2255 carries the same ingredient amounts and the ATCC comment to autoclave at 121 C while keeping the medium spinning during dispensing so the precipitate remains evenly distributed.

MediaDive medium 12 is DSMZ Soil Extract Medium: 400 g air-dried garden soil in 1000 ml tap water, sedimentation and centrifugation of the supernatant, 15 g agar per 1000 ml, and pH 6.8 to 7.0. It is not a match for ATCC 1/2 Strength Marine Medium.

The current normalized `strength_marine_medium.yaml` represents DI Water as 1000 `ML_PER_L`, keeps Marine Broth 2216 as an opaque complex component, records the ATCC autoclave and mixing instructions, and adds a `CONCENTRATION_VARIANT` parent link to `TOGO_M33_Marine_Broth_2216.yaml`.

## Completeness
The generated ingredient list has the right non-water ATCC quantities: 18.7 g/L Marine Broth 2216 and 15 g/L agar for solid medium.

The generated water row is incorrect because 1000 ml DI Water was imported as 1000 `G_PER_L`. The generated record also lacks the ATCC preparation steps and Marine Broth 2216 parent relationship already present in the curated normalized source.

The stale `kg_microbe_match: mediadive.medium:12` is a false link to DSMZ Soil Extract Medium and should be removed from the generated record by regenerating from the current normalized YAML.

## Findings
- The generated merged YAML predates a targeted 2026-09-12 repair in the normalized source.
- DI Water still has the legacy unit `G_PER_L` instead of `ML_PER_L`.
- The false `kg_microbe_match` points to MediaDive 12, an unrelated DSMZ Soil Extract Medium.
- The ATCC autoclave and dispensing note was not propagated into `preparation_steps`.
- The generated record lacks the curated `CONCENTRATION_VARIANT` relationship to Marine Broth 2216 at one-half strength.

## Recommended Edits
- Regenerate `data/merge_yaml/merged/strength_marine_medium.yaml` from the current `data/normalized_yaml/bacterial/strength_marine_medium.yaml`; do not hand-edit the generated merged YAML.
- Confirm regeneration changes DI Water to `ML_PER_L`, removes `kg_microbe_match: mediadive.medium:12`, and preserves the 2026-09-12 curation history.
- Preserve the `parent_media`, `variant_relationship`, `variant_modifications`, `sterilization`, and `references` blocks from the normalized source.

## Follow-up Checks
- Verify the regenerated record still has 18.7 g/L Marine Broth 2216 and 15.0 g/L agar.
- Verify MediaDive 12 does not appear in the regenerated YAML.
- Verify the ATCC autoclave-at-121-C and spinning-while-dispensing instruction appears in `preparation_steps` or equivalent preparation metadata.
- Re-run schema, strict, reference, and term validators on the regenerated merged YAML.

## Additional Notes
The final exact local search for `TOGO:M2255` and `CultureMech:008842` included ignored and hidden files under `data/normalized_yaml` and `data/merge_yaml/merged`. Earlier searches that included `mediadive.medium:12` or an unanchored `strength_marine_medium` slug also matched unrelated stale MediaDive fallbacks and `half_strength_marine_medium_with_1_0_nacl`; those outputs were discarded.

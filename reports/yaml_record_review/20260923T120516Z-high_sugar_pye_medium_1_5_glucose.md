# YAML Record Review: High-sugar PYE medium (1.5% glucose)
- Repository: CultureMech
- Record: data/merge_yaml/merged/high_sugar_pye_medium_1_5_glucose.yaml
- Started UTC: 2026-09-23T12:04:39Z
- Finished UTC: 2026-09-23T12:05:16Z
- Verdict: needs curation

## Target

Reviewed the generated Togo M2874 record for `High-sugar PYE medium (1.5% glucose)` at `data/merge_yaml/merged/high_sugar_pye_medium_1_5_glucose.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/high_sugar_pye_medium_1_5_glucose.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `TOGO:M2874`, whose payload lists high-sugar PYE as PYE supplemented with 1.5% glucose. The extra `kg_microbe_match: mediadive.medium:914` is incorrect: MediaDive 914 is DSMZ `PTYG-MEDIUM`, not high-sugar PYE.

## Evidence

Togo M2874 states that rich medium was PYE with 0.2% Bacto peptone, 0.1% yeast extract, 1 mM MgSO4, and 0.5 mM CaCl2, and that high-sugar PYE medium was PYE with 1.5% glucose or 3% sucrose. The generated `1.5% glucose` branch includes Bacto peptone at 0.2%, yeast extract at 0.1%, MgSO4 at 1 mM, CaCl2 at 0.5 mM, and glucose at 1.5%, which matches the selected Togo branch.

MediaDive 914 instead contains 5 g/L peptone, 5 g/L tryptone, 5 g/L yeast extract, 10 g/L glucose, 0.6 g/L magnesium sulfate heptahydrate, 0.06 g/L CaCl2, and 1000 ml distilled water at pH 7.0. It is a different medium.

## Completeness

The ingredient list matches the Togo M2874 high-sugar PYE glucose variant. The record should not expose DSMZ PTYG-MEDIUM as an asserted KG-Microbe match.

## Findings

- `kg_microbe_match: mediadive.medium:914` is an erroneous cross-reference to DSMZ PTYG-MEDIUM.
- The Togo M2874 original source citation is absent; the payload preserves the source text but not a `src_url`.
- The general Togo comment also mentions a 3% sucrose high-sugar variant, but this record only captures the 1.5% glucose branch and does not link to the alternate branch if one exists.

## Recommended Edits

- Remove or correct `kg_microbe_match: mediadive.medium:914` in `data/normalized_yaml/bacterial/high_sugar_pye_medium_1_5_glucose.yaml`.
- Add the underlying publication reference if it can be recovered from Togo or manual curation.
- Link this glucose variant to any curated 3% sucrose sibling, if present.
- Regenerate the merged artifact after normalized-source edits.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Confirm the regenerated high-sugar PYE record has no MediaDive 914 cross-reference.

## Additional Notes

None.

# YAML Record Review: High-sugar PYE medium (3% sucrose)
- Repository: CultureMech
- Record: data/merge_yaml/merged/high_sugar_pye_medium_3_sucrose.yaml
- Started UTC: 2026-09-23T12:06:02Z
- Finished UTC: 2026-09-23T12:06:42Z
- Verdict: pass with minor issues

## Target

Reviewed the generated Togo M2875 record for `High-sugar PYE medium (3% sucrose)` at `data/merge_yaml/merged/high_sugar_pye_medium_3_sucrose.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/high_sugar_pye_medium_3_sucrose.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `TOGO:M2875`, whose payload names `High-sugar PYE medium (3% sucrose)`. This is the sucrose sibling of the Togo M2874 1.5% glucose high-sugar PYE branch.

## Evidence

Togo M2875 states that rich PYE contains 0.2% Bacto peptone, 0.1% yeast extract, 1 mM MgSO4, and 0.5 mM CaCl2, and that high-sugar PYE medium may be PYE with 1.5% glucose or 3% sucrose. The generated M2875 record has the PYE base plus 3% sucrose with matching concentration units.

## Completeness

The formula is complete relative to Togo M2875. The payload does not include an original `src_url`, so the underlying publication was not checked beyond the source text embedded in Togo.

## Findings

- No composition defects found.
- The original publication citation is absent because Togo M2875 exposes no `src_url`.
- The generated record does not explicitly link the sucrose variant to the Togo M2874 1.5% glucose high-sugar PYE sibling.

## Recommended Edits

- Add the underlying publication reference if it can be recovered from Togo or manual curation.
- Add a variant or sibling relationship to the 1.5% glucose branch.

## Follow-up Checks

- Confirm future regeneration preserves 3% sucrose and does not inherit the bad `kg_microbe_match: mediadive.medium:914` cross-reference from the glucose sibling.

## Additional Notes

None.

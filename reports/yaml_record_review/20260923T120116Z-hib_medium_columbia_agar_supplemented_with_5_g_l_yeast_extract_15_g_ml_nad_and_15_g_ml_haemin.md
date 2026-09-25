# YAML Record Review: Hib medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/hib_medium_columbia_agar_supplemented_with_5_g_l_yeast_extract_15_g_ml_nad_and_15_g_ml_haemin.yaml
- Started UTC: 2026-09-23T12:00:45Z
- Finished UTC: 2026-09-23T12:01:16Z
- Verdict: needs curation

## Target

Reviewed the generated Togo M2189 record for Hib medium at `data/merge_yaml/merged/hib_medium_columbia_agar_supplemented_with_5_g_l_yeast_extract_15_g_ml_nad_and_15_g_ml_haemin.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hib_medium_columbia_agar_supplemented_with_5_g_l_yeast_extract_15_g_ml_nad_and_15_g_ml_haemin.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `TOGO:M2189`, whose title describes Hib medium as Columbia agar supplemented with 5 g/L yeast extract, 15 ug/ml NAD, and 15 ug/ml haemin. The Togo source does not disclose the Columbia agar base formulation.

## Evidence

The Togo M2189 payload lists 1 L Columbia agar, 5 g/L yeast extract, 15 ug/ml NAD, and 15 ug/ml haemin. The generated record imports yeast extract correctly at 5 g/L, but it converts the two 15 ug/ml growth-factor rows to 15 g/L and converts the 1 L Columbia agar base to 1 g/L.

## Completeness

The normalized source, `data/normalized_yaml/bacterial/hib_medium_columbia_agar_supplemented_with_5_g_l_yeast_extract_15_g_ml_nad_and_15_g_ml_haemin.yaml`, already has a September 2026 repair that represents Columbia agar as a 1000 ml/L opaque commercial base and converts 15 ug/ml NAD and haemin to 15 mg/L. The generated artifact is stale relative to that repaired source.

## Findings

- Columbia agar is represented as `1 G_PER_L` even though the source lists 1 L commercial agar base.
- NAD is off by 1000-fold: 15 ug/ml is 15 mg/L, not 15 g/L.
- Haemin is off by 1000-fold: 15 ug/ml is 15 mg/L, not 15 g/L.
- The generated record lacks the repaired source note explaining that Columbia agar is intentionally retained as an opaque complex base.
- The simple supplementation instruction from the repaired source is not present in the generated artifact.

## Recommended Edits

- Regenerate this artifact from the repaired normalized source.
- Preserve Columbia agar as an opaque 1000 ml/L base.
- Preserve NAD and haemin at 15 mg/L.
- Preserve the preparation step that supplements Columbia agar with yeast extract, NAD, and haemin.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated artifact.
- Confirm no regenerated NAD or haemin row has `G_PER_L` units.

## Additional Notes

None.

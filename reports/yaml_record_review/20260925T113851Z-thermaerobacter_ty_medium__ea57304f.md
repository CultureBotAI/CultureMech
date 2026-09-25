# YAML Record Review: THERMAEROBACTER TY MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermaerobacter_ty_medium__ea57304f.yaml
- Started UTC: 2026-09-25T11:34:05Z
- Finished UTC: 2026-09-25T11:38:51Z
- Verdict: pass with minor issues

## Target

- Generated YAML for JCM Medium J734, THERMAEROBACTER TY MEDIUM.
- The record was merged from `thermaerobacter_ty_medium`.
- The checked sources were the normalized JCM J734 record, MediaDive J734, JCM Medium 734, and the related TOGO M758 transcription.

## Validation

- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The source pointer is grounded to MediaDive/JCM J734.
- JCM Medium 734 is THERMAEROBACTER TY MEDIUM and matches the direct MediaDive J734 payload.
- An exact `mediadive.medium:J734` search used `rg --no-ignore --hidden` scoped to `data`; the direct JCM record and the TOGO M758 JCM transcription are currently generated as separate records.

## Evidence

- JCM Medium 734 lists 1 g tryptone, 2 g yeast extract, 1 g NaCl, 1 g MgSO4 x 7 H2O, 2 g CaCl2 x 2 H2O, and 1 L distilled water.
- JCM Medium 734 states that solid medium is prepared by adding 20.0 g/L gellan gum.
- MediaDive J734 imports the 20.0 g/L gellan gum solid-medium statement as a preparation step.

## Completeness

- The five non-water ingredients match JCM 734.
- The solid-medium preparation note is present.
- The 1 L distilled-water row is missing.
- The duplicate TOGO M758 transcription remains separate.

## Findings

- The 1000 ml JCM/MediaDive distilled-water row is omitted.
- This JCM J734 record is not merged or source-duplicate-linked with the TOGO M758 transcription of the same medium.

## Recommended Edits

- Preserve the 1 L distilled-water row when JCM J734 is regenerated.
- Merge or source-duplicate-link the direct JCM J734 and corrected TOGO M758 records once TOGO's optional gellan gum branch is fixed.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.

## Additional Notes

- None found.

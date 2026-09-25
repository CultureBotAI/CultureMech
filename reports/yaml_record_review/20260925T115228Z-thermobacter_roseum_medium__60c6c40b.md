# YAML Record Review: THERMOBACTER ROSEUM MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermobacter_roseum_medium__60c6c40b.yaml
- Started UTC: 2026-09-25T11:49:20Z
- Finished UTC: 2026-09-25T11:52:28Z
- Verdict: needs curation

## Target

- Generated YAML for JCM Medium J899, THERMOBACTER ROSEUM MEDIUM.
- The record was generated directly from `thermobacter_roseum_medium`.
- The checked sources were JCM Medium 899 and MediaDive J899.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to JCM/MediaDive Medium J899.
- JCM 899 and MediaDive J899 both identify the formula as THERMOBACTER ROSEUM MEDIUM.
- The generated record is a direct single-source import with no merged source duplicates.

## Evidence

- JCM 899 lists a main recipe with 1 ml Vitamin solution, 1 ml Trace element solution, 6 ml 5% Na2S x 9H2O, and 1 L Distilled water.
- Vitamin solution is a separate 1 L stock added at 1 ml/L.
- Trace element solution is a separate stock with 5 ml 25% HCl, 995 ml Distilled water, and milligram-scale metal salts; JCM adds it at 1 ml/L.
- JCM 899 instructs the curator to aseptically and anaerobically add the autoclaved or filter-sterilized supplemental solutions and check pH at 7.5-7.6.

## Completeness

- The JCM preparation steps are present.
- pH 7.5-7.6 is present in preparation text but not mapped to structured `ph_range`.
- The main 1 L distilled-water row is missing.
- Vitamin solution and Trace element solution are flattened at undiluted stock strength.

## Findings

- Vitamin solution was expanded at full 1 L stock strength instead of as a 1 ml/L addition.
- Trace element solution was expanded at full stock strength instead of as a 1 ml/L addition.
- The JCM 899 Trace element solution 5 ml 25% HCl row is absent.
- The 6 ml 5% Na2S x 9H2O solution row was converted to 6 G_PER_L sodium sulfide nonahydrate instead of being retained as a solution addition or converted from percentage stock strength.
- The main 1 L distilled-water row is missing.

## Recommended Edits

- Regenerate JCM 899 with Vitamin solution, Trace element solution, and 5% Na2S x 9H2O retained as stock additions, or expand them only after applying the 1 ml/L, 1 ml/L, and 6 ml/L addition volumes.
- Preserve the Trace element solution 25% HCl row.
- Map the pH 7.5-7.6 check to a structured pH range or explicitly document why it remains preparation text only.
- Preserve the main 1 L distilled-water row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that corrected JCM 899 no longer has undiluted vitamin and trace rows, a 6 G_PER_L Na2S x 9H2O row, or a missing Trace element solution HCl row.

## Additional Notes

- None found.

# YAML Record Review: THERMOANAEROBIUM MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoanaerobium_medium__bc6fb085.yaml
- Started UTC: 2026-09-25T11:45:33Z
- Finished UTC: 2026-09-25T11:49:19Z
- Verdict: needs curation

## Target

- Generated YAML for JCM Medium J671, THERMOANAEROBIUM MEDIUM.
- The record was generated directly from `thermoanaerobium_medium`.
- The checked sources were JCM Medium 671 and MediaDive J671.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to JCM/MediaDive Medium J671.
- JCM 671 and MediaDive J671 both identify the formula as THERMOANAEROBIUM MEDIUM.
- The generated record is a direct single-source import with no merged source duplicates.

## Evidence

- JCM 671 lists a main recipe with 9 ml Trace element solution, 5 ml Trace vitamins, 950 ml Distilled water, 50 ml 10% Glucose solution, and 10 ml 5% Na2S x 9H2O solution.
- MediaDive J671 normalizes those source rows to a 1024 ml main solution.
- Trace element solution is a separate 1 L stock added at 9 ml/L.
- JCM 671 gives an initial pH adjustment to 7.0 and final readjustment to pH 7.2-7.4 if necessary.

## Completeness

- JCM/MediaDive pH 7.3 is present.
- The JCM main and trace-element preparation steps are present.
- The 950 ml main distilled-water row is missing.
- Trace element solution and Trace vitamins are flattened at undiluted stock strength.

## Findings

- Trace element solution was expanded at full 1 L stock strength instead of as a 9 ml/L addition.
- Trace vitamins were expanded at full stock strength instead of as a 5 ml/L addition.
- The main-medium NaCl row was summed with the Trace element solution NaCl row, producing 1.878906 G_PER_L NaCl before applying source-scope dilution.
- The 50 ml 10% Glucose solution row was converted to 50 G_PER_L glucose instead of retaining the solution or applying the percentage stock strength.
- The 10 ml 5% Na2S x 9H2O solution row was converted to 10 G_PER_L sodium sulfide nonahydrate instead of retaining the solution or applying the percentage stock strength.
- The 950 ml main distilled-water row is missing.

## Recommended Edits

- Regenerate JCM 671 with Trace element solution and Trace vitamins retained as stock additions, or expand them only after applying the 9 ml/L and 5 ml/L dilution factors.
- Preserve the 10% Glucose solution and 5% Na2S x 9H2O solution rows as solution additions, or convert them from percentage stock strength before dilution.
- Keep duplicate ingredient names in separate recipe scopes until stock dilution is applied so NaCl is not over-summed.
- Preserve the main 950 ml distilled-water row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that corrected JCM 671 has diluted trace rows and no 50 G_PER_L glucose or 10 G_PER_L Na2S x 9H2O rows.

## Additional Notes

- None found.

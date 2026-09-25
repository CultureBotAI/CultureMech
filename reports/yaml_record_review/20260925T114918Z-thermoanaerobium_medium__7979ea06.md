# YAML Record Review: Thermoanaerobium Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoanaerobium_medium__7979ea06.yaml
- Started UTC: 2026-09-25T11:45:33Z
- Finished UTC: 2026-09-25T11:49:18Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M690, Thermoanaerobium Medium.
- The record was generated directly from `TOGO_M690_Thermoanaerobium_Medium`.
- The checked sources were TOGO M690, JCM Medium 671, and MediaDive J671.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to TOGO Medium M690.
- TOGO M690 cites JCM Medium 671 as its original source.
- This is the TOGO transcription of the JCM 671 source that is also represented by a separate direct JCM/MediaDive generated record.

## Evidence

- TOGO M690 and JCM 671 list a main recipe with 950 ml Distilled water, 9 ml Trace element solution, 5 ml Trace vitamins, 50 ml 10% Glucose solution, and 10 ml 5% Na2S x 9 H2O solution.
- JCM 671 gives an initial pH adjustment to 7.0 and final readjustment to pH 7.2-7.4.
- The trace element solution is a separate 1 L stock added at 9 ml/L.
- JCM 671 points Trace vitamins to another JCM medium rather than listing the vitamin recipe inline.

## Completeness

- TOGO source pH 7.2-7.4 is missing.
- The 950 ml main water row is present but was merged with the trace-element stock water row as 951 G_PER_L.
- Trace element solution, Trace vitamins, 10% Glucose solution, and 5% Na2S x 9H2O solution are present as stock-solution references.
- Trace element solution contents were also duplicated into top-level `ingredients` at stock strength.

## Findings

- TOGO source pH 7.2-7.4 was not mapped to `ph_range`.
- The main 950 ml Distilled water row was summed with the trace-stock 1 L water row, producing a 951 G_PER_L water ingredient.
- The main 1 mg Resazurin row was imported as 1 G_PER_L rather than 0.001 G_PER_L before volume adjustment.
- The main 3 mg FeSO4 x 7H2O row was imported as 3 G_PER_L rather than 0.003 G_PER_L before volume adjustment.
- Trace element solution contents were added as undiluted top-level ingredient rows even though the source uses a 9 ml/L stock addition.
- The 50 ml 10% Glucose solution and 10 ml 5% Na2S x 9H2O solution additions were stored as 50 G_PER_L and 10 G_PER_L instead of being retained as solution additions or converted from percentage stock strength.

## Recommended Edits

- Regenerate TOGO M690 with pH 7.2-7.4 mapped to `ph_range`.
- Keep Trace element solution, Trace vitamins, 10% Glucose solution, and 5% Na2S x 9H2O solution as solution additions, or expand them only after applying their stock strengths and addition volumes.
- Convert milligram rows in the main and stock recipes to G_PER_L by dividing by 1000 before any source-scope dilution.
- Preserve the main 950 ml distilled-water row independently from the trace-element stock water row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that the corrected TOGO M690 record no longer has 951 G_PER_L water, 3 G_PER_L FeSO4 x 7H2O, 1 G_PER_L Resazurin, or undiluted Trace element solution rows in the main ingredient list.

## Additional Notes

- None found.

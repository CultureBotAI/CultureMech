# YAML Record Review: Thermococcus Celer Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermococcus_celer_medium__482c1c27.yaml
- Started UTC: 2026-09-25T11:52:30Z
- Finished UTC: 2026-09-25T11:55:07Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M150, Thermococcus Celer Medium.
- The record was generated directly from `TOGO_M150_Thermococcus_Celer_Medium`.
- The checked sources were TOGO M150, JCM Medium 159, and MediaDive J159.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to TOGO Medium M150.
- TOGO M150 cites JCM Medium 159 as its original source.
- This TOGO transcription is separate from the direct JCM 159 generated record.

## Evidence

- JCM 159 lists 1 L Modified Brock's salt base solution, 40 g NaCl, 2 g Yeast extract, 10 g Sulfur, 0.5 g Na2S x 9H2O, and 1 mg Resazurin.
- JCM 159 gives pH 5.8 and directs pH adjustment with H2SO4.
- Yeast extract is autoclaved as a 10% solution under N2, sulfur is steamed, and Na2S x 9H2O is neutralized as a 5% solution before addition.

## Completeness

- JCM source pH 5.8 is missing.
- The 1 L Modified Brock's salt base solution cross-reference is present in `solutions`.
- The 1 mg Resazurin row is present but stored as 1 G_PER_L.
- The preparation-only H2SO4 and N2 entries were promoted to variable top-level ingredients.

## Findings

- JCM source pH 5.8 was not mapped to `ph_value`.
- The 1 L Modified Brock's salt base solution row was stored as 1 G_PER_L.
- The 1 mg Resazurin row was converted to 1 G_PER_L instead of 0.001 G_PER_L.
- H2SO4 and N2 were added as variable-concentration top-level ingredients even though JCM 159 uses them as a pH-adjusting solution and an autoclaving atmosphere.

## Recommended Edits

- Regenerate TOGO M150 with pH 5.8 mapped to `ph_value`.
- Preserve Modified Brock's salt base solution as a 1 L stock-addition cross-reference to JCM Medium 165.
- Convert the 1 mg Resazurin row to 0.001 G_PER_L.
- Keep H2SO4 and N2 in preparation text rather than as top-level medium components unless a source row gives a final concentration.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that corrected TOGO M150 has no 1 G_PER_L Modified Brock's salt base solution or 1 G_PER_L Resazurin rows.

## Additional Notes

- None found.

# YAML Record Review: THERMOCOCCALES RICH MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermococcales_rich_medium__f0105777.yaml
- Started UTC: 2026-09-25T11:52:30Z
- Finished UTC: 2026-09-25T11:55:06Z
- Verdict: pass with minor issues

## Target

- Generated YAML for JCM Medium J811, THERMOCOCCALES RICH MEDIUM.
- The record was generated directly from `thermococcales_rich_medium`.
- The checked sources were JCM Medium 811 and MediaDive J811.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to JCM/MediaDive Medium J811.
- JCM 811 and MediaDive J811 both identify the formula as THERMOCOCCALES RICH MEDIUM.
- The generated record is a direct single-source import with no merged source duplicates.

## Evidence

- JCM 811 lists PIPES, salts, 3.3 mg Na2WO4 x 2 H2O, 6.8 mg FeCl3 x 6 H2O, 1 g Yeast extract, 4 g Tryptone, 10 g Sulfur, 0.5 g Na2S x 9 H2O, 1 mg Resazurin, and 1 L Distilled water.
- JCM 811 gives pH 6.8 and N2 bubbling for 30 min.
- JCM 811 includes the high-pressure cultivation comment for JCM 16557.

## Completeness

- pH 6.8 is present.
- JCM preparation steps and the JCM 16557 high-pressure comment are present.
- The milligram rows were converted correctly.
- The 1 L Distilled water row is missing.

## Findings

- The only source-fidelity issue found was omission of the 1 L Distilled water row.

## Recommended Edits

- Preserve the 1 L JCM 811 Distilled water row in the generated record.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that the corrected record still has 0.0033 G_PER_L Na2WO4 x 2 H2O and 0.0068 G_PER_L FeCl3 x 6 H2O.

## Additional Notes

- None found.

# YAML Record Review: THERMOANAEROMONAS medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoanaeromonas_medium__b7e31a5b.yaml
- Started UTC: 2026-09-25T11:49:20Z
- Finished UTC: 2026-09-25T11:52:27Z
- Verdict: needs curation

## Target

- Generated YAML for KOMODO Medium 963 and DSMZ Medium 963, THERMOANAEROMONAS MEDIUM.
- The record was merged from `KOMODO_963_THERMOANAEROMONAS_medium` and `thermoanaeromonas_medium`.
- The checked sources were the normalized KOMODO 963 and DSMZ 963 records, MediaDive 963, and DSMZ Medium 963.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to KOMODO Medium 963, with explicit DSMZ Medium 963 provenance through `mediadive.medium:963`.
- The direct DSMZ 963 source record and the KOMODO 963 record represent the same DSMZ formulation.
- MediaDive and DSMZ both identify Medium 963 as THERMOANAEROMONAS MEDIUM with final pH 6.5.

## Evidence

- DSMZ 963 lists a 1011 ml main recipe with 10 ml Trace element solution, 1 ml Wolin's vitamin solution (10x), and 1000 ml Distilled water.
- Trace element solution is a 1 L stock added at 10 ml/L.
- Wolin's vitamin solution (10x) is a 1 L stock added at 1 ml/L.
- DSMZ 963 gives an 80% N2 plus 20% CO2 anoxic preparation, initial bicarbonate pH adjustment to 6.8-7.0, and final complete-medium pH 6.5.

## Completeness

- Final pH 6.5 and the intermediate 6.8-7.0 adjustment are both present as top-level structured pH values.
- The DSMZ preparation steps are missing.
- The main 1000 ml distilled-water row is missing.
- Trace element solution and Wolin's vitamin solution (10x) are flattened at undiluted stock strength.

## Findings

- The merged record places both the final pH 6.5 and the intermediate 6.8-7.0 adjustment in top-level pH slots without distinguishing their process roles.
- The DSMZ preparation step that describes N2-CO2 gassing, bicarbonate, thiosulfate, vitamin, and cysteine addition is absent.
- Trace element solution was expanded at full 1 L stock strength instead of as a 10 ml/L addition.
- Wolin's vitamin solution (10x) was expanded at full 1 L stock strength instead of as a 1 ml/L addition.
- Main-medium NaCl and CaCl2 x 2 H2O rows were summed with separate Trace element solution rows before source-scope dilution was applied.
- The 1000 ml main distilled-water row is missing.

## Recommended Edits

- Regenerate DSMZ 963 with Trace element solution and Wolin's vitamin solution (10x) retained as stock additions, or expand them only after applying the 10 ml/L and 1 ml/L dilution factors.
- Keep duplicate ingredient names in separate recipe scopes until stock dilution is applied so NaCl and CaCl2 are not over-summed.
- Restore the DSMZ preparation text and keep the 6.8-7.0 bicarbonate adjustment separate from the final pH 6.5.
- Preserve the main 1000 ml distilled-water row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that corrected DSMZ 963 no longer has undiluted Trace element solution or Wolin vitamin rows in the main ingredient list.

## Additional Notes

- None found.

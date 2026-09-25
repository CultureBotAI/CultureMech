# YAML Record Review: THERMUS_MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/THERMUS_MEDIUM.yaml
- Started UTC: 2026-09-25T11:24:56Z
- Finished UTC: 2026-09-25T11:28:20Z
- Verdict: needs curation

## Target

- Generated YAML for KOMODO Medium 1033, THERMUS medium.
- The record was merged from `KOMODO_1033_THERMUS_medium`.
- The checked sources were the normalized KOMODO 1033 row, MediaDive 1033, and DSMZ Medium 1033.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The source pointer is grounded to KOMODO 1033 and its notes point to DSMZ Medium 1033 through `mediadive.medium:1033`.
- The KOMODO import copied ingredients from DSMZ Medium 1033.
- Direct DSMZ/MediaDive 1033 and TOGO M2298 records exist separately instead of being merged or duplicate-linked with this KOMODO record.

## Evidence

- DSMZ/MediaDive 1033 lists 0.1 g/L nitrilotriacetic acid, 0.06 g/L CaSO4 x 2 H2O, 0.1 g/L MgSO4 x 7 H2O, 0.008 g/L NaCl, 0.1 g/L KNO3, 0.69 g/L NaNO3, 0.1 g/L Na2HPO4, 10 ml/l Traceelements Solution, 10 ml/l 0.17 mM FeCl3 x 6 H2O, 1 g/L tryptone, 1 g/L yeast extract, 15 g/L agar, and 1000 ml Distilled water.
- MediaDive 1033 lists Traceelements Solution as a 1 L stock containing 0.22 g MnSO4 x H2O, 0.05 g ZnSO4 x 7 H2O, 0.05 g H3BO3, 2.5 mg CuSO4 x 5 H2O, 2.5 mg Na2MoO4 x 2 H2O, and 4.6 mg CoCl2 x 6 H2O.
- DSMZ Medium 1033 gives pH 8.2 and the preparation steps for dissolving NTA first, adjusting to pH 8.0, dissolving the rest of the ingredients, adjusting to pH 8.2, and autoclaving.

## Completeness

- pH 8.2 is present.
- The 1000 ml final-medium water row is missing.
- The DSMZ preparation steps are missing.
- Traceelements Solution was expanded at undiluted stock strength.

## Findings

- MnSO4 x H2O, ZnSO4 x 7 H2O, H3BO3, CuSO4 x 5 H2O, Na2MoO4 x 2 H2O, and CoCl2 x 6 H2O are copied from the 10 ml/l Traceelements Solution stock as if the full 1 L stock were present in 1 L final medium.
- The 1000 ml Distilled water row from DSMZ 1033 is omitted.
- This KOMODO 1033 record is not merged with the direct DSMZ/MediaDive 1033 import or the TOGO M2298 DSMZ 1033 transcription.

## Recommended Edits

- Regenerate KOMODO 1033 with Traceelements Solution kept as a 10 ml/l stock addition, or expand it only after applying the 10 ml/l dilution.
- Preserve the 1000 ml Distilled water row and DSMZ preparation steps.
- Merge or explicitly duplicate-link the KOMODO, direct DSMZ/MediaDive, and TOGO 1033 records after all three share the same corrected stock model.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that DSMZ 1033 and KOMODO 1033 no longer diverge as independent exact `mediadive.medium:1033` records.

## Additional Notes

- None found.

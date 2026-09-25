# YAML Record Review: thermus_medium__917b7fab

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermus_medium__917b7fab.yaml
- Started UTC: 2026-09-25T11:16:58Z
- Finished UTC: 2026-09-25T11:21:05Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M1880, Thermus medium.
- The record was merged from `TOGO_M1880_Thermus_medium`.
- The checked sources were TOGO M1880, NBRC M1124, and the referenced TOGO M1879 trace-elements source.

## Validation

- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The source pointer is grounded to TOGO M1880, which points at the NBRC_M1124-2 branch of NBRC M1124.
- NBRC_M1124-2 is a solid-medium branch of the same NBRC M1124 Thermus medium reviewed in `thermus_medium__51bec529`.
- TOGO M1880 records pH 7.5 and cross-references TOGO M1879 for the 10 ml Trace elements solution.

## Evidence

- NBRC M1124 lists 1 g Bacto Yeast Extract, 1 g Bacto Tryptone, 1 g sodium glutamate monohydrate, 0.06 g CaSO4 x 2 H2O, 0.1 g MgSO4 x 7 H2O, 0.008 g NaCl, 0.1 g KNO3, 0.69 g NaNO3, 0.11 g Na2HPO4, 1.24 g Na2S2O3 x 5 H2O, 10 ml Trace elements solution, 8 g Gelrite if needed, 1 L Distilled water, and pH adjustment to 7.5 with NaOH.
- NBRC M1124 also states that solid medium is made from equal volumes of separately autoclaved 1.6% Gelrite and double-strength liquid medium containing 2 g/L MgSO4 x 7 H2O.
- TOGO M1880 carries Gelrite, 2 g MgSO4 x 7 H2O, Na2S2O3 x 5 H2O, and a 10 ml `*Trace elements solution` cross-reference to M1879.

## Completeness

- The NBRC_M1124-2 source rows are present at the same masses emitted by TOGO.
- Source pH 7.5 is missing.
- The record has Gelrite at 8 g/L but is still typed as `LIQUID`.
- The 10 ml Trace elements solution addition is present only as a `G_PER_L` solution placeholder.

## Findings

- This record should be a solid variant of the NBRC M1124 Thermus medium rather than a separate liquid base recipe.
- The 2 g/L MgSO4 x 7 H2O value comes from the double-strength liquid pre-mix and needs to be reconciled with the equal-volume Gelrite dilution before it is treated as a final-medium concentration.
- The 10 ml Trace elements solution addition is represented as a 10 g/L placeholder.
- The 1 L source water row is represented as 1 g/L.

## Recommended Edits

- Regenerate TOGO M1880 as a solid-medium variant under the NBRC M1124 Thermus medium parent.
- Preserve pH 7.5 and the equal-volume Gelrite/double-strength preparation text.
- Keep the M1879 trace solution as a 10 ml/l stock addition or link to the M1879 stock without typing that volume as `G_PER_L`.
- Recalculate or document the final MgSO4 x 7 H2O concentration for the solid formulation.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that the repaired NBRC M1124 and M1124-2 records are connected as parent and variant instead of independent base media.

## Additional Notes

- None found.

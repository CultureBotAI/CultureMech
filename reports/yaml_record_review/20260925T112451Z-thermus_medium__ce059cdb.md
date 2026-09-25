# YAML Record Review: thermus_medium__ce059cdb

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermus_medium__ce059cdb.yaml
- Started UTC: 2026-09-25T11:21:09Z
- Finished UTC: 2026-09-25T11:24:51Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M1860, Thermus medium.
- The record was merged from `TOGO_M1860_Thermus_medium`.
- The checked sources were TOGO M1860 and NBRC M1104.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 after the startup line only and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The source pointer is grounded to TOGO M1860, which points at NBRC M1104.
- TOGO M1860 records pH 7.5 source metadata.
- This NBRC Thermus medium has sodium glutamate, optional 20 g agar, and an internally defined 10 ml Trace elements solution, but lacks the thiosulfate row present in NBRC M1129.

## Evidence

- NBRC M1104 lists 1 L Distilled water, 1 g Bacto Yeast Extract, 1 g Bacto Tryptone, 1 g sodium glutamate monohydrate, 0.06 g CaSO4 x 2 H2O, 0.1 g MgSO4 x 7 H2O, 0.008 g NaCl, 0.1 g KNO3, 0.69 g NaNO3, 0.11 g Na2HPO4, 10 ml Trace elements solution, 20 g agar if needed, and pH adjustment to 7.5 with NaOH.
- The Trace elements solution is a 1 L stock containing 12.8 g NTA, 1.35 g FeCl3 x 6 H2O, 0.1 g MnCl2 x 4 H2O, 0.024 g CoCl2 x 6 H2O, 0.1 g CaCl2 x 2 H2O, 0.1 g ZnCl2, 0.025 g CuCl2 x 2 H2O, 0.01 g H3BO3, 0.024 g Na2MoO4 x 2 H2O, 1 g NaCl, 0.12 g NiCl2 x 6 H2O, 0.004 g Na2SeO4, and 0.004 g Na2WO4.
- NBRC gives Trace elements solution preparation text to dissolve NTA first, adjust that stock to pH 6.5 with NaOH, add minerals, and set the final stock to pH 7.0.

## Completeness

- The source main-medium solutes and the optional 20 g agar row are present.
- Source pH 7.5 and the trace-stock preparation notes are missing.
- The 10 ml Trace elements solution row is present as a `solutions` placeholder, but it is typed as 10 g/L instead of as a 10 ml/l stock addition.

## Findings

- Trace elements solution was flattened into the final medium at whole-stock strength even though the source adds only 10 ml/l.
- Stock NaCl was summed with main-medium NaCl, yielding 1.008 g/L instead of preserving the 0.008 g/L main row and the separate 10 ml/l trace stock.
- The generated water row is 2.0 g/L because the 1 L main-medium water and 1 L trace-stock water were both misread as 1 g/L and summed.
- Trace-stock rows such as 12.8 g/L NTA, 1.35 g/L FeCl3 x 6 H2O, and 0.12 g/L NiCl2 x 6 H2O are stock concentrations, not final-medium concentrations.

## Recommended Edits

- Regenerate TOGO M1860 with Trace elements solution preserved as a 10 ml/l stock addition or expanded only after applying the 10 ml/l dilution.
- Restore pH 7.5 and the NBRC preparation text for the trace stock.
- Keep the optional agar instruction modeled as a solid variant or as an explicitly optional solidifying component rather than letting it obscure the liquid parent.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that the repaired final medium no longer contains 2 g/L water, 1.008 g/L NaCl, or undiluted Trace elements solution rows.

## Additional Notes

- None found.

# YAML Record Review: thermovibrio_ammonificans_medium__6f230cd3

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermovibrio_ammonificans_medium__6f230cd3.yaml
- Started UTC: 2026-09-25T11:00:15Z
- Finished UTC: 2026-09-25T11:04:36Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M365, Thermovibrio Ammonificans Medium, merged with TOGO Medium M440, TB2 Medium.
- The record was merged from `TOGO_M365_Thermovibrio_Ammonificans_Medium` and `TOGO_M440_TB2_Medium`.
- The checked sources were TOGO M365, TOGO M440, MediaDive/JCM J371, and the JCM 371 page.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 after the startup line only and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- TOGO M365 correctly points to JCM_M371, Thermovibrio Ammonificans Medium.
- TOGO M440 is not an exact duplicate of M365; it is a TB2 variant that uses Medium 371 with 30 g/l final NaCl and an additional 4 ml/l 3% Na2S x 9 H2O solution.
- The generated record lacks the pH 5.5 and preparation text available from the JCM 371 source.

## Evidence

- JCM/MediaDive J371 defines Thermovibrio Ammonificans Medium as 750 ml water plus 250 ml Synthetic seawater (2 x), 10 ml Trace minerals, 6.15 g NaCl, 0.5 g KH2PO4, 0.375 g CaCl2 x 2 H2O, 10 mg ammonium sulfate, 0.025 mg KI, 0.1 mg Na2WO2 x 2 H2O, 2 mg NiCl2 x 6 H2O, 1 g KNO3, 5 g MES, 0.5 g Na2S x 9 H2O, and 1 mg resazurin.
- The JCM 371 preparation adjusts pH to 5.5, uses an H2/CO2 gas mixture, and adds separately sterilized KNO3 and MES before pressurizing inoculated bottles to 200 kPa H2/CO2.
- TOGO M440 states that TB2 uses Medium 371 supplemented with 30 g/l final NaCl and an additional 4 ml/l neutralized 3% Na2S x 9 H2O solution before inoculation.

## Completeness

- The TOGO base ingredients and gas placeholders are present.
- pH 5.5 and the JCM/TOGO preparation comment were not imported.
- Synthetic seawater and Trace minerals are retained only as empty solution placeholders with mass-per-liter units.

## Findings

- M440 was merged as a duplicate of M365 even though its 30 g/l NaCl and extra Na2S x 9 H2O stock make it a TB2 variant of JCM 371, not the base formula.
- Multiple TOGO mg rows were imported as g/L rows in the generated base record: 1 mg resazurin became 1 g/L, 2 mg NiCl2 x 6 H2O became 2 g/L, 10 mg ammonium sulfate became 10 g/L, 0.1 mg Na2WO2 x 2 H2O became 0.1 g/L, and 0.025 mg KI became 0.025 g/L.
- The 250 ml Synthetic seawater and 10 ml Trace minerals additions were moved to empty solution placeholders with G_PER_L units instead of volume units or correctly expanded diluted stock rows.
- The exact ignored/hidden source-ID search found a separate direct JCM J371 merged record, `thermovibrio_ammonificans_medium__75e77987`, so the TOGO and direct JCM records still need to be reconciled.

## Recommended Edits

- Split TOGO M440 into a TB2 variant of the JCM 371 parent instead of merging it as a source duplicate of M365.
- Re-import M365 with mg units preserved, pH 5.5 retained, and the JCM preparation comment retained as preparation steps.
- Model Synthetic seawater as a 250 ml/l stock and Trace minerals as a 10 ml/l stock, or expand them only after applying those dilutions.
- Reconcile the TOGO M365/M440 record with the direct JCM J371/J440 record after the quantitative formula and TB2 variant modeling are fixed.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that M365 has the JCM 371 base formula and that M440 contributes only a TB2 variant with 30 g/l final NaCl and the additional 3% Na2S x 9 H2O solution.

## Additional Notes

- None found.

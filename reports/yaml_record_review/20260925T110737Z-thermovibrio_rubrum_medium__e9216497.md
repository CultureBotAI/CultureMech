# YAML Record Review: thermovibrio_rubrum_medium__e9216497

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermovibrio_rubrum_medium__e9216497.yaml
- Started UTC: 2026-09-25T11:05:02Z
- Finished UTC: 2026-09-25T11:07:37Z
- Verdict: needs curation

## Target

- Generated YAML for JCM Medium J322, THERMOVIBRIO RUBRUM MEDIUM.
- The record was merged from `thermovibrio_rubrum_medium`.
- The checked sources were MediaDive REST entry J322 and the JCM Medium 322 page.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The source record is correctly identified as MediaDive/JCM Medium J322.
- pH 6.8 and the JCM H2/CO2 preparation step are retained.
- The exact ignored/hidden source-ID search found no other generated merged record for `mediadive.medium:J322` in the generated/normalized YAML corpus.

## Evidence

- MediaDive/JCM J322 defines a 1000 ml main solution with 500 ml Synthetic seawater (2 x), 500 ml distilled water, 0.5 g KH2PO4, 0.25 g ammonium sulfate, 1 g KNO3, 0.5 g Na2S x 9 H2O, and 1 mg resazurin.
- Synthetic seawater (2 x) is a 1000 ml stock recipe used at 500 ml/l in the main medium.
- The source preparation adjusts pH to 6.5-7.0, separately autoclaves KNO3 and neutralized Na2S x 9 H2O solutions under N2, and pressurizes inoculated bottles to 200 kPa H2/CO2.

## Completeness

- The pH and JCM preparation step are present.
- The generated record omits the explicit 500 ml water row.
- Synthetic seawater (2 x) was expanded as full-strength top-level stock rows rather than a 500 ml/l stock addition or half-strength final seawater rows.

## Findings

- The top-level salts from Synthetic seawater are about twofold too high for the JCM 322 final medium. The generated formula lists the 2 x stock concentrations directly, including 55.4 g/L NaCl, 14 g/L MgSO4 x 7 H2O, 11 g/L MgCl2 x 6 H2O, and 1.5 g/L CaCl2 x 2 H2O, even though the source adds only 500 ml of this stock per liter.
- Because the stock rows were flattened, the final formula no longer records that half of the main medium is the 2 x synthetic seawater stock and half is distilled water.

## Recommended Edits

- Regenerate JCM 322 with Synthetic seawater (2 x) represented as a 500 ml/l stock addition, or expand the stock rows after applying the 0.5 dilution.
- Restore the explicit 500 ml water row if direct JCM imports are expected to retain source water.
- Keep the pH 6.8 and JCM preparation text that already match the source.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare the regenerated seawater salts against MediaDive/JCM J322 and verify that each 2 x stock concentration is diluted by half in the final medium.

## Additional Notes

- None found.

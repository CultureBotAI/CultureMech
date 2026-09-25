# YAML Record Review: thermotoga_ye_medium__6e3df876

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermotoga_ye_medium__6e3df876.yaml
- Started UTC: 2026-09-25T11:00:13Z
- Finished UTC: 2026-09-25T11:04:34Z
- Verdict: needs curation

## Target

- Generated YAML for JCM Medium J320, THERMOTOGA YE MEDIUM.
- The record was merged from `thermotoga_ye_medium`.
- The checked sources were MediaDive REST entry J320 and the JCM Medium 320 page.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 after the startup line only and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The direct source record is correctly identified as MediaDive/JCM Medium J320.
- pH 6.5 and the JCM anaerobic preparation step are retained.
- The exact ignored/hidden source-ID search found no other generated merged record for `mediadive.medium:J320` in the generated/normalized YAML corpus.

## Evidence

- MediaDive/JCM J320 defines a 1020 ml main solution with 1000 ml water plus 10 ml/l Trace minerals, 10 ml/l Trace vitamins, 2 g yeast extract, 20 g NaCl, 3 g MgCl2 x 6 H2O, 6 g MgSO4 x 7 H2O, 1 g ammonium sulfate, 0.3 g CaCl2 x 2 H2O, 0.2 g KH2PO4, 0.5 g KCl, 0.05 g NaBr, 0.025 g H3BO3, 0.02 g SrCl2 x 6 H2O, 0.01 g ferric citrate, 0.5 g Na2S x 9 H2O, and 1 mg resazurin.
- Trace minerals is a 1000 ml JCM stock used at 10 ml/l in the main medium.
- Trace vitamins is a 1000 ml JCM stock used at 10 ml/l in the main medium.

## Completeness

- The pH and JCM preparation text are present.
- The generated record omits the 1000 ml distilled-water row.
- Trace minerals and Trace vitamins were expanded as undiluted top-level stock recipes rather than preserved as 10 ml/l stock additions or expanded after dilution.

## Findings

- The final formula is not quantitatively faithful to JCM 320. NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and H3BO3 have all been summed with undiluted Trace minerals rows even though only 10 ml of Trace minerals are added per liter.
- The 10 ml/l Trace vitamins addition was expanded as a full 1000 ml stock recipe, so each vitamin is about 100-fold too high in the final top-level recipe.
- The formula should not include full-strength Trace minerals ingredients such as 1.5 g/L nitrilotriacetic acid and 0.5 g/L MnSO4 x n H2O at the final-medium top level.

## Recommended Edits

- Regenerate JCM 320 with Trace minerals and Trace vitamins represented as 10 ml/l additions, or with each stock row expanded only after the correct 10 ml/l dilution is applied.
- Stop summing main-medium NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and H3BO3 with undiluted Trace minerals stock rows.
- Restore the explicit 1000 ml water row if direct JCM imports are expected to retain source water.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare regenerated vitamin and trace-mineral concentrations against MediaDive/JCM J320 and verify that the Trace minerals and Trace vitamins stocks contribute only 10 ml/l each.

## Additional Notes

- None found.

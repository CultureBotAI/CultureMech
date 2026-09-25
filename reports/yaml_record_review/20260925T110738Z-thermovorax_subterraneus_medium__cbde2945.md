# YAML Record Review: thermovorax_subterraneus_medium__cbde2945

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermovorax_subterraneus_medium__cbde2945.yaml
- Started UTC: 2026-09-25T11:05:03Z
- Finished UTC: 2026-09-25T11:07:38Z
- Verdict: needs curation

## Target

- Generated YAML for JCM Medium J713, THERMOVORAX SUBTERRANEUS MEDIUM.
- The record was merged from `thermovorax_subterraneus_medium`.
- The checked sources were MediaDive REST entry J713 and the JCM Medium 713 page.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 after the startup line only and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The source record is correctly identified as MediaDive/JCM Medium J713.
- The JCM/MediaDive preparation steps for Solutions A, B, C, Trace mineral solution, and Se-W solution are present.
- The exact ignored/hidden source-ID search found no other generated merged record for `mediadive.medium:J713` in the generated/normalized YAML corpus.

## Evidence

- MediaDive/JCM J713 is a multi-solution recipe: 45 ml Solution A are combined with 2.5 ml Solution B and 2.5 ml Solution C to complete the medium in each vessel.
- Solution B is itself a 50 ml stock containing NH4Cl, NaCl, CaCl2 x 2 H2O, MgCl2 x 6 H2O, 1 ml Trace mineral solution, 1 ml Vitamin solution, 1 ml Se-W solution, and 47 ml water.
- Solution C is a 50 ml stock containing L-Cysteine HCl x H2O, yeast extract, NaHCO3, 49 ml water, and 1 ml of 24% Na2S x 9 H2O.
- Trace mineral solution, Vitamin solution, and Se-W solution are stock solutions nested inside Solution B, not direct final-medium top-level recipes.

## Completeness

- The JCM preparation text is present.
- The generated record flattens Solution A, Solution B, Solution C, Trace mineral solution, Vitamin solution, and Se-W solution to one top-level ingredient list.
- Water rows from Solution A, Solution B, Solution C, and the nested stocks are omitted.

## Findings

- The final formula is not quantitatively faithful to JCM 713. Solution B and Solution C are added at 2.5 ml per 50 ml final medium, but the generated record carries their 50 ml stock concentrations directly, including 6 g/L NH4Cl, 6 g/L NaCl, 2.2 g/L CaCl2 x 2 H2O, 10 g/L L-Cysteine HCl x H2O, 4 g/L yeast extract, and 8 g/L NaHCO3.
- Trace mineral solution, Vitamin solution, and Se-W solution are nested inside Solution B at 1 ml per 50 ml Solution B, then Solution B is added at 2.5 ml per 50 ml final medium; the generated record instead expands all three inner stocks at full stock strength.
- Solution C's 1 ml of 24% Na2S x 9 H2O is not represented as a solution addition or as a correctly diluted final Na2S x 9 H2O amount.

## Recommended Edits

- Regenerate JCM 713 as a multi-solution recipe that preserves Solution A, Solution B, and Solution C and records the final 45 ml plus 2.5 ml plus 2.5 ml assembly step.
- Keep Trace mineral solution, Vitamin solution, and Se-W solution nested under Solution B, or expand them only after both the 1 ml/50 ml Solution B dilution and the 2.5 ml/50 ml final-medium dilution are applied.
- Model the 24% Na2S x 9 H2O addition in Solution C as a solution row or as a correctly diluted concentration.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare the regenerated formula against JCM 713 and verify that no Solution B, Solution C, trace, vitamin, or Se-W stock row appears at full stock strength in the final medium.

## Additional Notes

- None found.

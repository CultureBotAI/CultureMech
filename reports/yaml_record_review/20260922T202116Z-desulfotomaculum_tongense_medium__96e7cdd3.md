# YAML Record Review: desulfotomaculum_tongense_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/desulfotomaculum_tongense_medium__96e7cdd3.yaml
- Started UTC: 2026-09-22T20:18:43Z
- Finished UTC: 2026-09-22T20:21:16Z
- Verdict: needs curation

## Target

Generated MediaRecipe `CultureMech:003311`, `desulfotomaculum_tongense_medium`, from JCM medium J963 through MediaDive.

The generated record has `media_term.id` `mediadive.medium:J963` and links to the JCM 963 recipe.

## Validation

- LinkML open validation: passed.
- Strict validation: passed with 0 error rows.
- LinkML reference validation: passed with 0 checks.
- LinkML term validation: passed.
- Embedded history validation: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged records.

## Identity and Grounding

The MediaDive identity is grounded to JCM 963, `DESULFOTOMACULUM TONGENSE MEDIUM`.

TOGO M1013 is another import of the same original source, `JCM_M963`, but it remains in the separate generated `DESULFOTOMACULUM_TONGENSE_MEDIUM.yaml` output. The MediaDive and TOGO records should be reconciled as the same source recipe after the shared solution-modeling errors are fixed.

## Evidence

The MediaDive J963 payload lists a main solution with Sea Salt, KH2PO4, NH4Cl, sodium pyruvate, 1 mg resazurin, 1000 ml distilled water, 10 ml trace vitamins, 20 ml 8% NaHCO3 solution, and 10 ml 5% Na2S x 9 H2O solution.

MediaDive resolves the trace vitamins stock as its own solution with ten vitamin or growth-factor constituents. The generated record has no `solutions` block and places those ten stock constituents directly in the top-level final formula.

TOGO M1013 preserves the same high-level source structure: 20 ml 8% NaHCO3, 10 ml 5% Na2S x 9H2O, and 10 ml trace vitamins from a referenced stock after the main medium is prepared under N2/CO2.

## Completeness

The target preserves the basal salts, pyruvate, resazurin, pH, and preparation text.

It omits the 1000 ml distilled-water row, does not model any post-autoclave addition as a solution, and expands the trace vitamins stock into direct top-level ingredient rows at stock concentration.

## Findings

1. **The trace vitamin stock was flattened into the final formula.**

   Biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid all come from the trace vitamins stock added at 10 ml per liter.

2. **Two milliliter stock additions became grams per liter.**

   NaHCO3 and Na2S x 9 H2O are present as `20` and `10` `G_PER_L`, matching the 20 ml and 10 ml source addition volumes.

3. **The main water row is missing.**

   Both MediaDive J963 and TOGO M1013 have 1000 ml distilled water in the main solution. The generated MediaDive record has no water row, so the main solution volume cannot be reconstructed.

4. **Exact JCM M963 provider records are split.**

   MediaDive J963 and TOGO M1013 point to the same JCM medium but produce separate generated records, each with provider-specific stock artifacts.

## Recommended Edits

Rebuild the MediaDive J963 import so trace vitamins, 8% NaHCO3, and 5% Na2S x 9 H2O are modeled as after-cooling solution additions with milliliter volumes.

Restore the 1000 ml main water row.

Link MediaDive J963 and TOGO M1013 as the same JCM M963 source recipe and regenerate them into one canonical Tongense medium.

If the trace vitamins stock is expanded, keep its ten constituents under a nested `solutions` entry rather than top-level `ingredients`.

## Follow-up Checks

Compare the regenerated output against MediaDive J963 and TOGO M1013 and confirm that the only post-autoclave top-level additions are three solution references.

Check that the final top-level formula no longer contains stock-only vitamin rows.

Run the focused LinkML open, strict, reference, and term validators on the regenerated record.

## Additional Notes

No source YAML was edited during this review. Exact local searches for the Tongense source family included ignored files.

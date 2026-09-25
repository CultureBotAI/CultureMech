# YAML Record Review: desulfotomaculum_bs_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/desulfotomaculum_bs_medium__98723365.yaml
- Started UTC: 2026-09-22T20:14:16Z
- Finished UTC: 2026-09-22T20:16:30Z
- Verdict: needs curation

## Target

Generated MediaRecipe `CultureMech:003212`, `desulfotomaculum_bs_medium`, from JCM medium J866 through MediaDive.

The generated record has `media_term.id` `mediadive.medium:J866` and links to the JCM 866 recipe page.

## Validation

- LinkML open validation: passed.
- Strict validation: passed with 0 error rows.
- LinkML reference validation: passed with 0 checks.
- LinkML term validation: passed.
- Embedded history validation: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged records.

## Identity and Grounding

The lead identity is grounded to JCM 866, `DESULFOTOMACULUM BS MEDIUM`.

The same JCM source appears through TOGO M903 in `DESULFOTOMACULUM_BS_MEDIUM.yaml`, so the JCM 866 recipe is split across MediaDive and TOGO outputs. The normalized MediaDive source has also been updated with a `TOGO_M904_Bs_107_Medium.yaml` child relationship for the related JCM 867 Bs 107 variant, but this generated YAML predates that September 2026 repair and does not expose the variant relationship.

## Evidence

JCM 866 lists a 940 ml basal solution with 1.0 ml trace metal solution from Medium 294 and 1.0 mg resazurin. After autoclaving, it adds five solutions per 9.4 ml basal aliquot: 0.25 ml of 8% NaHCO3, 0.2 ml of 1 M sodium pyruvate, 0.05 ml trace vitamins from Medium 197, 0.1 ml of 1% freshly prepared sodium dithionite, and 0.04 ml of 5% Na2S x 9 H2O.

MediaDive J866 preserves the same topology and expands trace metal solution and trace vitamins as nested stocks. The generated record has no `solutions` block, drops the 940 ml water row, and lifts every trace metal and vitamin constituent into the top-level final formula.

## Completeness

The basal salts and pH 7.2 are present, and the source preparation text is preserved.

The generated final formula is incomplete and mis-scaled. It loses the trace metal and vitamin solution boundaries, copies the five post-autoclave milliliter additions as direct gram-per-liter rows, and cannot represent that JCM expresses those post-autoclave volumes per 9.4 ml aliquot rather than per liter of bulk basal medium.

## Findings

1. **Trace metal stock constituents are top-level final ingredients.**

   HCl, FeCl2, CoCl2, MnCl2, ZnCl2, H3BO3, Na2MoO4, NiCl2, CuCl2, AlCl3, and Na2WO4 come from the trace metal solution referenced at 1 ml. They should be nested under that stock, not read as direct ingredients in the final medium.

2. **Trace vitamin stock constituents are top-level final ingredients.**

   The ten vitamin and growth-factor rows come from Medium 197 trace vitamins. The source adds only 0.05 ml of that stock per 9.4 ml medium aliquot.

3. **After-cooling aliquot volumes became gram-per-liter ingredient values.**

   NaHCO3, sodium pyruvate, sodium dithionite, and Na2S x 9 H2O have top-level `G_PER_L` values of `0.25`, `0.2`, `0.1`, and `0.04`. Those are milliliter stock additions per 9.4 ml aliquot in JCM 866.

4. **The basal water row is absent.**

   JCM and MediaDive both include 940 ml distilled water in the main recipe. The generated YAML has no distilled-water ingredient or equivalent main-solution volume.

5. **The generated output is stale relative to normalized variant curation.**

   The normalized MediaDive source now links `TOGO_M904_Bs_107_Medium.yaml` as a substituted-component variant of JCM 866. This generated file lacks that relationship because it was last merged before the repair.

## Recommended Edits

Rebuild MediaDive J866 with nested trace metal and trace vitamin solutions and explicit stock additions instead of flattening their formulas into the main ingredient list.

Represent the five post-autoclave additions with their source units and aliquot basis. Resolve whether downstream normalized output should scale the 9.4 ml aliquot additions to final per-liter quantities or keep them as aliquot-level recipe instructions.

Restore the 940 ml main water row.

Regenerate merged YAML from the current normalized source so the Bs 107 child relationship is carried forward, and link the exact TOGO M903 / JCM 866 duplicate to the same canonical record.

## Follow-up Checks

Compare the regenerated output against both JCM 866 and MediaDive J866 and confirm that no trace metal or vitamin stock constituent remains in the top-level ingredient list.

Regenerate JCM 866, TOGO M903, and the JCM 867 Bs 107 variant together and verify that exact duplicates and substituted-component variants are represented separately.

Run the focused LinkML open, strict, reference, and term validators on the regenerated record.

## Additional Notes

No source YAML was edited during this review. Exact local searches for the BS medium used gitignore-independent search.

# YAML Record Review: desulfosporosinus_bsrei1_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/desulfosporosinus_bsrei1_medium__be3de813.yaml
- Started UTC: 2026-09-22T20:04:34Z
- Finished UTC: 2026-09-22T20:07:00Z
- Verdict: needs curation

## Target

Generated MediaRecipe `CultureMech:003211`, `desulfosporosinus_bsrei1_medium`, from JCM medium J865 through MediaDive.

The generated record has `media_term.id` `mediadive.medium:J865` and links directly to the JCM 865 recipe.

## Validation

- LinkML open validation: passed.
- Strict validation: passed with 0 errors.
- LinkML reference validation: passed with 0 checks.
- LinkML term validation: passed.
- Embedded history validation: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged records.

## Identity and Grounding

The MediaDive identity is grounded to JCM medium 865, `DESULFOSPOROSINUS BSREI1 MEDIUM`.

The equivalent TOGO import, `TOGO_M902_Desulfosporosinus_Bsrei1_Medium.yaml`, also cites JCM M865, but it was not linked to this record. Its generated record is instead in the separate `DESULFOSPOROSINUS_BSREI1_MEDIUM.yaml` cluster and was merged with TOGO M814, an Acidophilus / JCM M784 import, so the provider-level identity graph needs re-checking around JCM M865.

## Evidence

The JCM 865 page lists a 910 ml base medium with salts, 1.0 ml trace element solution, yeast extract, L-cysteine, 1.0 mg resazurin, and water. It then instructs adding four anaerobic stocks after cooling:

- 60.0 ml 5% NaHCO3 solution
- 20.0 ml 1 M fructose solution
- 10.0 ml trace vitamins from Medium 197
- 8.0 ml 5% Na2S x 9 H2O solution

The MediaDive J865 payload has the same source topology and resolves the 1.0 ml trace element solution as its own stock recipe. The generated YAML has no `solutions` block and promotes the trace-element stock constituents to top-level final-medium ingredients.

## Completeness

The 910 ml base formula is present and normalized against MediaDive's 1009 ml final volume.

Five source additions are not structurally represented: the 1 ml trace element stock and the four after-cooling additions. Their stock contexts are lost, and the four after-cooling milliliter quantities appear as direct `G_PER_L` rows with values `60`, `20`, `10`, and `8`.

## Findings

1. **The referenced trace-element stock was flattened into the final ingredient list.**

   HCl, FeSO4, H3BO3, MnCl2, CoCl2, NiCl2, CuCl2, ZnSO4, and Na2MoO4 belong to the trace-element stock added at 1 ml. As generated, they read as final-medium concentrations.

2. **After-cooling solution volumes were copied as grams per liter.**

   `NaHCO3`, `Fructose`, `Trace vitamins (see Medium No. 197)`, and `Na2S x 9 H2O` have top-level concentrations of `60`, `20`, `10`, and `8` `G_PER_L`. Those numbers are milliliter additions from the JCM after-cooling table, not mass concentrations.

3. **The generated record has no structured solution for JCM Medium 197 vitamins.**

   The JCM source references Medium 197 for trace vitamins. The target stores only a top-level placeholder ingredient, so CultureMech cannot recover the vitamin formula or the 10 ml stock dose.

4. **The exact TOGO/JCM M865 counterpart is not connected to this MediaDive/JCM J865 record.**

   TOGO M902 has the same original JCM source but emits into a separate generated cluster. That leaves the JCM 865 recipe duplicated across providers and risks cross-merging with the distinct JCM M784 Acidophilus source.

## Recommended Edits

Rebuild the MediaDive J865 import so the trace element recipe is nested under `solutions` and added to the main medium as a 1 ml stock dose.

Model the 60 ml 5% NaHCO3, 20 ml 1 M fructose, 10 ml Medium 197 trace vitamins, and 8 ml 5% Na2S x 9 H2O additions as post-autoclave solution additions instead of top-level gram-per-liter ingredients.

Resolve Medium 197 vitamins as a linked or expanded stock recipe so the trace vitamin placeholder is not the only representation of that addition.

Add equivalence between MediaDive J865, JCM 865, and TOGO M902; re-evaluate the separate TOGO M902 / M814 merge and keep the JCM M784 recipe distinct unless the source establishes equivalence.

## Follow-up Checks

Compare the regenerated YAML against both the JCM 865 page and the MediaDive J865 REST payload and confirm that the main formula has exactly one trace-element stock addition and four after-cooling stock additions.

Regenerate MediaDive J865 and TOGO M902 together and verify that exact JCM M865 duplicates collapse while JCM M784 remains separate.

Run the focused LinkML open, strict, reference, and term validators on the regenerated record.

## Additional Notes

No source YAML was edited during this review. Exact local searches for the BSR.EI1 records included ignored files.

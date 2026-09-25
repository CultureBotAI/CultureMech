# YAML Record Review: Sulfurimonas Hongkongensis Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/sulfurimonas_hongkongensis_medium__c34a692a.yaml
- Started UTC: 2026-09-25T08:35:22Z
- Finished UTC: 2026-09-25T08:37:26Z
- Verdict: needs curation

## Target

- Reviewed generated record `CultureMech:010415` in `data/merge_yaml/merged/sulfurimonas_hongkongensis_medium__c34a692a.yaml`.
- Source: `data/normalized_yaml/bacterial/TOGO_M988_Sulfurimonas_Hongkongensis_Medium.yaml`.
- Media term: `TOGO:M988`, `Sulfurimonas Hongkongensis Medium`.
- Original source: JCM medium 941, `SULFURIMONAS HONGKONGENSIS MEDIUM`.
- Merge fingerprint: `c34a692a0cfa580c3b5a3798d64426becd731be58986d8865115f6d860fbee3f`.

## Validation

- LinkML schema validation passed: `No issues found`.
- Strict validation passed with 0 error rows.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The TOGO `M988` identity matches JCM medium 941, `SULFURIMONAS HONGKONGENSIS MEDIUM`.
- Exact ignored-file-inclusive searches found `CultureMech:010415`, `TOGO:M988`, the `c34a692a0cfa580c3b5a3798d64426becd731be58986d8865115f6d860fbee3f` fingerprint, and `TOGO_M988_Sulfurimonas_Hongkongensis_Medium` in the generated record, the normalized source, and the normalized indexes at expected locations.
- MediaDive `J941` also resolves to the same JCM page and confirms pH 7.0, source `JCM`, and `complex_medium: no`.

## Evidence

- TOGO M988 and JCM 941 agree that the recipe is organized as Solution A through Solution E, with Solution A containing KH2PO4, KNO3, NH4Cl, NaCl, 2 ml SL-4 trace element solution, and 930 ml water.
- TOGO M988 explicitly represents the final mixture as 932 ml Solution A, 10 ml Solution B, 40 ml Solution C, 20 ml Solution D, 1 ml Solution E, and an N2 atmosphere.
- JCM 941 gives `Adjust pH to 7.0 with NaOH` after Solution A.
- JCM 941 instructs separate autoclaving of Solutions A, B, C, and E under N2, filter sterilization of Solution D, combination after sterilization, and storage under N2.
- MediaDive J941 resolves the JCM page into the same Solution A through E stocks and additionally resolves the SL-4 cross-reference to Trace element solution SL-4 with a nested SL-6 trace solution.

## Completeness

- The generated record carries the TOGO M988 ID, the JCM original URL, the main ingredients, a cross-reference for SL-4, and all five solution addition names.
- The generated record does not preserve the pH 7.0 adjustment as `ph_range` or a preparation step.
- The generated record has no `preparation_steps`, so the required N2/autoclave/filter-sterilization workflow is missing.
- The SL-4 cross-reference is retained only as an empty-composition solution and the referenced SL-4/SL-6 trace chemistry from MediaDive J941 is not represented.

## Findings

- The top-level solution additions have corrupted units. TOGO records 932 ml Solution A, 10 ml Solution B, 40 ml Solution C, 20 ml Solution D, and 1 ml Solution E, but the generated YAML stores those as `932`, `10`, `40`, `20`, and `1` `G_PER_L`.
- The solution hierarchy is split into a flat ingredient list plus empty `solutions` stubs. The generated ingredient rows erase which chemicals belong to Solution A, B, C, D, E, and the SL-4 cross-reference, so the final recipe cannot be reconstructed safely.
- The generated `Distilled water` row merged four separate stock waters into `1000.0` `G_PER_L`, losing the 930 ml, 10 ml, 40 ml, and 20 ml stock contexts.
- The medium is marked `medium_type: COMPLEX` and `composition_type: UNDEFINED`, but JCM 941 lists a defined recipe and MediaDive J941 classifies the source as not complex.
- JCM's pH adjustment and sterilization/storage instructions are absent.

## Recommended Edits

- Fix the TOGO import or solution migration for `data/normalized_yaml/bacterial/TOGO_M988_Sulfurimonas_Hongkongensis_Medium.yaml` so main-recipe milliliter solution additions remain milliliter additions, not `G_PER_L` concentrations.
- Preserve Solution A through E as separate subrecipes, including the 2 ml SL-4 addition inside Solution A and the 1 ml 0.1 N H2SO4 addition inside Solution E.
- Preserve the JCM pH 7.0 adjustment and N2/autoclave/filter-sterilization instructions as preparation steps.
- Use the source-backed defined classification for this JCM recipe.
- Regenerate `data/merge_yaml/merged/sulfurimonas_hongkongensis_medium__c34a692a.yaml`; do not hand-edit this generated file.

## Follow-up Checks

- Revalidate the normalized TOGO source after solution-unit and preparation-step fixes.
- Regenerate merged YAML and verify that this record has no `G_PER_L` units on Solution A through E additions.
- Verify whether the SL-4 trace solution should remain a cross-reference to JCM Medium 340 or be expanded through the MediaDive J941/JCM mapping.

## Additional Notes

- Empty optional fields were not treated as defects.
- JCM 941 and MediaDive J941 were checked in addition to TOGO M988.

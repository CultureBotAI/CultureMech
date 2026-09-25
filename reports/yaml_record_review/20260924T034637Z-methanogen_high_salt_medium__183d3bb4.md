# YAML Record Review: methanogen_high_salt_medium__183d3bb4
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanogen_high_salt_medium__183d3bb4.yaml
- Started UTC: 2026-09-24T03:44:31Z
- Finished UTC: 2026-09-24T03:46:37Z
- Verdict: needs curation

## Target
- ID: CultureMech:007634
- Name: methanogen_high_salt_medium
- Label: Methanogen High Salt Medium
- Category: archaea
- Source: TOGO M1114, imported from JCM_M1048-2
- Merge fingerprint: 183d3bb44921c77b75682b1e8b82b9f20a42d91476f3ebabbf1a0fb91c452f0b
- Merged from: TOGO_M1114_Methanogen_High_Salt_Medium
- Maintained owner: data/normalized_yaml/archaea/TOGO_M1114_Methanogen_High_Salt_Medium.yaml

## Validation
- Open schema validation: Passed; no issues found.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; 0 reference checks, all passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The record identity matches TOGO M1114, a JCM_M1048-2 import for the JCM 30226 tetramethylammonium variant of JCM 1048.
- An exhaustive hidden and ignored search for `JCM_M1048`, `JCM_M1048-2`, `TOGO:M1114`, and `CultureMech:007634` found the direct MediaDive J1048 owner, the TOGO M1113 base JCM 1048 import, and this TOGO M1114 variant.
- The base medium, Wolfe's mineral solution, and Trace vitamins references match the JCM 1048 page through TOGO M1114, M257, and M190.

## Evidence
- TOGO M1114 preserves the main JCM 1048 salts, yeast extract, 1 mg Resazurin, 10 ml Wolfe's mineral solution from M257, 10 ml Trace vitamins from M190, and the 5% Na2S x 9 H2O and 5% L-Cysteine HCl x H2O solution additions.
- TOGO M1114 also carries the JCM 1048 comment that strain JCM 30226 should receive 20 mM final tetramethyl ammonium instead of methanol.
- The generated YAML keeps tetramethyl ammonium only as a top-level `VARIABLE` ingredient and drops the 20 mM final concentration.
- The generated `solutions` array contains empty `Unknown solution` stubs for Wolfe's mineral solution, Trace vitamins, 5% Na2S x 9 H2O solution, and 5% L-Cysteine HCl x H2O solution.
- Source milliliter quantities are encoded as `G_PER_L`: 10 ml Wolfe's mineral solution, 10 ml Trace vitamins, 2 ml 5% Na2S x 9 H2O solution, and 10 ml 5% L-Cysteine HCl x H2O solution.
- The TOGO preparation and variant comments are absent from `preparation_steps`.
- TOGO's N2-CO2 atmosphere was imported as variable Carbon dioxide gas and Nitrogen gas top-level ingredients.
- The source has 1 L water and 1 mg Resazurin, but the YAML stores both as `1 G_PER_L`.

## Completeness
- The base salts and tetramethylammonium variant marker are present.
- Wolfe's mineral solution, Trace vitamins, Na2S x 9 H2O solution, and L-Cysteine HCl x H2O solution are unresolved empty placeholders.
- The 20 mM tetramethylammonium concentration and anaerobic preparation instructions are absent.
- Empty optional fields are acceptable, but these empty solution stubs stand in for required source subrecipes.

## Findings
- Major: `data/normalized_yaml/archaea/TOGO_M1114_Methanogen_High_Salt_Medium.yaml` loses the 20 mM final tetramethylammonium concentration that distinguishes JCM_M1048-2 from the base JCM 1048 recipe.
- Major: All four solutions in `data/normalized_yaml/archaea/TOGO_M1114_Methanogen_High_Salt_Medium.yaml` are empty `Unknown solution` placeholders; M257, M190, and the 5% reducing-agent stocks need real formulas or explicit source references.
- Major: Milliliter solution additions and milligram Resazurin are imported with `G_PER_L` units, making 10 ml, 2 ml, and 1 mg values dimensionally wrong.
- Major: The N2-CO2 preparation atmosphere is represented as variable gas ingredients rather than scoped preparation or atmosphere instructions.
- Major: The TOGO comments that define anaerobic boiling, N2-CO2 dispensing, overnight standing, and tetramethylammonium substitution are missing from preparation steps.

## Recommended Edits
- Re-curate `data/normalized_yaml/archaea/TOGO_M1114_Methanogen_High_Salt_Medium.yaml` from TOGO M1114 and the underlying JCM 1048 variant comment.
- Preserve tetramethylammonium as 20 mM final and scope it as the replacement substrate for methanol.
- Resolve Wolfe's mineral solution from TOGO M257 and Trace vitamins from TOGO M190 instead of leaving empty `Unknown solution` stubs.
- Model the 5% Na2S x 9 H2O and 5% L-Cysteine HCl x H2O stocks as 2 ml and 10 ml solution additions.
- Convert the 1 mg Resazurin row to the correct mass concentration rather than `1 G_PER_L`.
- Move N2-CO2 gas handling into preparation or atmosphere fields and restore the JCM preparation prose.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanogen_high_salt_medium__183d3bb4.yaml`.
- Confirm that `Unknown solution` is gone from this TOGO M1114 owner.
- Confirm that tetramethylammonium has a final 20 mM concentration and methanol is not added to the M1114 variant.
- Confirm that milliliter stock additions are not represented as `G_PER_L`.
- Confirm that gas rows are scoped to preparation or atmosphere instead of top-level ingredients.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- The direct MediaDive/JCM J1048 base record and the TOGO M1113 base import should be repaired before deciding how this tetramethylammonium variant should link back to its parent.

# YAML Record Review: methanogen_high_salt_medium__05a62aba
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanogen_high_salt_medium__05a62aba.yaml
- Started UTC: 2026-09-24T03:42:49Z
- Finished UTC: 2026-09-24T03:44:30Z
- Verdict: needs curation

## Target
- ID: CultureMech:000287
- Name: methanogen_high_salt_medium
- Label: METHANOGEN HIGH SALT MEDIUM
- Category: archaea
- Source: JCM, imported through MediaDive as mediadive.medium:J1048
- Merge fingerprint: 05a62aba63781ca08a65dcd41e187db9efa013b16df6a454e6ea40e91e38596a
- Merged from: methanogen_high_salt_medium
- Maintained owner: data/normalized_yaml/archaea/methanogen_high_salt_medium.yaml

## Validation
- Open schema validation: Passed; no issues found.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; 0 reference checks, all passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The ID, label, JCM source URL, and `mediadive.medium:J1048` term identify direct JCM 1048, METHANOGEN HIGH SALT MEDIUM.
- An exhaustive hidden and ignored search for `mediadive.medium:J1048`, `CultureMech:000287`, `JCM_M1048`, and `JCM_M1048-2` found the direct MediaDive owner, a TOGO M1113 import of JCM 1048, and a TOGO M1114 import of the JCM 1048-2 tetramethylammonium variant.
- NiCl2 x 6 H2O is grounded to generic nickel dichloride, and MnSO4 x n H2O is grounded to generic manganese(II) sulfate; both hydrate-bearing source labels need narrower treatment if suitable terms are available.

## Evidence
- JCM 1048 defines a 1 L base medium containing 23.4 g NaCl, 11.0 g MgCl2 x 6 H2O, 3.8 g NaHCO3, NH4Cl, KCl, KH2PO4, CaCl2 x 2 H2O, 10 ml Wolfe's mineral solution from JCM medium 265, 10 ml Trace vitamins from JCM medium 197, 1 mg Resazurin, 1 g Sodium acetate, 2 g Yeast extract, and water.
- The source then instructs users to add, per liter after autoclaving, 10 ml 50% Methanol solution, 10 ml 5% L-Cysteine HCl x H2O solution, and 2 ml 5% Na2S x 9 H2O solution.
- MediaDive preserves Wolfe's mineral solution, Trace vitamins, and nested Trace minerals as reusable solutions under the JCM 1048 main solution.
- The YAML lacks a `solutions` array and flattens Wolfe's mineral solution, Trace vitamins, and the nested Trace minerals into top-level ingredients.
- The post-autoclave milliliter solution additions are encoded as `10 G_PER_L` Methanol, `10 G_PER_L` L-Cysteine HCl x H2O, and `2 G_PER_L` Na2S x 9 H2O rather than as 10 ml, 10 ml, and 2 ml stock additions.
- The duplicate top-level NaCl and CaCl2 x 2 H2O rows created by flattening have been summed across main-medium and trace-mineral scopes.

## Completeness
- The base JCM 1048 ingredients, Wolfe mineral ingredients, trace-vitamin ingredients, trace-mineral ingredients, and JCM preparation text are all present in flattened form.
- The 10 ml Wolfe's mineral solution, 10 ml Trace vitamins, and Trace minerals nesting inside Wolfe's mineral solution are absent structurally.
- The 50% methanol, 5% cysteine, and 5% sulfide post-autoclave solution additions are absent structurally.
- Empty optional fields are acceptable; no optional-field omission was counted as a defect.

## Findings
- Major: `data/normalized_yaml/archaea/methanogen_high_salt_medium.yaml` flattens the 10 ml Wolfe's mineral solution, 10 ml Trace vitamins, and nested Trace minerals instead of modeling the solution additions from JCM 1048.
- Major: NaCl and CaCl2 x 2 H2O are summed across incompatible main-medium and trace-mineral scopes in `data/normalized_yaml/archaea/methanogen_high_salt_medium.yaml`.
- Major: The 50% methanol, 5% cysteine, and 5% sulfide additions are represented as unsupported `G_PER_L` final ingredients rather than as source milliliter stock additions.
- Minor: The Trace minerals preparation step is stored as a top-level pH adjustment and is detached from its stock recipe.
- Minor: Hydrate-specific grounding is incomplete for NiCl2 x 6 H2O and MnSO4 x n H2O.

## Recommended Edits
- Re-curate `data/normalized_yaml/archaea/methanogen_high_salt_medium.yaml` from JCM 1048 plus the referenced JCM 265 and JCM 197 stock formulas.
- Model Wolfe's mineral solution and Trace vitamins as 10 ml solution additions to the JCM 1048 main recipe.
- Model Trace minerals as a nested stock inside Wolfe's mineral solution.
- Keep the post-autoclave 50% methanol, 5% L-Cysteine HCl x H2O, and 5% Na2S x 9 H2O additions as milliliter stock additions, not as grams per liter.
- Remove duplicate-summed NaCl and CaCl2 x 2 H2O rows that cross solution scopes.
- Re-ground NiCl2 x 6 H2O and MnSO4 x n H2O if suitable hydrate-specific CHEBI terms are available.
- After repair, reconcile the direct JCM 1048 record with the TOGO M1113 base import and the TOGO M1114 JCM 30226 tetramethylammonium variant.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanogen_high_salt_medium__05a62aba.yaml`.
- Confirm that Wolfe's mineral solution, Trace vitamins, and Trace minerals appear as nested solution objects or references.
- Confirm that 50% methanol, 5% cysteine, and 5% sulfide additions no longer appear as `10 G_PER_L`, `10 G_PER_L`, and `2 G_PER_L` final rows.
- Confirm that NaCl and CaCl2 x 2 H2O are no longer summed across the main and trace-mineral scopes.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- The JCM 1048 comment for strain JCM 30226 is a strain-specific tetramethylammonium alternative to methanol; it should become either a scoped variant or a discussion item rather than an unscoped base-recipe ingredient.

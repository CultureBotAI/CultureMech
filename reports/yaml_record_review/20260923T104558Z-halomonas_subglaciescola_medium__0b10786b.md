# YAML Record Review: halomonas_subglaciescola_medium__0b10786b

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halomonas_subglaciescola_medium__0b10786b.yaml`
- Started UTC: 2026-09-23T10:45:58Z
- Finished UTC: 2026-09-23T10:47:28Z
- Verdict: needs curation

## Target

Generated merged YAML for Togo Medium M615, `Halomonas Subglaciescola Medium`, imported from the solid-medium branch of JCM medium 607.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches Togo `TOGO:M615`, which points to JCM medium 607 as `JCM_M607-2`.
- An ignored-file-inclusive exact search for `TOGO:M615`, `medium/M615`, `JCM_M607-2`, `jcm_grmd?GRMD=607`, and `TOGO_M615_Halomonas_Subglaciescola_Medium` found the Togo M615 import, the direct JCM J607 import, and the Togo M614 sibling from the same JCM page.
- The MgSO4 x 7 H2O, CaCl2 x 2 H2O, MgCl2 x 6 H2O, KNO3, salt, and agar groundings are appropriate.
- Peptone and yeast extract are intentionally ungrounded undefined ingredients.

## Evidence

- JCM 607 lists a 1 L main solution containing 100 g NaCl, 5 g MgCl2 x 6 H2O, 9.5 g MgSO4 x 7 H2O, 5 g KCl, 0.2 g CaCl2 x 2 H2O, 0.1 g ammonium sulfate, 0.1 g KNO3, 5 g peptone, 1 g yeast extract, and 1 L distilled water.
- The JCM 607 preparation text adjusts the base to pH 7.0, adds 15 g/L agar only for solid medium, autoclaves, cools to 50C, and then adds 20 ml metal solution, 20 ml phosphate solution, and 1 ml filter-sterilized trace vitamins.
- The two 20 ml additions refer to the metal and phosphate solutions defined on JCM 607; the 1 ml trace-vitamin addition points to JCM medium 197.
- Togo M615 preserves the cross-medium additions as 20 ml, 20 ml, and 1 ml reference rows, not as gram-per-liter ingredient concentrations.

## Completeness

- Missing pH: the generated record omits the source pH target of 7.0.
- Mis-scaled water: the 1 L distilled-water row was normalized to `1 G_PER_L`.
- Mis-scaled additions: the 20 ml metal solution, 20 ml phosphate solution, and 1 ml trace-vitamin additions became empty `solutions` with `G_PER_L` concentrations.
- Missing preparation: the generated record has no pH, agarization, autoclaving, cooling, or post-autoclave addition steps.

## Findings

1. The generated Togo M615 record omits the pH 7.0 adjustment from JCM 607.
2. The record treats the source's optional 15 g/L agar instruction as an unconditional `SOLID_AGAR` ingredient.
3. Distilled water was imported as `1 G_PER_L` instead of the 1 L base volume.
4. The three post-autoclave additions are unusable empty `solutions` with 20, 20, and 1 `G_PER_L` concentrations instead of 20 ml, 20 ml, and 1 ml addition volumes.
5. The KNO3 ingredient still carries a legacy `mediaingredientmech_term` even though it is already grounded to CHEBI:63043.

## Recommended Edits

- Add `ph_value: 7.0` and preparation steps for pH adjustment, optional agarization, autoclaving, cooling to 50C, and post-autoclave solution addition.
- Replace distilled water with the correct 1 L final-volume representation.
- Scope the 15 g/L agar row to an explicit solid variant of the JCM 607 base.
- Convert the metal, phosphate, and trace-vitamin references to proper stock-solution additions with milliliter volumes and with compositions resolved from JCM 607 and JCM 197 where possible.
- Replace the stale KNO3 `mediaingredientmech_term` with a CHEBI-keyed MediaIngredientMech link.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Re-run an ignored-file-inclusive exact search for `TOGO:M615`, `JCM_M607-2`, and `jcm_grmd?GRMD=607` after regeneration.
- Verify that the regenerated JCM 607 family keeps Togo M614, Togo M615, and the direct JCM J607 import aligned without merging stock-solution concentrations into the main liter.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.

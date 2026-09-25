# YAML Record Review: halomonas_variabilis_medium__43327f1c

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halomonas_variabilis_medium__43327f1c.yaml`
- Started UTC: 2026-09-23T10:50:37Z
- Finished UTC: 2026-09-23T10:51:32Z
- Verdict: needs curation

## Target

Generated merged YAML for direct MediaDive/JCM medium J604, `HALOMONAS VARIABILIS MEDIUM`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches MediaDive `mediadive.medium:J604` and the JCM 604 source page.
- An ignored-file-inclusive exact search for `mediadive.medium:J604`, `JCM_M604`, `GRMD=604`, and `halomonas_variabilis_medium` found the direct JCM J604 import, the Togo M611 import from the same JCM page, and their two merged outputs.
- MgSO4 x 7 H2O and the core NaCl/KCl salts are grounded appropriately.
- NiCl2 x 6 H2O is grounded too broadly to anhydrous nickel dichloride and needs a hydrate-specific term.
- Proteose peptone is intentionally ungrounded but is missing the source `BD-Difco` qualifier.

## Evidence

- JCM 604 defines a 1 L Halomonas variabilis base with 95 g NaCl, 81 g MgSO4 x 7 H2O, 1 g KCl, 7.5 g yeast extract, 2.5 g Proteose peptone (BD-Difco), 10 ml SL-4 trace element solution, 1 ml trace vitamins from JCM 197, and 1 L distilled water, then instructs pH adjustment to 7.5.
- MediaDive J604 preserves the 10 ml SL-4 and 1 ml trace-vitamin additions as `solution` rows and keeps the SL-6 trace-element recipe nested under SL-4.
- The generated YAML flattens SL-4, nested SL-6, and trace-vitamin stock components into the top-level ingredient list at stock concentrations.
- The generated YAML scales the five base ingredients over a 1011 ml combined volume, producing non-source concentrations such as 93.9664 g/L NaCl and 80.1187 g/L MgSO4 x 7 H2O.

## Completeness

- Missing ingredient: the 1000 ml distilled-water row was dropped, as were the stock water rows.
- Missing topology: the 10 ml SL-4 addition, 100 ml SL-6-in-SL-4 addition, and 1 ml trace-vitamin addition were flattened away.
- Missing qualifier: Proteose peptone lost the `BD-Difco` attribute.
- Missing preparation: the record keeps pH adjustment but omits the JCM default 121 C, 15 min autoclaving.

## Findings

1. The generated direct JCM J604 record flattens SL-4, SL-6, and trace-vitamin stock recipes into the main ingredient list instead of preserving solution boundaries.
2. Stock components are present at stock concentrations instead of being diluted by the 10 ml, 100 ml, and 1 ml addition volumes.
3. The five base ingredients were normalized over 1011 ml, obscuring the source 1 L formula.
4. All distilled-water rows were dropped.
5. Proteose peptone lost the source `BD-Difco` qualifier.
6. NiCl2 x 6 H2O is grounded to anhydrous nickel dichloride rather than to a hydrate-specific term.
7. The JCM default autoclaving semantics are missing.

## Recommended Edits

- Preserve the main, SL-4, SL-6, and trace-vitamin recipes as scoped solutions with the original 10 ml, 100 ml, and 1 ml transfer volumes.
- Restore distilled water with the correct final-volume representation inside each 1 L source solution.
- Keep the base formula at its declared 1 L scale instead of converting it over 1011 ml.
- Restore the `BD-Difco` qualifier on Proteose peptone.
- Re-ground NiCl2 x 6 H2O to a hydrate-specific CHEBI term.
- Add the JCM default 121 C, 15 min autoclaving step if the curation model captures default source sterilization.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:J604`, `TOGO:M611`, and `GRMD=604` after regeneration.
- Verify that regenerated JCM 604 records retain `ph_value: 7.5` and no top-level vitamin or SL-6 ingredients remain in the main recipe.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.

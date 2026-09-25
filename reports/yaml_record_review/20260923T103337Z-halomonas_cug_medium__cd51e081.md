# YAML Record Review: halomonas_cug_medium__cd51e081

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halomonas_cug_medium__cd51e081.yaml`
- Started UTC: 2026-09-23T10:33:37Z
- Finished UTC: 2026-09-23T10:34:10Z
- Verdict: needs curation

## Target

Generated merged YAML for the direct MediaDive/JCM import of JCM medium 1050, `HALOMONAS/CUG MEDIUM`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches MediaDive `mediadive.medium:J1050`.
- JCM now returns no composition for medium 1050, but MediaDive `J1050` and the TOGO M1116/M1117 archived payloads preserve the source formula.
- A gitignore-independent exact search for `mediadive.medium:J1050` and `GRMD=1050` found the direct JCM import plus the related TOGO liquid and solid parses.
- `NaNO3` is grounded to sodium nitrate through `term`, but still has a stale legacy `mediaingredientmech_term` instead of a `mediaingredientmech_chebi_term`.

## Evidence

- The MediaDive J1050 REST payload lists 0.5 g Yeast extract, 0.5 g Peptone, 0.5 g Glucose, 0.5 g Casamino acids with `BD-Difco`, 0.5 g soluble Starch, 0.3 g Sodium pyruvate, 30 g NaCl, 20.1 g Na2SO4, 6 g MgCl2 x 6 H2O, 1 g KCl, 0.5 g CaCl2 x 2 H2O, 0.3 g K2HPO4, 0.05 g MgSO4 x 7 H2O, 0.05 g NaNO3, and 1000 ml Distilled water.
- The generated direct record preserves the source pH of 7.5 and all non-water numeric solute concentrations.
- The generated preparation step combines the base pH instruction with the separate 15 g/L agar solid-medium instruction.

## Completeness

- Missing ingredient: the explicit 1000 ml distilled-water row was dropped.
- Missing qualifier: Casamino acids lost `BD-Difco`.
- Missing soluble qualifier: MediaDive records Starch with `attribute: soluble`, but the generated row is only `Starch`.
- Missing variant structure: the 15 g/L solid agar variant is present only as prose inside an `ADJUST_PH` step on the liquid base record.

## Findings

1. The generated direct record omits distilled water and the final 1000 ml volume as structured data.
2. The Casamino acids and Starch ingredients lost source qualifiers that distinguish `BD-Difco` Casamino acids and soluble starch.
3. The `NaNO3` row still carries `mediaingredientmech_term: MediaIngredientMech:000171` even though the row has a valid CHEBI sodium nitrate grounding.
4. The solid-medium agar sentence is unscoped and should be represented by a linked 15 g/L solid variant, not embedded in the liquid base pH adjustment.

## Recommended Edits

- Add distilled water with the correct final-volume representation.
- Restore the `BD-Difco` and soluble-starch qualifiers.
- Replace the stale `NaNO3` `mediaingredientmech_term` with an id-safe CHEBI-keyed link.
- Keep J1050 as the liquid base and link the TOGO M1117 agar form as the solid variant.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Verify that the M1116/M1117 TOGO records and the direct MediaDive/JCM J1050 record reconcile to one liquid base plus one 15 g/L agar variant.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:J1050`, `TOGO:M1116`, and `TOGO:M1117` after regeneration.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.

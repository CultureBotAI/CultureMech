# YAML Record Review: halophile_starch_casein_medium__a671ca4d

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halophile_starch_casein_medium__a671ca4d.yaml`
- Started UTC: 2026-09-23T10:55:52Z
- Finished UTC: 2026-09-23T10:56:27Z
- Verdict: needs curation

## Target

Generated merged YAML for the Togo Medium M1061 liquid branch of JCM medium 1005, `Halophile Starch-Casein Medium`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches Togo `TOGO:M1061`, which points to JCM medium 1005 as `JCM_M1005`.
- An ignored-file-inclusive exact search for `TOGO:M1061`, `JCM_M1005`, and `jcm_grmd?GRMD=1005` found this Togo M1061 import, the Togo M1062 solid branch, and the direct MediaDive/JCM J1005 import.
- The MgSO4 x 7 H2O, FeSO4 x 7 H2O, K2HPO4, NaCl, starch, and NaOH groundings are appropriate.
- Casein is intentionally ungrounded as an undefined ingredient.
- KNO3 still carries a legacy `mediaingredientmech_term` despite having a current CHEBI grounding.

## Evidence

- JCM 1005 lists a 1 L formula with 100 g soluble starch, 10 g casein, 10 g KNO3, 5 g K2HPO4, 5 g MgSO4 x 7 H2O, 0.1 g FeSO4 x 7 H2O, and 200 g NaCl.
- JCM 1005 instructs bringing the medium to 1.0 L with distilled water, adding 20 g/L agar only for solid medium, autoclaving, and adjusting pH to 7.2-7.5 with NaOH.
- Togo M1061 preserves the source pH range as `7.2-7.5`, keeps agar out of the liquid component list, and records NaOH only as part of the preparation comment.

## Completeness

- Missing pH: the generated record has no `ph_value` for the 7.2-7.5 source range.
- Mis-scaled water: the 1 L distilled-water row became `1 G_PER_L`.
- Missing preparation: the generated record has no final-volume, autoclave, or pH-adjustment steps.
- Misplaced pH reagent: NaOH was promoted from the pH-adjustment instruction to a variable top-level ingredient.

## Findings

1. The generated Togo M1061 record omits the 7.2-7.5 pH range.
2. Distilled water was imported as `1 G_PER_L` instead of the 1 L final volume.
3. NaOH is modeled as a variable ingredient instead of as the reagent named by the pH-adjustment step.
4. Preparation steps are missing entirely.
5. KNO3 still carries a legacy `mediaingredientmech_term`.

## Recommended Edits

- Add the 7.2-7.5 source pH range in the available structured pH representation.
- Replace the water row with the correct 1 L final-volume representation.
- Remove NaOH from `ingredients` and represent pH adjustment with NaOH as a preparation step.
- Add preparation steps for final volume, autoclaving, and pH adjustment.
- Replace the stale KNO3 `mediaingredientmech_term` with a CHEBI-keyed MediaIngredientMech link.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Re-run an ignored-file-inclusive exact search for `TOGO:M1061`, `TOGO:M1062`, and `mediadive.medium:J1005` after regeneration.
- Verify that regenerated M1061 stays liquid, while the 20 g/L agar instruction is represented only on the M1062 solid branch.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.

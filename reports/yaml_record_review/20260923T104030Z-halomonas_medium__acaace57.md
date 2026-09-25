# YAML Record Review: halomonas_medium__acaace57

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halomonas_medium__acaace57.yaml`
- Started UTC: 2026-09-23T10:40:30Z
- Finished UTC: 2026-09-23T10:43:03Z
- Verdict: needs curation

## Target

Generated merged YAML for Togo Medium M616, `Halomonas Medium`, imported from historical JCM medium 608.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches Togo `TOGO:M616`, which points to JCM medium 608.
- An ignored-file-inclusive exact search for `TOGO:M616`, `medium/M616`, `JCM_M608`, `mediadive.medium:J608`, and `jcm_grmd?GRMD=608` found the Togo M616 import, the direct MediaDive/JCM J608 import, and their two merged outputs.
- The direct JCM J608 record is a duplicate of the same formulation and can be reconciled with this Togo-derived record after pH adjustment and water-volume handling are normalized.
- The hydrate-sensitive magnesium sulfate heptahydrate and ferrous ammonium sulfate hexahydrate groundings are appropriate.
- Potassium hydroxide is grounded correctly in isolation but is a pH-adjustment reagent rather than a recipe ingredient in the source text.

## Evidence

- JCM 608 lists the same 1 L Halomonas Medium formula: 80 g NaCl, 7.5 g Casamino acids (BD-Difco), 5 g Proteose peptone No. 3 (BD-Difco), 1 g Yeast extract (BD-Difco), 3 g sodium citrate, 7 g MgSO4 x 7 H2O, 0.5 g K2HPO4, 0.05 g Fe(NH4)2(SO4)2 x 6 H2O, and 1 L distilled water.
- JCM 608 instructs adjusting pH to 7.0 with KOH and otherwise using JCM's default 121 C, 15 min autoclaving.
- Togo M616 preserves `ph: 7.0`, carries the 1 L distilled-water row, retains the BD-Difco complex-ingredient qualifiers, and records KOH only in the pH-adjustment comment.
- MediaDive J608 also preserves the pH 7.0 target, the direct source URL, 1000 ml distilled water, the three BD-Difco qualifiers, and an `Adjust pH to 7.0 with KOH.` preparation step.

## Completeness

- Missing pH: the generated record omits `ph_value: 7.0`.
- Mis-scaled ingredient: the explicit 1 L distilled-water row was normalized to `1 G_PER_L`.
- Missing preparation: the generated record has no `ADJUST_PH` step for KOH and no default JCM autoclaving semantics.

## Findings

1. The generated Togo M616 record omits the source pH target of 7.0.
2. Distilled water was imported as `1 G_PER_L` instead of a 1 L final-volume row.
3. KOH was promoted from the pH-adjustment instruction to a defaulted variable-concentration ingredient.
4. The generated record drops the pH-adjustment and default autoclaving steps.

## Recommended Edits

- Add `ph_value: 7.0`.
- Replace the water row with the correct 1 L final-volume representation.
- Remove KOH from `ingredients` and represent `Adjust pH to 7.0 with KOH.` as an `ADJUST_PH` preparation step.
- Add the JCM default 121 C, 15 min autoclaving step if the curation model captures default source sterilization.
- Reconcile this Togo M616 import with the direct MediaDive/JCM J608 duplicate so both sources point to one curated recipe.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Re-run an ignored-file-inclusive exact search for `TOGO:M616`, `JCM_M608`, and `mediadive.medium:J608` after regeneration.
- Verify that regenerated merged YAML has no variable KOH ingredient for JCM 608 and retains the BD-Difco qualifiers on Casamino acids, Proteose peptone No. 3, and Yeast extract.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.

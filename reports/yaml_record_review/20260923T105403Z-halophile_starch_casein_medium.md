# YAML Record Review: halophile_starch_casein_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halophile_starch_casein_medium.yaml`
- Started UTC: 2026-09-23T10:54:03Z
- Finished UTC: 2026-09-23T10:55:00Z
- Verdict: needs curation

## Target

Generated merged YAML for direct MediaDive/JCM medium J1005, `HALOPHILE STARCH-CASEIN MEDIUM`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches MediaDive `mediadive.medium:J1005` and the JCM 1005 source page.
- An ignored-file-inclusive exact search for `mediadive.medium:J1005`, `GRMD=1005`, and `halophile_starch_casein_medium` found this direct JCM J1005 archaeal import plus two Togo-derived bacterial siblings from the same JCM page.
- Casein is intentionally ungrounded as an undefined ingredient.
- Starch is grounded to CHEBI:28017, but the generated preferred term dropped the source's `soluble` qualifier.
- KNO3 still carries a legacy `mediaingredientmech_term` despite having a current CHEBI grounding.

## Evidence

- JCM 1005 lists a 1 L formula with 100 g soluble starch, 10 g casein, 10 g KNO3, 5 g K2HPO4, 5 g MgSO4 x 7 H2O, 0.1 g FeSO4 x 7 H2O, and 200 g NaCl.
- The JCM preparation text brings the medium to 1.0 L with distilled water, adds 20 g/L agar only for solid medium, autoclaves, and adjusts pH to 7.2-7.5 with NaOH.
- MediaDive J1005 preserves `attribute: soluble` on the starch row and records the pH target as 7.3.
- The generated direct record omits water and has a single `AUTOCLAVE` step whose description also contains pH adjustment.

## Completeness

- Missing final volume: distilled water to 1 L is present only in prose, not as a structured water/final-volume row.
- Missing qualifier: `Starch` lost the source `soluble` attribute.
- Missing variant: the optional 20 g/L agar solid form is retained only in preparation prose.
- Underspecified preparation: the pH adjustment with NaOH is not separated from autoclaving as an `ADJUST_PH` step.

## Findings

1. The generated direct JCM J1005 record omits a structured distilled-water/final-volume representation.
2. Soluble starch was reduced to generic `Starch`.
3. The optional 20 g/L agar solid form is not represented as a separate variant.
4. Autoclaving and pH adjustment with NaOH are compressed into a single `AUTOCLAVE` action.
5. KNO3 still carries a legacy `mediaingredientmech_term`.

## Recommended Edits

- Add distilled water or an equivalent structured final-volume representation for the 1 L formula.
- Restore the soluble-starch qualifier.
- Represent the 20 g/L agar instruction as an explicit solid variant.
- Split preparation into autoclaving and `ADJUST_PH` semantics while preserving the pH range.
- Replace the stale KNO3 `mediaingredientmech_term` with a CHEBI-keyed MediaIngredientMech link.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:J1005`, `TOGO:M1061`, `TOGO:M1062`, and `GRMD=1005` after regeneration.
- Verify that the regenerated direct and Togo-derived JCM 1005 records preserve the liquid and solid forms without making the NaOH pH-adjustment reagent a variable top-level ingredient.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.

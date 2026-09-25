# YAML Record Review: Heart Infusion Agar With 5% Horse Blood
- Repository: CultureMech
- Record: data/merge_yaml/merged/heart_infusion_agar_with_5_horse_blood.yaml
- Started UTC: 2026-09-23T11:44:25Z
- Finished UTC: 2026-09-23T11:45:07Z
- Verdict: needs curation

## Target

Reviewed the generated Togo M1172 / JCM 1099 branch for `Heart Infusion Agar With 5% Horse Blood` at `data/merge_yaml/merged/heart_infusion_agar_with_5_horse_blood.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/heart_infusion_agar_with_5_horse_blood.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `TOGO:M1172`, which imports `JCM_M1099`. JCM Medium 1099 is `HEART INFUSION AGAR WITH 5% HORSE BLOOD`, so the generated record is pointed at the intended source recipe.

## Evidence

Togo M1172 and JCM 1099 list a one-liter recipe containing 25.0 g Heart infusion broth (BD-Difco), 50.0 ml horse blood, 15.0 g agar, and 950.0 ml distilled water. JCM also gives the preparation: mix all ingredients except horse blood, autoclave, cool to about 50 C, aseptically add sterile defibrinated horse blood to 5% final, mix, and quickly dispense into sterile petri dishes.

The generated record has the correct four ingredient names and preserves the 25 g/L broth and 15 g/L agar values. It incorrectly serializes the two milliliter quantities as `950 G_PER_L` water and `50 G_PER_L` horse blood, has no preparation steps, and does not capture the autoclave and late sterile blood addition.

## Completeness

The generated record is stale relative to the normalized source file, `data/normalized_yaml/bacterial/TOGO_M1172_Heart_Infusion_Agar_With_5_Horse_Blood.yaml`. That source already keeps water and horse blood in `ML_PER_L`, grounds horse blood to `UBERON:0000178`, retains the BD-Difco broth as an unmapped commercial base, and adds structured autoclaving, cooling, blood-addition, and plate-pouring steps.

## Findings

- JCM's 950.0 ml distilled water was converted to `950 G_PER_L`.
- JCM's 50.0 ml horse blood was converted to `50 G_PER_L`, obscuring that it is a 5% final volume supplement.
- The generated artifact omits all JCM preparation instructions.
- The source's required sequence is lost: horse blood must be excluded from autoclaving, then aseptically added after cooling the sterile base.
- The generated artifact has not been regenerated from the repaired September 2026 normalized source.

## Recommended Edits

- Regenerate the generated merge output from `data/normalized_yaml/bacterial/TOGO_M1172_Heart_Infusion_Agar_With_5_Horse_Blood.yaml`.
- Preserve `950.0 ML_PER_L` distilled water and `50.0 ML_PER_L` horse blood.
- Preserve the repaired `AUTOCLAVE`, aseptic blood-addition, and `POUR_PLATES` preparation steps.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated artifact.
- Confirm the regenerated artifact no longer reports any milliliter source rows as `G_PER_L`.

## Additional Notes

None.

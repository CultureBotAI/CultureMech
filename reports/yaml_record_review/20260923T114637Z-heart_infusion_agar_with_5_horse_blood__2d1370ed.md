# YAML Record Review: HEART INFUSION AGAR WITH 5% HORSE BLOOD
- Repository: CultureMech
- Record: data/merge_yaml/merged/heart_infusion_agar_with_5_horse_blood__2d1370ed.yaml
- Started UTC: 2026-09-23T11:45:51Z
- Finished UTC: 2026-09-23T11:46:37Z
- Verdict: needs curation

## Target

Reviewed the generated direct JCM branch for JCM 1099, `HEART INFUSION AGAR WITH 5% HORSE BLOOD`, at `data/merge_yaml/merged/heart_infusion_agar_with_5_horse_blood__2d1370ed.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/heart_infusion_agar_with_5_horse_blood__2d1370ed.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is correctly grounded to `mediadive.medium:J1099` for JCM Medium 1099. However, its `kg_microbe_match` is `mediadive.medium:12`, which resolves to DSMZ `SOIL EXTRACT MEDIUM`, not this JCM horse-blood agar recipe.

## Evidence

JCM 1099 and MediaDive's `J1099` REST payload list the same one-liter medium: 25.0 g Heart infusion broth (BD-Difco), 50.0 ml horse blood, 15.0 g agar, and 950.0 ml distilled water. JCM states to mix everything except horse blood, autoclave, cool to about 50 C, aseptically add 5% final sterile defibrinated horse blood, mix, and quickly dispense into sterile petri dishes.

The generated record lists only Heart Infusion Broth, Horse blood, and Agar. It converts Horse blood to `50 G_PER_L`, omits 950 ml distilled water entirely, and keeps the complete JCM preparation text in a single `AUTOCLAVE` step even though the source text spans mixing, autoclaving, cooling, aseptic blood addition, mixing, and plate pouring.

## Completeness

The direct normalized source, `data/normalized_yaml/bacterial/heart_infusion_agar_with_5_horse_blood.yaml`, already has the correct 950 ml/L distilled water, 50 ml/L horse blood, explicit autoclave metadata, and structured preparation steps. The generated artifact is stale relative to that repair. The bad `kg_microbe_match: mediadive.medium:12` is still present in the normalized source and should be fixed at the curation layer.

## Findings

- The generated record omits the 950 ml distilled-water row from the source recipe.
- Horse blood is represented as `50 G_PER_L` instead of 50 ml/L or a 5% final volumetric supplement.
- JCM's post-autoclave sterile blood addition and plate pouring are collapsed into one broad `AUTOCLAVE` preparation step.
- `kg_microbe_match: mediadive.medium:12` is a wrong cross-reference to DSMZ Soil Extract Medium.
- The direct JCM branch and the Togo wrapper branch for JCM 1099 remain split into separate generated records.

## Recommended Edits

- Regenerate this generated artifact from the repaired direct JCM normalized source.
- Correct or remove `kg_microbe_match: mediadive.medium:12` in `data/normalized_yaml/bacterial/heart_infusion_agar_with_5_horse_blood.yaml`.
- Preserve the structured steps for base mixing, autoclaving at 121 C, cooling to 50 C, aseptic horse-blood addition, and plate pouring.
- Merge or alias this direct JCM branch with the Togo M1172 branch after both are regenerated.

## Follow-up Checks

- Confirm the generated artifact retains `950.0 ML_PER_L` water and `50.0 ML_PER_L` horse blood.
- Verify no regenerated `HEART INFUSION AGAR WITH 5% HORSE BLOOD` record refers to `mediadive.medium:12`.

## Additional Notes

None.

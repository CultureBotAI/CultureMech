# YAML Record Review: Heart Infusion Agar (supplemented with 5% sheep blood)
- Repository: CultureMech
- Record: data/merge_yaml/merged/heart_infusion_agar_supplemented_with_5_sheep_blood.yaml
- Started UTC: 2026-09-23T11:42:59Z
- Finished UTC: 2026-09-23T11:43:41Z
- Verdict: needs curation

## Target

Reviewed the generated Togo Medium M2291 branch for `Heart Infusion Agar (supplemented with 5% sheep blood)` at `data/merge_yaml/merged/heart_infusion_agar_supplemented_with_5_sheep_blood.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/heart_infusion_agar_supplemented_with_5_sheep_blood.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `TOGO:M2291`, and the title matches the Togo source. The Togo API payload for M2291 names Heart Infusion Agar supplemented with 5% sheep blood and reports routine growth for 2 days at 37 C in an incubator containing 5% CO2.

## Evidence

The Togo payload lists `sheep blood` with a value of `5 %`, `CO2` with a concentration of `5 %`, and `Heart Infusion Agar (Difco)` as an opaque commercial base. Its comment clarifies that 5% sheep blood was the supplement and that 5% CO2 was the incubator gas condition.

The generated merged record still represents sheep blood as `5 PERCENT_W_V`, turns `CO2` into a variable medium ingredient, keeps `Heart Infusion Agar (Difco)` as a variable ingredient, and lacks the source growth temperature, aeration, and preparation note.

## Completeness

The generated record is stale relative to the normalized source file, `data/normalized_yaml/bacterial/heart_infusion_agar_supplemented_with_5_sheep_blood.yaml`. That source has a September 2026 curation entry which moves CO2 to `aeration`, sets `temperature_value: 37.0`, changes sheep blood to `5 PERCENT_V_V`, gives the Difco agar base the remaining 95% v/v, and adds a preparation step for supplementing the base with Oxoid sheep blood.

## Findings

- The generated artifact has not been regenerated from the already repaired normalized YAML source.
- `CO2` is a gas-phase incubation condition in the source comment, not a culture-medium ingredient.
- Sheep blood should be represented as the 5% supplement rather than as 5% w/v.
- `Heart Infusion Agar (Difco)` is an intentionally opaque commercial base, but the generated record leaves it as a variable ingredient with no source-preserving concentration.
- The generated record omits the source's 37 C incubation condition, 5% CO2 atmosphere, and sheep-blood supplementation preparation step.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/heart_infusion_agar_supplemented_with_5_sheep_blood.yaml` from the repaired normalized source.
- Confirm the regenerated artifact keeps `CO2` in `aeration` and does not restore it as an ingredient.
- Preserve the curated 5% v/v sheep blood supplement, 95% v/v Difco base representation, 37 C temperature, and supplementing preparation step.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated merged YAML.
- Diff the regenerated file against `data/normalized_yaml/bacterial/heart_infusion_agar_supplemented_with_5_sheep_blood.yaml` to confirm the September 2026 repair propagated.

## Additional Notes

None.

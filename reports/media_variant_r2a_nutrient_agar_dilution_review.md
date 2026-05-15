# R2A And Nutrient Agar Dilution Variant Review

Date: 2026-05-14

## Scope

Reviewed three explicit dilution records in R3 A/R2A and Nutrient Agar No. 2
families. The selected pairs share a recognizable base medium, keep the agar
state, and differ by scaled nutrient/salt concentrations, so they were modeled
as `CONCENTRATION_VARIANT` child records.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/r3_a_medium.yaml` | `data/normalized_yaml/bacterial/half_strength_r2a.yaml` | `CONCENTRATION_VARIANT` | Yeast extract, proteose peptone, casamino acids, glucose, starch, phosphate, and magnesium sulfate are lower; agar remains 15 g/L |
| `data/normalized_yaml/bacterial/r3_a_medium.yaml` | `data/normalized_yaml/bacterial/1_10_r2a_medium.yaml` | `CONCENTRATION_VARIANT` | R3 A/R2A nutrients and salts are ten-fold or near ten-fold lower; agar remains 15 g/L |
| `data/normalized_yaml/bacterial/JCM_J23_1_10_NUTRIENT_AGAR_NO._2.yaml` | `data/normalized_yaml/bacterial/JCM_J24_1_100_NUTRIENT_AGAR_NO._2.yaml` | `CONCENTRATION_VARIANT` | Peptone, beef extract, and NaCl are ten-fold lower; agar remains 15 g/L and pH remains 7.1 |

## Deferred

- `data/normalized_yaml/bacterial/half_strength_r2a_medium_in_75_seawater.yaml`
  was deferred because the 75% seawater condition is not captured as a simple
  concentration-only child in the parsed ingredient list.
- Half-strength TSB agar records were deferred because the parsed formulations
  did not show a clean half-strength nutrient axis.

## Validation

- `just apply-media-variant-links --proposals /tmp/r2a_nutrient_agar_dilution_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/r2a_nutrient_agar_dilution_variant_links.tsv --apply`
- Targeted `just validate-schema` passed for all 5 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,315 parent-to-child links, 2,315 child-to-parent links, 0 errors, and
  0 warnings.

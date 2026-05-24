# TOGO SW, CM+YE, GYM, And R2A Variant Review

Date: 2026-05-14

## Scope

Reviewed six source-local TOGO/NBRC or TOGO/JCM formulation-strength pairs.
The selected pairs share a recognizable base medium and were modeled as
`CONCENTRATION_VARIANT` child records instead of unrelated duplicate media.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/TOGO_M629_SW-20_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M831_SW-10_Medium.yaml` | `CONCENTRATION_VARIANT` | SW-10 liquid halves the SW-20 salt and yeast extract concentrations |
| `data/normalized_yaml/bacterial/TOGO_M630_SW-20_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M832_SW-10_Medium.yaml` | `CONCENTRATION_VARIANT` | SW-10 agar halves the SW-20 salt and yeast extract concentrations, with agar adjusted from 20 g/L to 18 g/L |
| `data/normalized_yaml/bacterial/TOGO_M51_CM_YE_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M268_Modified_CM_YE_Medium_B.yaml` | `CONCENTRATION_VARIANT` | MgSO4 decreases from 20 g/L to 10 g/L and NaCl decreases from 200 g/L to 100 g/L |
| `data/normalized_yaml/bacterial/TOGO_M2035_CM_YE_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M1592_Modified_CM_YE_medium_B.yaml` | `CONCENTRATION_VARIANT` | MgSO4 decreases from 20 g/L to 10 g/L and NaCl decreases from 200 g/L to 100 g/L |
| `data/normalized_yaml/bacterial/TOGO_M2331_GYM_Streptomyces_Medium.yaml` | `data/normalized_yaml/bacterial/full_media_gym_streptomyces_medium.yaml` | `CONCENTRATION_VARIANT` | Agar increases from 12 g/L to 20 g/L |
| `data/normalized_yaml/bacterial/TOGO_M881_1_2_R2A_Agar.yaml` | `data/normalized_yaml/bacterial/TOGO_M839_1_10_R2A_Agar.yaml` | `CONCENTRATION_VARIANT` | R2A agar powder decreases from 9.1 g/L to 1.82 g/L with added agar adjusted from 7.5 g/L to 15 g/L |

## Deferred

- Modified Haloalkaliphile and Modified Halosimplex candidates were left for
  later review because their parsed deltas mix salt concentration changes,
  hydrate/name differences, and possible water-normalization artifacts.
- Gauze's Synthetic Medium with 18% NaCl and Nutrient Agar with 50% soil
  extract and 5% NaCl remain deferred because they combine salinity changes
  with additional formulation changes.

## Validation

- `just apply-media-variant-links --proposals /tmp/togo_sw_cmye_gym_r2a_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/togo_sw_cmye_gym_r2a_variant_links.tsv --apply`
- Targeted `just validate-schema` passed for all 12 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,301 parent-to-child links, 2,301 child-to-parent links, 0 errors, and
  0 warnings.

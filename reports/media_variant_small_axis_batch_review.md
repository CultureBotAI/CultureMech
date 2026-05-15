# Small-Axis Media Variant Batch Review

Date: 2026-05-13

## Scope

Reviewed a set of source-backed media records where paired formulations share
the same ingredient identities and differ by one concentration axis. Applied
the pairs that had clear parent/child direction and deferred the M17 wt/vol
glucose pair because its record names use percent notation while parsed
concentrations are stored as g/L.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/modified_m1_medium_with_20_mm_lactate_pinchuk_et_al.yaml` | `data/normalized_yaml/bacterial/modified_m1_medium_with_18_mm_lactate_pinchuk_et_al.yaml` | `CONCENTRATION_VARIANT` | Lactate decreases from 20 mM to 18 mM |
| `data/normalized_yaml/bacterial/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.yaml` | `data/normalized_yaml/bacterial/rdm_base_medium_vitamins_maltose_0_5_g_l_nh4cl.yaml` | `CONCENTRATION_VARIANT` | Ammonium chloride decreases from 18.7 mM to 9.348 mM |
| `data/normalized_yaml/bacterial/p2_1_butanol_challenge.yaml` | `data/normalized_yaml/bacterial/p2_1_5_butanol_challenge.yaml` | `CONCENTRATION_VARIANT` | 1-Butanol increases from 98.4633 mM to 147.695 mM |
| `data/normalized_yaml/bacterial/nutrient_broth_with_0_5_nacl.yaml` | `data/normalized_yaml/bacterial/nutrient_broth_with_1_0_nacl.yaml` | `SALINITY_VARIANT` | NaCl increases from 5 g/L to 10 g/L |
| `data/normalized_yaml/bacterial/TOGO_M5_Nutrient_Broth_With_0.5_NaCl.yaml` | `data/normalized_yaml/bacterial/TOGO_M3_Nutrient_Broth_With_1.0_NaCl.yaml` | `SALINITY_VARIANT` | NaCl increases from 5 g/L to 10 g/L |
| `data/normalized_yaml/bacterial/marine_agar_broth_2216_3_nacl.yaml` | `data/normalized_yaml/bacterial/marine_agar_broth_2216_10_nacl.yaml` | `SALINITY_VARIANT` | NaCl increases from 30 g/L to 100 g/L |
| `data/normalized_yaml/bacterial/TOGO_M957_R2A_Agar_With_1_NaCl.yaml` | `data/normalized_yaml/bacterial/TOGO_M1376_R2A_Agar_With_3_NaCl.yaml` | `SALINITY_VARIANT` | NaCl increases from 10 g/L to 30 g/L |
| `data/normalized_yaml/bacterial/1_2_isp_2_10_nacl.yaml` | `data/normalized_yaml/bacterial/1_2_isp_2_15_nacl.yaml` | `SALINITY_VARIANT` | NaCl increases from 100 g/L to 150 g/L |
| `data/normalized_yaml/bacterial/mrs_5_nacl.yaml` | `data/normalized_yaml/bacterial/mrs_8_nacl.yaml` | `SALINITY_VARIANT` | NaCl increases from 50 g/L to 80 g/L |

## Deferred

- `m17_medium_oxoid_supplemented_with_0_5_wt_vol_glucose.yaml` and
  `m17_medium_oxoid_supplemented_with_1_wt_vol_glucose.yaml` should be reviewed
  separately because the medium names encode wt/vol percentages, while parsed
  concentrations are currently represented as g/L.

## Validation

- `just apply-media-variant-links --proposals /tmp/small_axis_media_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/small_axis_media_variant_links.tsv --apply`
- Targeted `just validate-schema` loop passed for all 18 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,244 parent-to-child links, 2,244 child-to-parent links, 0 errors, and
  0 warnings.

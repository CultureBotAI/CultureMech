# Mixed One-Axis Variant Review

Date: 2026-05-13

## Scope

Reviewed six remaining one-axis concentration or salinity variants spanning
TOGO, DSMZ, and FEBA records. Each applied child shares the same parsed
ingredient set as its parent and differs by one concentration axis.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/togo_medium_m1414.yaml` | `data/normalized_yaml/bacterial/togo_medium_m1415.yaml` | `CONCENTRATION_VARIANT` | Sucrose increases from 200 g/L to 400 g/L |
| `data/normalized_yaml/specialized/r2a_low_k2hpo4.yaml` | `data/normalized_yaml/specialized/r2a_high_k2hpo4.yaml` | `CONCENTRATION_VARIANT` | Potassium phosphate dibasic increases from 50 micromolar to 1.75 mM |
| `data/normalized_yaml/bacterial/anoxybacillus_medium.yaml` | `data/normalized_yaml/bacterial/anaerobacillus_medium.yaml` | `SALINITY_VARIANT` | NaCl increases from 4.99002 g/L to 14.9701 g/L |
| `data/normalized_yaml/bacterial/nutriment_agar.yaml` | `data/normalized_yaml/bacterial/nutriment_agar_with_150_g_l_nacl.yaml` | `SALINITY_VARIANT` | NaCl increases from 5 g/L to 150 g/L |
| `data/normalized_yaml/bacterial/tetragenococcus_halophilus_medium_to_mrs_medium_add_6_5_nacl.yaml` | `data/normalized_yaml/bacterial/tetragenococcus_muriaticus_medium_mrs_medium_10_nacl_ph_7_5_8_0.yaml` | `SALINITY_VARIANT` | NaCl increases from 65 g/L to 100 g/L; child name includes pH 7.5-8.0 |
| `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_medium.yaml` | `data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_medeium_b.yaml` | `CONCENTRATION_VARIANT` | Yeast extract decreases from 5 g/L to 0.5 g/L |

## Deferred

- The GYM Streptomyces 10% to 15% NaCl candidate was not applied because the
  proposed 10% record already has a different parent link.

## Validation

- `just apply-media-variant-links --proposals /tmp/mixed_one_axis_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/mixed_one_axis_variant_links.tsv --apply`
- Targeted `just validate-schema` loop passed for all 12 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,280 parent-to-child links, 2,280 child-to-parent links, 0 errors, and
  0 warnings.

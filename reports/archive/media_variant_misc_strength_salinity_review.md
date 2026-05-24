# Miscellaneous Strength And Salinity Variant Review

Date: 2026-05-14

## Scope

Reviewed five remaining low-cardinality, explicit formulation variants across
TOGO, MediaDive/JCM, and specialized records. The selected pairs share a
recognizable base medium and differ by strength, nutrient concentration, or
salinity-related salts.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/mycorrhiza_medium.yaml` | `data/normalized_yaml/bacterial/1_5_mycorrhiza_medium.yaml` | `CONCENTRATION_VARIANT` | Yeast extract decreases from 2 g/L to 0.4 g/L and glucose decreases from 20 g/L to 4 g/L; agar remains 15 g/L |
| `data/normalized_yaml/specialized/kb.yaml` | `data/normalized_yaml/specialized/kb_half.yaml` | `CONCENTRATION_VARIANT` | KB-half halves all parsed KB components |
| `data/normalized_yaml/bacterial/r2a_agar.yaml` | `data/normalized_yaml/bacterial/5_x_r2a_agar.yaml` | `CONCENTRATION_VARIANT` | R2A nutrient and salt components increase five-fold; agar remains 15 g/L |
| `data/normalized_yaml/bacterial/5_salt_water_growth_medium.yaml` | `data/normalized_yaml/bacterial/modified_growth_medium_with_23_total_salt_concentration.yaml` | `CONCENTRATION_VARIANT` | Parsed salt concentrations are unchanged while peptone and yeast extract double |
| `data/normalized_yaml/bacterial/TOGO_M159_Halobacteria_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M1065_Modified_Halobacteria_Medium-3.yaml` | `SALINITY_VARIANT` | NaCl increases from 200 g/L to 270 g/L and MgSO4 x 7H2O decreases from 20 g/L to 15 g/L |

## Deferred

- `data/normalized_yaml/bacterial/1_5_marine_broth_0_5_sodium_pyruvate.yaml`
  was deferred because the parsed agar and water values appear to include a
  normalization artifact.
- Modified AS-168, Haloalkaliphile, and Halosimplex candidates remain deferred
  because the deltas mix several salt, hydrate, and pH-relevant changes.

## Validation

- `just apply-media-variant-links --proposals /tmp/misc_strength_salinity_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/misc_strength_salinity_variant_links.tsv --apply`
- Targeted `just validate-schema` passed for all 10 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,320 parent-to-child links, 2,320 child-to-parent links, 0 errors, and
  0 warnings.

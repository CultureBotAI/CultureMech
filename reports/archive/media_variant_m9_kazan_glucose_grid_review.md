# M9 Kazan Glucose-Grid Variant Review

Date: 2026-05-13

## Scope

Reviewed the MediaDB M9 Kazan glucose-dose records:

- `data/normalized_yaml/bacterial/m9_with_2_g_l_glucose_kazan.yaml`
- `data/normalized_yaml/bacterial/m9_with_4_g_l_glucose_kazan.yaml`
- `data/normalized_yaml/bacterial/m9_with_8_g_l_glucose_kazan.yaml`
- `data/normalized_yaml/bacterial/m9_with_16_g_l_glucose_kazan.yaml`
- `data/normalized_yaml/bacterial/m9_with_32_g_l_glucose_kazan.yaml`

## Decision

Applied `CONCENTRATION_VARIANT` links from parent
`m9_with_2_g_l_glucose_kazan` to the 4, 8, 16, and 32 g/L glucose child
records.

Rationale:

- All five records are MediaDB records imported from the same reference:
  Mazumdar et al. (2014) PLOS One.
- All five records share the same parsed ingredient identities and the same
  physical state.
- The only parsed concentration difference is beta-D-glucose:
  11.1012, 22.2025, 44.405, 88.8099, and 177.62 mM.
- The child records preserve their full formulations and now carry explicit
  child-to-parent links, while the parent carries reciprocal `variant_children`
  links.

## Applied Links

| Parent | Child | Relationship | Modification summary |
|---|---|---|---|
| `m9_with_2_g_l_glucose_kazan` | `m9_with_4_g_l_glucose_kazan` | `CONCENTRATION_VARIANT` | Glucose increased from 2 g/L (11.1012 mM) to 4 g/L (22.2025 mM). |
| `m9_with_2_g_l_glucose_kazan` | `m9_with_8_g_l_glucose_kazan` | `CONCENTRATION_VARIANT` | Glucose increased from 2 g/L (11.1012 mM) to 8 g/L (44.405 mM). |
| `m9_with_2_g_l_glucose_kazan` | `m9_with_16_g_l_glucose_kazan` | `CONCENTRATION_VARIANT` | Glucose increased from 2 g/L (11.1012 mM) to 16 g/L (88.8099 mM). |
| `m9_with_2_g_l_glucose_kazan` | `m9_with_32_g_l_glucose_kazan` | `CONCENTRATION_VARIANT` | Glucose increased from 2 g/L (11.1012 mM) to 32 g/L (177.62 mM). |

## Validation

Validation was run after applying the links:

- Targeted schema validation passed for all 5 touched M9 Kazan YAML files.
- `just validate-media-variant-links` scanned 15,827 records and reported
  2,203 parent-to-child links, 2,203 child-to-parent links, 0 errors, and
  0 warnings.

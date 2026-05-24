# Strength And Buffer Concentration Variant Review

Date: 2026-05-13

## Scope

Reviewed three one-axis concentration variants where the records share the same
base medium and differ only in medium strength, agar concentration, or buffer
concentration.

## Applied Decisions

| Parent | Child | Difference | Decision |
|---|---|---|---|
| `data/normalized_yaml/bacterial/TOGO_M33_Marine_Broth_2216.yaml` | `data/normalized_yaml/bacterial/quarter_strength_marine_broth_2216.yaml` | Marine broth 2216 decreases from 37.4 g/L to 9.35 g/L | Apply as `CONCENTRATION_VARIANT` |
| `data/normalized_yaml/bacterial/TOGO_M1431_YM_Agar.yaml` | `data/normalized_yaml/bacterial/TOGO_M18_YM_Agar.yaml` | Agar increases from 15 g/L to 20 g/L | Apply as `CONCENTRATION_VARIANT` |
| `data/normalized_yaml/bacterial/bl_medium.yaml` | `data/normalized_yaml/bacterial/bl_medium_low_mops.yaml` | MOPS decreases from 190 mM to 40 mM | Apply as `CONCENTRATION_VARIANT` |

## Deferred

- Corynebacterium and osmophilic fungi candidates were not applied because the
  proposed parent records already have different parent links.
- Sucrose-Bennett and TSBY salt candidates were left for later review because
  they cross source families and include pH or source-specific ambiguity.

## Validation

- `just apply-media-variant-links --proposals /tmp/one_axis_strength_buffer_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/one_axis_strength_buffer_variant_links.tsv --apply`
- Targeted `just validate-schema` loop passed for all 6 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,274 parent-to-child links, 2,274 child-to-parent links, 0 errors, and
  0 warnings.

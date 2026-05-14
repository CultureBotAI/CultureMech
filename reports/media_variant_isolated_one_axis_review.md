# Isolated One-Axis Variant Review

Date: 2026-05-13

## Scope

Reviewed six isolated one-axis variant pairs across bacterial, fungal, and
specialized media records. Each applied pair shares the same ingredient set,
medium type, and physical state, and differs by one concentration axis.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/2_malt_agar.yaml` | `data/normalized_yaml/bacterial/4_malt_agar.yaml` | `CONCENTRATION_VARIANT` | Malt extract (BD-Difco) increases from 20 g/L to 40 g/L |
| `data/normalized_yaml/bacterial/ma2.yaml` | `data/normalized_yaml/bacterial/ma4.yaml` | `CONCENTRATION_VARIANT` | Malt extract increases from 20 g/L to 40 g/L |
| `data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml` | `data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml` | `CONCENTRATION_VARIANT` | Glycerol increases from 21.718 mM to 43.436 mM |
| `data/normalized_yaml/fungal/yeast_mineral_medium_7_5_g_l_ethanol.yaml` | `data/normalized_yaml/fungal/yeast_mineral_medium_7_9_g_l_ethanol.yaml` | `CONCENTRATION_VARIANT` | Ethanol increases from 162.8 mM to 171.5 mM |
| `data/normalized_yaml/specialized/marine_aob_medium_a.yaml` | `data/normalized_yaml/specialized/marine_aob_medium_b.yaml` | `SALINITY_VARIANT` | NaCl increases from 29.1036 g/L to 40.7869 g/L |
| `data/normalized_yaml/specialized/varel_bryant_medium.yaml` | `data/normalized_yaml/specialized/varel_bryant_medium_lowcys.yaml` | `CONCENTRATION_VARIANT` | L-Cysteine decreases from 8.25 mM to 3 mM |

## Notes

- `ma2.yaml` already had variant children; `ma4.yaml` was added to that existing
  parent group rather than creating a competing parent.
- No organism growth claims were added in this batch.

## Validation

- `just apply-media-variant-links --proposals /tmp/isolated_one_axis_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/isolated_one_axis_variant_links.tsv --apply`
- Targeted `just validate-schema` loop passed for all 12 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,255 parent-to-child links, 2,255 child-to-parent links, 0 errors, and
  0 warnings.

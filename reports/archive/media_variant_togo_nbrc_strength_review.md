# TOGO/NBRC Strength Variant Review

Date: 2026-05-13

## Scope

Reviewed four source-local TOGO/NBRC medium pairs whose names and formulations
represent lower-strength or higher-strength versions of the same base medium.
The selected pairs preserve the recognizable parent formulation and change
organic nutrients, base powder strength, or recipe concentration while keeping
the medium family intact.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/TOGO_M1022_Artificial_Seawater_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M723_Low-Strength_Artificial_Seawater_Medium.yaml` | `CONCENTRATION_VARIANT` | Yeast extract decreases from 3 g/L to 0.1 g/L and peptone decreases from 2.5 g/L to 0.5 g/L; seawater salts remain unchanged |
| `data/normalized_yaml/bacterial/TOGO_M46_Potato-Carrot_Agar.yaml` | `data/normalized_yaml/bacterial/TOGO_M47_1_10_Potato-Carrot_Agar.yaml` | `CONCENTRATION_VARIANT` | Carrot decreases from 25 g/L to 2.5 g/L and potato decreases from 300 g/L to 30 g/L; agar remains 15 g/L |
| `data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml` | `data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml` | `CONCENTRATION_VARIANT` | R2A nutrient and salt components increase five-fold while agar remains 15 g/L |
| `data/normalized_yaml/bacterial/TOGO_M15_Nutrient_Agar_NO._2.yaml` | `data/normalized_yaml/bacterial/TOGO_M16_1_10_Nutrient_Agar_NO._2.yaml` | `CONCENTRATION_VARIANT` | NaCl, beef extract, and peptone decrease ten-fold while agar remains 15 g/L |

## Deferred

- TOGO nutrient agar with soil extract and 5% NaCl was not applied because it
  combines salinity, extract, and concentration changes.
- TOGO Gauze's Synthetic Medium with 18% NaCl was not applied because it
  combines salinity with FeSO4 and agar concentration discrepancies.
- The parsed 1/100 Nutrient Agar No. 2 record was not applied in this batch
  because the NaCl concentration needs source review before it can be trusted
  as a dilution variant.

## Validation

- `just apply-media-variant-links --proposals /tmp/togo_nbrc_strength_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/togo_nbrc_strength_variant_links.tsv --apply`
- Targeted `just validate-schema` passed for all 8 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,295 parent-to-child links, 2,295 child-to-parent links, 0 errors, and
  0 warnings.

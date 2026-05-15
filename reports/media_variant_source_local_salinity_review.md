# Source-Local Salinity Variant Review

Date: 2026-05-13

## Scope

Reviewed four source-local salinity pairs where the records share a recognizable
base medium and differ by an explicit salt concentration axis.

## Applied Decisions

| Parent | Child | Source family | Difference | Decision |
|---|---|---|---|---|
| `data/normalized_yaml/bacterial/trypticase_soy_broth_agar_with_3_nacl.yaml` | `data/normalized_yaml/bacterial/trypticase_soy_broth_agar_with_10_nacl.yaml` | JCM/MediaDive | Added NaCl increases from 30 g/L to 100 g/L | Apply as `SALINITY_VARIANT` |
| `data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_isp_2_with_2_nacl.yaml` | `data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_isp_2_with_5_nacl.yaml` | JCM/MediaDive | NaCl increases from 20 g/L to 50 g/L | Apply as `SALINITY_VARIANT` |
| `data/normalized_yaml/bacterial/JCM_J59_CM_YE_MEDIUM.yaml` | `data/normalized_yaml/bacterial/modified_cm_ye_medium_a.yaml` | JCM/MediaDive | NaCl decreases from 199.8 g/L to 149.85 g/L | Apply as `SALINITY_VARIANT` |
| `data/normalized_yaml/bacterial/TOGO_M51_CM_YE_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M107_Modified_CM_YE_Medium_A.yaml` | TOGO/JCM | NaCl decreases from 200 g/L to 150 g/L | Apply as `SALINITY_VARIANT` |

## Notes

- pH-modified 5% NaCl TSB/ISP-2 records were not included in this batch because
  they combine salinity and pH differences.
- The GYM Streptomyces 10% to 15% NaCl candidate was not included because the
  KOMODO 10% record already has a different parent link.
- No organism growth claims were added in this batch.

## Validation

- `just apply-media-variant-links --proposals /tmp/source_local_salinity_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/source_local_salinity_variant_links.tsv --apply`
- Targeted `just validate-schema` loop passed for all 8 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,265 parent-to-child links, 2,265 child-to-parent links, 0 errors, and
  0 warnings.

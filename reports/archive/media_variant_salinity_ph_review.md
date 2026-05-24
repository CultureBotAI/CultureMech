# Salinity And pH Variant Review

Date: 2026-05-13

## Scope

Reviewed two child records that extend existing salinity parent groups and add
an explicit pH condition. These were modeled as `SALINITY_VARIANT` children with
the pH difference captured in `variant_modifications` rather than as unrelated
new parent records.

## Applied Decisions

| Parent | Child | Difference | Decision |
|---|---|---|---|
| `data/normalized_yaml/bacterial/trypticase_soy_broth_agar_with_3_nacl.yaml` | `data/normalized_yaml/bacterial/trypticase_soy_broth_agar_with_5_nacl_ph_8_0.yaml` | Added NaCl increases from 30 g/L to 50 g/L; child specifies pH 8.0 | Apply as `SALINITY_VARIANT` with pH noted in modifications |
| `data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_isp_2_with_2_nacl.yaml` | `data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_isp_2_with_5_nacl_ph_9_0.yaml` | NaCl increases from 20 g/L to 50 g/L; child specifies pH 9.0 | Apply as `SALINITY_VARIANT` with pH noted in modifications |

## Notes

- Both parent records already had reviewed salinity children. This batch extends
  those existing parent groups.
- No organism growth claims were added in this batch.

## Validation

- `just apply-media-variant-links --proposals /tmp/salinity_ph_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/salinity_ph_variant_links.tsv --apply`
- Targeted `just validate-schema` loop passed for all 4 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,271 parent-to-child links, 2,271 child-to-parent links, 0 errors, and
  0 warnings.

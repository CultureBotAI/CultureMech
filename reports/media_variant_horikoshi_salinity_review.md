# Horikoshi-I Salinity Variant Review

Date: 2026-05-13

## Scope

Reviewed the JCM Horikoshi-I liquid medium records with 2%, 3.5%, 5%, and 10%
NaCl. The records share the same Horikoshi-I base medium and differ only in
NaCl concentration.

## Applied Decisions

| Parent | Child | Difference | Decision |
|---|---|---|---|
| `data/normalized_yaml/bacterial/horikoshi_i_medium_with_2_nacl.yaml` | `data/normalized_yaml/bacterial/horikoshi_i_medium_with_3_5_nacl.yaml` | NaCl increases from 20 g/L to 35 g/L | Apply as `SALINITY_VARIANT` |
| `data/normalized_yaml/bacterial/horikoshi_i_medium_with_2_nacl.yaml` | `data/normalized_yaml/bacterial/horikoshi_i_medium_with_5_nacl.yaml` | NaCl increases from 20 g/L to 50 g/L | Apply as `SALINITY_VARIANT` |
| `data/normalized_yaml/bacterial/horikoshi_i_medium_with_2_nacl.yaml` | `data/normalized_yaml/bacterial/JCM_J345_HORIKOSHI-1_MEDIUM_WITH_10_NaCl.yaml` | NaCl increases from 20 g/L to 100 g/L | Apply as `SALINITY_VARIANT` |

## Notes

- The 2% NaCl record was selected as the lowest-salt parent for this salinity
  grid.
- All records are JCM/MediaDive liquid complex Horikoshi-I formulations.
- No organism growth claims were added in this batch.

## Validation

- `just apply-media-variant-links --proposals /tmp/horikoshi_salinity_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/horikoshi_salinity_variant_links.tsv --apply`
- Targeted `just validate-schema` loop passed for all 4 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,261 parent-to-child links, 2,261 child-to-parent links, 0 errors, and
  0 warnings.

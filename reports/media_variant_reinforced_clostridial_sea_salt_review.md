# Reinforced Clostridial Sea-Salt Variant Review

Date: 2026-05-13

## Scope

Reviewed two source-specific Reinforced Clostridial Medium sea-salt pairs for
explicit parent/child variant modeling:

- TOGO/JCM M482 to M483
- JCM/MediaDive J481 to J482

## Decision

Both pairs were applied as `SALINITY_VARIANT` relationships. The 3% sea-salt
record was kept as the parent formulation, and the 4% sea-salt record was linked
as the child variant.

## Evidence

| Parent | Child | Source family | Difference | Decision |
|---|---|---|---|---|
| `data/normalized_yaml/bacterial/TOGO_M482_Reinforced_Clostridial_Medium_With_3_Sea_Salt.yaml` | `data/normalized_yaml/bacterial/TOGO_M483_Reinforced_Clostridial_Medium_With_4_Sea_Salt.yaml` | TOGO/JCM | `Sea salts (Sigma)` increases from 30 g/L to 40 g/L; reinforced clostridial medium and agar unchanged | Apply as `SALINITY_VARIANT` |
| `data/normalized_yaml/bacterial/reinforced_clostridial_medium_with_3_sea_salt.yaml` | `data/normalized_yaml/bacterial/reinforced_clostridial_medium_with_4_sea_salt.yaml` | JCM/MediaDive | `Sea Salt` increases from 30 g/L to 40 g/L; reinforced clostridial medium and agar unchanged | Apply as `SALINITY_VARIANT` |

## Notes

- The TOGO records cite source URLs for TOGO M482 and M483, with JCM original
  records GRMD 481 and 482.
- The JCM/MediaDive records cite the same JCM GRMD 481 and 482 source family.
- No organism growth claims were added in this batch; this pass only models
  medium formulation variants already present in the local YAML corpus.

## Validation

- `just apply-media-variant-links --proposals /tmp/reinforced_clostridial_salt_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/reinforced_clostridial_salt_variant_links.tsv --apply`
- Targeted `just validate-schema` loop passed for all 4 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,235 parent-to-child links, 2,235 child-to-parent links, 0 errors, and
  0 warnings.

# Halobacteria Medium Variant Review

Date: 2026-05-13

## Scope

Reviewed source-local Halobacteria medium variants from JCM/MediaDive and TOGO.
The applied records share a Halobacteria-style base formulation and differ by
one salt or magnesium-sulfate concentration axis.

## Applied Decisions

| Parent | Child | Source family | Difference | Decision |
|---|---|---|---|---|
| `data/normalized_yaml/bacterial/JCM_J168_HALOBACTERIA_MEDIUM.yaml` | `data/normalized_yaml/bacterial/JCM_J377_LENTIBACILLUS_MEDIUM.yaml` | JCM/MediaDive | NaCl decreases from 200 g/L to 100 g/L; pH remains 7.1 | Apply as `SALINITY_VARIANT` |
| `data/normalized_yaml/bacterial/TOGO_M159_Halobacteria_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M959_Halobacteria_Medium_With_15_NaCl.yaml` | TOGO/JCM liquid | NaCl decreases from 200 g/L to 150 g/L | Apply as `SALINITY_VARIANT` |
| `data/normalized_yaml/bacterial/TOGO_M159_Halobacteria_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M576_Modified_Halobacteria_Medium.yaml` | TOGO/JCM liquid | MgSO4 hydrate decreases from 20 g/L to 2 g/L | Apply as `CONCENTRATION_VARIANT` |
| `data/normalized_yaml/bacterial/TOGO_M160_Halobacteria_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M960_Halobacteria_Medium_With_15_NaCl.yaml` | TOGO/JCM solid | NaCl decreases from 200 g/L to 150 g/L | Apply as `SALINITY_VARIANT` |

## Notes

- JCM/MediaDive, TOGO liquid, and TOGO solid records were modeled as separate
  source-local parent groups.
- `JCM_J168_HALOBACTERIA_MEDIUM.yaml` already had existing child links; this
  batch only added the reviewed Lentibacillus medium child.
- No organism growth claims were added in this batch.

## Validation

- `just apply-media-variant-links --proposals /tmp/halobacteria_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/halobacteria_variant_links.tsv --apply`
- Targeted `just validate-schema` loop passed for all 7 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,269 parent-to-child links, 2,269 child-to-parent links, 0 errors, and
  0 warnings.

# LB Salinity Variant Review

Date: 2026-05-13

## Scope

Reviewed source-specific LB/Luria broth salt variants where tryptone and yeast
extract are unchanged and the only formulation axis is sodium chloride.

## Applied Decisions

| Parent | Child | Source family | Difference | Decision |
|---|---|---|---|---|
| `data/normalized_yaml/bacterial/lb.yaml` | `data/normalized_yaml/bacterial/lb_miller.yaml` | FEBA | Sodium Chloride increases from 5 g/L to 10 g/L | Apply as `SALINITY_VARIANT` |
| `data/normalized_yaml/bacterial/lb.yaml` | `data/normalized_yaml/bacterial/lb_highsalt.yaml` | FEBA | Sodium Chloride increases from 5 g/L to 35 g/L | Apply as `SALINITY_VARIANT` |
| `data/normalized_yaml/bacterial/lennox.yaml` | `data/normalized_yaml/bacterial/luria_broth.yaml` | TOGO | NaCl increases from 5 g/L to 10 g/L | Apply as `SALINITY_VARIANT` |

## Notes

- The FEBA and TOGO records were modeled as separate source-local parent groups
  rather than cross-linking source families.
- No organism growth claims were added in this batch.

## Validation

- `just apply-media-variant-links --proposals /tmp/lb_salt_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/lb_salt_variant_links.tsv --apply`
- Targeted `just validate-schema` loop passed for all 5 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,258 parent-to-child links, 2,258 child-to-parent links, 0 errors, and
  0 warnings.

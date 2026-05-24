# LB, R2A, And CYS Variant Review

Date: 2026-05-14

## Scope

Reviewed three explicit strength or salinity variants in LB, R2A, and CYS
medium records. The selected pairs preserve a recognizable base formulation and
change one concentration axis.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/TOGO_M2314_LB_medium.yaml` | `data/normalized_yaml/bacterial/lb_0_1x.yaml` | `CONCENTRATION_VARIANT` | Tryptone decreases from 10 g/L to 1 g/L, yeast extract from 5 g/L to 0.5 g/L, and sodium chloride from 10 g/L to 0.5 g/L |
| `data/normalized_yaml/specialized/r2a.yaml` | `data/normalized_yaml/specialized/r2a_1x.yaml` | `CONCENTRATION_VARIANT` | All parsed R2A components are ten-fold lower in the `.1x` child |
| `data/normalized_yaml/bacterial/cys_medium.yaml` | `data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml` | `SALINITY_VARIANT` | NaCl increases from 3 g/L to 20 g/L while all other parsed ingredients remain unchanged |

## Deferred

- SNA/5 and NSW variants were deferred because the water/seawater amount needs
  source-level interpretation before modeling.
- CYS KOMODO parent-direction proposals were not used; the canonical MediaDive
  `cys_medium` record is the clearer parent for the modified-NaCl child.

## Validation

- `just apply-media-variant-links --proposals /tmp/lb_r2a_cys_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/lb_r2a_cys_variant_links.tsv --apply`
- Targeted `just validate-schema` passed for all 6 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,326 parent-to-child links, 2,326 child-to-parent links, 0 errors, and
  0 warnings.

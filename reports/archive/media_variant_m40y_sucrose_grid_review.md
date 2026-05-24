# M40Y Sucrose-Grid Variant Review

Date: 2026-05-13

## Scope

Reviewed the TOGO M40Y/MY50G/M60Y records:

- `data/normalized_yaml/bacterial/TOGO_M26_M40Y_Agar.yaml`
- `data/normalized_yaml/bacterial/TOGO_M3048_M40Y_agar.yaml`
- `data/normalized_yaml/bacterial/my50g.yaml`
- `data/normalized_yaml/bacterial/TOGO_M27_M60Y_Agar.yaml`
- `data/normalized_yaml/bacterial/m60y.yaml`

## Decision

Applied one `SOURCE_DUPLICATE` link and three `CONCENTRATION_VARIANT` links
under parent `m40y_agar` (`TOGO:M26`).

Rationale:

- The two M40Y records share the same parsed ingredient identities and
  concentrations and differ by source record: JCM M33 versus NBRC M1598.
- The MY50G and M60Y records share the same parsed ingredient identities and
  physical state as M40Y.
- The only parsed concentration difference for the MY50G/M60Y records is
  sucrose: 400, 500, or 600 g/L.
- The child records preserve their full formulations and now carry explicit
  child-to-parent links, while the parent carries reciprocal `variant_children`
  links.

## Applied Links

| Parent | Child | Relationship | Modification summary |
|---|---|---|---|
| `m40y_agar` (`TOGO:M26`) | `m40y_agar` (`TOGO:M3048`) | `SOURCE_DUPLICATE` | Same parsed M40Y formulation; source differs. |
| `m40y_agar` (`TOGO:M26`) | `my50g` | `CONCENTRATION_VARIANT` | Sucrose increased from 400 g/L to 500 g/L. |
| `m40y_agar` (`TOGO:M26`) | `m60y_agar` | `CONCENTRATION_VARIANT` | Sucrose increased from 400 g/L to 600 g/L. |
| `m40y_agar` (`TOGO:M26`) | `m60y` | `CONCENTRATION_VARIANT` | Sucrose increased from 400 g/L to 600 g/L. |

## Validation

Validation was run after applying the links:

- Targeted schema validation passed for all 5 touched M40Y/MY50G/M60Y YAML
  files.
- `just validate-media-variant-links` scanned 15,827 records and reported
  2,220 parent-to-child links, 2,220 child-to-parent links, 0 errors, and
  0 warnings.

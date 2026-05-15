# ASW Barley Salinity-Grid Variant Review

Date: 2026-05-13

## Scope

Reviewed the CCAP artificial seawater plus barley records:

- `data/normalized_yaml/bacterial/asw_150_barley.yaml`
- `data/normalized_yaml/bacterial/asw_225_barley.yaml`
- `data/normalized_yaml/bacterial/asw_300_barley.yaml`

## Decision

Applied `SALINITY_VARIANT` links from parent `asw_150_barley` to child records
`asw_225_barley` and `asw_300_barley`.

Rationale:

- All three records share the same ingredient identities: NaCl, KCl,
  MgCl2 x 6 H2O, MgSO4 x 7 H2O, and CaCl2 x 2 H2O.
- The source names and preparation text describe artificial seawater plus
  barley formulations at different salinities.
- The child records preserve their full formulations and now carry explicit
  child-to-parent links, while the parent carries reciprocal `variant_children`
  links.

## Source Records

| Record | Source | Formulation notes |
|---|---|---|
| `asw_150_barley` | CCAP Medium C6, `https://www.ccap.ac.uk/wp-content/uploads/MR_ASW_150.pdf` | Artificial seawater with 150 psu plus barley. |
| `asw_225_barley` | CCAP Medium C7, `https://www.ccap.ac.uk/wp-content/uploads/MR_ASW_225.pdf` | Name/source ID indicate 225 psu; preparation text says 255 psu. |
| `asw_300_barley` | CCAP Medium C8, `https://www.ccap.ac.uk/wp-content/uploads/MR_ASW_300.pdf` | Artificial seawater with 300 psu plus barley. |

## Applied Links

| Parent | Child | Relationship | Modification summary |
|---|---|---|---|
| `asw_150_barley` | `asw_225_barley` | `SALINITY_VARIANT` | Higher salinity than 150 psu parent; NaCl, MgCl2 x 6 H2O, and MgSO4 x 7 H2O concentrations differ. |
| `asw_150_barley` | `asw_300_barley` | `SALINITY_VARIANT` | Higher salinity than 150 psu parent; NaCl, KCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, and CaCl2 x 2 H2O concentrations differ. |

## Validation

- Targeted schema validation passed for all 3 touched ASW barley YAML files.
- `just validate-media-variant-links` scanned 15,827 records and reported
  2,199 parent-to-child links, 2,199 child-to-parent links, 0 errors, and
  0 warnings.

## Remaining Notes

The `asw_225_barley` source text inconsistency should be resolved against the
upstream CCAP PDF before using the exact salinity value in downstream analyses.

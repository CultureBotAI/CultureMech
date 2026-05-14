# 802 Glucose-Grid Variant Review

Date: 2026-05-13

## Scope

Reviewed the TOGO/NBRC 802 glucose records:

- `data/normalized_yaml/bacterial/802_5_glucose.yaml`
- `data/normalized_yaml/bacterial/togo_medium_m1562.yaml`
- `data/normalized_yaml/bacterial/togo_medium_m1605.yaml`

## Decision

Applied `CONCENTRATION_VARIANT` links from parent `802_5_glucose` to
`togo_medium_m1562` and `togo_medium_m1605`.

Rationale:

- All three records are TOGO records with NBRC original sources.
- All three records share the same parsed ingredient identities, solution entry,
  and physical state.
- The only parsed ingredient concentration difference is Glucose: 50 g/L in the
  parent and 5 g/L in both child records.
- The child records preserve their full formulations and now carry explicit
  child-to-parent links, while the parent carries reciprocal `variant_children`
  links.

## Applied Links

| Parent | Child | Relationship | Modification summary |
|---|---|---|---|
| `802_5_glucose` | `togo_medium_m1562` | `CONCENTRATION_VARIANT` | Glucose decreased from 50 g/L to 5 g/L. |
| `802_5_glucose` | `togo_medium_m1605` | `CONCENTRATION_VARIANT` | Glucose decreased from 50 g/L to 5 g/L. |

## Validation

Validation was run after applying the links:

- Targeted schema validation passed for all 3 touched 802 glucose YAML files.
- `just validate-media-variant-links` scanned 15,827 records and reported
  2,222 parent-to-child links, 2,222 child-to-parent links, 0 errors, and
  0 warnings.

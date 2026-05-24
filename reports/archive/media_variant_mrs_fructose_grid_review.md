# MRS Fructose-Grid Variant Review

Date: 2026-05-13

## Scope

Reviewed the TOGO/NBRC MRS fructose-dose records:

- `data/normalized_yaml/bacterial/mrs_1_fructose.yaml`
- `data/normalized_yaml/bacterial/mrs_2_fructose.yaml`
- `data/normalized_yaml/bacterial/mrs_10_fructose.yaml`

## Decision

Applied `CONCENTRATION_VARIANT` links from parent `mrs_1_fructose` to
`mrs_2_fructose` and `mrs_10_fructose`.

Rationale:

- All three records are TOGO records with NBRC original sources.
- All three records share the same parsed ingredient identities and physical
  state.
- The only parsed concentration difference is Fructose: 10, 20, and 100 g/L.
- The child records preserve their full formulations and now carry explicit
  child-to-parent links, while the parent carries reciprocal `variant_children`
  links.

## Applied Links

| Parent | Child | Relationship | Modification summary |
|---|---|---|---|
| `mrs_1_fructose` | `mrs_2_fructose` | `CONCENTRATION_VARIANT` | Fructose increased from 1% (10 g/L) to 2% (20 g/L). |
| `mrs_1_fructose` | `mrs_10_fructose` | `CONCENTRATION_VARIANT` | Fructose increased from 1% (10 g/L) to 10% (100 g/L). |

## Validation

Validation was run after applying the links:

- Targeted schema validation passed for all 3 touched MRS fructose YAML files.
- `just validate-media-variant-links` scanned 15,827 records and reported
  2,213 parent-to-child links, 2,213 child-to-parent links, 0 errors, and
  0 warnings.

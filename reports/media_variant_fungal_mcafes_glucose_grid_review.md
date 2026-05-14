# Fungal mCAFEs Glucose-Grid Variant Review

Date: 2026-05-13

## Scope

Reviewed the CultureBotHT fungal mCAFEs records:

- `data/normalized_yaml/fungal/fungal_growth_media_mcafes_v1.yaml`
- `data/normalized_yaml/fungal/fungal_growth_media_mcafes_v2.yaml`
- `data/normalized_yaml/fungal/fungal_growth_media_mcafes_v3.yaml`

## Decision

Applied `CONCENTRATION_VARIANT` links from parent
`Fungal growth media mCAFEs v1` to v2 and v3.

Rationale:

- All three records are CultureBotHT fungal mCAFEs records.
- All three records share the same parsed ingredient identities and physical
  state.
- The only parsed concentration difference is D-Glucose: 20 g/L, 5 g/L, or
  20 mM.
- The child records preserve their full formulations and now carry explicit
  child-to-parent links, while the parent carries reciprocal `variant_children`
  links.

## Applied Links

| Parent | Child | Relationship | Modification summary |
|---|---|---|---|
| `Fungal growth media mCAFEs v1` | `Fungal growth media mCAFEs v2` | `CONCENTRATION_VARIANT` | D-Glucose changed from 20 g/L to 5 g/L. |
| `Fungal growth media mCAFEs v1` | `Fungal growth media mCAFEs v3` | `CONCENTRATION_VARIANT` | D-Glucose changed from 20 g/L to 20 mM. |

## Validation

Validation was run after applying the links:

- Targeted schema validation passed for all 3 touched fungal mCAFEs YAML files.
- `just validate-media-variant-links` scanned 15,827 records and reported
  2,226 parent-to-child links, 2,226 child-to-parent links, 0 errors, and
  0 warnings.

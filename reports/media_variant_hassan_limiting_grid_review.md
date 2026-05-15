# Hassan Minimal-Media Limiting-Nutrient Variant Review

Date: 2026-05-13

## Scope

Reviewed the MediaDB Hassan minimal-media limiting-nutrient records:

- `data/normalized_yaml/bacterial/glucose_minimal_media_hassan_et_al.yaml`
- `data/normalized_yaml/bacterial/glucose_limiting_minimal_media_hassan_et_al.yaml`
- `data/normalized_yaml/bacterial/histidine_limiting_minimal_media_hassan_et_al.yaml`
- `data/normalized_yaml/bacterial/thiamine_limiting_minimal_media_hassan_et_al.yaml`

## Decision

Applied `CONCENTRATION_VARIANT` links from parent
`glucose_minimal_media_hassan_et_al` to the three limiting-nutrient child
records.

Rationale:

- All four records are MediaDB records imported from the same reference:
  Mazumdar et al. (2014) PLOS One.
- All four records share the same parsed ingredient identities and physical
  state.
- Each child differs from the parent by exactly one parsed concentration:
  D-Glucose, Histidine, or Thiamine.
- The child records preserve their full formulations and now carry explicit
  child-to-parent links, while the parent carries reciprocal `variant_children`
  links.

## Applied Links

| Parent | Child | Relationship | Modification summary |
|---|---|---|---|
| `glucose_minimal_media_hassan_et_al` | `glucose_limiting_minimal_media_hassan_et_al` | `CONCENTRATION_VARIANT` | D-Glucose decreased from 27.7531 mM to 4.0 mM. |
| `glucose_minimal_media_hassan_et_al` | `histidine_limiting_minimal_media_hassan_et_al` | `CONCENTRATION_VARIANT` | Histidine decreased from 1.92926 mM to 0.0643087 mM. |
| `glucose_minimal_media_hassan_et_al` | `thiamine_limiting_minimal_media_hassan_et_al` | `CONCENTRATION_VARIANT` | Thiamine decreased from 0.113053 mM to 0.000188423 mM. |

## Validation

Validation was run after applying the links:

- Targeted schema validation passed for all 4 touched Hassan minimal-media YAML
  files.
- `just validate-media-variant-links` scanned 15,827 records and reported
  2,216 parent-to-child links, 2,216 child-to-parent links, 0 errors, and
  0 warnings.

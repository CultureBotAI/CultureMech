# Desulfovibrio Marine/Brackish Salinity Variant Review

Date: 2026-05-13

## Scope

Reviewed the Desulfovibrio marine/brackish medium records:

- `data/normalized_yaml/bacterial/desulfovibrio_marine_medium.yaml`
- `data/normalized_yaml/bacterial/brackish_water_desulfovibrio_postgate_medium.yaml`
- `data/normalized_yaml/bacterial/desulfovibrio_medium_brackish.yaml`

## Decision

Applied `SALINITY_VARIANT` links from parent `desulfovibrio_marine_medium` to
the two brackish medium records.

Rationale:

- The parent is KOMODO/DSMZ Medium 163, labeled Desulfovibrio marine medium.
- The child records are DSMZ/KOMODO Medium 410, labeled brackish
  Desulfovibrio medium.
- All three records share the same parsed ingredient identities and physical
  state.
- The only parsed concentration difference is NaCl: 25.5102 g/L in the marine
  parent and 10.2041 g/L in both brackish child records.
- The parent already had a reviewed `SOURCE_DUPLICATE` child; this batch adds
  the brackish variants without changing that existing link.

## Applied Links

| Parent | Child | Relationship | Modification summary |
|---|---|---|---|
| `desulfovibrio_marine_medium` | `brackish_water_desulfovibrio_postgate_medium` | `SALINITY_VARIANT` | NaCl decreased from 25.5102 g/L to 10.2041 g/L. |
| `desulfovibrio_marine_medium` | `desulfovibrio_medium_brackish` | `SALINITY_VARIANT` | NaCl decreased from 25.5102 g/L to 10.2041 g/L. |

## Validation

Validation was run after applying the links:

- Targeted schema validation passed for all 3 touched Desulfovibrio
  marine/brackish YAML files.
- `just validate-media-variant-links` scanned 15,827 records and reported
  2,224 parent-to-child links, 2,224 child-to-parent links, 0 errors, and
  0 warnings.

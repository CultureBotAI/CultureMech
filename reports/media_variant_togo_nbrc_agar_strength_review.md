# TOGO/NBRC Agar Strength Variant Review

Date: 2026-05-13

## Scope

Reviewed two TOGO/NBRC solid complex agar pairs with matching parsed ingredient
sets and a single concentration axis. The selected pairs were modeled as
`CONCENTRATION_VARIANT` child records rather than unrelated duplicate media.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/TOGO_M1540_Enriched_Cytophaga_Agar.yaml` | `data/normalized_yaml/bacterial/flavobacterium_columnare_agar.yaml` | `CONCENTRATION_VARIANT` | Agar (if needed) decreases from 15 g/L to 10 g/L |
| `data/normalized_yaml/bacterial/bn_agar.yaml` | `data/normalized_yaml/bacterial/togo_medium_m1570.yaml` | `CONCENTRATION_VARIANT` | Nutrient Broth (OXOID) decreases from 13 g/L to 6.5 g/L |

## Deferred

- Cross-source TSBY salt and Methanocaldococcus medium candidates were left for
  later provenance review before any parent/child modeling.

## Validation

- `just apply-media-variant-links --proposals /tmp/togo_nbrc_agar_strength_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/togo_nbrc_agar_strength_variant_links.tsv --apply`
- Targeted `just validate-schema` passed for all 4 touched YAML files after
  normalizing pre-existing invalid `bn_agar.yaml` solution metadata.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,291 parent-to-child links, 2,291 child-to-parent links, 0 errors, and
  0 warnings.

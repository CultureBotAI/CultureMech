# YPS Source-Duplicate Review

Date: 2026-05-14

## Scope

Reviewed two source-duplicate links under `yeast_peptone_succinate_medium`.
The selected child records all preserve the same parsed solid-agar formula as
the parent: yeast extract 3 g/L, peptone 3 g/L, sodium succinate 2.3 g/L, and
agar 15 g/L. The parent and children are pH 7.2 DSMZ/KOMODO Medium 988 records.

The cross-category fungal `DERIVED_FROM` candidate in the same ingredient
signature group was not applied in this batch.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/yeast_peptone_succinate_medium.yaml` | `data/normalized_yaml/bacterial/medium_988_modified_for_dsm_15761.yaml` | `SOURCE_DUPLICATE` | Same DSMZ/KOMODO Medium 988 source, parsed ingredients, concentrations, pH, and solid-agar state; child is a DSM 15761 source copy. |
| `data/normalized_yaml/bacterial/yeast_peptone_succinate_medium.yaml` | `data/normalized_yaml/bacterial/medium_988_modified_for_dsm_15867.yaml` | `SOURCE_DUPLICATE` | Same DSMZ/KOMODO Medium 988 source, parsed ingredients, concentrations, pH, and solid-agar state; child is a DSM 15867 source copy. |

## Notes

- This batch completes the currently proposed bacterial YPS exact-signature
  `SOURCE_DUPLICATE` family; the review scan found 0 remaining unlinked
  `SOURCE_DUPLICATE` rows for ingredient signature `b99befe3d9e91c51`.
- Existing child formulas were preserved; this batch only adds explicit
  parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/yps_source_duplicate_links.tsv`
- `just apply-media-variant-links --proposals /tmp/yps_source_duplicate_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the three touched YAML
  files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,546 parent-to-child links, 2,546 child-to-parent links, 0 errors, and 0
  warnings.

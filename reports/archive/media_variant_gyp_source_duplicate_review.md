# GYP Source-Duplicate Review

Date: 2026-05-14

## Scope

Reviewed eight source-duplicate links under GYP glucose yeast peptone medium.
The selected child records all preserve the same parsed solid-agar formula as
the parent: glucose 20 g/L, yeast extract 10 g/L, peptone 10 g/L, Na-acetate
10 g/L, agar 10 g/L, MgSO4 x 7 H2O 40 g/L, MnSO4 x 4 H2O 2 g/L, FeSO4 x 7 H2O
2 g/L, and NaCl 2 g/L.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/gyp_glucose_yeast_peptone_medium.yaml` | `data/normalized_yaml/bacterial/medium_852_modified_for_dsm_45022.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and solid-agar state; child is a DSM strain-specific copy of DSMZ Medium 852/GYP. |
| `data/normalized_yaml/bacterial/gyp_glucose_yeast_peptone_medium.yaml` | `data/normalized_yaml/bacterial/medium_852_modified_for_dsm_45023.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and solid-agar state; child is a DSM strain-specific copy of DSMZ Medium 852/GYP. |
| `data/normalized_yaml/bacterial/gyp_glucose_yeast_peptone_medium.yaml` | `data/normalized_yaml/bacterial/medium_852_modified_for_dsm_45025.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and solid-agar state; child is a DSM strain-specific copy of DSMZ Medium 852/GYP. |
| `data/normalized_yaml/bacterial/gyp_glucose_yeast_peptone_medium.yaml` | `data/normalized_yaml/bacterial/medium_852_modified_for_dsm_45026.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and solid-agar state; child is a DSM strain-specific copy of DSMZ Medium 852/GYP. |
| `data/normalized_yaml/bacterial/gyp_glucose_yeast_peptone_medium.yaml` | `data/normalized_yaml/bacterial/medium_852_modified_for_dsm_45027.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and solid-agar state; child is a DSM strain-specific copy of DSMZ Medium 852/GYP. |
| `data/normalized_yaml/bacterial/gyp_glucose_yeast_peptone_medium.yaml` | `data/normalized_yaml/bacterial/medium_852_modified_for_dsm_45029.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and solid-agar state; child is a DSM strain-specific copy of DSMZ Medium 852/GYP. |
| `data/normalized_yaml/bacterial/gyp_glucose_yeast_peptone_medium.yaml` | `data/normalized_yaml/bacterial/medium_852_modified_for_dsm_45031.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and solid-agar state; child is a DSM strain-specific copy of DSMZ Medium 852/GYP. |
| `data/normalized_yaml/bacterial/gyp_glucose_yeast_peptone_medium.yaml` | `data/normalized_yaml/bacterial/medium_852_modified_for_dsm_45032.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and solid-agar state; child is a DSM strain-specific copy of DSMZ Medium 852/GYP. |

## Notes

- This batch completes the currently proposed GYP exact-signature
  `SOURCE_DUPLICATE` family; the review scan found 0 remaining unlinked rows
  for ingredient signature `3aff06d8e9e60471`.
- Existing child formulas were preserved; this batch only adds explicit
  parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/gyp_source_duplicate_links.tsv`
- `just apply-media-variant-links --proposals /tmp/gyp_source_duplicate_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the nine touched YAML
  files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,530 parent-to-child links, 2,530 child-to-parent links, 0 errors, and 0
  warnings.

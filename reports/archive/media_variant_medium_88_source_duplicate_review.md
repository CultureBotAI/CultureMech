# Medium 88 Source-Duplicate Review

Date: 2026-05-14

## Scope

Reviewed seven source-duplicate links under `KOMODO_88-2_For_DSM_18786`.
The selected child records all preserve the same parsed liquid formula as the
parent: (NH4)2SO4 1.3 g/L, KH2PO4 0.28 g/L, MgSO4 x 7 H2O 0.25 g/L,
CaCl2 x 2 H2O 0.07 g/L, FeCl3 x 6 H2O 0.02 g/L, sulfur 10 g/L, yeast extract
0.5 g/L, Na2S x 9 H2O 0.5 g/L, MnCl2 x 4 H2O 0.18 g/L, Na2B4O7 x 10 H2O
0.45 g/L, ZnSO4 x 7 H2O 0.022 g/L, CuCl2 x 2 H2O 0.005 g/L,
Na2MoO4 x 2 H2O 0.003 g/L, VOSO4 x 2 H2O 0.003 g/L, and CoSO4 x 7 H2O
0.001 g/L.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/KOMODO_88-2_For_DSM_18786.yaml` | `data/normalized_yaml/bacterial/medium_88_modified_for_dsm_10039.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and liquid state; child is a DSM strain-specific copy of the Medium 88/Sulfolobus formulation. |
| `data/normalized_yaml/bacterial/KOMODO_88-2_For_DSM_18786.yaml` | `data/normalized_yaml/bacterial/medium_88_modified_for_dsm_12421.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and liquid state; child is a DSM strain-specific copy of the Medium 88/Sulfolobus formulation. |
| `data/normalized_yaml/bacterial/KOMODO_88-2_For_DSM_18786.yaml` | `data/normalized_yaml/bacterial/medium_88_modified_for_dsm_18247.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and liquid state; child is a DSM strain-specific copy of the Medium 88/Sulfolobus formulation. |
| `data/normalized_yaml/bacterial/KOMODO_88-2_For_DSM_18786.yaml` | `data/normalized_yaml/bacterial/medium_88_modified_for_dsm_5389.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and liquid state; child is a DSM strain-specific copy of the Medium 88/Sulfolobus formulation. |
| `data/normalized_yaml/bacterial/KOMODO_88-2_For_DSM_18786.yaml` | `data/normalized_yaml/bacterial/medium_88_modified_for_dsm_6482.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and liquid state; child is a DSM strain-specific copy of the Medium 88/Sulfolobus formulation. |
| `data/normalized_yaml/bacterial/KOMODO_88-2_For_DSM_18786.yaml` | `data/normalized_yaml/bacterial/medium_88_modified_for_dsm_7519.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and liquid state; child is a DSM strain-specific copy of the Medium 88/Sulfolobus formulation. |
| `data/normalized_yaml/bacterial/KOMODO_88-2_For_DSM_18786.yaml` | `data/normalized_yaml/specialized/sulfolobus_medium_anaerobic.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and liquid state; child is a named specialized copy of the Medium 88/Sulfolobus formulation. |

## Notes

- This batch completes the currently proposed Medium 88 exact-signature
  `SOURCE_DUPLICATE` family; the review scan found 0 remaining unlinked rows
  for ingredient signature `7914b41f36c2b043`.
- Existing child formulas were preserved; this batch only adds explicit
  parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/medium_88_source_duplicate_links.tsv`
- `just apply-media-variant-links --proposals /tmp/medium_88_source_duplicate_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the eight touched YAML
  files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,537 parent-to-child links, 2,537 child-to-parent links, 0 errors, and 0
  warnings.

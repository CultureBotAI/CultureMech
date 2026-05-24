# Phototrophic Medium Source-Duplicate Review

Date: 2026-05-14

## Scope

Reviewed six source-duplicate links under `for_dsm_17935`. The selected child
records all preserve the same parsed liquid formula as the parent: KH2PO4
0.5 g/L, MgCl2 x 6 H2O 1 g/L, NaCl 20 g/L, NH4Cl 0.6 g/L,
CaCl2 x 2 H2O 0.15 g/L, yeast extract 0.4 g/L, ferric citrate 0.005 g/L,
HCl 1 g/L, ZnCl2 0.07 g/L, MnCl2 x 4 H2O 0.1 g/L, H3BO3 0.06 g/L,
CoCl2 x 6 H2O 0.2 g/L, CuCl2 x 2 H2O 0.02 g/L,
NiCl2 x 6 H2O 0.02 g/L, Na2MoO4 x 2 H2O 0.04 g/L, and NaHCO3 100 g/L.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/for_dsm_17935.yaml` | `data/normalized_yaml/bacterial/for_dsm_17936.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and liquid state; child is a DSM strain-specific copy of the phototrophic medium formulation. |
| `data/normalized_yaml/bacterial/for_dsm_17935.yaml` | `data/normalized_yaml/bacterial/for_dsm_18632.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and liquid state; child is a DSM strain-specific copy of the phototrophic medium formulation. |
| `data/normalized_yaml/bacterial/for_dsm_17935.yaml` | `data/normalized_yaml/bacterial/for_dsm_18805.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and liquid state; child is a DSM strain-specific copy of the phototrophic medium formulation. |
| `data/normalized_yaml/bacterial/for_dsm_17935.yaml` | `data/normalized_yaml/bacterial/for_dsm_18858.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and liquid state; child is a DSM strain-specific copy of the phototrophic medium formulation. |
| `data/normalized_yaml/bacterial/for_dsm_17935.yaml` | `data/normalized_yaml/bacterial/phototrophic_medium.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and liquid state; child is a named copy of the phototrophic medium formulation. |
| `data/normalized_yaml/bacterial/for_dsm_17935.yaml` | `data/normalized_yaml/specialized/phototrophic_medium.yaml` | `SOURCE_DUPLICATE` | Same parsed ingredients, concentrations, and liquid state; child is a named specialized copy of the phototrophic medium formulation. |

## Notes

- This batch completes the currently proposed phototrophic exact-signature
  `SOURCE_DUPLICATE` family; the review scan found 0 remaining unlinked rows
  for ingredient signature `b17ab642616dba56`.
- Existing child formulas were preserved; this batch only adds explicit
  parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/phototrophic_source_duplicate_links.tsv`
- `just apply-media-variant-links --proposals /tmp/phototrophic_source_duplicate_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the seven touched YAML
  files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,543 parent-to-child links, 2,543 child-to-parent links, 0 errors, and 0
  warnings.

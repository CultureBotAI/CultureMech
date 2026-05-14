# Sulfurimonas Medium Source-Duplicate Review

Date: 2026-05-14

## Scope

Reviewed one source-duplicate link under
`KOMODO_1053_SULFURIMONAS_PARALVINELLA_MEDIUM`. The parent and child are both
liquid DSMZ/KOMODO Medium 1053 records at pH 6.5 with the same parsed
ingredient and concentration signature. The child record is a DSM 19353 copy
of the same source formulation.

The shared formula includes seawater/mineral salts, sulfur and thiosulfate,
trace metals, vitamins, and NaOH as a variable pH-adjustment component: NaCl
20.7824 g/L, MgSO4 x 7 H2O 6.95648 g/L, MgCl2 x 6 H2O 2.96736 g/L,
sulfur 9.8912 g/L, Na2S2O3 x 5 H2O 0.98912 g/L, NaHCO3 0.98912 g/L,
NaNO3 0.98912 g/L, CaCl2 0.791296 g/L, KCl 0.326409 g/L, NH4Cl 0.24728 g/L,
and matching trace-element and vitamin components.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/KOMODO_1053_SULFURIMONAS_PARALVINELLA_MEDIUM.yaml` | `data/normalized_yaml/bacterial/for_dsm_19353.yaml` | `SOURCE_DUPLICATE` | Same DSMZ Medium 1053 source, parsed ingredients, concentrations, pH, and liquid state; child is a DSM 19353 source copy. |

## Notes

- This batch completes the currently proposed Sulfurimonas exact-signature
  `SOURCE_DUPLICATE` family; the review scan found 0 remaining unlinked rows
  for ingredient signature `d8a407fee10ce971`.
- Existing child formulas were preserved; this batch only adds explicit
  parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/sulfurimonas_source_duplicate_links.tsv`
- `just apply-media-variant-links --proposals /tmp/sulfurimonas_source_duplicate_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the two touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,544 parent-to-child links, 2,544 child-to-parent links, 0 errors, and 0
  warnings.

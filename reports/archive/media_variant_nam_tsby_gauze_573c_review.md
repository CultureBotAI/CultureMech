# NAM, TSBY, Gauze, And 573C Variant Review

Date: 2026-05-14

## Scope

Reviewed four remaining low-cardinality candidate links covering one equivalent
source formulation and three concentration-variant relationships.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/TOGO_M2771_Serpulina_Murdochii_Medium.yaml` | `data/normalized_yaml/bacterial/nam_agar.yaml` | `SOURCE_DUPLICATE` | Both records share the tryptic soy agar base and blood supplement; 5% w/v sheep blood in the parent is represented as 50 g/L in the child. |
| `data/normalized_yaml/bacterial/JCM_J427_TSBY_SALT_MEDIUM.yaml` | `data/normalized_yaml/bacterial/tsby_salt_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps pH, TSBY base, yeast extract, NaCl, KCl, MgCl2, NH4Cl, and CaCl2 unchanged but increases MgSO4 x 7 H2O from 0.25 to 3.45 g/L. |
| `data/normalized_yaml/bacterial/TOGO_M72_Gauze_s_Synthetic_Medium_NO._1.yaml` | `data/normalized_yaml/bacterial/TOGO_M920_Gauze_s_Synthetic_Medium_NO._1_With_18_NaCl.yaml` | `CONCENTRATION_VARIANT` | Child keeps water, MgSO4, K2HPO4, KNO3, and soluble starch unchanged, increases NaCl from 0.5 to 180 g/L, lowers FeSO4 from 10 to 0.01 g/L, and changes agar from 15 to 18 g/L. |
| `data/normalized_yaml/bacterial/573c_medium.yaml` | `data/normalized_yaml/bacterial/alicyclobacillus_cellulosilyticus_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps the cellulose, ammonium sulfate, phosphate, glucose, yeast extract, and tryptone levels effectively unchanged but lowers MgSO4, CaCl2, and FeCl3 concentrations. |

## Notes

- NAM Agar was modeled as a source duplicate because the apparent blood
  difference is a unit representation difference.
- TSBY Salt was modeled as a concentration variant rather than a salinity
  variant because the reviewed axis is MgSO4.
- Existing child formulas were preserved; this batch only adds explicit
  parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/nam_tsby_gauze_573c_links.tsv`
- `just apply-media-variant-links --proposals /tmp/nam_tsby_gauze_573c_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the eight touched YAML
  files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,358 parent-to-child links, 2,358 child-to-parent links, 0 errors, and 0
  warnings.

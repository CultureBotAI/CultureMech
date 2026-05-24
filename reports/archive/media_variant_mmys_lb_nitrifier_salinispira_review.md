# MMYS, LB, Nitrifier, And Salinispira Variant Review

Date: 2026-05-13

## Scope

Reviewed four one-axis variants across TOGO and DSMZ records. The selected pairs
share a parsed ingredient set, medium type, and physical state, and differ by
one NaCl or nitrite concentration axis.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/TOGO_M186_Mmys-I_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M192_Mmys-III_Medium.yaml` | `SALINITY_VARIANT` | NaCl increases from 30.2 g/L to 50.2 g/L |
| `data/normalized_yaml/bacterial/TOGO_M2897_LB_medium.yaml` | `data/normalized_yaml/bacterial/luria_bertani_lb_medium.yaml` | `SALINITY_VARIANT` | NaCl increases from 0.5 g/L to 10 g/L |
| `data/normalized_yaml/bacterial/nitrospira_moscoviensis.yaml` | `data/normalized_yaml/bacterial/autotrophic_nitrobacter_medium.yaml` | `CONCENTRATION_VARIANT` | NaNO2 increases from 0.5 g/L to 2 g/L |
| `data/normalized_yaml/bacterial/salinispira_l21_ls_medium.yaml` | `data/normalized_yaml/bacterial/salinivirga_l21_hs_medium.yaml` | `SALINITY_VARIANT` | NaCl increases from 60.3472 g/L to 90.0208 g/L |

## Deferred

- SL/Petrotoga, MB/Methanosarcina, and TSBY salt pairs were left for later
  review because they cross source families or represent same-medium source
  discrepancies that should not be converted automatically.

## Validation

- `just apply-media-variant-links --proposals /tmp/mmys_lb_nitrifier_salinispira_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/mmys_lb_nitrifier_salinispira_variant_links.tsv --apply`
- Targeted `just validate-schema` loop passed for all 8 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,289 parent-to-child links, 2,289 child-to-parent links, 0 errors, and
  0 warnings.

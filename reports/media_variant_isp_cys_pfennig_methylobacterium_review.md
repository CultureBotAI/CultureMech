# ISP, CYS, Pfennig, And Methylobacterium Variant Review

Date: 2026-05-13

## Scope

Reviewed five one-axis salinity or concentration variants across TOGO and DSMZ
records. Parent records were chosen from the local source family and existing
formulation context rather than blindly following proposal direction.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/inorganic_salts_starch_agar_isp_medium_no_4.yaml` | `data/normalized_yaml/bacterial/inorganic_salt_solution_agar_isp_medium_no_4_10_nacl.yaml` | `SALINITY_VARIANT` | NaCl increases from 1 g/L to 100 g/L |
| `data/normalized_yaml/bacterial/inorganic_salts_starch_agar_isp_medium_no_4.yaml` | `data/normalized_yaml/bacterial/isp_4_plus_20_nacl.yaml` | `SALINITY_VARIANT` | NaCl increases from 1 g/L to 200 g/L |
| `data/normalized_yaml/bacterial/TOGO_M627_CYS_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M628_CYS_Medium_For_YMO722.yaml` | `SALINITY_VARIANT` | NaCl decreases from 20 g/L to 16 g/L |
| `data/normalized_yaml/bacterial/DSMZ_46_PFENNIG_S_MEDIUM_I_WITH_SALT.yaml` | `data/normalized_yaml/bacterial/pfennigs_medium_i_with_salt.yaml` | `SALINITY_VARIANT` | NaCl increases from 10 g/L to 30 g/L |
| `data/normalized_yaml/bacterial/TOGO_M1553_Methylobacterium_Medium.yaml` | `data/normalized_yaml/bacterial/togo_medium_m1529.yaml` | `CONCENTRATION_VARIANT` | MgSO4·7H2O decreases from 1 g/L to 0.5 g/L |

## Deferred

- The KOMODO/DSMZ CYS concentration discrepancy was not applied because both
  records point to DSMZ Medium 1108 but disagree on NaCl, making it more likely
  a source/import discrepancy than a curated variant.
- The Trypticase Soy Broth liquid salt pair was left for later review because
  it crosses TOGO and JCM/MediaDive source families.

## Validation

- `just apply-media-variant-links --proposals /tmp/isp_cys_pfennig_methylobacterium_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/isp_cys_pfennig_methylobacterium_variant_links.tsv --apply`
- Targeted `just validate-schema` loop passed for all 9 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,285 parent-to-child links, 2,285 child-to-parent links, 0 errors, and
  0 warnings.

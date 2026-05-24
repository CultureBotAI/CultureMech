# TOGO Trypticase Soy Broth Agar NaCl/pH Variant Review

Date: 2026-05-14

## Scope

Reviewed a source-local TOGO/NBRC trypticase soy broth agar family where the
parsed base formulation is unchanged and the variant axis is added NaCl or pH.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/TOGO_M907_Trypticase_Soy_Broth_With_5_NaCl.yaml` | `data/normalized_yaml/bacterial/TOGO_M1355_Trypticase_Soy_Broth_Agar_With_3_NaCl.yaml` | `SALINITY_VARIANT` | Added NaCl changes from 5% (50 g/L) to 3% (30 g/L); parsed trypticase soy broth agar base remains unchanged. |
| `data/normalized_yaml/bacterial/TOGO_M907_Trypticase_Soy_Broth_With_5_NaCl.yaml` | `data/normalized_yaml/bacterial/TOGO_M488_Trypticase_Soy_Broth_Agar_With_10_NaCl.yaml` | `SALINITY_VARIANT` | Added NaCl changes from 5% (50 g/L) to 10% (100 g/L); parsed trypticase soy broth agar base remains unchanged. |
| `data/normalized_yaml/bacterial/TOGO_M907_Trypticase_Soy_Broth_With_5_NaCl.yaml` | `data/normalized_yaml/bacterial/TOGO_M489_Trypticase_Soy_Broth_Agar_With_5_NaCl_pH_8.0.yaml` | `PH_VARIANT` | Added NaCl remains 5% (50 g/L); child source label specifies pH 8.0. |

## Notes

- The parent and children all share the parsed trypticase soy broth agar base:
  pancreatic digest of casein, peptic digest of soybean meal, glucose, sodium
  chloride, dipotassium phosphate, and agar.
- The pH child was updated with `ph_value: 8.0`, matching its source label and
  the equivalent normalized non-TOGO record.
- This batch keeps the source-local TOGO records linked within their own group
  instead of merging them with the already curated JCM/MediaDive TSB agar
  salinity group.

## Validation

- `just apply-media-variant-links --proposals /tmp/togo_tsb_nacl_ph_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/togo_tsb_nacl_ph_variant_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the four touched YAML
  files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,332 parent-to-child links, 2,332 child-to-parent links, 0 errors, and 0
  warnings.

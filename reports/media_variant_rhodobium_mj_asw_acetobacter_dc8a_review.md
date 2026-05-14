# Rhodobium, MJ, ASW, Acetobacter, And DC-8A Concentration Review

Date: 2026-05-14

## Scope

Reviewed five concentration-variant links with directly inspectable formula
deltas across bacterial and algae media records.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/rhodobium_gokurnum_medium.yaml` | `data/normalized_yaml/bacterial/modified_rhodobacter_spaeroides_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps phosphate, sorbitol, pyruvate, ferric citrate, HCl, and trace components effectively unchanged but lowers MgCl2, NaCl, NH4Cl, and CaCl2, raises yeast extract, and changes pH from 6.8 to 7.0. |
| `data/normalized_yaml/bacterial/mj_basal_medium.yaml` | `data/normalized_yaml/bacterial/mj_medium_for_microaerophilic_autotrophs.yaml` | `CONCENTRATION_VARIANT` | Child keeps the marine salt, trace metal, and vitamin base unchanged but raises NaHCO3 from 1.4985 to 5 g/L and Na2S2O3 x 5 H2O from 1.4985 to 15 g/L, with pH 5.5 recorded in the child. |
| `data/normalized_yaml/algae/asw_ses.yaml` | `data/normalized_yaml/algae/nss_low.yaml` | `CONCENTRATION_VARIANT` | Child keeps vitamins, inositol, thymine, and tricine unchanged but halves NaNO, Na HPO, and K HPO concentrations. |
| `data/normalized_yaml/bacterial/gluconacetobacter_xylinus_medium.yaml` | `data/normalized_yaml/bacterial/acetobacter_diazotrophicus_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps water, yeast extract, and agar unchanged, lowers glucose from 100 to 50 g/L, and raises CaCO3 from 20 to 30 g/L. |
| `data/normalized_yaml/bacterial/dc_8a_medium.yaml` | `data/normalized_yaml/bacterial/paenibacillus_dc_8a_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps pH and all parsed ingredients unchanged except xylose, which increases from 10 to 100 g/L. |

## Notes

- Candidate rows with sea-water normalization artifacts or unclear formula
  axes were left for separate review.
- Existing child formulas were preserved; this batch only adds explicit
  parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/rhodobium_mj_asw_acetobacter_dc8a_links.tsv`
- `just apply-media-variant-links --proposals /tmp/rhodobium_mj_asw_acetobacter_dc8a_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the ten touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,363 parent-to-child links, 2,363 child-to-parent links, 0 errors, and 0
  warnings.

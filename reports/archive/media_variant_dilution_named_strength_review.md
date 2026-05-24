# Dilution And Named Strength Variant Review

Date: 2026-05-14

## Scope

Reviewed seven source-local or same-provider records with explicit dilution,
half-strength, quad-strength, or named-strength formulations. The selected
pairs share a recognizable base medium and were modeled as
`CONCENTRATION_VARIANT` child records.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/1_2_marine_broth_agar.yaml` | `data/normalized_yaml/bacterial/1_5_marine_agar_broth.yaml` | `CONCENTRATION_VARIANT` | Bacto Marine Broth 2216 decreases from 18.7 g/L to 7 g/L; agar remains 15 g/L |
| `data/normalized_yaml/bacterial/1_2_marine_broth_agar.yaml` | `data/normalized_yaml/bacterial/1_10_marine_broth_agar.yaml` | `CONCENTRATION_VARIANT` | Bacto Marine Broth 2216 decreases from 18.7 g/L to 3.7 g/L; agar remains 15 g/L |
| `data/normalized_yaml/bacterial/lb_medium.yaml` | `data/normalized_yaml/bacterial/1_3_lb.yaml` | `CONCENTRATION_VARIANT` | Yeast extract decreases from 5 g/L to 1.67 g/L and peptone decreases from 10 g/L to 3.33 g/L; NaCl and agar remain unchanged |
| `data/normalized_yaml/bacterial/tryptone_soya_broth_tsb.yaml` | `data/normalized_yaml/bacterial/diluted_tryptone_soya_broth_tsb_1_10.yaml` | `CONCENTRATION_VARIANT` | All parsed TSB components are ten-fold lower in the 1:10 child |
| `data/normalized_yaml/bacterial/f_2.yaml` | `data/normalized_yaml/bacterial/f_2_quad.yaml` | `CONCENTRATION_VARIANT` | NaNO3 and NaH2PO4 x 2 H2O increase from 1 g/L to 4 g/L |
| `data/normalized_yaml/bacterial/DSMZ_1419_HYPHOMICROBIUM_MEDIUM.yaml` | `data/normalized_yaml/bacterial/half_strenghs_hyphomicrobium_medium.yaml` | `CONCENTRATION_VARIANT` | Phosphate, methylamine hydrochloride, ammonium sulfate, and peptone are half-strength; agar and trace/vitamin solutions remain effectively unchanged |
| `data/normalized_yaml/bacterial/isp_5_medium.yaml` | `data/normalized_yaml/bacterial/glycerol_asparagine_agar_isp_5.yaml` | `CONCENTRATION_VARIANT` | ISP-5 defined base recipe is near-identical after rounding and agar decreases from 20 g/L to about 15 g/L |

## Deferred

- `data/normalized_yaml/bacterial/f_10.yaml` was deferred because the parsed
  concentration difference is dominated by a natural-seawater amount that needs
  source interpretation before modeling it as an f/2 dilution child.
- Other proposed LB and TSB salt/agar records were deferred where dilution,
  salinity, pH, and physical-state changes were mixed.

## Validation

- `just apply-media-variant-links --proposals /tmp/dilution_and_named_strength_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/dilution_and_named_strength_variant_links.tsv --apply`
- Targeted `just validate-schema` passed for all 13 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,312 parent-to-child links, 2,312 child-to-parent links, 0 errors, and
  0 warnings.

# Defined And Source-Local Strength Concentration Review

Date: 2026-05-14

## Scope

Reviewed three small concentration-variant pairs where the child record shares
the recognizable parent formulation but changes a limited set of concentrations.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml` | `data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml` | `CONCENTRATION_VARIANT` | Continuous-cultivation CDM lowers glucose from 126.2 to 40.37 mM and ammonium sulfate from 55.24 to 37.84 mM; remaining parsed concentrations match. |
| `data/normalized_yaml/bacterial/3n_bbm_v.yaml` | `data/normalized_yaml/bacterial/3n_bbm_v_recipe_for_customer_orders.yaml` | `CONCENTRATION_VARIANT` | Customer-order 3N-BBM+V lowers CaCl2, MgSO4, K2HPO4, KH2PO4, and NaCl relative to the parent while retaining the same trace/vitamin/agar base. |
| `data/normalized_yaml/bacterial/TOGO_M1540_Enriched_Cytophaga_Agar.yaml` | `data/normalized_yaml/bacterial/togo_medium_m1491.yaml` | `CONCENTRATION_VARIANT` | Source-local child lowers Bacto Tryptone from 2.0 to 0.5 g/L and beef extract from 0.5 to 0.2 g/L while water, yeast extract, sodium acetate, and agar remain unchanged. |

## Notes

- These links were selected from remaining high-confidence low-cardinality
  proposal rows after excluding candidates where the parsed ingredients did not
  expose the named variant axis cleanly.
- All three child records retain full YAML formulations; the new links only add
  explicit parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/defined_strength_concentration_links.tsv`
- `just apply-media-variant-links --proposals /tmp/defined_strength_concentration_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the six touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,338 parent-to-child links, 2,338 child-to-parent links, 0 errors, and 0
  warnings.

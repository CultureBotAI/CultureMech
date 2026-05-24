# Rhodobacter, Halosimplex, And Acetobacter Concentration Review

Date: 2026-05-14

## Scope

Reviewed four concentration-variant links where child records retain a
recognizable parent formulation and differ by explicit component
concentrations.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/TOGO_M517_Rhodobium_Gokurnum_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M585_Rhodobacter_Sphaeroides_Medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps water, yeast extract, KH2PO4, pyruvate, sorbitol, HCl, and trace components unchanged, lowers NaCl, CaCl2, and MgCl2, and raises NH4Cl. |
| `data/normalized_yaml/bacterial/TOGO_M517_Rhodobium_Gokurnum_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M593_Modified_Rhodobacter_Spaeroides_Medium.yaml` | `CONCENTRATION_VARIANT` | Child lowers NaCl, CaCl2, MgCl2, and NH4Cl and raises yeast extract from 0.4 to 0.6 g/L while retaining the same core formulation. |
| `data/normalized_yaml/bacterial/TOGO_M293_Halosimplex_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M986_Modified_Halosimplex_Medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps K2HPO4, KCl, ammonium sulfate, sodium pyruvate, glycerol, and agar unchanged while MgSO4 decreases from 20 to 10 g/L and NaCl increases from 200 to 210 g/L. |
| `data/normalized_yaml/bacterial/JCM_J890_ACETOBACTER_EUROPAEUS_MEDIUM.yaml` | `data/normalized_yaml/bacterial/gluconacetobacter_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps glucose and ethanol unchanged, raises yeast extract and peptone, lowers acetic acid, and lowers agar from 20 to 15 g/L. |

## Notes

- These candidates were selected after inspecting ingredient/concentration
  deltas directly.
- The broader Haloalkaliphile candidate remains unapplied because its parsed
  water/carbonate representation requires a separate source-level review.
- Existing child formulas were preserved; this batch only adds explicit
  parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/rhodobacter_halosimplex_acetobacter_links.tsv`
- `just apply-media-variant-links --proposals /tmp/rhodobacter_halosimplex_acetobacter_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the seven touched YAML
  files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,346 parent-to-child links, 2,346 child-to-parent links, 0 errors, and 0
  warnings.

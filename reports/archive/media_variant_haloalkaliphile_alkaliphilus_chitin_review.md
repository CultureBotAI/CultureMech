# Haloalkaliphile, Alkaliphilus, And Chitin Medium Concentration Review

Date: 2026-05-14

## Scope

Reviewed four concentration-variant links where child records retain a
recognizable parent formulation and differ by explicit salt, carbonate,
thiosulfate, or yeast-extract concentrations.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/TOGO_M301_Haloalkaliphile_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M1302_Modified_Haloalkaliphile_Medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps MgSO4, NaCl, KCl, CaSO4, sodium glutamate, citrate, yeast extract, and casamino acids unchanged while Na2CO3 increases from 8 to 80 g/L; water amount differs by source normalization. |
| `data/normalized_yaml/bacterial/haloalkaliphile_medium.yaml` | `data/normalized_yaml/bacterial/modified_haloalkaliphile_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps yeast extract, casamino acids, Na glutamate, MgSO4, CaSO4, KCl, and NaCl unchanged while Na2CO3 increases from 8 to 80 g/L; citrate hydrate label differs. |
| `data/normalized_yaml/bacterial/alkaliphilus_3b_medium.yaml` | `data/normalized_yaml/bacterial/alkaliphilus_lacv_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps pH and most base/supplement concentrations unchanged, increases NaCl from 0.993049 to 9.93049 g/L and thiosulfate from 1.48957 to 2.97915 g/L, and lowers yeast extract from 50 to 20 g/L. |
| `data/normalized_yaml/bacterial/chitinivibrio_medium.yaml` | `data/normalized_yaml/bacterial/chitinispirillum_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps pH, NaCl, K2HPO4, chitin, MgSO4, yeast extract, NH4Cl, sulfide, vitamins, and trace elements unchanged while NaHCO3 decreases from 15 to 8 g/L and Na2CO3 decreases from 95 to 22 g/L. |

## Notes

- These candidates were applied only after direct ingredient and concentration
  inspection.
- The TOGO Haloalkaliphile child records a normalized water amount that differs
  from the parent; the curated variant axis is Na2CO3 because the rest of the
  base formulation is unchanged or hydrate-equivalent.
- Existing child formulas were preserved; this batch only adds explicit
  parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/haloalkaliphile_alkaliphilus_chitin_links.tsv`
- `just apply-media-variant-links --proposals /tmp/haloalkaliphile_alkaliphilus_chitin_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the eight touched YAML
  files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,350 parent-to-child links, 2,350 child-to-parent links, 0 errors, and 0
  warnings.

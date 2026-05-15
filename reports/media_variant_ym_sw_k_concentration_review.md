# YM, SW-20, And K Medium Concentration Review

Date: 2026-05-14

## Scope

Reviewed four remaining high-confidence concentration-variant links where the
child record shares the parent formulation and the parsed concentration deltas
are explicit.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/TOGO_M630_SW-20_Medium.yaml` | `data/normalized_yaml/bacterial/TOGO_M1033_Kushneria_Aurantia_Medium.yaml` | `CONCENTRATION_VARIANT` | Child halves MgSO4, yeast extract, NaCl, CaCl2, MgCl2, KCl, NaHCO3, and NaBr relative to SW-20 while agar remains 20 g/L. |
| `data/normalized_yaml/bacterial/ym_agar.yaml` | `data/normalized_yaml/bacterial/my20_agar.yaml` | `CONCENTRATION_VARIANT` | Child keeps peptone, yeast extract, malt extract, and agar unchanged but increases glucose from 10 g/L to 200 g/L. |
| `data/normalized_yaml/bacterial/ym_agar.yaml` | `data/normalized_yaml/bacterial/acidomonas_medium.yaml` | `CONCENTRATION_VARIANT` | Child doubles glucose, peptone, yeast extract, malt extract, and agar and changes pH from 6.2 to 4.0. |
| `data/normalized_yaml/bacterial/JCM_J1154_K_MEDIUM.yaml` | `data/normalized_yaml/bacterial/medium_k.yaml` | `CONCENTRATION_VARIANT` | Child keeps ammonium sulfate, KH2PO4, NaCl, and MgSO4 unchanged, lowers FeSO4 and methanol, increases agar, and changes pH from 7.4 to 7.2. |

## Notes

- These links were selected from the remaining low-cardinality proposal rows
  after direct ingredient inspection.
- Candidate records with name-only salt claims or multiple unresolved parsed
  differences remain unapplied for later review.
- Existing child YAML formulations were preserved; this batch only added
  explicit parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/ym_sw_k_concentration_links.tsv`
- `just apply-media-variant-links --proposals /tmp/ym_sw_k_concentration_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the seven touched YAML
  files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,342 parent-to-child links, 2,342 child-to-parent links, 0 errors, and 0
  warnings.

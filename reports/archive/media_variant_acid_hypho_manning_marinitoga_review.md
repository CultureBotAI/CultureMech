# Acidimicrobium, Hyphomicrobium, Manning, And Marinitoga Review

Date: 2026-05-14

## Scope

Reviewed four concentration-variant links with directly inspected formula
deltas across JCM, KOMODO, and normalized bacterial media records.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml` | `data/normalized_yaml/bacterial/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml` | `CONCENTRATION_VARIANT` | Child keeps acidic pH 1.7 and the same component set but changes sulfate/phosphate salts, raises FeSO4 from 0.00998004 to 25 g/L, and lowers yeast extract from 2.5 to 0.16 g/L. |
| `data/normalized_yaml/bacterial/JCM_J884_HYPHOMICROBIUM_MEDIUM.yaml` | `data/normalized_yaml/bacterial/hyphomicrobium_strain_x_medium.yaml` | `CONCENTRATION_VARIANT` | Child shares the methylamine agar and trace-element formulation but changes phosphate/ammonium/methylamine and raises trace-element stock concentrations, with pH 7.2 recorded in the child. |
| `data/normalized_yaml/bacterial/KOMODO_1023_MANNING_medium.yaml` | `data/normalized_yaml/bacterial/sulfobacillus_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps the same component set and yeast extract level, changes ammonium sulfate, KCl, K2HPO4, MgSO4, Ca(NO3)2, and FeSO4 concentrations, and resolves H2SO4 from variable to 1 g/L. |
| `data/normalized_yaml/bacterial/JCM_J1047_MARINITOGA_MEDIUM.yaml` | `data/normalized_yaml/bacterial/JCM_J997_MARINITOGA_MEDIUM.yaml` | `CONCENTRATION_VARIANT` | Child keeps pH 7.0 and the same sea-salt/PIPES/yeast-extract/tryptone/reducing-agent base but lowers glucose from 14 to 2.5 g/L and reducing agents from 10 to 0.5 g/L, with small rounded base concentrations. |

## Notes

- The water-only GAM row and malformed NBRC TSB rows were left unapplied.
- Existing child formulas were preserved; this batch only adds explicit
  parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/acid_hypho_manning_marinitoga_links.tsv`
- `just apply-media-variant-links --proposals /tmp/acid_hypho_manning_marinitoga_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the eight touched YAML
  files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,367 parent-to-child links, 2,367 child-to-parent links, 0 errors, and 0
  warnings.

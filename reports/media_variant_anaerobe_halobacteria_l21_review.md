# Anaerobe, Halobacteria, And L21 Concentration Review

Date: 2026-05-14

## Scope

Reviewed four concentration-variant links with directly inspected formula
deltas across anaerobe, halobacteria, and L21-style bacterial media records.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/desulfovibrio_oceani_medium.yaml` | `data/normalized_yaml/bacterial/desulfovibrio_arsenicitolerans_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps the same sulfate-reducer base but changes salinity, bicarbonate, sulfide, lactate, and pH-related formulation axes. |
| `data/normalized_yaml/bacterial/gudongella_medium.yaml` | `data/normalized_yaml/bacterial/methanobacterium_medium.yaml` | `CONCENTRATION_VARIANT` | Child shares the anaerobic carbonate/bicarbonate medium pattern but changes the bicarbonate/carbonate buffer concentration profile. |
| `data/normalized_yaml/bacterial/halobacteria_hmd_medium.yaml` | `data/normalized_yaml/bacterial/halosarcina_pallida_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps the halobacteria high-salt base and differs mainly on ammonium, casamino-acid, and pH axes. |
| `data/normalized_yaml/bacterial/kiritimatiella_l21_ls_medium.yaml` | `data/normalized_yaml/bacterial/sedimentisphaera_l21_hs_medium.yaml` | `CONCENTRATION_VARIANT` | Child shares the L21-style base and differs by NaCl, reducing-agent, and pH axes. |

## Notes

- These links were selected after direct formula inspection.
- Extreme scaling rows and name-only rows where the parsed axis was not
  represented clearly in the YAML were left unapplied.
- Existing child formulas were preserved; this batch only adds explicit
  parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/anaerobe_halobacteria_l21_links.tsv`
- `just apply-media-variant-links --proposals /tmp/anaerobe_halobacteria_l21_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the eight touched YAML
  files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,371 parent-to-child links, 2,371 child-to-parent links, 0 errors, and 0
  warnings.

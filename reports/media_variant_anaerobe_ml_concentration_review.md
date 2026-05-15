# Anaerobe And ML Medium Concentration Review

Date: 2026-05-14

## Scope

Reviewed four concentration-variant links in anaerobic defined/complex media
and alkaline ML media. Each child record retains a recognizable parent
formulation and differs by explicit concentration axes.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/acetobacterium_medium.yaml` | `data/normalized_yaml/bacterial/moorella_thermoacetica_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps the anaerobic base, fructose, reductants, trace elements, and vitamins unchanged but lowers NaHCO3 from 9.79432 to 0.979432 g/L and records pH 6.5. |
| `data/normalized_yaml/bacterial/desulfobacter_medium.yaml` | `data/normalized_yaml/bacterial/desulfobacter_curvatus_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps the defined sulfate-reducer base, carbonate, sulfide, trace elements, and vitamins but raises NaCl, MgCl2, and sodium acetate concentrations. |
| `data/normalized_yaml/bacterial/desulfotignum_medium.yaml` | `data/normalized_yaml/bacterial/desulfobacterium_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps the defined sulfate-reducer base, carbonate, trace elements, and vitamins but changes NaCl, MgCl2, pyruvate, and sulfide concentrations. |
| `data/normalized_yaml/bacterial/ml_medium.yaml` | `data/normalized_yaml/bacterial/ml_15_medium.yaml` | `CONCENTRATION_VARIANT` | Child keeps the alkaline salt base with small normalization-scale differences and increases yeast extract from 5 to 20 g/L. |

## Notes

- These candidates were selected from remaining high-confidence, low-cardinality
  proposals after direct formula inspection.
- Sea-water amount rows and broader cyanobacteria/acidophile pairs were left
  unapplied for separate review because their parsed axes are less clean.
- Existing child formulas were preserved; this batch only adds explicit
  parent/child variant metadata.

## Validation

- `just apply-media-variant-links --proposals /tmp/anaerobe_ml_concentration_links.tsv`
- `just apply-media-variant-links --proposals /tmp/anaerobe_ml_concentration_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the eight touched YAML
  files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,354 parent-to-child links, 2,354 child-to-parent links, 0 errors, and 0
  warnings.

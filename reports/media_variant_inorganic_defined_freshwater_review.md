# Inorganic And Defined Freshwater Concentration Variant Review

Date: 2026-05-13

## Scope

Reviewed five MediaDB-backed concentration-variant pairs where the records share
the same ingredient identities and differ by one concentration axis.

## Applied Decisions

| Parent | Child | Difference | Decision |
|---|---|---|---|
| `data/normalized_yaml/bacterial/inorganic_medium.yaml` | `data/normalized_yaml/bacterial/fex5_medium.yaml` | Ferrous sulfate increases from 0.05 mM to 0.25 mM | Apply as `CONCENTRATION_VARIANT` |
| `data/normalized_yaml/bacterial/MEDIADB_435_Defined_freshwater_medium_CoSO4.yaml` | `data/normalized_yaml/bacterial/MEDIADB_434_Defined_freshwater_medium_CoSO4.yaml` | Toluene increases from 1 mM to 10 mM | Apply as `CONCENTRATION_VARIANT` |
| `data/normalized_yaml/bacterial/MEDIADB_446_Defined_freshwater_medium_CoCl2.yaml` | `data/normalized_yaml/bacterial/MEDIADB_448_Defined_freshwater_medium_CoCl2.yaml` | Nitrate increases from 5 mM to 20 mM | Apply as `CONCENTRATION_VARIANT` |
| `data/normalized_yaml/bacterial/MEDIADB_419_Defined_freshwater_medium_CoSO4.yaml` | `data/normalized_yaml/bacterial/MEDIADB_421_Defined_freshwater_medium_CoSO4.yaml` | Nitrate increases from 5 mM to 20 mM | Apply as `CONCENTRATION_VARIANT` |
| `data/normalized_yaml/bacterial/MEDIADB_463_Defined_freshwater_medium_CoCl2.yaml` | `data/normalized_yaml/bacterial/MEDIADB_457_Defined_freshwater_medium_CoCl2.yaml` | Toluene increases from 1 mM to 10 mM | Apply as `CONCENTRATION_VARIANT` |

## Notes

- The inorganic/Fex5 pair is modeled with the lower-ferrous-sulfate inorganic
  medium as parent and Fex5 as the higher-ferrous-sulfate child.
- The defined freshwater pairs are source-local MediaDB records. Each child
  keeps the full original formulation and receives the explicit parent link,
  relationship, and concentration-difference summary.
- No organism growth claims were added in this batch.

## Validation

- `just apply-media-variant-links --proposals /tmp/inorganic_defined_freshwater_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/inorganic_defined_freshwater_variant_links.tsv --apply`
- Targeted `just validate-schema` loop passed for all 10 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,249 parent-to-child links, 2,249 child-to-parent links, 0 errors, and
  0 warnings.

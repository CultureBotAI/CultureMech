# Specialized Strength Variant Review

Date: 2026-05-14

## Scope

Reviewed four specialized medium records with explicit strength or named
formulation variants. The selected pairs keep the same recognizable parent
medium family and differ by concentration sets, so they were modeled as
`CONCENTRATION_VARIANT` child records.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/specialized/ms_basal_salts_robin.yaml` | `data/normalized_yaml/specialized/ms_basal_salts_robin_0_5x.yaml` | `CONCENTRATION_VARIANT` | Basal salts and trace elements are half-strength, including ammonium nitrate 1650 to 825 mg/L and potassium nitrate 1900 to 950 mg/L |
| `data/normalized_yaml/specialized/ms_basal_salts_robin.yaml` | `data/normalized_yaml/specialized/ms_basal_salts_robin_lowphosphate_0_5x.yaml` | `CONCENTRATION_VARIANT` | Most salts are half-strength and potassium phosphate monobasic is lowered from 1250 uM to 30 uM |
| `data/normalized_yaml/specialized/sgw_northen_exometabolite_mix_1.yaml` | `data/normalized_yaml/specialized/sgw_northen_exometabolite_mix_2x.yaml` | `CONCENTRATION_VARIANT` | Basal salts and vitamins remain unchanged while parsed exometabolite components decrease, including D-mannitol 880.5 to 176.1 uM |
| `data/normalized_yaml/specialized/sgw_northen_exometabolite_mix_1.yaml` | `data/normalized_yaml/specialized/sgw_northen_exometabolite_mix_5x.yaml` | `CONCENTRATION_VARIANT` | Basal salts and vitamins remain unchanged while parsed exometabolite components decrease, including D-mannitol 880.5 to 440.25 uM |

## Deferred

- `data/normalized_yaml/specialized/r2a_20mm_nitrate.yaml` was deferred because
  the parsed ingredient list does not expose the nitrate axis implied by the
  record name.
- `data/normalized_yaml/algae/asw_ses.yaml` to
  `data/normalized_yaml/algae/nss_low.yaml` was deferred with the broader algae
  family review because the local names do not establish a clean parent-child
  formulation relationship by themselves.

## Validation

- `just apply-media-variant-links --proposals /tmp/specialized_strength_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/specialized_strength_variant_links.tsv --apply`
- Targeted `just validate-schema` passed for all 6 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,305 parent-to-child links, 2,305 child-to-parent links, 0 errors, and
  0 warnings.

# TSB And GYM Salinity Variant Review

Date: 2026-05-14

## Scope

Reviewed three explicit salinity variants in TSB and GYM Streptomyces medium
families. The selected records preserve the recognizable base formulation and
change the supplemental NaCl axis.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/trypticase_soy_broth_with_nacl.yaml` | `data/normalized_yaml/bacterial/tryptic_soy_broth_containing_1_nacl.yaml` | `SALINITY_VARIANT` | Added NaCl changes from 15 g/L to 1% w/v while the parsed TSB base remains unchanged |
| `data/normalized_yaml/bacterial/trypticase_soy_broth_with_nacl.yaml` | `data/normalized_yaml/bacterial/trypticase_soy_broth_plus_1_sodium_chloride.yaml` | `SALINITY_VARIANT` | Added salt changes from 15 g/L NaCl to 1% w/v sodium chloride while the parsed TSB base remains unchanged |
| `data/normalized_yaml/bacterial/gym_streptomyces_medium_10_nacl.yaml` | `data/normalized_yaml/bacterial/gym_agar_with_15_nacl.yaml` | `SALINITY_VARIANT` | NaCl increases from 100 g/L to 150 g/L while glucose, yeast extract, malt extract, CaCO3, and agar remain unchanged |

## Deferred

- `data/normalized_yaml/bacterial/trypticase_soy_broth_with_5_nacl.yaml` was
  deferred because it crosses the TOGO/MediaDive source boundary and should be
  reviewed with the broader TSB family.
- Seawater YPG and sulfate-reducing bacterium candidates were deferred because
  their parsed differences are not clean salinity-only axes.

## Validation

- `just apply-media-variant-links --proposals /tmp/tsb_gym_salinity_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/tsb_gym_salinity_variant_links.tsv --apply`
- Targeted `just validate-schema` passed for all 5 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,323 parent-to-child links, 2,323 child-to-parent links, 0 errors, and
  0 warnings.

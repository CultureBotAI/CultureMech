# HMM Junlon PW 110 Concentration-Grid Variant Review

Date: 2026-05-13

## Scope

Reviewed the MediaDB HMM Junlon PW 110 records:

- `data/normalized_yaml/bacterial/hmm_with_1_g_l_junlon_pw_110_hobbs_et_al.yaml`
- `data/normalized_yaml/bacterial/hmm_with_0_5_g_l_junlon_pw_110_hobbs_et_al.yaml`
- `data/normalized_yaml/bacterial/hmm_with_1_5_g_l_junlon_pw_110_hobbs_et_al.yaml`
- `data/normalized_yaml/bacterial/hmm_with_2_g_l_junlon_pw_110_hobbs_et_al.yaml`

## Decision

Applied `CONCENTRATION_VARIANT` links from parent
`hmm_with_1_g_l_junlon_pw_110_hobbs_et_al` to the 0.5, 1.5, and 2 g/L Junlon
PW 110 child records.

Rationale:

- All four records are MediaDB records imported from the same source family and
  reference.
- All four records share the same parsed ingredient identities and physical
  state.
- The record names describe a Junlon PW 110 dose series. In the current parsed
  YAML, that dose axis appears as the `Propenoate` concentration:
  6.93866, 13.8773, 20.816, and 27.7546 mM.
- The child records preserve their full formulations and now carry explicit
  child-to-parent links, while the parent carries reciprocal `variant_children`
  links.

## Applied Links

| Parent | Child | Relationship | Modification summary |
|---|---|---|---|
| `hmm_with_1_g_l_junlon_pw_110_hobbs_et_al` | `hmm_with_0_5_g_l_junlon_pw_110_hobbs_et_al` | `CONCENTRATION_VARIANT` | Junlon dose changes from 1 g/L to 0.5 g/L; parsed Propenoate changes from 13.8773 mM to 6.93866 mM. |
| `hmm_with_1_g_l_junlon_pw_110_hobbs_et_al` | `hmm_with_1_5_g_l_junlon_pw_110_hobbs_et_al` | `CONCENTRATION_VARIANT` | Junlon dose changes from 1 g/L to 1.5 g/L; parsed Propenoate changes from 13.8773 mM to 20.816 mM. |
| `hmm_with_1_g_l_junlon_pw_110_hobbs_et_al` | `hmm_with_2_g_l_junlon_pw_110_hobbs_et_al` | `CONCENTRATION_VARIANT` | Junlon dose changes from 1 g/L to 2 g/L; parsed Propenoate changes from 13.8773 mM to 27.7546 mM. |

## Validation

Validation was run after applying the links:

- Targeted schema validation passed for all 4 touched HMM Junlon YAML files.
- `just validate-media-variant-links` scanned 15,827 records and reported
  2,233 parent-to-child links, 2,233 child-to-parent links, 0 errors, and
  0 warnings.

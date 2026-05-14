# MRS NaCl Salinity Variant Review

Date: 2026-05-13

## Scope

Reviewed two parallel MRS NaCl salinity families:

- JCM/MediaDive records:
  - `data/normalized_yaml/bacterial/mrs_medium_with_10_nacl.yaml`
  - `data/normalized_yaml/bacterial/mrs_medium_with_2_5_nacl.yaml`
  - `data/normalized_yaml/bacterial/mrs_medium_with_2_5_nacl_ph_9_0.yaml`
- TOGO-imported records:
  - `data/normalized_yaml/bacterial/TOGO_M249_MRS_Medium_With_10_NaCl.yaml`
  - `data/normalized_yaml/bacterial/TOGO_M602_MRS_Medium_With_2.5_NaCl.yaml`
  - `data/normalized_yaml/bacterial/TOGO_M977_MRS_Medium_With_2.5_NaCl_pH_9.0.yaml`

## Decision

Applied `SALINITY_VARIANT` links within each source family from the 10% NaCl
parent to the two 2.5% NaCl child records.

Rationale:

- The MediaDive/JCM and TOGO records are parallel source imports with slightly
  different parsed ingredient representations, so they were kept as two
  separate parent groups instead of merged blindly.
- Within each source family, the child records share the same parsed ingredient
  identities and physical state as the parent.
- The main parsed concentration difference is NaCl: 100 g/L in the parent and
  25 g/L in the child records.
- The pH 9.0 child records also carry an explicit alkaline pH condition, which
  is recorded in the variant modification text.

## Applied Links

| Parent | Child | Relationship | Modification summary |
|---|---|---|---|
| `mrs_medium_with_10_nacl` | `mrs_medium_with_2_5_nacl` | `SALINITY_VARIANT` | NaCl decreased from 100 g/L to 25 g/L. |
| `mrs_medium_with_10_nacl` | `mrs_medium_with_2_5_nacl_ph_9_0` | `SALINITY_VARIANT` | NaCl decreased from 100 g/L to 25 g/L; pH 9.0 specified. |
| `TOGO_M249_MRS_Medium_With_10_NaCl` | `TOGO_M602_MRS_Medium_With_2.5_NaCl` | `SALINITY_VARIANT` | NaCl decreased from 100 g/L to 25 g/L. |
| `TOGO_M249_MRS_Medium_With_10_NaCl` | `TOGO_M977_MRS_Medium_With_2.5_NaCl_pH_9.0` | `SALINITY_VARIANT` | NaCl decreased from 100 g/L to 25 g/L; pH 9.0 specified. |

## Validation

Validation was run after applying the links:

- Targeted schema validation passed for all 6 touched MRS NaCl YAML files.
- `just validate-media-variant-links` scanned 15,827 records and reported
  2,230 parent-to-child links, 2,230 child-to-parent links, 0 errors, and
  0 warnings.

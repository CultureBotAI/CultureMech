# M9 Park Zinc-Grid Variant Review

Date: 2026-05-13

## Scope

Reviewed four MediaDB M9 Park zinc-dose grids:

- Zinc acetate without cysteine:
  - `m9_with_0_67_zinc_acetate_park_et_al`
  - `m9_with_3_35_zinc_acetate_park_et_al`
  - `m9_with_6_03_zinc_acetate_park_et_al`
- Zinc acetate with 0.5 cysteine-HCl:
  - `m9_with_0_67_zinc_acetate_and_05_cysteine_hcl_park_et_al`
  - `m9_with_3_35_zinc_acetate_and_05_cysteine_hcl_park_et_al`
  - `m9_with_6_03_zinc_acetate_and_05_cysteine_hcl_park_et_al`
- Zinc sulfate without cysteine:
  - `m9_with_0_67_zinc_sulfate_park_et_al`
  - `m9_with_3_35_zinc_sulfate_park_et_al`
  - `m9_with_6_03_zinc_sulfate_park_et_al`
- Zinc sulfate with 0.5 cysteine-HCl:
  - `m9_with_0_67_zinc_sulfate_and_05_cysteine_hcl_park_et_al`
  - `m9_with_3_35_zinc_sulfate_and_05_cysteine_hcl_park_et_al`
  - `m9_with_6_03_zinc_sulfate_and_05_cysteine_hcl_park_et_al`

## Decision

Applied `CONCENTRATION_VARIANT` links within each grid from the lowest zinc-dose
record to the two higher zinc-dose records.

Rationale:

- All twelve records are MediaDB records imported from the same reference:
  Mazumdar et al. (2014) PLOS One.
- Within each three-record grid, the parsed ingredient identities and physical
  state match.
- Within each three-record grid, exactly one parsed concentration changes:
  Zinc Acetate or Zinc sulfate.
- The cysteine-containing grids keep cysteine-HCl constant at 3.17219 mM.

## Applied Links

| Parent | Child | Relationship | Modification summary |
|---|---|---|---|
| `m9_with_0_67_zinc_acetate_park_et_al` | `m9_with_3_35_zinc_acetate_park_et_al` | `CONCENTRATION_VARIANT` | Zinc Acetate increased from 30.5239 mM to 152.62 mM. |
| `m9_with_0_67_zinc_acetate_park_et_al` | `m9_with_6_03_zinc_acetate_park_et_al` | `CONCENTRATION_VARIANT` | Zinc Acetate increased from 30.5239 mM to 274.715 mM. |
| `m9_with_0_67_zinc_acetate_and_05_cysteine_hcl_park_et_al` | `m9_with_3_35_zinc_acetate_and_05_cysteine_hcl_park_et_al` | `CONCENTRATION_VARIANT` | Zinc Acetate increased from 30.5239 mM to 152.62 mM; cysteine-HCl unchanged. |
| `m9_with_0_67_zinc_acetate_and_05_cysteine_hcl_park_et_al` | `m9_with_6_03_zinc_acetate_and_05_cysteine_hcl_park_et_al` | `CONCENTRATION_VARIANT` | Zinc Acetate increased from 30.5239 mM to 274.715 mM; cysteine-HCl unchanged. |
| `m9_with_0_67_zinc_sulfate_park_et_al` | `m9_with_3_35_zinc_sulfate_park_et_al` | `CONCENTRATION_VARIANT` | Zinc sulfate increased from 23.3019 mM to 116.51 mM. |
| `m9_with_0_67_zinc_sulfate_park_et_al` | `m9_with_6_03_zinc_sulfate_park_et_al` | `CONCENTRATION_VARIANT` | Zinc sulfate increased from 23.3019 mM to 209.717 mM. |
| `m9_with_0_67_zinc_sulfate_and_05_cysteine_hcl_park_et_al` | `m9_with_3_35_zinc_sulfate_and_05_cysteine_hcl_park_et_al` | `CONCENTRATION_VARIANT` | Zinc sulfate increased from 23.3019 mM to 116.51 mM; cysteine-HCl unchanged. |
| `m9_with_0_67_zinc_sulfate_and_05_cysteine_hcl_park_et_al` | `m9_with_6_03_zinc_sulfate_and_05_cysteine_hcl_park_et_al` | `CONCENTRATION_VARIANT` | Zinc sulfate increased from 23.3019 mM to 209.717 mM; cysteine-HCl unchanged. |

## Validation

Validation was run after applying the links:

- Targeted schema validation passed for all 12 touched M9 Park zinc YAML files.
- `just validate-media-variant-links` scanned 15,827 records and reported
  2,211 parent-to-child links, 2,211 child-to-parent links, 0 errors, and
  0 warnings.

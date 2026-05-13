# 802 NaCl Salinity Grid Variant Review

Date: 2026-05-11

## Decision

Applied parent/child `MediaRecipe` links for the TOGO/NBRC 802 salinity grid.
The records share the same 802 base formulation and vary sodium chloride
concentration across 2%, 3%, 5%, and 10% NaCl.

Applied parent group:

| Parent path | Signature | Children | Relationship |
|---|---|---:|---|
| `data/normalized_yaml/bacterial/802_2_nacl.yaml` | `cf7e86da02e4150a` | 3 | `SALINITY_VARIANT` |

The parent record now contains `variant_children` links. Each child record now
contains `parent_media`, `variant_relationship: SALINITY_VARIANT`, and a
`variant_modifications` note.

## Evidence From Local Records

- Source family: `original_name` values are `802 + 2% NaCl`, `802 + 3% NaCl`,
  `802 + 5% NaCl`, and `802 + 10% NaCl`.
- Source system: `media_term.term.id` values are `TOGO:*`.
- Source notes: records cite TOGO Medium and NBRC source IDs in `notes` and
  `curation_history`.
- Variable dimension: sodium chloride concentration.
- Parent baseline: `802 + 2% NaCl`, represented as 20 g/L NaCl.
- Child NaCl levels: 30 g/L, 50 g/L, and 100 g/L NaCl.

## Validation

- Applied actions: 12
  - `add_variant_child`: 3
  - `add_parent_media`: 3
  - `set_variant_relationship`: 3
  - `add_variant_modification`: 3
- Targeted schema validation: 4/4 touched 802 YAML files passed.
- Parent/child link validation:
  - YAML records scanned: 15,827
  - Parent-to-child links: 1,527
  - Child-to-parent links: 1,527
  - Errors: 0
  - Warnings: 0
- Focused test: `uv run pytest tests/test_media_variant_links.py -q --no-cov`
  passed with 8 tests.
- `git diff --check` passed.

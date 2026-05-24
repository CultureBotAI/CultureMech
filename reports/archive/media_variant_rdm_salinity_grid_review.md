# RDM NaCl Salinity Grid Variant Review

Date: 2026-05-11

## Decision

Applied parent/child `MediaRecipe` links for the MediaDB RDM salinity grid. The
records share the same RDM base formulation and vary sodium chloride
concentration across 10 mM, 20 mM, and 50 mM NaCl.

Applied parent group:

| Parent path | Signature | Children | Relationship |
|---|---|---:|---|
| `data/normalized_yaml/bacterial/rdm_10_mm_nacl.yaml` | `4dec2a88209ec06e` | 2 | `SALINITY_VARIANT` |

The parent record now contains `variant_children` links. Each child record now
contains `parent_media`, `variant_relationship: SALINITY_VARIANT`, and a
`variant_modifications` note.

## Evidence From Local Records

- Source family: `original_name` values are `RDM - 10 mM NaCl`, `RDM - 20 mM
  NaCl`, and `RDM - 50 mM NaCl`.
- Source system: `media_term.term.id` values are `MEDIADB:*`.
- Source notes: records cite MediaDB and Mazumdar et al. (2014) PLOS One in
  `curation_history`.
- Variable dimension: sodium chloride concentration.
- Parent baseline: `RDM - 10 mM NaCl`, represented as 10.0 mM sodium chloride.
- Child NaCl levels: 20.0 mM and 50.0 mM sodium chloride.

## Validation

- Applied actions: 8
  - `add_variant_child`: 2
  - `add_parent_media`: 2
  - `set_variant_relationship`: 2
  - `add_variant_modification`: 2
- Targeted schema validation: 3/3 touched RDM YAML files passed.
- Parent/child link validation:
  - YAML records scanned: 15,827
  - Parent-to-child links: 1,529
  - Child-to-parent links: 1,529
  - Errors: 0
  - Warnings: 0
- Focused test: `uv run pytest tests/test_media_variant_links.py -q --no-cov`
  passed with 8 tests.
- `git diff --check` passed.

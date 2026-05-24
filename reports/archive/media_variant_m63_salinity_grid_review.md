# Modified M63 Salinity Grid Variant Review

Date: 2026-05-11

## Decision

Applied parent/child `MediaRecipe` links for three modified M63 salinity grids
from MediaDB. Each group has a shared compatible-solute/carbon-source dimension
and varies sodium chloride concentration across 0.6 M, 0.75 M, 1.5 M, and
2.5 M.

Applied parent groups:

| Parent path | Signature | Children | Relationship |
|---|---|---:|---|
| `data/normalized_yaml/bacterial/modified_m63_medium_with_ectoine_and_0_6_m_nacl.yaml` | `42d068b346bbb298` | 3 | `SALINITY_VARIANT` |
| `data/normalized_yaml/bacterial/modified_m63_medium_with_glucose_and_0_6_m_nacl.yaml` | `abfd3d312a99ff4e` | 3 | `SALINITY_VARIANT` |
| `data/normalized_yaml/bacterial/modified_m63_medium_with_hydroxyectoine_and_0_6_m_nacl.yaml` | `0db83e9ece8944f6` | 3 | `SALINITY_VARIANT` |

The parent records now contain `variant_children` links. Each child record now
contains `parent_media`, `variant_relationship: SALINITY_VARIANT`, and a
`variant_modifications` note.

## Evidence From Local Records

- Source family: all records are modified M63 media.
- Source system: `media_term.term.id` values are `MEDIADB:*`.
- Source notes: records cite MediaDB and Mazumdar et al. (2014) PLOS One in
  `curation_history`.
- Variable dimension: sodium chloride concentration.
- Parent baseline for each group: 0.6 M NaCl, represented as 600.0 mM sodium
  chloride in the ingredient list.
- Child NaCl levels: 0.75 M, 1.5 M, and 2.5 M, represented as 750.0 mM,
  1500.0 mM, and 2500.0 mM sodium chloride.

## Validation

- Applied actions: 36
  - `add_variant_child`: 9
  - `add_parent_media`: 9
  - `set_variant_relationship`: 9
  - `add_variant_modification`: 9
- Targeted schema validation: 12/12 touched M63 YAML files passed.
- Parent/child link validation:
  - YAML records scanned: 15,827
  - Parent-to-child links: 1,524
  - Child-to-parent links: 1,524
  - Errors: 0
  - Warnings: 0
- Focused test: `uv run pytest tests/test_media_variant_links.py -q --no-cov`
  passed with 8 tests.
- `git diff --check` passed.

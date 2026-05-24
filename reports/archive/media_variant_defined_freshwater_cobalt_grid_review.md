# Defined Freshwater Cobalt Grid Variant Review

Date: 2026-05-11

## Decision

Applied parent/child `MediaRecipe` links for two MediaDB defined freshwater
medium cobalt-source grids. The records share a recognizable defined
freshwater base formulation within each cobalt salt family and vary only
concentration levels for acetate and/or ferric oxide.

Applied parent groups:

| Parent path | Signature | Children | Relationship |
|---|---|---:|---|
| `data/normalized_yaml/bacterial/MEDIADB_416_Defined_freshwater_medium_CoSO4.yaml` | `d886f172259919ee` | 3 | `CONCENTRATION_VARIANT` |
| `data/normalized_yaml/bacterial/MEDIADB_444_Defined_freshwater_medium_CoCl2.yaml` | `5a3514d1623cfe0a` | 3 | `CONCENTRATION_VARIANT` |

The parent records now contain `variant_children` links. Each child record now
contains `parent_media`, `variant_relationship: CONCENTRATION_VARIANT`, and a
`variant_modifications` note.

## Evidence From Local Records

- Source family: `original_name` values are `'Defined freshwater medium
  (CoSO4` and `'Defined freshwater medium (CoCl2`.
- Source system: `media_term.term.id` values are `MEDIADB:416`,
  `MEDIADB:417`, `MEDIADB:423`, `MEDIADB:424`, `MEDIADB:444`,
  `MEDIADB:447`, `MEDIADB:451`, and `MEDIADB:455`.
- Source notes: all eight records cite MediaDB, Institute for Systems Biology,
  and `https://mediadb.systemsbiology.net/` in `curation_history`.
- CoSO4 grid:
  - parent `MEDIADB:416`: acetate 113.2 mM, ferric oxide 100.0 mM,
    cobaltous sulfate 0.006494 mM
  - child `MEDIADB:417`: acetate 113.2 mM, ferric oxide 250.0 mM,
    cobaltous sulfate 0.006494 mM
  - child `MEDIADB:423`: acetate 10.0 mM, ferric oxide 100.0 mM,
    cobaltous sulfate 0.006494 mM
  - child `MEDIADB:424`: acetate 50.0 mM, ferric oxide 100.0 mM,
    cobaltous sulfate 0.006494 mM
- CoCl2 grid:
  - parent `MEDIADB:444`: acetate 113.2 mM, ferric oxide 100.0 mM,
    cobalt chloride 0.007702 mM
  - child `MEDIADB:447`: acetate 113.2 mM, ferric oxide 250.0 mM,
    cobalt chloride 0.007702 mM
  - child `MEDIADB:451`: acetate 50.0 mM, ferric oxide 100.0 mM,
    cobalt chloride 0.007702 mM
  - child `MEDIADB:455`: acetate 10.0 mM, ferric oxide 100.0 mM,
    cobalt chloride 0.007702 mM

## Validation

- Applied actions: 24
  - `add_variant_child`: 6
  - `add_parent_media`: 6
  - `set_variant_relationship`: 6
  - `add_variant_modification`: 6
- Targeted schema validation: 8/8 touched MediaDB cobalt-grid YAML files
  passed.
- Parent/child link validation:
  - YAML records scanned: 15,827
  - Parent-to-child links: 1,535
  - Child-to-parent links: 1,535
  - Errors: 0
  - Warnings: 0
- Focused test: `uv run pytest tests/test_media_variant_links.py -q --no-cov`
  passed with 8 tests.
- Lint: `uv run ruff check scripts/apply_media_variant_links.py
  scripts/propose_media_variant_links.py tests/test_media_variant_links.py`
  passed.
- `git diff --check` passed after updating the apply-plan TSV writer to emit
  LF line endings.

# XED Agar Variant Review

Date: 2026-05-13

## Decision

Applied parent/child `MediaRecipe` links for the XED Agar concentration
variant family. The records share the same xylan, yeast extract, and agar base
medium, with agar concentration as the observed formulation difference.

Applied parent group:

| Parent path | Signature | Children | Relationship |
|---|---|---:|---|
| `data/normalized_yaml/bacterial/JCM_J581_XED_AGAR.yaml` | `2b26a51f391142ee` | 2 | `CONCENTRATION_VARIANT` |

The parent record now contains `variant_children` links. Each child record now
contains `parent_media`, `variant_relationship: CONCENTRATION_VARIANT`, and a
`variant_modifications` note.

## Evidence From Local Records

- Parent source: JCM Medium J581, `XED AGAR`, with 7 g/L xylan, 3 g/L yeast
  extract, 20 g/L agar, and pH 7.0.
- Child source: KOMODO Medium 1026, `XED-AGAR`, enriched from DSMZ Medium
  1026, with 7 g/L xylan, 3 g/L yeast extract, 18 g/L agar, and pH 7.0.
- Child source: DSMZ Medium 1026, `XED-AGAR`, with 7 g/L xylan, 3 g/L yeast
  extract, 18 g/L agar, and pH 7.0.
- Source notes: records cite JCM, KOMODO/DSMZ, or DSMZ in `media_term`,
  `notes`, and `curation_history`.

## Validation

- Applied actions: 8
  - `add_variant_child`: 2
  - `add_parent_media`: 2
  - `set_variant_relationship`: 2
  - `add_variant_modification`: 2
- Targeted schema validation: 3/3 touched XED Agar YAML files passed.
- Parent/child link validation:
  - YAML records scanned: 15,827
  - Parent-to-child links: 1,541
  - Child-to-parent links: 1,541
  - Errors: 0
  - Warnings: 0
- Focused test: `uv run pytest tests/test_media_variant_links.py -q --no-cov`
  passed with 8 tests.
- Lint: `uv run ruff check scripts/apply_media_variant_links.py
  scripts/validate_media_variant_links.py tests/test_media_variant_links.py`
  passed.

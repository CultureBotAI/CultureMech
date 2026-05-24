# TCG Medium Variant Review

Date: 2026-05-13

## Decision

Applied parent/child `MediaRecipe` links for the TCG medium concentration
variant family. The records share the same tryptone, casitone, glucose, sea
water, and agar base medium, with agar concentration as the observed
formulation difference.

Applied parent group:

| Parent path | Signature | Children | Relationship |
|---|---|---:|---|
| `data/normalized_yaml/bacterial/JCM_J720_TCG_MEDIUM.yaml` | `3ce61b2bc10aaf9a` | 2 | `CONCENTRATION_VARIANT` |

The parent record now contains `variant_children` links. Each child record now
contains `parent_media`, `variant_relationship: CONCENTRATION_VARIANT`, and a
`variant_modifications` note.

## Evidence From Local Records

- Parent source: JCM Medium J720, `TCG MEDIUM`, with 3 g/L tryptone, 5 g/L
  casitone, 4 g/L glucose, 1000 g/L sea water, and 15 g/L agar.
- Child source: KOMODO Medium 1009, `TCG medium`, enriched from DSMZ Medium
  1009, with the same non-agar components and 20 g/L agar.
- Child source: DSMZ Medium 1009, `TCG MEDIUM`, with the same non-agar
  components and 20 g/L agar. The preparation note specifies artificial
  seawater.
- Source notes: records cite JCM, KOMODO/DSMZ, or DSMZ in `media_term`,
  `notes`, and `curation_history`.

## Validation

- Applied actions: 8
  - `add_variant_child`: 2
  - `add_parent_media`: 2
  - `set_variant_relationship`: 2
  - `add_variant_modification`: 2
- Targeted schema validation: 3/3 touched TCG medium YAML files passed.
- Parent/child link validation:
  - YAML records scanned: 15,827
  - Parent-to-child links: 1,543
  - Child-to-parent links: 1,543
  - Errors: 0
  - Warnings: 0
- Focused test: `uv run pytest tests/test_media_variant_links.py -q --no-cov`
  passed with 8 tests.
- Lint: `uv run ruff check scripts/apply_media_variant_links.py
  scripts/validate_media_variant_links.py tests/test_media_variant_links.py`
  passed.

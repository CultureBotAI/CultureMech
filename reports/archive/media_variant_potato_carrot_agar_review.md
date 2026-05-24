# Potato-Carrot Agar Variant Review

Date: 2026-05-11

## Decision

Applied parent/child `MediaRecipe` links for the Potato-Carrot Agar
concentration-variant family. The records share a recognizable potato, carrot,
and agar base medium, while potato, carrot, and/or agar concentrations vary.

Applied parent group:

| Parent path | Signature | Children | Relationship |
|---|---|---:|---|
| `data/normalized_yaml/bacterial/JCM_J54_POTATO-CARROT_AGAR.yaml` | `80268265dbacd17d` | 2 | `CONCENTRATION_VARIANT` |

The parent record now contains `variant_children` links. Each child record now
contains `parent_media`, `variant_relationship: CONCENTRATION_VARIANT`, and a
`variant_modifications` note.

## Evidence From Local Records

- Parent source: JCM Medium J54, `POTATO-CARROT AGAR`, with 300 g/L potato,
  25 g/L carrot, and 15 g/L agar.
- Child source: JCM Medium J55, `1/10 POTATO-CARROT AGAR`, with 30 g/L potato,
  2.5 g/L carrot, and 15 g/L agar. The preparation note points to Medium No.
  54.
- Child source: DSMZ Medium 1765, `Potato Carrot Agar`, with 150 g/L potato,
  30 g/L carrot, and 20 g/L agar.
- Source notes: records cite JCM or DSMZ in `curation_history` and
  `media_term`; the JCM records also include JCM source URLs.

## Validation

- Applied actions: 8
  - `add_variant_child`: 2
  - `add_parent_media`: 2
  - `set_variant_relationship`: 2
  - `add_variant_modification`: 2
- Targeted schema validation: 3/3 touched Potato-Carrot Agar YAML files
  passed.
- Parent/child link validation:
  - YAML records scanned: 15,827
  - Parent-to-child links: 1,537
  - Child-to-parent links: 1,537
  - Errors: 0
  - Warnings: 0
- Focused test: `uv run pytest tests/test_media_variant_links.py -q --no-cov`
  passed with 8 tests.
- `git diff --check` passed.

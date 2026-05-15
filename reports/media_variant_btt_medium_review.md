# BTT Medium Variant Review

Date: 2026-05-13

## Decision

Applied parent/child `MediaRecipe` links for the BTT medium concentration
variant family. The records share the same glucose, yeast extract, meat
extract, casitone, and agar base medium. The main formulation difference is
agar concentration, with a minor pH-range difference between the JCM parent and
DSMZ/KOMODO children.

Applied parent group:

| Parent path | Signature | Children | Relationship |
|---|---|---:|---|
| `data/normalized_yaml/bacterial/JCM_J1178_BTT_MEDIUM.yaml` | `f16eefbb7fe8c11d` | 2 | `CONCENTRATION_VARIANT` |

The parent record now contains `variant_children` links. Each child record now
contains `parent_media`, `variant_relationship: CONCENTRATION_VARIANT`, and a
`variant_modifications` note.

## Evidence From Local Records

- Parent source: JCM Medium J1178, `BTT MEDIUM`, with 10 g/L glucose, 1 g/L
  yeast extract, 1 g/L meat extract, 2 g/L casitone, 15 g/L agar, and pH 5.5.
- Child source: KOMODO Medium 1109, `BTT medium`, enriched from DSMZ Medium
  1109, with the same non-agar components and 20 g/L agar; pH range 5.5-6.0.
- Child source: DSMZ Medium 1109, `BTT MEDIUM`, with the same non-agar
  components and 20 g/L agar; pH range 5.5-6.0 and an optional MES buffer note.
- Source notes: records cite JCM, KOMODO/DSMZ, or DSMZ in `media_term`,
  `notes`, and `curation_history`.

## Validation

- Applied actions: 8
  - `add_variant_child`: 2
  - `add_parent_media`: 2
  - `set_variant_relationship`: 2
  - `add_variant_modification`: 2
- Targeted schema validation: 3/3 touched BTT medium YAML files passed.
- Parent/child link validation:
  - YAML records scanned: 15,827
  - Parent-to-child links: 1,539
  - Child-to-parent links: 1,539
  - Errors: 0
  - Warnings: 0
- Focused test: `uv run pytest tests/test_media_variant_links.py -q --no-cov`
  passed with 8 tests.
- Lint: `uv run ruff check scripts/apply_media_variant_links.py
  scripts/validate_media_variant_links.py tests/test_media_variant_links.py`
  passed.
- `git diff --check` passed after updating both media-variant TSV writers to
  emit LF line endings.

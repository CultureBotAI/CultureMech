# Zahorchak ATP/Mg2+ Media Variant Review

Date: 2026-05-11

## Decision

Applied parent/child `MediaRecipe` links for the Zahorchak et al. concentration
grid records from MediaDB. These records are a bounded, source-named family with
explicit concentration changes in the medium names and shared formulation
structure.

Two parent groups were applied:

| Parent path | Signature | Children | Relationship |
|---|---|---:|---|
| `data/normalized_yaml/bacterial/zahorchak_et_al_medium_10_mm_exogenous_atp_10_mm_mg_2.yaml` | `a451d0b41bb50a0d` | 24 | `CONCENTRATION_VARIANT` |
| `data/normalized_yaml/bacterial/zahorchak_et_al_medium_no_exogenous_atp_10_mm_mg_2.yaml` | `812c7a4f12d1fe82` | 4 | `CONCENTRATION_VARIANT` |

The parent records now contain `variant_children` links. Each child record now
contains `parent_media`, `variant_relationship: CONCENTRATION_VARIANT`, and a
`variant_modifications` note.

## Evidence From Local Records

- Source family: `original_name` values all start with `Zahorchak et al medium`.
- Source system: `media_term.term.id` values are `MEDIADB:*`.
- Source notes: records cite MediaDB and Mazumdar et al. (2014) PLOS One in
  `curation_history`.
- Variable dimensions:
  - exogenous ATP concentration: no exogenous ATP, 1.25 mM, 2.5 mM, 5.0 mM,
    10 mM, or 20 mM
  - Mg2+ concentration: 1.25 mM, 2.5 mM, 5.0 mM, 10 mM, or 20 mM

## Validation

- Applied actions: 112
  - `add_variant_child`: 28
  - `add_parent_media`: 28
  - `set_variant_relationship`: 28
  - `add_variant_modification`: 28
- Targeted schema validation: 30/30 touched Zahorchak YAML files passed.
- Parent/child link validation:
  - YAML records scanned: 15,827
  - Parent-to-child links: 1,515
  - Child-to-parent links: 1,515
  - Errors: 0
  - Warnings: 0
- Focused test: `uv run pytest tests/test_media_variant_links.py -q --no-cov`
  passed with 8 tests.
- `git diff --check` passed.

## Ingredient Caveat

The exogenous-ATP records have a first ingredient entry with an empty
`preferred_term` and a millimolar concentration. The surrounding
`original_name` identifies that dimension as exogenous ATP, and local reference
data maps ATP to `CHEBI:15422`, but this pass did not rewrite ingredient
identity fields. That should be handled as a separate ingredient-normalization
batch so the content manifest and variant proposals can be regenerated
consistently afterward.

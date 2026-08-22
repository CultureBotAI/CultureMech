# CultureMech repository guidance

Use this file as the repository-level contract. Detailed workflows live in
`.claude/skills/*/SKILL.md`; follow the relevant skill rather than duplicating
its procedure here.

## Data authority

- `data/raw/`: immutable upstream captures. Large payloads are ignored; source
  README files are tracked.
- `data/raw_yaml/`: mechanical, reproducible conversion output. Do not curate.
- `data/normalized_yaml/`: authoritative, version-controlled recipe corpus.
- `data/merge_yaml/merged/`: derived canonical merges. Regenerate; do not edit
  instead of fixing normalized inputs or merge rules.
- `src/culturemech/schema/culturemech.yaml`: authoritative schema. Generated
  dataclasses and schema documentation must change in the same commit.
- `app/data.js`, `pages/normalized/`, `pages/media/`, and generated page assets
  are ignored CI outputs. Never hand-edit or commit them; see
  `docs/DATA_LAYERS.md`.

## Required validation

Choose checks by changed surface:

- Python: `just test-fast` when available, otherwise targeted `uv run pytest ...`;
  run the full `just test` for cross-cutting changes.
- One recipe: `just validate path/to/recipe.yaml` plus relevant semantic checks.
- Corpus or schema: `just validate-strict`, `just assign-ids-check`, and
  `just validate-products`. Regenerate schema-derived files after schema edits.
- Merge inputs/rules: `just verify-merges` and `just audit-merge-freshness`.
- Renderer/browser: renderer tests plus `python -m culturemech.web_artifacts`
  after generating browser data and normalized pages.

`just validate-all` aggregates open-schema LinkML failures; `validate-strict`
is the closed-schema corpus gate and rejects unknown fields.

## Recipe and schema editing rules

- IDs are permanent. Never reuse, renumber, or hand-pick an apparently free ID.
  Run `just assign-ids-check`; use `just assign-ids --dry-run` before applying
  assignments, then refresh the registry with `just refresh-id-registry`.
- `curation_history` is append-only. Add a dated event describing the evidence
  and exact change; do not rewrite or delete earlier events.
- Preserve YAML presentation. Use the repository round-trip helpers/ruamel.yaml,
  modify only intended nodes, and review the diff for whole-file reflow.
- Bulk mutators default to preview. Support `--dry-run`; require an explicit
  apply action, summarize changed/skipped/failed records, and fail nonzero on
  partial output.
- Do not invent ontology IDs, labels, citations, or evidence. Verify ID/label
  correspondence and preserve primary-source provenance. Keep unresolved
  values explicit rather than forcing a plausible grounding.

## External dependencies

`culturebotai-claw` supplies shared browser/QC helpers. Configure it through
`PYTHONPATH` when composition graphs or the QC dashboard are required. The page
renderer may run without it only in an explicit degraded mode: it warns and
publishes a visible notice. External data and embedding paths come from recipe
arguments or `CMM_AUTOMATION_DATA_DIR`, `MICROBE_MEDIA_PARAM_DIR`, and
`KG_MICROBE_EMBEDDINGS`; never commit workstation paths.

## Skill routing

- New records/IDs: `create-recipe`, then `manage-identifiers`.
- Recipe QA: `review-recipes`; broad schema/pipeline audits:
  `audit-schema-gaps`; quick diagnosis: `schema-gap-analysis`.
- Sources: `fetch-source` or `scrape-jcm-media`.
- Grounding: `id-label-correspondence`, `match-kg-microbe`, and
  `manage-ingredient-hierarchy`.
- Research: `deep-research-medium` and `research-ingredient-roles`.
- Visualization: `generate-ingredient-umap` and `render-media-role-graph`.
- Reporting/backlog: `stats-report` and `next-tasks`.

Run `uv run python scripts/validate_claude_skills.py` after changing a skill.

## Claude permissions and hooks

Keep `.claude/settings.local.json` untracked and narrowly task-scoped. Start
from `.claude/settings.example.json`; do not grant wildcard `uv run`, package
uninstallation, `sudo`, repository creation, or broad shell access.

Coordination hooks are intentionally disabled when
`KG_MICROBE_ORCHESTRATION_ROOT` is unset. When set, the checker and status
directory are required; lock-check errors fail closed. See `.claude/hooks/README.md`.

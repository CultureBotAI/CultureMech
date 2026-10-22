# CultureMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `culturemech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/CultureMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
- task_id: culturemech-infra-0001
  summary: Extend batch_review_recipes.py solution validation for P3.1 placeholders and chebi_term coverage
  status: resolved
  issue_url: https://github.com/CultureBotAI/CultureMech/issues/633
  disposition: Resolved in PR #632 (commit 377d68c67960b43fe622c68f28e25f4194e4420e) by adding P3.1 placeholder checks and chebi_term/preferred_term placeholder coverage to _validate_solution() with unit tests in tests/test_batch_review_recipes.py.
```
<!-- mech-infra-tasks:end -->

## Tasks

### `culturemech-infra-0001` — Extend `batch_review_recipes.py` solution validation for P3.1 placeholders and `chebi_term` coverage

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019`, cycle `1`, stage `4` (`record_review`)
- **Issue**: https://github.com/CultureBotAI/CultureMech/issues/633
- **Status**: `resolved`
- **Observation**: During Stage 4 adversarial review, `scripts/batch_review_recipes.py` (`_validate_solution()`) omitted P3.1 placeholder detection for `data/normalized_yaml/solutions/` records and only scanned `preferred_term` in `_validate_recipe()`, missing placeholder text inside nested `chebi_term` mappings.
- **Desired outcome**: Symmetrize placeholder detection across both media recipes and stock solutions, covering `preferred_term` and `chebi_term.{id,label,preferred_term}` with regression tests.
- **Evidence paths**:
  - `scripts/batch_review_recipes.py`
  - `tests/test_batch_review_recipes.py`
  - `reviews/structured/20261017/batch_review_recipes_all.json`
- **Disposition**: Resolved in PR #632 (`377d68c67960b43fe622c68f28e25f4194e4420e`); verified via `uv run pytest tests/test_batch_review_recipes.py`.


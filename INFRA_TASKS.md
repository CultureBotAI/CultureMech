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
- task_id: culturemech-infra-0002
  summary: Define Stage 2 (causal_graphs) native schema class/slot, validator targets, maintained writer, KGX causal-edge exporter, and curation skill (or reclassify stage scope)
  status: open
  issue_url: https://github.com/CultureBotAI/CultureMech/issues/658
  disposition: Open prerequisite for Stage 2 (causal_graphs); assessed in reviews/structured/20261023T073000Z-cycle2-stage2-stage3-prerequisite-assessment/review.yaml and queued for Stage 6 (infra_implementation) or parent workflow scope reclassification.
- task_id: culturemech-infra-0003
  summary: Define Stage 3 (protein_examples) UniProtKB prefix, typed ProteinExample schema class, OAK/id-label validator configuration, reference cofactor ChEBI cleanup, writer, KGX exporter, and curation skill
  status: open
  issue_url: https://github.com/CultureBotAI/CultureMech/issues/659
  disposition: Open prerequisite for Stage 3 (protein_examples); assessed in reviews/structured/20261023T073000Z-cycle2-stage2-stage3-prerequisite-assessment/review.yaml and queued for Stage 6 (infra_implementation).
- task_id: culturemech-infra-0004
  summary: Coordinate Cycle 2 blocked-stage advancement past Stages 2-3 and between-cycle profile reload migration under reload_profile_between_cycles_only
  status: deferred
  issue_url: https://github.com/CultureBotAI/CultureMech/issues/660
  disposition: Blocked on external session coordinator advancement for active Cycle 2 (goal-4672) and on completion of culturemech-infra-0002 (#658) and culturemech-infra-0003 (#659) before between-cycle profile reload in Cycle 3+.
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

### `culturemech-infra-0002` — Define Stage 2 (`causal_graphs`) native schema, validator, writer, KGX exporter, and curation skill prerequisites

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019`, cycle `2`, stage `2` prerequisite assessment (`goal-4672`)
- **Issue**: https://github.com/CultureBotAI/CultureMech/issues/658
- **Status**: `open`
- **Priority**: `P1` (blocking prerequisite for Stage 2 `causal_graphs`)
- **Dependencies**: Parent Mech / KG-Microbe domain boundary decision on whether growth-media recipes carry directed causal mechanism edges or remain composition/role-only.
- **Observation**: CultureMech natively represents media compositions, stock solutions, preparation steps, sterilization, organism growth metrics, perturbations (`3/15,915` records), strain modifications (`2/15,915`), nutrient overrides (`2/15,915`), and three-facet ingredient roles (`nutritional_roles` in `217`, `physicochemical_roles` in `249`, `cellular_metabolic_roles` in `5`), rendered as bipartite Mermaid composition/role diagrams by `scripts/render_media_role_graph.py` and exported as 10 composition/growth/attribute edge shapes by `src/culturemech/export/kgx_export.py`. Across all `15,915` normalized YAML records and git-ignored directories (`data/merge_yaml/merged/`, `data/curation/`, `data/reference/`, `workspace/`, `tmp/`), no native `CausalEdge` / `MechanismGraph` schema class or `MediaRecipe` slot, causal-edge writer, KGX causal-predicate exporter, or `.claude/skills/` causal-graph curation skill exists (`mech_shared.yaml` mentions `causal_graphs#edge_x` only in the shared `Discussion.attaches_to` docstring, and `scripts/repair_top_causal_graph_score15.py` only curates composition/roles/preparation).
- **Desired outcome**: Either (A) implement a typed `CausalEdge` class (with ontology-grounded subject/object, constrained causal predicate enum, organism/condition context, and mandatory claim-scoped `EvidenceItem`), `conf/id_label_targets.yaml` validation rules, a `curation_history`-appending writer, KGX causal-edge export in `src/culturemech/export/kgx_export.py`, unit tests, and a `.claude/skills/` curation skill, **or** (B) formally reclassify Stage 2 as `not_applicable` for composition-centric growth-media repositories in the parent workflow contract.
- **Evidence paths**:
  - `src/culturemech/schema/culturemech.yaml`
  - `src/culturemech/schema/mim_roles.yaml`
  - `src/culturemech/schema/mech_shared.yaml`
  - `src/culturemech/export/kgx_export.py`
  - `scripts/render_media_role_graph.py`
  - `scripts/repair_top_causal_graph_score15.py`
  - `workflow/mech-workflow.yaml`
  - `reviews/structured/20261023T073000Z-cycle2-stage2-stage3-prerequisite-assessment/review.yaml`
- **Disposition**: Open prerequisite tracked in https://github.com/CultureBotAI/CultureMech/issues/658 for Stage 6 (`infra_implementation`) execution.

### `culturemech-infra-0003` — Define Stage 3 (`protein_examples`) `UniProtKB` prefix, typed `ProteinExample` schema class, OAK/id-label validator configuration, writer, and skill prerequisites

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019`, cycle `2`, stage `2` prerequisite assessment (`goal-4672`)
- **Issue**: https://github.com/CultureBotAI/CultureMech/issues/659
- **Status**: `open`
- **Priority**: `P1` (blocking prerequisite for Stage 3 `protein_examples`)
- **Dependencies**: None for schema/validator/writer implementation; required before `workflow/mech-workflow.yaml` Stage 3 can transition from `blocked` to `applicable`.
- **Observation**: `src/culturemech/schema/culturemech.yaml` declares 15 prefixes without `UniProt` or `UniProtKB` and defines only untyped `range: string` slots (`CofactorDescriptor.enzyme_examples`, `CofactorDescriptor.biosynthesis_genes`, `CofactorRequirement.genes`, `TransporterAnnotation.genes`, `StrainModification.genes_affected`), with `0` populated cofactor/transporter/enzyme instances across `15,915` normalized records. `data/reference/cofactors.yaml` (48 entries from `src/culturemech/import/import_cofactors.py`) stores only generic enzyme family names in `enzyme_examples` with `0` UniProt accessions, `0` `NCBITaxon` bindings, and a duplicate `CHEBI:60052` mapping across `heme C` and `heme d1`; `docs/ENRICHMENT_GUIDE.md` also references a non-existent `Nitrate_Mineral_Salts_Medium_(NMS)_ENRICHED_EXAMPLE.yaml`. Furthermore, `conf/oak_config.yaml` and `conf/id_label_targets.yaml` have no `UniProtKB` adapter/prefix handling, `src/culturemech/export/kgx_export.py` emits no protein nodes/edges, and no repository-local protein-example curation skill exists.
- **Desired outcome**: Add `UniProtKB` prefix, `UniProtTerm` (validated accession pattern + canonical protein label), and `ProteinExample` class (binding `uniprot_term`, explicit `NCBITaxonTerm` organism, optional gene/EC/isoform scope, and mandatory claim-scoped `EvidenceItem`) to `src/culturemech/schema/culturemech.yaml`; configure `conf/id_label_targets.yaml` and `scripts/validate_strict.py`; fix `data/reference/cofactors.yaml` ChEBI collisions and `docs/ENRICHMENT_GUIDE.md` example path; add a `curation_history`-appending writer, KGX protein export, unit tests, and a `.claude/skills/` protein-example curation skill.
- **Evidence paths**:
  - `src/culturemech/schema/culturemech.yaml`
  - `conf/id_label_targets.yaml`
  - `conf/oak_config.yaml`
  - `data/reference/cofactors.yaml`
  - `src/culturemech/import/import_cofactors.py`
  - `src/culturemech/export/kgx_export.py`
  - `docs/ENRICHMENT_GUIDE.md`
  - `workflow/mech-workflow.yaml`
  - `reviews/structured/20261023T073000Z-cycle2-stage2-stage3-prerequisite-assessment/review.yaml`
- **Disposition**: Open prerequisite tracked in https://github.com/CultureBotAI/CultureMech/issues/659 for Stage 6 (`infra_implementation`) execution.

### `culturemech-infra-0004` — Coordinate Cycle 2 blocked-stage advancement and between-cycle profile reload migration

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019`, cycle `2`, stage `2` prerequisite assessment (`goal-4672`)
- **Issue**: https://github.com/CultureBotAI/CultureMech/issues/660
- **Status**: `deferred`
- **Priority**: `P1` (active cycle coordination blocker)
- **Dependencies**: External session coordinator (`culturebotai-claw` / `kg_microbe_progress`) for active Cycle 2 stage advancement; `culturemech-infra-0002` (#658) and `culturemech-infra-0003` (#659) for next-cycle profile unblocking.
- **Observation**: In `mech-goal-sequence-20261019`, Cycle 2 pinned `effective-workflow.json` (`workflow_sha256: 22e8c558fe158db19d847bc478901422f5697a48760bb6a9d852de8254ae4071`) with Stages 2 (`causal_graphs`) and 3 (`protein_examples`) set to `applicability: "blocked"` and `skill_paths: []` under `cycle_policy.reload_profile_between_cycles_only: true`. Candidate edits in `workflow/mech-workflow.yaml` take effect only at the next cycle boundary (`next_profile_path`) and cannot mutate or unblock active Cycle 2 (`status.json` `goal-4672`, `phase: "blocked"`, `stage: 2`).
- **Desired outcome**: Preserve coordinator runtime state integrity (`effective-workflow.json`, `status.json`, `completion.json` untouched by repository agent); have the external coordinator advance active Cycle 2 past blocked Stages 2 and 3 to Stage 4 (`record_review`) using the verified prerequisite assessment (`20261023T073000Z-cycle2-stage2-stage3-prerequisite-assessment`), and reload `workflow/mech-workflow.yaml` at a subsequent cycle boundary only after `culturemech-infra-0002` and `culturemech-infra-0003` are implemented and validated at Stage 6 (`infra_implementation`).
- **Evidence paths**:
  - `workflow/mech-workflow.yaml`
  - `workflow/parent/mech-cycle.yaml`
  - `reviews/structured/20261023T073000Z-cycle2-stage2-stage3-prerequisite-assessment/review.yaml`
- **Disposition**: Deferred on external coordinator advancement for active Cycle 2 and on Stage 6 implementation of `culturemech-infra-0002` (#658) and `culturemech-infra-0003` (#659); tracked in https://github.com/CultureBotAI/CultureMech/issues/660.

## Cycle 2 Stage 2–3 Prerequisite Dependency, Acceptance & Validation Plan

| Step | Task ID / Issue | Layer | Scope & Owner Paths | Depends On | Acceptance Criteria & Validation Commands |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Stage 2 Domain & Schema Prerequisite** | `culturemech-infra-0002` ([#658](https://github.com/CultureBotAI/CultureMech/issues/658)) | Schema & Workflow Contract | `src/culturemech/schema/culturemech.yaml` (define `CausalEdge` with typed `subject`, causal `predicate` enum, typed `object`, `organism_context`, and claim-scoped `EvidenceItem`) or parent `workflow/parent/mech-cycle.yaml` scope decision | None | `.venv/bin/python scripts/audit_schema.py` exits `0` with `0` ungrounded `range: string` causal fields; `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` exits `0`. |
| **2. Stage 3 Typed UniProt Schema & Reference Cleanup** | `culturemech-infra-0003` ([#659](https://github.com/CultureBotAI/CultureMech/issues/659)) | Schema & Reference Data | `src/culturemech/schema/culturemech.yaml` (`UniProtKB` prefix, `UniProtTerm`, `ProteinExample` binding `uniprot_term` + `NCBITaxonTerm` + `EvidenceItem`), `src/culturemech/import/import_cofactors.py`, `data/reference/cofactors.yaml`, `docs/ENRICHMENT_GUIDE.md` | None | `.venv/bin/python scripts/audit_schema.py` exits `0`; duplicate `CHEBI:60052` in `data/reference/cofactors.yaml` is resolved; `docs/ENRICHMENT_GUIDE.md` references existing records in `data/normalized_yaml/`. |
| **3. Validator & ID-Label Correspondence Configuration** | `culturemech-infra-0002` ([#658](https://github.com/CultureBotAI/CultureMech/issues/658)), `culturemech-infra-0003` ([#659](https://github.com/CultureBotAI/CultureMech/issues/659)) | Validation | `conf/id_label_targets.yaml`, `conf/oak_config.yaml`, `scripts/validate_id_label.py`, `scripts/validate_strict.py` | Steps 1–2 | `.venv/bin/python scripts/validate_id_label.py` and `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` validate `CausalEdge` and `ProteinExample` fixtures with `0` `UNKNOWN_PREFIX` or missing-snippet errors. |
| **4. Maintained Writers & KGX Export** | `culturemech-infra-0002` ([#658](https://github.com/CultureBotAI/CultureMech/issues/658)), `culturemech-infra-0003` ([#659](https://github.com/CultureBotAI/CultureMech/issues/659)) | Writers & Exporters | `scripts/` (authoritative `data/normalized_yaml/` writers only; never write directly to `data/merge_yaml/merged/`, `app/`, `pages/`, or `output/`), `src/culturemech/export/kgx_export.py` | Steps 1–3 | `.venv/bin/python scripts/audit_writers.py` confirms `100%` of recipe writers append `curation_history` and validate before write; `.venv/bin/pytest tests/` passes unit tests for KGX causal-edge and `biolink:Protein` emission. |
| **5. Repository-Local Skills & Next-Cycle Profile Update** | `culturemech-infra-0002` ([#658](https://github.com/CultureBotAI/CultureMech/issues/658)), `culturemech-infra-0003` ([#659](https://github.com/CultureBotAI/CultureMech/issues/659)) | Skills & Workflow Profile | `.claude/skills/`, `.agents/skills/`, `workflow/mech-workflow.yaml`, `tests/` | Steps 1–4 | New `.claude/skills/` skills exist on disk with negative controls against fabricating causal edges or ungrounded gene strings; `workflow/mech-workflow.yaml` Stage 2/3 `skill_paths` and `applicability` validate cleanly. |
| **6. Coordinator Blocked-Stage Advancement & Cycle Reload** | `culturemech-infra-0004` ([#660](https://github.com/CultureBotAI/CultureMech/issues/660)) | External Coordinator / Cycle Boundary | Coordinator session `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/culturemech/{effective-workflow.json,status.json}` (read-only to repository agent) | Steps 1–5 (for Cycle 3+ reload); immediate for active Cycle 2 skip to Stage 4 | Active Cycle 2 (`goal-4672`) is advanced by the coordinator past pinned `blocked` Stages 2–3 to Stage 4 (`record_review`) without fabricating a Stage-2 `completion.json` receipt; updated `workflow/mech-workflow.yaml` is reloaded by the coordinator only between cycles (`reload_profile_between_cycles_only: true`). |



# Stage 6 Infrastructure Implementation Plan — `mech-goal-sequence-20261019` (Cycle 1)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `6` (`infrastructure` — `Infrastructure implementation plan and upgrades`)
- **Repository**: `CultureBotAI/CultureMech` (`culturemech`)
- **Source Revision**: `6a639c4b597e95b6061f2d1c7baa04de84ba2f00`
- **Scope Frozen At**: `2026-10-21T20:08:55Z`
- **Frozen `INFRA_TASKS.md` Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md`
- **Frozen Snapshot SHA-256**: `6af52c250457b5e35392e4151c0521fc9839136ede49625db74344f64eae89c7`

---

## 1. Frozen `INFRA_TASKS.md` Snapshot & Scope Reconciliation

At Stage 6 dispatch (`2026-10-21T20:08:55Z`), the session supervisor froze `INFRA_TASKS.md` (`3,525` bytes, SHA-256 `6af52c250457b5e35392e4151c0521fc9839136ede49625db74344f64eae89c7`) and saved the exact bytes to `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md`.

### 1.1 Machine-Readable Inventory in Frozen Snapshot

| Task ID | Summary | Frozen Status | Linked GitHub Issue | Disposition in Frozen Snapshot |
|---|---|---|---|---|
| `culturemech-infra-0001` | Extend `batch_review_recipes.py` solution validation for P3.1 placeholders and `chebi_term` coverage | `resolved` | [Issue #633](https://github.com/CultureBotAI/CultureMech/issues/633) | Resolved in PR #632 (commit `377d68c67960b43fe622c68f28e25f4194e4420e`) by adding P3.1 placeholder checks and `chebi_term`/`preferred_term` placeholder coverage to `_validate_solution()` with unit tests in `tests/test_batch_review_recipes.py`. |

### 1.2 Pending Scope Accounting (`InfrastructurePlan` Contract)

Per `kg_microbe_workflows` (`validate_goal_evidence` for Stage 6 `InfrastructurePlan`):
- `pending_tasks` is computed as `{item["task_id"]: item for item in notebook["tasks"] if item["status"] != "resolved"}`.
- Because `culturemech-infra-0001` is already `status: resolved` in the frozen `INFRA_TASKS.md` snapshot and no additional `note`, `open`, or `deferred` tasks were added during Stage 5 (`resolve_review_findings`), `pending_tasks` is empty (`{}`).
- Accordingly, `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/evidence.yaml` records:
  - `outcome: no_findings`
  - `findings: []`
  - `groups: []`
  - `infra_tasks: []`
  - `carry_forward_ids: []`
- `INFRA_TASKS.md` remains byte-identical (`6af52c250457b5e35392e4151c0521fc9839136ede49625db74344f64eae89c7`) with `culturemech-infra-0001` preserved in its `resolved` state.

---

## 2. Prior-Stage Verified Closure & Tracked Index Synchronization

In accordance with the workflow instruction:
> *"After prior closure is verified, update the tracked review latest index from `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/culturemech/verified-evidence-index.json` in this goal."*

`reviews/workflow/latest.yaml` has been synchronized with `verified-evidence-index.json` (`authority: verified_closure`) to record both verified Cycle 1 closures prior to Stage 6:

1. **Cycle 1, Stage 4 (`record_review`)**:
   - Evidence: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` (`sha256: a10907eb4a96adc166694ee37eedc99fafb144abaefd8abe0d130185470437fd`)
   - PR: `#632` (head `e0016088c5dc263c3414d6d0bf4e3b4c269cd4e4`, merge commit `24a1d277eb7f0437af53af0d178a30f9bfa6374c`, merged `2026-10-21T02:14:58Z`, verified `2026-10-21T02:24:29.091184+00:00`, all 9 required checks `SUCCESS`).
2. **Cycle 1, Stage 5 (`resolve_review_findings`)**:
   - Evidence: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml` (`sha256: 4df846ec65c3aaafc78a9cb379afa743aca8a5a42df197290a7b03da0738c41e`)
   - PR: `#654` (head `cb07347bfee7480cd9001c93803474e1a81f7283`, merge commit `6a639c4b597e95b6061f2d1c7baa04de84ba2f00`, merged `2026-10-21T20:04:58Z`, verified `2026-10-21T20:08:55.813422+00:00`, all 9 required checks `SUCCESS`).

---

## 3. Repository Infrastructure & Open GitHub Issue Queue Triage (`review-open-issues`)

To inform Cycle 2 intake without mutating the frozen Cycle 1 `INFRA_TASKS.md` scope, the complete open GitHub issue queue in `CultureBotAI/CultureMech` (`68` open issues, `#150` through `#628`) was audited against current `main` (`6a639c4b597e95b6061f2d1c7baa04de84ba2f00`).

### 3.1 Dependency-Aware Layer Architecture

```
1. Schema & Generators (src/culturemech/schema/culturemech.yaml)
        ↓
2. Raw / Import & Parser Normalization (src/culturemech/import/, scripts/repair_*)
        ↓
3. Normalized Corpus & Stock Solution Extraction (data/normalized_yaml/)
        ↓
4. Chemical Grounding & MIM Label Index (src/culturemech/data/mediaingredientmech/label_index.csv, scripts/audit_*)
        ↓
5. Recipe Merge & Deduplication (data/merge_yaml/merged/)
        ↓
6. KGX Export, Browser Data, & Static Pages (output/kgx/, app/, pages/)
```

### 3.2 Priority Tier Summary Across All 68 Open Issues

| Priority Tier | Count | Issue Numbers | Disposition for Cycle 2 Intake |
|---|---:|---|---|
| **P1 — Data Correctness / Silent KGX Loss / Math Defects** | 21 | `#150`, `#182`, `#255`, `#258`, `#283`, `#288`, `#292`, `#372`, `#394`, `#403`, `#476`, `#495`, `#522`, `#523`, `#540`, `#551`, `#575`, `#585`, `#600`, `#616`, `#628` | Primary candidates for Cycle 2 record review and targeted repair scripts; gate baselines ratchet down monotonically as cohorts close. |
| **P2 — Completeness / Provenance / Schema / Curation Tooling** | 34 | `#151`, `#152`, `#159`, `#175`, `#181`, `#183`, `#241`, `#242`, `#244`, `#262`, `#279`, `#301`, `#371`, `#438`, `#448`, `#460`, `#461`, `#464`, `#468`, `#477`, `#494`, `#496`, `#497`, `#524`, `#525`, `#532`, `#534`, `#535`, `#536`, `#539`, `#550`, `#553`, `#566`, `#576` | Secondary backlog; bounded cohorts (`#525`, `#534`, `#535`, `#536`, `#550`, `#566`) are ready for deterministic script/curation passes in future cycles. |
| **Needs-Human — Source Ambiguity / Editorial Judgment** | 8 | `#498`, `#506`, `#533`, `#548`, `#549`, `#554`, `#565`, `#567` | Require primary literature lookup or explicit curator judgment on variant identity before automated edits. |
| **Cross-Repo / Upstream-Blocked** | 5 | `#284`, `#310`, `#421`, `#462`, `#574` | Depend on `MediaIngredientMech`, `KG-Microbe`, or external provider billing/API availability. |

### 3.3 Key Cohort Verification Highlights

- **Stock-vs-Medium & Concentration Plausibility (`#150`, `#476`, `#522`, `#523`, `#540`, `#551`, `#575`, `#585`, `#600`, `#616`, `#628`)**:
  - In Cycle 1 Stages 4–5, the `komodo_962_thermincola_carboxydiphila_medium` 2x stock-vs-final concentration defect was fully remediated (`PR #654`), lowering the corpus plausibility gate count by 9 rows (`9,246 -> 9,237` vs `--max-allowed 9252`, `169 <= 171` cocktails).
  - Remaining tracked cohorts (`#628` MediaDive 5003a Trace Elements x1000, `#616` JCM Trace Vitamins x2, `#600` KOMODO 641/616/464 Trace Vitamins x10, `#585` MediaDive 457b/c mineral solution x50, `#575` MediaDive 3118 mineral solution x20) follow the same deterministic repair pattern for future cycles.
- **Merged Duplicate Summing & Repeated Rows (`#283`, `#394`)**:
  - Current `audit-merged-duplicates` baseline holds `IDENTICAL_PARTS = 0`, `DIFFERING_PARTS = 3,772`, `COEXISTING_ROW = 276`, and `REPEATED_INGREDIENT = 539`.
  - In Cycle 1 Stage 5 (`PR #654`), the `D2O` (`CHEBI:41981`) vs `Distilled water` (`CHEBI:15377`) false collision in `TOGO_M2765_SC_Medium.yaml` was resolved.
- **Chemical Grounding & Label Correspondence (`#255`, `#258`, `#372`, `#403`, `#495`)**:
  - `check-mim-label-index` and `check-chebi-structure-index` pass cleanly; `audit-ungrounded-ingredients` holds at `<= 3,217` distinct names.

---

## 4. Domain Applicability Verification (`Stage 2` and `Stage 3`)

Per `.claude/skills/culturemech-evolve-workflow/SKILL.md`, Stage 6 verifies that repository-specific stage `applicability` settings in `workflow/mech-workflow.yaml` remain accurate:
- **Stage 2 (`causal_graphs`)**: `applicability: blocked` (`applicability_reason` documented) — CultureMech curates growth media and stock solution recipes (`MediaRecipe`, `SolutionRecipe`) and does not contain causal graph models.
- **Stage 3 (`protein_examples`)**: `applicability: blocked` (`applicability_reason` documented) — CultureMech does not curate protein mechanism examples.
- **Stages 1, 4, 5, 6**: `applicability: enabled` — All four enabled stages in `mech-goal-sequence-20261019` Cycle 1 are active and verified.

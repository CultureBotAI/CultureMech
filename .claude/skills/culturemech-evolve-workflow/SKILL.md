---
name: culturemech-evolve-workflow
description: "Adapt and maintain CultureMech's recurring goal-cycle workflow profile and optional LinkML extension while work proceeds. Use at goal preflight, when a real workflow requirement appears, for grouped review remediation, or for the infrastructure implementation goal."
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Evolve the CultureMech workflow

Repository: `CultureBotAI/CultureMech`. Scientific records: `data/merge_yaml/merged/*.yaml`.
Native scientific schemas: `src/culturemech/schema/culturemech.yaml`.

## Authority and preflight

<!-- canonical:begin authority -->
Read the coordinator's active-cycle status and immutable effective-profile pin,
then workflow/mech-workflow.yaml and its hash-pinned parent snapshots at
workflow/parent/mech-cycle.yaml and workflow/parent/workflow.yaml. Validate the
profile through the installed CLAW workflow loader, using the verified CLAW
checkout if the package is unavailable locally. Its structured parent is the
source of truth for goal order, closure gates, evidence, and cycle behavior.
Repository-local .claude/skills are the source of truth for executing native
work. Resolve skill paths from the profile and inspect them before each goal.
Read the supervisor-supplied status.json for the exact run, cycle, stage, native
goal identity, active profile, evidence requirements and closure receipt path.
Use receipt_template, goal_evidence_schema_path and effective_workflow_path
from that status to construct the goal_evidence and closure receipt; replace
placeholders with observed proof. Bind all output to this goal;
never infer a fresh goal or cycle from an edited candidate profile.

At each goal preflight, verify the active cycle and profile version, native goal
identity, prerequisites, corpus scope and maintained input owners. Record any
new repository requirement in INFRA_TASKS.md as work reveals it. A blocked
capability stays blocked until its prerequisite is implemented; a domain-based
inapplicability decision needs evidence and does not remove the stage's closure.
Preserve the running cycle's pinned contract. A profile edit takes effect only
at the verified next-cycle activation boundary.
<!-- canonical:end authority -->

## Local evolution

<!-- canonical:begin adaptation -->
Adapt native skill bindings, validation commands, record scopes, evidence paths
allowed by the parent, and applicability reasons when inspected repository
behavior supports a change. Keep domain notes outside these managed regions.
Record a versioned rationale, real issue link, supporting paths and hashes,
validation results, compatibility assessment, and activation cycle. Search
ignored and hidden files before asserting that a capability or path is absent.

For a genuine local data requirement, add a namespaced LinkML class and a
separate extension data document under workflow/schema and workflow, and bind
both file hashes plus the class name through the profile's extension field.
Validate the extension and the complete effective profile. Extend the local
model narrowly; do not rewrite the shared schema or hide unknown parent keys in
an extension. Shared changes belong in the CLAW parent with compatibility and
migration review. Do not weaken review retention, GitHub issue evidence,
closure verification, cancellation/stop behavior, or cycle identity.

Prepare changes in workflow/mech-workflow.yaml as the next-cycle candidate.
The coordinator retains the active cycle as an immutable runtime effective-profile
snapshot; consult its status and pinned profile, and never edit that snapshot.
The candidate activates only after reviewed closure at the cycle boundary. Keep
older profile versions and evidence interpretable. If no supported activation
path exists, record the blocker instead of switching an active cycle manually.
<!-- canonical:end adaptation -->

## Review output and grouped remediation

<!-- canonical:begin reviews -->
Stage 4 reviews every eligible record in a frozen inventory using the native
record and cohort rubrics. Save actual review output files with stable finding
IDs, reviewed input hashes, evidence, reviewer identity and independence,
coverage, limitations, and dispositions. Use the parent-defined revision paths
under reviews/workflow, including an evidence manifest and file hashes. Commit
these outputs. Do not overwrite a prior review, reuse a cycle ID, or substitute
a terminal summary for the report. A later revision requires supersedes_evidence
pointing to the exact immediately preceding revision, with its path and hash;
previous_evidence separately pins the prior-stage or prior-cycle input and stays
fixed across corrections. Preserve all ancestor manifests and artifact bytes.
Open or deferred findings retain their IDs across revisions and cycles.

Update the tracked latest-review index only during a subsequent goal, using the
supervisor's verified-evidence-index.json identified in status.json. Carry only
entries with verified_closure authority and preserve their evidence hashes and
closure references. Do not publish an unverified current-stage report as latest
or write the supervisor's runtime index. Include the tracked index update in
that subsequent goal's normal commit sequence.

Stage 5 consumes the latest accepted stage-4 outputs. Group related problems by
shared cause and repair ownership, search open and closed issues before creating
new ones, and link each finding to a real issue or an evidenced non-actionable
disposition. Keep unrelated scientific questions in separate groups. Implement
accepted fixes through maintained native inputs and writers, validate affected
records and derived products, and obtain fresh review of the changed content.
Save the issue map, checks, resolutions, unresolved blockers, and new evidence
revision. Do not edit the original review to make its findings disappear.

The goal's scientific review output and its commit sequence's independent PR
review are different evidence. Both must be retained when required. No findings
means a documented empty result; never fabricate issues or fixes to fill a quota.
<!-- canonical:end reviews -->

## Evidence preparation and validation

<!-- canonical:begin evidence -->
Read the packaged stage-4, stage-5 and stage-6 examples under the verified CLAW
checkout's src/kg_microbe_workflows/examples directory and its README.md. They
are illustrative empty outcomes, not proof of work. Replace example identities,
source revisions, outcomes, paths and hashes with actual observations and files.
A source_revision records the input being reviewed; the closure receipt records
the final commit containing the output. Never copy an example as a live receipt.

Use `python -m kg_microbe_workflows validate-evidence <evidence.yaml> --root <repo>`
from the verified CLAW environment. For stage 5, add
`--previous <verified-stage-4-evidence.yaml>`; carry later-cycle finding history
through the parent-defined predecessor references. Add `--required-output <kind>`
for every output kind required by the active effective stage, including any
requirements beyond the base contract. The Python helper
`save_goal_evidence(repository_root, data, previous=None)` validates and creates
the manifest atomically only when its revision path is absent. It does not create
the supporting report, findings, issue map, validation or infrastructure files:
write those actual artifacts first and compute their SHA-256 hashes. A failed
validation is a blocker, not a reason to omit the evidence manifest. Validation
alone does not establish GitHub closure or that bytes were committed.
<!-- canonical:end evidence -->

## Infrastructure intake and implementation

<!-- canonical:begin infrastructure -->
Maintain INFRA_TASKS.md during every goal. Its machine-readable task inventory is
a fenced YAML mapping between the mech-infra-tasks:start and mech-infra-tasks:end
HTML comment markers, with schema_version and tasks. Keep task_id, summary,
status (note, open, deferred or resolved), issue_url and disposition in that
inventory. Status note may retain a pending issue link; other states require a
real issue URL. Retain richer observations, originating cycle and goal, evidence,
priority and dependencies in notes keyed by the same stable task ID.
Search for an existing issue before creating one. When issue access is blocked,
retain a visibly pending-link entry and the blocker; do not claim complete issue
intake or invent a URL. Preserve closed entries and their resolution links.

For stage 6, read the supervisor-frozen infra_scope content, hash and cutoff
time in status.json. Save that exact byte content as the infra_snapshot artifact;
do not replace it with the notebook as it looks later in the goal. The plan must
account for every non-resolved task in that frozen snapshot and preserve existing
issue URLs. Group related needs, write a bounded implementation plan with dependencies, acceptance
criteria and validation, and create or reuse real issues for the plan. Implement
the selected work, check its behavior, update the ledger with issue/PR outcomes,
and save the snapshot, plan, validation and evidence manifest. Explicitly carry
forward blocked or deferred work; do not erase it. New tasks discovered after
the cutoff belong to the next intake; never expand the frozen task-ID scope.
If a new prerequisite blocks a selected task, retain both entries and explicitly
defer that selected task with its issue and reason. Implementation details may
change within an existing frozen task. An empty intake is a real no-op with
evidence, not a reason to invent upgrades. Complete the commit sequence, write the required closure
receipt, and stop. Only the supervisor verifies closure, activates a validated
next-cycle profile, and dispatches the next /goal; never start it yourself.
<!-- canonical:end infrastructure -->

## Closure after every goal

<!-- canonical:begin closure -->
Validate and commit only goal-owned changes, push the feature branch and open or
update its PR, independently review the exact head, file actual deduplicated
findings as issues, fix them and re-review. Follow current native merge-queue and
protection rules; verify actual merge, required checks and landed content before
deleting only the owned feature branch. Retain the PR, issue, reviewed head,
merge commit and cleanup receipt. A genuine no-diff goal needs an evidence-backed
no-op receipt. Passing tests, enabled auto-merge, or a completion sentence is not
proof of closure. Build the structured receipt from receipt_template and write it to
completion_receipt_path from status.json, including the required goal_evidence
artifact reference and hash,
then stop. The supervisor alone decides advancement or restart. A cancelled or
blocked goal never advances silently.
<!-- canonical:end closure -->

## Repository-specific adaptation

Use the profile's exact native skill bindings and this repository's review
profile to retain scientific rubrics and generated-input ownership. Add local
workflow decisions and tested commands here, outside managed regions, as the
repository evolves. Keep runtime observations dated; recheck them before use.

Local candidate: `workflow/mech-workflow.yaml`. The coordinator target uses
`workflow_next_profile_path` for boundary activation. The current cycle retains
an immutable runtime effective-profile snapshot; inspect its status and pin
before editing the candidate, and never edit the runtime snapshot.

Read `docs/record-review-profile.md` and each selected native review skill
for the current scientific rubric, saver and generated-input ownership. Native
structured reviews retain their own format and location; the workflow evidence
manifest includes their immutable artifacts or a hash-bound aggregate report.
A native issue-only saver does not waive the cycle report or coverage ledger
when no findings exist.

The following domain constraints were inherited from the previous inspected
workflow and must be rechecked against current source before changing a binding:

- Authoritative curation is data/normalized_yaml; merged recipes and Pages are generated.
- Native schema has no native causal graph (`CausalEdge` / `MechanismGraph`) slot yet (#658). Do not invent causal fields or equate composition/role visualizations with causal mechanisms.
- Typed UniProtKB protein-example representation (`UniProtKB` prefix, `UniProtTerm`, `ProteinExample`, `protein_examples` slots on `MediaRecipe`, `OrganismDescriptor`, `CofactorDescriptor`, `CofactorRequirement`, and `TransporterAnnotation`), semantic validation (`src/culturemech/validation/protein_examples.py`, `scripts/validate_protein_examples.py`, `src/culturemech/validation/write_validated.py`, `scripts/validate_strict.py`), maintained history-appending writer (`scripts/apply_protein_examples.py`), KGX `biolink:Protein` export (`src/culturemech/export/kgx_export.py`), and `.claude/skills/curate-protein-examples/SKILL.md` are implemented for https://github.com/CultureBotAI/CultureMech/issues/659 (`culturemech-infra-0003`).

### Profile Evolution Log

- **Profile version `1.1.0` (2026-10-25, issue https://github.com/CultureBotAI/CultureMech/issues/659 / `culturemech-infra-0003`)**:
  - **Rationale**: Bind `.claude/skills/curate-protein-examples/SKILL.md` to Stage 3 (`protein_examples`) in `workflow/mech-workflow.yaml` after implementing the repository-local typed `UniProtKB` / `ProteinExample` schema, validator, writer, KGX exporter, reference cofactor ChEBI fix, and unit test suite (`tests/test_protein_examples.py`).
  - **Supporting paths**: `src/culturemech/schema/culturemech.yaml`, `src/culturemech/validation/protein_examples.py`, `scripts/validate_protein_examples.py`, `scripts/apply_protein_examples.py`, `src/culturemech/export/kgx_export.py`, `conf/id_label_targets.yaml`, `conf/oak_config.yaml`, `data/reference/cofactors.yaml`, `.claude/skills/curate-protein-examples/SKILL.md`, `tests/test_protein_examples.py`.
  - **Validation**: `kg_microbe_workflows validate`, `scripts/audit_schema.py`, `scripts/audit_writers.py`, `scripts/validate_claude_skills.py`, `scripts/check_vendored_sync.sh`, and `pytest tests/test_protein_examples.py` all pass (`0` errors).
  - **Compatibility & activation cycle**: Backward-compatible candidate update (`reload_profile_between_cycles_only: true`). Active Cycle 2 runtime files (`effective-workflow.json`, `status.json`, `completion.json`) remain untouched, and Stage 2 (`#658`) and Stage 3 remain `applicability: blocked` until between-cycle coordinator activation (`https://github.com/CultureBotAI/CultureMech/issues/660`).

Verified local inspection: 01e60706cb29ecefbf49204369dd8238df7b52fc. This records an inspected
local revision, not a claim about the current published default branch.

Run profile validation from the verified CLAW checkout, with its interpreter
and current source on PYTHONPATH (do not assume a global console command exists):

```bash
PYTHONPATH="/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src" "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python" -m kg_microbe_workflows validate --profile "/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech/workflow/mech-workflow.yaml" --parent "/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech/workflow/parent/mech-cycle.yaml" --schema "/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech/workflow/parent/workflow.yaml"
```

After deployment, use the installed reviewed CLAW source path recorded in the
rollout receipt; revalidate that checkout identity before execution.

The coordinator installed this adaptation skill, workflow/mech-workflow.yaml,
workflow/parent/mech-cycle.yaml, workflow/parent/workflow.yaml, and INFRA_TASKS.md
as the user-authorized workflow bootstrap. Include these files in this goal’s
next commit/PR closure unless they are already committed; preserve unrelated
local changes. Installation alone is not publication or completion evidence.

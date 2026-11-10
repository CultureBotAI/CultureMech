---
name: repository-freshness
description: Verify canonical repository freshness before a new agy or Codex goal freezes input, and after its actual merge, under an explicitly adopted boundary contract.
scope: domain
---

# Repository freshness for CultureMech

Repository: `CultureBotAI/CultureMech`.

This file is a **candidate adapter**. Its presence, this PR, or a canonical
source commit does not activate it. Read `proposal.json` beside this file:
`proposal_only` and `blocked_on_canonical_release` prohibit execution authority.
The active parent/profile, native goal, evidence and runtime adoption remain
unchanged until a separately approved release and verified cycle boundary.

**Durable session state.**
Use the gitignored `<repo>/.temp/` as the durable work root for review campaigns,
worktrees, batch state, draft review bundles and handoffs. Use
`~/agent-work/<repo>/` when a separate clone is needed. Verify `.temp/` is ignored
before use; provision a missing ignore rule through an authorized repository
change. Keep maintained helpers and accepted evidence in their native tracked
directories; a durable scratch root does not replace their provenance contract.

Never store session state or helper scripts in `/tmp/`, `/private/tmp/` or `$TMPDIR`.
Only disposable caches and pytest temporary fixtures may use system temp roots.
Use a unique subdirectory for each task and preserve other sessions' state.

Report every auxiliary clone for identity verification and inventory in
session_repository_roots, and owned campaign/handoff directories in
session_state_paths. Missing inventory is unknown, not healthy. Report new paths
to the supervisor/operator; do not edit live configuration or expand authority.

For authorized Git work, push each committed batch branch to `origin` the same
day, whether or not a PR is opened. Verify the exact pushed head with the remote;
a local commit or remote-tracking ref alone is not publication proof. Inspect
the repository's current workflow triggers before claiming a branch push runs
no CI. A goal delivering commits cannot close while recorded commits exist only
locally. Publication failure is a retained blocker, never permission to discard
the branch. This rule grants no Git mutation, merge, cleanup or provider
authorization beyond the task and the skill's existing boundaries.


After adoption, both Intel agy and M5 Codex use the same packaged freshness
runner and immutable adoption record. Before a new goal creates its issue,
record, source or infrastructure inventory, run the adopted pre-goal gate and
read the inventory from the verified fetched HEAD. This applies to empty and
no-change goals too. Retain the result's repository, canonical remote/default
branch, before/fetched/after revisions, observation time and status with the
new goal. A transported instruction is not evidence that the gate succeeded.

After GitHub verifies the actual merge, run the post-merge gate with the actual
merge commit. It must prove that commit is an ancestor of the freshly fetched
canonical revision and that the owned eligible checkout is exactly at that
revision. Own-merge inclusion alone does not establish freshness: a newer
external backlog commit must also be present. Do not close or dispatch the next
goal while the gate holds. A no-change outcome has no fabricated merge SHA;
it still needs the pre-goal check and the adopted no-change closure check.

Use `python -m kg_microbe_workflows.freshness_cli run --request REQUEST.json --apply`
from the adopted canonical release, then `python -m
kg_microbe_workflows.freshness_cli verify --request REQUEST.json`
before inventory consumption. The exact release's
`docs/guides/REPOSITORY_FRESHNESS.md` defines the strict request and receipt shapes.
A candidate package does not authorize these commands against a live checkout. The supervisor owns its guarded hooks;
standalone Codex uses that same runner with the approved adoption record and
explicit owned checkout. Do not substitute `git pull`, a remembered origin SHA,
an edited receipt, or a claim that a branch contains the goal's merge.

Dirty/staged/overwrite-colliding, ahead/diverged, detached/feature, active Git
operation, ambiguous/shared owner, wrong remote, fetch failure and ref-race
states hold with their recorded diagnosis. Never reset, stash, clean, switch
another session's branch, rebase or force. Preserve noncolliding ignored
reports. Feature tasks use a separately owned fresh base. The live claw
control checkout returns a deployment-required hold; its code changes require
reviewed deployment, pin refresh, restart and heartbeat verification.

Approved future adoption binds the released canonical source, this policy's
exact digest, the unchanged active workflow digest, exact repository root,
run/cycle boundary and predecessor closure receipt. Previously running goals
stay explicitly unadopted. Candidate generation never writes native identity,
ledgers, receipts, status, counters, budgets or active workflow/vendored pins.

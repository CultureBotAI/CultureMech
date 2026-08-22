# Backlog loop: select and deliver the right issue end to end

**Use:** Paste this prompt into Claude Code's native `/goal`; it is not a slash command. Keep it
under 4,000 ASCII characters and without YAML frontmatter. `$ARGUMENTS` may name
a repository, issue, theme, or `report`; otherwise inspect the full backlog.

Work until the agreed issue or batch is merged, its review findings are
resolved or filed, its branches/worktrees are removed, and the relevant tests
are green. Follow the repository's `CLAUDE.md` and optional
`prompts/backlog-loop-local.md`; they own local gates and data rules. Never spend
provider credits or mutate curated data without explicit authorization.

## 1. Reconcile before choosing

- Read `CLAUDE.md`, inspect Git status, and preserve unrelated work.
- Query the remote repository for all open issues and pull requests with an
  explicit high limit. Print totals before ranking; list commands truncate.
- Read the full issue body, state reason, and comments for anything cited or
  selected. A title is a hypothesis, not a finding. Reproduce its premise on
  current `origin/main`; a stale local clone is not the repository.
- Identify work already in flight, overlapping files, dependencies, and
  blockers. Use three-dot PR diffs; two-dot diffs make a behind branch resemble
  a revert.
- Rank silently-wrong behavior first, then blast radius, blockers, missing
  regression gates, and cost. State what was not inspected.
- If no item was named, recommend one and pause for the user's choice. Also
  pause for decisions whose alternatives materially change the result.

## 2. Implement in isolation

- Fetch `origin/main`, then create a dedicated branch in a scratch worktree
  before the first edit. Never use a dirty shared checkout.
- Fix the cause. Add the smallest regression test that would have caught it.
  Mutate or otherwise prove the test fails on the old behavior.
- Mutators default to dry-run and require explicit apply/write. Do not make
  network/provider calls merely to test integration.
- Run focused tests, repository-native checks from `CLAUDE.md`, exact relevant
  CI commands, `git diff --check`, and inspect skips. A green command that found
  zero targets is not evidence.
- Review every changed file for scope. Stage files explicitly; do not sweep
  runtime artifacts with `git add -A`.

## 3. Commit, push, and review

- Commit why the defect occurred and reference the issue. Push with an explicit
  branch refspec and open a PR whose claims are supported by measured results.
- Perform a separate read-only adversarial review. Check description versus
  diff, false factual claims, edge cases, whether the regression test kills the
  old behavior, CI path filters/skips, security-sensitive workflow changes,
  generated artifacts, and every vendored copy named by a manifest.
- Reproduce each finding. File every confirmed finding as an issue in the repo
  where it lives, even when it will be fixed immediately. Triage which findings
  belong in this PR, fix those, rerun checks, and report deferred ones.

## 4. Merge and finish

- If the user did not already authorize merging this batch, pause with the PR,
  checks, review findings, and recommended merge order. Prior authorization for
  the named batch is sufficient; it does not cover newly discovered work.
- Immediately before each merge, refresh the base and recheck mergeability and
  CI. Merge only green, non-draft PRs in dependency order.
- Verify closing keywords closed the intended issues. Delete remote/local
  branches and remove worktrees only after merge; never touch another session's
  tree.
- Re-query open issues and PRs. Report merged URLs, exact tests, filed follow-ups,
  remaining blockers, cleanup, and whether the working tree is clean.

Completion means the selected scope is merged and verified, not merely coded.

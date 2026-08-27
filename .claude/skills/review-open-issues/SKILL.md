---
name: review-open-issues
description: Sweep and prioritize CultureMech's complete open GitHub issue queue using current corpus, schema, grounding, gate-baseline, and export evidence. Use for full backlog triage or deciding which issues are genuinely urgent; do not use as permission to close issues, run bulk mutators, or implement fixes.
category: workflow
requires_database: false
requires_internet: true
version: 2.0.0
---

# Review and prioritize open issues

Produce a complete, dependency-aware triage of CultureMech's open issues.
The issue queue, `NEXT_TASKS.md`, and the corpus itself are different surfaces:
sweep the queue, then test every claim against the current repository and the
authoritative project contracts.

This is a read-only review by default. It does not implement fixes, run bulk
corpus mutators, close or edit issues, change labels, or maintain a tracker
unless the user separately authorizes that exact mutation.

**When to use**: the user asks to review, triage, or prioritize issues or the
backlog; asks what is genuinely urgent; or a review pass has just filed a batch
of issues that need sorting.

**When NOT to use**: `NEXT_TASKS.md` upkeep, picking the next unit of work to
implement, or acting on a single known issue. That is `next-tasks`, the lighter
pass that runs one `gh issue list` as *context* for reconciling the backlog file
and never assesses issue validity individually. This skill produces a ranking,
not a fix, and is expensive enough that it should not run on every "what's next"
question.

## Sources of truth

Use these before relying on an issue title or an old planning document:

- `CLAUDE.md` — the repository contract: data authority per layer, required
  validation per changed surface, and the recipe/schema editing rules;
- `docs/DATA_LAYERS.md` — which layer generates which, and which paths are
  ignored CI output that must never be hand-edited;
- `project.justfile` — the authoritative gate baselines. Each ratchet recipe
  carries its own `--max-allowed` history in a comment explaining what the
  number means and why it moved;
- `src/culturemech/schema/culturemech.yaml` — the authoritative schema; a claim
  about a slot is checked here, not in generated dataclasses or docs;
- `docs/KGX_SEMANTIC_MODEL.md` and `src/culturemech/export/kgx_export.py` — what
  actually reaches the knowledge graph;
- `docs/SSSOM_PIPELINE.md` and `src/culturemech/data/mediaingredientmech/label_index.csv`
  — publication-time ingredient identity;
- `docs/RECIPE_ID_LIFECYCLE.md` — ID permanence and retirement;
- `curation_history` on the affected records — append-only, dated, and often the
  only record of why a value looks wrong;
- current source, tests, CI workflows, and committed report artifacts for actual
  behavior.

Treat issue bodies and titles as claims, not current status. Read comments: this
repository records corrections and narrowed residual work there. A merged PR is
evidence only after its code and acceptance criteria are checked.

## Workflow

### 1. Fetch the entire queue

Confirm the repository, current count, labels, and full queue. Never silently
accept `gh`'s default 30-item limit.

```bash
gh repo view --json nameWithOwner,url,defaultBranchRef
gh issue list --state open --limit 5000 --json number | jq length
gh issue list --state open --limit 5000 \
  --json number,title,body,comments,labels,createdAt,updatedAt,author
gh label list --limit 200
```

Fetch the count first, then re-run with `--limit` comfortably above it. `gh`
auto-paginates, so one call with a high enough limit returns the full set — but
omitting `--limit` caps silently at 30, which looks like a complete sweep.

State the exact number reviewed and whether coverage was complete. Read every
issue body and its comments. Batch independent `gh` and `git` calls into single
rounds to keep the sweep cheap — but read the queue yourself rather than
splitting it across agents. Steps 2 and 5 rank issues against each other, and a
reader who only saw one group cannot do that; a split sweep is first-page
sampling arriving by another route.

### 2. Build the dependency graph before assigning rank

Place issues at the earliest affected layer:

```text
data/raw/ capture (immutable; large payloads gitignored)
  -> data/raw_yaml/ mechanical conversion
  -> data/normalized_yaml/ authoritative curated corpus
  -> ingredient grounding and ontology identity (SSSOM / MIM label index)
  -> data/merge_yaml/merged/ canonical merges
  -> KGX export, browser data, pages/, derived reports
  -> an outward-facing count, claim, or published graph
```

An upstream identity or correctness problem invalidates every derived layer
below it. Recommend fixing the root before regenerating or polishing downstream
output.

Group issues that share a root cause. Most of this queue is filed in batches by
review passes, so the duplicates cluster on:

- a shared PR or commit reference in the title or body;
- the same file, function, script, or `just` recipe named;
- a near-identical failure scenario described from a different angle.

Report groups explicitly and keep every individual issue number visible. A
human may want to close duplicates deliberately, not have them hidden.

For each issue, record when applicable:

- corpus layer and owning repository (CultureMech, MediaIngredientMech, kg-microbe);
- affected records, and whether the claim is per-row or per-name;
- schema slot, ontology prefix, unit enum, and `record_kind` assumptions;
- which gate would have caught it, and whether that gate exists;
- prerequisites, blockers, duplicates, and superseding issues;
- cheapest decisive evidence and acceptance test;
- execution class: read-only audit, single-record edit, corpus-wide mutator
  (dry-run + canary required), full-corpus regeneration, or paid research/API run.

### 3. Check current reality and staleness

For each issue or group representative:

- Search exact issue references in history:

  ```bash
  git log --all --oneline --perl-regexp --grep '#<N>\b'
  gh pr list --state merged --search '<N>' --limit 100
  ```

  The word boundary is required: `#48` must not match `#480`. GitHub PR search
  is only a lead — it matches the number anywhere in indexed text; open each
  candidate and verify that it actually resolves the issue.

- Use `rg` to confirm that named paths, scripts, `just` recipes, flags, and
  slots still exist and behave as described. Inspect tests as well as
  implementation — a passing test that never exercises the guarded path is a
  known failure mode here.
- Compare acceptance criteria with the merged change. If only part is fixed,
  retain the issue with a narrowed residual; do not recommend closure merely
  because a related PR merged.
- Distinguish an observation from its action issue. Prefer closing a fully
  recorded observation as superseded when a separate open issue owns the only
  remaining work.
- Verify counts against their actual immediate source. A committed report under
  `data/import_tracking/reports/` is derived and can lag, and `data/merge_yaml/`
  is derived from `data/normalized_yaml/` rather than authoritative. Regenerate,
  or run `just audit-merge-freshness` for the merge layer, before quoting a
  number from either — do not assume today's drift state in either direction.
- The local checkout can lag `origin/main`. Verify what the repository contains
  with `gh api` or a fresh `git fetch`, not the working tree alone.

### 4. Apply corpus stop-the-line checks

Treat these as P0 when live or externally consequential:

- a bulk mutator that destroys curated content — groundings, nested
  sub-solutions, or multi-line labels — while reporting success;
- an invented or unverified ontology ID, label, or citation, or a grounding
  whose term formula contradicts the ingredient name;
- ID reuse, renumbering, or a hand-picked "free" ID; a rewritten or deleted
  `curation_history` event;
- silent edge loss or duplication in the KGX export, garbage nodes minted from
  unparsed composition text, or an export that writes no file at all;
- a derived artifact committed as if authoritative, or a hand-edited path that
  `docs/DATA_LAYERS.md` lists as ignored CI output;
- a gate baseline raised to make a run pass rather than lowered as the backlog
  is repaired;
- a corpus-wide change landed without a canary, where the cost of being wrong
  multiplies across ~15,900 records.

Prefer a gate run over prose as evidence — but check first whether the gate
runs on its own. Only three block a pull request today:

- `just validate-strict` (validate-strict.yaml, tests.yaml);
- `just audit-concentration-plausibility` (concentration-plausibility.yaml);
- `just check-chebi-grounding` (chebi-consistency.yaml).

An issue asserting a defect that one of *these* already blocks is P2 unless it
shows the gate is porous.

The rest run only when someone types the command, so they contain nothing on
their own: `just assign-ids-check`, `just audit-derived-artifacts`,
`just audit-unparsed-composition` and `just check-mim-label-index` appear in no
workflow, and `just audit-merge-freshness` is a nightly alert whose own
workflow header says it runs "NOT as a blocking per-PR gate". They are the cheapest
decisive evidence a triager can run — run them and cite the output — but never
downgrade an issue because one of them exists. An invariant guarded only by an
unrun command is unguarded, and a missing gate over a consequential invariant is
itself worth an issue.

Re-derive that split rather than trusting this list; workflows change.

### 5. Assign priority and execution order

Use priority for consequence and a separate readiness/cost annotation for
ordering.

- **P0 — stop the line.** Corpus corruption, a wrong published grounding or
  count, silent wrong scientific output, or a blocker that must be resolved
  before an already-planned costly operation.
- **P1 — important and schedulable.** Correctness, reproducibility, provenance,
  or gate-coverage gaps; defects that can waste a large curation or research
  pass; missing guards for a likely workflow.
- **P2 — low-risk or historical.** Documentation drift, refactors, theoretical
  edge cases, optional audits, and work confined to legacy paths without active
  spillover.
- **CLOSE/UPDATE.** Fixed, superseded, duplicate, no-longer-applicable, or title
  materially broader than the remaining work. Cite the exact commit/PR/code or
  comment that supports the disposition.

Calibrate P0 sparingly. Then order work within and across tiers using:

1. upstream unblockers before downstream consumers;
2. authoritative-corpus correctness before derived-layer regeneration;
3. recover already-paid-for evidence before rerunning a billed research sweep;
4. read-only audits before mutators; dry-run and canary before fan-out;
5. add the missing gate before clearing the backlog it would protect;
6. combine issues only when one patch genuinely satisfies each issue's
   acceptance criteria.

Do not prioritize by age, sunk effort, or a `P0` string in a stale title alone.

### 6. Report

Return a compact report with:

1. coverage: repository, timestamp, number reviewed, and completeness;
2. top 2–3 next actions, including why they unblock later work;
3. a dependency-ordered P0/P1/P2 table with issue number, current status,
   evidence, blockers, execution class, and next acceptance test;
4. CLOSE/UPDATE candidates with specific evidence;
5. unresolved evidence gaps and cross-repository ownership;
6. a short sequence showing which costly work must wait.

Call out old issues explicitly rather than silently dropping them. Separate
measured findings, code inspection, inference, and proposed/untested work.

## Conventions this skill enforces

- **Full-queue coverage, not first-page sampling.** State exactly how many
  issues were reviewed and whether coverage was complete.
- **Evidence over vibes.** Every CLOSE/UPDATE/duplicate recommendation cites a
  specific commit, PR, artifact, or code location — never "this looks done."
- **P0 is rare.** If more than ~10% of the queue lands P0, the calibration is
  wrong; recheck. A stale `P0:` string in a title is not evidence.
- **Titles are claims and they drift.** Issues get retitled mid-life, including
  to `[WITHDRAWN/RESOLVED]`, while staying open. Re-read titles at report time
  rather than trusting the ones fetched at the start of the sweep.
- **The queue moves during the sweep.** Parallel PRs can resolve issues while
  triage is in progress. Re-check the open set immediately before reporting,
  and say so if it changed.
- **Read-only by default.** Reporting and ranking happen automatically; closing
  issues or touching a tracker requires explicit confirmation.

## Measurement discipline

The recurring failure here is not misreading evidence, it is mismeasuring it.
Before citing any of the following, confirm how it was obtained:

- **Rows versus names.** Several gates count distinct ingredient *names*, not
  corpus rows, because one regrounding decision fixes every row of a name. A
  count compared against the wrong denominator turns a 5-name backlog into a
  thousand-row emergency, or hides one.
- **Derived files are not sources.** A number read from a committed report, from
  `data/merge_yaml/`, or from generated page assets can predate its source.
  Confirm against the actual immediate source or regenerate.
- **Exit codes through pipes.** `cmd | tail -3; echo $?` reports `tail`'s
  status, not `cmd`'s, so a fail-closed gate looks like it passed. Use
  `cmd >/tmp/o 2>/tmp/e; echo $?`, or `${PIPESTATUS[0]}`.
- **Whitespace-splitting file lists.** `git status --porcelain | awk '{print $2}'`
  turns one path containing spaces into several bogus entries — and this corpus
  has many spaced filenames. Use `--porcelain -z | tr '\0' '\n'`.
- **Glob patterns tested by shape.** A `case`/regex check on a `.gitignore`
  pattern tests what it looks like; `git check-ignore --no-index <path>` tests
  what it does. Only the second is evidence.
- **Local git state is not repository state.** Sibling clones and `/tmp`
  worktrees hold untracked scratch copies that can fake cross-repo alignment.
  Verify with `gh api`, not the filesystem.
- **A green diff is not an unchanged file.** YAML round-trips can reflow a whole
  file while the intended node is correct. Review the diff, not just the value.
- **Truncated tool output.** Several checkers elide long lines. Re-read the
  cited file at the cited line before acting on it.
- **Backticks in a double-quoted `-m`.** `git commit -m "...`cmd`..."` executes
  the backticked text and ships the output in place of the example. Write
  reports and commit messages containing shell examples via `-F <file>` or a
  quoted heredoc, then read the result back before pushing.

## Notes and limitations

- `gh issue list --json` omits `comments` unless explicitly requested. This
  repository records corrections, withdrawals, and narrowed residual scope in
  comments, so a body-only fetch will systematically overstate what is open.
- `gh pr list --search "<N>"` matches the number anywhere in indexed text, so it
  returns unrelated PRs. Treat every hit as a lead and open it before citing it.
  Likewise `git log --grep '#<N>'` needs the `\b` anchor.
- An issue may be fully addressed in code while its acceptance criteria are not.
  Partial fixes keep the issue open with a narrowed residual; say which part is
  done and which is not.
- Evidence recovery is sometimes impossible. When an issue's residual asks for a
  value the sources do not carry, say so and recommend superseding it — a
  plausible guess that round-trips is still false chemistry.
- Cross-repository issues are common in this org. Note when a fix should
  propagate to MediaIngredientMech or kg-microbe, but do not open issues in
  sibling repos without being asked.
- No @-mentions in issue comments or reports without explicit per-mention
  authorization (standing rule).

## Related

- `next-tasks` — the lighter, `NEXT_TASKS.md`-scoped check; run that for
  "what's next" during active work, and this skill for a full-queue sweep.
  Items promoted from this ranking are often logged there so `next-tasks` picks
  them up on the next reconcile.
- `review-recipes` — per-record QA; an issue about one record's content is
  usually its job, not this one's.
- `audit-schema-gaps` — broad schema and pipeline audits, when triage shows the
  queue is a symptom of a missing contract.

## Mutation boundary

Do not close, comment on, relabel, retitle, or create issues or trackers during
the review. If the user later asks to act, present the exact issue numbers and
proposed mutation first. Apply closures one issue at a time, carrying the Step 3
evidence into the comment so the reason survives with the issue:

```bash
gh issue close <N> --comment "<commit/PR/code that resolves this>"
```

Confirm each number before its own close. A general "yes, go ahead" is not
authorization for an unattended loop — an agent closing a live issue because it
*looks* stale is worse than leaving noise in the queue.

If maintaining a tracker issue is requested, search first — `gh issue list
--search "tracker" --state open` is authoritative — and update an existing one
in place rather than creating a second.

Do not run bulk corpus mutators, regenerate derived layers, or launch billed
research sweeps as part of triage. A recommended command is a proposal, not
permission to run it.

Do not open cross-repository issues or use `@` mentions without explicit
authorization.

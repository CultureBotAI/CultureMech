---
name: review-open-issues
description: Sweep and triage the full open-issue queue for CultureMech — not just NEXT_TASKS.md. Fetches every open issue, checks each against the current code/schema for staleness (already fixed, superseded, or no longer reproducible), flags likely duplicates, and assigns a priority tier (P0 blocking/correctness/security, P1 real-but-schedulable, P2 low-severity/process/doc). Produces a short, ranked report; only touches GitHub (closing stale issues, updating/creating a tracker issue) when asked. Use when the user asks to "review issues", "prioritize the backlog", "triage open issues", or the open-issue count has grown large enough that NEXT_TASKS.md-only review is insufficient.
category: workflow
requires_database: false
requires_internet: true
version: 1.0.0
---

# Review & Prioritize Open Issues

## Overview

**Purpose**: the raw GitHub issue queue and `NEXT_TASKS.md` are different
surfaces. `next-tasks` reconciles a small, curated, actively-maintained backlog
file. This skill sweeps the *entire* open-issue queue — which grows much
larger and drifts independently (issues opened by review passes, other agents,
or humans, many of which are never transcribed into `NEXT_TASKS.md`) — and
produces an honest, current priority ranking.

**Why this is a distinct skill, not a `next-tasks` step**: `next-tasks`
Step 1 already runs `gh issue list --limit 30` as *context* for reconciling the
backlog file: it stops at the first page and never assesses issue validity
individually. This skill is the deep pass: paginate the whole queue, check each
issue against current code, and produce a full triage — expensive enough that
it should not run on every "what's next" invocation, only when explicitly
asked or when the backlog has clearly gone stale.

**When to use**: the user asks to "review issues", "prioritize open issues",
"triage the backlog", "what issues are actually urgent", or after a large
review pass (like a fleet PR review) has filed a batch of new issues that need
sorting.

**When NOT to use**: for `NEXT_TASKS.md` upkeep or picking the next unit of
work to implement — that's `next-tasks`. This skill produces a priority
ranking; it does not implement fixes.

## Workflow

### Step 1 — Fetch the full open-issue queue

```bash
gh issue list --state open --limit 300 --json number,title,body,labels,createdAt,updatedAt \
  -q '.[] | "\(.number)\t\(.createdAt[:10])\t\(.title)"'
```

Do not truncate silently. `gh issue list --limit` has no hard cap near 300 —
`gh` auto-paginates through GitHub's API, so a repo with thousands of open
issues still returns the full set from a single call with a high enough
`--limit`. If the 300-item fetch above turns out to be short, first confirm
the true count (`gh issue list --state open --limit 5000 --json number | jq
length` — omitting `--limit` silently caps at gh's default of 30), then
re-run Step 1 with `--limit` comfortably above that count rather than
sampling.

### Step 2 — Group and dedupe

Issues filed from the same review pass (same PR, same session) often overlap —
several may describe the same root cause from different angles. Group by:
- shared PR/commit reference in the title or body,
- same file/function named,
- near-identical failure scenario.

Note groups explicitly in the report; do not silently merge them (a human may
want to close duplicates deliberately, not have them hidden).

### Step 3 — Check each issue against current reality

For each issue (or each group's representative), spot-check:

- **Already fixed?** `git log --oneline --all --perl-regexp --grep "#<N>\b"`
  and `gh pr list --state merged --search "<N>"` — an issue whose fix already
  merged should be flagged STALE/CLOSE, not re-surfaced as open work. Plain
  `--grep "#<N>"` substring-matches unrelated numbers (`#48` also matches
  `#480`, `#4823`, ...) — the `\b` word-boundary anchor above is required, not
  optional.
- **Still reproducible?** If the issue names a specific file/line/function,
  confirm it still exists in that shape (`grep`/`git log -p` the cited
  location) — code moves, and a stale issue pointing at a renamed/removed
  function is noise, not a live defect.
- **Superseded?** Does a newer issue or a merged PR's description explicitly
  supersede this one?

### Step 4 — Assign priority

- **P0 — blocking/correctness/security.** Data corruption, a crash/hang in a
  path every caller hits, a security-relevant defect (injection, secret
  exposure, auth bypass), or something that silently produces wrong output
  with no detection. Fix before anything else ships.
- **P1 — real, schedulable.** A genuine defect or gap that doesn't block
  everything but should be fixed soon — most test-coverage gaps for
  safety-critical code, real (if narrow) bugs, process gaps that have already
  caused a near-miss.
- **P2 — low-severity/process/doc.** Documentation drift, stale comments,
  minor test-coverage gaps in non-critical paths, style/convention issues.

Do not default everything to P1 — that makes the tier meaningless. Use P0
sparingly and justify it; most issues are P1 or P2.

### Step 5 — Present the report

- Ranked list, P0 first, one line per issue/group with number + one-sentence
  why.
- Explicitly call out: issues recommended for closing (fixed/stale/duplicate),
  with the evidence (commit/PR that fixed it, or why it no longer applies).
- **Recommend a top 2–3** to act on next, with reasoning.
- Do not silently drop old issues from the report — if something is 6 months
  old and still open, say so; that itself is a signal.

### Step 6 — Act only when asked

This skill does not close issues, comment, or create/update a tracker issue on
its own. When the user confirms:
- **Closing stale/duplicate issues**: use `gh issue close <N> --comment
  "<reason>"`, one at a time, with the evidence from Step 3 in the comment.
- **Maintaining a tracker issue** (the "[P0-P2 tracker]" pattern used
  elsewhere in this org, e.g. CommunityMech#669): if one already exists for
  this repo, update it in place rather than creating a second one — the
  search below is authoritative, not this note: `gh issue list --search
  "tracker" --state open`. As of this skill's authoring, CultureMech's own
  prior tracker (#327, "Repository review remediation: prioritized execution
  tracker") was CLOSED, so there was no open tracker at that time — re-run the
  search rather than trusting that stays true. If it comes back empty and the
  user wants a new one, create it with the Step 5 ranking as its body, and
  link every tracked issue number.

Never bulk-close without per-item confirmation of the evidence — an agent
closing a live issue because it *looks* stale is worse than leaving noise in
the queue.

## Conventions this skill enforces

- **Full-queue coverage, not first-page sampling.** State exactly how many
  issues were reviewed and whether coverage was complete.
- **Evidence over vibes.** Every STALE/CLOSE/duplicate recommendation cites a
  specific commit, PR, or code location — never "this looks done."
- **P0 is rare.** If more than ~10% of issues land P0, the tier calibration is
  probably wrong; recheck.
- **Read-only by default.** Reporting and ranking happen automatically;
  closing issues or touching a tracker issue requires explicit confirmation.

## Notes & limitations

- `gh issue list --json` doesn't include `comments` unless explicitly
  requested (add `comments` to the `--json` field list) — Step 1's query
  above doesn't request it, so a "fixed already" claim buried in a later
  comment thread won't surface from that fetch alone; either widen the
  `--json` fields or check `gh issue view <N> --comments` for issues that
  look ambiguous.
- Cross-repo issues (a defect described once but relevant to multiple Mechs)
  are common in this org — note if an issue's fix should propagate elsewhere,
  but do not open issues in sibling repos without being asked.
- No @-mentions in issue comments or tracker updates without explicit
  per-mention authorization (standing rule).

## Related

- `next-tasks` — the lighter, `NEXT_TASKS.md`-scoped backlog check; run that
  for "what's next" during active work. Run this skill for a full-queue sweep.

## Related files

- `NEXT_TASKS.md` — items promoted from this skill's ranking often get logged
  here too, so `next-tasks` picks them up on the next reconcile.

# Issue Triage and Delivery Goal Prompt

Reusable prompt for working the open-issue backlog end to end: prioritize, verify,
implement, review, and land — one issue at a time, with the merge decision left
with the human.

```text
/goal Review and prioritize this repo's open GitHub issues, then take the top one through the full cycle — branch, implement, push, open a PR, review it adversarially, file issues from the review, address what belongs in the PR, and merge and delete the branch once I approve. Respect dependencies between PRs, and pause to ask when a decision is mine to make.
```

```text
Work the open-issue backlog for this repository.

## 1. Prioritize

List the open issues and rank them. Rank by, in order:

1. **Data that asserts something false about itself** — a record contradicting its
   own contents. These are provable, so they are actionable without judgement.
2. **Silent-rot risks** — a derived artifact, index, registry or report that
   nothing checks. These get worse invisibly and are cheap to guard.
3. **Blockers** — anything preventing other work from proceeding at all.
4. **Corpus repair needing judgement** — large, valuable, but curation rather than
   automation.
5. **Cosmetic or single-record items.**

Prefer an issue whose fix generalizes (a guard, a gate, a shared helper) over one
that fixes N records once. A one-off sweep decays; a guard does not.

State the ranking with one line of reasoning each, name the top item, and start it.

## 2. Verify the issue before acting on it

**Issues are frequently wrong, including ones written carefully.** Reproduce every
load-bearing claim before writing code, and say what you found:

- **Counts drift.** Numbers were true when filed and the corpus has moved. Re-measure.
- **Scope is often understated or overstated.** An issue reporting one bad record
  may be describing a systemic import path; an issue reporting a systemic problem
  may be describing three records.
- **The stated cause may be wrong even when the symptom is real.** Check whether
  the thing blamed is actually responsible before fixing it there.
- **The issue may already be fixed.** If so, close it with the evidence and move on.

If verification changes the picture, say so plainly and re-decide the approach.
Do not implement the fix the issue proposes if the evidence points elsewhere.

## 3. Know what is provable and what is only assumable

Before designing a rule, ask which direction the evidence actually supports.
Presence is usually provable; absence usually is not. A finite list of bad
patterns can prove a record IS bad; it can never prove a record is fine, because
the list is not exhaustive.

Build the rule in the provable direction only, and say explicitly which records
you are leaving alone and why. Where a claim needs evidence you do not have,
require positive evidence rather than inferring from "nothing matched".

## 4. Implement

- **Branch before the first edit.** Never commit to `main`.
- Reuse existing detectors and helpers rather than writing a second one; two
  implementations of the same rule will drift. If a rule needs to be shared, lift
  it into one module and point both callers at it.
- **Guards over sweeps.** If the corpus already violates the invariant, baseline
  the gate at the current count rather than demanding zero — a gate wired to a red
  suite gets switched off. Then guard the baseline itself, so it fails both when
  the count rises AND when the baseline is left far above reality and quietly
  stops biting.
- **Canary before any batch.** Run one unit end to end through the same code path
  as the batch, verify the side effects on disk rather than the exit code, and only
  then fan out. If the canary needed a fix, re-canary; do not fix and fan out in
  one step. Prefer a canary whose correct answer you already know, so it tests
  usability and not merely success.
- **Fix costs, do not raise ceilings.** If a job times out, find why it is slow
  before increasing the limit. Raising a timeout twice means the gate is decaying.
- Use explicit paths with `git add`, not `-A`, when the checkout may hold work in
  flight from elsewhere.

## 5. Review the PR

A separate, adversarial, **read-only** pass. Do not edit, push, or regenerate
anything while reviewing. Do not restate the commit message.

Try to falsify the change:

- Does the diff do only what it claims? Check for incidental reflow, swept-in
  unrelated files, or a wider blast radius than described.
- Could it silently change behaviour for existing callers? Prove it cannot, or
  measure it.
- If it widened or relaxed a guard, does that guard still reject what it used to?
  Enumerate the cases. Widening a check to accommodate your own change is how a
  guard stops guarding.
- Did moving or restamping records invalidate a derived artifact — an index, a
  registry, a committed report, a path column? These go stale silently.
- Does any documentation, comment or docstring now describe behaviour the code
  does not have?
- Are the new tests capable of failing? Mutate the code and confirm they catch it.
  A test that passes against the bug is not a test.

## 6. File issues from the review

Every finding becomes a GitHub issue, including ones you fix immediately, and
including "won't fix". The issue is the record that the finding existed and what
was decided. Do not fix silently and do not leave a finding only in a comment.

## 7. Address, then report

Fix in this PR what belongs in this PR. Leave the rest filed, and say which is
which and why — "as needed" is a judgement, not a rubber stamp. Scope creep and
silent scope reduction are both failures; state explicitly what you did not do.

If the review changed the work, note it in the PR so the reasoning survives.

## 8. Dependencies between PRs

Before opening or merging, check whether this PR interacts with others in flight:

- **Same-file, same-anchor edits.** Recipes, config blocks and list entries added
  at the same insertion point conflict even when logically independent. Stack them
  at distinct anchors, and expect a hands-on resolve for each after the first
  merges.
- **Overlapping record sets.** Two PRs touching the same records will conflict on
  data even if their purposes differ. Check for overlap and say whether it exists.
- **Guard interactions.** A PR that changes data may break a guard another PR
  added, or vice versa. Run the other PR's tests against this branch.
- **Ordering.** If one PR must land first, say so and why, and re-verify the
  second after the first merges rather than assuming it still applies.

Do not batch several unrelated concerns into one PR to avoid conflicts.

## 9. Merging is the human's decision

Do not merge without explicit approval in the current conversation. Approval of
one PR is not approval of the next. When CI is green, report that and ask.

After an approved merge, delete the branch both remote and local.

## 10. Pause and ask when the decision is not yours

Stop and put a direct question when:

- The choice is scientific or editorial rather than technical — which of two
  records survives a dedupe, which taxonomy to follow, whether a threshold is right.
- The fix would delete data or retire an identifier.
- The work would spend money or run for hours, and the scope is not obviously
  bounded.
- The issue's premise turns out to be wrong and the right fix is materially
  different from the one requested.
- Two defensible approaches differ in ways you cannot settle from the code.

Ask one clear question with the options and a recommendation. Do not proceed on an
assumption and mention it afterwards.

## Reporting

Lead with what changed and what it means, not a narration of steps. Say what you
verified rather than what you believe. Where a measurement contradicted an earlier
claim — including your own — state the correction plainly and move on.
```

# Source-Explicit Water Inputs After pH Review

The frozen [plan](plan.json) has applied 107 water-input corrections in
exact tracked standalone solution records. The guarded apply changed all 107
targets. The earlier pH-7.0 cohort is separate and unchanged.

Each correction replaces a diagnosed `PERCENT_V_V` import error with the source's
literal water input per preparation batch: 103 inputs of 1 L, one of 0.5 L, one
of 0.9 L and two of 0.8 L. These are not final volumes, percentages, stock
strengths or concentrations in receiving media. No density is assumed.

## Source Review

All 107 complete source recipe, preparation and equipment responses and the
complete corresponding records were inspected. [Frozen context](inspected-context.json)
retains the original record texts, exact source responses and retrieval metadata.
Shared ingredient/history representations were lossless; earlier evidence was
represented by its source and existing reviewer only after reproducing the
entire original record exactly. This does not newly endorse non-water claims.

Each water row explicitly gives `Distilled water`, compound ID 4, a positive
milliliter amount and no condition, attribute or optional flag. The preparation
contains one literal pH-adjustment instruction, with no water make-up instruction.
The separately inspected source attributes and equipment are preserved in the
context; they are not silently used to infer final volumes or stock strengths.

The official DSMZ dataset was located from existing source IDs. Its API URLs,
literal water-row snippets, preparation excerpts, locators, retrieval dates and
response hashes accompany each correction. Individual authors and
publication year are not supplied; no DOI or bibliographic metadata is invented.

The [51 deferred candidates](deferred.json) remain unchanged because stock rows,
local preparation differences or other context require separate reconciliation.
They are triage, not completed source reviews. Per-record `*-followup.md` files
supplement existing canonical reports and intentionally do not create duplicate
`- Record:` markers or increase unique-path coverage.

## Guarded Changes

[`repair_solution_water_ph_adjustments.py`](../../../scripts/repair_solution_water_ph_adjustments.py)
requires the exact frozen context bytes and also verifies the in-memory context.
Every selected record, source response and metadata object must still match.
The existing pH-7 helper supplies common construction and plan-validation logic;
its original CLI remains pinned to the earlier 52-record cohort. The general
solution reviewer's preparation-dependent water guard is unchanged.

The batch adds 107 ingredient evidence entries, 107 append-only `codex` events
and two root references, reusing the other 105. There are no changes to other
quantities, ingredient identities, IDs, preparation, prior evidence/history,
placeholders, variants or growth associations. Across the complete batch the
only deleted YAML lines are the old water values and units.

## Validation

The independent [baseline inversion](baseline-inversion.json) reconstructs all
107 original records and confirms all 51 deferred hashes remain unchanged.
The [applied inversion](post-inversion.json) independently repeats these checks
against the saved YAML: 107 corrected amounts, 107 evidence entries, two new
references and 107 append-only events, with every unrelated field preserved.
All before/after preview closed-schema checks pass. The
[baseline journal](baseline-validation.json) records open-schema checks,
maintained matcher exclusion, 339 passing regression tests and the successful
historical pH-7.0 plan/result verification. The
[post-apply journal](post-validation.json) is terminal: 23 of its 24 commands
passed. The separate reference-title failure below remains unresolved.

Completed post-edit checks include 339 passing regression tests, all 107 exact
record/snippet readbacks, a zero-change reapplication, the 15,910-record strict
schema and unique-ID gates, and the ontology-product gate with 91 non-blocking
warnings. All 107 excerpts also pass the installed deterministic
[source-content checker](automated-snippet-readback.json). The separate sampled
full-reference gate fails because its URL reader returns the API URL as a title
instead of the descriptive dataset title. This is not counted as a pass.

All ten earlier solution-batch readbacks pass. The
[readback and coverage reconciliation](post-readbacks-summary.json) confirms
4,770 record hashes, 23,902 retained supported snippets, 166 explicitly
superseded hashes and four separately verified historical snippets for withdrawn
quantity claims. The broad `just test-fast` suite passed: 7,491 passed, 16
skipped and 1,839 deselected in 332.43 seconds. The separately selected
339-test suite covers the new water regressions that the fast tier excludes.
Ruff and Black checks passed for the two water helpers, new tests and independent
audit. `git diff --check` passed. A final
[saved-file inversion](final-inversion.json) repeated the complete 107-record
comparison and 51 unchanged deferred hashes after the full suite.

The validation runtime is a partial locked Python 3.13 development environment:
five visualization packages are omitted after the recorded `llvmlite` build
failure. Results must not be described as full maintained-project CI.

## Remaining Work

Non-water liquid inputs, conflicting source agar amounts, source-qualified
stock/preparation boundaries and ingredient mappings remain unresolved. Water
evidence does not validate those other claims. The 51 deferred candidates need
individual reconciliation. No generated merges or pages are edited or published,
and the existing global merge failures are not resolved by this batch.

The [reconciled handoff](remaining-handoff.json) verifies current hashes for all
2,710 original water candidates: the earlier 52 and these 107 are corrected,
leaving 2,551 unchanged candidates. It also retains 14 non-water leads with
source snippets and locators, not approved amounts: seven liquid inputs, three
agar amount conflicts and four stock/preparation or alternative-substrate leads.
The subsequent [original-recipe investigation](agar-original-source-handoff.md)
inspects the three agar sources without applying further edits or assuming
final-volume concentrations.

This is local curation work, not a PR approval, merge or publication. The
all-record ingredient objective remains unfinished.

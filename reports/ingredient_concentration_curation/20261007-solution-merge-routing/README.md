# Standalone Solution Routing Repair

This fixes a pipeline defect exposed by the evidence-backed medium 111 edits.
It adds no scientific assertions, ingredient edits, review coverage or growth
associations. The normalized solution remains authoritative and available to
solution consumers; excluding it from medium merging does not delete it.

## Defects And Changes

The [observed fingerprint](../20261007-dsmz111-preparation/fingerprint-impact.json)
used only solution 190's nested glucose/water preparation while ignoring all ten
root composition entries. The existing record-class discriminator identifies
that root as `SolutionRecipe`. The generator then attempted to publish it as a
medium and dropped it with a missing `name` error.

- Use the existing classifier to reject standalone solution roots before medium
  fingerprinting. Embedded stock compositions still contribute to their parent
  medium's fingerprint, including nested stocks.
- Count standalone exclusions separately from invalid/missing ingredients and
  parsing errors. Count successfully fingerprinted records rather than groups.
- Reject standalone solution inputs in direct merge calls, including calls with
  a precomputed fingerprint that previously bypassed fingerprinting.
- Record input routing, actual written output count and group errors in merge
  statistics. A failed output group now returns nonzero instead of success.
- Permit a solution-only input directory to produce zero medium groups without
  dividing by zero in progress reporting.
- Keep standalone concentration review operational without invoking a medium
  fingerprinter. Preview and apply both enforce the root class and unchanged
  ingredient/stock fields; new previews explicitly record fingerprint scope.
- Keep the earlier retention auditor usable: a standalone exclusion is reported
  explicitly, not treated as successful merged evidence retention.

Before the repair, the new regression selection had 12 failures and one pass.
After the repair and CLI coverage, 65 focused merge tests pass. Fixtures without
source records are explicitly synthetic; the real solution 190 regression checks
its frozen post-curation hash and retained root/nested composition.

## Validation

The [corpus routing audit](routing-audit.json) checks all 15,910 exact tracked
normalized paths: 11,125 media and 4,785 standalone solutions. All standalone
solutions remain outside medium groups. Of the media, 10,783 are fingerprinted
into 6,492 groups; 340 input errors and two records without valid ingredients
remain separately reported. All normalized bytes remain unchanged during the
audit, and all three curated medium 111 hashes match the frozen scientific plan.

The same audit still detects evidence loss in the DSMZ medium 111 copy: its
ingredients, stocks, notes, evidence, references and history are not fully
retained in the canonical group. The KOMODO copy retains those fields. Routing
success does not make that merge scientifically or provenance-complete.

The initial [validation run](validation.json) caught six failures in the solution
review adapter, which still called the medium fingerprinter. After the guarded
adapter fix, the [broad focused rerun](focused-retry.json) passes **955 tests**,
with zero errors, failures or skips. A separate [Python 3.13 run](python313-validation.json)
passes **66 core merge tests** in a cached environment. This is additional
minor-version coverage, not full project dependencies or CI. The full `just test`
attempt in the isolated Python 3.11 environment failed before collection because
`pytest-cov` was missing.

An additional [Python 3.13 solution-review run](python313-solution-review-validation.json)
passes **45 tests**, including the repaired preview/apply path and drift guards.
Both Python 3.13 artifacts record the tested source hashes.

All seven main validation commands are terminal. Temporary regeneration now
[writes all 6,492 groups](generation-stats.json), with **zero group-write errors**.
The [freshness comparison](merge-freshness.json) still fails: 6,320 tracked and
6,492 fresh files; 3,719 only tracked, 3,891 only fresh, 1,657 changed and 944
unchanged. These are the same output counts as the earlier failed generation,
but the standalone solution is now correctly excluded rather than silently
dropped during output. The raw input-to-output reduction includes exclusions
and must not be described as a count of duplicate records removed.

Global verification remains unsuccessful with 1,247 name conflicts and 3,287
fingerprint issues in tracked merged output. The [scientific readback](scientific-readback.json)
passes full-record inversion for the three medium 111 inputs and preserves all
historical snippets. Whitespace checks pass. No normalized record, generated
tracked merge, or previously frozen scientific review plan changed in this
pipeline repair.

Ruff passes for the new test and audit. The older fingerprint, matcher and merger
modules have respectively 12, 14 and 33 pre-existing diagnostics; comparison
against HEAD finds no additional diagnostic code/message pairs. The CLI module
passes. Unrelated legacy typing/style issues were not rewritten.

## Remaining Scope

This does not make concentration-independent ingredient fingerprints sufficient
evidence of formulation identity. It does not resolve evidence loss between
medium copies, quantity variants, source conflicts, missing validation tools or
the remaining all-record concentration review. No generated corpus is published,
and no commit, PR or merge is claimed for this local repair.

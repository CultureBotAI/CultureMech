# DSMZ 2 Base-Medium And Preparation-Stage Repair

Applied locally on 2026-10-07 to
`data/normalized_yaml/bacterial/bacillus_pasteurii_medium.yaml`,
`CultureMech:001399`. This is follow-up work on an already reported record,
not an additional unique reviewed path or completion of the all-record goal.

## Source Verification

The original [DSMZ 2 recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium2.pdf)
explicitly uses [DSMZ 1](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1.pdf)
as its base. Both complete single-page PDFs were visually inspected. The
[receiving-medium API record](https://mediadive.dsmz.de/rest/medium/2) identifies
the base by solution ID and dose; its embedded base exactly matches the
[independent medium 1 API capture](https://mediadive.dsmz.de/rest/medium/1).
Source bytes and local baseline are hash-pinned in the [plan](plan.json).

The source distinguishes base preparation from the later urea addition. The
previous flattened record put the base's pH-adjustment instruction after the
receiving recipe's instruction not to adjust pH. This was a preparation-stage
error, not a conflict to resolve by selecting a different pH value.

## Applied Changes

- Relocated Peptone, Meat extract, and Agar into the explicitly linked base
  solution. Existing ingredient names, chemical identifiers, notes, and numeric
  values are preserved. Agar support remains scoped to the existing solid state.
- Added the explicit base-solution dose and its previously omitted water amount
  as separate batch-volume fields, with source snippets and conversion arithmetic.
  No measured final volume or receiving-medium dilution is inferred.
- Retained and supported the existing urea concentration; its source unit is
  already per liter and is not divided by volume again.
- Moved the two base-preparation texts verbatim into the solution's preparation
  notes. Corrected the receiving urea-addition action from `ADJUST_PH` to `MIX`,
  retaining the original description and conditional supplement text.
- Added six evidence entries supporting eight scoped changes, four source
  references, and one append-only curation event. Three recipe-level claims share
  one source-reference entry, with separate exact excerpts and field scopes.

The [follow-up result](followup.md) lists old/new fields, quantities, source
locators, exact excerpts, and decisions. The original first-pass report keeps
its historical rows and one `- Record:` target line, with a link to this repair.
Explicit hash-linked successor verification prevents later edits from being
silently mistaken for the original batch output.

## Remaining Scope

The source's manganese sporulation supplement remains conditional prose. It was
not made a mandatory ingredient or silently converted into a new variant.
Variant-specific modeling remains open. Chemical identity mappings were preserved,
not newly validated; no growth association or optimal-growth claim was added.

This repair does not fix the other receiving-media stock/variant conflicts,
the remaining source-review queue, or the broader merger's evidence-loss behavior.
The [current coverage snapshot](../20261007-followup-coverage-after-dsmz2.json)
still contains 10,631 normalized records outside the follow-up reports, plus
unresolved claims within reported records.

## Verification

- Baseline single-record open/closed-schema checks passed. Post-edit open-schema
  validation passed; full strict validation scanned 15,910 records without errors.
- The ID gate passed for all 15,910 records; no IDs were added or changed.
- 283 selected regression tests passed, covering this repair, stale/source/plan
  guards, medium/solution evidence batches, record I/O, and merge/freshness behavior.
- Exact source read-back verified all eight excerpts/scopes and six persisted
  evidence entries. Reapplying the repair changed zero records.
- The 500-record medium-batch read-back still verifies all hashes and 907 original
  snippets, with this one explicit successor. Historical unsupported fields are
  checked against the pinned pre-repair snapshot, not mistaken for current fields.
- An [independent semantic diff](../20261007-diff-audit-after-dsmz2.json) explicitly
  inverts the structural/preparation changes and proves unrelated fields unchanged.
- The [actual maintained-merger check](merge-retention.json) retains ingredients,
  stock composition/dose, preparation steps, evidence, and references for this
  record. Its current fingerprint group contains this record alone. This is not
  a passing assertion about the separate groups that lost evidence in the prior audit.
- Repeating the [prior 160-record retention audit](../20261007-mediadive-media-0000-0500/merge-retention-after-dsmz2.json)
  still finds 119 records with evidence loss and 112 with missing bibliography
  entries. Only 230 of those 907 claims survive; this remains an unresolved failure.
- Full merge verification remains failing with 1,247 name conflicts and 3,286
  fingerprint issues. Freshness also exits 1: 3,723 only-tracked, 3,865 only-generated,
  1,487 changed, and 1,110 unchanged records. See [validation.json](validation.json).
- Product validation exited 2 because `oaklib` is unavailable; reference validation
  exited 2 because `linkml-reference-validator` could not be spawned. Neither is
  counted as a passing check.
- Ruff, Black, and `git diff --check` passed.

Checks used the isolated Python 3.11 runtime, not a maintained Python 3.13/CI run.
No generated recipes were copied into the worktree. Changes remain uncommitted.

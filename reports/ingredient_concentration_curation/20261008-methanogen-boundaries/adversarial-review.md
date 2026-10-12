# Adversarial Self-Review

This is a local self-review with independent audit logic and mutation tests,
not approval from a separate reviewer or a GitHub review. No GitHub issues were
created by this cohort.

## Corrected Findings

1. **Stock constituents were asserted as direct-medium ingredients.** The
   source graph places vitamins, FeCl2, trace elements and Wolfe/mineral
   components in separate preparations. The applied plan restores those
   boundaries and checks all original nodes, including the three J265 entries
   whose old quantities summed main and stock concentrations. Tests reject
   missing/extra stocks, moved amounts, altered chemical annotations and
   unexpected root assertions.
2. **Liquid additions were represented as mass concentrations.** The repaired
   stock doses distinguish batch inputs in liters from additions explicitly
   prescribed per liter. Tests reject substituting ML_PER_L for an absolute
   batch dose. Percentage labels do not establish a w/v or v/v basis.
3. **Preparation scope could change the formulation.** J985's distribution
   step no longer asserts autoclaving of the combined preparation. J265's
   mineral-stock pH instructions no longer appear as a final-medium adjustment.
   The independent audit checks exact preparation descriptions and history.
4. **Initial mutator/report audit gaps.** The first preview stripped leading
   whitespace from prior notes, omitted ingredient names in its table, and
   described preparation edits only generically in curation history. These
   were fixed before application. Prior note text now survives verbatim;
   history includes exact changed fields and references. The initial plan is
   retained as an unapplied artifact.
5. **Batch writes needed drift resistance.** The writer rechecks the complete
   baseline, stable ID, reviewed commit, exact tracked path, capture hashes,
   source graph and proposed result. Tests cover read-only preview, no-op
   reapplication, forged plans, symlink targets and an edit to the last target
   that must prevent writes to every target.

## Open Findings

- **Unestablished quantities remain unasserted.** Batch mass does not prove a
  final concentration. Source-declared stock `g_l` values are explicitly
  qualified as provider assertions, not measured final volumes. Three legacy
  TOGO gas placeholders remain unsupported and unchanged. Unknown percentage
  bases and normality/density conversions are not filled with estimates.
- **J985 trimethylamine source disagreement remains unresolved.** MediaDive
  states 30% and TOGO states 3%; the original JCM985 recipe is unavailable.
  Both source versions remain represented in the claim explanation, with no
  selected numeric strength and no assertion that the media are equivalent.
- **Reference-validation integration remains failed.** All 103 attached
  snippets match pinned official-source captures; the installed matcher passes
  102 and fails on one HTML table row. Complete validation additionally reports
  four API-title mismatches across the three records. A source-aware metadata
  and table-extraction fix must validate actual source semantics, not replace
  titles by URLs or rewrite quotes just to make a gate pass.
- **Merged publication is not finished.** Runtime formulation-aware merging
  preserves every reviewed assertion in these three actual groups, but it does
  not update the tracked canonical merges. The corpus freshness and legacy
  merge-verifier results remain separate gates in `validation.json`.
- **Full-corpus scientific coverage is incomplete.** The six next-source
  captures and 185-slot claim map are triage only. A report count, valid schema,
  or passing test does not turn unsupported claims into reviewed evidence.

The applied [independent audit](applied-audit.json), [plan](plan.json),
[reference results](reference-validation.json) and
[merge-retention result](merge-retention.json) preserve the evidence for these
decisions. The 56 repair tests include deliberately wrong values, fabricated
snippets, missing claim coverage, changed history and incompatible dose units.

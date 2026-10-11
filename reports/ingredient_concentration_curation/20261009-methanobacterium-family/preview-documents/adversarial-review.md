# Medium-119 Preview Adversarial Review

This is a local review of an unapplied proposal, not a completed batch or a
published PR review. Source disagreements remain open in
`issue-source-conflicts.md`.

## Checks and Findings

- Independently project each source's quantities and stages, rather than
  comparing the builder to itself: all nineteen previews pass. There are 650
  source/input nodes, 633 old quantity slots and 3,095 evidence-linked claims.
- Test every source/input node against a deliberately invented concentration.
  Test omitted/extra nodes, invented ontology annotations, unsupported quotes,
  duplicate evidence, rewritten history, removed claims/lineage, wrong titles,
  fabricated publication years, incorrect old values and changed source identity.
- Test reciprocal exact-path family references, independent stock strengths and
  doses, final-volume restrictions, source-specific rates and preserved nulls.
- Exercise the guarded writer in a temporary repository, including an unchanged
  no-op and a concurrent modification to the last record before any writes.
- Initial dedicated test run: **931 passed, one failed**, 216.29 seconds. The
  failed expectation capitalized KOMODO 119_3468's literal `methanol` label as
  `Methanol`; the frozen source and proposed YAML correctly use lowercase. The
  test expectation is corrected without changing the scientific proposal.
  The terminal `focused.json` rerun passes **1,187 tests** in 298.45 seconds,
  including all 932 dedicated medium-119 tests and the reference-validator tests.
  Two dependency deprecation warnings remain. This is not the whole fast tier.
- `baseline-final.json` passes all **38 baseline commands** with current code/test
  hashes; `cached.json` passes all **904 reference checks** against the 23
  hash-checked captures. `audit.json` independently accounts for all source nodes,
  old quantity slots, evidence entries and append-only history.

## Remaining Before Application

Read terminal baseline, focused and reference receipts; verify their data/code
dependencies, source hashes, schema validity and claim coverage. Inspect the
rendered YAML changes for presentation churn and the relationship explanations
for complete claim support. Any further correction requires a new preview, not
overwriting this frozen plan. Apply all nineteen through the guarded writer only
after those checks pass, then run readback/no-op, corpus gates, indexes, merge
retention and freshness, fast tests and cumulative accounting. No recipe edits,
growth associations, commits, PRs or merges have been made by this batch.

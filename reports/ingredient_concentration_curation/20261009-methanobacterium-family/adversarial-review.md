# Medium-119 Adversarial Review

This is a local review of the now-applied repair, not a published PR review.
Terminal batch verification is in `validation.json`. Source disagreements remain open in
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

## Applied Follow-Up

`apply.json` records nineteen writes, nineteen exact readbacks, and zero changes
on the no-op rerun. Independent preview and applied audits agree. The whole
corpus inventory proves that only these nineteen YAML records changed in this
batch. `presentation.json` verifies 179 unchanged root spans and 150 historical
event spans byte-for-byte. The original four preview documents are archived
without changing the preview validation's historical hash dependencies.

All 57 individual post-edit commands and corpus strict/ID/product checks pass.
Runtime merge-retention checks preserve all nineteen records' claims. Index
reconciliation refreshed five files, with metadata changes confined to seventeen
of the nineteen repaired IDs. Cumulative reconciliation and canonical-report
linking are complete. The fast tier passes **11,100 tests**, with 16 skipped,
1,945 deselected and two dependency warnings, in 2,119.51 seconds. Final QA
passes all 32 checks including 55 registry tests. The terminal receipt verifies
the current corpus, frozen proposal, source receipts, prior-document archives,
applied ledgers and next-candidate handoff hashes. The existing partial locked
environment is not clean CI or full-suite validation.

Global merge verification retains 1,247 name conflicts and 3,287 fingerprint
issues; freshness retains 4,275 tracked-only, 8,732 fresh-only and 2,045 changed
files. These are unresolved failures, not overridden by local passes.
No growth associations,
commits, PRs or merges have been made by this batch.

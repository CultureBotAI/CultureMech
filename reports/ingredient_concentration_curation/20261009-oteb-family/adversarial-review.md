# OTEB Adversarial Review

The current artifact is an applied six-record repair. Review challenges
scientific scope and evidence preservation, not just schema compatibility.

## Independent Checks

The independent auditor reparses pinned source captures and projects the
expected rows, quantities and stage boundaries without importing the repair
builder. It checks all 115 old quantity fields, 127 output nodes, exact
per-source identities, retained annotations, reciprocal family links,
reference metadata and append-only history. It also rejects changed prior
supported evidence. The independent baseline audit passes.

The tests deliberately mutate each source node's quantity and recompute its
serialized hash. A matching hash cannot substitute for agreement with the
source. Additional mutations cover omitted/extra ingredients, invented
grounding, false snippets, duplicate evidence, rewritten history, missing
claims or lineage, false source titles/years and changed stable IDs.

Domain checks cover both maltose rows, separate calf and fetal serum entries,
provider nulls, conflicting thiamine aliases, no guessed final-volume or
percentage basis, correct stock input identity, exact preservation of fifteen
prior evidence entries, and retention of source formulations through runtime
merging. Guard tests cover apply/readback/no-op, concurrent edits and symlinks
in a temporary fixture, not the authoritative corpus.

## Current Outcomes

The preview's 180 capture-backed reference checks and independent six-record
projection pass. All 495 focused tests, twelve preview schema/strict commands,
lint, formatting and whitespace checks pass. Presentation checks preserve
48 unchanged metadata spans and 45 old history entries. Fifteen prior supported
evidence entries are preserved exactly. Actual application, readback and no-op
also pass, as do all eighteen per-record checks and corpus strict/ID/product
checks. Runtime merge retention passes for four medium-shaped records; the two
standalone solutions remain excluded.

The shared cumulative auditor now registers only the applied OTEB plan. Ten
targeted registry checks pass, including recomputed-hash attacks on quantity,
snippet and earlier history. Its initial quantity test incorrectly assumed
the first ingredient had an amount; it now selects an explicitly quantified
ingredient. No recipe or source evidence changed to fix that test. Broader
QA passes all 91 tests; the fast tier passes 11,972, with 16 skipped and
1,970 deselected. Their terminal receipts are pinned in `validation.json`.

No original ambiguity is settled by a green automated check. Final-volume,
serum and duplicate-row uncertainties remain in the applied YAML and local issue.
Global merge verification and freshness remain failing. This batch's tests
do not constitute clean CI or the complete suite.

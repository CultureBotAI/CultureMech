# Applied J And Dasycladales Ingredient Review

Applied locally on 2026-10-10. The all-record objective remains incomplete.
Historical [source previews](../20261010-utex-j-das-preview/README.md) are excluded
from canonical coverage; only their applied successor reports are counted.

## Changes

- Exactly two authoritative records changed; permanent IDs and previous history
  preserved. [Application](apply.json), exact readback and repeat no-op pass.
- Fifty evidence entries, seven new references and eight enriched bibliography
  entries. Changed claims carry source URLs, snippets and scoped explanations in
  the YAML. Unknown DOI, authors and publication year are not manufactured.
- Four DAS supplement doses retain their numbers with an explicit starting-seawater
  basis. Seven unsupported carrier/water fractions are removed without invented
  replacements. The final-volume conflict remains unresolved.
- Two prepared DAS stocks are separated from pure chemical composition, with two
  source-explicit component-stock strengths. Two supplied vitamin salt forms are
  corrected; unsupported anhydrous phosphate mappings are removed.
- J's optional agar formulation becomes a variant. Two [canonical reports](records/)
  cover all 47 original/new claim rows. No taxa-media associations are added.

At this batch's checkpoint, the [cumulative audit](cumulative.json) verifies **5,418 edited records, 38,252
added evidence entries and 1,844 quantity corrections**. Basis corrections,
removed slots and added strengths are counted separately. Follow-up coverage is
**11,946 / 15,910**, leaving **3,964 outside coverage**; this is not scientific
certification of every concentration.

## Verification

- [Preview](preview.json): four baseline schema/strict commands, 115 tests, Ruff
  and Black pass; one unavailable Koza integration module is skipped.
- [Post-edit](post.json): four actual schema/strict commands, 245 regression tests
  and `git diff --check` pass.
- [Source recheck](source-validation-v2.json): forty retained fields, 45 captured
  snippets and five manual identity-ledger entries checked; forty altered amounts
  and twelve altered bases rejected. Eight actual/proposed schema commands pass.
  The first runner stopped on an existing preview-log filename without overwriting
  it; v2 uses separate logs.
- [Indexes](index-comparison.json): fourteen comparisons, no semantic changes or
  writes. [Runtime retention](runtime-retention.json) preserves both records'
  ingredients, stocks, evidence, references and variants; persisted merges remain
  unregenerated.
- The applied [consumer fix](../20261010-volume-basis-consumers/README.md) retains
  94 quantity cells and fifteen basis cells across seventeen rendered records.
  [Installed-wheel checks](wheel.json) pass for the CLI, renderer, template hashes,
  qualified dose, nested stock and packaged MIM resource.
- [Live references](references-live.json): J passes 22 snippets and four titles.
  DAS aborts on a supplier timeout without per-claim output. Earlier sandbox
  commands fail DNS; aborted checks are not passes.
- [Generated web output](web.json): browser export, page generation and coverage
  checks pass for all 15,910 normalized records. The outputs are local previews,
  not published artifacts. Composition graphs are unavailable and marked degraded.
  Browser visual inspection was unavailable because no browser surface was enabled.
- [Corpus](corpus.json): strict, ID, product and MIM-index gates pass. Merge
  verification and freshness fail, with 15,056 derivation differences (2,045
  changed, 4,275 only in tracked output and 8,736 only in a fresh derivation).
- [Full tests](full.json) finished: 19,215 passed, nineteen skipped and two
  warnings in 8,757.08 seconds. Assertions pass, but the command exits 1 because
  four tests exceed the 120-second call budget. The [terminal checkpoint](applied-checkpoint.json)
  pins the exact tested code and corpus; it is not an all-gates pass and does not
  cover the subsequent eighteen-record batch or nested-stock export patch.

## Open Issues

DAS final-volume and B12 sterilization conflicts, unresolved phosphate hydrate
identity and supplier-access limits remain explicit. Printed molarity annotations
and unrelated growth/culture-condition claims are not independently certified.
Outstanding repository-wide gates prevent publication readiness. The later
[eighteen-record follow-up](../20261010-next-utex-applied/README.md), including
the seven soil/seawater proposals, is now applied and has its own verification
receipts and updated cumulative totals.
No commit, push, PR, merge or branch deletion is claimed.

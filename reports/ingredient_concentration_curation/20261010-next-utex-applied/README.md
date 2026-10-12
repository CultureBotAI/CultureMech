# Applied UTEX Concentration Follow-Up

This is the eighteen-record historical checkpoint. A later
[three-record Volvocacean/BG-11 batch](../20261010-utex-volvocacean-bg11/README.md)
is now applied; consult its terminal receipts for successor totals and gates.

Applied locally on 2026-10-10. The all-record objective is **not complete**.
The [terminal checkpoint](applied-checkpoint.json) pins the final local state;
the [local issues](ISSUES.md) distinguish unresolved gates from successful checks.
No commit, push, PR, merge or branch deletion is claimed.

## Records And Evidence

| Batch | Edited records | Claim rows | Added evidence |
| --- | ---: | ---: | ---: |
| [Soil/seawater](../20261010-utex-soil-seawater/README.md) | 7 | 29 | 35 |
| [Organic media](../20261010-utex-organic-five/README.md) | 5 | 26 | 26 |
| [Prepared blends](../20261010-utex-six-blends/README.md) | 6 | 12 | 8 |
| Total | 18 | 67 | 69 |

The [guarded application](apply.json) changes exactly eighteen normalized paths,
with exact readback and repeat no-op. Fourteen unsupported quantity slots are
removed without replacement guesses, twelve retained doses gain explicit volume
bases, and nine optional formulations are represented as variants. Forty-four
structured quantities retain their numeric values and units. Previous history,
permanent IDs and unrelated assertions are preserved.

Changed claims carry persistent source URLs, literal excerpts and scoped
explanations in YAML. Bibliography entries retain source titles, source type,
discovery mode and access date. DOI, authors and year remain unknown where not
established. No taxa-media associations are added.

The [cumulative audit](cumulative.json) verifies **5,436 edited records, 38,321
added evidence entries and 1,844 quantity corrections**. Basis corrections and
removed slots are counted separately. [Canonical follow-up coverage](followup-coverage.json)
is **11,964 / 15,910**, leaving **3,946 outside coverage**. Historical structural
audit reports already exist for the corpus; neither report presence nor these
follow-up totals certify every concentration scientifically.

## Verification

- [Pre-apply](preview.json): real-schema dry runs for all eighteen records,
  369 installed-code tests, Ruff and Black pass; one Koza module is skipped.
- [Post-edit](post.json): all 36 actual schema/strict commands, 357 regression
  tests and `git diff --check` pass. [Eighteen canonical reports](reports.json)
  have exactly one exact `- Record:` entry each and cover all 67 claim rows.
- [Independent source readback](source-readback-applied.json) checks all 44
  retained quantities, nine optional variants and 69 evidence entries against
  the pinned source projections. Source-validation mutation tests remain linked
  from the three original proposal packets.
- [Installed references](references.json): fourteen commands pass; four fail
  only on HTML-encoded apostrophes in titles. All 69 snippet checks pass; the
  total is 86 valid and four invalid checks. The unchanged proposals separately
  passed [ninety fresh-source checks](../20261010-utex-reference-parser-preview/v3/live-reference-preview-network.json)
  with the isolated strict parser. That parser is still **not installed**;
  the two validation results are not interchangeable.
- [Consumer checks](consumers-v2.json): eighteen rendered pages retain 44
  quantity cells, twelve bases and nine variants. Fourteen records preserve
  ingredients, stocks, evidence, references, variants and existing history through
  singleton merging. Four prepared blends are excluded by the ingredient-based
  matcher both before and after curation. The first checker incorrectly required
  all eighteen to merge; [that failure](consumers-attempt-01.json) is retained.
- [Indexes](indexes-applied.json): three regenerated files contain only the
  expected ingredient-count changes for five carbonate variants, plus generated
  timestamps. Eleven semantically unchanged indexes are not rewritten.
- The [KGX fix](../20261010-kgx-nested-stock-review/README.md) is installed:
  recursive inline stocks, basis/composition-sensitive stock identities and
  stock-ingredient publications are retained. Actual DAS output includes both
  child nodes and their 25%/75% links. [Fresh installed-wheel checks](wheel-v2.json)
  pass for the CLI, nested edges, qualifiers, references and packaged MIM data.
  The first wheel attempt used a Python without build dependencies; v2 explicitly
  selects the maintained environment and preserves the [failed attempt](wheel.json).
- [Corpus gates](corpus.json): strict validation, permanent IDs, product labels
  and the MIM index pass. Merge verification and freshness fail. The fresh
  derivation has 10,781 records versus 6,320 tracked, with 15,056 differences:
  2,045 changed, 4,275 only in tracked output and 8,736 only in fresh output.
  The total matches the preceding checkpoint; this is not proof of equal
  contents. Persisted merged YAML was not broadly regenerated.

The preceding frozen [full suite](../20261010-utex-j-das/full.json) has 19,215
passed, nineteen skipped and two warnings, but exits 1 for four tests over the
120-second runtime budget. It predates this packet and has **not** been rerun
after these code and record changes. Targeted passing tests are not a current
full-suite pass.

## Remaining Limits

The Erdschreiber quarter-strength table/prose ratio conflict, source final-volume
ambiguities and printed-molarity limitations remain explicit. Linked parent
composition and unrelated chemical identity, organism, growth, role, salinity
and culture-condition assertions are not newly certified. Four prepared blends
remain unmergeable by the ingredient-based matcher.

Composition graphs and Koza TSV integration are unavailable; page checks inspect
HTML content, not browser screenshots. The broader UTEX parser compatibility
issues, full-suite runtime failures and publication restrictions remain open.
Eight additional source reviews are read-only previews, not added canonical
coverage. Forty-five of the 64 captured UTEX records remain source-preparation
only. Git/GitHub publication operations were previously denied and not retried.

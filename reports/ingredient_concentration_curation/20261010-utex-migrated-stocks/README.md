# Migrated UTEX Stock Evidence Review

Applied locally to Beijerinck's Solution, Bold Trace Stock and Boron Stock.
This batch does not complete the all-record concentration goal and is not
publication-ready.

## Changes

- Thirteen new evidence entries: nine supported amount claims, one partial
  manganese claim and three stock/receiving-medium context claims.
- Three existing bibliography entries enriched with institutional source and
  discovery metadata; no named author, year or DOI is invented.
- Three context notes corrected, with one appended history event per record.
- All ten structured concentrations and chemical identities retained. No numeric
  replacement, assumed working dilution or taxa-media association is added.

The source's manganese formula remains in conflict with the assigned identity.
Contradictory source concentration annotations are recorded explicitly; they
are not silently converted into stock molarities or receiving-medium doses.

## Results

The [scientific preview](../20261010-utex-migrated-stock-preview/README.md)
checks every existing concentration claim against captured official recipe
content. The [application receipt](apply.json) records three changed paths,
successful readback and a repeat no-op. The [three canonical reports](records/)
cover all ten claims: nine supported and one held.

The [cumulative audit](cumulative.json) verifies 5,409 edited records,
38,145 new evidence entries and 1,844 quantity corrections. The
[coverage snapshot](followup-coverage.json) records 11,937 canonical follow-up
targets out of 15,910 normalized records, leaving 3,973 outside follow-up
coverage. Report presence does not mean all claims are resolved.

## Validation

- [Preview](preview.json): twelve baseline/proposed schema/strict passes,
  43 guard tests, lint and formatting pass.
- [Post-edit checks](post.json): six actual schema/strict passes, 190 regression
  tests and diff whitespace check pass.
- [Indexes](indexes.json): fourteen semantic comparisons unchanged; all three
  standalone stocks are correctly excluded from medium merging.
- [Live references](references.json): all thirteen snippets pass, but all three
  bibliography title checks fail on page-title suffix/entity differences.
  Successful orchestration does not make the reference gate a pass.
- [Corpus checks](corpus.json): strict schema, IDs, products and the MIM snapshot
  pass; product validation retains 91 warnings and 96,008 no-adapter skips.
  Merge verification fails with 1,247 name conflicts and 3,287 fingerprint
  issues. Freshness fails with 15,056 derivation differences.
- [Fast tier](fast.json): 15,565 passed, sixteen skipped, 3,498 deselected and
  two dependency deprecation warnings in 43:57. This is not a full-suite pass.

All scheduled validation commands are terminal. The
[checkpoint](applied-checkpoint.json) verifies unchanged hashes for all 15,910
normalized records and the tested code, and preserves the failed reference and
merge gates separately from successful test execution. See the
[issue dispositions](issues.md) for retained limitations. These are local
artifacts, not evidence of a commit, push, PR or merge.

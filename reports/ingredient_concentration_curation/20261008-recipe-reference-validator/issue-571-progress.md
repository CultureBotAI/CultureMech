Local implementation and verification are complete for this reference-parser
repair, but the changes are **not committed or published yet**. Please keep this
issue open until the fix ships.

- Added literal JCM/TOGO/MediaDive recipe handling through the existing LinkML
  traversal. It checks accession identity, preserves chemical notation and
  bracketed accessions, extracts API titles from metadata, and uses a separate
  integrity-checked raw cache. Other providers retain upstream behavior.
- Freshly fetched all 13 official responses used by the seven-record nested
  trace-stock cohort; every raw hash matched its frozen capture.
- The stricter checks exposed two excerpts ending mid-word at `solution`
  inside `solutions`. Expanded those quotations with exact source text and
  append-only curation events. No ingredient, quantity, unit or scope changed.
- All seven actual `just validate-references` commands now pass: **206 excerpt
  checks and 19 title checks**, including the original failing cases.
- **225 final focused tests pass**, including altered amounts, units, decimal
  commas, Unicode signs, hydrate digits, titles, accessions, malformed sources,
  corrupt caches, redirects, concurrent edits and rehashed forged repair data.
  Lint, formatting, schema/strict baselines and post-edit checks pass.

The full suite completed with 10,179 passed, 19 skipped and two concentration
history-test failures. Those reproduced independently of the reference adapter;
their applied-repair list was stale. The fix shares the cumulative audit registry
and independently audits the repair chain; all ten relevant tests pass afterward.
This is not described as a clean full-suite rerun or clean CI environment.

Reports are local under
`reports/ingredient_concentration_curation/20261008-recipe-reference-validator/`.
The seven-record success does not certify the whole corpus: earlier J151/M142
bibliographies still have descriptive rather than actual source titles, the
91-record dependency queue remains open, and global merge verification still
reports 1,247 name conflicts and 3,287 fingerprint issues. The all-record
concentration goal and PR/merge workflow remain unfinished.

# Local Issue Draft: KOMODO Detail-Page Reference Validation

Not submitted to GitHub. This is a validator integration finding, not a reason
to weaken supported source quotations or change recipe amounts.

## Local Resolution

The [KOMODO parser repair](../20261008-komodo-reference-validation/README.md)
resolves the table/pH matching finding: all 31 previously failing quotations
and all 86 cohort checks now pass without changing YAML. All four reference
CLI commands pass against refreshed, hash-verified captures. The regression
suite includes real base/variant pages and malformed/identity/amount cases.

The requests refresh still encountered HTTP 403; a separately recorded urllib
public capture returned HTTP 200 and identical content. Retrieval failures
remain explicit, not silently waived or claimed fixed. The evidence and
required-fix description below are retained as the original finding.

## Evidence

- `live.json`: five freshly retrieved official sources match their inspected
  capture hashes. The generic fallback nevertheless reports 37 fetch failures
  among 86 snippet/title checks (49 pass).
- Sandboxed `post.json` reference commands encounter DNS restrictions for
  KOMODO. These environmental errors are distinct from scientific mismatches.
- `applied-live.json`: an approved retry fetches the detail pages and passes
  55 of 86 checks. Thirty-one fail on quotations crossing table-cell boundaries,
  including ingredient rows and `PH Info` pairs. The source bytes are unchanged.
- `audit.py`: independently parses both actual tables, preserves row labels,
  chemical forms, displayed amounts and source identity, and checks all 201
  cohort excerpts literally. The original PDF page image was also inspected.
- `komodo-parser-diagnostic.json`: the generic cache contains raw HTML matching
  the inspected source. All 31 failed quotes are interrupted by HTML tags in
  that representation; every unchanged quote matches table-aware rendered
  text. The installed `URLSource.fetch()` explicitly returns HTML without
  parsing it. This is reproduced behavior, not an inferred source conflict.

The affected public URLs are the inspected `MediaInfo=1021` and
`MediaInfo=1021_16929` detail pages recorded in `context.json`. The current
`recipe_source()` dispatcher at the time of these failing receipts did not
recognize this official recipe endpoint and delegated to the generic extractor.

## Required Fix

Add narrowly scoped official-source handling after validating allowed
host/path/query forms, accession identity and actual table headings. Preserve
formula characters, decimal precision, signs, nulls and neighboring cell
boundaries. Do not permit arbitrary URLs, silent redirects, login/challenge
pages, or a row from another medium to satisfy a claim.

Add regression fixtures for base and strain-variant pages, malformed/duplicate
rows, wrong accession, missing or nonrecipe tables, and literal amount/chemical
form mismatches. Rerun the unchanged YAML evidence checks and broader recipe
reference tests. Retain historical failing receipts and report actual results.

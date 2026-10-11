# Adversarial Review

## Defect Resolved

NBRC 1219's original HTML contains the water ingredient, value and unit in
separate cells. The generic reference cache retained those tags. Searching that
raw content failed for the actual contiguous rendered excerpt. The earlier
failure was not a reason to alter the quote or substitute TOGO's conflicting
amount. The new parser uses the accession-checked composition table and passes
the original excerpt without changing any YAML bytes.

## Negative Checks

- Wrong or missing accession/name, unexpected title, duplicate identity or
  composition sections, misplaced/nested/empty tables and ambiguous rows fail.
- Declared hidden content is rejected at ancestor, table, composition and
  ingredient levels. Script/style/template content and unrelated page text
  cannot supply an otherwise missing recipe quotation.
- Altered units, decimals, signs, precision, chemical forms and hydrate digits
  do not match. Existing literal-matcher boundary tests remain in the suite.
- HTTP errors and redirects do not produce a generic fallback or successful
  cache entry. The real live retrieval returned the original unchanged HTML.
- Existing provider, title, cache-integrity and nested-evidence tests pass.

No unresolved defect was found in this reviewed scope. The source parser is
not a scientific entailment engine or browser/CSS renderer. It verifies literal
text in a structurally identified recipe, not every use of a quoted quantity.
Uninspected NBRC layouts remain an explicit coverage limitation.

## Broader Gaps

The corpus inventory found 188 exact NBRC reference URLs but only one explicit
snippet-bearing reference entry. This repair does not supply evidence for the
other references. It does not resolve M1946's source-version conflict, the
eleven linked Middlebrook formulations, earlier PDF bibliography title gaps,
global generated-merge failures or publication. Those remain in the full goal.

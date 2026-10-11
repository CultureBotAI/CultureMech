# Adversarial Self-Review

This is local self-review, not independent PR approval.

## Addressed

- An official host alone does not establish recipe identity. The dispatcher
  accepts only the known HTTPS detail paths, one `MediaInfo` query and supported
  accession forms. The returned ID and medium heading must agree exactly.
- A valid page title does not make a catalog, challenge or unrelated table a
  recipe. The feature and ingredient table shapes, single occurrence and
  provider's amount-basis sentence are required.
- Repeated `Table0` HTML IDs are not treated as unique selectors. Recipe table
  headers distinguish the ingredient table from the separate SEED totals.
- Cell boundaries are preserved without splitting inline formula digits.
  Nulls do not become zero; displayed decimals do not become approximate or
  calculated values. Wrong signs, hydrates and hydrolysate names do not match.
- Duplicate ingredient names, conflicting duplicates, duplicate metadata,
  missing/extra cells, row/column spans and hidden content fail closed.
- Literal matching is limited to the recipe section. Calculated ion totals,
  scripts and unrelated footer text cannot satisfy ingredient quotations.
- Failures do not delegate to fuzzy or generic matching. Redirect and HTTP
  failures are retained, not silently converted into source passes.
- Immutable real base/variant HTML fixtures and 31 actual failed checks prove
  the parser change repairs the observed fault without editing YAML snippets.
- Full-corpus byte inventories before/after checks prevent a validation repair
  from silently changing ingredient data. Per-record hashes match the applied
  hydrolysate plan.

## Residual Limits

The fresh requests transport encountered HTTP 403. An explicit separate urllib
capture succeeded with unchanged source bytes; both outcomes are preserved.
The first direct-capture helper rejected a missing Content-Type header before
writing cache entries. Its retry records the absent header and requires exact
source bytes and recipe identity instead of inventing a MIME assertion.

Parser scope is intentionally source-specific, not a claim that every future
KOMODO page shape will be accepted. Supported accession parsing alone does not
prove that an accession exists or that the old no-prefix URL avoids redirects.
Tables with unrecognized structure remain errors requiring inspection.

Passing occurrence checks does not establish ingredient identity, density,
percentage basis, dose, final volume, stock dilution or organism growth. The
remaining Middlebrook records still require full source-specific review and
guarded, evidence-backed edits. Global merge/freshness and publication remain
unresolved; local issue drafts were not submitted externally.

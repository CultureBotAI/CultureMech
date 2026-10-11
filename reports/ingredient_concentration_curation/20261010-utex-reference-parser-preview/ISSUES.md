# Deferred UTEX Reference-Parser Issues

These are local review findings, not filed GitHub issues. The parser is uninstalled.

## P1: Existing Stock Layouts Rejected

The [existing-record impact check](v3/existing-record-impact.json) found legitimate
captured pages outside the parser's currently supported structure. Examples include
prose-only BBM stocks, variant concentration headers, case-different canonical
URLs, malformed/variable table shapes and recipe ancestry in the captured HTML.
Eleven captured instances across ten source URLs fail parsing. Missing usable
captures leave 102 snippets and 26 titles unassessed; these are not evidence failures.

Disposition: do not install v3. Extend layout handling only after inspecting each
source, preserve exact source identity and table boundaries, and add representative
positive and adversarial tests. Do not weaken literal matching or silently fall back
after a recognized-source structural failure. Recheck all existing UTEX references.

## P2: Existing Excerpts And Titles Need Review

Against available accepted captures, 32 snippets and ten titles across fourteen
existing records would fail the strict parser. Context inspection identifies
28 extraction-spaced water-formula excerpts and four excerpts missing the
sentence-ending period required by the strict token-boundary matcher. Adding
that existing source period is an excerpt-boundary correction, not an amount
change. Ten titles are valid exact base titles without the UTEX site suffix;
they need parser compatibility handling, not automatic bibliography rewriting.
The [read-only dispositions](v3/existing-text-dispositions.json) verify all proposed
literal excerpts against each captured source version. A failed literal match
alone is not an amount error.

Disposition: keep the existing records unchanged during the frozen full run.
Inspect exact source text and affected record context, then use a separate guarded,
append-only evidence follow-up for the four affected F/2 records. Preserve the
valid short titles; accept only the exact known site-suffix variation in future
parser work. Do not change concentrations merely to
satisfy the new validator or rewrite earlier curation history.

## Resolved Within The Pending Proposals

The eighteen pending recipes have five corrected snippet strings. All 69 snippets
and 21 titles pass fresh-source checks with the isolated parser. This establishes
the scoped proposal reference result, not general parser compatibility. The
[v3 integration packet](../20261010-next-utex-integration-preview/v3/validation.json)
therefore excludes parser installation and leaves the installed reference gate
unchanged. Its known generic title/extraction limitations must be reported honestly.

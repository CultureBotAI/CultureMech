# UTEX Literal Reference Parser Preview

The current [v3 parser](v3/recipe_references.py) is **not installed**. It checks
the exact canonical URL, decoded page title, recipe section and five-column
recipe tables, including the inspected stock-group rows and explicit-liter
header. Chemical subscripts retain their digits. Table-layout scripts are
excluded from evidence. Matching remains literal, not fuzzy.

## Verification

- [Regression checks](v3/validation.json): 60 new tests and 544 existing reference
  tests pass, along with Ruff, Black and patch checking. Baseline failures confirm
  the new tests exercise missing behavior.
- [Captured-source checks](v3/capture-validation.json): all 73 captured layouts
  parse; the 18 current proposals have 69 matching snippets and 21 matching titles.
  Parser acceptance is not scientific review of all 73 sources.
- [Live proposal checks](v3/live-reference-preview-network.json): all 18 CLI
  commands pass, with 90 valid and zero invalid checks, using newly retrieved
  public pages. Earlier sandbox connection failures are retained separately.
- Soil/seawater v2 corrects one snippet; organic-medium v3 corrects four snippets.
  Quantities, units and volume bases are unchanged by these revisions.

The first parser rejected UTEX's embedded table-layout scripts. V2 excludes
their text; v3 additionally handles two inspected table-layout variations.
All prior receipts remain historical. A source-capture check initially required
HTTP metadata absent from the old liver-extract capture; the corrected receipt
records that gap rather than inventing metadata. The live run separately verifies
the retrieved source and its transport identity.

## Installation Limits

The [existing-record impact check](v3/existing-record-impact.json) identifies
32 snippet and ten title mismatches across fourteen existing records, plus
unsupported stock layouts and unavailable captures. These are documented in
[local issues](ISSUES.md); the parser must not be installed yet. No corpus record
or installed code was changed by this review.

The [current nine-file integration preview](../20261010-next-utex-integration-preview/v3/validation.json)
excludes this parser while retaining the exact corrected record proposals and
the separate tested KGX fix. V2's eleven-file packet is superseded. Passing the
eighteen proposals does not establish corpus-wide parser compatibility.

This is not a full-suite pass, completed all-record review or publication approval.

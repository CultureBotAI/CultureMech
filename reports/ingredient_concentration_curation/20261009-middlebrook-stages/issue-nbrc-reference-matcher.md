# NBRC Recipe Reference Matcher Gap

Status: resolved locally by the [NBRC parser repair](../20261009-nbrc-reference-validation/README.md);
not published to GitHub. Historical failure receipts are preserved.

The original recipe page
https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1219
was inspected and captured in `context.json`. Its rendered table explicitly
contains the exact text `Distilled water 900 mL`. This differs from TOGO M1946's
895 ml input and is recorded as a source-version conflict, not a replacement
of the TOGO assertion.

`live.json` records the sole automated reference failure at
`M1946 / evidence[1].snippet`: `Text part not found as substring`.
The adapters used for that receipt did not recognize NBRC catalogue URLs,
and the generic path did not match this actual table excerpt. Inspection of
the ignored generic cache confirmed it stored the raw HTML, with tags between
the ingredient, amount and unit. The identified recipe-table parser now
passes the unchanged excerpt and all 240 cohort reference checks against
fresh byte-identical original sources.

The independent captured-source audit verifies the quote after HTML text
extraction. This manual check is not an automated pass and does not verify
every other NBRC statement or all CultureMech references.

The repair adds exact host/path/accession routing, recipe-table identity,
literal numeric/unit preservation and negative tests for unrelated/hidden
page text. The original manual check remains historical; the new automated
pass is recorded separately. The source-version conflict remains unresolved,
and other NBRC references are not thereby scientifically verified.

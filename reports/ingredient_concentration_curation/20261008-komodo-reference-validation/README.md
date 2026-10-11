# KOMODO Ingredient Evidence Validation

The official-recipe validator now handles exact KOMODO detail-page URLs and
matches their ingredient tables without weakening quotations. All **86
reference checks** on the four hydrolysate records pass, including all **31
previously failing table/pH quotations**. All four `just validate-references`
commands pass using refreshed, hash-verified captures.

No normalized YAML, concentration, snippet, source reference or curation event
was changed by this validator work. Cumulative accounting remains **5,174
edited records and 33,094 added evidence entries**, with **11,786 of 15,910**
exact paths in follow-up reports and **4,124** outside them. These counts do
not establish that all claims in reported records are resolved.

## Source Handling

The parser requires the exact requested accession, matching medium heading,
one feature table, one five-column ingredient table and the provider's
per-liter statement. It preserves chemical case, subscripts, signs, displayed
precision and nulls. Duplicate/ambiguous rows, hidden content and unexpected
table shapes fail closed. It excludes the separate calculated SEED ion totals
and unrelated page content. No fuzzy matching or amount conversion is added.

This is text occurrence validation, not proof of scientific entailment,
serum density, stock scope or concentration arithmetic. Those decisions remain
in the source-specific per-record reviews.

## Actual Validation

- `focused.json`: 452 passing tests, including immutable base/variant captures,
  all 31 prior failures, identity/table corruption, quantity/formula mismatches,
  nulls, hidden content, redirects and unchanged non-KOMODO behavior. Lint,
  formatting and tracked whitespace checks pass.
- `live.json`: the three non-KOMODO sources refreshed identically, then the
  requests transport received HTTP 403 for KOMODO. This attempt remains failed.
- `direct-refresh.json`: the first direct capture stopped before caching
  because its helper expected an explicit HTML Content-Type header.
- `direct-refresh-retry.json`: both public KOMODO GETs returned HTTP 200 with
  byte-identical HTML and no Content-Type header. The receipt retains the
  missing header, actual timestamp, URL, response hash and urllib transport.
  Python's `text/plain` default is recorded, not asserted as a server header.
  Hash/identity/table checks passed before explicit cache insertion.
- `cached.json`: 86/86 checks and all four CLI commands pass against those five
  refreshed sources. K1021: 21; K1021_16929: 22; M2287: 13; DSMZ 1021: 30.
- `fast.json`: the current parser fast tier passes **9,644 tests**, with 16
  skipped, 1,945 deselected and two warnings in 799.19 seconds. This is the
  actual new run, not the historical 9,541-test hydrolysate result.
- [validation.json](validation.json): reconciles terminal checks, source hashes,
  unchanged record/evidence bytes, exact report coverage and remaining failures.

The nine captured KOMODO pages for the next Middlebrook cohort also parse.
This is parser coverage only, not completed scientific review of those records.
All 24 next candidates and their 28 captures remain separate preparation work.
The [source-inspection handoff](next-middlebrook-source-findings.md) records
the four visually checked PDF pages, source conflicts and initial findings
from the complete DSMZ 645/857/911 YAMLs. No Middlebrook edits are applied.

## Remaining Work

The requests HTTP 403 is not repaired by this change. The parser does not
silently switch transport or use the lossy generic cache after a source error.
The successful direct capture and cached validation are explicit separate
steps; fresh retrieval must continue to report actual failures.

Global merge verification still reports 1,247 name conflicts and 3,287
fingerprint issues, and generated-data freshness fails. The unchanged corpus
retains its completed strict/ID checks and product-validation limitations in
the [hydrolysate receipt](../20261008-lactalbumin-formulations/validation.json).
The all-record objective, source uncertainties and publication remain open.
No commit, push, GitHub issue submission, PR, merge or branch deletion occurred.

Runtime: existing partial locked Python 3.13 environment, not clean CI or a
complete-suite claim. The first offline test attempt had a decorator syntax
error during collection; it was corrected before the 452-test run. Historical
fetch and validation failures are not overwritten.

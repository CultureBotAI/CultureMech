# DSMZ 803, 1046 and 1065 Water Inputs

Applied locally to nine already-reported normalized records: the KOMODO medium,
MediaDive medium and linked standalone main solution for each accession. This
follow-up does not add unique reviewed or edited paths and does not complete the
all-record objective.

## Changes And Evidence

The [independent applied audit](diff-audit.json) verifies nine quantity/unit
corrections, eighteen evidence entries, nine original-PDF references, nine water
input notes and nine append-only curation events. Six medium records previously
encoded water as `1000 G_PER_L`; three solution records used `1000 PERCENT_V_V`.
All nine now encode `1 L`, with the explicit calculation `1000 ml / 1000 = 1 L`
and a note identifying this as source batch input, not measured final volume,
mass concentration, percentage or an assumed density conversion.

Each edit has a literal excerpt from the exact linked MediaDive API recipe and
a short water-row quotation from the original DSMZ PDF. The [frozen context](inspected-context.json)
contains complete before-records, API captures and metadata, PDF text and hashes,
and the original-recipe mapping. The medium APIs explicitly link solutions
1634, 2114 and 2155. These are corroborating representations from the same
provider, not independent experimental confirmations. Authors and publication
year are unstated; a copyright date is not substituted for publication year.

All non-water quantities, chemical mappings, preparation, identifiers,
relationships, prior evidence and history are preserved. The nine [supplemental
reports](records/) contain 57 concentration rows: nine corrected, 45 verified
unchanged against the source, and three unsupported legacy placeholder rows left
unchanged. Their `- Follow-up target:` lines supplement existing exact-path
reports; they do not create duplicate `- Record:` entries or inflate coverage.

## Verification

The [baseline](baseline.json) passes 34 source/write-guard tests, all nine
open-schema checks and strict validation of all 15,910 normalized records.
Actual PDF bytes and extracted pages were checked against all three captured
hashes. Preview diffs were inspected before application.

The [post-edit journal](validation.json) records successful application,
nine-record readback, no-op reapplication, independent whole-record inversion,
both schema classes, full-corpus strict validation, stable IDs and variant links.
The focused selection passes **107 tests**; it includes the 34 guard tests, so
these totals must not be added. Ruff and Black checks pass for the seven changed
Python files. `just test-fast` passes **7,673 tests**, with **16 skipped and 1,864
deselected**, in 561.39 seconds. Product validation exits successfully with
91 warnings and 96,057 entries skipped for lack of an adapter; those skipped
identifiers have not been validated. The journal is terminal, and
`git diff --check` passes.

Global merge verification **fails** with **1,247 name conflicts** and **3,287
fingerprint issues**. The [freshness audit](merge-freshness.json) also **fails**:
6,320 tracked versus 6,498 freshly generated records, 3,720 paths only in tracked
output, 3,898 only in fresh output, 1,700 changed shared paths and 900 unchanged.
Those counts match the preceding batch; the water repair does not resolve them.
The fresh run excludes 4,785 standalone solutions and skips 342 recipe inputs
(340 other errors and two without valid ingredients). It ran in a temporary
directory and did not overwrite tracked merged records.

All five affected historical cohort CLI verifications pass with explicit
successor plans. The first [historical journal](historical-readback.json)
subsequently failed a scratch report-count assertion that incorrectly assumed
backticked field labels. The failed attempt is preserved. A [separate recheck](historical-readback-recheck.json)
verifies all nine current hashes, nine supplemental reports and 57 report rows,
reusing only the five successful CLI results.

The [final source/hash/report check](final-checks.json) passes for all nine live
records and reports, six API captures, three original PDF byte/text captures
and three mapping rows. It verifies the exact cumulative delta independently;
it explicitly preserves the failed citation, global merge and freshness gates.

The [actual merger check](merge-retention.json) preserves both full evidence
entries, the corrected amount, input note, PDF reference and curation event for
all six media. The three standalone solutions are excluded from medium merge
groups as expected. This scoped pass does not resolve earlier merge evidence
losses or establish that all members of a fingerprint group are exact variants.

The [reference retry](reference-validation-recheck.json) is terminal but **not a
full citation-validation pass**. Nine API snippets pass the installed matcher;
nine PDF snippets fail its text retrieval. The PDF quotations were separately
checked against the actual PDF text and hashes. Full citation checks report
27 issues: nine API title fallbacks, nine PDF title fallbacks and nine unmatched
PDF snippets. The restricted-network first attempt is retained separately in
[reference-validation.json](reference-validation.json). No fabricated title or
injected cache was used to produce a pass.

The runtime is the partial locked Python 3.13 environment, not full CI. Consult
[adversarial-review.md](adversarial-review.md) for unresolved scope and publication
gates. Generated merged records and pages have not been hand-edited. No commit,
push, PR, merge or branch deletion is claimed for this batch.

## Cumulative Status

The [cumulative independent audit](../20261008-diff-audit-after-water-803.json)
verifies **5,067 distinct edited records, 30,033 new evidence entries, 5,344 new
references, 5,262 appended events and 1,365 quantity corrections**. Evidence
entries include identity and preparation claims, not just concentration claims.
The [coverage snapshot](../20261008-followup-coverage-after-water-803.json) covers
**11,110 of 15,910 normalized paths**, leaving **4,800** outside these follow-up
reports. Reported records also contain unresolved claims. No taxa-media growth
associations were added.

# KOMODO Concentration Follow-Up: Paths 3000-3632

This batch reports 633 exact normalized paths from the frozen KOMODO inventory.
It is an evidence-only source pass, not completion of concentration curation for
these records or the full corpus.

## Applied Scope

- 38 records receive 226 concentration-evidence entries and 38 identity-only
  mapping entries, plus 76 references and 38 append-only curation events.
- 595 records remain unchanged. Existing quantities, units, ingredient lists,
  organism associations, physical states and previous history are preserved.
- All 633 records have one exact-path report under [records](records), including
  unchanged and inaccessible-source cases. The plan contains 226 evidence-only,
  5,112 conflict and 8,183 unsupported rows. Rows also cover preparation and
  relationship context; these are not interchangeable with ingredient counts.
- Twenty source-pinned withholdings exclude 158 initial candidate claims.
  See [the adversarial review](adversarial-review.md) and
  [withholdings.json](withholdings.json) for unresolved corrections.

## Sources And Evidence

The 534 distinct MediaDive endpoints have actual captured responses: 233 are
accessible and 301 returned HTTP 404. An inaccessible endpoint is not evidence
that its recipe does not exist elsewhere. Exact captured KOMODO table rows
establish accession identity, not quantities or equivalence of variants.

All 58 initially editable candidates were inspected using complete frozen YAML
and source contexts. Ten original DSMZ PDFs were captured for consequential
cross-checks; the ambiguous citrate line in PDF 1270 was also inspected visually.
The [source journal](source-captures.json),
[original PDF journal](original-recipe-captures.json),
[candidate context](inspected-candidate-context.json) and [plan](plan.json)
preserve identities, response hashes, access times and decisions.

Supported concentration claims refer only to provider-declared main-recipe
`g_l` values. They do not establish measured final volume, downstream dilution,
stock topology or ontology mappings. Each new claim has a persistent source URL,
exact excerpt, field locator, hash and scope explanation. Authors and publication
years absent from the dataset are not fabricated.

Two [unapplied water-input proposals](water-input-handoff.json), for 1117 and
1252, retain the separately verified 1000 ml input amounts for a future guarded
repair. Those water claims do not receive support in the evidence-only pass.

## Verification

The [baseline journal](baseline.json) passes independent source/arithmetic
inversion, open-schema validation of all 633 targets, full-corpus strict
validation and 177 guard tests. Rendered diffs add 7,678 lines without removing
or rewriting any existing line.

Application, exact readback, no-op rerun, the
[independent persisted-diff audit](diff-audit.json), all target schema checks,
279 focused tests and post-edit strict validation pass. The sequential checks
in [validation.json](validation.json) are terminal. The fast suite passes
7,673 tests, with 16 skipped and 1,889 deselected, in 365.11 seconds. The 25 new
persisted-cohort checks are included in the focused result, not the fast-tier
pass count. Black, Ruff and the tracked-diff whitespace check also pass.

The [merge-retention check](merge-retention.json) fails for fourteen records
with full-entry loss in canonical ingredient locations; only 126 of 226 full
concentration entries and 139 amount quotations are retained there. Full
[citation validation](reference-validation.json) fails on 38 API titles, while
all 264 new excerpts pass the installed source-text matcher. Product validation
passes with 91 warnings and 96,057 entries skipped for lack of an adapter. The
global merge check fails with 1,247 name conflicts and 3,287 fingerprint issues.
Freshness fails with 6,320 tracked and 6,498 regenerated paths: 3,720 are
tracked-only, 3,898 fresh-only, 1,708 shared paths changed and 892 unchanged.
The [final aggregate check](final-checks.json) passes: 633 exact record hashes,
633 reports, 13,521 report rows, 534 API captures and ten original PDF captures
were rechecked. The two water proposals remain unapplied. The cumulative delta
is exactly 38 edited paths, 264 evidence entries, 76 references and 38 events;
quantity corrections are unchanged.

The [cumulative audit](../20261008-diff-audit-after-komodo-3633.json) now counts
5,105 edited paths, 30,297 new evidence entries and 1,365 quantity corrections.
The [coverage audit](../20261008-followup-coverage-after-komodo-3633.json) reports
11,743 of 15,910 normalized paths, with 4,167 outside follow-up coverage and
unresolved claims inside reported records. No taxa-media growth associations
were added. Neither scientific completion nor publication readiness is claimed.

Checks use the partial locked Python 3.13 environment, not full CI. No commit,
push, PR, merge or branch deletion is asserted by this local batch.

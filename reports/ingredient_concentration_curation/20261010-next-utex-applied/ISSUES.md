# Local Verification Issues

These are local issue records, not GitHub issues. The all-record concentration
objective and publication readiness remain incomplete.

## Open: Full-Suite Runtime Gate

The frozen preceding run has 19,215 passed, nineteen skipped and two warnings,
but exits 1. Four tests exceed the configured 120-second call budget:

| Test | Seconds |
| --- | ---: |
| `test_researched_manifest.py::test_prioritizer_output_does_not_depend_on_local_research_dir` | 218.2 |
| `test_linked_middlebrook.py::test_preview_apply_readback_and_noop` | 144.0 |
| `test_record_kinds.py::test_prioritizer_ranks_no_solution_records` | 130.3 |
| `test_ranking_duplicates.py::test_ranking_has_no_exact_duplicate_records` | 122.3 |

Evidence: [terminal full-run receipt](../20261010-utex-j-das/full.json) and
[log](../20261010-utex-j-das/full-00.log), lines 19243-19254. No failed assertion
is reported. Coverage is 33.28%, above the 17% threshold. The prior fast run
already exceeded the limit for linked Middlebrook; the other three costs are
observed here, not assumed pre-existing. Profile repeated corpus parsing and
schema validation before changing fixtures or limits. No test is allowlisted or
budget relaxed in this batch. The prior run does not cover subsequently installed
code or record edits.

## Open: UTEX Reference Compatibility

The proposed strict UTEX parser remains uninstalled. Its existing-record layout,
excerpt-spacing and title issues are documented in the
[parser review](../20261010-utex-reference-parser-preview/ISSUES.md). Ninety
fresh-source checks of the eighteen unchanged proposals pass with that isolated
parser; this must not be described as an installed-reference-validator pass.

The actual installed-validator run in [references.json](references.json) has
fourteen passing commands and four failing commands. The failures in
`references-13.log` through `references-16.log` are title-only: apostrophes in
Erdschreiber titles are retrieved as `&#39;`. All snippet checks pass. Inspection
of the installed `linkml_reference_validator.etl.sources.url.URLSource._extract_title`
shows a regex returning the raw title capture without HTML entity decoding.
The fallback `SupportingTextValidator.validate_title` then compares that title
with the decoded record title. Do not corrupt bibliography titles or silently
patch site-packages to clear this gate. A maintained upstream extraction/cache
fix needs regression cases for numeric and named entities, literal entity-looking
text, stale encoded cache entries and genuinely different titles. This is distinct
from enabling the broader strict UTEX recipe parser.

## Open: Scientific Limits

The quarter-strength Erdschreiber source has a 250 mL plus 750 mL table (1:3)
and contradictory 1:4 prose. Soil and added-liquid displacement leave several
final-volume concentrations undetermined. Optional carbonate and agar do not
belong in every liquid parent recipe. Preserve exact input amounts, volume bases,
variant scope and conflicts; do not infer a final concentration or silently pick
one conflicting source statement. Source-printed molarities and unrelated
chemical identities are not independently certified by this batch.

## Open: Publication And Broader Gates

Four prepared blends (`CultureMech:000013`, `000030`, `000031`, `000241`)
have no direct or inline component composition usable by the ingredient-based
matcher. Both before and after documents raise the same
`UnfingerprintableMediumError`; the matcher excludes them. The first consumer
checker incorrectly required all eighteen to merge. Its failure is retained in
`consumers-attempt-01.json`; the revised check must prove baseline equivalence
and explicitly limit successful merge-retention coverage to fourteen records.
Do not invent child-stock composition to force a merge fingerprint.

The terminal [corpus check](corpus.json) passes strict, ID, product-label and
MIM-index gates, but both merge gates still fail. Freshness finds 15,056
differences: 2,045 changed, 4,275 only in tracked output and 8,736 only in the
fresh derivation. Do not replace thousands of derived merged records merely
to clear the gate. Koza TSV integration, complete graph rendering and browser
visual inspection remain unavailable. Git/GitHub publication operations were
previously denied; no commit, push, PR, merge or branch deletion is claimed.

## Resolved Locally: Nested-Stock Export

The three findings in the [KGX adversarial review](../20261010-kgx-nested-stock-review/README.md)
are addressed by the installed v3 patch: nested inline stocks are traversed,
stock fingerprints retain volume bases and nested formulation differences, and
stock-ingredient publications are emitted. Installed regression tests,
[actual-DAS checks](consumers-v2.json) and the [installed wheel](wheel-v2.json)
pass. This resolution does not implement general snippet export or replace the
unavailable Koza TSV integration and current full-suite gate.

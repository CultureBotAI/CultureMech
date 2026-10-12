# F/2 Variant And NH4 Evidence Follow-Up

## Applied Locally, Checks Recorded

The [guarded successor plan](plan-v2.json) changes two previously curated records:
the F/2 parent and its NH4 child. Earlier ingredient/stock curation and history
remain intact. The [source ledger](source-review-v2.json) records exact excerpts,
source identity, provenance, old/new operations and remaining limits.

- Add DOI-backed evidence for the existing 4.41 mM nitrate variant, preserving
  its PMID evidence and separating the phosphorus-repletion experiment.
- Add the missing half-strength formulation snippet to the Matsui variant's
  existing DOI evidence, without equating artificial and natural seawater.
- Replace the unqualified 10 nM selenite wording with the explicitly scoped
  Table S1 formulation: 0.001 micromolar = 1 nanomolar. Retain the table's 0.1 mM
  sodium metasilicate and specify its nonahydrate form.
- Correct both NH4 child relationship descriptions to a 175 mL aliquot in a
  250 mL flask. Correct chemical-formula subscript spacing in the pinch snippet
  and its supporting explanation. The pinch remains unquantified.

Two evidence entries, two bibliography entries and two append-only history
events are added; two existing bibliographies gain discovery/source context.
One existing variant snippet is completed, and one existing snippet is corrected.
No structured parent ingredient or stock concentrations, taxa-media associations,
permanent IDs, prior history, or unrelated growth assertions change.

## Evidence Limits

Table S1 is a complete study-specific modified artificial-seawater recipe, not
two additions to canonical UTEX F/2. Its selenite value is explicitly attributed
to the supplement. The main methods remain inaccessible, so possible
main-text/table disagreement and the preexisting UTEX LB2658 assertion are not
resolved. The Tetraselmis source is an inspected abstract, not complete methods.

Matsui methods were manually inspected through the web tool in the preceding
source-review turn; current header retrieval succeeded, but a later lookup
returned a browser-check page. No complete HTTP capture or automated reference
pass is asserted. The source ledger preserves that distinction. Earlier UTEX
stock molarity, salinity-version, catalog-identity and vitamin-step issues remain.

## Preview And Validation

The initial unapplied ledger/plan remain as history. A review corrected the
PDF's unit-heading quotation from a micro sign to its exact Greek mu before
application. Direct PDF text extraction and the visually inspected page support
the separate numeric values, chemical rows and unit headings.

An initial focused run had two test-fixture KeyErrors and thirty passes; the
fixture used the wrong concentration-inventory field name. That was fixed before
application. The final [preview](preview.json) passes all eight baseline/proposed
schema commands, 32 focused tests, Ruff, Black and diff checks. Guarded
[application](apply.json), readback and repeat no-op pass, with exactly the two
intended normalized records changed.

Both records already have canonical follow-up reports. Their existing reports
are extended with seven successor claim rows, not duplicated. Cumulative
reconciliation verifies 5,377 edited records, 37,339 added evidence entries,
6,042 added references, 5,618 history events and 1,751 structured quantity
corrections. The narrative selenite correction is counted separately. Follow-up
reports cover 11,905 of 15,910 exact normalized paths, leaving 4,005 outside
coverage. Coverage does not certify every amount; this successor adds no newly
edited or newly reviewed paths.

All four post-edit schema/strict commands and 354 focused tests pass. Index
regeneration finds no semantic changes, and both runtime merge-retention checks
pass. The fast tier finishes with **15,089 passed, sixteen skipped, 3,498
deselected and two dependency warnings**, in 1,986.09 seconds. This is not a
full-suite pass.

The NH4 production reference check passes two snippets and one title, with no
issues. The F/2 parent command aborts on a supplier timeout and produces no
per-claim results; its manual source review is not an automatic reference pass.
Corpus strict, ID, product and MIM-index checks pass, retaining 91 product
warnings and 96,008 no-adapter skips. Global merge verification still fails with
1,247 name conflicts and 3,287 fingerprint issues. Freshness still fails with
15,056 differences: 2,045 changed, 4,275 only tracked and 8,736 only freshly derived.

The [terminal checkpoint](validation.json) verifies the tested recipe, code,
schema, registry, report and capture hashes. Its explicit reference and merge
gate failures remain open. Nothing is committed, merged or publication-ready,
and the all-record objective is not complete.

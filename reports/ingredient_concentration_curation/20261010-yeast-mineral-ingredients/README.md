# Yeast Mineral Ingredient Curation

Applied locally to MediaDB 397-400, four exact normalized records. The
[application receipt](apply.json) verifies readback, repeat no-op and that only
these four normalized paths changed. The [plan](plan.json) preserves full
before/after snapshots; [four per-record reports](records/) cover all 84 original
ingredient amounts and four added antifoam nodes.

## Applied Changes

- 56 amount replacements use the primary papers' directly stated mass units,
  preserving printed precision. No molecular-weight or assumed-volume conversion
  is used, and this does not mean every prior molar conversion was numerically
  wrong. The para-aminobenzoic acid corrections change both dose and identity.
- Two antifoam concentrations are added at 0.025 mL/L. Two other antifoam nodes
  remain unquantified as final-medium concentrations; their evidence records
  the source's 0.05 mL per liter of water input instead.
- 34 primary identity mappings, twelve existing MIM links and forty labels are
  corrected to source-specified forms. Two unsupported anhydrous molybdate
  mappings are removed without guessed replacement identifiers.
- Preparation now separates heat sterilization from later filter-sterilized
  vitamin addition. No pore size, hold time or pressure is invented. Both ends
  of the ethanol variant relationship acknowledge the source-specific antifoam
  and culture-stage differences.
- 218 scoped evidence entries, fifty references and four append-only curation
  events are added. IDs, categories, organism/role claims and prior history are
  preserved. No taxa-media associations are added.

The [primary-source preview](../20261010-yeast-mineral-source-preview/README.md)
documents inspected methods and title-page images, PubMed identity checks and
official ChEBI readings. Verduyn 1992 supplies MediaDB 397/398; Flikweert 1996
supplies 399/400. The [capture recheck](source-recheck.json) verifies both PDFs,
rendered pages/text, accession-specific database HTML and the dated SQL export
against their pinned hashes, plus the immutable MIM metadata. That is not an
automatic live-reference pass.

## Validation

Eight baseline and eight proposed-record schema/strict checks pass. The guard
passes 68 tests, lint, formatting and a real-schema dry run; the separate
84-claim semantic audit rejects forty altered previews. Installed guard/test
bytes match the tested draft. Application, readback and repeat no-op pass.

All eight actual-record schema/strict checks and 386 regression tests pass.
Cumulative reconciliation verifies 5,406 edited records, 38,132 new evidence
entries and 1,844 quantity corrections. Three indexes are refreshed, and all
four runtime merge-retention checks pass. The [applied checkpoint](applied-checkpoint.json)
pins that original snapshot and its validation results.

Corpus strict, ID, product and MIM-index checks pass. Production reference
validation passes 84 snippets and ten titles but fails 134 snippets and forty
titles. Merge verification fails with 1,247 name conflicts and 3,287 fingerprint
issues; freshness finds 15,056 derivation differences. These failures are not
waived. The preceding Hajjaj fast tier does not certify the new yeast code.

The [URL-only successor](../20261010-yeast-chebi-urls/README.md) repairs the
confirmed encoded-colon ChEBI citation defect. The original plan and checkpoint
remain historical; current per-record reports include the successor hashes.
Successor validation is recorded separately, not asserted by this checkpoint.

## Remaining Work

Twenty-six mineral molarities retain water-input/final-volume gaps and two
molybdate amounts retain the 1992 printed-formula conflict. The two 1996 antifoam
entries do not acquire invented final concentrations. The [issue ledger](issues.md)
records these limits. This batch is not full scientific verification of these
formulations or completion of the all-record goal. Nothing here is committed,
merged or publication-ready.

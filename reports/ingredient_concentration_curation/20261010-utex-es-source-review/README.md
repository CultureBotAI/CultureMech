# UTEX Enriched Seawater Source Review

## Historical Preview

The proposals below were subsequently refined and applied in the
[six-record ES batch](../20261010-utex-es/README.md). This directory retains the
original read-only source-review state, not a second coverage increment.

Six exact normalized records and all 124 stored concentration claims were
inspected. Twelve official UTEX pages and six linked recipe PDFs were captured;
all six PDF page images were manually inspected. The source captures and table
links are pinned in [source-captures.json](source-captures.json).

[Claim decisions](claim-review-preview.json) and [per-record previews](preview-records/)
propose 52 quantity/stage corrections and 72 evidence-only dispositions. They
do not edit normalized data, append curation events or increase canonical
follow-up coverage. Baseline schema checks are recorded in [baseline.json](baseline.json);
all twelve baseline schema/strict commands pass. All 15,910 normalized hashes
remain unchanged. An ignored-inclusive canonical report inventory confirms
all six targets were outside the existing follow-up coverage.

## Supported Next Edits

- In the parent, ES/10, ES/2 and ES/4 records, move ES Fe Solution, P-II Metal
  Solution and all three vitamin stocks under the enrichment stock. UTEX lists
  their doses per 2 L of enrichment, not as direct finished-medium additions.
- Represent 1 L seawater and the respective 20, 2, 10 or 5 mL enrichment inputs
  as absolute aliquots. The parent HTML heading says "For 1 Liter Total", but
  its procedure and PDF specify addition per liter of seawater. Do not infer
  a measured final volume from this inconsistent shorthand.
- Remove 24 unsupported water-fraction quantities while retaining the solvent
  ingredients and source-specific makeup/buffer instructions.
- Retain the explicitly supported stock mass concentrations. The two dilution
  recipes support 500/500 and 665/335 mL per 1 L total; do not round the latter
  to an exact mathematical two-thirds.

## Identity And Procedure Limits

UTEX's glycerophosphate row names CAS 13408-09-8 and a disodium pentahydrate.
The inspected [Sigma 50020 page](https://www.sigmaaldrich.com/US/en/product/sigma/50020)
identifies it as beta-glycerol phosphate disodium salt pentahydrate. The existing
[CHEBI:15978](https://www.ebi.ac.uk/chebi/CHEBI:15978) assertion instead denotes
sn-glycerol 3-phosphate. The packaged MIM index repeats that incorrect mapping.
Remove the unsupported primary/MIM assertions in a guarded follow-up; no exact
replacement ontology ID was established in this bounded search. Retain the
source's mass and chemical form, not an inferred molecular-weight conversion.

The [ES Fe recipe](https://utex.org/products/ES-Fe-solution) explicitly names
ferrous ammonium sulfate hexahydrate but associates catalog F1513. The inspected
[current supplier page](https://www.sigmaaldrich.com/US/en/product/sigma/f1513)
identifies F1513 as iron(III) chloride hexahydrate. Preserve this conflict; the
source formula and mass must not be silently replaced using the catalog number.

The enrichment recipe omits a later vitamin-addition step despite listing doses.
The P-II recipe permits a cobalt sulfate alternative without specifying a
replacement mass/hydrate. Neither gap licenses a guessed instruction or amount.
The 2/3 PDF has a 2019 copyright notice, not a verified HTML revision date.
Generic growth, lighting and temperature claims remain outside this review.

Before applying, pin chemical identity evidence for the glycerophosphate,
cyanocobalamin and thiamine-form decisions; add evidence to every changed claim,
preserve earlier history, validate the proposed YAML, and inspect all diffs.

The subsequent [identity preview](identity-review-preview.json) now pins those
three identity decisions for twelve ingredient nodes in four expanded records.
It proposes 24 primary/MIM identifier-field actions, separate from the 124
quantity claims. Reused chemical captures were rehashed; the supplier 50020
and ChEBI:15978 pages were manually inspected through the web tool, not stored
as fabricated HTTP captures. All six target hashes remain unchanged. None of
these identity proposals is applied or adds canonical review coverage.

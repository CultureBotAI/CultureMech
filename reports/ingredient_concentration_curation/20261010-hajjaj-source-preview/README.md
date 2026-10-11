# Hajjaj MediaDB Source Triage

[Source triage](source-triage.json) pins eighteen unchanged authoritative records
and 217 stored ingredient claims. This is a read-only lead, not eighteen completed
reviews or an increment in canonical follow-up coverage.

The [publisher's primary article](https://journals.asm.org/doi/full/10.1128/aem.67.6.2596-2602.2001)
was inspected. The triage identifies chemical-form, experimental-row and volume-basis
questions requiring claim-level review.

The PMC browser returned a browser-check page, and the public Europe PMC XML
endpoint returned HTTP 500 after the sandboxed attempt failed DNS. A direct
publisher download returned HTTP 403. There is no claimed raw article capture.
The triage records manual publisher inspection and
does not attach unverified numeric evidence to recipes. All eighteen record
hashes were checked against the earlier source assessment and again after writing
the triage artifact; no recipes, IDs, categories or concentrations were changed.

Next: map each record to its exact experimental row, verify chemical identifiers,
and prepare guarded, evidence-backed edits. Existing bacterial classification of
these Aspergillus-source records is flagged separately from ingredient curation.

[Identity leads](identity-leads.json) preserve eight exact packaged-index results.
The heptamolybdate lookup conflicts with the
[ChEBI:91249 definition](https://www.ebi.ac.uk/chebi/CHEBI:91249), which identifies
orthomolybdate. All eighteen molybdate nodes require review; no replacement ID is
assigned and the immutable MIM snapshot is unchanged. The other lookup results
are candidates, not blanket approval of their identity in each formulation.

## Claim-Level Preview

The [claim preview](claim-review-preview.json) and eighteen [per-record previews](records/)
now account for all 217 ingredient claims in the explicitly source-linked cohort.
Every current amount was rechecked against its hash-pinned official MediaDB HTML
table and the 2015-10-07 SQL export. Both representations agree; that agreement
does not independently verify the paper's molar concentrations.

- 37 nutrient claims have proposed replacements in the paper's stated mass units,
  with exact experimental-row locators. No mass/molar calculation is approved.
- 180 mineral claims remain held for volume-basis review: the methods specify
  inputs per liter of distilled water, not an explicit final solution volume.
- 108 ingredient nodes have supplied-hydrate correction proposals. Five of the
  six hydrate identifiers also have independently inspected official ChEBI pages;
  the copper result remains explicitly identified as a packaged-index candidate.
- 18 orthomolybdate identifiers are proposed for removal, without an invented
  replacement. Nine glutamate-hydrate mappings and one isoleucine stereochemical
  assignment still need review.

All [36 baseline schema/strict commands](baseline.json) passed on the unchanged
eighteen records. These are shape checks, not scientific certification or
post-edit validation. The [preview receipt](claim-preview-checks.json) verifies
unchanged normalized-record hashes and zero canonical coverage increment.

## Family Boundary

An ignored-inclusive filename-family and report search found two additional
pending records, MediaDB 330 and 331. Their official pages and SQL export have no
source/growth link. They were therefore excluded by the earlier source-121 join,
not because they were already reviewed.

The [boundary review](boundary-review.json) preserves all 26 additional claim rows
and two [candidate reports](candidate-records/). Their paired-carbon formulations
are leads to Table 2 rows 8 and 9, not automatically established article provenance.
The named-family candidate queue is now **20 records / 243 claims**. This is not a
claim that every differently named medium in the paper has been identified.

The [independent preview check](preview-validation.json) confirms all twenty
Markdown reports are marked `State: preview` and excluded from canonical
follow-up coverage, with all 15,910 normalized-record hashes unchanged. The
36 baseline commands cover the eighteen linked records, not the two unlinked
candidates. No recipes, evidence entries, categories, IDs or concentrations
were changed. [Open decisions](issues.md) must be resolved through the guarded
curation workflow; source-access limits remain recorded above.

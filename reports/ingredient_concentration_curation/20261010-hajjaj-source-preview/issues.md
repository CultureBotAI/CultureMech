# Hajjaj Ingredient Review Decisions

Local review findings only. No GitHub issue or remote mutation was made.

## Wrong Molybdate Identifier

All eighteen explicitly source-linked records use `CHEBI:91249` for the supplied
heptamolybdate tetrahydrate. Its [official formula](https://www.ebi.ac.uk/chebi/CHEBI:91249)
is `2H4N.MoO4`, an orthomolybdate rather than the compound in the
[synthetic-medium methods](https://doi.org/10.1128/AEM.67.6.2596-2602.2001).
The two unlinked sibling records have the same local mapping, but their source
association remains a separate question.

Proposed disposition: remove the conflicting identifier with narrow identity
evidence and preserve the source chemical form. Do not assign the same ID again
from the packaged MIM synonym, invent a replacement, or edit the immutable index.
The current concentration is a database assertion, not evidence for that identity.

## Supplied Forms And Mass Units

Six mineral hydrates are explicit in the article; the 108 corresponding nodes in
the linked cohort currently use unspecified or different forms. The claim preview
records exact-label MIM candidates and five separately inspected ChEBI pages.
Copper dihydrate lacks the separate public-page check. Sodium-glutamate hydrate
and isoleucine stereochemistry need further identity review.

The 37 nutrient mass-unit proposals come from initial treatment amounts, not
residual measurements or lovastatin yields. Resolve identifier and evidence
guards before applying them. Keep Table 2 glutamic-acid equivalents distinct
from the weighed sodium-glutamate hydrate, and preserve the batch-text/Figure 3
glucose discrepancy for record 318.

## Mineral Volume Basis

The methods' water-input basis does not by itself establish final solution
volume. No new final molarity or mass-per-final-volume value is approved for
the 180 mineral claims. Their existing values were reproduced from MediaDB,
but source-table agreement does not settle this scientific ambiguity. Preserve
the database provenance and the hold rather than silently applying an assumed
one-liter final volume.

## Missing Source Links On Siblings

MediaDB 330 and 331 have zero linked sources and no growth/source join rows in
the inspected export. A source-ID-only selection misses both. Their two-carbon
treatments are plausible matches to Table 2 rows 8 and 9; this is explicitly a
curator inference, not an existing database citation. Reconcile their complete
formulations and provenance before applying the article-based corrections.
Both remain in the all-record queue, with 26 claim rows in the boundary review.

## Other Uncertified Claims

The linked records' bacterial classification and generic filtration instruction
are not supported by this fungal study's inspected synthetic-medium methods.
Those findings are separate from ingredient amounts. No path rename, inferred
sterilization protocol, taxon-media association or growth assertion is approved
by the preview. Baseline schema checks do not resolve these questions.

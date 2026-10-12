# OTEB Source-Review Handoff

Read-only preparation for six records, not applied curation or a complete
per-claim scientific review. The current cohort is D1245, K1245, K1245_18691,
K6000, S2474 and S5688. Existing family links close over the first five; the
original medium's explicit stock link adds S5688. This is not proof of exhaustive
biological family membership.

The restricted-network attempt is preserved in `next-1245-context-initial.json`.
Its approved successor captured six sources successfully; the extended context
adds the explicitly linked sugar-stock source for **seven captures**. Their
raw content, source URLs, timestamps and hashes are frozen in
`next-1245-context-extended.json`. `next-1245-inspection.json` enumerates **126
source rows** and pins the two visually inspected original PDF pages. Its row
statuses deliberately remain pending until the full guarded claim review.
Schema/strict baselines are recorded separately in `next-1245-baseline.json`;
all twelve commands pass. The old-slot inventory accounts for **115 existing
quantity fields**, including two placeholders, without approving the candidate
source mappings as edits. K6000 currently has no quantity fields; its missing
composition is still part of the required review.

`next-1245-coverage.json` accounts for every captured row: 105 have explicit
old-field candidates and **21 are unrepresented**. Eleven old fields have no
recipe-row counterpart: nine supplier-tagged LB additions and two placeholders.
One old collapsed maltose field maps to two distinct literal source rows.
These are structural mappings, not endorsements of serum equivalence or inferred
concentration conversions.

## Source-Specific Decisions Needed

1. **Restore exact KOMODO tables, not copied DSMZ ingredients.** K1245 lists
   27 rows. K1245_18691 retains those rows and adds `fetal bovine serum` with
   displayed Gram Amount `100.00`; its pH is null, whereas K1245 reports 6.8-7.2.
   Both tables already contain `Calf Serum` at `99.70`. Preserve those separately
   and document the source difference, rather than silently replacing calf serum
   or endorsing biological interchangeability. The exact row excerpts and URLs
   are in the inspection receipt. Their current `SOURCE_DUPLICATE` link cannot
   describe identical source formulations.
2. **Keep provider rates and unknowns scoped.** KOMODO explicitly labels Gram
   Amounts as per-liter rates. Preserve exact displayed precision, including
   4.98 peptone/broth/yeast, 1.99 dibasic phosphate, 0.80 sugar rates, 1.60 maltose
   and 7.48E-5 thiamine pyrophosphate in K1245. Acid and vitamin-K1 nulls are not
   zero and cannot be filled from the rounded Mol Amount or SEED aggregation.
   Record rates as this provider's assertions, not independent measurements.
3. **Reconstruct the original's preparation boundaries.** The
   [official DSMZ recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1245.pdf)
   separately lists basal masses, seven liquid acid inputs, 0.1 ml vitamin-K1
   solution, 100 ml inactivated calf serum, 100 ml sugar stock and 800 ml water.
   The API instead calls the serum fetal bovine serum. Preserve this identity
   disagreement with both source excerpts. Do not infer a liquid's mass from
   its input volume or silently keep flattened stock rates as medium rates.
4. **Do not invent a denominator.** The original prints final volume 7.0 ml
   +/- 0.7 after its formulation, while its ingredient inputs are much larger;
   this is not a defensible batch-conversion denominator. The medium API's
   declared 1000 ml also does not equal its 1003.1 ml listed liquid-input total.
   Keep those statements distinct. Stock water 1000 ml is an input, not an
   explicit make-up-to-final-volume instruction. Qualified standalone API rates
   already supported by evidence must not be silently recertified as measured
   final-volume concentrations or discarded without claim-level accounting.
5. **Preserve the maltose ambiguity.** Both the original and API visibly list
   two separate maltose rows of 8 g in the stock. Do not choose an intended
   total or deduplicate merely because the names match. K6000 independently
   displays maltose `16.00`, whereas K1245 displays `1.60`; these are explicit
   source-specific rates, not curator permission to resolve the original's
   duplication. The original's 750 microgram thiamine-pyrophosphate quantity
   belongs in the sugar stock, not directly in the receiving medium.
6. **Review the standalone solutions on their own schema.** S2474 has liquid
   inputs represented as percentages and vitamin K1 as an unsupported mass rate.
   The original's `1% soln` does not establish w/v, w/w or v/v. Separate its
   0.1 ml input from the unresolved percentage basis. S5688 already has a
   supported 1 L water input and retains both maltose rows. Preserve earlier
   water evidence and qualified unaffected API rates; inspect missing stock
   references and bibliography titles. Never fabricate `source_data` merely
   to obtain an evidence container.
7. **Fill K6000 from its own source.** Its current ingredient list is empty,
   but its official table has eleven rows with ten numerical Gram Amounts and
   null water. It is already a semantic solution in a MediaRecipe-shaped
   record. Retain that distinction and verify runtime merge behavior. Its
   KOMODO accession 6000 must not be treated as an independently verified DSMZ
   medium-6000 equivalence just because an old importer constructed that URL.
8. **Inspect identity and procedural errors.** The original specifies dibasic
   phosphate, unlike copied monobasic ChEBI grounding. Source-specific serum
   labels and thiamine-pyrophosphate aliases also need review. Withdraw only
   proven inexact annotations; do not invent new ontology terms. The genuine
   source yeast input must be separated from supplier-tagged false LB additions.
   A 25-degree pH measurement is not heating or an incubation optimum, and the
   anoxic-description paragraph does not instruct pouring plates.

## Before Applying

Read all six current YAML records completely and map every existing quantity,
ingredient, stock, metadata, family-link and provenance claim to old/new fields.
The inspection receipt is source inventory, not that mapping. Preserve every
prior history event and retain unsupported or conflicting source statements
explicitly. Every scientific edit requires a scoped exact snippet, persistent
source URL, locator, bibliography context and guarded history event.

Build a frozen preview and an independent source projection. Challenge wrong
amounts, missing/extra rows, variant identity, duplicate maltose handling,
serum substitutions, invented density/volume bases and stock-versus-medium
scope. Follow the full application, readback, no-op, per-record, corpus,
index, merge-retention and report-reconciliation gates. Do not alter current
medium-829 records while their pinned fast-tier run is still in progress.

No taxa-media association has been proposed, and no ingredient YAML was changed
during this source preparation. Missing authors/publication years remain
unknown; the PDF's copyright footer alone does not establish publication year.

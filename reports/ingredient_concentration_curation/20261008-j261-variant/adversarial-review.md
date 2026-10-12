# Adversarial Review

Local review of the four-record repair, not an independent human or GitHub PR review.

## Resolved Findings

1. J261 inherited sulfur and unmodified parent amounts despite an explicit
   variant instruction. Three final rates now replace the parent's values;
   sulfur is absent from active composition and archived in history.
2. M253 batch milligrams and stock milliliters had been asserted as g/L.
   The repair separates batch notes and liter-valued stock inputs, without
   inferring final volumes or percentage bases.
3. The inherited M253 preparation would add sulfur and use pH 6.5. It is now
   cited as overridden context; effective preparation applies the explicit
   sulfur omission and pH 7.0.
4. A copied-ingredient fingerprint had produced a false `SOURCE_DUPLICATE`
   relationship and a stale parent path. Exact tracked reciprocal links now
   identify the composite variant. Parent formulations are unchanged.
5. The first compiler preview used an unsupported preparation action. Schema
   validation rejected it before writing; the action was changed to the
   supported `MIX` enum. A list-index claim extraction error was also caught
   before any plan or recipe write.

## Verification

The independent audit derives stock membership and quantities from the
captured source rows, not compiler lineage. It checks old quantity coverage,
literal evidence, annotation retention, the sulfur archive, parent-only link
changes, the final-rate overrides, preparation scope and source metadata.

Mutation tests reject guessed final rates, stock-dose units, missing or extra
stock members, altered water inputs, invented annotations/quotes/years,
rewritten history, guessed percentage basis, restored sulfur, stale parent
paths, duplicate relationships, inherited final pH, an additive parent copy,
and altered stock preparation. Guard tests cover preview nonmutation,
preflight concurrency rejection, forged plans, readback and idempotent apply.

## Remaining Issues

- Final batch volumes, percent basis and sulfide stock-addition volume remain
  unknown. Batch and provider-declared stock rates are not final-medium rates.
- Reference validation still rejects exact-source chemical-subscript and
  bracketed excerpts; API title extraction falls back to the URL. Literal
  source verification is recorded separately, not substituted for a green gate.
- Generated indexes inspect direct ingredients only for hierarchy enrichment.
  Moving KI into its stock changes the index flag without removing the annotation.
- Broad checks are terminal. Merge verification fails with 1,247 name
  conflicts and 3,287 fingerprint issues; freshness fails with 4,275
  tracked-only, 8,732 fresh-only and 2,045 changed shared paths. The all-record
  review remains unfinished. Tracked merged outputs were not patched by hand.

No GitHub issue or PR review was submitted in this cohort.

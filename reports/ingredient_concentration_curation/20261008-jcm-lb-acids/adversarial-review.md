# Adversarial Review

## Findings Addressed

1. All three formulations incorrectly contained LB constituents in place of
   source-listed methylbutyric acids. Exact node paths and LB supplier metadata
   identify the false nodes; genuine Tryptone and yeast extract are preserved.
   Restoration uses current recipe evidence, not historical numeric values.
2. J266 collapsed main and trace-stock amounts for four salts, flattened three
   stock compositions, and assigned stock pH to the main medium. The repaired
   graph preserves separate stage amounts, source stock doses and preparation
   procedures, while retaining the contradictory metadata as a scoped note.
3. J675 omitted late preparation inputs from its ingredient graph. The original
   prose supports sodium carbonate, cysteine and the fatty-acid dose. Their
   additions do not establish a final volume or warrant g/L conversions.
4. J1203 confused liquid inputs with mass concentrations and resazurin dose
   with stock strength. Milliliters become liters of batch input, not grams.
   Unspecified percentage basis and glucose stock strength remain unresolved.
5. A preview pH snippet omitted the sentence-ending period required by the
   literal matcher. The final preview was rebuilt and all reference checks
   passed before application; the rejected preview was never applied.
6. Metadata reconciliation initially expected an unknown-source index. Its
   all-target guard stopped before writing. Inspection of generated changes
   established the MediaDive index; only the four verified files were refreshed.

The independent auditor reconstructs expected ingredient and stock membership
from source rows, checks all old quantity fields, and verifies additional
prose-supported inputs. It compares every attached quotation and field claim,
preserves inherited annotations and append-only history, and rejects inferred
chemical IDs or bibliography metadata.

The 93 dedicated tests challenge restored-acid deletion, false LB reintroduction,
genuine-ingredient loss, main/stock mixing, invented concentrations and percentage
bases, liquid-density assumptions, changed pH, missing late additions, lost legacy
links, erased history, changed excerpts, duplicate evidence, source conflicts,
concurrent edits, symlinks, forged plans and partial application. All pass.
The 746-test focused selection also passes. This is local adversarial self-review
with mutation tests, not external PR approval or independent human review.

## Remaining Findings

- The unchanged identity queue contains 117 candidates: 76 acid-name and 41
  albumin-name substitutions. Prior report coverage did not prevent these errors.
- J201/J220 are the next inspected baselines. JCM201 currently returns no recipe;
  the captured response is not usable formulation evidence. MediaDive J201
  remains available. J220 has both current provider and original-page support.
- Global merge/freshness failures, other unresolved concentration claims and
  chemical-grounding gaps remain outside these three repairs. No global success,
  full-record completion or publication readiness is claimed.

No GitHub issue, PR or review was submitted in this batch. Earlier local issue
drafts and the outstanding external-publication authorization remain unchanged.

# Adversarial Review

This is a local review of the eleven-record repair, not an independent human
approval or a claim that the all-record goal is complete.

## Addressed Findings

1. Copied DSMZ ingredients cannot stand in for each KOMODO table. The builder
   reconstructs all nine provider-specific tables, preserving literal amounts,
   nulls and secondary-name conflicts. The independent audit derives the
   expected rows from source captures without importing the mutator.
2. Restoring albumin must not remove genuine casein digest or salt. Only the
   supplier-tagged false LB nodes are removed. Dedicated tests retain both
   genuine ingredients and reject extra or omitted nodes.
3. DSMZ 645 alternatives and DSMZ 911 base-table detail must not be summed into
   the receiving medium. Distinct variant and solution scopes preserve every
   source input. Batch masses are not converted with an assumed final volume.
   The complete displaced 645 ingredient nodes remain in append-only history.
4. Hemin's 60 micromoles does not establish 60 uM, and 1N NAOH does not specify
   an addition dose. These unsupported assertions are explicitly rejected by
   tests. The separate KOMODO hemin rate remains provider-qualified.
5. The former exact-duplicate forest incorrectly used the hemin variant as a
   parent of plain media. All nine edges are reconciled on both ends with
   source evidence, and the complete forest is tested for reciprocity/cycles.
   The revised preview strengthens the 645a link with the original preparation
   excerpt; `preview-initial.json` preserves the earlier preview.
6. A later HTTP 403 cannot be reported as a source-validation success. Both
   failed live receipts are retained. Cached checks separately validate hashes,
   identities, source titles, primary excerpts and PDF binary/extraction agreement.
7. Evidence, history and unrelated metadata must survive every transformation.
   Mutation tests challenge amounts, omissions, fabricated mappings/quotes,
   duplicate evidence, history edits, source titles/year, lineage, old values,
   family links and provenance across all eleven records. Concurrent changes
   prevent all writes; repeated apply adds no evidence/history.

The dedicated suite passed 172 tests; the broader focused suite passed 792.
The fast tier passed 10,086 tests (16 skipped); see [validation.json](validation.json)
for the exact terminal receipt and runtime limits.
The independent applied audit accounts for all 244 old quantity slots and
781 claims. Runtime merges retain all eleven formulations separately with
their claims and schema validity. Corpus checks and fast-tier results are
reported separately and must not be replaced by these narrower successes.

## Remaining Limits

Provider normalization differences, the precise historical hemin formulation,
unspecified strain modifications and unrecertified chemical annotations remain
explicit uncertainties, tracked in [the local issue](issue-source-limits.md).
Global merge/freshness problems and publication are not resolved by this batch.

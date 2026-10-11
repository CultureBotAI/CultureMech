# Seven UTEX Stock Ingredient Reviews

Applied locally on 2026-10-10. The all-record objective remains incomplete.
The source preview is retained separately under
`../20261010-utex-seven-stock-preview/`; its reports do not add canonical coverage.

## Applied Scope

- Seven exact normalized SolutionRecipe paths, with permanent IDs, source metadata,
  categories and previous history preserved. See [plan](plan.json) and
  [application receipt](apply.json).
- Fifty-seven evidence entries, sixteen references and seven enriched bibliography
  entries. Every changed amount, identity and preparation-context claim has a
  scoped source URL and snippet in the YAML itself.
- DAS Macro's two prepared-stock doses move from pure-ingredient composition to
  nested stock descriptors. The source-explicit 0.70 M and 0.02 M component-stock
  strengths are added; existing 25% and 75% dose fractions retain their 40 mL basis.
- Seven supplied chemical identities and matching MIM links are corrected. The
  unsupported anhydrous phosphate ID is removed from the heptahydrate without an
  invented replacement ID. Numerical mass concentrations are unchanged.
- Seven [per-record reports](records/) cover 36 current concentration fields.
  No taxa-media association is added.

The [cumulative reconciliation](cumulative.json) verifies **5,416 edited records,
38,202 added evidence entries and 1,844 quantity corrections**. Follow-up reports
cover **11,944 / 15,910** exact normalized paths, leaving **3,966 outside coverage**.
Report coverage is not certification that every concentration is scientifically
verified. The initial full-corpus structural audit remains a separate artifact.

## Verification

- [Preview](preview.json): 28 baseline/proposed schema/strict passes, 99 guard
  tests, lint and formatting. [Formatting follow-up](preview-style.json) proves
  the audit-script change was import order only and rechecks all 36 source claims.
- The independent source audit checks sixteen raw captures and rejects 92 altered
  proposals. It distinguishes 49 captured-content snippet entries from eight
  entries supported by the manual identity-source ledger.
- [Application](apply.json): exactly seven changed paths; readback and repeat no-op
  pass. The complete 15,910-record inventory is pinned.
- [Post-edit checks](post.json): fourteen schema/strict passes, 247 regression
  tests and `git diff --check` pass.
- [Indexes](indexes.json): four semantically changed indexes regenerated; all
  seven standalone stocks excluded from medium merging without errors.
- [Live references](references.json): EDTA, G9 and both J macro-component records
  pass. DAS Macro, DAS Vitamin Cocktail and Minor Nutrients abort on supplier
  timeouts without per-claim output; those commands are not passes.
- [Corpus checks](corpus.json): strict, IDs, products and the MIM index pass;
  merge verification and freshness fail, with 15,056 derivation differences.
  The receipt's orchestration status does not turn those failed gates into passes.
- The [fast tier](fast.json) is terminal: 15,665 passed, sixteen skipped and
  3,498 deselected. The command failed its runtime gate because the linked
  Middlebrook preview/apply test took 155.1 seconds against a 120-second budget.
  There were no test assertion failures; this is still not a passing tier.
- The [terminal checkpoint](applied-checkpoint.json) verifies all 15,910 record
  hashes and the unchanged code tested by that run before subsequent work.

## Unresolved Issues

1. DAS phosphate hydrate has no established exact ontology ID; the packaged
   stock-label mapping is not chemical-form evidence. Sodium nitrate retains a
   publication-resolver ambiguity; no snapshot or resolver override is introduced.
2. The B12 table's autoclaving note conflicts with filtration directions. No
   sterilization sequence or unspecified titrant/temperature is invented.
3. Printed stock/receiving molarity annotations and the EDTA micromolar annotation
   are not promoted to independently verified concentrations. The nickel formula
   typo remains explicit; the exact supplier product establishes its hydrate.
4. The P2250 identity relies on the earlier documented manual SDS inspection.
   Fresh retrieval failed. No successful fresh capture or PDF image inspection
   is asserted for that source.
5. Automated reference timeouts and outstanding corpus gates prevent an all-gates
   pass. No publication readiness, completed all-record review or GitHub action is
   claimed.

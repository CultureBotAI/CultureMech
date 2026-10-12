# Unapplied MediaDB Evidence Proposal

This is a preview, not an applied curation batch. It changes **zero** authoritative
records and contributes **zero** to the applied evidence or report-coverage totals.

**Do not apply plan-v2 as a batch.** A subsequent primary-source read identified
a stock/final-medium conflict in record 308. The
[primary-source holds](primary-source-holds.json) supersede any inference of
scientific readiness from the passing semantic checks. The Kazan thiamine and
Vogel multi-molar amounts also need source review; they are not automatically
corrected from their magnitude.

Record 308 has since received a separate
[applied primary-source correction](../20261009-kaminskyj-stocks/README.md).
Its entry in this historical draft is superseded and has a stale before hash.
The twelve modified M63 entries (MediaDB 4-15) are also superseded by a separate
[applied primary-source correction](../20261009-m63-primary/README.md). Their
before hashes are stale, and the old draft preserves chemical-form errors that
the primary-source review corrects. A further 54 entries are superseded by the
[applied Geobacter primary-source review](../20261009-geobacter-primary/README.md).
Its other two records were outside this draft. The draft itself remains wholly
unapplied; the other 386 candidates and ten AMS1 holds remain pending. Do not
apply this old draft over the 67 separately curated entries. Partial primary-source
curation does not certify every ingredient or resolve all source conflicts.

The [revised proposal](plan-v2.json) covers 453 exact normalized-record paths and
proposes 7,406 ingredient evidence entries, 450 new references, metadata for three
existing bare references and 453 appended history events. All quantities,
ingredient identities, mappings, preparation, relationships and growth evidence
are preserved. Each proposed snippet comes from that record's official MediaDB
compound table with its explicit mM header and persistent recipe URL.

The live tables agree with the dated SQL export, but these are two representations
of the same database, not independent experimental verification. Existing
chemical-form and original-article uncertainties remain explicit. In particular,
the ten AMS1 records are excluded pending the source/formulation conflict in
[the source dispositions](../20261009-mediadb-exceptions/remaining-source-dispositions.json).
This exclusion is not removal from the all-record objective.

## Checks

- Before/after schema validation and round-trip semantic equality pass for all
  453 proposals; source-record hashes remain unchanged.
- [Independent semantic verification](verification.json) accounts for all 7,406
  proposed entries and rejects 2,718 forged quantity, snippet, source, identity,
  history and root-field changes without relying on plan hashes for rejection.
- Three existing references (TAP auto, TAP hetero/mixo and Vogel medium N) are
  enriched in place. Their previous growth claims and TAP variant links remain
  unchanged; no duplicate reference identifiers are introduced.
- The original [partial failed proposal](plan.json) and the earlier
  [renderer-type error](initial-preview-failure.json) are preserved. Neither
  wrote normalized recipes. The failed partial proposal must not be applied.

## Before Application

Review the remaining source/chemical-identity flags, integrate an independently
guarded and mutation-tested apply path with readback and no-op checks, and run
the real post-edit gates. The open production MediaDB reference-adapter problem
is not cured by these preview checks. Generate canonical per-record reports and
refresh cumulative accounting only after the actual application state is known.
The six-record batch's fast-tier run does not test this new report-only preview
code. No commit, push, PR, merge or branch deletion is claimed.

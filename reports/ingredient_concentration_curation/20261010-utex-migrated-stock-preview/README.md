# Migrated UTEX Stock Source Triage

Read-only preview of three standalone stocks and all ten stored concentration
claims. The [source ledger](source-triage.json) pins the current records and
records the original manual readings of the official pages. The subsequent
[source-backed proposal](mutation-preview-v1/plan.json) pins three HTTP-200
HTML captures, exact table cells, basis excerpts and candidate YAML changes.
No authoritative recipe edit, applied evidence entry or canonical follow-up
coverage increment is asserted.

## Findings

- [Beijerinck's Solution](https://utex.org/products/beijerincks-solution): the
  three stock mass concentrations match the official preparation. The record's
  narrative instead labels receiving TAP-medium millimolar values as stock
  concentrations. That wording and the calcium narrative require correction.
- [Bold Trace Stock](https://utex.org/products/bbm-bold-trace-stock-solution):
  the six preparation amounts are listed for a one-liter stock. Five are
  evidence-only candidates. Hold the manganese claim because the printed source
  formula and the assigned dichloride identity differ. The source's concentration
  columns and stock-concentration footnote require an explicit discrepancy
  disposition, not silent reinterpretation of micromolar values.
- [Boron Stock](https://utex.org/products/bbm-boron-stock-solution): the mass
  preparation supports 11 g/L. Its approximate micromolar parenthetical remains
  an unresolved source discrepancy. No replacement molarity or assumed receiving
  medium is proposed.

These are nine evidence-only candidates and one held concentration/form claim,
plus narrative-source problems. The [three per-record reports](records/) are
explicitly marked preview and include all ten existing concentration nodes.
No role, category, organism or identifier change is proposed. Institutional
source provenance is established; named authors, publication year and DOI are
not fabricated. Other cited documents remain uninspected leads.

## Checks

All [six baseline schema/strict commands](validation.json) pass. At that
historical triage checkpoint, all 15,910 normalized hashes were unchanged and
canonical coverage was 11,930. Those are not current whole-corpus totals.

The [six proposed-record schema/strict checks](mutation-preview-v1/validation.json)
also pass. The draft adds thirteen scoped evidence entries, enriches three
existing bibliography entries and repairs three context notes. It retains all
ten structured amounts, including the held manganese claim; no molarity or
working dilution is guessed. Beijerinck's starting water changes from 900 to
the source's approximately 800 mL before final makeup. All three authoritative
stock hashes were unchanged at this preview checkpoint. The independent
[semantic audit](mutation-preview-v1/semantic-audit.json) checks all ten claims
and rejects 27 altered proposals. Guarded application is tracked separately in
the successor batch; these proposals alone do not complete the stock reviews.

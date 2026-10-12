# Rumen Bacteria Ingredient Review

**Preview only: thirteen normalized records are unchanged. The all-record goal
still covers all 15,910 normalized records.**

The [proposal](plan.json) contains 717 evidence-linked claims covering all 187
old quantity fields and 214 proposed ingredient/stock nodes. Independent
projection from the source captures gives **214 proposed evidence additions,
15 bibliography entries and thirteen curation events**, not applied totals.
The thirteen claim ledgers are in `records/`; they are follow-up previews,
not duplicate canonical reports.

## Scientific Decisions

- Restore each KOMODO table's exact displayed rates, precision and nulls.
  The DSM17630 variant changes sixteen rates and adds rumen fluid at the
  provider's 29.13 g/L. This is not a density conversion of DSMZ's 30 ml/l.
  Replace unsupported exact-duplicate relationships with source derivation
  and strain-specific variant relationships.
- DSMZ330 explicitly states nominal final volume 1003 ml. Eleven main mass
  rates use 1.003 L and six-significant-digit arithmetic, not measured
  precision. Listed liquid inputs sum to 1003.6 ml; do not replace the stated
  denominator or assume volume additivity.
- Keep mineral stock batch masses without an explicit final denominator in
  notes. Preserve acid liquid input volumes. Hemin stock is made up to 100 ml;
  do not add another fixed 100 ml water. Keep reagent strengths, stock doses
  and final-medium concentrations distinct.
- JCM1029's live original recipe is unavailable. DJ1029 and TOGO M1093 use
  inspected dataset evidence with exact batch inputs and explicit limitations.
  MediaDive standalone rates remain qualified provider assertions, not new
  original-methods verification.
- M1093 explicitly links M124, which identifies JCM133. Only the seven VFA
  stock rows are imported; the other 24 Medium10 table rows are excluded.
- Preserve all thirteen old evidence entries at their existing paths. Stock607
  metadata corrections use the inspected parent dataset's explicit id/name
  and identical non-null recipe rows, preserving its six old evidence entries.
- Remove false LB expansions and placeholders. Withdraw copied sodium-salt
  groundings where KOMODO says only Resazurin; do not invent replacement IDs.
  Other existing chemical annotations are preserved, not recertified.

Every proposed scientific change has a persistent source URL and literal
snippet in the proposed YAML. Unknown authors, publication years and scientific
bases remain unknown. No organism-growth association is added.

## Checks

- `audit.json`: independent projection accounts for all 214 nodes and 187 old
  quantity fields without importing the builder.
- `references.json`: 245/245 checks pass using sixteen hash-checked official
  captures with networking disabled. This is not a new live refresh.
- `presentation.json`: 98 unchanged root spans and 99 prior history text spans
  are preserved.
- `schema.json`: all 26 preview schema/strict commands pass.
- `focused.json`: 695 tests pass with two dependency warnings; lint, formatting
  and whitespace checks pass.
- Application is disabled pending a frozen review and guarded-application tests.

The existing partial locked Python 3.13 environment is not clean CI or full-suite
certification. No new cumulative edit or review-coverage totals are claimed.
Global merge verification/freshness and publication remain unresolved. See
[source conflicts](issue-source-conflicts.md), [adversarial review](adversarial-review.md)
and [next work](next-work.md).

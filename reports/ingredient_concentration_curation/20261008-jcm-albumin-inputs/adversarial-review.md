# Adversarial Review

## Findings Addressed

1. Both records contained LB constituents in place of albumin. Exact source
   rows identify different preparations: a 50 g fraction V batch input in
   J201 and a 10 ml dose of a percentage-labeled stock in J220. Neither is
   repaired by merely reverting a historical concentration or using the other
   recipe's albumin amount.
2. Several liquid inputs were encoded as g/L. The repair separates product
   or stock dose, unknown stock strength, batch water and receiving-medium
   concentration. Neither API volume 1000/1036 nor summed inputs proves a
   measured final volume, especially after J201's later additions.
3. J201's gelatin and serum were absent from the structured formulation.
   The provider's preparation supports one 200 ml gelatin-solution addition
   before medium filtration and serum afterward, not a guessed 6% v/v dose.
4. J220's hemin solvent normality does not justify a final-medium molarity,
   a 15 ml NaOH dose, or applying stock filtration to hemin. The nested solvent
   and the three specifically filtered stocks retain their distinct scopes.
5. J201's original page is unavailable. Its failure response is not stored
   as SUPPORT evidence. The source gap is explicit in notes and bibliography;
   only the available MediaDive recipe supports the formulation. A bibliography
   or fresh HTTP 200 response alone is not evidence of recipe availability.
6. The old FILTER_STERILIZE action implied a 0.22 micrometer membrane not stated
   in J201's source. FILTER retains the explicit filtration without that assumption;
   the original preparation wording and order remain unchanged.

The independent auditor reconstructs the two ingredient/stock graphs and checks
all old quantities, every current numeric field, all source rows, exact evidence,
source availability, preserved annotations and append-only history. Its 73
dedicated tests challenge LB reintroduction, albumin removal/form changes, invented
groundings, mass/dose confusion, percentage and normality assumptions, missing
solvent, incorrect filtration, lost legacy links, fabricated original corroboration,
changed quotations, missing claims, changed history, concurrent edits, forged plans
and symlinks. All pass; the wider 819-test focused selection also passes.

This is local adversarial self-review with mutation tests, not external PR approval
or independent human review. No GitHub issue, comment or PR was submitted.

## Remaining Findings

- The unchanged identity queue contains 115 candidates: 76 acid-name and 39
  albumin-name substitutions. Existing report coverage did not prevent these errors.
- TOGO M194/M213 retain the corresponding albumin substitutions and quantity
  errors. Their complete current YAMLs and fresh TOGO responses were inspected,
  but neither record was edited or counted as reviewed here.
- The expanded M244/J252 handoff also preserves albumin substitutions for later
  repair. M244 has milligram values misencoded as g/L; J252's scaled numbers
  still lack a supported final-volume denominator. Their original source
  explicitly supplies 10% (w/v) albumin stock, unlike the unspecified percentage
  bases in J201/J220. These candidates remain unchanged and are not new coverage.
- Existing chemical groundings, unspecified percentage bases and unknown final
  volumes remain unresolved where evidence does not establish them. Product
  validation is not a blanket scientific recertification.
- Global merge/freshness failures and publication remain separate outstanding work.

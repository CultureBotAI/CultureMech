# Methanofollis Source-Specific Concentration Preview

State: six-record preview only. No normalized YAML changes have been applied
in this batch. The full 15,910-record objective remains unfinished.

The [plan](plan.json) covers K161, D161 and standalone solutions S209, S241,
S277 and S5980. The [independent audit](audit.json) projects directly from
seven hash-verified source captures, independently of the repair builder and
its decision table. Its 433 claims account for all 130 previous quantity fields
and 147 source/input nodes. Proposed additions are 118 evidence entries, six
references and six append-only history events, not current cumulative totals.

## Source Decisions

- Keep KOMODO's displayed rates, precision and five null amounts distinct from
  the original DSMZ formulation. Its 300.00 g/L rumen-fluid value is a provider
  assertion, not a conversion from the original 300 ml dose.
- Use DSMZ's explicit nominal final volume of 1001 ml for the ten main mass
  rates. The listed liquid inputs sum to 1001.5 ml; retain this disagreement.
  Arithmetic is separate from exact snippets and is rounded to six significant
  digits, not represented as measured precision.
- Separate mineral, fatty-acid and vitamin stock preparation from receiving
  doses. Preserve batch masses in notes where final stock volume is unstated.
  Keep liquid inputs in liters without assuming density or percentage basis.
- Clarified rumen fluid is procedure-only. The 30% vial-fill instruction is
  storage context, not a medium concentration. No standalone CultureMech ID was
  found for source stock 2618 in the ignored-inclusive normalized inventory.
- Restore unquantified KOH and NaOH titrants. Keep reagent strengths separate
  from volumes. Remove false LB expansions and legacy placeholders with evidence
  and append-only archival history.
- Replace reversed SOURCE_DUPLICATE links with reciprocal DERIVED_FROM links
  using exact current archaea paths. This does not assert equivalent recipes.
- Preserve all 32 existing supported evidence entries and their field paths.
  Withdraw the copied anhydrous thiamine grounding from the explicit dihydrate;
  preserve Resazurin and cysteine groundings matched by the pinned MIM resolver.

Every claim has its source URL, exact snippet, field path, old/new value and
basis in the [six preview ledgers](records/). Bibliographic titles, source type,
discovery mode, access date and capture hash are recorded. Authors and
publication years are unknown and remain absent. No growth association is added.

## Gates And Limits

[Focused checks](focused.json): 525 tests pass, with two dependency warnings;
Ruff, Black and whitespace checks pass. [References](references.json): 159 checks
pass against seven offline, hash-verified official captures. This is not a new
live refresh. [Presentation](presentation.json) checks unchanged root sections
and earlier history. [Schema](schema.json) records the twelve preview commands;
only terminal successful receipts count as passes.

The original preview receipt predates a lint-only lambda-to-def change.
[Recheck](preview-rechecked.json) must prove exact byte/claim/lineage reproduction
without replacing the original plan. [Adversarial review](adversarial-review.md)
and [unresolved issues](issue-source-conflicts.md) record the decisions and limits.
Guarded application, post-edit checks, broader tests, accounting, canonical report
reconciliation and merge retention remain pending. No publication is claimed.

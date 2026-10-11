# Methanofollis Source-Specific Concentration Repair

State: six records applied locally. Guarded application, independent readback
and no-op pass, and only the six intended normalized records changed.
All eighteen per-record post-edit checks, corpus, index and runtime
merge-retention checks pass, as do 12,699 fast-tier tests. Global merge
verification and freshness still fail. The full 15,910-record objective remains
unfinished.
The original [preview documents](preview-documents/) remain
immutable alongside the [preview validation](validation-preview.json).

The [plan](plan.json) covers K161, D161 and standalone solutions S209, S241,
S277 and S5980. The [independent audit](audit.json) projects directly from
seven hash-verified source captures, independently of the repair builder and
its decision table. Its 433 claims account for all 130 previous quantity fields
and 147 source/input nodes. [Applied readback](apply.json) confirms 118 added
evidence entries, six references and six append-only history events. These are
batch additions, not current cumulative totals. [Cumulative accounting](cumulative-audit.json)
is 5,258 edited records, 35,769 added evidence entries, 5,816 references and
5,472 history events. Exact follow-up coverage remains 11,802 of 15,910,
with 4,108 outside these reports. Report presence is not complete verification.

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

[Current focused checks](focused-v2.json): 530 tests pass, with two dependency warnings;
Ruff, Black and whitespace checks pass. [References](references.json): 159 checks
pass against seven offline, hash-verified official captures. This is not a new
live refresh. [Presentation](presentation.json) checks unchanged root sections
and earlier history. [Schema](schema.json) records the twelve preview commands;
only terminal successful receipts count as passes.

The original preview receipt predates a lint-only lambda-to-def change.
[Recheck](preview-rechecked.json) proves exact byte/claim/lineage reproduction
without replacing the original plan. [Adversarial review](adversarial-review.md)
and [unresolved issues](issue-source-conflicts.md) record the decisions and limits.
Guarded application and all eighteen [post-edit commands](post.json) pass.
[Corpus strict/ID/product gates](corpus.json) pass, retaining 91 product warnings
and 96,004 no-adapter skips. The six [applied ledgers](applied-records/) are
linked from existing canonical reports without duplicate Record markers.
Six indexes are refreshed. Runtime merging preserves both medium formulations
separately and excludes the four standalone stocks. Applied presentation checks
preserve 40 unchanged metadata sections, 54 history entries and all 32 prior
evidence entries. [Terminal validation](validation.json) records 12,699 fast-tier
passes, 16 skipped, 2,243 deselected and two dependency warnings; 106 additional
QA tests pass. The source corpus and tested code remained unchanged throughout
these gates.
Global merge verification retains 1,247 name conflicts and 3,287 fingerprint
issues. Freshness retains 6,320 tracked versus 10,781 fresh outputs, with 4,275
tracked-only, 8,736 fresh-only, 2,045 changed and zero unchanged. These are failures,
not clean CI or publication readiness.

The [remaining inventory](remaining-inventory.json) retains 33 acid-name
candidates in 28 connected families, one external neighbor and two family-link
identity findings, with none in the repaired cohort. Its 4,859 title candidates
across 4,857 paths are source-verification leads, not established defects.
The separate 71-record queue and every other unresolved record remain in scope.
[Next-family preparation](next-212-source-notes.md) covers 22 unchanged records;
source captures and comparisons are not completed scientific reviews.

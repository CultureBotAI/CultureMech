# KOMODO Concentration Review: Records 2500-2999

This source pass covers **500 previously uncovered exact normalized paths**.
It applies evidence-only edits to **43 records** and leaves **457 unchanged**.
It is not completion of the all-record curation objective or resolution of every
claim in the reports.

## Applied Changes

The [independent applied audit](diff-audit.json) verifies **250 new concentration
evidence entries**, **43 identity-only mapping snippets**, **86 references** and
**43 append-only curation events**. All numeric values, units, chemical identities,
stocks, variants, conditions and organism associations are unchanged. Each new
concentration entry contains the exact recipe URL and literal JSON excerpt,
field/ingredient scope, locator, source hash, access date and arithmetic.

New mapping references use the actual captured HTML title,
`KOMODO - the Known Media Database`. New previews freeze and later recheck that
title; historical plans still reproduce their prior references unchanged.
Earlier title-repair findings are not silently declared resolved.

## Inspection And Remaining Claims

The [source preparation](source-captures.json) verifies all 500 original hashes
against the exact tracked inventory and preceding coverage snapshot. It covers
265 distinct endpoints: 262 accessible sources and three actual HTTP 404 captures
affecting four records. Missing responses were not synthesized.

The [complete candidate inspection](preparation-findings.md) reviewed all 54
initial candidates and their complete API responses. Eleven source-pinned
withholdings remove 75 initially proposed evidence entries for stock, formulation,
version or ingredient-identity conflicts. Seven official PDFs were captured for
consequential cross-checks; five page renderings were also inspected. The final
plan has **250 evidence-only, 9,839 conflict and 13,198 unsupported report rows**.
These rows include preparation, stock and variant contexts, not just individual
ingredient concentrations or independent scientific findings.

There is one result under `records/` per exact path, including unchanged records.
API concentration evidence is scoped to the provider-declared recipe and does
not establish measured final volume, secondary ontology mappings, equivalent
variants, historical source-version identity or growth. Inherited water-unit,
percentage, preparation, grounding and atmospheric-note issues remain explicit.

## Verification

[Baseline](baseline.json): independent provenance-only inversion, open-schema
validation of all 500 targets, strict validation of all 15,910 normalized records,
and 177 focused tests pass. Rendered diffs contain 8,484 inserted lines with no
removed lines or replacement blocks.

[Initial post-edit validation](validation.json): application, 500-record readback,
250 amount snippets, 43 mapping snippets, no-op reapplication, independent diff
and all-target open-schema validation pass. The focused selection found one
historical test failure and passed 268 tests. That test omitted two already
applied source-pinned follow-up plans for six older MediaDive records. Its explicit
successor list was repaired without changing recipe data, expected hashes or
historical plans. The original failed journal is retained.

The focused rerun passes **269 tests**. Strict validation of all **15,910**
normalized records, stable-ID checks and variant-link validation also pass.
Ruff and Black checks pass for the five changed Python files in this pass.

The [independent final checks](final-checks.json) pass: all 500 live hashes and
exact per-record reports, 265 API captures, the frozen mapping title, seven
original PDF captures, and the separate three-record water-input handoff. The
prior KOMODO cohort's readback also passes with explicit successor plans.

[Reference validation](reference-validation.json): all **293 new snippets** pass
the installed supporting-text matcher. Full citation validation still fails on
**43 API titles**: the installed URL source falls back to the URL when JSON has
no HTML title. No new mapping-page title failures remain. This is not a full
citation-validation pass or resolution of older title findings. Product
validation exits successfully with 91 warnings; 96,057 entries are skipped for
lack of an adapter, not validated product identities.

[Actual merge retention](merge-retention.json) fails: **215 of 250 full
concentration entries** survive, and **222 of 250 amount quotes** retain their
ingredient, quantity, reference and field scope. Eight records lose full entries;
six lose amount quotes; seven lose mapping evidence, references or curation
events. Normalized source records retain the evidence. Concentration-independent
group membership is not proof of exact formulation equivalence.

Global merge verification fails with **1,247 name conflicts** and **3,287
fingerprint issues**. The [freshness audit](merge-freshness.json) also fails:
6,320 tracked versus 6,498 freshly generated records, 3,720 paths only in tracked
output, 3,898 only in fresh output, 1,700 changed shared paths and 900 unchanged.
Regeneration used a temporary directory; tracked merged records were not edited.

The [validation recheck](validation-recheck.json) is terminal. `just test-fast`
passes **7,638 tests**, with **16 skipped and 1,864 deselected**, in 669.86 seconds.
The 269-test focused selection separately covers the new cohort and title guards;
these overlapping test totals must not be added. `git diff --check` also passes.
Previously completed application/schema checks are reused only after checking
all 500 live hashes and are explicitly identified in the journal. The runtime
is the partial locked Python 3.13 environment, not full CI. Publication remains
gated on unresolved merge retention, global merge/freshness and citation results;
no generated merges or pages are hand-edited.

The [cumulative audit](../20261007-diff-audit-after-komodo-3000.json) verifies
5,067 edited records and 30,015 new evidence entries. The
[coverage snapshot](../20261007-followup-coverage-after-komodo-3000.json) covers
11,110 of 15,910 normalized paths, with 4,800 outside follow-up reports. These are
not counts of fully resolved records. Three water-input corrections have a
[frozen proposal](water-input-handoff.json) and
[original PDF corroboration](water-recipe-captures.json), and were unapplied at
this batch's completion. On 2026-10-08, the [water-input follow-up](../20261008-dsmz803-1046-1065-water/README.md)
applied them across nine linked KOMODO, MediaDive medium and standalone solution
records using a separate source-pinned plan. Historical CLI readback passes with
that explicit successor; this batch's frozen plan and reports remain unchanged.

No commit, push, PR, merge or branch deletion is claimed for this batch.
The next uncovered inventory slice starts at offset 3000; the eleven withheld
records and earlier unresolved records also remain in the scientific curation
scope.

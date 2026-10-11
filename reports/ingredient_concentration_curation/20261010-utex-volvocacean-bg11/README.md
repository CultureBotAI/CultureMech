# Volvocacean And BG-11 Concentration Follow-Up

Applied locally on 2026-10-11 UTC (2026-10-10 local time). The all-record goal
is not complete. No commit, push, PR, merge or branch deletion is claimed.

## Changes

Three records now have **eight additional source-URL/snippet evidence entries**
and [three canonical per-record reports](records/) covering **15 claim rows**.
The [pinned v2 proposal](plan-v2.json) and [application receipt](apply.json)
preserve exact before/after text, source capture hashes, field changes and counts.

- Volvocacean retains its supported 800/200 mL liquid blend. Its Waris preparation
  now specifies no pH adjustment, and the missing autoclaving step is restored.
- Both BG-11 salt records retain their source-printed NaCl molarities. Two
  unsupported prepared-base doses are removed without replacement numbers;
  notes distinguish partial base preparation from final volume makeup.
- Three optional agar formulations are represented separately. Their amounts
  remain literal batch additions, not assumed final-volume concentrations.
  Both BG-11 thiosulfate doses remain unresolved.
- Titles, source type, discovery mode and access date accompany the persistent
  source URLs. Unknown authors, publication years and DOIs are not invented.
  No taxa-media associations are added.

Primary evidence: [Volvocacean](https://utex.org/products/volvocacean-medium),
[BG-11-1 + 0.36% NaCl](https://utex.org/products/bg-11-1-plus-0-point-36-percent-nacl-medium),
and [BG-11 + 1% NaCl](https://utex.org/products/bg-11-plus-1-percent-nacl-medium).
Linked parent compositions and unrelated biological assertions are not certified.

## Verification

- [Preview v2](preview-v2.json): real-schema preflight, exact source readback,
  111 tests, Ruff and Black pass. Guard tests cover forged plans, concurrent
  edits, invalid schema, links, rollback and no-op reruns.
- [Application](apply.json): exactly three normalized paths change; exact
  readback and repeated no-op pass. Eight evidence entries and their separately
  quoted excerpts match the pinned sources.
- [Post-edit](post.json): six actual schema/strict commands, 112 tests and
  `git diff --check` pass.
- [Fresh-network reference checks](references-live.json): all three commands
  and all eleven checks pass (eight excerpts, three titles). The first
  [sandbox commands](references.json) failed on DNS before citation checking;
  those failures are preserved, not presented as evidence mismatches.
- [Consumers](consumers.json): three HTML pages retain four quantity cells and
  three variants. The two BG-11 singleton merges retain ingredients, stocks,
  variants, evidence, references and history. Volvocacean remains excluded by
  the ingredient-based matcher before and after curation. All fourteen generated
  indexes are semantically unchanged and are not rewritten. Rendering checks
  inspect the DOM, not browser screenshots; composition graphs are degraded.

The [corpus gates](corpus.json) pass strict schema, permanent IDs and product
labels. Merge verification and freshness fail. A fresh derivation has 10,781
records versus 6,320 tracked: 2,045 changed, 4,275 only in tracked output and
8,736 only in fresh output, totaling 15,056 differences. These counts match the
preceding checkpoint, not necessarily its contents. No broad merged-output
regeneration was applied.

The [cumulative audit](cumulative.json) verifies **5,439 edited records, 38,329
added evidence entries and 1,844 quantity corrections**. [Canonical follow-up
coverage](followup-coverage.json) is **11,967 / 15,910**, leaving **3,943 outside
this follow-up coverage**. Historical structural audits already cover the corpus;
follow-up report presence is not complete scientific verification.

The [terminal checkpoint](applied-checkpoint.json) is the authority for final
status. The full suite has not been rerun for this batch; preceding runtime
failures, broader UTEX parser/title issues and publication restrictions are not
resolved by these focused checks.

## Review Dispositions

[Local issues](ISSUES.md) distinguish resolved defects from the missing
thiosulfate dose, BG-11-1 naming discrepancy and other scope limits. The initial
unapplied `plan.json` and failed `preview.json` are retained. Only `plan-v2.json`
was applied. Earlier read-only source reports remain marked as previews and do
not double-count canonical coverage.

# Seventh Receiving-Medium Source Pass

This is an applied local batch, not completion of the all-record objective.
Baseline commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.
The frozen inventory slice `[3000:3319]` contains 319 JCM records.
Only authoritative normalized YAML was changed; no generated merges were copied.

## Outcome

- 319 exact-path reports, each with one record marker and all scoped claim rows.
- 37 edited records, 282 unchanged; zero failed or schema-blocked proposals.
- 192 new evidence entries, 37 bibliography entries, 37 append-only events.
- No numerical, unit, chemical-identity, stock, variant, or growth-claim changes.
- 47 preliminary claims withheld across nine records: six whole, three partial.
- Remaining report rows: 6,142 conflict and 8,057 unsupported. These include
  source inventory/preparation rows, not only independent concentration claims.

[preflight.json](preflight.json) verifies provenance-only changes, unchanged
unsupported quantities, and downgrade-only manual decisions. [plan.json](plan.json)
freezes all record/source hashes and proposals, including the source-pinned
[withholdings](withholdings.json). Guarded apply rebuilt the claims before
writing. Readback verified all 319 hashes and 192 persisted snippets.
Reapplication changed zero records.

## Source Scope

All 43 preliminary candidates' complete main ingredient tables, preparation,
proposed amounts and local context were inspected. [Source-scope findings](preparation-findings.md)
record omitted volumes, separate stock additions, unknown titrant amounts,
unverified chemical forms, and legacy variant comparisons that confuse stock
doses with mass concentrations. Selected original JCM sources were inspected,
not all 319 original recipes. Twenty API responses contain no recipe table.

Each added YAML entry has its exact MediaDive PURL, literal row excerpt,
locator, arithmetic/basis explanation, retrieval date, and response hash.
JCM is the original collection; DSMZ is the dataset provider. Unknown authors
and publication years remain unknown. Claims support provider-declared
main-recipe rates, not independently measured final volume, downstream assay
dilutions, post-titration total concentrations, or secondary chemical mappings.

The original J1105 and J1249 preparation conflicts are confirmed but not yet
repaired. The [J1105 structural repair handoff](jcm1105-repair-handoff.md)
specifies its verified base/stock representation and successor requirements.
The unavailable J1163/J1323 original pages do not justify guessed
chemical substitutions. J1264's fractional liquid volume is not rounded away
to make arithmetic appear consistent.

## Verification

[validation.json](validation.json) records actual commands, exit codes and logs.
The isolated Python 3.11 focused selection passed **589 tests**. Baseline and
post-edit strict scans covered all 15,910 normalized records with zero errors.
Representative open-schema and canonical-ID checks passed. All six earlier
medium readbacks, JCM 896 and KOMODO 12 readbacks, independent semantic-diff,
and exact-path coverage checks passed. The sixth cohort readback follows the
JCM 896 successor without rewriting its historical plan.

[Actual-group retention](merge-retention.json) fails: 37 records in 36 groups,
192 accepted claims, 187 retained. Three records lose evidence and seven lose
the new bibliography entry. All 192 entries remain intact in authoritative
YAML. No evidence is copied across different formulations to force a pass.

Product validation cannot load `oaklib`; reference validation lacks its
executable. The full suite lacks coverage support; the no-coverage retry fails
on missing `dotenv`, `rapidfuzz`, `pandas`, and `bs4` imports. These are not
maintained Python 3.13 or CI passes. Dependency pins were not changed.
Black and Ruff pass for the new preflight checker.

All 25 post-apply jobs and both baseline jobs are terminal. Global merge
verification fails with 1,247 name conflicts and 3,287 fingerprint issues.
[Freshness](merge-freshness.json) fails: 6,320 tracked versus 6,491 fresh records,
with 3,719 only tracked, 3,890 only fresh, 1,644 changed and 957 unchanged.
Regeneration was temporary only. `git diff --check` passes; an additional
ignored/hidden-inclusive scan found no trailing whitespace in the new batch
and public-source artifacts. No gate failure is treated as a pass.

## Remaining Scope

The [independent diff](../20261007-diff-audit-after-media-3319.json) now counts
4,845 edited records, 28,024 new evidence entries, 4,873 new references and
4,849 curation events. Quantity/unit corrections remain 1,159.
[Follow-up coverage](../20261007-followup-coverage-after-media-3319.json) is
8,099 exact paths, with 7,811 outside these reports. Report presence does not
mean all claims are resolved.

The next source-inventory offset is 3319. All ten remaining public-medium
HTML pages and their 21 recipe tables are now captured in a separate
[source handoff](../20261007-public-medium-source-handoff.md), not applied
or counted as completed per-record reviews. Earlier unsupported claims and
other source collections remain in scope. Changes are local and uncommitted;
no PR, merge or all-record completion is asserted.

# FeCl2 Stock Concentration Follow-Up

One existing normalized stock record is corrected locally: CultureMech:012919,
MediaDive solution 3846. This is not completion of all-record concentration work.

## Source And Change

The frozen [source context](inspected-context.json) includes successful HTTP 200
captures of the solution API, MediaDive medium J187 and the original JCM187
recipe. The medium API explicitly links solution 3846 and the original recipe;
the three source ingredient rows agree on identities and batch amounts.

The original FeCl2 stock table specifies `25% HCl (7.7 M) 10.0 ml`. The prior
direct HCl `2.5 G_PER_L` assertion is replaced by a nested reagent-strength
assertion, `7.7 MOLAR`, with a separate `0.01 L` batch dose. This is a stock-stage
rebase, not a computed final concentration. The unspecified percentage basis,
density and measured final volume are not inferred. The provider's `g_l=2.5`
remains visible in its literal quote, with an explicit scope warning.

The FeCl2 tetrahydrate `1.5 G_PER_L` is retained only as the existing qualified
provider-declared concentration, not independent final-volume verification. The
water `0.99 L` remains a batch input. Their prior snippets and explanations are
preserved, with current field locators appended after the HCl relocation. All
chemical annotations, stable identity, placeholder and prior history survive.

The [plan](plan.json), [supplemental claim table](record.md) and independent
[diff audit](diff-audit.json) cover every old/new amount slot. The existing
canonical exact-path report links this follow-up, without adding a duplicate
`- Record:` entry or claiming another uniquely reviewed record. Changes add
three evidence entries, one reference and one curation event; one stock strength
is rebased and one batch-dose slot added. No organism-medium claims are added.

`preview-initial.json` preserves the first, unapplied preview. Self-review found
that the API evidence explanation carried JCM capture metadata; this was fixed
before the authoritative write. The current plan is the applied decision.

## Verification

Baseline and post-edit open/closed schema checks pass. All 15,910 normalized
records pass the strict-schema scan, and ID checks pass. The guarded writer's
readback and no-op rerun pass. The first focused selection passes 76 tests;
after strengthening the independent audit against hidden extra stock entries,
the combined repair/index/manifest selection passes 55 tests.

All five evidence snippets literally match their pinned API or rendered-HTML
source. The installed reference validator remains nonzero: it reports the
existing API-title mismatch and fails to match the JCM table row after its own
text extraction. Its separate snippet matcher passes four of five. These are
explicit failures, not an automated citation-validation pass; see
[reference-validation.json](reference-validation.json).

The [index preview](index-refresh-plan.json) and
[application](index-refresh-application.json) update only this record's metadata
in three generated indexes: two direct ingredients and one nested stock.
Timestamp-only generator outputs are not copied. Comparing all normalized input
hashes with the preceding merge audit proves that only the reviewed source YAML
changed during this follow-up.

The [cumulative audit](../20261008-diff-audit-after-fecl2.json) now records 5,116
edited records, 30,449 added evidence entries, 5,451 references and 5,316 events.
The stock-stage rebase is counted separately from the unchanged 1,386 quantity
corrections. [Coverage](../20261008-followup-coverage-after-fecl2.json) remains
11,749 of 15,910 paths, with 4,161 outside follow-up reports. Report presence is
not proof that every concentration is verified. The cumulative auditor now
restricts its scientific-record inventory to YAML, excluding generated indexes.

The fast tier passes 7,885 tests (16 skipped, 1,890 deselected). Product validation
exits 0 with 91 warnings and 96,063 no-adapter skips; it is not complete chemical
identity verification. All [broad checks](validation.json) are terminal. Legacy
merge verification fails with 1,247 name conflicts and 3,287 fingerprint issues.
The temporary [freshness comparison](merge-freshness.json) fails with 4,275
tracked-only, 8,732 fresh-only and 2,045 changed shared paths: 6,320 tracked
versus 10,777 fresh outputs, with none unchanged. Tracked merged YAML was not
rewritten. Checks use the partial locked Python 3.13 runtime, not full CI.
No commit, push, PR, issue, merge or branch deletion is claimed.

The terminal [final check](final-checks.json) passes all 27 current repair tests,
Ruff, Black and `git diff --check`. It rechecks the applied source hash, all
normalized source hashes, three index hashes, literal source bindings, semantic
inversion and the single canonical report. The standalone stock remains excluded
from medium merging. Known citation and merged-output failures remain explicit;
publication is not ready.

## Remaining Work

The legacy placeholder remains unsupported. Final stock volume and percentage
basis remain unestablished. The standalone stock is excluded from medium merging;
its repair does not automatically repair flattened components in receiving media.
The current J985 medium still requires stock-boundary correction, including the
explicit per-liter sulfide addition and unresolved 3%/30% trimethylamine conflict.
The [next-record source map](next-j985-handoff.json) accounts for all 32 existing
J985 ingredient quantities: 22 belong to stock compositions and three encode
liquid-stock doses as g/L. It is triage only, not an applied edit or another
completed review.
The [JCM265 source map](next-j265-handoff.json) similarly inventories 62 existing
slots across J265 and M257. It identifies three main-plus-stock sums in J265,
incorrect batch/stock/per-liter units, and the nested Wolfe/mineral boundary;
neither record was edited or counted as newly reviewed by this triage.
JCM265/M257, the remaining record inventory, citation validation and stale tracked
merged outputs also remain unfinished.

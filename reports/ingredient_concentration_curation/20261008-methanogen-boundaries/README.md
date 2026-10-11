# Methanogen Stock-Boundary Repair

Three existing normalized records are edited locally. This is a bounded step
toward all-record concentration curation, not completion of that objective.

| Source | Stable ID | Per-record result | Claim rows |
| --- | --- | --- | --- |
| MediaDive J985 | CultureMech:003334 | [J985](records/J985.md) | 55 |
| MediaDive J265 | CultureMech:000295 | [J265](records/J265.md) | 52 |
| TOGO M257 | CultureMech:009148 | [M257](records/M257.md) | 31 |

J985/J265 already had exact-path review reports; those historical reports now
link these supplements. M257 adds one canonical report. There are no additional
`- Record:` entries for the two previously covered paths. Prior review decisions
remain available and are explicitly superseded, rather than silently rewritten.

## Evidence And Changes

The [frozen context](inspected-context.json) contains current record snapshots
and nine official-source captures with exact URLs, access timestamps, HTTP
statuses and SHA256 hashes. Source authors and publication years were not
supplied; access and copyright dates were not promoted to publication years.

The [guarded plan](plan.json) and [independent readback audit](applied-audit.json)
account for every original quantity slot and every new assertion. The audit
independently maps source rows to preparation stages, checks units and literal
snippets, preserves chemical annotations and earlier history, and rejects
unreviewed root changes. The initial unapplied preview remains in
[preview-initial.json](preview-initial.json). Self-review tightened note
preservation, explicit preparation history, and ingredient labels in the report
before application.

- J985: restore separate vitamin, FeCl2, trace-element and selenite/tungstate
  stocks; place their constituents inside the stocks. Represent trimethylamine
  and bicarbonate batch doses separately from unestablished stock strengths.
  Preserve the explicit later sulfide addition as 8 ml per liter. Represent
  FeCl2 stock's HCl reagent as 7.7 M with a separate 10 ml batch dose. The
  distribution step is ALIQUOT, not AUTOCLAVE.
- J265: restore Wolfe's stock and its nested trace-mineral preparation, and a
  separate vitamin stock. Split three historical sums that added main-medium
  and stock concentrations. Cysteine and sulfide are each added at 10 ml per
  liter, not 10 g/L. Move the trace-mineral pH-adjustment instruction into its
  stock and retain KOH as explicitly unquantified; root pH is unchanged.
- M257: correct the 980 ml water input to 0.98 L; put Ni, W and Se additions and
  the one-liter trace-mineral input inside Wolfe's stock. Correct batch and
  per-liter solution doses separately. Preserve source batch masses, including
  milligram-scale resazurin and ferrous ammonium sulfate, without asserting an
  unstated final volume. Restore preparation and post-inoculation pressure text.

The original [JCM265 recipe](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=265)
distinguishes its base preparation, later per-liter reducers, and Wolfe's stock.
The [JCM187 stock table](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187)
corroborates the explicitly stated HCl reagent strength. These are preparation
claims, not organism-growth evidence or proof of whole-medium equivalence.

This cohort adds 103 evidence entries, five references and three curation events.
It restores 55 ingredient nodes to stock context, adds 13 stock descriptors and
21 quantity slots, withdraws 41 unsupported concentration assertions, and keeps
36 source batch masses in supported notes. Four stock-stage concentrations are
rebased, five existing stock-dose bases corrected, and one existing water
quantity corrected. These counters describe different operations and must not
be summed as distinct ingredient concentrations.

## Verification

Baseline and post-edit open/closed schema checks pass for all three records.
Readback and no-op application pass. The initial repair selection passes 56
tests; repair, record-I/O and plausibility tests pass 95; index and content-review
manifest tests pass 39. Ruff, Black and diff whitespace checks pass. All 15,910
normalized records pass strict schema, and the ID gate passes.

All 103 attached evidence snippets match their pinned source captures. All
additional exact excerpts in the claim plan are also independently checked.
The installed citation matcher passes 102 of 103 snippets but cannot match the
JCM table-row quote after its own extraction. All three complete reference
commands exit 1: API title extraction returns URLs instead of source labels,
and J985 also reports that table-row mismatch. See
[reference-validation.json](reference-validation.json). These are failed gates,
not an automated reference-validation pass; quotations were not changed to
silence the validator.

The maintained index generator produced all indexes; only four with semantic
changes were copied, under a hash-guarded [publication plan](index-refresh-plan.json).
Only the three reviewed records' ingredient/solution counts change within those
indexes. Timestamp-only outputs were not published. An aggregate hash comparison
against the preceding FeCl2 follow-up proves no other normalized YAML changed.

The [merge-retention check](merge-retention.json) grouped all 15,910 inputs using
the formulation-aware matcher and verified schema and full scientific-claim
retention for this cohort's actual merge results. Each record stays in its own
group. No tracked merged YAML was rewritten. Full-corpus grouping is not a claim
that every other merged output was re-audited by this focused check.

The [cumulative audit](../20261008-diff-audit-after-methanogen-boundaries.json)
records 5,119 edited records, 30,552 added evidence entries, 5,456 references and
5,319 curation events. [Coverage](../20261008-followup-coverage-after-methanogen-boundaries.json)
is 11,750 of 15,910 paths, with 4,160 outside these follow-up reports. Presence
of a report is not proof that every concentration was verified.

All [broad checks](validation.json) are terminal. The fast tier passes 7,943
tests (16 skipped, 1,890 deselected). Product validation exits 0 with 91 warnings
and 96,070 no-adapter skips; it is not complete chemical-identity verification.
The legacy merge verifier fails with 1,247 name conflicts and 3,287 fingerprint
issues. The temporary [freshness comparison](merge-freshness.json) fails:
6,320 tracked versus 10,777 regenerated outputs, with 4,275 tracked-only paths,
8,732 fresh-only paths, 2,045 changed shared paths and none unchanged. Tracked
merges were not rewritten. The runtime is the partial locked Python 3.13
environment, not full CI. Publication is not ready. No commit, push, PR,
GitHub issue, merge or branch deletion is claimed by this cohort.

The terminal [final check](final-checks.json) rechecks all three applied hashes,
the normalized-corpus aggregate hash, four index hashes, semantic inversion,
and one canonical report per target. It passes all 56 repair tests again,
Ruff, Black and `git diff --check`. The [adversarial self-review](adversarial-review.md)
separates fixed defects from unresolved scientific and publication findings.

## Remaining Work

J985's source disagreement over trimethylamine strength (MediaDive 30%, TOGO
3%) remains explicit. The original JCM985 page returns Nothing found. Percent
bases, measured final volumes, and three legacy M257 gas placeholders remain
unverified. TOGO's referenced vitamin/mineral stock compositions were not
silently replaced by the corresponding complete growth media. Existing
chemical groundings were preserved, not recertified by this concentration audit.

The [next source context](next-stock-source-context.json) captures J151/J187/J197
and TOGO M142/M180/M190 plus their original JCM recipes. The
[next claim map](next-stock-claim-map.json) accounts for 185 existing quantity
slots and records stock-boundary collisions, percentage/normality limitations,
preparation pH scope, and the NaS2/Na2S source spelling conflict. It is triage
only: none of those six records was edited or counted as newly reviewed here.
They require full record/baseline review and guarded evidence-backed decisions.
The all-record inventory, citation validation, stale tracked merges and the
requested GitHub publication workflow remain unfinished.

# M689 Ingredient And Stock Repair

Applied locally to `CultureMech:010094` at reviewed commit
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. This advances, but does not complete,
the all-record ingredient review or the requested publication workflow.

The [canonical record report](records/M689.md) contains one exact tracked path
and all 66 claim decisions. The [pinned context](context.json) has SHA256
`6b81dbac10cc4ea690b661f517aa88968b1945cb6a4a794c1b642a00f87fbc44`.
All eight freshly fetched official responses match their inspected captures;
see [live verification](live.json). Its reference checks describe the first
preview, not the revised applied record. [Application](application.json)
checks the revised record: 50 excerpts and eight titles pass.

## Scientific Decisions

- Corrected four liquid stock additions from `G_PER_L` to `ML_PER_L`: iron
  chloride 10, trace elements 10, trace minerals 25, vitamins 10. The original
  receiving recipe explicitly specifies a per-liter addition stage.
  [JCM670](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=670)
- Expanded only the named stock sections: M180 iron chloride and trace elements,
  M142 trace minerals, and M190 vitamins. Their ingredients are not direct
  medium ingredients. No other parts of the referenced media are inherited.
- Preserved the iron stock's acid input as 10 ml = 0.01 L per stock batch,
  separately from its explicit 7.7 M reagent strength. No percentage basis,
  density or final iron-stock volume is inferred.
  [JCM187](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187)
- Corrected the water input to liters. Withdrew four unsupported final-medium
  mass rates while retaining their source batch amounts, including resazurin
  0.5 mg. Water input is not a measured final volume after supplements.
- Removed the nitrogen and sodium hydroxide quantity placeholders. Nitrogen
  remains atmosphere context; NaOH is an optional pH-adjustment reagent.
- Preserved the vitamin row's asterisk-linked filtration instruction and the
  trace-mineral stock's separate pH preparation. Chemical mappings/history
  remain unchanged and are not recertified. Authors/year are not supplied.

## Accounting And Validation

The independent [applied audit](applied-audit.json) accounts for all 11 old
quantity fields and 47 source rows: four stock-dose corrections, one water-unit
correction, six removed unsupported quantity slots, six newly scoped quantity
slots, 50 evidence entries, eight references and one appended curation event.
These are not 50 new final-medium concentrations or organism-growth claims.

Baseline and post-apply schema/strict checks pass. Guarded readback and no-op
rerun pass. The source audit and adversarial tests reject unit/scope mistakes,
fabricated excerpts, missing/extra ingredients and rewritten history.
The final focused run passes 324 tests; lint, formatting and whitespace checks
pass. The fast tier passes 8,278 tests, with 16 skipped and 1,945 deselected;
the full suite was not rerun for this localized repair. Full-corpus routing
places the repaired record in a separate merge group,
and the generated output retains its quantities, scoped ingredients and evidence.
Only that output is recertified by [merge retention](merge-retention.json), not
all 10,777 generated groups. No tracked merged YAML is hand-edited or regenerated.
Global merge verification still exits 1 with 1,247 name conflicts and 3,287
fingerprint issues. Freshness also exits 1: 6,320 tracked versus 10,777 fresh,
2,045 shared paths changed, 4,275 tracked-only, 8,732 fresh-only, zero unchanged.
These are the same unresolved counts as the preceding pass, not new passing gates.
See [self-review](adversarial-review.md) and [validation](validation.json) for
terminal test and publication-gate results. This uses the existing partial
locked Python 3.13 environment, not a clean CI installation.

`preview-v1.json` preserves the unapplied first draft. It had misleading inherited
provenance wording for new stock rows and retained a gas placeholder. Those were
fixed before application; only `plan.json` describes the applied result.

## Remaining Scope

The [remaining queue](remaining-queue.json) contains 90 unchanged records from
the original 91-record follow-up. Their source captures are leads, not completed
reviews. [M809 handoff](next-work.md) records an inspected preparation-volume
boundary requiring repair. All-record coverage, earlier bibliography mismatches,
and global merge/freshness failures still require work. No commit, push, PR,
merge or branch deletion was performed in this pass.

Current [follow-up coverage](followup-coverage.json) is 11,762 of 15,910 exact
normalized paths, leaving 4,148 outside this report set. Report presence is not
proof that every claim is resolved. The cumulative independent audit now counts
5,135 edited records, 31,218 evidence entries, 5,504 references and 5,339 events.

The [issue #150 progress draft](issue-150-progress.md) is saved locally but was
not posted: the approval checker rejected external disclosure of local project
results without payload-specific user approval. Issue #150 was verified open
before the attempted update. Posting the draft awaits user approval; ingredient
review can continue independently.

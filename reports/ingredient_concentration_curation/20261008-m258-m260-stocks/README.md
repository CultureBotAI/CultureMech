# M258 Identity And M260 Nested Stock Repair

Applied locally on branch `codex/curate-ingredient-evidence`, against HEAD
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. The all-record objective and
publication workflow remain incomplete.

## Applied Changes

- M258: remove the three unrelated LB constituents and restore
  alpha-methylbutyric acid in the fatty-acid stock. Retain its source batch
  amount, 0.5 g, without inventing a stock/final-medium rate or chemical ID.
  Mark the previous LB supplier paragraph as superseded historical provenance.
- M258: separate 660 ml main water, 300 ml clarified rumen fluid, 20 ml
  fatty-acid stock, two 10 ml cross-referenced stocks and separately prepared
  reducing agents. Preserve rumen extraction, stock-only concentrated NaOH,
  medium pH 6.5, overnight rest and post-inoculation pressure instructions.
- M260: separate 900 ml main water from the 1 L water input used to prepare
  MJ(-N) seawater. The 100 ml seawater dose belongs to the medium; the 10 ml
  trace-mineral dose belongs inside the seawater stock.

Every correction has an official persistent URL and exact snippet inside its
YAML. Water inputs do not establish final volumes. Batch masses remain in
evidence-backed notes; unspecified gas/titrant quantities and percentage bases
are not replaced by guessed rates. Existing unrelated chemical annotations
are preserved, not recertified. No taxa-media associations were added.

## Accounting

The independent audit covers all 47 old quantity fields, 86 source rows and
201 claim decisions. This batch adds 163 evidence entries, 10 bibliography
entries and two append-only curation events. It removes 39 unsupported quantity
fields, corrects six stock doses and two water quantities, adds five scoped
water fields, relocates 19 existing nodes and adds two reducing preparations.

Cumulative accounting is 5,154 edited records and 32,531 added evidence
entries. Follow-up reports cover 11,781 of 15,910 exact normalized paths;
4,129 are outside this report set. Coverage does not mean that all scientific
claims are verified. The M142-dependent queue contains 71 unchanged records.

## Verification

Eight refreshed official responses match the frozen source captures. All 173
automated primary-snippet/title checks pass; the independent audit also checks
additional exact excerpts stored in evidence explanations. Both baseline and
applied schema/strict checks, applied reference checks, all-target guarded
application, readback and no-op rerun pass. The new 72-test suite and wider
740-test focused suite pass. Lint, formatting and diff checks pass.

Only these two normalized YAMLs changed relative to the batch baseline. Four
metadata indexes were regenerated. Full-corpus routing yields 10,777 groups
from 15,910 inputs; both target outputs preserve their claims and evidence in
separate, schema-valid groups. No tracked merged YAML was written.

All intended checks are terminal in `validation.json`. The fast tier passes
8,849 tests (16 skipped, 1,945 deselected). Strict and ID checks pass for all
15,910 records. Product validation exits successfully with 91 warnings and
96,086 no-adapter skips; this does not recertify all chemical identities.
Checks used the existing partial locked Python 3.13 runtime, not clean CI.

Global merge verification still fails with 1,247 name conflicts and 3,287
fingerprint issues. Freshness still fails: 6,320 tracked versus 10,777 fresh
outputs, with 4,275 tracked-only paths, 8,732 fresh-only paths and 2,045 changed
shared paths. These failure counts are unchanged from the prior batch.
Commit, push, PR review, merge and branch cleanup have not been completed.

## Historical Substitution Finding

`audit_historical_lb.py` parsed all 758 normalized YAML paths changed by
historical commit `7e8bd7c6026306323b6d86bc0238fa35b8fa1d17`, with no parse
failures. Among 145 detected LB expansions, 80 displaced methylbutyric or
methylbutanoic acid names and 42 displaced albumin-related names. The remaining
23 displaced LB-named ingredients; their formulation correctness is not
recertified by this inventory.

M258 is repaired here. M2366 already has restored albumin in its existing
stock-boundary curation. The other 120 candidates still have the LB trio at
the root: 79 acid-related and 41 albumin-related cases. Ninety already have
follow-up reports and 30 are outside coverage. This queue has no overlap with
the 71-record M142 queue and does not increment scientific-review coverage.

The exact pending baselines and the next J266 source capture are frozen in
`next-lb-identity-context.json`. See `next-work.md` and the local-only
`issue-lb-identity-substitutions.md`. No GitHub issue or comment was posted.

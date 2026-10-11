# Allisonella Ingredient and Stock Review

Two normalized records are applied locally. This is not completion of the
all-record objective or publication workflow. The [plan](plan.json) contains
194 claims covering all 42 prior quantity slots and 43 source/input nodes.
The applied changes add 67 evidence entries, five references and two append-only
history events. No record, permanent ID or taxa-media association was added.

## Scientific Changes

- DSMZ 1006 restores the missing DL-2-methylbutyric acid and removes the false
  supplier-tagged LB expansion, preserving genuine yeast extract, Trypticase
  and NaCl. The seven fatty-acid stock inputs are liquid volumes, not masses
  or receiving-medium concentrations; the receiving dose is separately 3.10 ml.
- Resazurin is represented as a 0.1% w/v stock with a separate 0.50 ml dose.
  DSMZ batch masses remain explicit in notes with source evidence. Neither
  1,000 ml input water nor the API volume encoding proves measured final volume.
- KOMODO 1006 retains its own displayed per-liter rates and null amounts.
  It does not acquire DSMZ stock quantities, inferred gas doses or molarities.
  Copied chemical annotations are not transferred to its less-specific
  cysteine and resazurin labels; original nodes are archived in history.
- Reciprocal links now describe source derivation, not an exact duplicate.
  The aerobic flag versus anoxic-preparation disagreement is explicit.

Every changed scientific claim has a persistent source URL and exact snippet
attached in YAML. Reference metadata includes title, source type, discovery mode,
access date and capture hash. Authors and publication years are not invented.
Existing chemical annotations otherwise remain preserved, not recertified.

## Evidence and Validation

The [live retry](live-retry.json) successfully refreshes all three sources,
matches the frozen captures and original PDF binary, and passes 72 of 72
reference checks. The initial [sandbox network failure](live.json) is retained.
All 526 focused tests, lint and formatting pass, including 80 dedicated
Allisonella tests. [Guarded application](apply.json) passes independent preview
and applied audits, exact readback and a no-op rerun. All six post-edit
schema/strict/reference commands pass.

Full-corpus strict-schema and ID checks pass for 15,910 records. Product
validation retains 91 non-blocking warnings and 96,040 no-adapter skips. The
variant validator reports no findings under its ID-fallback rules; the separate
remaining-family inventory still has 21 stale exact paths. Four generated
indexes were refreshed, with record metadata changes limited to DSMZ 1006.
[Runtime retention](merge-retention.json) groups all 15,910 inputs and preserves
both formulations separately, schema-valid and claim-preserving. Derived merged
YAML was not written. Global merge verification still has 1,247 name conflicts
and 3,287 fingerprint issues; freshness has 4,275 tracked-only, 8,732 fresh-only,
2,045 changed and zero unchanged files. The fast tier passes **10,167 tests**
(16 skipped, 1,945 deselected). Local QA passes fourteen checks, including
re-running cumulative accounting. The [terminal validation receipt](validation.json)
checks the current corpus, code, plan, sources and terminal logs, retaining both
global failures and the initial network failure. This uses the existing partial
locked Python 3.13 environment, not clean CI or the complete test suite.

[Cumulative accounting](cumulative-audit.json) records 5,200 edited records and
33,660 added evidence entries. [Follow-up coverage](followup-coverage.json)
remains 11,798 exact normalized paths, with 4,112 outside these reports.
The two existing canonical reports link to [D1006](records/D1006.md) and
[K1006](records/K1006.md); no duplicate `- Record:` entries were introduced.
Report presence is not proof every scientific issue is resolved.

See [adversarial review](adversarial-review.md), [source limitations](issue-source-limits.md)
and [remaining work](next-work.md). No commit, push, public issue, PR, merge or
branch deletion occurred in this batch; the earlier publication approval remains
unresolved.

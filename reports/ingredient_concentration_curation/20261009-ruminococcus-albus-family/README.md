# Ruminococcus Albus Ingredient Review

**Ten records are applied locally. The full 15,910-record goal remains open.**
The thirteen-record family includes ten repaired records, unchanged J675 and
solution4674 comparisons, and inaccessible KOMODO3037. Its empty ingredient
list does not constitute a completed review.

## Applied Changes

The frozen [plan](plan.json) accounts for **507 evidence-linked claims**,
**126 old quantity fields** and **138 output ingredient/stock nodes**.
[Independent applied readback](apply.json) confirms **155 added evidence entries,
16 references and ten history events**. Only the ten intended YAML records
changed; guarded readback and a no-op rerun pass. The original preview and
its receipts remain immutable; earlier human documents are archived in
`preview-documents/`, and current claim ledgers are in `applied-records/`.

Each applied scientific change has a persistent source URL and literal snippet
in the YAML. Unknown authors and publication years remain unknown. No
organism-growth association was added.

The repair restores KOMODO precision/nulls and both DSM18848 supplements,
source-specific stock boundaries, missing acid rows and liquid input units.
It removes unsupported LB expansions and the incorrect M2636 stock4674 link
without changing stock4674's supported formula. Original batch masses and
unspecified percentages remain in evidenced notes. Provider-qualified stock
rates are not promoted to measured final-medium concentrations. Differing
calcium hydrate labels remain source-specific.

## Verification

- `focused-v2.json`: **568 passing tests**, two dependency warnings, lint and
  formatting. Includes guarded apply/readback/no-op, concurrent-edit, symlink,
  pinned-plan and independent source-projection attacks.
- `references.json`: **179/179** checks against fourteen hash-checked official
  captures with network disabled, not a new live refresh.
- `post.json`: all **30 per-record schema/strict/reference commands pass**.
- `corpus.json`: strict-schema and ID checks pass for **15,910 records**.
  Product checks pass with 91 warnings and 96,001 no-adapter skips. Current
  variant-link validation has no findings under its ID-fallback rules.
- `qa.json`: **96 tests pass**, plus lint, formatting and whitespace checks.
- `presentation-applied.json`: 76 unchanged metadata spans, 77 prior history
  spans and seven existing S882 evidence entries/field paths are preserved.
  The six S4674 evidence entries remain in its unchanged record.
- Six generated indexes are refreshed. Runtime merging preserves all six
  medium-shaped targets, including restored K3017, and excludes the four
  standalone solution records. It does not write derived YAML.

The [terminal validation](validation.json) records **12,269 fast-tier passes**,
16 skipped, 1,975 deselected and two dependency warnings in 2,102.62 seconds.
Current code, record, source-capture and receipt hashes match the checked
checkpoint. The environment is the existing partial locked Python 3.13
environment, not clean CI or full-suite certification.

Global merge verification still fails with **1,247 name conflicts and 3,287
fingerprint issues**. Freshness also fails: 6,320 tracked outputs versus 10,779
fresh outputs, 4,275 tracked-only, 8,734 fresh-only, 2,045 changed and zero
unchanged. These are separate from the repaired cohort's passing retention.

## Accounting And Remaining Work

[Cumulative accounting](cumulative-audit.json) is **5,245 edited records,
35,437 added evidence entries, 5,795 references and 5,453 history events**.
Eight existing canonical reports now link to applied ledgers; M694 and M2636
have new canonical reports. Exact follow-up coverage is **11,801 of 15,910**,
leaving **4,109** outside these reports. Report presence does not certify every
concentration. Thirty-eight acid-name candidates and the separate 71-record
M142 queue remain, alongside all other unfinished corpus work.

The [next medium-330 preparation](next-330-preparation.json) remains read-only:
thirteen records, 187 old quantity fields, 238 source-table rows, 32 original
PDF rows and seven linked TOGO VFA rows. Sixteen successful official captures,
two visually inspected PDF pages and 26 passing baseline commands support the
next review. JCM1029's live endpoint returned no recipe; that gap remains
explicit despite available MediaDive/TOGO captures. No medium-330 YAML edits
or new evidence entries are counted here.

See [source conflicts](issue-source-conflicts.md), [adversarial review](adversarial-review.md)
and [next work](next-work.md). No commit, push, public issue, PR, merge or branch
cleanup was performed for this local checkpoint.

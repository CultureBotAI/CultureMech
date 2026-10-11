# Remaining Ingredient Work

The active objective covers all 15,910 normalized records. Neither completion of
medium212 nor preparation of medium323 completes that objective. This checkpoint
applies 21 recipe changes but adds no taxa-media associations and publishes no
GitHub changes.

## Medium212

The controlling proposal is `plan-v2.json`, SHA256
`496c0f734f231756ee97a80021429802c1af9136472b77798c9f2162ad4b2d4c`.
It contains 22 records, 21 applied edits and one byte-exact no-op (S608).
The normalized corpus is now at SHA256
`a55dbe72d9740772e93f5dbb870bc17709d68b4b494cd12f69e5bb02b7c41f23`.
Use the terminal receipts, not a progress-log percentage, to decide which gates
finished. Do not overwrite the original preview, failed tests or source captures.

The frozen preview and nested receipt hashes now guard apply/verify. Application,
independent readback and no-op pass; the focused successor suite has 837 passes.
All 44 post-edit schema/strict commands and 241 supported reference checks pass.
BacDive's captured-HTML manual check remains separate from the production
validator, which has no page adapter; no versioned DOI-PDF claim is made.
Corpus strict/ID/product checks pass. All 22 canonical reports link to applied
ledgers; the 44 explicitly marked immutable preview ledgers do not inflate
coverage. Six indexes are refreshed. Runtime merging retains all four media
separately and excludes eighteen standalone solutions. Post-application
presentation checks pass in `presentation-applied.json`. The serial wrapper
stopped on the original preview receipt's filename collision; the helper now
uses a distinct applied receipt and the historical preview remains untouched.
Final QA passes 127 tests plus Ruff, Black and whitespace checks. The current
fast tier passes 12,700 tests, with 16 skipped, 2,829 deselected and two warnings.
`validation.json` freezes the applied checkpoint. `test-selection.json`
documents the medium212 module's corpus classification and its separate focused
pass; do not substitute the historical preview test result or compare the
different fast selections as though they were identical.

The cumulative registry uses `applied-plan.json`, SHA256
`7d208f749fbf0172c3682994dc256ac7bdc3383852e373682c1b7a344e84f30e`,
which contains only the 21 changed records and links to the complete proposal.
Keep the nine generic nickel withdrawals without accepting the rejected MIM
replacement ID. Global merge verification and freshness remain failures, not
waived gates; do not hand-edit derived YAML to hide them.

## Medium323

Four exact records are prepared in `next-323-local-preparation.json`: K323,
D323, S599 and S6552. Five captured primary sources, one visually inspected PDF
page, twenty PDF table rows, twenty-one KOMODO rows, 62 old quantity fields and
nine existing evidence entries are documented. All eight baseline schema/strict
commands pass. This checkpoint has not created a guarded proposal or changed
recipes for this family.

Use `next-323-adjudication.json` to interpret the earlier source and identity
inspection receipts before building its proposal:

- Use the original's explicit final-volume statement, not an additive-liquid
  assumption. Separate fatty-acid stock doses and resazurin reagent strength
  from final-medium solute concentrations.
- Retain the supported D323/S599 resazurin rate: 1 g/L stock times 0.0005 L,
  divided by 1.002 L final volume, rounds to 0.000499002 g/L. Add evidence;
  do not repeat the initial numerical-error interpretation. S599 water's
  998.003992015968 value is ml/L, not percent v/v.
- Preserve the conditional agar table/procedure discrepancy rather than
  silently choosing or averaging the quantities. Review physical-state metadata
  after removing copied agar from source formulations that do not list it.
- Restore each provider's own formulation, including KOMODO's nine nulls and
  its bicarbonate rather than the original's carbonate. Do not convert nulls to
  zero or transfer ontology IDs between different chemical forms.
- Correct unsupported stock percentages using explicit liquid inputs without
  inventing densities. Do not automatically declare provider-reported mass rates
  false; distinguish their scope from original batch doses.
- Preserve the nine supported S599 evidence entries and restore its omitted
  stock input. Adjudicate D-glucose using the source's full identity fields,
  including KOMODO's semi-unique name, not only its displayed label.
- Correct the -20 C storage action from HEAT to STORE only in a guarded,
  source-backed proposal. Resolve physical state explicitly: the required enum
  has no unknown option, and an omitted agar row alone does not prove LIQUID.

## Full Corpus

The current cumulative audit records 5,263 edited records and 35,955 added
evidence entries. Exact follow-up reports cover 11,802 paths, with 4,108 outside
them; a report does not certify every concentration. The 31 acid-name candidates,
separate 71-record queue and all other unresolved records remain in scope.

Local HEAD is `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`; upstream was not
refreshed. The earlier outbound GitHub-write denial remains unresolved and must
not be retried through another route. Public-source read approval is separate
from repository publication authority. PR, remote issue, merge and branch-cleanup
work is not complete.

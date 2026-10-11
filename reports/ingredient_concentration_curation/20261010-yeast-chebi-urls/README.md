# Yeast ChEBI Citation Repair

Applied URI-only follow-up to the four yeast mineral records. The
[source review](source-review.json) scanned all 15,910 normalized YAML files,
including ignored filesystem files, and matched that inventory to exact tracked
paths. Eighty live reference fields in four records used encoded-colon ChEBI
paths that returned HTTP 404. Prior curation history was excluded from mutation.

Ten canonical colon-form URLs returned HTTP 200, with matching official page
titles and formula snippets. The [preview receipt](preview.json) rechecks the
captured bytes. ChEBI supports identity only, not recipe concentrations.

## Applied Scope

The [application receipt](apply.json) verifies forty evidence URL corrections,
forty bibliography URL corrections and four appended history events. Readback
and repeat no-op pass, and exactly the four reviewed normalized paths changed.
Concentrations, chemical identities, snippet wording, other claim text and all
prior history are unchanged. No new evidence entry or taxa-media association
is counted. The [plan](plan.json) links the original applied record hashes to
the repaired hashes.

The [four existing canonical reports](../20261010-yeast-mineral-ingredients/records/)
are refreshed, not duplicated. Their former preview-only status wording is
corrected; [report receipts](reports.json) retain original and current hashes.
The original batch checkpoint is historical and remains unmodified.

## Validation

All sixteen baseline/proposed schema/strict commands, 42 guard tests, lint and
formatting pass. All eight actual-record schema/strict commands pass. Tests
cover altered quantities, snippets, identities, history, URLs, paths and counts,
source/record drift, schema failure, rollback and concurrent-edit preservation.
The initial test setup caught a report-path guard mistake before application;
it was fixed and the suite rerun successfully. No crash-atomic multi-file
guarantee is asserted.

The [applied checkpoint](applied-checkpoint.json) records 174 passing post-repair
regressions, successful cumulative reconciliation and four runtime-retention
checks. Live validation now passes 124 snippets and fifty titles: exactly eighty
formerly failing checks pass, with no regressions. Ninety-four snippet failures
remain: 47 abstract-only retrievals and 47 unavailable-content results. Manual
PDF inspection is not an automatic reference-validator pass.

Corpus strict, ID, product and MIM-index checks pass. Merge verification and
freshness still fail; the latter finds 15,056 derivation differences. The
ignored-inclusive live URL scan finds no remaining encoded-colon ChEBI reference
in all 15,910 normalized records; prior history is deliberately excluded.
Full fast-tier coverage on newly added code remains pending at this checkpoint.
Nothing here asserts publication readiness or completion of the all-record goal.

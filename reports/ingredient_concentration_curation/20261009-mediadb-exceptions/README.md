# Applied MediaDB Ingredient Exceptions

Six authoritative records are edited locally through the guarded [plan](plan.json).
The [application receipt](apply.json) verifies readback, repeat no-op and that only
these six normalized YAML records changed. All source amounts are database
assertions, not quantities independently verified in the original journal articles.

| MediaDB record | Applied correction |
| --- | --- |
| [430, CoSO4 freshwater](records/430.md) | Restore 3-methylbutanoic acid, 10 mM; remove unrelated LB product expansion. |
| [460, CoCl2 freshwater](records/460.md) | Restore 3-methylbutanoic acid, 10 mM; remove unrelated LB product expansion. |
| [473, McN](records/473.md) | Restore 2-methylbutanoic and 3-methylbutanoic acids, each 0.04896 mM; remove unrelated LB expansion. |
| [474, McNA](records/474.md) | Restore the same two source-reported fatty acids; retain its distinct acetate addition; remove unrelated LB expansion. |
| [288, Song CDM](records/288.md) | Withdraw six VARIABLE defaults where MediaDB gives no amount. |
| [289, Song optimal CDM](records/289.md) | Withdraw thirteen VARIABLE defaults; preserve its distinct zinc sulfate amount. |

The batch adds **156 ingredient/formulation evidence entries, twelve references,
six quantity fields and six curation events**. It removes twelve copied LB
ingredient nodes and nineteen unsupported VARIABLE fields, for **31 withdrawn
quantity fields**. It adds **zero taxa-media associations**. Existing IDs,
chemical mappings, unrelated preparation/role/growth claims and earlier history
are preserved. New fatty-acid rows do not invent ontology identifiers.

Every ingredient now carries an exact excerpt from its own official MediaDB
table, with a persistent URL, table locator, column basis, access date and
versioned-export corroboration. Nineteen entries support ingredient membership
and explain the unknown amount; they are not numeric concentration evidence.
The six reports account for all **164 historical/current claim rows**, including
removed LB additions. They each have exactly one exact-path `- Record:` line.

## Validation

- [Preview](preview.json): twelve baseline schema/strict checks, 93 tests,
  lint and formatting pass.
- [Adversarial checks](adversarial-checks.json): 54 semantic forgeries rejected
  after rebuilding their hashes and claim inventories.
- [Post-edit](post.json): twelve actual-record schema/strict checks and 243
  regression tests pass; one source-dump test skips. All 156 literal snippets
  match the hash-pinned live source tables.
- The six standard reference checks first failed because of sandbox DNS.
  [The network-enabled rerun](references-live.json) also fails: its generic
  URL cache stores raw HTML, so table-cell excerpts are not found as raw
  substrings, and the SQL export's descriptive title is not recognized.
  These are open validator issues, not green reference gates.
- [Index refresh](reconcile-indexes.json): three maintained generated indexes
  refreshed for four changed ingredient counts; unrelated metadata unchanged.
- [Runtime merge retention](reconcile-retention.json): all six formulations
  remain separate and retain their claims with valid schema. No generated
  merged YAML was hand-edited or published.
- [Corpus checks](corpus.json) are terminal: strict validation of 15,910 records,
  ID checks and product checks pass. Global merge verification still fails with
  1,247 name conflicts and 3,287 fingerprint issues; freshness reports 15,056
  differences. The receipt's aggregate `passed` covers required checks only,
  not these two explicitly failing gates.
- [Fast-tier results](fast.json) are terminal: 13,158 passed, sixteen skipped,
  3,498 deselected and two dependency warnings. Code and all normalized-record
  hashes remained unchanged during the run. This does not replace earlier
  failed full-suite runs or test the later report-only proposal code.
- The [final local checkpoint](validation.json) pins the receipts, actual
  record hashes and unchanged 15,910-record inventory. Local application and
  the fast tier pass; production references, global merge/freshness and the
  full objective explicitly do not.

## Coverage And Remaining Work

[Cumulative accounting](reconcile-cumulative.json) verifies **5,290 edited records
and 36,605 added evidence entries**. Exact follow-up coverage is **11,818 of
15,910**, leaving **4,092 outside this follow-up**. Report coverage does not
certify every claim in a record.

The [469-record comparison](cohort-assessment.json) is the earlier read-only
MediaDB assessment, not 469 completed scientific reviews. Its six exceptions
are the records handled here; the remaining 463 still require follow-up.
Live source table captures are corroborated against the official 2015-10-07 SQL
export; [source-review.json](source-review.json) pins the selected source facts.

The [remaining live comparison](remaining-live-comparison.json) has finished all
463 requests without access/parse failures or recipe changes. Compound names
and amounts agree with the export. Three heading flags (324, 387 and 477) are
trailing export whitespace, not composition differences. This comparison adds
no canonical reviews or in-record evidence and does not increase follow-up
coverage. The primary-paper conflict described in [issues.md](issues.md) is a
reason not to equate database agreement with scientific verification.
The [independent disposition pass](remaining-source-dispositions.json) rechecks
all 7,606 source rows, preserves the three heading flags with explicit
whitespace-only decisions and holds ten AMS1 records. It identifies 453
database-evidence candidates, not 453 completed scientific reviews.

[Open issues](issues.md) retain primary-source, chemical-form, importer and
reference-validator gaps. The work is local and uncommitted. The all-record
goal and requested GitHub publication workflow are not complete.

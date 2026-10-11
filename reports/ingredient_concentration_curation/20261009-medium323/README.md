# Applied Medium323 Ingredient Review

Four authoritative records are repaired locally through the guarded
[successor plan](plan-v2.json). [Application, readback and repeat no-op](apply.json)
pass; only the intended four normalized YAML files changed.

| Record | Result |
| --- | --- |
| [KOMODO323](records/K323.md) | Restored its own compound table and source rates, removed copied DSMZ and unrelated LB assertions, and preserved null input amounts. |
| [MediaDive solution599](records/S599.md) | Corrected water units, restored the evidenced stock addition and completed missing formulation evidence. |
| [MediaDive solution6552](records/S6552.md) | Replaced erroneous percentages with source input volumes and supported the explicit provider stock mass rates. |
| [DSMZ323](records/D323.md) | Restored the fatty-acid stock boundary, missing constituent, dose and water; removed unrelated LB nodes and corrected storage action. |

The batch adds **65 evidence entries, seven references and four history events**.
It corrects **15 quantity fields**, withdraws **14 unsupported quantity fields**,
adds **five quantity fields**, and relocates four existing stock components.
There are **zero new taxa-media associations**. Every changed formulation claim
has a persistent source URL and exact snippet; missing DOI, authors or year are
not invented. The four canonical reports are extended without adding duplicate
`- Record:` entries; the linked follow-ups cover all 61 current quantity claims
and the removed historical fields.

## Source Decisions

The complete KOMODO page supports retaining the existing L-cysteine hydrochloride
hydrate links: the compound row includes cpd00084, and the same page's SEED table
names it L-Cysteine. This supersedes the earlier draft's withdrawal. The supplied
1.13 g/L quantity comes from the compound table, never the SEED aggregate molarity.
The independent auditor checks the separate SEED table for identity; the
concentration parser correctly excludes it from amount extraction.

KOMODO and DSMZ remain separate formulations with reciprocal `UNCERTAIN` links.
No exact-duplicate or historical-derivation claim is made. The KOMODO physical
state remains unverified, the conditional agar source discrepancy remains
disclosed, and sodium-resazurin identity remains wrong in the upstream MIM index
despite the two local mapping withdrawals. Solution599's generic glucose
secondary mapping is retained as a limitation. See the
[adversarial review](adversarial-review.md).

## Validation

- [Final preview](preview-final.json): eight baseline schema/strict commands,
  82 production reference checks, 75 focused tests, lint and formatting pass.
- [Post-edit checks](post.json): the twelve actual-record schema/strict/reference
  commands and 312 regression tests pass, with two dependency warnings.
- [Report reconciliation](reconcile-reports.json): four existing canonical
  reports extended, with no duplicate coverage.
- [Cumulative accounting](reconcile-cumulative.json): 5,284 edited records,
  36,449 added evidence entries, 11,812 follow-up paths and 4,098 outside follow-up.
- Generated indexes and runtime merge retention pass their separate receipts.
- [QA rerun](reconcile-qa-v2.json): 204 tests, lint, formatting and diff checks pass.
- [Fast rerun](fast-v2.json): 13,064 passed, 16 skipped, 3,498 deselected;
  code and normalized input hashes remained unchanged throughout the run.
- [Corpus gates](corpus.json): strict validation, IDs and products pass.
  Merge verification still fails with 1,247 name conflicts and 3,287 fingerprint
  issues; freshness still reports 15,056 differing records. Those failures
  were recorded as non-required diagnostics, not converted into passing gates.

The failed initial cache-wrapper checkpoint and superseded previews are retained.
An adversarial fixture exposed a late directory-symlink issue; the writer was
fixed and the regression added before any authoritative write. Earlier draft
artifacts remain unapplied historical proposals, not current application authority.
The first reconciliation QA run failed on two tests that assumed current bytes
must equal a historical batch result. They now verify and invert registered
successor edits before counting the original batch. The interrupted first fast
run and failed QA receipt remain preserved; only the terminal v2 runs passed.

This is local, uncommitted work. No GitHub write, publication or all-record
completion is claimed. The full objective still covers all 15,910 normalized
records, including those outside current follow-up coverage.

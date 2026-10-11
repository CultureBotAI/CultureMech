# Adversarial Review

## Publication Blocker: Merge Retention

The [actual-group retention audit](merge-retention.json) preserves only 198 of
220 accepted amount quotes and 184 complete evidence entries. All 220 remain
intact in the authoritative normalized records. A successful source pass is not
a successful canonical publication gate.

| KOMODO medium | Accepted | Full entries retained | Amount quotes retained | Mapping/references/event retained |
| --- | ---: | ---: | ---: | --- |
| 570 | 5 | 0 | 5 | no |
| 572 | 3 | 0 | 3 | no |
| 617a | 3 | 0 | 0 | no |
| 624 | 10 | 0 | 0 | yes |
| 625 | 6 | 0 | 6 | no |
| 656 | 2 | 0 | 0 | yes |
| 729 | 3 | 0 | 0 | yes |
| 774 | 4 | 0 | 0 | no |

Exact paths and all competing group members are in the audit. For example,
617a groups with 617 and multiple nutrient-agar records; 774 groups with several
other peptone/yeast/glucose/agar formulations. Shared ingredient fingerprints
do not establish exact concentration or preparation equivalence. Do not repair
this by copying evidence indiscriminately across different formulations.

Code inspection explains the loss mechanism: `RecipeMerger.merge_group` copies
one canonical record (line 87), while `_merge_ingredients` independently selects
one ingredient list by ChEBI annotation count (lines 347-363 of
`src/culturemech/merge/merger.py`). It does not reconcile source-scoped evidence
across exact formulations. Root provenance from another group member can also
be omitted. This is a maintained merge-rule issue, not a missing snippet in the
new normalized edits.

Required follow-up: separate exact formulations and genuine variants in the
maintained merge path, preserve source-scoped provenance and append-only events,
then rerun actual-group retention and global merge/freshness gates. No generated
merge was replaced or published by this cohort. This file records local review
findings; it does not claim a new GitHub issue or completed merge fix.

## Unsupported Preliminary Claims

The initial machine preview would have supported 155 additional amount claims
across 23 records with unresolved source/preparation scope. These proposals were
removed before application using pinned source excerpts and hashes, and all 23
local records remain unchanged. The underlying formulation problems are still
open; withholding is not a repair. See [preparation findings](preparation-findings.md)
and [original-source handoff](original-source-handoff.md).

## Applied Change Checks

Independent inversion verifies that the 46 changes only append provenance;
all quantities, ingredient identities, stocks, preparation, variants and growth
claims are preserved. Each accepted excerpt is literal captured-source text,
with exact source membership, stated units and decimal arithmetic checked.
Source rows with unresolved qualifiers, optionality or inconsistent amounts
remain unsupported/conflicted. Mapping excerpts establish identity only.

The [report contract](report-contract.json) checks 500 unique exact git-tracked
paths, one Record line per report, all 19,371 claim rows, current result hashes,
and the cumulative coverage partition. No concentration evidence has been
propagated to source variants merely because their historical links say duplicate.

## Bibliographic Follow-up

The full reference gate fails even though all 266 individual snippets pass the
installed deterministic matcher. The captured mapping page's literal title is
`KOMODO - the Known Media Database`, not the descriptive title inserted by the
reviewer. The [source-pinned title handoff](reference-title-handoff.json) records
the exact excerpt and required guarded successor correction. This finding is
not dismissed as an API limitation. The separate MediaDive API checks use a
URL-as-title fallback; those do not establish a scientifically wrong recipe name.
Eight fetch errors also occurred. Cached snippet success is not uninterrupted
live source availability, nor a full reference-gate pass.

Schema/test passes do not resolve these failures or make unsupported amounts
verified. Product validation passes with warnings and adapter skips; see the
batch README for exact counts and the partial-runtime limitation.

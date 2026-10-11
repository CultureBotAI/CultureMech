# MediaDive Solution Evidence: Records 500-999

Status: **applied locally; all-record curation remains incomplete**.

This batch covers offsets `[500:1000]` of the frozen
[source inventory](../20261007-source-inventory.json): 500 exact tracked paths,
from solution 672 through solution 1382, with gaps. It continues the
[first batch's source and evidence contract](../20261007-mediadive-solutions-0000-0500/README.md).
The [pinned plan](plan.json) and [per-record reports](records/) retain every
decision, source hash, exact snippet, locator, old/new quantity, and record hash.

## Results

| Result | Count |
| --- | ---: |
| Records processed / changed / unchanged | 500 / 412 / 88 |
| Operational failures / schema-blocked records | 0 / 0 |
| Water quantity/unit corrections | 159 |
| Unchanged mass concentrations receiving evidence | 2,110 |
| New ingredient-level evidence entries | 2,269 |
| Unsupported / conflicting claim rows retained | 1,654 / 232 |

The 4,155 decision rows include 326 source-only ingredient or stock references;
they are not 4,155 independent media. No ingredient membership, identity, role,
growth association, or prior provenance was rewritten. Only supported quantity
objects and append-only evidence, bibliography, and curation history changed.

For example, solution 672's table states 870 ml distilled water. Its old
`944.6254071661239 PERCENT_V_V` becomes `0.87 L` per batch, not a final-volume
claim. Five unchanged mass concentrations in that record receive evidence for
the source's explicit `g_l` values and declared 921 ml solution volume. Its
brand/stock-strength attributes and two missing nested stock references remain
unresolved; this is not a complete formulation repair.

Every accepted claim has its exact official DSMZ source URL and JSON snippet in
the YAML, plus field scope, calculation, retrieval timestamp, and response hash.
Bibliographies include title, source type, discovery mode, source organization,
and access date. Individual authors, publication year, and DOI were not supplied
by these responses and were not invented.

## Unresolved Decisions

The 1,886 unchanged unresolved rows comprise:

- 500 legacy placeholder/other out-of-scope-context rows.
- 423 stock-strength, brand, or material-grade attributes.
- 326 source-only ingredients or nested stocks.
- 264 water rows requiring preparation-instruction review.
- 227 disagreements between source `g_l`, amount, unit, and volume.
- 88 other unit/liquid contexts and 42 optional/conditional rows.
- 11 missing numeric inputs, 4 ambiguous compound matches, and 1 exact-label mismatch.

For instance, solution 687 declares 1002 ml volume but reports salt `g_l` values
equal to the masses in grams. Those arithmetic conflicts were not converted into
SUPPORT evidence. Source statements are retained, not averaged or silently fixed.

## Verification And Baseline

- All 500 sources retrieved successfully; source origin, response ID, status,
  raw-byte SHA256, and capture timestamp checked.
- All 500 baseline and proposed records passed closed-schema validation;
  write-time validation and whole-batch hash preflight ran before edits.
- Read-back checked all 500 record hashes and **2,269 exact new snippets**.
- Full-corpus baseline `just validate-strict --workers 1` passed for all
  **15,910 records**; `just assign-ids-check` also passed.
- The 164-test regression selection passed before apply. Final post-edit checks
  and cumulative counts are recorded in the [curation status](../README.md).
- `linkml-reference-validator` remains unavailable in the isolated Python 3.11
  runtime; `oaklib` is also absent. Source retrieval and exact snippet checks
  above are separate from those unavailable automated validators.
- Standalone solution composition edits leave merge fingerprints unchanged.
  Existing full merge-gate failures remain unresolved; no generated merges or
  pages were hand-edited or regenerated for this excluded solution-only batch.

The local reviewed commit remains
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. A fresh fetch during this batch found
`origin/main` at `62d4ea2934` (shared-schema synchronization, PR #568). Its diff
adds cross-corpus links and does not change the concentration fields used here.
The dirty curation branch was not rebased or merged automatically.

The source review is automated exact-ID/form/arithmetic checking, supplemented
by inspection of representative sources and conflicts. It is not a claim that
every sentence in every source has been manually read or every record finished.
The next inventory slice begins at offset 1000; unresolved rows remain in scope.

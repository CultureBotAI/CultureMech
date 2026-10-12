# MediaDive Solution Evidence: Records 1000-1499

Status: **applied locally; all-record curation remains incomplete**.

This batch covers offsets `[1000:1500]` of the frozen
[source inventory](../20261007-source-inventory.json): 500 exact tracked paths,
from solution 1383 through solution 2017, with gaps. It uses the
[established evidence contract](../20261007-mediadive-solutions-0000-0500/README.md).
The [pinned plan](plan.json) and [per-record reports](records/) include source
hashes, exact snippets, locators, decisions, and before/after record hashes.

## Results

| Result | Count |
| --- | ---: |
| Records processed / changed / unchanged | 500 / 461 / 39 |
| Operational failures / schema-blocked records | 0 / 0 |
| Water quantity/unit corrections | 129 |
| Unchanged mass concentrations receiving evidence | 2,752 |
| New ingredient-level evidence entries | 2,881 |
| Unsupported / conflicting claim rows retained | 1,904 / 173 |

All 4,958 decision rows are retained, including 439 source-only ingredients or
stock additions. Accepted quantities describe this exact solution, not a dose or
final concentration in a receiving medium. Water additions are represented in
liters per batch; final volume is never inferred from a water row alone.

Each accepted claim has its official DSMZ source URL, exact JSON snippet, field
scope, calculation, retrieval timestamp, and source-response hash in the YAML.
Bibliographies include source title, type, discovery mode, organization, and
access date. These responses do not supply individual authors or publication
year; neither those fields nor a DOI was invented. Prior evidence/history,
ingredient membership, identities, roles, and growth associations were preserved.

## Unresolved Decisions

The 2,077 unchanged unresolved rows comprise:

- 499 legacy placeholder/other out-of-scope-context rows.
- 471 stock-strength, brand, or material-grade attributes.
- 439 source-only ingredients or nested stocks.
- 326 water rows requiring preparation-instruction review.
- 166 disagreements between source `g_l`, amount, unit, and volume.
- 92 other unit/liquid contexts and 40 optional/conditional rows.
- 33 missing numeric inputs and 4 nonpositive source volumes.
- 4 ambiguous compound matches and 3 ingredient-inventory identity conflicts.

Source 1383 illustrates the amount/unit check: its copper sulfate pentahydrate
row specifies 1 mg and `g_l=0.001` for a declared 1000 ml solution. The existing
`0.001 G_PER_L` is unchanged and now has evidence. Its 1000 ml water addition is
corrected from `1000 PERCENT_V_V` to `1 L` per batch.

**Separate identity issue:** that same record's `Na2MoO4 x H2O` source/local
ingredient label is accompanied by a local secondary ChEBI label `sodium molybdate
(anhydrous)`. The concentration evidence is scoped to upstream compound 641 and
its exact stated form; it does not validate that secondary ontology mapping.
Reconcile the hydrate form with primary ontology evidence in the identity review.
No replacement ontology ID was guessed in this concentration batch.

Solution 1939 was already curated to CHEBI-rooted ingredient IDs and no longer
has a legacy `ingredients` placeholder. Automatic matching against upstream
compound IDs is intentionally unresolved, not treated as permission to replace
its prior curation. Its original concentrations and record bytes remain unchanged.

## Verification And Reviewer Fix

- All 500 sources retrieved successfully as part of the
  [1,000-source retrieval](../20261007-source-fetch-0500-1500.json).
- All baseline and proposed records passed closed-schema validation; the whole
  batch was hash-preflighted and write-time validated before recipe edits.
- Read-back checked all 500 result hashes and **2,881 exact new snippets**.
- A second apply changed zero records and recognized all 461 applied results.
- The first preview exposed a reviewer error on solution 1939: the media
  fingerprinter rejects a missing `ingredients` key, although that key is optional
  for a valid `SolutionRecipe`. The failed preview was archived outside the
  repository and never applied. A new preview was generated after the fix.
- The reviewer now proves that the actual merger inputs (`ingredients` and
  `solutions`, including key presence) are identical before/after; it additionally
  compares fingerprints when an ingredient list is present. Four new tests cover
  absent placeholders, preserved scientific conflicts, and rejection of changes
  to either merger input field. This does not change the merger itself.
- Across both new 500-record batches, 999 records have null media fingerprints;
  solution 1939 is also excluded by the merger because its ingredient list is
  absent. No generated merge/page output was patched. Existing full merge-gate
  failures remain unresolved.
- Full-corpus baseline validation and the ID gate passed. Final post-edit corpus
  validation and regression results are recorded in the [curation status](../README.md).
- Ontology/reference validator packages remain unavailable in the isolated
  Python 3.11 runtime. Actual source retrieval and exact snippet/arithmetic checks
  above are not represented as passes of those validators.

Local baseline: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. A fresh remote check
found `origin/main` at `62d4ea2934`, with unrelated shared cross-corpus-link schema
additions; the dirty branch was not automatically rebased.

This is structured-source verification with representative manual source and
conflict inspection, not manual reading of every source sentence or complete
scientific verification of every record. Resume the frozen inventory at offset
**1500**, solution **2018**, `CultureMech:011421`; **3,270** further records need
this pass. Unresolved rows and the rest of the normalized corpus remain in scope.

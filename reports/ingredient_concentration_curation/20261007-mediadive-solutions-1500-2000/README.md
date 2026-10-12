# MediaDive Solution Evidence: Records 1500-1999

Status: **applied locally; the all-record objective remains incomplete**.

This batch covers offsets `[1500:2000]` of the frozen
[source inventory](../20261007-source-inventory.json), solution IDs 2018 through
2656 with gaps. The [pinned plan](plan.json) and [500 per-record reports](records/)
retain exact paths, stable IDs, original/proposed amounts, decisions, raw-source
hashes, snippets, locators, and before/after record hashes. It follows the
[established evidence contract](../20261007-mediadive-solutions-0000-0500/README.md).

| Result | Count |
| --- | ---: |
| Records processed / changed / unchanged | 500 / 457 / 43 |
| Operational failures / schema-blocked records | 0 / 0 |
| Water quantity/unit corrections | 99 |
| Unchanged mass concentrations receiving evidence | 2,723 |
| New ingredient evidence entries | 2,822 |
| Unsupported / conflicting claim rows retained | 1,805 / 149 |

There are 4,776 decision rows, including 407 source-only ingredient or stock
references. Each accepted claim has an official source URL, exact JSON excerpt,
field scope, arithmetic explanation, retrieval timestamp, and response hash in
the YAML. Bibliographies identify source title/type, discovery mode, organization,
and access date; unavailable individual-author and publication-year metadata were
not fabricated. Water corrections preserve batch addition amounts in liters,
not an assumed final volume. Existing mass concentrations did not change.

## Unresolved Work

The 1,954 unchanged unresolved rows comprise 499 legacy placeholder/other-context
rows, 407 source-only stock/ingredient references, 399 source attributes, 335
water preparation contexts, 110 source arithmetic disagreements, 107 other
unit/liquid contexts, 56 optional/conditional rows, 24 ambiguous compound matches,
15 ingredient-inventory conflicts, one missing numeric input, and one source zero.

Solution 2018 illustrates partial scope: four unchanged mass concentrations gain
evidence, while its optional agar, legacy placeholder, and preparation-dependent
water row remain outside this automatic application. A per-record report is not
a claim that the complete recipe or every ontology mapping is now verified.
All unresolved values, source disagreements, and preparation context remain
visible rather than being replaced by inferred numbers.

## Verification

- All 500 official sources retrieved successfully; source origin, ID, status,
  bytes, and metadata checked.
- All baseline and proposed records passed closed-schema validation, with
  write-time validation and whole-batch hash preflight before edits.
- Read-back matched all 500 record hashes and all **2,822** new source snippets.
- An idempotence rerun changed zero records and recognized 457 applied results.
- Reviewer plus current batch-integrity tests: **40 passed** after this batch.
  The final wider regression selection is recorded in the [status](../README.md).
- Full baseline schema and ID gates passed for all **15,910** normalized records.
  Final post-edit corpus validation is recorded in the status after the full run.
- Actual merger input fields (`ingredients` and `solutions`, including key
  presence) stayed unchanged; fingerprint checks passed where applicable. The
  standalone compositions remain excluded by the current merger. Existing merge
  failures are not claimed fixed, and no generated merge/page output was patched.
- Unavailable ontology/reference validators remain distinct from the successful
  source retrieval, exact-snippet, arithmetic, and schema checks.

Local reviewed baseline: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`; freshly fetched
`origin/main`: `62d4ea2934df4ee85dbe3e1c2f5c89a5d069960b`. No IDs, ingredient
membership, roles, growth associations, or prior provenance were rewritten.
Source verification is structured exact-ID/form/arithmetic checking plus
representative manual inspection, not manual reading of every source sentence.
The next inventory slice begins at offset 2000; the full corpus and unresolved
claims remain in scope.

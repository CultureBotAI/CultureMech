# MediaDive Solution Evidence: Records 2000-2499

Status: **applied locally; the all-record objective remains incomplete**.

This batch covers offsets `[2000:2500]` of the frozen
[source inventory](../20261007-source-inventory.json), solution IDs 2657 through
3397 with gaps. The [pinned plan](plan.json) and [500 per-record reports](records/)
retain exact paths, stable IDs, original/proposed amounts, decisions, raw-source
hashes, snippets, locators, and before/after record hashes. It follows the
[established evidence contract](../20261007-mediadive-solutions-0000-0500/README.md).

| Result | Count |
| --- | ---: |
| Records processed / changed / unchanged | 500 / 442 / 58 |
| Operational failures / schema-blocked records | 0 / 0 |
| Water quantity/unit corrections | 102 |
| Unchanged mass concentrations receiving evidence | 2,692 |
| New ingredient evidence entries | 2,794 |
| Unsupported / conflicting claim rows retained | 1,830 / 185 |

There are 4,809 decision rows, including 398 source-only ingredient or stock
references. Each accepted claim has an official source URL, exact JSON excerpt,
field scope, arithmetic explanation, retrieval timestamp, and response hash in
the YAML. Bibliographies identify source title/type, discovery mode, organization,
and access date; unavailable individual-author and publication-year metadata were
not fabricated. Water corrections preserve batch addition amounts in liters,
not an assumed final volume. Existing mass concentrations did not change.

## Unresolved Work

The 2,015 unresolved rows comprise 494 legacy placeholder/other-context rows,
398 source-only stock/ingredient references, 360 source attributes, 342 water
preparation contexts, 148 source arithmetic disagreements, 112 other unit/liquid
contexts, 101 optional/conditional rows, 16 ambiguous compound matches, 15 missing
numeric inputs, 15 exact solution-ID/name mismatches, eight nonpositive source
volumes, and six ingredient-inventory conflicts. These values remain unchanged.

Solution 2683, Carbonate Salts Solution, was inspected as a representative
correction: its source specifies 5 g each of NaHCO3 and Na2CO3 in the declared
500 mL solution, with `g_l: 10` for each. The existing mass concentrations remain
10 g/L with new evidence. Its 500 mL batch water addition was corrected from the
imported 1000% value to 0.5 L, with an exact source snippet; the source has an
explicit empty preparation-step list and no competing local instruction.

## Verification

- All 500 sources were captured from the official endpoint with checked origin,
  source ID, status, bytes, and metadata.
- All baseline and proposed records passed closed-schema validation, including
  whole-batch hash preflight and write-time validation.
- Read-back matched all 500 record hashes and all **2,794** new source snippets.
- An idempotence rerun changed zero records and recognized 442 applied results.
- Reviewer and current batch-integrity tests: **46 passed** after this batch.
  The final wider selection is recorded in the [status](../README.md).
- Merge input fields (`ingredients` and `solutions`, including key presence)
  remained unchanged; fingerprints were checked where applicable. No generated
  merge/page files were patched; existing merge issues are not claimed fixed.
- Source name whitespace is preserved in data and the plan; only report headings
  are trimmed. Missing or malformed preparation-step metadata cannot authorize a
  water correction.
- Ontology/reference validator availability is reported separately from schema,
  source, and exact-snippet checks.

Reviewed local baseline: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.
IDs, ingredient membership, roles, growth associations, and prior provenance were
preserved. Source verification is structured exact-ID/form/arithmetic checking
plus representative manual inspection, not manual reading of every source
sentence. The next slice starts at offset 2500; the full corpus and unresolved
claims remain in scope.

# MediaDive Solution Evidence: Records 4500-4769

Status: **applied locally; the all-record objective remains incomplete**.

This final slice covers offsets `[4500:4770]` of the frozen
[source inventory](../20261007-source-inventory.json), source IDs 6014 through
6571 with gaps. The [plan](plan.json) and [270 per-record reports](records/)
retain exact tracked paths, stable IDs, old/new quantities, decisions, source
hashes, literal snippets, locators, calculations, and before/after record hashes.

| Result | Count |
| --- | ---: |
| Records processed / changed / unchanged | 270 / 150 / 120 |
| Operational failures / schema-blocked records | 0 / 0 |
| Water quantity/unit corrections | 15 |
| Unchanged mass concentrations receiving evidence | 517 |
| New ingredient evidence entries | 532 |
| Unsupported / conflicting claim rows retained | 1,119 / 22 |

The 1,673 decision rows include 201 source-only ingredient/stock references.
Each accepted claim has an official source URL, exact excerpt, scope, arithmetic,
retrieval timestamp, and response hash in YAML. Source title/type/discovery/
organization/access metadata are recorded; missing authors/year are not invented.
Water changes represent batch additions in liters, not final concentrations.
Mass values remain unchanged with evidence for provider-declared concentrations.

## Unresolved Work

The 1,141 unresolved rows comprise 371 source attributes, 265 placeholder or
other-context rows, 201 source-only ingredients/stocks, 109 missing numeric
inputs, 99 other unit/liquid contexts, 45 water preparation contexts, 27 optional
or conditional rows, 13 source inventory conflicts, seven exact ID/name
mismatches, two source-zero contexts, one source arithmetic conflict, and one
existing mass-value conflict. These were not converted into supported claims.

Representative manual inspection of solution 6248 (A-5 Trace Metals) confirmed
the six exact salt/hydrate forms and their amounts against its declared 1000 mL
stock volume. The existing mass concentrations remain unchanged. Its explicit
1000 mL water addition becomes 1 L per batch, with an empty source preparation
step list and no competing local instruction. No final-medium amount is inferred.

## Verification

Baseline/proposed schema checks, source captures, write-time validation, and
whole-batch hash preflight passed. Read-back matched all 270 result hashes and
all **532** new snippets. A rerun changed zero records and recognized 150 applied
results. Wider regression/corpus checks are recorded in the cumulative
[status](../README.md).

The maintained reviewer preserved merge input fields, ingredient identity and
membership, stable IDs, and prior evidence/history. No generated files were
patched. All 4,770 pending root solution records now have this source pass;
unresolved claims, receiving recipes, nested stocks, and variants still require
review. This is not a completed all-record scientific review.

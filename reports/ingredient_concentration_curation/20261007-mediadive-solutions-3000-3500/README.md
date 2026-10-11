# MediaDive Solution Evidence: Records 3000-3499

Status: **applied locally; the all-record objective remains incomplete**.

This batch covers offsets `[3000:3500]` of the frozen
[source inventory](../20261007-source-inventory.json), source IDs 4030 through
4677 with gaps. The [plan](plan.json) and [500 per-record reports](records/)
retain exact paths/IDs, old/new quantities, decisions, source hashes, literal
snippets, locators, arithmetic, and before/after record hashes.

| Result | Count |
| --- | ---: |
| Records processed / changed / unchanged | 500 / 465 / 35 |
| Operational failures / schema-blocked records | 0 / 0 |
| Water quantity/unit corrections | 120 |
| Unchanged mass concentrations receiving evidence | 2,664 |
| New ingredient evidence entries | 2,784 |
| Unsupported / conflicting claim rows retained | 1,940 / 47 |

The 4,771 decision rows include 431 source-only ingredient/stock references.
Each accepted claim has an official source URL, exact excerpt, claim scope,
conversion explanation, retrieval timestamp, and response hash in YAML. Source
title/type/discovery/organization/access metadata are recorded; missing authors
and publication year were not invented. Water values represent batch additions
in liters, not final-medium volume or percentages. Mass quantities are unchanged.

## Unresolved Work

The 1,987 unresolved rows comprise 556 source attributes, 498 placeholder or
other-context rows, 431 source-only ingredients/stocks, 311 water preparation
contexts, 95 missing numeric inputs, 39 other unit/liquid contexts, 22 source
arithmetic conflicts, 21 ingredient-inventory conflicts, ten optional/conditional
rows, and four ambiguous compound matches. They remain unchanged.

Representative manual inspection of solution 4032 (Main sol. J317) checked the
complete source and local record. Its 1000 mL water batch addition becomes 1 L;
the provider's separate 1004 mL volume is not mistaken for delivered water or a
measured final volume. Its brand-specific yeast extract and three omitted stock
references remain unresolved rather than having their context discarded.

## Verification

All 500 source captures, baseline/proposed schema checks, write-time validation,
and whole-batch hash preflight passed. Read-back matched 500 result hashes and
**2,784** exact source snippets. An idempotence rerun changed zero records and
recognized 465 applied results. Merge input fields are unchanged; no generated
files were edited. Final test/corpus results and unavailable external validators
are recorded in the cumulative [status](../README.md).

Source verification combines structured exact-ID/form/arithmetic checks with
representative manual inspection; it does not claim every source sentence or
secondary ontology mapping was manually validated. The next slice begins at
offset 3500. No growth associations, IDs, ingredient identities/membership, or
prior provenance were rewritten.

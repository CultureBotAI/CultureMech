# MediaDive Solution Evidence: Records 4000-4499

Status: **applied locally; the all-record objective remains incomplete**.

This batch covers offsets `[4000:4500]` of the frozen
[source inventory](../20261007-source-inventory.json), source IDs 5266 through
6013 with gaps. The [plan](plan.json) and [500 per-record reports](records/)
retain exact paths/IDs, old/new quantities, decisions, source hashes, literal
snippets, locators, arithmetic, and before/after record hashes.

| Result | Count |
| --- | ---: |
| Records processed / changed / unchanged | 500 / 409 / 91 |
| Operational failures / schema-blocked records | 0 / 0 |
| Water quantity/unit corrections | 114 |
| Unchanged mass concentrations receiving evidence | 2,086 |
| New ingredient evidence entries | 2,200 |
| Unsupported / conflicting claim rows retained | 2,135 / 82 |

The 4,417 decision rows include 422 source-only ingredient/stock references.
Each accepted claim has an official source URL, exact excerpt, scope, arithmetic,
retrieval timestamp, and response hash in YAML. Source title/type/discovery/
organization/access metadata are recorded; absent authors and year were not
invented. Water values represent batch additions in liters; mass values are
unchanged and evidence is scoped to provider-declared stock concentrations.

## Unresolved Work

The 2,217 unresolved rows comprise 707 source attributes, 499 placeholder or
other-context rows, 422 source-only ingredients/stocks, 233 water preparation
contexts, 115 missing numeric inputs, 110 other unit/liquid contexts, 43 ambiguous
matches, 40 optional/conditional rows, 34 source arithmetic conflicts, nine
nonpositive source volumes, and five exact solution-ID/name mismatches.

Representative manual inspection of solution 5281 (Mineral solution) confirmed
three exact salt/hydrate forms and their 25, 37.5, and 0.3 g amounts with an
explicit provider-declared 1000 mL solution volume. The corresponding g/L values
remain unchanged with evidence. Its 1000 mL batch water addition becomes 1 L;
the source has an explicit empty step list and no competing local instruction.

## Verification

All baseline/proposed schema checks, source captures, write-time validation, and
whole-batch hash preflight passed. Read-back matched 500 result hashes and
**2,200** exact source snippets. An idempotence rerun changed zero records and
recognized 409 applied results. Reviewer and nine-batch integrity checks passed
**50 tests**. Final corpus/wider regression results and unavailable external
validators are recorded in the cumulative [status](../README.md).

Merge input fields stayed unchanged; no generated files were patched. The next
slice begins at offset 4500. Structured source checking and representative manual
inspection do not establish full scientific verification of unresolved claims or
secondary ontology mappings. No growth associations, IDs, ingredient identities/
membership, or previous provenance were rewritten.

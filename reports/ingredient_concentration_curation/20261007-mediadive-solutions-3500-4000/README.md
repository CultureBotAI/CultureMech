# MediaDive Solution Evidence: Records 3500-3999

Status: **applied locally; the all-record objective remains incomplete**.

This batch covers offsets `[3500:4000]` of the frozen
[source inventory](../20261007-source-inventory.json), source IDs 4678 through
5265 with gaps. The [plan](plan.json) and [500 per-record reports](records/)
retain exact paths/IDs, old/new quantities, decisions, source hashes, literal
snippets, locators, arithmetic, and before/after record hashes.

| Result | Count |
| --- | ---: |
| Records processed / changed / unchanged | 500 / 443 / 57 |
| Operational failures / schema-blocked records | 0 / 0 |
| Water quantity/unit corrections | 103 |
| Unchanged mass concentrations receiving evidence | 2,720 |
| New ingredient evidence entries | 2,823 |
| Unsupported / conflicting claim rows retained | 2,433 / 182 |

The 5,438 decision rows include 613 source-only ingredient/stock references.
Each accepted claim has an official source URL, exact excerpt, scope, arithmetic,
retrieval timestamp, and hash in YAML. Source title/type/discovery/organization/
access metadata are recorded; missing authors and year were not invented. Water
values represent batch additions in liters, not final-medium volume or percentages.

## Unresolved Work

The 2,615 unresolved rows comprise 891 source attributes, 613 source-only
ingredients/stocks, 490 placeholder or other-context rows, 296 water preparation
contexts, 116 ingredient-inventory conflicts, 100 missing numeric inputs, 37
source arithmetic conflicts, 36 other unit/liquid contexts, 28 ambiguous matches,
seven optional/conditional rows, and one existing mass-concentration conflict.

Representative manual inspection of solution 4697 (Substrate solution) confirmed
the exact local/source identities, two 12.5 g components, declared 100 mL volume,
and explicit 125 g/L values. Existing mass concentrations remain unchanged with
evidence; its 100 mL batch water addition becomes 0.1 L, not 1000%.

The previously curated solution 4941 (Main sol. J930) remains unchanged. Its NaCl
value is 15 g/L, but the API reports 13.6364 g/L using a declared 1100 mL volume.
Manual inspection of the [original JCM 930 table](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=930)
found 1 L basal medium, 100 mL serum, and 15 g NaCl, with percentages in its title.
The table supplies batch additions, not an explicit final-volume instruction.
Neither reinterpretation of the earlier curation nor automatic replacement by
the API denominator is justified by this check. The report retains that conflict.

## Verification

All baseline/proposed schema checks, source captures, write-time validation, and
whole-batch hash preflight passed. Read-back matched all 500 result hashes and
**2,823** literal source snippets. An idempotence rerun changed zero records and
recognized 443 applied results. Reviewer and eight-batch integrity tests passed
**49 tests**. Final corpus/wider regression results and unavailable external
validators are recorded in the cumulative [status](../README.md).

Merge input fields stayed unchanged; no generated files were patched. The next
slice begins at offset 4000. Exact-ID/form/arithmetic checking and representative
manual inspection do not imply full verification of unresolved fields, secondary
ontology mappings, or every source sentence. No growth associations, IDs,
ingredient identities/membership, or previous provenance were rewritten.

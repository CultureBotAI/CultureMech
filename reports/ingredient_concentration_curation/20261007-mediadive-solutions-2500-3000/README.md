# MediaDive Solution Evidence: Records 2500-2999

Status: **applied locally; the all-record objective remains incomplete**.

This batch covers offsets `[2500:3000]` of the frozen
[source inventory](../20261007-source-inventory.json), solution IDs 3398 through
4029 with gaps. The [pinned plan](plan.json) and [500 per-record reports](records/)
retain exact paths, stable IDs, original/proposed amounts, decisions, raw-source
hashes, snippets, locators, and before/after record hashes. It follows the
[established evidence contract](../20261007-mediadive-solutions-0000-0500/README.md).

| Result | Count |
| --- | ---: |
| Records processed / changed / unchanged | 500 / 445 / 55 |
| Operational failures / schema-blocked records | 0 / 0 |
| Water quantity/unit corrections | 103 |
| Unchanged mass concentrations receiving evidence | 2,376 |
| New ingredient evidence entries | 2,479 |
| Unsupported / conflicting claim rows retained | 1,837 / 108 |

There are 4,424 decision rows, including 317 source-only ingredient or stock
references. Each accepted claim has an official source URL, exact JSON excerpt,
field scope, arithmetic explanation, retrieval timestamp, and response hash in
the YAML. Bibliographies identify source title/type, discovery mode, organization,
and access date; unavailable individual-author and publication-year metadata were
not fabricated. Water corrections preserve batch addition amounts in liters,
not an assumed final volume. Existing mass concentrations did not change.

## Unresolved Work

The 1,945 unresolved rows comprise 505 source attributes, 493 legacy
placeholder/other-context rows, 317 source-only stock/ingredient references,
295 water preparation contexts, 94 missing numeric inputs, 91 other unit/liquid
contexts, 53 source arithmetic disagreements, 45 ingredient-inventory conflicts,
42 optional/conditional rows, and ten ambiguous compound matches. These values
remain unchanged.

Representative manual source/record inspection covered solution 3398, whose
three source-only stock doses and preparation-dependent water remain unresolved,
and solution 3409 (Se/W solution). The latter specifies 4 mg each of Na2SeO3 and
Na2WO4 with `g_l: 0.004` and an explicit 1000 mL solution volume. Both mass
concentrations remain unchanged with evidence; its 1000 mL batch water addition
was corrected from 1000% to 1 L. The source has an explicit empty step list, and
the local record supplies no competing preparation instruction.

Source 3435 illustrates why source arithmetic disagreements are not silently
corrected: its NaCl row reports 70 g and `g_l: 3500`, although the source root
volume is 1000 mL. It also repeats sulfide and cysteine as mass and stock-addition
rows. That formulation requires original-recipe and preparation-stage review,
not a blanket divide-by-50 replacement.

The [original DSMZ 1656 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1656.pdf)
was downloaded on 2026-10-07 and both rendered pages were inspected. Page 1's
main table states `NaCl 70.00 g`, but gives no main-batch water or final-volume
line; the two water rows belong to separately headed stock recipes. Page 2
describes post-sterilization stock additions, with inconsistent cysteine versus
cysteine-hydrochloride wording. Consequently neither 3500 g/L nor a replacement
70 g/L is established by this PDF alone. The original-source check confirms an
unresolved denominator/preparation-stage gap, not permission to infer a liter.
PDF SHA256: `622a5a42dfa765150c788126116b7f9b725dfff2d743537c688992b3c6d238b6`.
Its 2012 copyright notice is not treated as a verified publication year. No
scientific YAML field was changed by this follow-up investigation.

## Verification

- All 500 inventory hashes matched before preview; official source captures
  passed origin, source ID, status, byte-hash, and metadata checks.
- All baseline and proposed records passed closed-schema validation, including
  whole-batch hash preflight and write-time validation.
- Read-back matched all 500 record hashes and all **2,479** new source snippets.
- An idempotence rerun changed zero records and recognized 445 applied results.
- The full relevant regression selection passed **178 tests** after this batch.
- A cumulative read-back across all six source-review batches matched all 3,000
  result hashes and 15,567 source snippets. The independent semantic diff and
  post-edit corpus gates are recorded in the [status](../README.md).
- Actual merger input fields (`ingredients` and `solutions`, including key
  presence) remain unchanged. No generated merge/page files were patched.
- `validate-products` could not load ontology adapters because `oaklib` is not
  installed in the isolated runtime. `validate-references` on solution 3409
  exited 2 because `linkml-reference-validator` could not be spawned. Neither
  unavailable check is counted as a pass or as a newly introduced data defect.

Reviewed local baseline: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.
No IDs, ingredient membership, roles, growth associations, or earlier provenance
were rewritten. Source verification combines structured exact-ID/form/arithmetic
checks and representative manual inspection, not manual reading of every source
sentence. The next slice starts at offset 3000, solution 4030; 1,770 further
inventory records, other record types, and unresolved claims remain in scope.

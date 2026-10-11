# Medium212 Ingredient Curation

This is an unapplied, full-family successor preview (`plan-v2.json`), not completed curation. The complete
15,910-record objective remains active. Local HEAD is
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`; upstream was not refreshed and no
GitHub action is claimed.

## Scope

- 22 exact normalized paths: four media and eighteen standalone preparations.
- 25 hash-bound primary captures, including two original DSMZ PDFs and the
  BacDive strain page. The seven PDF pages have an earlier retained visual review.
- 271 source quantity rows and 259 old quantity fields accounted for.
- 21 proposed edits; S608 remains a byte-exact no-op.
- 887 evidence-linked claims, proposing 186 added evidence entries, six
  references and 21 history events. These are not applied cumulative additions.
- 69 existing evidence entries retain their content; fourteen explanations gain
  append-only context. Exact evidence-entry equality is not claimed for those
  fourteen entries. The first preview and its original ledgers remain immutable;
  current per-record ledgers are in `records-ledgers-successor/`.

## Scientific Decisions

KOMODO, original DSMZ212, original DSMZ212a and BacDive DSM2805 are separate
source formulations. The preview restores their own rates or preparation stages
and removes the false K212/DSMZ212a duplicate relationship. BacDive quantities
are source-reported strain-specific rates, not recalculations from rounded DSMZ
instructions; no organism-growth association is added.

The DSMZ root inputs total 1003 ml and 1008 ml respectively, but neither original
states that sum is a final-volume make-up. Solution A also contains a stated-dose
versus listed-liquid-input discrepancy: 942 versus 942.5 ml and 917 versus
916.6 ml. Forty-nine original batch masses stay in notes without an invented
concentration denominator. SL-10 alone supplies an explicit final-volume
instruction. Standalone API stock rates remain provider-qualified.

Five old quantities misrepresent liquid inputs: vitamin K1 and 95% ethanol in
S125, 0.1% w/v resazurin solution in S446/S453, and 25% HCl in S595. Their
preview values are the stated liquid amounts in liters; unknown density or
percentage basis is not inferred. Seventeen false composition placeholders and
their incomplete-composition flags are removed only after all source rows are
represented. Three unsupported high-metal flags are withdrawn, not set false.

Source authors and publication years remain unknown, not inferred from copyright
or retrieval dates. Evidence uses persistent source URLs. The BacDive DOI
redirect was located, but the versioned PDF was not inspected and no DOI-backed
claim is made.

## Validation

All 44 baseline schema/strict commands and all 44 successor schema/strict commands
pass. The successor presentation check preserves unchanged root spans and prior history.
The first focused run had 550 passes and two failures: corrupted recipe-level
snippets escaped the new auditor. That defect is fixed and both attacks are
retained. The corrected first-preview suite had 824 passes; the successor suite
has **827 passes**, with two dependency warnings. The independent successor
auditor covers all 271 source rows, 259 old quantities and 887 claims. The full
fast tier passes **13,255 tests**, with 16 skipped, 2,243 deselected and two
dependency warnings, in 2,122.23 seconds. The corpus, proposal and pinned code
hashes remain unchanged. This uses the existing partial Python 3.13 environment,
not clean CI or the complete test suite.

The first reference attempt could not find a maintained raw-cache entry and
failed with networking explicitly disabled. A successor uses the already
inspected, hash-bound captures and rechecks original PDF bytes and extraction.
The production validator has no BacDive page adapter; manual literal capture
verification is separate from an automated-adapter pass. All **241** supported
official-source checks pass for the successor. `references-successor.json`
deliberately does not claim a complete automated pass: B2805 is the sole adapter
gap. Its HTML-backed excerpts are checked by the independent auditor.

## Application Gate

Application is still disabled in the builder. The adversarial review identified a
chemical-form problem in five records: their generic nickel-chloride
grounding does not preserve the source's explicit hexahydrate. The packaged MIM
answer is itself marked REJECTED and must not become a replacement ID.
[The frozen identity disposition](identity-review.json) supports withdrawing
nine generic assertions while preserving the source label, supported quantity,
and S595's existing upstream compound accession. The successor implements and
independently checks those nine withdrawals, with no replacement chemical ID.
It also distinguishes evidence-only additions from numerical corrections and
names each withdrawn old ingredient in the ledger. These are preview fixes,
not applied recipe changes.

Do not overwrite the first preview or its failed receipts. The terminal
[preview validation](validation-preview.json) does not enable recipe writes;
a reviewed, hash-bound apply gate is still required. Complete application,
readback/no-op, corpus and merge gates, and reconcile per-record reports and
indexes. No YAML changes or publication are claimed by this checkpoint.
The [handoff](next-work.md) retains the exact successor hash, required gates and
full remaining scope. The two preview-ledger versions coexist with the prior
canonical reports for these 22 paths; the duplicate-rejecting coverage command
has not been rerun. Report reconciliation remains an explicit application task.

## Next Source Family

The four-record medium323 family is prepared, not edited. An ignored-inclusive
inventory found both exact media and both stock accessions, including S6552.
Five primary captures are retained: the earlier medium API plus four newly
downloaded public sources. The initial sandbox network failures are preserved.
The original PDF page was rendered and visually inspected; its twenty table
rows, twenty-one KOMODO rows, 62 old quantity fields and nine prior evidence
entries are captured in `next-323-source-inspection.json`.

The original states a 1002 ml final volume, while liquid inputs total 1001.90 ml;
the header, not additive volume, is the concentration denominator. Conditional
agar has a table-versus-procedure discrepancy. Provider mass rates derived from
liquid inputs are not automatically declared false; review their stated scope
separately from source-explicit batch doses. K323's nine nulls, carbonate form,
glucose identity and copied solid-state metadata need source-specific decisions.
No guarded proposal or completed review is claimed for that next family.

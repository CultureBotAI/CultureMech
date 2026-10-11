# Medium212 Ingredient Curation

The reviewed successor (`plan-v2.json`) is applied locally: 21 changed records
and one byte-exact no-op. Post-application validation is terminal in
`validation.json`; this is not an all-record completion claim. The complete 15,910-record objective
remains active. Local HEAD is
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`; upstream was not refreshed and no
GitHub action is claimed.

## Scope

- 22 exact normalized paths: four media and eighteen standalone preparations.
- 25 hash-bound primary captures, including two original DSMZ PDFs and the
  BacDive strain page. The seven PDF pages have an earlier retained visual review.
- 271 source quantity rows and 259 old quantity fields accounted for.
- 21 applied edits; S608 remains a byte-exact no-op.
- 887 evidence-linked claims, adding 186 evidence entries, six references and
  21 history events, verified by independent readback and cumulative accounting.
- 69 existing evidence entries retain their content; fourteen explanations gain
  append-only context. Exact evidence-entry equality is not claimed for those
  fourteen entries. The first preview and its original ledgers remain immutable;
  applied per-record ledgers are in `applied-records/`. The prior README,
  adversarial review and handoff remain archived in `preview-documents/`.

## Scientific Decisions

KOMODO, original DSMZ212, original DSMZ212a and BacDive DSM2805 are separate
source formulations. The applied successor restores their own rates or preparation stages
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
replacement values are the stated liquid amounts in liters; unknown density or
percentage basis is not inferred. Seventeen false composition placeholders and
their incomplete-composition flags are removed only after all source rows are
represented. Three unsupported high-metal flags are withdrawn, not set false.

Source authors and publication years remain unknown, not inferred from copyright
or retrieval dates. Evidence uses persistent source URLs. The BacDive DOI
redirect was located, but the versioned PDF was not inspected and no DOI-backed
claim is made.

## Preview Validation History

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

## Applied Validation

The guarded builder now requires the exact frozen preview validation and every
referenced receipt before application or verification. The adversarial review identified a
chemical-form problem in five records: their generic nickel-chloride
grounding does not preserve the source's explicit hexahydrate. The packaged MIM
answer is itself marked REJECTED and must not become a replacement ID.
[The frozen identity disposition](identity-review.json) supports withdrawing
nine generic assertions while preserving the source label, supported quantity,
and S595's existing upstream compound accession. The successor implements and
independently checks those nine withdrawals, with no replacement chemical ID.
It also distinguishes evidence-only additions from numerical corrections and
names each withdrawn old ingredient in the ledger. These fixes are now applied.

The new application regressions pass **837 tests**, including receipt tampering,
concurrent edits, symlinks, readback and no-op application. The initial test run
failed because its temporary fixture lacked a Git index; that receipt remains
preserved, and the successor fixture uses a real temporary repository.
`apply.json` confirms independent preview/applied audit equality and no changes
outside the 21 reviewed targets. All 44 actual-written schema/strict commands,
21 supported reference CLI commands and 241 supported reference checks pass.
The BacDive manual evidence check remains separate. Corpus strict/ID/product
checks pass. Six indexes are refreshed; runtime merging retains the four media
separately and excludes all eighteen standalone solutions. Post-application
presentation checks preserve unchanged root spans and prior history across
all 22 records. All **127 final QA tests** pass, as do Ruff, Black and whitespace
checks. The current fast-tier run passes **12,700 tests**, with 16 skipped,
2,829 deselected and two dependency warnings, in 1,622.17 seconds.
`test-selection.json` documents the changed selection: the application fixture
contains a normalized-data path, so the existing classifier assigns all 565
medium212 tests to the corpus tier. They pass separately within the 837-test
focused run. The eight follow-up coverage tests also belong to the corpus tier and
pass within the 127-test QA run. The historical preview fast count is not a
like-for-like comparison. The later Halobacteria tests have a separate receipt.

The serial runner stopped when its presentation output name collided with an
immutable initial-preview receipt. No receipt was overwritten. The helper now
uses `presentation-applied.json`; that actual-written check is terminal and
passing. Completed earlier phases were not restarted. The current fast-tier
receipt and final `validation.json` are terminal.

Global merge verification reports 1,247 name conflicts and 3,287 fingerprint
issues; freshness fails. These failures are not waived. The cumulative audit
records **5,263 edited records and 35,955 added evidence entries**. Canonical
follow-up coverage is **11,802 of 15,910**, with **4,108** outside the reports.
Report presence does not certify every concentration. The coverage check
excludes 44 immutable, explicitly marked preview ledgers, rejects duplicate
canonical reports and validates exact paths even for excluded previews.
All 22 canonical reports now link to applied ledgers.

Do not overwrite the first preview, successor preview or failed receipts.
`applied-plan.json` registers only the 21 changed records for cumulative
inversion, while the complete reviewed proposal and applied ledgers retain
the S608 no-op. The [handoff](next-work.md) retains the full remaining scope.
The applied checkpoint is validated locally; publication and all-record
completion are not claimed.

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
The later [source adjudication](next-323-adjudication.json) corrects an initial
interpretation: the existing D323/S599 resazurin rate is supported by the
0.1% w/v stock, 0.50 ml dose and explicit 1002 ml final volume. It needs
evidence, not a numerical correction. S599 water instead needs a unit correction
from percent to ml/L. S6552 provider-reported mass rates remain distinct from
unsupported percentages; no density is invented. Storage at -20 C supports
STORE rather than HEAT. Conditional agar, physical state and source-specific
identity decisions remain open. No guarded proposal or completed review is
claimed for that next family.

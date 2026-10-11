# KOMODO 650, 752, And 762 Preparation Repairs

Three authoritative normalized records are corrected locally. This is a
hash-linked follow-up to the existing 500-record report, not three additional
unique reviewed paths and not completion of the all-record objective.

## Corrections

- **650:** replace the imported pyruvate mass conversion with the source-explicit
  20 mM amount; correct 1000 ml tap water to 1 L batch input; restore pH,
  nitrogen/heat/autoclave instructions and the post-autoclave pyruvate addition.
- **752:** relocate manganese chloride tetrahydrate and iron sulfate heptahydrate
  into their explicit 0.36 g/L and 50 g/L stocks, with separate 0.001 L batch
  addition doses. Restore the 1 L water input. Apply only the liquid preparation
  instruction, not the source's distinct agar/carbonate alternative.
- **762:** relocate carbonate and bicarbonate into the separate preparation.
  Retain 5.4 g and 4.2 g input masses in evidence-backed notes and withdraw the
  misleading flattened concentration fields at that stage. Restore 0.9 L base
  water and 0.1 L preparation water. Neither 54/42 g/L stock strengths nor a
  numeric stock dose is asserted: the source gives water input, not final volume.

All twenty original ingredient nodes and their chemical identifiers are preserved
through explicit relocation/correction; unrelated fields and history are intact.
Fourteen unchanged g/L values are supported only as provider-declared nominal
main-recipe rates, not measured final-volume concentrations. There are **29 new
evidence entries, six references and three appended curation events**. The
separate count categories are two quantity/unit corrections, two stock-stage
concentration rebases, four ingredient relocations, five new quantity slots,
and two unsupported quantity-slot withdrawals. No growth association is added.

## Evidence

Amounts and preparation are supported by literal JSON excerpts from the captured
official [650](https://mediadive.dsmz.de/rest/medium/650),
[752](https://mediadive.dsmz.de/rest/medium/752), and
[762](https://mediadive.dsmz.de/rest/medium/762) responses. Hashes, retrieval dates,
locators and exact excerpts are stored in YAML and [plan.json](plan.json).
The source reader pins the preceding cohort's full inspected context and mapping
plan. The KOMODO mapping row establishes source identity only, never amounts.
Its new reference uses the actual captured HTML title, `KOMODO - the Known Media
Database`; earlier batches' descriptive-title problem is not silently rewritten.
Individual authors and publication years remain unknown, not invented.

The [original 650 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf)
and [762 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium762.pdf)
were text-inspected again and corroborate the pyruvate and separate-carbonate
instructions. The 752 PDF failed to open through the web tool; the official
[752 mobile recipe](https://www.bacmedia.dsmz.de/medium/752?mobile=1)
corroborates both metal stocks and the liquid/agar distinction. No PDF visual
inspection, new hashed PDF capture, or new PDF-backed YAML evidence is claimed.

## Verification

The preview and applied independent audits verify literal excerpts, explicit
conversion inputs, preparation boundaries and complete-record inversion.
`preflight.json` and `diff-audit.json` use early count labels
`ingredients_relocated` and `stock_concentrations_rebased`; the final audit uses
the cumulative auditor's existing labels `stock_nodes_relocated` and
`stock_stage_concentrations_rebased` for the same changes.

Baseline: 77 focused tests; all three open-schema checks; strict schema validation
of all 15,910 normalized records. Applied readback, no-op rerun, three open-schema
checks, full strict validation, IDs, and previous-cohort successor verification
passed. The post-edit focused suite passed 275 tests. The actual merge-group
retention check passes for all three repaired records, but it does not establish
equivalence with other group members. The global merge and freshness gates fail;
see [adversarial-review.md](adversarial-review.md) for exact findings and counts.

The first reference run ended with sandbox DNS failures, not a successful
validation. Its terminal state is recorded in `reference-validation.json`.
The network-enabled retry in `reference-network-validation.json` validates all
29 snippets against retrieved/cached content, but full reference validation still
fails on three API URL-as-title fallback mismatches. No source title was replaced
by a URL to bypass that gate. Product validation passes with 91 non-blocking
warnings and 96,047 no-adapter skips. The final `just test-fast` run passed
**7,514 tests**, with 16 skipped and 1,839 deselected. All three final source
readbacks and complete-record inversions pass; report hashes and snippets still
match. See `final-checks.json` and `final-readback.json`. Ruff, Black and
`git diff --check` pass. Checks used the partial locked Python 3.13 environment,
not full CI; no full-suite or publication-gate pass is asserted.

## Remaining Work

The six-record handoff below has since been addressed by the
[DSMZ/standalone follow-up](../20261007-dsmz650-752-762-preparations/README.md).
The pinned handoff snapshots remain unchanged as historical evidence. Its newer
merge audit exposes loss of the DSMZ records' distinct provenance; the earlier
KOMODO-specific retention result does not imply all duplicate sources survive.

These source edits do not prove safe merging of concentration-independent groups.
Historical duplicate links are preserved with an explicit limitation, not
revalidated as identical formulations. At this batch's original readback, the
three linked DSMZ records and their standalone main-solution records contained
corresponding flattened quantity or water-unit errors; the linked follow-up now
corrects them and reconciles their existing evidence. Do not copy this medium's evidence to a strain variant
or treat a standalone stock as a growth medium. Full reference validation,
merge retention and generated-data freshness must pass before publication.
The six current record snapshots and three original solution source captures are
preserved in `related-record-handoff.json` and `related-source-handoff.json`.

The current work remains local on `codex/curate-ingredient-evidence`. No commit,
push, PR, merge, branch deletion, or generated-page publication is claimed.

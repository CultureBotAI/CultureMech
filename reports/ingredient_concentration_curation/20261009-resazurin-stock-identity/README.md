# Resazurin Stock Identity Follow-Up

Three local primary `CHEBI:8806` mappings have been withdrawn from named sodium
resazurin stocks in DSMZ161, DSMZ212 and DSMZ212a. This is not a concentration
change: all source names, amounts, units, preparation stages and prior history
are preserved. Each existing PDF evidence entry retains its exact snippet and
previous explanation, with the identity disposition appended.

The source PDFs were visually inspected at DSMZ161 page 1 and DSMZ212/212a
pages 1-2. Text was re-extracted from the hash-pinned PDFs and compared with the
captured sources. They specify sodium resazurin (0.1% w/v), 0.50 ml. The local
ChEBI snapshot identifies CHEBI:8806 as sodium-free Resazurin, C12H7NO4, charge 0.
No replacement ID or absence of an appropriate ontology term is asserted.

**Still open:** the packaged MIM resolver returns CHEBI:8806 for this exact
stock label even after local term removal. The immutable index and resolver
are unchanged. This follow-up does not certify correct publication-time
identity. See [adversarial review](adversarial-review.md) for the finding and
the live ontology-access limitation. No GitHub write was attempted.

## Applied Change

- Three unsupported primary identities removed.
- Three existing evidence explanations extended; zero new evidence entries.
- Three append-only curation events; zero new references.
- Zero concentration changes and zero taxa-media associations added.

[Application/readback/repeat-no-op](apply.json) passed and the full normalized
inventory confirms only these three recipe files changed. The
[preview validation](preview-validation-v2.json) includes six baseline
schema/strict checks, 44 safety tests, lint and formatting. The failed first
checkpoint harness receipt remains preserved and did not edit recipes.
The [preview diff](preview.diff) preserves unrelated YAML presentation.

## Verification

- [Post-edit checks](post-validation.json): actual-written schema, strict,
  reference and regression results. All nine per-record commands pass, along
  with 943 focused regression tests (two dependency warnings).
- [Corpus gates](corpus.json): strict, IDs, products, merge and freshness checks;
  a successful scoped edit does not waive global failures.
- [Report reconciliation](reconciliation-final.json): existing canonical reports are
  extended, not duplicated. Index metadata is checked for changes.
- [Cumulative accounting](cumulative-audit.json) and
  [follow-up coverage](followup-coverage.json): updated after independent inversion
  of the registered applied history.
- [Fast regression tier](fast.json): 13,063 passed, sixteen skipped, 3,423
  deselected and two dependency warnings. This is not a full-suite rerun.

The [final local checkpoint](validation.json) pins the terminal receipts and
unchanged post-application corpus hash. Strict validation passes for all 15,910
normalized records; ID and product checks pass, with 91 product warnings and
96,010 unsupported-adapter skips. Global merge verification still fails with
1,247 name conflicts and 3,287 fingerprint issues. Freshness reports 15,056
differing records. These failures remain open; no merge readiness is asserted.

The first reconciliation receipt is retained: cumulative inversion and report
updates succeeded, but coverage was initially given the narrower cumulative
registry. The final reconciliation uses the previous complete coverage registry
plus this applied plan, without changing recipe or report bytes again.

The all-record goal remains active across all 15,910 normalized recipes. The
four [medium323 drafts](../20261009-medium323-draft-v2/README.md) remain unapplied;
their independent source checks cover 62 old quantity fields and 79 reference
checks, and the draft checker rejects 18 adversarial mutations. A full inverse
audit and guarded application writer are still required. Report presence is not full
concentration verification. No clean full-suite, merge readiness or publication
is claimed here.

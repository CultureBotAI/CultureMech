# Adversarial Self-Review

This is local self-review, not independent human or PR approval.

## Addressed

- Duplicate labels must not delete genuine yeast extract. Original indices,
  complete baseline hashes and false-LB supplier metadata are guarded; every
  old ingredient is accounted for as retained/relocated or explicitly removed.
- Similar BSK names do not authorize mixed formulations. Tests reject changing
  JCM's glutamate product to TOGO's glutamine-free product, transferring heated
  serum to M2410, or inventing composition for CMRL products.
- DSMZ 1829's final-volume denominator is explicit in the inspected PDF.
  The serum correction uses volume/volume, without density. Water is makeup,
  not an additive fixed dose. The first preview's wording could imply makeup
  before titration; it was revised before application, with a regression test.
- JCM 173's unusual Neopeptone input is 2.5 mg in both sources. Tests reject a
  thousand-fold reinterpretation. API stock rates are attributed at stock scope;
  water inputs do not silently supply parent doses or independently measured
  final stock volumes.
- Source pH adjustment timing is not evidence of a measured final pH. JCM's
  flattened final-pH claim is withdrawn; M2410's adjustment remains before its
  later gelatin/serum additions.
- Normality is not silently converted to molarity. Unspecified percentage
  bases remain textual; no gelatin mass or serum dose is inferred for M2410.
- The source's filter pore size controls the action: 0.22 micrometers in JCM,
  0.2 in TOGO, unstated in DSMZ. No generalized filter-sterilization enum is
  allowed to supply a different pore size.
- Every old quantity and source row is independently accounted for. Tests
  reject corrupted amounts, units, identity, history, evidence, bibliographic
  metadata, claim inventories and lineage. All-target guards precede writes;
  concurrent edits, symlinks and forged plans are rejected in fixture tests.

## Limits

Original-source authors/publication years are not supplied. Do not turn a
copyright year into publication metadata. Existing groundings and general
applications remain preserved, not comprehensively recertified. M2410's exact
dry-ingredient order still needs reliable original table inspection.

Report presence and literal snippet matches are not scientific completion of
the corpus. Global merge/freshness gates and publication require their own
results; passing record-level gates cannot close those findings.

## Final Checks

All checks are terminal in `validation.json`: 373 focused and 9,443 fast-tier
tests pass, as do all 74 reference checks, record-level validation, corpus
strict schema and ID checks. Product validation passes with 91 warnings and
96,070 no-adapter skips. Independent audit/readback/no-op checks account for
69 new evidence entries, all 139 claim excerpts and all prior quantity slots.
Only the three reviewed normalized records changed from this batch baseline.

Global merge verification and generated-data freshness still fail. The three
repaired formulations retain their claims in separate schema-valid runtime
merges, but that does not certify the rest of the generated corpus. No PR
approval, publication, merge or branch cleanup is claimed.

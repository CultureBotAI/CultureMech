# J And Dasycladales Ingredient Preview

Status: **historical source-backed preview, now applied through its successor**.
See the [applied batch](../20261010-utex-j-das/README.md) for current records and
validation. These preview reports add no canonical follow-up coverage.

The current proposal is [v3](mutation-preview-v3/plan.json), SHA256
`6a367592593e5ecab4525f4f1f7434ef152d5c36792929db65684e3730d687db`.
The initial [source triage](source-triage.json) and v1/v2 proposals remain as
historical evidence of the review; v3 supersedes their blanket removal of the
four DAS supplement dose fields.

## Proposed Changes

- Add fifty scoped evidence entries across two records. Source metadata records
  title, source type, discovery mode and access date; unknown authors, publication
  years and DOIs are not manufactured.
- Retain four DAS supplement ratios with an explicit basis: per liter of starting
  Pasteurized Seawater before supplement addition. The conflicting total-volume
  heading remains unresolved; no measured 3.1215 L final volume is inferred.
- Remove seven unsupported carrier/water fractions, retaining literal preparation
  inputs and makeup instructions in notes and evidence.
- Separate DAS prepared-stock doses from pure chemical composition, add the two
  source-explicit inner stock strengths, and remove unsupported anhydrous phosphate
  mappings from the heptahydrate.
- Correct two supplied vitamin salt forms using the seven-stock identity ledger.
  Its supplier-access limitations, and the B12 sterilization conflict, remain.
- Represent J Medium's explicitly optional 12.5 g/L agar formulation as a variant.

## Verification And Limits

[Validation](mutation-preview-v3/validation.json) passes eight baseline/proposed
CLI schema/strict checks. Forty retained concentration fields are independently
checked against literal source amounts; forty altered quantities and twelve
altered/omitted volume bases are rejected. All authoritative target hashes remain
unchanged. This does not replace a full scientific review.

The [draft application guard](mutation-preview-v3/guard-preview/validation.json)
passes 36 adversarial tests, Ruff and Black. It inverts the permitted diff,
reconciles change counts, rejects altered plans and concurrent edits, and tests
rollback/no-op behavior in temporary fixture repositories. The guard was
subsequently installed and used by the applied successor; these receipts describe
the earlier isolated checks.

The HTML and linked recipe PDFs give the same DAS volume conflict. The PDF page
images were inspected during the source review, with capture/render hashes in
the triage ledger. Generic culture conditions, growth and role assertions are not
certified by this concentration review.

The [consumer fix](../20261010-volume-basis-consumers/README.md), guarded application
and cumulative audit integration now have applied-successor receipts. Broader
gates and unresolved source limitations are tracked in that successor README.

# Adversarial Self-Review

This is a local self-review, not an independent reviewer or an approved PR.

## Findings Addressed Before Apply

1. The imported four stock doses had mass units even though JCM670 specifies
   liquid additions per liter. Corrected each dose with its own amount and the
   receiving preparation context; tests reject mass and absolute-dose swaps.
2. Resazurin was 0.5 g/L while the source lists 0.5 mg per batch. Retained the
   batch amount and removed the unsupported final rate, without assuming final
   volume. Other batch-only mass rates receive the same explicit treatment.
3. Flattened stock cross-references concealed distinct preparation stages.
   The iron acid dose, reagent molarity, trace-stock preparation, and vitamin
   filtration are now separately represented and evidenced. Tests reject
   stock/medium swaps and invented percentage bases.
4. The initial preview inherited wording claiming prior duplicate collapse and
   removal of an old concentration for newly added stock ingredients. The new
   repair removes that inapplicable wording and represents new batch notes as
   additions, not null-to-null concentration removals. The unapplied draft is
   retained as `preview-v1.json`; no historical YAML event was rewritten.
5. The initial preview retained an unsupported nitrogen VARIABLE placeholder.
   It is now removed with direct source atmosphere context and evidence. NaOH
   remains an unquantified pH-adjustment input, never a fabricated zero amount.

## Independent Checks

`audit.py` does not call the mutator's `build()`. It independently constructs the
expected source-section membership, computes doses/units, verifies all original
quantity coverage and every source row, compares all retained annotations and
history, and reconstructs evidence attachments from literal source quotations.
It rejects malformed scope even if a plan is rehashed. The shared guarded
runner additionally rejects concurrent changes, symlinks and plan drift.

All eight HTTP responses were freshly retrieved and raw-checksum matched before
application. The reference wrapper validates primary excerpts and titles; the
independent claim audit also validates additional excerpts in explanations.
Literal occurrence does not independently prove scientific entailment. Scope
decisions above require the inspected source tables and surrounding preparation.

## Limits

No new chemical grounding, DOI, author, publication year, density, normality
conversion, final volume, or taxa-media association is inferred. Source-defined
batch masses are retained in notes where the schema has no mass-per-batch slot.
The explicit 7.7 M acid strength is not a final-medium molarity.

Global publication readiness and all-record review completion are not established
by this one-record repair. Terminal gate results are preserved in validation.json;
failures must not be relabeled as passes. Earlier M142/J151 source-title corrections
and the remaining ingredient queue are separate outstanding work.

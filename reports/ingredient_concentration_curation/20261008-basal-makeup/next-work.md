# Remaining Ingredient Work

Subsequent status: the M196/M197/M198 candidates below have since been applied
in [the Pyrodictium follow-up](../20261008-pyrodictium-variants/README.md).
Its handoff supersedes this queue count. The source context and candidate
notes below are preserved as the historical pre-application assessment.

The applied four-record cohort advances but does not finish the all-record
objective. `remaining-queue.json` contains 86 hash-checked unchanged records
from the M142-dependent queue. The current broader follow-up report coverage is
11,766 of 15,910 exact normalized paths; 4,144 are outside that report set.
Report presence does not establish that all claims are resolved.

## Pyrodictium Candidates

`next-pyrodictium-context.json` has SHA256
`09b7f63c7eff389cfce01e637008468bf4558ed2ca0a294e70d5d5c5d1b1615a`.
It freezes unchanged current M196, M197 and M198 baselines and eight official
source captures. This is read-only preparation, not an applied repair, live
source refresh, or completed concentration review. The full three baselines,
TOGO rows/comments, and original JCM203/JCM204/JCM205 texts were inspected.

- M196/JCM203 contains 1 L M142 salt base and 10 ml M142 trace minerals as
  batch inputs. Expand only those two stock sections, not the whole M142
  medium. Neither stock dose establishes final medium volume.
- M196 has two identical sulfide-stock labels in its current solutions list.
  One is a TOGO self-reference and one is the expanded row. Original JCM203
  specifies one later 10 ml per-liter dose, not two doses or a self-nested
  solution. Reconcile and preserve both original annotations without summing.
- Source resazurin is 1 mg per batch, not the imported 1 g/L. The parent has
  no explicit final batch volume. Retain the source mass without inventing a
  final-medium rate. Sulfur and parent yeast quantities have the same boundary.
- M197/JCM204 explicitly overrides yeast extract to 0.2 g/L final. M198/JCM205
  explicitly overrides yeast to 0.5 g/L final and sodium tungstate dihydrate to
  0.1 mg/L. These are supported final rates, unlike inherited unqualified batch
  masses. Correct M198's imported 0.1 g/L tungstate without changing hydrate.
- M198's original instruction also says to omit citric acid. Neither JCM203's
  main table nor JCM151's salt-base/trace-mineral tables contains citric acid.
  Preserve the source's omission instruction as context; do not introduce then
  remove a citric-acid ingredient by accidentally inheriting JCM151's main medium.
- TOGO's inherited preparation says H2-CO4; original JCM203 says H2-CO2.
  Use an exact original excerpt for effective atmosphere instructions and
  explicitly preserve the discrepancy. Gas atmosphere and titration are not
  fixed ingredient amounts. Sulfur sterilization and later sulfide dosing have
  separate preparation stages.
- Preserve the 5% sulfide label and stock pH 7.0 without inventing a percentage
  basis. Parent/variant relationship links need exact tracked IDs/paths and
  original JCM204/JCM205 evidence. Existing chemical mappings remain unrecertified.

Before application: refresh and inspect the eight sources, run baseline gates,
preview every changed claim, independently audit all old quantity fields and
source memberships, test duplicate-stock handling and explicit final-rate
overrides, and verify no-op/history preservation. Do not reuse the basal-makeup
assumption from the preceding cohort: JCM203 has no such makeup instruction.

## Other Outstanding Work

The J151 and M142 bibliography-title mismatches remain documented in
`../20261008-recipe-reference-validator/next-work.md`. Corpus-wide merge
verification/freshness gates remain unresolved. Scoped retention is not a
publication-readiness decision. Generated metadata's hierarchy-enrichment flag
also does not inspect nested stocks; see `adversarial-review.md`.

No commit, push, PR, merge, or branch deletion was performed in this pass.
The prior issue #150 progress comment remains unposted after the approval
checker rejected external disclosure of the draft. Do not retry or route around
that rejection without new authorization. Local ingredient curation can proceed.

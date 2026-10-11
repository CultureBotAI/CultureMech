# Middlebrook Ingredient and Stock Stages

Thirteen authoritative normalized records are repaired locally. This is a
curation batch, not completion of the all-record goal or resolution of every
scientific uncertainty in these records.

The guarded [plan](plan.json) and immutable [source context](context.json)
account for 234 old quantity slots, 229 source/input nodes and 548 claims.
The [application receipt](apply.json) verifies 13 changed records, independent
source auditing, exact readback and a no-op rerun. Only those 13 normalized
YAMLs changed from this batch's baseline. Added provenance is 225 evidence
entries, 15 references and 13 append-only curation events.

## Corrections

- Restore source-listed albumin and remove falsely substituted LB constituents.
- Separate basal ingredients, commercial-base details, ADC/OADC stock recipes
  and their addition doses. Genuine casein digest and NaCl are preserved.
- Correct volume-as-mass encodings. Keep exact gram/milligram amounts in
  evidence-backed notes when no final-volume denominator is stated.
- Preserve unspecified percentage bases; only the explicit M2403 ADC v/v
  basis is asserted. Do not infer density or final volume.
- Retain source-specific catalase amounts, cooling/sterilization context,
  Mycobactin J reconstitution scope, and conflicting source statements.
- Correct M2399's liquid classification to the source's agar preparation.

## Validation

All 26 baseline schema/strict commands pass. The [focused retry](focused-retry.json)
passes lint, formatting and 526 tests. The earlier lint failure and first audit
weakness remain documented in [adversarial-review.md](adversarial-review.md).

All 14 DSMZ/TOGO source captures refresh identically. The [reference receipt](live.json)
passes 239 of 240 checks. NBRC 1219's independently inspected water quote fails
the generic automated matcher; its [local issue](issue-nbrc-reference-matcher.md)
was resolved by the later [NBRC parser repair](../20261009-nbrc-reference-validation/README.md).
This batch's original receipt is not an all-reference automated pass.

The [final receipt](validation.json) reconciles all terminal checks. The fast
tier passes 9,819 tests (16 skipped); strict schema and IDs pass for all 15,910
normalized records. Product validation retains 91 warnings and 96,053
no-adapter skips. Four metadata indexes were refreshed; all 13 formulations
retain their claims in separate schema-valid runtime merges.

Global merge verification still fails with 1,247 name conflicts and 3,287
fingerprint issues. Freshness finds 4,275 tracked-only files, 8,732 fresh-only
files and 2,045 changed files, with none unchanged. This is not clean CI or
an all-record completion claim. Earlier failure receipts remain preserved.

## Remaining Work

M1946 retains TOGO's 895 ml water alongside the current NBRC page's 900 mL
conflict. M2879's ADC/Tween plate table conflicts with its quoted cultivation
sentence. M2402's broth prose mentions agar without an ingredient row. M2404's
ethanol retention/final volume is not specified. Original ATCC ashx links were
inaccessible; literature behind the cultivation quotations was not identified.
Chemical ontology annotations are retained, not comprehensively recertified.
No taxa-media associations were added.

Continue the full corpus: the 11 remaining linked DSMZ/KOMODO Middlebrook
variants, other identity/concentration queues, unresolved source claims,
global merge/freshness and publication. Per-record outputs are under `records/`;
D857 supplements its earlier canonical follow-up, and the 12 TOGO outputs add
canonical follow-up paths without rewriting the historical full-corpus audit.

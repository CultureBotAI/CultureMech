# Adversarial Review

## Addressed Findings

1. Three supplier-tagged LB constituents replaced albumin in each record. The
   repair removes those explicit nodes only; genuine BSK peptone and yeastolate
   remain. Existing identifiers and earlier curation history are preserved.
2. Flattening conflated stock composition, stock dose and receiving-medium
   concentration. Independent reconstruction checks the complete A-D graph,
   nested CMRL/NaOH inputs, all source rows and every previous quantity field.
   Water inputs do not establish final volumes.
3. DSMZ 403 is not the JCM201 formulation. Its 50.05 g fraction V input, exact
   product alternatives, 86 ml inactivated serum and separate water inputs are
   preserved. Neither BSA replacement nor purchased BSK-H is an extra ingredient.
4. A 5 M titrant is not a 5 ml dose. Solution A's pH 7.6 is not final-medium pH.
   The audit rejects invented titrant doses, moved pH scope and default 121 C
   autoclaving of the explicitly 115 C gelatin preparation.
5. DSMZ 751 is not JCM220: glucose is 5 ml of 10% stock, not 1 ml of 50% stock.
   Unknown percentage bases remain unknown; 0.05 N NaOH does not become molarity.
   Tests reject wrong cysteine forms, albumin fractions and invented strengths.
6. Only albumin, glucose and cysteine are separately filtered and added after
   autoclaving/cooling. The hemin row is before that source boundary. Tests
   reject moving hemin into the late-addition filtration group.
7. Liquid SC changes all three source-specified features together. It is an
   inline variant, not a sequential instruction that overwrites the solid base.
   Existing DSMZ/KOMODO source-duplicate links are retained for validation.
8. A passing source-download status is not a reference-validation pass. All four
   binaries/responses match the inspected captures, but the PDF checker failures
   remain explicit. A local issue documents its raw-PDF-as-text cache behavior.

All 126 dedicated tests pass, including forged-plan, concurrent-edit and symlink
guards before any target write. One unused loop variable was found by lint and
removed without changing the reviewed output. Its initial failed receipt is
retained separately from the retry.

The focused regression selection passes 459 tests and the fast tier passes
9,300 tests (16 skipped). Strict schema and serial ID checks pass for all 15,910
records. Product validation passes with 91 warnings and 96,073 no-adapter skips;
it does not recertify every chemical mapping.
The SC source-duplicate pair agrees exactly across eight formulation/evidence
fields, with reciprocal links checked independently. All intended checks are
terminal in [validation.json](validation.json); automated PDF checks remain
failing. The receipt builder's initial UTF-8 metadata-key error is recorded
alongside its successful retry; no source or recipe data changed for that fix.

This is local adversarial self-review with an independent reconstruction, not
external PR approval or independent human review. No issue or PR was published.

## Remaining Findings

Chemical mappings are preserved, not comprehensively recertified. Unknown final
volumes and percentage bases remain explicit. The PDF validation adapter,
remaining identity and concentration queues, global merges/freshness and the
publication workflow still require work.

Subsequent resolution: the [PDF validation follow-up](../20261008-recipe-pdf-validation/README.md)
fixes extraction and passes all 122 reference checks without changing these
records. The original results above remain historical; other findings are open.

# Middlebrook Adversarial Review

This review concerns the guarded 13-record proposal, not all-record completion.
No GitHub publication has occurred.

## Findings Addressed

- The first audit accepted a fabricated primary evidence snippet if the real
  snippet was also retained in an additional excerpt. It now checks every
  primary snippet directly against its captured source as well as checking
  each claim's linkage. All 13 corruption cases now pass.
- The concurrent-edit test initially expected AssertionError, but the guarded
  writer correctly raises ValueError before any writes. The test now checks
  the actual contract and byte preservation.
- The first focused run passed 526 tests but failed lint on two ambiguous
  variable names. Those names were changed without altering the frozen plan.

The first dedicated run was 160 passed / 14 failed. The first focused run's
immutable receipt is `focused.json`; the corrected run is recorded separately.

## Scientific Boundaries

- Do not transfer DSMZ 857's 0.3 mg ADC catalase to TOGO recipes that list 3 mg,
  or replace OADC amounts with an ADC formulation.
- TOGO gram/milligram rows without a verified final-volume denominator remain
  exact batch masses in evidence-backed notes. Unspecified percentages remain
  unresolved. Only M2403's explicit ADC v/v basis is asserted.
- Commercial powder details are grouped under their own descriptor and are
  not extra ingredients alongside the same powder at root scope.
- Genuine pancreatic casein digest and NaCl survive. Only the specifically
  guarded false LB constituent nodes are removed.
- M1946 retains 895 ml as the TOGO assertion and documents the current NBRC
  page's 900 mL input as a source-version conflict.
- M2879's table/prose disagreement, M2402's agar-in-broth wording and M2404's
  ethanol reconstitution scope remain explicit. No organism-growth claim is
  inferred from quoted cultivation prose.

## Remaining Validation Limit

The 14 DSMZ/TOGO captures refreshed identically. The NBRC original was captured
and inspected separately; its literal water quote passes the independent audit
but fails the generic automated reference matcher. This is not an automated
reference pass. Original ATCC ashx links were inaccessible via web.open.
Full-corpus merge/freshness and publication remain separate, unfinished work.

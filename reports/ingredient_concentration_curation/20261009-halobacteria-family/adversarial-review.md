# Halobacteria Adversarial Review

Scope: five exact source records and the locally applied successor proposal. These
are local findings, not GitHub issues or a published PR review.

1. **P1: Trace-metal amounts were inflated one thousandfold. Fixed locally.**
   M1064, M159 and M160 each import FeCl2 tetrahydrate at 36 g/L and MnCl2
   tetrahydrate at 0.36 g/L. Both primary JCM168 and each provider's own TOGO
   response give milligrams. JCM's explicit final-volume make-up supports
   36 mg/L and 0.36 mg/L. No density or molecular-weight conversion is used.

2. **P1: Final-volume water was treated as ingredient mass. Fixed locally.**
   The three TOGO records assert water at 1 g/L. Changing that to a fixed 1 L
   input would still be wrong: the instruction makes the complete preparation
   up to 1 L. All five written records retain water as unquantified make-up.

3. **P1: Modified-medium identity was erased by copying its base. Fixed with an explicit limit.**
   JCM1007 lacks its pyruvate and carbonate input and falsely declares an exact
   duplicate relationship to JCM168. It also retains the base magnesium amount.
   The successor restores the explicit modified ingredients, pH and magnesium
   target and repairs that reciprocal relationship. However, the source's
   lower final magnesium target conflicts operationally with adding magnesium
   to an unchanged base. Both facts remain visible; 21 g/L is not inferred.

4. **P2: Initial preview inferred a preparation-step ordering. Fixed before application.**
   The first proposal combined the page's generic sterilization instruction
   with recipe-specific steps into a newly ordered protocol. Not every relative
   order is explicit in the source. The successor preserves existing step
   arrays and adds cited preparation excerpts in notes instead. The first
   proposal is retained unchanged for comparison; only the reviewed successor
   has been applied.

5. **P2: Trace-metal corrections could trigger an unjustified flag removal. Avoided.**
   The schema counts Na, K and other metals in `high_metal`. These recipes have
   200 g/L sodium chloride. The applied successor preserves every existing flag rather
   than treating corrected trace-metal units as proof that the flag is false.

## Checks

Independent source projection covers 51 old quantities, 55 output nodes and
171 claims. Every changed non-provenance field is covered by a claim with a
literal source excerpt and matching in-record evidence. Rehashed amount,
water, snippet, history, high-metal, physical-state and unrelated-field attacks
are rejected; magnesium attacks using 20 or 21 g/L are rejected separately.
The historical preview passed 103 focused tests, twenty baseline/proposal
schema/strict commands, five reference CLI commands and 105 reference checks.
The application successor passes 332 focused tests, including proposal, receipt,
validation-log, symlink and concurrent-edit attacks. Independent written-output
auditing matches all 171 claims; repeat application changes nothing. Ten
actual-written schema/strict commands and 105 reference checks also pass.
The first focused attempt stopped at a formatting check and remains retained;
the corrected successor passes. Corpus strict/ID/product, presentation, report
reconciliation, three-index refresh and all five merge-retention checks pass.
All 260 final QA tests pass. Product-check warnings and missing adapters remain
explicit limitations. The current fast-tier run passes 12,701 tests, with 16
skipped, 2,962 deselected and two dependency warnings. The 117 family tests are
corpus-tier and pass separately within the focused and QA runs. `validation.json`
pins the terminal applied checkpoint; no clean CI or publication is claimed.

Remaining scope includes the operational magnesium ambiguity, other linked
variants, the separate medium323 preparation, unresolved corpus concentrations
and the known global merge/freshness failures. None is marked complete here.

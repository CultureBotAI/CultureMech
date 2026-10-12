# Halobacteria Preview Adversarial Review

Scope: five exact source records and the unapplied successor proposal. These
are local findings, not GitHub issues or a published PR review.

1. **P1: Trace-metal amounts were inflated one thousandfold. Fixed in preview.**
   M1064, M159 and M160 each import FeCl2 tetrahydrate at 36 g/L and MnCl2
   tetrahydrate at 0.36 g/L. Both primary JCM168 and each provider's own TOGO
   response give milligrams. JCM's explicit final-volume make-up supports
   36 mg/L and 0.36 mg/L. No density or molecular-weight conversion is used.

2. **P1: Final-volume water was treated as ingredient mass. Fixed in preview.**
   The three TOGO records assert water at 1 g/L. Changing that to a fixed 1 L
   input would still be wrong: the instruction makes the complete preparation
   up to 1 L. All five proposed records retain water as unquantified make-up.

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
   proposal is retained unchanged for comparison; no recipe was written.

5. **P2: Trace-metal corrections could trigger an unjustified flag removal. Avoided.**
   The schema counts Na, K and other metals in `high_metal`. These recipes have
   200 g/L sodium chloride. The preview preserves every existing flag rather
   than treating corrected trace-metal units as proof that the flag is false.

## Checks

Independent source projection covers 51 old quantities, 55 output nodes and
171 claims. Every changed non-provenance field is covered by a claim with a
literal source excerpt and matching in-record evidence. Rehashed amount,
water, snippet, history, high-metal, physical-state and unrelated-field attacks
are rejected; magnesium attacks using 20 or 21 g/L are rejected separately.
All 103 focused tests, twenty baseline/proposal schema/strict commands, five
reference CLI commands and 105 supported reference checks pass. Application
remains disabled pending the reviewed apply gate and explicit readback/no-op
checks. The earlier applied family's fast-tier run does not include these new
tests; their isolated terminal results are recorded separately.

Remaining scope includes the operational magnesium ambiguity, other linked
variants, the separate medium323 preparation, unresolved corpus concentrations
and the known global merge/freshness failures. None is marked complete here.

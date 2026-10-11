# Adversarial Self-Review

This is a local self-review with an independent checker and mutation tests,
not a separate human review or a posted GitHub PR review.

## Resolved Before Application

- Duplicate sulfide stock: the original JCM203 directive specifies one later
  10 ml/L addition. M196's two imported nodes must not double the dose. The
  richer original annotation is retained, both old quantity pointers are
  accounted for, and the checker rejects a second retained node.
- Batch versus final volume: 1 L salt base, stock table water inputs and solid
  masses do not establish final-medium or final-stock concentrations. Mutation
  tests reject inserted final rates and changed batch-dose bases. The preceding
  cohort's basal-makeup rule is deliberately not applied here.
- Variant-specific rates: the checker requires the original explicit 0.2 and
  0.5 g/L yeast rates and 0.1 mg/L tungstate rate. It rejects inherited parent
  yeast amounts, the old tungstate unit, incorrect parent links and altered
  chemical annotations. The parent is not changed to match either variant.
- Inheritance membership: only M142 salt-base and trace-mineral tables belong
  here. Tests reject importing M142's whole main medium or introducing its
  citric acid. The original child omission directive remains context.
- Preparation scope: tests reject wrong gas instructions, fabricated fixed
  gas amounts, invented sulfide percentage bases and lost original context.
  The TOGO typo is quoted as a discrepancy, not as the effective instruction.
- Excerpt boundary: the first independent audit omitted the terminal period
  from a sentence-ending M197 check. The literal validator correctly rejected
  that boundary. The audit was corrected to use the complete literal excerpt;
  neither the validator nor the source evidence was relaxed. All 79 new tests
  passed after correction and before application.

## Guards And Residual Risks

The checker is separate from the mutator's formulation builder. It verifies
source membership, amount/unit/basis, original annotation preservation,
append-only history, bibliography, link evidence and preparation. It covers
all 32 old quantity fields and 111 source rows; repeated source nitrogen is
accounted for without manufacturing an extra ingredient. The 184 claim
decisions map to 130 evidence entries because related source excerpts can
share an evidence entry with explicit field locators.

Application checks the pinned commit, full before/after bytes, IDs, exact
tracked paths, source hashes, schema and all targets before the first write.
Tests reject symlink targets, concurrent edits and a forged last-record plan.
Readback and a no-op rerun leave evidence and history unchanged.

No source supplies an unambiguous percentage basis for the sulfide label or
an explicit final volume for inherited unqualified batch masses. These remain
unresolved rather than being converted. Existing chemical mappings, legacy
quality flags and M197's composition classification are preserved, not
recertified by this concentration work.

Full-corpus merge routing is checked, but only three generated outputs are
independently recertified. Global merge verification and freshness are not
passing publication gates. Fast/focused checks do not replace a full clean-CI
test run. No PR review, GitHub issue publication, merge or branch deletion is
claimed by this document.

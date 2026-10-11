# Filtered Media And Sulfide Preparation Repair

Applied locally to three exact normalized records at reviewed commit
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. This advances, but does not complete,
the all-record ingredient goal or the requested publication workflow.

Canonical reports, each with one exact tracked `- Record:` entry:

- [M199: unnamed JCM206 medium](records/M199.md)
- [M206: Archaeoglobus Fulgidus Medium](records/M206.md)
- [M207: Archaeoglobus Profundus Medium](records/M207.md)

## Scientific Decisions

M199's flattened salt-base ingredients now belong to its salt-base stock.
Original JCM206 explicitly specifies 17 g/L NaCl and 2.5 mg/L KI in that stock.
The NaCl rate is retained at the proper scope; the KI unit is corrected from
g/L to mg/L. Neither rate is propagated to the receiving medium or used to
invent a final-volume denominator for other stock ingredients.

Prepared salt-base and trace-mineral inputs retain batch-volume units rather
than mass rates or inferred per-liter doses. M206 and M207 retain 990 ml water
as 0.99 L input. Water plus stock additions does not establish final volume.
Unqualified solid amounts, including source milligram quantities, are preserved
in evidence-backed batch notes rather than asserted as final concentrations.

All three recipes specify a separate sulfide preparation. Each now has an
unquantified solution descriptor whose composition notes preserve the 0.5 g
receiving-batch contribution. That contribution is not an invented stock-batch
recipe, stock strength or addition volume. M199/JCM206 and M206/JCM213 state a
5% label without its basis; M207/JCM214 does not state that strength at all.
No strength or dose is borrowed across recipes.

Only M142/JCM151's trace-mineral table is expanded, with its KOH titrant and
stock-specific pH adjustments. Original table excerpts corroborate its chemical
forms and amounts. The complete Pyrococcus medium is not inherited.

Original preparation is retained separately for each recipe: filtration,
sulfide neutralization/autoclaving and later addition, plus M199's separately
steamed sulfur. M206's 1 N sulfuric acid remains an unquantified titration
reagent in notes; normality is not converted to molarity. Gas and titrant
VARIABLE placeholders are removed with evidence. Atmosphere and post-inoculation
pressure remain source-specific rather than being converted to dissolved-gas
concentrations. No pore size is invented for the filtration instruction.

## Evidence And Verification

The [frozen context](context.json) has SHA256
`9ef2e61a0c079c15a0cc2577004711a46a8d425872737561c8e333a2655490d4`.
All eight fresh official responses match their inspected captures. The
independent [applied audit](applied-audit.json) accounts for all 63 old quantity
fields, 105 source rows and 234 claim decisions. It counts 208 added evidence
entries, 12 bibliography entries, three appended history events, four stock-dose
corrections, four other quantity corrections, two stock-rate scope repairs,
15 relocated ingredient nodes and 54 removed unsupported quantity fields.
Three new quantity fields are stock-water inputs, not final-medium rates.
No taxa-media association is added. Existing IDs, chemical annotations and
unrelated metadata are preserved, not recertified.

Baseline and applied schema/strict checks pass for all three records. Reference
validation passes 208 primary excerpts and 12 titles; the independent audit
also checks additional excerpts stored in explanations. Guarded application,
readback and a no-op rerun pass. All 86 new tests and 581 focused tests pass.
The fast tier passes 8,538 tests with 16 skipped and 1,945 deselected.
Ruff, Black and whitespace checks pass. Wider terminal outcomes and artifact
hashes are recorded in [validation](validation.json). Explicit-root strict
validation and ID checks both cover all 15,910 normalized records and pass.
Identifier-label validation exits successfully with 91 nonblocking warnings
and 96,087 pairs skipped for lack of an adapter; it does not recertify all
chemical groundings.
The runtime is the existing partial locked Python 3.13 environment, not clean
CI; the full test suite was not rerun for this localized repair.

[Merge retention](merge-retention.json) routes all 15,910 current normalized
inputs into 10,777 groups. Each repaired record occupies a separate group;
its actual generated output retains the repaired quantities, preparation and
evidence and passes schema validation. Only those three outputs are recertified.
No tracked merged YAML is rewritten. Four maintained metadata indexes are
refreshed with guarded scope; only the three records' root ingredient and
solution counts change.

Global merge verification still fails with 1,247 name conflicts and 3,287
fingerprint issues. Freshness still fails: 6,320 tracked versus 10,777 fresh,
2,045 changed shared paths, 4,275 tracked-only, 8,732 fresh-only and zero
unchanged. These counts match the preceding pass; they are not passing gates.

## Remaining Scope

[Follow-up coverage](followup-coverage.json) includes 11,772 of 15,910 exact
normalized paths, leaving 4,138 outside this report set. Report presence does
not prove every scientific claim resolved. The cumulative audit counts 5,145
edited records and 31,738 added evidence entries. These counts measure curation
follow-up, not the earlier completed structural inventory of normalized and
merged records.

The [handoff](next-work.md) preserves 80 unchanged M142-dependent candidates
and the next source-inspected M208/M209 pair. Global merge/freshness failures
remain separate from the successful scoped checks. No commit, push, PR, merge
or branch deletion was performed in this pass. The prior issue #150 progress
draft remains unposted pending authorization; local curation can continue.

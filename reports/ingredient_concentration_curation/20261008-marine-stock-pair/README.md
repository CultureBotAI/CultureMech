# Marine Stock And Water Deaggregation Repair

Applied locally to M208 and M209 at reviewed commit
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. This advances, but does not complete,
the all-record ingredient goal or the requested publication workflow.

Canonical reports, each with one exact tracked `- Record:` entry:

- [M208: Pyrobaculum Aerophilum Medium](records/M208.md)
- [M209: unnamed JCM216 medium](records/M209.md)

## Scientific Decisions

M208's 866 g/L water collapsed two separate source inputs: 865 ml main water
and 1 L marine-stock water. M209's 971 g/L similarly combined 970 ml main water
with 1 L stock water. Both now retain separate scoped water inputs in liters,
with the old duplicate-collapse annotation preserved and explicitly superseded.
Neither those inputs nor their sums establish final-medium or final-stock volume.

Local marine-stock solids are moved out of the receiving medium into the named
stock. Only M142/JCM151's trace-mineral table and M190/JCM197's vitamin table are
expanded; other parent stocks and whole-medium preparation are not inherited.
Prepared-stock doses are batch volumes: M208's marine stock is 0.125 L and the
four other stock additions are each 0.01 L. No per-final-liter dose is inferred.

Unqualified solid amounts, including original milligram values, are retained as
batch amounts in evidence-backed notes. Unsupported g/L fields are removed,
not replaced by assumed final concentrations. Original JCM table excerpts
corroborate each mass or water amount and exact printed chemical form.

M209's separately autoclaved sulfide retains its 0.5 g receiving-batch
contribution under a separate preparation descriptor. This is not a stock-batch
recipe. Its 5% basis, solvent volume and addition volume remain unspecified.
M208 does not inherit sulfide preparation. M208 retains 1 N acid, filtration,
dispensing, the 80:20:1 gas ratio and post-inoculation pressure. M209 retains
initial pH 6.0 and later pH 6.5, with its own gas and sulfide preparation stages.
No pore size, percentage normalization or normality-to-molarity conversion is
asserted. Gas and titrant VARIABLE placeholders are replaced by supported context.

Both original JCM215 and TOGO print `NaWO4` in the hydrated tungstate row.
The source formula/legacy-grounding discrepancy is noted without silently
normalizing either. Existing chemical annotations, quality flags, IDs and prior
curation events are preserved, not recertified. No taxa-media association is added.

## Evidence And Verification

The pinned [source context](../20261008-filtered-sulfide-media/next-marine-pair-context.json)
has SHA256 `03204b85c0510e83182322363d7722b7a492f333ed3d3f1e13b8c3f9d6c034c1`.
All eight fresh official source responses match the inspected captures. The
independent [applied audit](applied-audit.json) accounts for all 61 old quantity
fields, 102 source rows and 224 claim decisions. It counts 199 added evidence
entries, ten bibliography entries, two appended history events, five stock-dose
corrections, two water corrections, 23 relocated ingredient nodes, one separate
sulfide descriptor and 54 removed unsupported quantity fields. Five newly
represented water fields are stock inputs, not final concentration denominators.

Baseline and applied schema/strict checks pass for both records. Reference
validation passes all 199 primary excerpts and ten titles; the independent audit
also verifies extra excerpts stored in explanations. Guarded application,
readback and a no-op rerun pass. All 87 new tests and 668 focused tests pass.
The fast tier passes 8,626 tests with 16 skipped and 1,945 deselected.
Ruff, Black and whitespace checks pass. The [adversarial review](adversarial-review.md)
documents challenged assumptions and mutation tests, not an external PR approval.

All intended gates are terminal in [validation](validation.json). Explicit-root
strict validation and ID checks each cover all 15,910 normalized records and
pass. Identifier-label validation exits successfully with 91 nonblocking
warnings and 96,087 pairs skipped for lack of an adapter; it does not recertify
all chemical groundings. The runtime is the existing partial locked Python 3.13
environment, not clean CI. The full test suite was not rerun for this localized
repair.

[Merge retention](merge-retention.json) routes all 15,910 normalized inputs into
10,777 groups. Each repaired record occupies a separate group. Both actual
generated outputs retain the repaired quantities, preparation and evidence and
pass schema validation. Only these two outputs are recertified; no tracked
merged YAML is rewritten.

Five maintained metadata files are refreshed with guarded scope. M208's root
ingredient count changes from 28 to 14; M209's changes from 28 to 19 and its
solution count changes from three to four. The existing top-level-only hierarchy
enrichment check no longer emits M209's flag, reducing the generated aggregate
by one. Its legacy KNO3 annotation survives in the marine stock. This generator
limitation is documented in the [index plan](index-refresh-plan.json).

Global merge verification still fails with 1,247 name conflicts and 3,287
fingerprint issues. Freshness also fails: 6,320 tracked versus 10,777 fresh,
2,045 changed shared paths, 4,275 tracked-only, 8,732 fresh-only and zero
unchanged. These counts match the preceding pass, not passing gates. Those
failures are not waived by successful cohort checks.

## Remaining Scope

[Follow-up coverage](followup-coverage.json) includes 11,774 of 15,910 exact
normalized paths, leaving 4,136 outside this report set. A report can still
contain unresolved scientific claims. The cumulative audit counts 5,147 edited
records and 31,937 added evidence entries. These follow-up counts are distinct
from the earlier completed structural audit.

The [handoff](next-work.md) preserves 78 unchanged M142-dependent candidates and
the source-inspected M225/M229/M234 preparation cohort. No commit, push, PR,
merge or branch deletion was performed in this pass. The prior issue #150
progress draft remains unposted pending authorization; local curation can continue.

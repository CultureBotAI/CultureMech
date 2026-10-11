# Basal Makeup And Supplement Repair

Applied locally to four exact normalized records at reviewed commit
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. This advances, but does not complete,
the all-record ingredient review or the requested publication workflow.

Canonical reports, each with exactly one tracked `- Record:` entry:

- [M809: Modified Haloanaerobium Medium](records/M809.md)
- [M823: S200 Medium](records/M823.md)
- [M853: Halanaerobacter Jeridensis Medium](records/M853.md)
- [M975: Halanaerobium Sehlinense Medium](records/M975.md)

## Scientific Decisions

The explicit 1 L makeup instruction applies to a basal preparation before
pH adjustment, heating, and later supplements. Its ingredient rates are now
nested at that stage rather than asserted as final supplemented-medium rates.
Makeup water is unquantified; neither the final supplemented volume nor a fixed
dose of heated/titrated basal medium is inferred.

M809's vitamins and trace minerals belong to basal preparation. Its later
glucose and reducing-stock doses are 25 ml per batch. M823, M853 and M975
explicitly specify their later stock doses per liter. All 17 imported liquid
addition quantities are corrected from mass rates with the source-specific
basis retained. [JCM779](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=779),
[JCM791](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=791),
[JCM929](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=929).

M823 and M853 resazurin is corrected to 1 mg/L at basal makeup. M853 is linked
to M823 as the source-defined salt-substitution and pH variant: 5 g/L magnesium
sulfate heptahydrate replaces basal calcium chloride dihydrate, and the effective
pH instruction is 7.5 instead of the inherited 7.0. The parent is not modified
to match the child. [JCM818](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=818).

M975's 10 M KOH is a reagent strength with unspecified titration dose. The
three 1 M glucose stocks retain explicit stock strengths. Unspecified percent
bases remain unresolved. M809's reducing stock retains 0.5 g of each solute
and 25 ml water as batch inputs; no final stock volume is assumed. Its former
26 g/L merged-water assertion is removed without losing the historical annotation.
M975's conflicting table-water versus makeup instruction remains explicit.

Only M142 trace minerals and M190 vitamins are expanded, with stock-only
preparation retained. Gas/titrant placeholders and unsupported water/final
mass-rate assertions are removed with source evidence. Existing chemical
groundings, IDs, quality flags, and prior history are preserved, not recertified.

## Evidence And Verification

The [pinned context](context.json) has SHA256
`e2970bd6a1ebf9d9ba9c900aa1666cf7e8c15aac8c2bb2739c40bc4506492198`.
All 12 freshly fetched official responses match their inspected captures.
The [independent applied audit](applied-audit.json) accounts for all 65 old
quantity fields, 133 source rows and 285 claim decisions. It counts 182 added
evidence entries, 20 bibliography entries, four appended events, 17 stock-dose
corrections, three other quantity corrections, nine newly scoped quantity slots
and 16 removed unsupported quantity slots. These are not 182 new final-medium
concentrations or organism-growth claims. No taxa-media association was added.

Baseline and post-apply schema/strict checks pass for each record. Reference
validation passes 182 primary excerpts and 20 titles; the independent audit
also checks additional quoted excerpts in explanations. Guarded application,
readback and a no-op rerun pass. The new tests pass 92 cases, the focused suite
passes 416, and the fast tier passes 8,371 with 16 skipped and 1,945 deselected.
Ruff, Black and whitespace checks pass. The full test suite was not rerun for
this localized repair; the runtime is the existing partial locked Python 3.13
environment, not a clean CI installation. Terminal corpus gate outcomes and
source/code hashes are in [validation](validation.json).

Full-corpus routing includes all 15,910 normalized inputs and produces 10,777
groups. Each repaired record occupies its own group; its actual generated
output preserves quantities, preparation and evidence and is schema-valid.
Only these four outputs are recertified by [merge retention](merge-retention.json).
No tracked merged YAML was hand-edited or regenerated. Global merge verification
still fails with 1,247 name conflicts and 3,287 fingerprint issues. Freshness
still fails: 6,320 tracked versus 10,777 fresh, 2,045 changed shared paths,
4,275 tracked-only, 8,732 fresh-only and zero unchanged. These counts match
the preceding pass, not passing publication gates.

The maintained index generator refreshed four metadata artifacts with guarded
scope. Its top-level-only hierarchy flag decreases by one when M975's preserved
KNO3 annotation moves into the basal preparation. See
[self-review](adversarial-review.md) for that index limitation and adversarial checks.

## Remaining Scope

The current [coverage report](followup-coverage.json) contains 11,766 of 15,910
exact normalized paths, leaving 4,144 outside this report set. Report presence
does not prove every claim resolved. The cumulative independent audit counts
5,139 edited records and 31,400 added evidence entries.

The [next-work handoff](next-work.md) preserves the 86-record unchanged
M142-dependent queue and source-inspected, unedited M196/M197/M198 candidates.
Earlier bibliography mismatches and global merge/freshness failures remain.
No commit, push, PR, merge or branch deletion was performed in this pass.
The prior issue #150 progress comment remains unposted pending authorization;
local ingredient review is not blocked by that publication restriction.

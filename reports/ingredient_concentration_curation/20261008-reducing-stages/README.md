# Reducing-Agent And Stock Preparation Repair

Applied locally to M225, M229, M234, M236 and M243 at reviewed commit
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. This advances, but does not complete,
the all-record ingredient goal or the requested publication workflow.

Canonical reports, each with one exact tracked `- Record:` entry:

- [M225: Methanocaldococcus Jannaschii Medium](records/M225.md)
- [M229: Thermotoga Medium](records/M229.md)
- [M234: unnamed JCM242 medium](records/M234.md)
- [M236: Stetteria Medium](records/M236.md)
- [M243: Methanothermus Fervidus Medium](records/M243.md)

## Scientific Decisions

M229's collapsed water and sodium chloride are separated into their source
preparations: 750 ml main water versus 1 L artificial-seawater water, and 20 g
main NaCl versus 27.7 g in that stock. M236 and M243 each recover three separate
water scopes. Preserved duplicate-collapse annotations are explicitly superseded,
not erased or interpreted as current quantities.

Local seawater, Ni-Se-W and mineral-solution recipes now occupy their own stock
descriptors. M142's trace-mineral table and M190's vitamin table are expanded
without importing other parent ingredients or whole-medium preparation. All
13 stock addition amounts are expressed as batch volumes in L, not g/L or ml/L.
The 2 x seawater label does not establish a final stock denominator.

Solid amounts, including original milligram values, are retained in evidence-
backed batch notes. Unsupported concentration fields are withdrawn without
assuming that water inputs, sums of liquid inputs, or example vessel volumes
establish final preparation volumes. Exact salts/hydrates and legacy annotations
survive; their ontology groundings are not recertified by this quantity review.

Eight separate reducing-agent descriptors retain the source 0.5 g contributions
to the receiving batches. They are not recipes for an unspecified volume of
stock. Their source 5% labels lack a defined percentage basis, and the stock
solvent/addition volumes are unspecified. No inferred numeric strength or dose
is asserted.

Recipe-specific preparation is retained. M225 and M243 explicitly stand
overnight; that instruction is not copied into M234. M229 separates medium
pH 6.5 from sulfide-stock pH 7.0 and has no added pressurization instruction.
M236 retains medium filtration, separately steamed solid sulfur, sulfide
neutralization/autoclaving, and late readjustment with sterile 1 N H2SO4.
Neither initial acid strength, molarity nor filtration pore size is guessed.
Gas/acid VARIABLE placeholders are replaced with supported preparation context.
No taxa-media association is added.

## Evidence And Verification

The [frozen context](context.json) has SHA256
`dea2ad0d74d2e1b5a2d5f333ce3ebc0fd368f4181aad51fbd7aaca180795ef67`.
All 14 fresh official source responses match the inspected captures. All
457 reference checks pass: 431 primary excerpts and 26 titles. Additional exact
excerpts in explanations are checked by the independent audit.

The [applied audit](applied-audit.json) accounts for 113 old quantity fields,
222 source rows and 520 claim decisions. It counts 431 evidence entries,
26 bibliography entries, five history events, 95 unsupported quantity fields
removed, 13 corrected stock doses, five corrected water inputs, 13 additional
water quantity fields, 39 relocated old nodes and eight separate reducing-stock
descriptors. These are not counts of added final concentrations. Source authors
and publication years were not supplied and are not invented.

All five baseline and applied schema/strict checks pass, as do applied reference
checks, guarded readback and a no-op rerun. The 149 new tests passed before
application; the focused regression suite passes 817 tests with two warnings.
Ruff, Black and whitespace checks pass. The [adversarial review](adversarial-review.md)
documents local source challenges and mutation tests, not an external PR approval.

All intended checks are terminal in [validation](validation.json). The fast tier
passes 8,776 tests, with 16 skipped, 1,945 deselected and two warnings. Explicit-
root strict validation and ID checks each pass for all 15,910 normalized records.
Product-label validation exits successfully with 91 nonblocking warnings
(50 implausible labels and 41 hydrate/anhydrous mismatches), plus 96,087 pairs
skipped for lack of an adapter. This does not recertify all chemical identities.

Global merge verification still fails with 1,247 name conflicts and 3,287
fingerprint issues. Freshness also fails: 6,320 tracked versus 10,777 fresh,
2,045 changed shared paths, 4,275 tracked-only, 8,732 fresh-only and zero
unchanged. These match the previous pass's counts; successful cohort checks
do not waive them or establish all-record/publication completion.

[Merge retention](merge-retention.json) routes all 15,910 normalized inputs into
10,777 groups. Each repaired record occupies its own group, and all five actual
generated outputs retain quantities, preparation and evidence and pass schema
validation. Only these outputs are recertified; no tracked merged YAML is written.

Four maintained indexes are refreshed with guarded scope: archaea, bacterial,
TOGO and master recipe indexes. Only the five targets' root ingredient and
solution counts change. No recipe-statistics or hierarchy-flag change is needed;
M236's legacy sulfur annotation remains on its root ingredient.

## Remaining Scope

[Coverage](followup-coverage.json) includes 11,779 of 15,910 exact normalized
paths, leaving 4,131 outside this follow-up report set. Report presence is not
proof that all scientific claims are resolved. [Cumulative accounting](cumulative-audit.json)
now counts 5,152 edited records and 32,368 added evidence entries.

The [handoff](next-work.md) preserves 73 unchanged M142-dependent candidates,
with the next six baselines and source captures frozen. It identifies M258's
historically verified wrong LB expansion and the M273/M274 formulation variant
and iron-amount conflict. Those six records were inspected, not edited or newly
counted as completed reviews.

No commit, push, PR, merge or branch deletion was performed in this pass. The
prior issue #150 progress draft remains unposted pending authorization; local
curation can continue. The runtime is the existing partial locked Python 3.13
environment, not clean CI; the full test suite was not rerun for this localized
repair.

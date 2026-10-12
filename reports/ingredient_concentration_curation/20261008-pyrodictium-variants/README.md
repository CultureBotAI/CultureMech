# Pyrodictium Ingredient And Variant Repair

Applied locally to three exact normalized records at reviewed commit
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. The all-record ingredient goal and
requested commit/push/PR/merge/branch-cleanup workflow remain incomplete.

Canonical reports, each with one exact tracked `- Record:` entry:

- [M196: Pyrodictium Brockii Medium](records/M196.md)
- [M197: Pyrodictium Ocultum Medium](records/M197.md)
- [M198: Pyrodictium Abysii Medium](records/M198.md)

## Scientific Decisions

The parent recipe gives 1 L prepared salt base and 10 ml trace minerals as
batch inputs, not a final-medium volume. Only the salt-base and trace-mineral
sections of M142/JCM151 are inherited. Their unqualified solid batch amounts
remain in evidence-backed notes; water inputs are not treated as final stock
volumes. Main resazurin, sulfur and parent yeast quantities likewise do not
establish final-medium rates.

The later sulfide addition is explicitly 10 ml per liter. M196's two extracted
sulfide nodes represent that one addition, not two doses or a nested stock.
The richer original annotation is preserved on the retained node. The source
5% label has no specified percentage basis, so no fixed stock strength or
derived final sulfide mass rate is invented. Stock pH 7.0 remains distinct
from medium pH 5.5.

The variants explicitly state final yeast rates: M197 retains 0.2 g/L, M198
retains 0.5 g/L. M198 sodium tungstate dihydrate is corrected from 0.1 g/L to
0.1 mg/L. Reciprocal evidence-backed links connect both children to M196.
M198's citric-acid omission directive is retained as context; no citric acid
is invented or deleted from inherited stock sections that do not contain it.

Original JCM203 preparation supports H2-CO2 rather than TOGO's H2-CO4 text.
The discrepancy remains explicit, and the original source supports the
effective atmosphere instruction. Separate sulfur sterilization, sulfide
preparation and addition, titration, and post-inoculation pressure remain
scoped to their stated stages. Gas and titrant placeholders are removed with
evidence, not replaced with guessed amounts.

## Evidence And Checks

The unchanged [frozen context](../20261008-basal-makeup/next-pyrodictium-context.json)
has SHA256
`09b7f63c7eff389cfce01e637008468bf4558ed2ca0a294e70d5d5c5d1b1615a`.
All eight fresh official source responses match those inspected captures.
The independent [applied audit](applied-audit.json) accounts for 32 old quantity
fields, 111 source rows and 184 claim decisions. The repair adds 130 evidence
entries, 16 bibliography entries and three history events. It corrects nine
stock-dose bases, removes 19 unsupported quantity slots, adds six scoped water
input slots and removes one duplicated stock node. Three explicit final-medium
rates are verified, including the one tungstate unit correction. These counts
are not 130 new final-medium concentrations. No taxa-media association is added.

Each record passes baseline and applied schema/strict checks. Reference checks
pass for 130 primary excerpts and 16 titles; the independent audit also checks
additional excerpts in evidence explanations. Application, readback and no-op
guards pass. The new tests pass 79 cases, the focused suite passes 495, and
the fast tier passes 8,451 with 16 skipped and 1,945 deselected. Ruff, Black
and whitespace checks pass. The existing partial locked Python 3.13
environment is not a clean CI install, and the full test suite was not rerun.
Broader terminal outcomes and artifact hashes are recorded in
[validation](validation.json). Explicit-root strict validation and ID checks
both cover all 15,910 normalized records and pass. Identifier-label validation
exits successfully with 91 nonblocking warnings and 96,087 pairs skipped for
lack of an adapter; this does not recertify all chemical groundings.

[Merge retention](merge-retention.json) routes all 15,910 current normalized
inputs into 10,777 groups. Each repaired record occupies its own group, and
its actual generated output preserves the repaired quantities, preparation,
links and evidence and passes schema validation. Only these three outputs
are recertified. No tracked merged YAML is rewritten. Three metadata indexes
are refreshed through the maintained generator; their only semantic change is
M196's root solution count from four to three after duplicate removal.

Global merge verification still fails with 1,247 name conflicts and 3,287
fingerprint issues. Freshness still fails: 6,320 tracked versus 10,777 fresh,
2,045 changed shared paths, 4,275 tracked-only, 8,732 fresh-only and zero
unchanged. The counts match the previous pass; these are not passing gates.

## Remaining Scope

The earlier [structural audit](../../ingredient_concentration_review/20261005T175229Z/summary.md)
finished with one report per record for its 22,230-record snapshot (15,910
normalized plus 6,320 merged). That completed inventory is distinct from the
unfinished scientific source-by-source review and corrections below.

[Follow-up coverage](followup-coverage.json) includes 11,769 of 15,910 exact
normalized paths; 4,141 remain outside this report set. Report presence does
not establish that every concentration is resolved. The cumulative audit
counts 5,142 edited records and 31,530 added evidence entries. These normalized
input counts must not be confused with the smaller merged-record inventory.

The [handoff](next-work.md) contains the remaining 83 unchanged M142-dependent
records and other unresolved work. Corpus-wide merge/freshness failures still
prevent publication readiness. The prior issue #150 progress comment remains
unposted pending authorization; local ingredient work is not blocked by that
publication restriction.

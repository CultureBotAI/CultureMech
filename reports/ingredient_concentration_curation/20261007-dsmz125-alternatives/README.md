# DSMZ 125 Alternative Preparations

Applied locally on 2026-10-07; not committed or published. This follow-up repairs
preparation scope and water inputs, not every scientific uncertainty in these
recipes. The full all-record concentration objective remains unfinished.

## Scope

- `CultureMech:000718`: `bacterial/methylobacterium_medium.yaml`.
- `CultureMech:004018`: `bacterial/KOMODO_125_METHYLOBACTERIUM_MEDIUM.yaml`.
- `CultureMech:011631`: `bacterial/mediadive_223_Main_sol_125.yaml`.

Paths are relative to `data/normalized_yaml`. The frozen [plan](plan.json)
contains complete before/after records, source captures, hashes and scoped
claims. Later reports use `Follow-up target`, not an additional `Record` entry,
so revisiting these paths does not inflate unique-record review coverage.

## Evidence And Decisions

The [original DSMZ recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium125.pdf)
states: "Add 5 ml methanol or incubate under methane-air (4:1). Adjust pH to 6.8."
The [medium API](https://mediadive.dsmz.de/rest/medium/125) and
[solution API](https://mediadive.dsmz.de/rest/solution/223) reproduce this
instruction and the basal table. The exact KOMODO 125 mapping links the same
original recipe; that mapping establishes identity, not quantities or growth.

The medium and solution response SHA-256 values are respectively
`2ccb593505b6c8f5cd63fd63bf1ecee7b33357bca201285eb2e958b70aff5ba1`
and `6f4797edabe8f2eb226a01b58ddc3e4c931f0e5b572ca01843860ecad4eb02ac`.
The frozen mapping capture SHA-256 is
`d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`.
No DOI, individual author or publication year is invented for these sources.

Both medium records now have separate inline methanol and methane-air options.
Neither is selected by default or combined with the other. Methanol is a 5 mL
batch addition, not a verified final-medium concentration. The 4:1 gas ratio
is not interpreted as a dissolved-methane dose. The standalone solution retains
the complete source preparation instruction and records the alternative scope
without adding unsupported root-level variants.

The source's 1000 mL distilled water becomes a `1 L` input in both medium
records. The standalone water input is corrected from `1000 PERCENT_V_V` to
`1 L`. Input volume is not asserted to be measured final volume. All 36 existing
basal concentration values and all 24 earlier ingredient evidence entries are
preserved, with basal-table context made explicit.

The [independent applied audit](diff-audit.json) verifies 23 new evidence entries,
five references, three curation events, one quantity/unit correction, two new
quantity slots and four inline preparation options. Each change has scoped
source support; these counts are different units and must not be added together.
No new record IDs or taxa-media growth associations are added.

## Remaining Uncertainty

Final liquid volumes, methanol purity and concentration, dissolved methane,
gas pressure and total gas volume remain unverified. The legacy KOMODO
`Aerobic: No` metadata is retained as unverified, not used to choose an option.
The standalone legacy variable-composition placeholder is unchanged.

The separately inspected `medium_125_modified_for_dsm_23675.yaml`,
`medium_125_modified_for_dsm_23679.yaml` and
`medium_125_modified_for_dsm_8269.yaml` remain unchanged. Their mapping names
explicitly identify strain-modified formulations; a link to the base PDF does
not establish those exact recipes. Existing source-duplicate links are preserved
as unresolved relationship hypotheses, not revalidated scientific equivalences.

## Verification

All six pre-edit schema checks passed. Applied readback, a zero-change second
apply, and independent full-record inversion passed. Twenty pre-apply guard
tests passed under both cached Python 3.11 and 3.13 environments; all 21 cohort
tests, including applied-record readback, subsequently passed under Python 3.13.

The broader regression and corpus checks are terminal in [validation.json](validation.json):
24 checks completed, including **976 passing focused regression tests**. All
15,910 normalized records pass strict schema validation; IDs, variant links,
three target schema checks, historical medium/solution/KOMODO readbacks,
cumulative semantic diff, coverage and whitespace checks also pass. Ruff and
Black checks pass for the seven changed Python files in this follow-up.
The separate [Python 3.13 result](python313-validation.json) records the 21-test
cohort run. Neither cached environment is a full maintained-environment or CI pass.

Product validation cannot load `oaklib`; the three reference checks cannot spawn
`linkml-reference-validator`. These four unavailable gates are not passes or
new scientific data findings. The remaining nonzero checks are actual-group
retention, global merge verification and freshness. Global verification still
reports 1,247 name conflicts and 3,287 fingerprint issues. Temporary generation
writes 6,493 of 6,493 groups with zero group-write failures, but the
[freshness comparison](merge-freshness.json) against 6,320 tracked outputs finds
3,719 only tracked, 3,892 only fresh, 1,657 changed and 944 unchanged.

The [actual-group retention check](merge-retention.json) fails full-field
retention for the DSMZ medium copy: ingredient metadata, root notes, references
and curation history are not all preserved. Its 16 scoped literal snippets
survive; shared quotes alone do not prove provenance retention. The canonical
KOMODO copy retains all checked fields and its 17 scoped snippets. Standalone
solution 223 correctly remains outside medium merging; exclusion is not a
medium-retention pass. The authoritative inputs remain intact, and no generated
merged records are published.

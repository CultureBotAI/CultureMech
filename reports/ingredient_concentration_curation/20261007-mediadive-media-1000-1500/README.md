# Receiving-Medium Concentration Source Pass: Records 1000-1499

Applied locally on 2026-10-07 against baseline
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. This is a partial source pass,
not completion of these recipes or the all-record ingredient objective.

## Scope And Result

The next 500 entries of the frozen [medium inventory](../20261007-medium-source-inventory.json)
have one exact-path result each under `records/`. IDs, exact tracked paths,
baseline hashes, and source captures were checked before preview and applying.
The [source-acquisition snapshot](../20261007-medium-source-fetch-1000-1500.json)
records 500 fresh official responses with zero failures; acquisition alone was
not counted as review. The next receiving-medium inventory offset is 1500.

- 142 authoritative normalized records changed; 358 remained unchanged.
- 869 ingredient evidence entries, 142 references, and 142 curation events added.
- No numerical amounts, units, ingredient identities, stocks, variants, growth
  associations, or previously existing evidence changed.
- No missing concentration slots were filled.
- Zero failed records and zero baseline/proposed closed-schema failures.

The [frozen plan](plan.json) contains every claim, decision, exact source snippet,
locator, calculation, and source/record hash. The independent
[preflight](preflight.json) removes only the proposed appended provenance and
proves equality with each original record. Read-back checks all 500 persisted
record hashes and 869 literal snippets; a repeated apply changes zero records.

## Evidence Scope

Evidence supports the provider-declared main-recipe concentration for the exact
accession, ingredient label/form, amount, unit, and applicable physical-state
condition. It does not independently establish measured final volume, a stock
composition, a downstream dilution, or secondary chemical-identity mappings.
No density, unknown stock strength, or missing final-volume basis is invented.

Each added YAML evidence entry cites the exact official MediaDive endpoint and
literal JSON row, full ingredient field path, source locator, retrieval time,
and response SHA256. Bibliography entries record title, institutional source,
source type, discovery mode, access date, and original recipe URL. Individual
authors and publication years are absent when not established from the source.

All 144 initially eligible records' main-solution preparation text and proposed
amounts were inspected. The original single-page DSMZ 1076b, 1293, and 1286 PDFs
were visually inspected in full. This is not manual inspection of all 500
original PDFs, nor proof that every claim in a processed record is resolved.

## Adversarial Findings

The [preparation-scope review](preparation-findings.md) withheld seven claims
across two records before applying the final batch:

- DSMZ 1076b combines mutually exclusive glucose/arginine/urea choices. Four
  proposed evidence entries, including unconditional urea support, were withheld.
- DSMZ 1293 has an explicit stock-to-medium ratio. Three proposed table-based
  claims were withheld pending preparation-stage and denominator reconciliation.
- DSMZ 1286's current glucose-only branch matches its original source. It does
  not combine alternatives; fructose is neither added nor implicitly verified.

Eleven new guard regression cases pass. None of the 277 previously accepted
medium records triggers either new guard; this is a bounded check for these
patterns, not a scientific revalidation of all their preparation instructions.
Historical plans and reports were not rewritten.

Other unresolved findings remain explicit:

- 309 records require source-specific stock-topology review.
- Three agar rows (DSMZ 1027, 1048, 1159) have conflicting source `amount` and
  `g_l` fields. No number or tolerance was changed to force agreement.
- Six records lack the required ingredient/preparation inventory; 17 have
  unresolved main-solution identity. Other source/name/duplicate-label conflicts
  remain recorded rather than bypassed.
- 11,030 unsupported rows include 9,457 source recipe rows, 1,107 preparation
  rows, 321 parent/child relationships, and 145 ingredient claims. There are
  also 7,595 conflict rows. These are report rows, not independent findings.

## Verification

The fresh baseline strict gate scanned all 15,910 normalized records without
errors; the representative open-schema check also passed. Post-apply outcomes
are captured in [validation.json](validation.json): 498 focused tests passed,
as did full strict validation, the ID gate, and representative open-schema
validation. Earlier medium source read-back and the KOMODO 12 repair still pass.
The [independent cumulative diff](../20261007-diff-audit-after-media-1500.json)
verifies 4,564 edited records, 26,554 new evidence entries, 4,592 references, and
4,568 curation events. The [coverage inventory](../20261007-followup-coverage-after-media-1500.json)
has 6,280 unique reported paths and 9,630 outside this follow-up.

The full suite cannot start because pytest-cov is missing. A retry without
coverage stops during collection on four missing dependency modules; it is not
a full-suite pass. Product validation cannot load OAK adapters, and automated
reference validation cannot launch its executable. These checks use isolated
Python 3.11, not the maintained Python 3.13/CI environment. Source verification,
schema validity, and merge retention are separate checks. No generated merge
or page files are copied into the worktree, and all changes remain uncommitted.

The [actual maintained merge-group audit](merge-retention.json) checks 142 records
in 130 real groups. Only 242 of 869 new amount/evidence pairs survive: 106 records
lose some or all new ingredient evidence and 100 lose the new bibliography entry.
This gate exits 1, confirming the existing mixed-source selection/evidence-loss
defect on this cohort. No general merger fix or safe-to-publish result is claimed.
The normalized records retain all their verified new snippets.

The global merge verifier also exits 1, with 1,247 name conflicts and 3,287
fingerprint issues. [Freshness](merge-freshness.json) exits 1: 6,320 tracked versus
6,491 freshly generated records, 3,718 only tracked, 3,889 only fresh, 1,526
changed, and 1,076 unchanged. Temporary regeneration did not update tracked
merged files. Ruff, Black, and the diff whitespace check pass for this batch's
changed surface. Its 500 reports have exactly one record line each, 500 unique
targets, and no preview state remaining.

The [next source-acquisition snapshot](../20261007-medium-source-fetch-1500-2000.json)
contains 500 fresh responses and verified baseline hashes for offsets 1500-1999,
with zero fetch failures. No review or edit is claimed for those targets; the
next review offset remains 1500 and reported coverage remains 6,280 paths.

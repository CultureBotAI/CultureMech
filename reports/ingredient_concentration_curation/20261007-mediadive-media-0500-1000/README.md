# Receiving-Medium Concentration Source Pass: Records 500-999

Applied locally on 2026-10-07 against baseline
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. This is another partial source pass,
not completion of these records or the all-record curation objective.

## Scope And Result

The next 500 entries of the frozen [medium inventory](../20261007-medium-source-inventory.json)
have one exact-path result each under `records/`. All target IDs and hashes were
checked before preview and again before writing. No target already had a report
in the evidence-backed follow-up inventory. The next inventory offset is 1000;
2,329 receiving-medium inventory entries remain outside these two batches.

- 117 authoritative normalized records changed; 383 remained unchanged.
- 653 ingredient evidence entries, 117 bibliography entries, and 117 curation
  events were appended.
- No numeric values, units, ingredient identities, stocks, variants, or growth
  associations changed. No missing concentration slots were filled.
- All 500 public source responses were retrieved serially with no failures.
- Zero failed records and zero baseline/proposed closed-schema failures.

The [frozen plan](plan.json) contains every decision, exact source quotation,
locator, old/new quantity, calculation, and source/record hash. An independent
preflight stripped only the proposed appended evidence, references, and history
and proved equality with every original record. Unsupported claims were not
changed. These counts describe edits and reports, not fully verified recipes.

## Evidence Boundaries

Evidence is limited to the exact source accession/name, ingredient form, local
quantity and applicable source condition. Explicit provider `g_l` values are
checked against the reported amount/unit/volume arithmetic; this is not proof of
measured final volume or a downstream dilution. Secondary chemical mappings
remain outside the amount-evidence claim. Supplier/stock attributes, optional
rows, ambiguous percentages, stock boundaries, and variant relationships remain
explicit follow-up rows rather than silently gaining support.

The retained quotations are literal excerpts of the official API responses at
`https://mediadive.dsmz.de/rest/medium/{id}`. Each evidence entry includes its
field path, source locator, access date, and response SHA256. References record
the title, institutional source, discovery mode, source type, and original
recipe link. Missing individual authors and publication years were not invented.

The complete single page of the [original DSMZ 468 recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium468.pdf)
was downloaded and visually checked against the API ingredient list and units.
PDF SHA256: `ac0f19aeeabdada654310865eb058c29ecdc77443bdf542fa037427f62e903e4`.
This is a representative original-document check, not manual inspection of all
500 PDFs. Main-solution preparation text was inspected for the records passing
the source-identity guard; the per-record reports retain preparation follow-ups.

## Unresolved Findings

- 349 records are blocked from automatic support by stock topology. The API
  stock composition cannot be treated as a direct-medium concentration.
- 32 arithmetic-conflict rows occur in eight records. No tolerance was widened
  and no existing quantity was replaced to force agreement.
- Ten records lack the source ingredient/preparation inventory required by the
  reviewer. Source identity, collection/link, and duplicate-label conflicts also
  remain open.
- 13,238 unsupported report rows include 11,437 unmatched source recipe rows,
  1,198 preparation-context rows, and 410 variant relationships. There are
  9,117 conflict rows. These are report rows, not independent scientific findings.
- Extraction input is not extract yield. The reviewer now withholds automatic
  support for soil/manure rows when the preparation separates solids. This
  prevents an unsupported main-medium interpretation for DSMZ 657; only its
  independently supported agar row gains evidence. Its stock boundary, water
  unit, and extraction-input representation still need repair.
- Applying that scope check to earlier work identified [an over-scoped DSMZ 12
  claim](extraction-scope-finding.md). The older record still needs authoritative
  correction; a hash/snippet read-back does not establish that its interpretation
  is scientifically valid.
- DSMZ 669's optional agar row has conflicting `amount` and `g_l` fields; its
  numeric value is not endorsed by this pass. DSMZ 752's solid-medium carbonate
  procedure is distinct from the current liquid record. DSMZ 584 and 849 retain
  their earlier curated ingredient notes/procedures without replacement.

## Verification

The [actual-group retention audit](merge-retention.json) exercises the maintained
matcher/merger for all 117 edited records in their 117 real corpus groups. Only
140 of 653 new amount/evidence pairs survive. Ninety-two records lose some or all
new ingredient evidence and 87 lose the new bibliography entry. The gate exits
1; normalized evidence remains intact. This confirms the pre-existing
single-ingredient-list/canonical-metadata selection problem on this new cohort,
not a reason to propagate evidence across unverified formulations.

The fresh full-corpus baseline strict check scanned 15,910 files with no errors;
the representative baseline open-schema check passed. The extraction guard has
seven new regression cases, including a negative control for ordinary separate
filter sterilization. Post-apply outcomes are captured in [validation.json](validation.json).
Global merge freshness and evidence-retention checks are separate gates, not
implied by schema success. No generated merge products are copied into the
worktree. All changes remain local and uncommitted.

The selected post-edit regression run passed 406 tests. Full strict validation
again passed for all 15,910 records, as did the ID gate. Read-back verifies all
500 record hashes and 653 new literal snippets; reapplication changes zero
records. The original medium batch still verifies its 500 hashes and 907
snippets through nine explicit successors, subject to the unresolved scope
finding above. The independent cumulative diff records 4,421 edited records and
25,675 new evidence entries. Current unique follow-up coverage is 5,779 paths,
leaving 10,131 outside these reports.

Product validation cannot load OAK adapters and the reference-validator
executable is unavailable; both exit 2, not success. These checks use isolated
Python 3.11. The preceding full-suite attempt failed for missing pytest-cov and,
without coverage, missing collection dependencies; it was not rerun here and
no full-suite or maintained Python 3.13/CI pass is asserted.

Final global merge verification exits 1 with 1,247 name conflicts and 3,287
fingerprint issues. [Freshness](merge-freshness.json) also exits 1: 6,320 tracked
versus 6,491 freshly generated records, 3,718 only tracked, 3,889 only fresh,
1,513 changed, and 1,089 unchanged. Regeneration was temporary only. Ruff and
Black passed for the edited Python files, the three post-report consistency
tests passed, 57 local report links resolved, and `git diff --check` passed.

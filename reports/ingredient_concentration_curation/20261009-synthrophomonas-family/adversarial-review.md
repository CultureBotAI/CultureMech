# Medium212 Adversarial Review

Scope: the initial 22-record preview in `plan.json`, its reviewed successor in
`plan-v2.json` and guarded application, not the full corpus or a published PR.
Findings are local issues; no GitHub issue creation is claimed. The successor
has changed 21 normalized records; S608 remains byte-exact unchanged.

## Findings

1. **P1: Generic nickel grounding loses the explicit hydrate form. Fixed and applied.**
   The initial proposal retained two `CHEBI:34887` assertions each in K212,
   D212, D212a and B2805, and one in S595. Their source rows specify
   `NiCl2 x 6 H2O`. The packaged
   MIM snapshot answers `CHEBI:53542` with `mapping_status=REJECTED`; substituting
   that answer would invent approval. Withdraw the nine generic assertions,
   retaining the supported mass rate and S595's `mediadive.compound:40` identity.
   Exact source PURLs, snippets, old pointers, fields and index hash are frozen in
   `identity-review.json`. This blocks application of the initial preview. The
   successor withdraws precisely these nine annotations, preserves quantities
   and compound:40, and passes the new explicit identity regression.

2. **P1: Recipe-level primary snippets escaped the new auditor. Fixed and retested.**
   The initial focused test run deliberately replaced the root evidence snippet
   in D212 and D212a with invented text. Both mutations escaped because the
   evidence traversal excluded the empty root path and the valid old text still
   appeared in extended explanations. Require every primary snippet, including
   root evidence, to be literal in the cited capture. Keep these regression
   attacks and rerun the independent audit. Root evidence is now checked; the
   corrected first-preview suite passes 824 tests and the successor suite passes
   827. This was an auditor defect, not a
   detected invented quote in the preview itself.

3. **Reference automation gap. Explicitly unresolved, manually checkable.**
   The production official-source validator has no BacDive page adapter. A
   cached primary HTML capture supports literal checking of the 32 strain rates
   and unquantified water row, but does not verify the separately located DOI
   version. Preserve PURL scope and report manual verification separately.

4. **P2: Evidence-only rows are mislabeled as corrections. Fixed and applied.**
   The shared emitter labels retained numerical quantities as `correct` even
   when the only addition is supporting evidence. This does not change an
   amount, but misstates the action in the claim ledger. In the successor,
   distinguish evidence-only additions, source-explicit nulls and unresolved
   final concentrations. Give withdrawn old quantities their original ingredient
   labels rather than a generic recipe-context label.
   The successor implements this distinction and adds regression checks for all
   32 unchanged BacDive quantities and the unquantified water row.

5. **P2: Preview ledgers would inflate or invalidate canonical coverage. Fixed.**
   Both immutable preview versions have a `- Record:` marker for the same 22
   targets as earlier canonical reports. Coverage now validates exact paths and
   one marker in every report, excludes only explicitly marked previews and
   continues to reject duplicate canonical reports. Eight focused coverage
   regressions pass, including hidden/ignored files and malformed previews.
   All 22 canonical reports link to the current applied ledgers. The 44 preview
   ledgers remain intact and are explicitly recorded as excluded from coverage.

6. **Application guards and cumulative accounting. Implemented and checked.**
   Apply/verify now require the frozen preview validation and every nested
   receipt hash, in addition to the shared source/target/concurrency guards.
   New regressions attack changed claims, proposal bytes, receipts and symlinks.
   A first fixture failed because it lacked a Git index; its receipt remains
   preserved. The corrected fixture uses a real temporary repository, and the
   successor run passes 837 tests. Readback and repeated application report no
   changes. The cumulative registry includes only the 21 actual changes, not
   the S608 no-op; the full proposal and ledgers retain all 22 reviewed records.

## Other Checks

The independent successor projection covers all 271 source nodes, all 259 old
quantity fields and 887 evidence-linked claims. All 44 successor schema/strict
commands pass. All 241 supported official reference checks pass, with the
BacDive adapter gap reported separately. Prior history and
unchanged root presentation are preserved. Source-reported rates, original batch
inputs and stock doses remain distinct; four KOMODO nulls and BacDive's
unquantified water are not converted to zero. Existing strain-growth annotations
remain unchanged. The historical preview fast tier passed 13,255 tests, with
16 skipped, 2,243 deselected and two dependency warnings. That result is not
substituted for the current application-code fast-tier run, which passes
12,700 tests, with 16 skipped, 2,829 deselected and two dependency warnings.
The existing classifier now assigns the entire medium212 module to corpus-tier
because its application fixture contains a normalized-data path. Its 565 tests
pass separately within the 837-test focused run. The eight coverage tests also
belong to corpus-tier and pass within the 127-test QA run. Collection and
receipt links are recorded in `test-selection.json`; the differing historical
fast-tier counts are not identical selections.
All 127 final QA tests pass, along with Ruff, Black and whitespace
checks. All 44 actual-written schema/strict commands and 241 supported
reference checks pass; the BacDive adapter gap is separate. Corpus strict/ID/
product gates pass. Six indexes are refreshed, four media are retained
separately by runtime merging, and eighteen standalone solutions are excluded.
Post-application presentation checks pass in a separately named receipt; the
original preview receipt was not overwritten when the first runner stopped
on that filename collision. Global merge verification and freshness remain failing.
The corpus-wide goal is not complete.

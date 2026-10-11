# Medium212 Adversarial Review

Scope: the initial 22-record preview in `plan.json` and its successor in
`plan-v2.json`, not the full corpus or a published PR. Findings are local issues;
no GitHub issue creation is claimed. No normalized YAML is changed yet.

## Findings

1. **P1: Generic nickel grounding loses the explicit hydrate form. Fixed in successor preview.**
   K212, D212, D212a and B2805 retain two `CHEBI:34887` assertions each; S595
   retains one. Their actual source rows specify `NiCl2 x 6 H2O`. The packaged
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

4. **P2: Evidence-only rows are mislabeled as corrections. Fixed in successor preview.**
   The shared emitter labels retained numerical quantities as `correct` even
   when the only addition is supporting evidence. This does not change an
   amount, but misstates the action in the claim ledger. In the successor,
   distinguish evidence-only additions, source-explicit nulls and unresolved
   final concentrations. Give withdrawn old quantities their original ingredient
   labels rather than a generic recipe-context label.
   The successor implements this distinction and adds regression checks for all
   32 unchanged BacDive quantities and the unquantified water row.

## Other Checks

The independent successor projection covers all 271 source nodes, all 259 old
quantity fields and 887 evidence-linked claims. All 44 successor schema/strict
commands pass. All 241 supported official reference checks pass, with the
BacDive adapter gap reported separately. Prior history and
unchanged root presentation are preserved. Source-reported rates, original batch
inputs and stock doses remain distinct; four KOMODO nulls and BacDive's
unquantified water are not converted to zero. Existing strain-growth annotations
remain unchanged. The full fast tier passes 13,255 tests, with 16 skipped,
2,243 deselected and two dependency warnings. Application remains disabled;
passing preview checks do not implement the reviewed apply gate or post-edit
validation. The corpus-wide goal is not complete.

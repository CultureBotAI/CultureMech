# Adversarial Review

This is a local adversarial audit, not an independent GitHub PR approval.
The full ingredient-review objective and publication workflow remain open.

## Addressed Findings

1. **Stock boundaries and duplicate sums.** M933 and M1153 combined nickel
   amounts from different stages and units; M933 did the same for selenium.
   Restored separate source-scoped nodes, preserving annotations and historical
   notes. Explicitly marked the old duplicate sums as superseded. The audit
   checks every original node and every source row, including repeated gases.
2. **Batch versus per-liter dosing.** Similar bicarbonate labels do not establish
   the same dose basis. M933/M1389 explicitly specify per-liter additions;
   M1390's first supplement block is a batch addition, while its later reducers
   are explicitly per liter. The repair uses the receiving source's instructions.
3. **Iron-stock final volume versus acid volume.** M1153 specifies 40 g made up
   to 100 mL with 0.1 N acid. The stock concentration is 400 g/L; 100 mL is not
   an independently specified acid dose. M1106 instead lists 2 g and 100 mL acid
   without establishing final stock volume. No 20 g/L rate is inferred there.
4. **Known versus unknown percentage basis.** Only M1378 explicitly supplies
   8% w/v bicarbonate strength. Its 1 g batch contribution supports 12.5 mL of
   that stock. Other percentage-labelled solutions remain unquantified in
   strength; their addition volumes are separately represented.
5. **Scope leakage from referenced stocks.** Only the M142 trace definition is
   expanded, not its entire Pyrococcus medium. Its KOH/pH instructions remain
   on that nested stock. Newly expanded ingredients receive no copied chemical
   grounding from another record. No final receiving volume is invented.
6. **Reproducibility and provenance loss.** The mutator previews first, pins
   source/baseline hashes and exact tracked paths, checks schemas before writing,
   and rejects concurrent edits and forged plans. Prior history is unchanged.
   All changes carry PURL/snippet support in the YAML, with an appended event.

## Verification

- 100 focused tests pass, including adversarial mutations of concentration,
  dose basis, acid makeup, percentage basis, nested membership, source quotes,
  annotations, prior history, bibliographic year and preparation scope.
- The independent applied audit accounts for 134 old quantity fields and 239
  source rows. The seven-record cohort adds 206 evidence entries, 19 references
  and seven events. A wider focused run passes 257 tests.
- Seven record pairs pass baseline and post-apply schema/strict checks.
  Guarded readback/no-op and independent source-tree audits pass.
- A fresh merge simulation retains all seven formulations and their evidence
  in separate schema-valid groups. It does not certify every other merge.

## Remaining Issues

- All seven reference commands fail. The 206 primary snippets match frozen
  sources literally; the installed matcher accepts 200 and rejects six because
  of bracket stripping or chemical-subscript rendering. API title extraction
  returns URLs instead of actual dataset names. No evidence is rewritten merely
  to conceal these validator limitations.
- M1153's sources both print `NaWO4`. Its old sodium-tungstate mapping is
  retained but explicitly not recertified; the formula discrepancy is unresolved.
- Gas placeholders remain unsupported fixed quantities. M190/M401 vitamin
  composition is still referenced rather than expanded in these records.
- Whole-corpus merge verification and generated-output freshness require further
  work. See terminal gate results in `validation.json` and `final-checks.json`.
- Filed [issue #571](https://github.com/CultureBotAI/CultureMech/issues/571) for
  the reproduced reference-validator defects after checking existing issues
  #150 and #565 and searching related issue history. Its fix remains open.
- No commit, push, PR, merge or branch deletion was performed for this cohort.
  These requested deliverables remain open.

# YAML Record Review: tindallia_texcocoensis_medium__c108e7bf

- Repository: CultureMech
- Record: `data/merge_yaml/merged/tindallia_texcocoensis_medium__c108e7bf.yaml`
- Started UTC: 2026-09-25T13:17:50Z
- Finished UTC: 2026-09-25T13:17:50Z
- Verdict: needs curation

## Target

Reviewed generated merged YAML for DSMZ medium 1223, `TINDALLIA TEXCOCOENSIS MEDIUM`.

The generated record is a single-source merge from `data/normalized_yaml/bacterial/tindallia_texcocoensis_medium.yaml`.

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 errors; the TSV contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed; the only diagnostic was the known eutils/pkg_resources startup warning.
- Embedded curation history: Not checked; the available history validator targets standalone `history/` records, not `MediaRecipe.curation_history`.

## Identity and Grounding

The medium identity is grounded to DSMZ medium 1223 by `media_term.term.id: mediadive.medium:1223`, the DSMZ link in `notes`, and the normalized source recipe.

The DSMZ 1223 source lists the parent medium per 1000 ml and adds 10 ml of trace element solution from DSMZ medium 141.

## Evidence

The generated record captures the directly listed DSMZ 1223 parent ingredients and pH 9.0.

Rows after `Resazurin` are trace-solution components from DSMZ medium 141. Those components are not independently present in the DSMZ 1223 parent formula; the parent formula calls for 10 ml of the stock.

## Completeness

No target organisms are present; that empty optional field is not a defect in this formulation review.

The generated record partially loses the stock boundary for the 10 ml trace element addition and cannot distinguish parent DSMZ 1223 salts from DSMZ 141 stock-solution ingredients.

## Findings

- Major issue: DSMZ medium 141 stock ingredients were flattened into the final DSMZ 1223 parent medium at stock concentrations. The source supports 10 ml trace stock per liter, not 1.5 g/L nitrilotriacetic acid, 3 g/L MgSO4 x 7 H2O, or the other stock recipe values as final concentrations.
- Major issue: the duplicate-ingredient cleanup added trace-stock salts to parent salts. `NaCl` is recorded as 76 g/L from 75 g/L parent NaCl plus 1 g/L trace-stock NaCl, and `CaCl2 x 2 H2O` is recorded as 0.30000000000000004 g/L from 0.2 g/L parent CaCl2 x 2 H2O plus 0.1 g/L trace-stock CaCl2 x 2 H2O. Those sums cross a source subrecipe boundary and are not source-backed final amounts.
- Minor issue: the trace-stock preparation text, including pH 6.5 and pH 7.0 adjustment, appears as a parent preparation step. That step belongs to DSMZ medium 141 trace stock, not directly to the DSMZ 1223 final medium.

## Recommended Edits

- Restore the DSMZ 1223 parent ingredient amounts without adding DSMZ 141 stock-solution rows to the parent totals.
- Model `Trace element solution (see medium 141), 10 ml` as a nested component or dilute its ingredients by 10 ml/L while retaining provenance that they came from DSMZ medium 141.
- Move the trace-stock pH 6.5 and pH 7.0 instructions under the trace component instead of the final Tindallia texcocoensis medium.

## Follow-up Checks

- Verify that regeneration no longer merges duplicate ingredients across parent and trace-stock levels.
- Re-run schema, strict, reference, and term validation after editing the normalized source YAML and regenerating the merge.

## Additional Notes

Exact local source search found the expected normalized DSMZ record for `tindallia_texcocoensis_medium`; the similarly numbered KOMODO medium 1223 record did not appear as an additional generated source for this merge. Ignored files were included for duplicate-report checks with `find`, and no pre-existing ignored report for this generated record was found.

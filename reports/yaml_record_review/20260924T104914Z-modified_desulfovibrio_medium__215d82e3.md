# YAML Record Review: modified_desulfovibrio_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_desulfovibrio_medium__215d82e3.yaml
- Started UTC: 2026-09-24T10:48:14Z
- Finished UTC: 2026-09-24T10:49:14Z
- Verdict: needs curation

## Target

Generated record `CultureMech:002489` for JCM/MediaDive medium `J1326`, `MODIFIED DESULFOVIBRIO MEDIUM`.

The generated record merges `modified_desulfovibrio_medium` from `data/normalized_yaml/bacterial/modified_desulfovibrio_medium.yaml`. The generated YAML was compared with that maintained owner, the JCM 1326 page, and MediaDive medium `J1326`.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed with no error rows.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct JCM/MediaDive `J1326` identity and preserves pH 7.3.

It flattens three JCM local sections, `Solution A`, `SolutionB`, and `SolutionC`, into one undifferentiated ingredient list. It also expands three medium references, `FeCl2 solution`, `Trace element solution`, and `Trace vitamins`, from MediaDive solution recipes and loses the JCM fact that the main formula adds only 1 ml, 1 ml, and 10 ml of those stocks.

## Evidence

JCM 1326 lists 0.5 g K2HPO4, 0.5 g KH2PO4, 1.0 g NH4Cl, 1.0 g Na2SO4, 2.0 g MgSO4 x 7 H2O, 0.1 g CaCl2 x 2 H2O, 2.0 g sodium lactate, 1.0 g yeast extract, 1.0 ml FeCl2 solution from JCM 187, 1.0 ml trace element solution from JCM 187, 10.0 ml trace vitamins from JCM 197, 1 mg resazurin, and 980 ml distilled water in `Solution A`.

The same page then lists `SolutionB` as 0.1 g FeSO4 x 7 H2O plus 10.0 ml distilled water and `SolutionC` as 0.1 g sodium thioglycolate, 0.1 g ascorbic acid, and 10.0 ml distilled water. MediaDive normalizes the direct rows over a 1012 ml final volume.

The generated record drops all three distilled-water rows and inserts full-strength stock compositions for the external FeCl2, trace-element, and vitamin stocks. For example, the generated HCl and FeCl2 x 4 H2O rows are the FeCl2 stock formula, not the final amounts produced by a 1 ml addition to JCM 1326; likewise, each trace-element and vitamin row reflects the referenced stock strength instead of the diluted contribution.

## Completeness

The generated YAML preserves the direct non-water rows from JCM 1326 and keeps the pH adjustment and N2 handling prose.

It is incomplete for local Solution A/B/C structure, solvent rows, and external stock-reference structure. It also does not retain explicit `see Medium No. 187` or `see Medium No. 197` references for the FeCl2, trace-element, and vitamin stocks.

## Findings

- High: FeCl2, trace-element, and trace-vitamin stock formulas are flattened as full-strength final-medium ingredients even though JCM 1326 adds only 1 ml, 1 ml, and 10 ml of those external stocks.
- Medium: The three JCM sections `Solution A`, `SolutionB`, and `SolutionC` are reduced to prose-only preparation labels, so row membership is not recoverable from the ingredient list.
- Medium: The 980 ml, 10 ml, and 10 ml distilled-water rows for the three local sections are absent.
- Low: `NiCl2 x 6 H2O` is grounded to generic nickel dichloride instead of a hexahydrate-specific term.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/modified_desulfovibrio_medium.yaml` with structured `Solution A`, `SolutionB`, and `SolutionC` groupings from JCM 1326.
- Preserve the FeCl2 solution, trace-element solution, and trace-vitamin additions as stock references with 1 ml, 1 ml, and 10 ml volumes rather than copying every component of the referenced JCM 187 and JCM 197 stocks into direct final-medium rows.
- Add the local distilled-water rows for 980 ml in `Solution A` and 10 ml each in `SolutionB` and `SolutionC`.
- Reassess the `NiCl2 x 6 H2O` ontology mapping during repair.
- Regenerate `data/merge_yaml/merged/modified_desulfovibrio_medium__215d82e3.yaml` after the maintained owner is repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated record against JCM 1326 and MediaDive `J1326` to verify Solution A/B/C row membership, the three solvent rows, the FeCl2/trace-element/vitamin stock references, pH 7.3, and N2 gas-handling text.

## Additional Notes

None found.

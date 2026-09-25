# YAML Record Review: methanosphaera_mcb_3_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanosphaera_mcb_3_medium.yaml
- Started UTC: 2026-09-24T05:11:53Z
- Finished UTC: 2026-09-24T05:11:53Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:009213` for TOGO medium `M2658`, "Methanosphaera (MCB-3) Medium", derived from DSMZ Medium 322.

## Validation

- LinkML open schema validation: Passed; exited 0 with no diagnostics.
- Strict recipe validation: Passed; `/private/tmp/methanosphaera_mcb_3_medium.strict.tsv` contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

- The TOGO `M2658` identity and DSMZ Medium 322 source URL are preserved.
- The generated record drops essential DSMZ 322 parent evidence: DL-Dithiothreitol is absent, pH 6.7-6.9 is absent, and the preparation steps are absent.
- The generated YAML has no `ph_value`, `ph_range`, or `preparation_steps` top-level keys; an exact `rg --no-ignore --hidden` check against this record returned no matches for those keys.
- The formula structure is not source-faithful because 10 ml Modified Wolin mineral stock and the Wolin vitamin stock are flattened into the parent list while several stock additions are represented as empty `G_PER_L` solution stubs.

## Evidence

- DSMZ 322 and MediaDive 322 agree that the parent formula includes 100 ml clarified rumen fluid, 10 ml Modified Wolin's mineral solution, 1.9 ml 0.1% Na2SeO4, 0.7 ml 0.1% NiCl2 x 6 H2O, 3 ml 0.1% FeSO4 x 7 H2O solution, 2 ml Wolin's vitamin solution (10x), 0.5 g DL-Dithiothreitol, and 900 ml distilled water.
- DSMZ 322 defines separate clarified rumen fluid, Modified Wolin mineral, Wolin vitamin, and FeSO4 stock preparations; MediaDive preserves at least clarified rumen fluid, Modified Wolin solution 241, Wolin solution 5980, and FeSO4 solution 5861 as child solutions.
- The generated parent water is `2900.0 G_PER_L` with duplicate notes showing a merge of the 900 ml parent water row plus two 1000 ml stock water rows.
- MediaDive solution 6187 is a small EDTA trace solution, and MediaDive solution 6241 is a three-compound, 100 ml vitamin solution. Those live solution records do not match the Modified Wolin and Wolin 10x stocks named in DSMZ 322.

## Completeness

- Several parent salts, organics, rumen fluid, methanol, cysteine, sulfide, and some stock-addition labels are present.
- DL-Dithiothreitol is missing.
- The pH range, two DSMZ preparation steps, and clarified-rumen-fluid preparation are missing.
- Child stock boundaries are absent or linked to the wrong live MediaDive solutions.

## Findings

1. Major - Required DL-Dithiothreitol is missing. DSMZ and MediaDive list 0.50 g DTT in the parent recipe and the DSMZ instructions say DTT is added from a sterile anoxic, filter-sterilized stock under 100% N2, but the generated YAML has no DTT row.
2. Major - Modified Wolin mineral stock is flattened into the parent formula. The record sums parent and stock MgSO4 x 7 H2O, NaCl, and CaCl2 x 2 H2O rows and exposes NTA, MnSO4, FeSO4, trace metals, selenite, tungstate, and KAl(SO4)2 x 12 H2O as parent ingredients even though DSMZ 322 adds only 10 ml of the stock.
3. Major - The vitamin stock is flattened and its milligram entries were serialized as grams per liter. Rows such as 2 mg biotin, 10 mg pyridoxine-HCl, and 0.1 mg Vitamin B12 appear as `2 G_PER_L`, `10 G_PER_L`, and `0.1 G_PER_L`.
4. Major - Main and stock water scopes were merged. The source has 900 ml parent water and separate 1 L waters for Modified Wolin and Wolin vitamin stocks, but the generated parent row is `2900.0 G_PER_L`.
5. Major - Several stock-addition volumes were converted to empty gram-per-liter solution stubs. The 0.5 ml resazurin, 1.9 ml selenate, 0.7 ml nickel, and 3 ml FeSO4 solution rows became `G_PER_L` stubs, and the named MediaDive links for `Trace element solution` and `Vitamin solution` do not match the DSMZ 322 stocks.
6. Major - pH and preparation instructions are absent. The record omits H2/CO2 sparging, pH 6.8-7.0 adjustment before autoclaving, pH 6.7-6.9 check before use, filter sterilization of vitamins and DTT, post-inoculation 1 bar H2/CO2 overpressure, and clarified rumen fluid preparation.

## Recommended Edits

- Recurate DSMZ 322 with distinct parent, clarified-rumen-fluid, Modified Wolin mineral, Wolin 10x vitamin, and FeSO4 stock scopes.
- Restore DL-Dithiothreitol as a 0.5 g parent addition and preserve its sterile anoxic stock handling.
- Keep resazurin, selenate, nickel, FeSO4, Modified Wolin, Wolin vitamin, methanol, and clarified rumen fluid as source-volume additions rather than `G_PER_L` stubs.
- Remove the wrong `mediadive.solution:6187` and `mediadive.solution:6241` links unless a source shows that TOGO intentionally substituted those stocks for DSMZ 322.
- Restore the pH range and both DSMZ 322 preparation paragraphs, including the 1 bar gas overpressure after inoculation.

## Follow-up Checks

- Re-run focused schema, strict, reference, and term validators on the regenerated merged YAML.
- Confirm that no regenerated parent row sums 900 ml, 1000 ml, and 1000 ml water into one parent concentration.
- Confirm that the final ingredient list includes DL-Dithiothreitol and no full-strength Modified Wolin or Wolin vitamin stock components as parent rows.

## Additional Notes

The stale generic `mediaingredientmech_chebi_term` on `MgSO4 x 7 H2O` should be refreshed after the formula structure is repaired; fixing it alone would not address the larger stock-flattening defect.

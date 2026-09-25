# YAML Record Review: methanofollis_ethanolicus_medium__33b4825e
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanofollis_ethanolicus_medium__33b4825e.yaml
- Started UTC: 2026-09-24T03:38:13Z
- Finished UTC: 2026-09-24T03:39:46Z
- Verdict: needs curation

## Target
- ID: CultureMech:010109
- Name: methanofollis_ethanolicus_medium
- Label: Methanofollis Ethanolicus Medium
- Category: archaea
- Source: TOGO:M701, imported from JCM_M682
- Merge fingerprint: 33b4825ecfa313ce06f42f13081d0384fcbba6b51a8f97424e2777124bf40ffb
- Merged from: TOGO_M701_Methanofollis_Ethanolicus_Medium

## Validation
- Open schema validation: Passed; no issues found.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; 0 reference checks, all passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The record identity matches TOGO M701 and JCM 682.
- `Solution A` and `Solution B` are local JCM 682 subrecipes, but the YAML links them to unrelated global MediaDive solution records `mediadive.solution:5342` and `mediadive.solution:5343`.
- CoCl2 x 6 H2O is grounded to generic cobalt dichloride, and NiCl2 x 6 H2O is grounded to generic nickel dichloride, despite hydrated source labels.

## Evidence
- JCM 682 defines Solution A as salts, yeast extract, trace vitamins, trace elements, NaHCO3, 1 mg Resazurin, and 900 ml water; Solution B as 0.46 ml ethanol plus 100 ml water; and the complete medium as 0.9 volume Solution A plus 0.1 volume Solution B plus 0.01 volume each of 3% L-Cysteine HCl x H2O and 3% Na2S x 9 H2O solutions.
- The JCM source instructs users to boil Solution A, cool under N2-CO2 80:20, dispense Solution A under the same gas, stand overnight after autoclaving, adjust and filter-sterilize Solution B under N2, then anaerobically add the reducing solutions and incubate with a 10% inoculum.
- The generated YAML has the children of Solution A, Solution B, Trace vitamins solution, and Trace element solution as top-level final ingredients.
- The generated YAML sums 900 ml Solution A water, 100 ml Solution B water, and the two 1 L trace-stock water rows into `1002.0 G_PER_L`.
- The generated `solutions` array keeps `Solution A`, `Solution B`, `Trace vitamins solution`, `Trace element solution`, and Na2S x 9 H2O as empty `Unknown solution` stubs.

## Completeness
- The JCM 682 formulas are present in flattened form.
- The nested Solution A/B, trace-vitamin, trace-element, and reducing-stock scopes are absent.
- The preparation workflow is absent.
- Empty optional fields are acceptable, but these empty solution stubs stand in for required source subrecipes.

## Findings
- JCM 682 solution hierarchy is flattened. Solution A, Solution B, trace vitamins, and trace elements need to be nested under their source scopes instead of promoted to final-medium ingredients.
- Local Solution A and Solution B are linked to the wrong reusable solutions. MediaDive 5342 and 5343 have unrelated compositions and must not be used for the JCM 682 local subrecipes.
- Source volume additions are represented as mass concentrations: 900 ml Solution A, 100 ml Solution B, 2 ml trace vitamins, 1 ml trace elements, and 10 ml Na2S solution are encoded as `G_PER_L`.
- The L-Cysteine HCl x H2O 3% reducing solution was left as a top-level `10 G_PER_L` ingredient rather than a 10 ml solution addition.
- Milligram vitamin stock rows are inflated to whole-number `G_PER_L` values, and 1 mg Resazurin likewise appears as `1 G_PER_L`.
- The preparation text that defines pH adjustment, N2/CO2 gas handling, filter sterilization, anaerobic addition, and final Solution A/B mixing was lost.
- CoCl2 x 6 H2O and NiCl2 x 6 H2O need hydrate-specific grounding if suitable CHEBI identifiers are available.

## Recommended Edits
- Re-curate `data/normalized_yaml/archaea/TOGO_M701_Methanofollis_Ethanolicus_Medium.yaml` from JCM 682.
- Model Solution A and Solution B as local nested subrecipes without `mediadive.solution:5342` or `mediadive.solution:5343` references.
- Nest the Trace vitamins solution and Trace element solution recipes under Solution A, with their own 1 L water rows.
- Represent the final medium as 0.9 volume Solution A, 0.1 volume Solution B, and 0.01 volume each of the two 3% reducing-agent stocks.
- Keep source milligram values inside their stock scopes and convert to grams only after respecting the stock scope.
- Restore preparation notes for Solution A boiling and N2/CO2 cooling, Solution B pH adjustment and filter sterilization under N2, anaerobic reducing-agent addition, and 10% inoculation.
- Re-ground CoCl2 x 6 H2O and NiCl2 x 6 H2O.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanofollis_ethanolicus_medium__33b4825e.yaml`.
- Confirm that `Unknown solution`, `mediadive.solution:5342`, and `mediadive.solution:5343` are gone from this JCM 682 owner.
- Confirm that source ml volumes are not encoded as `G_PER_L`.
- Confirm that water from the four solution scopes is no longer summed into a single `1002.0 G_PER_L` row.
- Confirm that source mg values are not inflated to grams per liter at final scope.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- The similarly named NBRC 1020/TOGO M1795 record is a separate source recipe and should be reviewed or repaired independently.

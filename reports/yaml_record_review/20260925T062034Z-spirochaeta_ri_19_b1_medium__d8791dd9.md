# YAML Record Review: spirochaeta_ri_19_b1_medium__d8791dd9

- Repository: CultureMech
- Record: data/merge_yaml/merged/spirochaeta_ri_19_b1_medium__d8791dd9.yaml
- Started UTC: 2026-09-25T06:19:30Z
- Finished UTC: 2026-09-25T06:20:35Z
- Verdict: needs curation

## Target

Generated merged YAML for DSMZ 509a, SPIROCHAETA RI 19.B1 MEDIUM.

## Validation

- LinkML open validation: Passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: Passed; `/private/tmp/spirochaeta_ri_19_b1_medium__d8791dd9.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The record is grounded to the correct DSMZ 509a source and preserves the pH range 6.8-7.0.

The ingredient hierarchy is not correct: DSMZ 509a is a named Solution A through Solution E assembly, but the generated record flattens those solutions and the three nested stocks into one parent ingredient list.

## Evidence

DSMZ 509a lists a final medium assembled from 962 ml Solution A, 20 ml Solution B, 1 ml Solution C, 10 ml Solution D, and 10 ml Solution E.

Solution A contains 4.00 g NaCl, 0.80 g MgCl2 x 6 H2O, 0.50 g KCl, 0.30 g NH4Cl, 0.20 g KH2PO4, 0.03 g CaCl2 x 2 H2O, 1.00 ml trace element solution SL-10, 1.00 ml selenite-tungstate solution, 0.50 ml sodium resazurin, and 960.00 ml distilled water. Solution B is Na2CO3 in 20.00 ml distilled water, Solution C is Wolin's vitamin solution (10x), Solution D is starch in 10.00 ml distilled water, and Solution E is Na2S x 9 H2O in 10.00 ml distilled water.

Trace element solution SL-10, selenite-tungstate solution, and Wolin's vitamin solution are separate 1 L stocks with their own water rows and preparation requirements.

## Completeness

The generated record omits every named final solution addition, the Solution A/B/D/E water rows, and all water rows from the nested stocks. It stores component concentrations at the concentration of the local stock, not the final medium.

## Findings

- Major: the 962 ml Solution A, 20 ml Solution B, 1 ml Solution C, 10 ml Solution D, and 10 ml Solution E final additions are not represented.
- Major: Solution B, D, and E contents are flattened at stock strength: 1 g Na2CO3 per 20 ml is represented as `50` `G_PER_L`, 1 g starch per 10 ml as `100` `G_PER_L`, and 0.3 g Na2S x 9 H2O per 10 ml as `30` `G_PER_L`.
- Major: trace element solution SL-10, selenite-tungstate solution, and Wolin's vitamin solution contents are parent ingredients instead of nested stock components.
- Major: the generated record drops the 960 ml Solution A water row, the 20 ml Solution B water row, the two 10 ml water rows in Solutions D and E, and all three 1 L stock water rows.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/spirochaeta_ri_19_b1_medium.yaml` to model DSMZ 509a as a Solution A through Solution E assembly with source milliliter volumes.
- Nest trace element solution SL-10, selenite-tungstate solution, and Wolin's vitamin solution under Solution A or Solution C as appropriate instead of flattening them into parent ingredients.
- Restore all source water rows at their original hierarchy.
- Keep the pH range 6.8-7.0 and the existing N2/CO2 sterilization instructions.
- Regenerate `data/merge_yaml/merged/spirochaeta_ri_19_b1_medium__d8791dd9.yaml` from the repaired normalized record.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated record.
- Confirm final Solution A through Solution E additions are present with 962 ml, 20 ml, 1 ml, 10 ml, and 10 ml volumes.
- Confirm Na2CO3, starch, and Na2S x 9 H2O are not parent ingredients at stock strength.
- Confirm the pH range remains 6.8-7.0.

## Additional Notes

None found.

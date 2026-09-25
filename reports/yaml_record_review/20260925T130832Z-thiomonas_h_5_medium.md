# YAML Record Review: thiomonas_h_5_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thiomonas_h_5_medium.yaml`
- Started UTC: 2026-09-25T13:08:32Z
- Finished UTC: 2026-09-25T13:08:32Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:001621`
- Name: `thiomonas_h_5_medium`
- Source grounding: direct DSMZ/MediaDive import of DSMZ Medium 493, `THIOMONAS (H5) MEDIUM`

## Validation

- Schema validation: passed with no issues.
- Strict validation: passed with zero errors; `/private/tmp/thiomonas_h_5_medium.strict.tsv` was header-only.
- Reference validation: passed with zero checks.
- Term validation: passed after the known EUtils warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The record is grounded to `mediadive.medium:493`.
- DSMZ Medium 493 and the MediaDive REST payload agree on a 1012 ml parent recipe with 2 ml of a 0.1% w/v NiCl2 x 6 H2O solution and 10 ml of Modified Wolin's mineral solution.
- The scoped source search found the related KOMODO 493 import reviewed earlier, but did not find a second direct DSMZ 493 generated record. The search included ignored and hidden files.

## Evidence

- The DSMZ 493 parent contains KCl 0.33 g, MgCl2 x 6 H2O 2.75 g, MgSO4 x 7 H2O 3.45 g, NH4Cl 1.25 g, CaCl2 x 2 H2O 0.14 g, K2HPO4 0.14 g, KH2PO4 0.14 g, NaCl 0.50 g, 2 ml of 0.1% w/v NiCl2 x 6 H2O, 10 ml Modified Wolin's mineral solution, 0.50 g yeast extract, and 1000 ml water.
- Modified Wolin's mineral solution is a separate 1 L stock with nitrilotriacetic acid 1.50 g, MgSO4 x 7 H2O 3.00 g, MnSO4 x H2O 0.50 g, NaCl 1.00 g, FeSO4 x 7 H2O 0.10 g, CoSO4 x 7 H2O 0.18 g, CaCl2 x 2 H2O 0.10 g, ZnSO4 x 7 H2O 0.18 g, CuSO4 x 5 H2O 0.01 g, AlK(SO4)2 x 12 H2O 0.02 g, H3BO3 0.01 g, Na2MoO4 x 2 H2O 0.01 g, NiCl2 x 6 H2O 0.03 g, Na2SeO3 x 5 H2O 0.30 mg, Na2WO4 x 2 H2O 0.40 mg, and 1000 ml water.
- The main recipe is adjusted to pH 3.5 before autoclaving; the mineral stock has its own KOH-mediated pH steps.

## Completeness

- The generated record captures the parent salts, the yeast extract, the stock components, and both preparation instructions.
- The generated record has no `target_organisms`; there are no growth claims to verify.

## Findings

- The 10 ml dose of Modified Wolin's mineral solution is flattened at stock concentrations and duplicate stock salts were summed into the parent recipe.
- Parent MgSO4 x 7 H2O, CaCl2 x 2 H2O, NaCl, and NiCl2 x 6 H2O are inflated to `6.45`, `0.24000000000000002`, `1.5`, and `0.032` g/L by summing parent and stock amounts.
- The 2 ml 0.1% NiCl2 x 6 H2O addition should remain distinct from the 10 ml mineral stock; the generated record erases that topology.
- The Modified Wolin's mineral solution pH preparation is promoted into the parent `preparation_steps`, where it reads as a final medium pH step.

## Recommended Edits

- Restore Modified Wolin's mineral solution as a stock recipe dosed at 10 ml in the DSMZ 493 parent.
- Keep the 2 ml 0.1% NiCl2 x 6 H2O addition separate from NiCl2 in the mineral stock.
- Move the pH 6.5 and pH 7.0 KOH instructions under the mineral stock and leave the parent recipe at pH 3.5 with sulfuric acid.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after the stock reconstruction.
- Compare the repaired direct DSMZ 493 record against the related KOMODO 493 record so both use the same stock model.

## Additional Notes

- Empty optional fields were not treated as defects.

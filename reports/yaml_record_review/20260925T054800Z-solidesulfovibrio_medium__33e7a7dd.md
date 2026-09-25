# YAML Record Review: solidesulfovibrio_medium__33e7a7dd

- Repository: CultureMech
- Record: data/merge_yaml/merged/solidesulfovibrio_medium__33e7a7dd.yaml
- Started UTC: 2026-09-25T05:47:00Z
- Finished UTC: 2026-09-25T05:48:01Z
- Verdict: needs curation

## Target

Generated merged YAML for DSMZ 896, SOLIDESULFOVIBRIO MEDIUM. The generated target kept CultureMech:002059 as the canonical DSMZ record and merged the KOMODO 896 branch as a SOURCE_DUPLICATE.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/solidesulfovibrio_medium.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The primary DSMZ identity is correct: DSMZ Medium 896 is SOLIDESULFOVIBRIO MEDIUM and has final pH 7.0. The KOMODO 896 DESULFOVIBRIO MAGNETICUS MEDIUM branch points back to DSMZ Medium 896 and has the same imported composition, so this looks like a source duplicate rather than a distinct recipe.

The generated merge loses the CHEBI grounding for `(-)-Quinic acid`. Both normalized inputs carry CHEBI:17521 for that row, but the generated record keeps only the preferred label and concentration.

## Evidence

DSMZ Medium 896 and the MediaDive 896 REST export agree that the final medium has a final volume of 1007 ml with 0.20 g KH2PO4, 0.06 g NH4Cl, 2 ml Fe(III) quinate solution 0.01 M, 4 ml Modified Wolin's mineral solution, 0.58 g Na2-fumarate, 0.44 g Na-pyruvate, 1 ml Wolin's vitamin solution (10x), 0.05 g L-Cysteine HCl x H2O, and 1000 ml distilled water.

They also agree that Modified Wolin's mineral solution, Fe(III) quinate solution, and Wolin's vitamin solution are separate 1000 ml stock recipes. The minerals, Fe(III) quinate components, and vitamin masses in the generated parent ingredient list are stock-solution concentrations, not final-medium concentrations.

## Completeness

The generated record omits the three final-medium stock-solution additions and the 1000 ml final distilled water row. It also omits the distilled-water rows for all three stock-solution preparations after flattening their solutes into the parent recipe.

Preparation text is mostly preserved: the parent N2 sparging, autoclaving, post-autoclave vitamin/cysteine additions, pH adjustment to 7.0, mineral-solution pH adjustment, and Fe(III) quinate N2 filtration instruction are present.

## Findings

- Critical: stock solutions are flattened at stock strength into the final medium. `Nitrilotriacetic acid` through `Na2WO4 x 2 H2O`, `FeCl3 x 6 H2O` and `(-)-Quinic acid`, and all Wolin vitamin rows are 1000 ml stock concentrations in the DSMZ source, but the generated record lists them as final `G_PER_L` ingredients.
- Critical: the generated ingredient list omits the actual final-medium additions for `Fe(III) quinate solution 0.01 M` at 2 ml, `Modified Wolin's mineral solution` at 4 ml, `Wolin's vitamin solution (10x)` at 1 ml, and `Distilled water` at 1000 ml in the 1007 ml final volume.
- Major: the generated merge drops the `(-)-Quinic acid` chemical grounding that is present in both normalized source records.
- Major: the KOMODO branch's note says `Aerobic: Yes` even though the DSMZ 896 preparation sparges the medium and stock solutions with 100% N2. Do not let this note override the DSMZ anaerobic handling when the normalized duplicate is repaired.

## Recommended Edits

- Repair the DSMZ 896 normalized source at `data/normalized_yaml/bacterial/solidesulfovibrio_medium.yaml` to model the 1007 ml final recipe with three stock-solution ingredients instead of flattening those stock solutions into the parent ingredient list.
- Repair or regenerate `data/normalized_yaml/bacterial/KOMODO_896_DESULFOVIBRIO_MAGNETICUS_MEDIUM.yaml` from the same DSMZ 896 structure before merging, because its composition was copied from DSMZ Medium 896 and currently has the same stock-flattening defect.
- Preserve CHEBI:17521 for `(-)-Quinic acid` during duplicate merging.
- Regenerate `data/merge_yaml/merged/solidesulfovibrio_medium__33e7a7dd.yaml` from the repaired normalized records.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated merged record.
- Diff the regenerated ingredient list against DSMZ 896 and confirm that the parent recipe contains 9 final rows, including 3 stock-solution additions and 1000 ml distilled water.
- Confirm that the stock-solution gram and milligram rows no longer appear as final `G_PER_L` ingredients unless a stock recipe is being represented in a scoped preparation record.

## Additional Notes

None found.

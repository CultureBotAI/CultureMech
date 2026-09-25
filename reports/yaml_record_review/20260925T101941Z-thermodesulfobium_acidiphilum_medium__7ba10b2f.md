# YAML Record Review: thermodesulfobium_acidiphilum_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobium_acidiphilum_medium__7ba10b2f.yaml
- Started UTC: 2026-09-25T10:16:00Z
- Finished UTC: 2026-09-25T10:19:41Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermodesulfobium_acidiphilum_medium__7ba10b2f`, which represents direct MediaDive/DSMZ medium `901a` as `CultureMech:002068`.

## Validation

- Schema: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; the strict TSV had only its header row and no error rows.
- Reference validation: Passed with 0 checks reported.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

The target has the expected `mediadive.medium:901a` identity, DSMZ 901a citation, and pH 4.5. An exact ignored-inclusive search for `mediadive.medium:901a` and `DSMZ_Medium901a.pdf` found a separate `TOGO_M3119_Thermodesulfobium_Acidiphilum_Medium` branch that still generates `data/merge_yaml/merged/THERMODESULFOBIUM_ACIDIPHILUM_MEDIUM.yaml`.

## Evidence

MediaDive 901a and the DSMZ Medium 901a PDF list a 1017 ml main solution with 1 ml Trace element solution SL-10, 0.5 ml 0.1% sodium resazurin, 3 g yeast extract, 1 ml Wolin's vitamin solution 10x, 15 ml neutralized 3% sulfide solution, and 1000 ml distilled water. SL-10 is a 1000 ml stock containing 10 ml 25% HCl plus iron and trace-metal salts; Wolin's vitamin solution 10x is a 1000 ml stock with milligram vitamin amounts; the neutralized sulfide solution is a 100 ml stock containing 3 g `Na2S x 9 H2O`.

## Completeness

The target preserves the DSMZ pH and preparation text. It does not preserve the three stock-solution additions; all three are expanded or converted into top-level ingredients.

## Findings

- High: the 1 ml SL-10 trace-element addition was flattened at stock concentration. The generated final medium includes 2.5 g/L HCl, 1.5 g/L `FeCl2 x 4 H2O`, 0.19 g/L `CoCl2 x 6 H2O`, and other SL-10 stock rows even though only 1 ml of SL-10 is added to 1017 ml of medium.
- High: the 1 ml Wolin's vitamin solution 10x addition was flattened at stock concentration. The generated biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid rows are the 1 L vitamin-stock values, not final-medium concentrations.
- High: the 15 ml neutralized sulfide stock was imported as `Na2S x 9 H2O` at `30 G_PER_L`. The source adds 15 ml of a 3% stock; 30 g/L is the stock strength, not the final-medium concentration.
- Medium: the TOGO M3119 import of the same DSMZ 901a recipe is unmerged with this direct MediaDive/DSMZ 901a branch.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/thermodesulfobium_acidiphilum_medium.yaml` so SL-10, Wolin's vitamin solution 10x, and neutralized sulfide solution remain nested stock additions with 1 ml, 1 ml, and 15 ml source amounts.
- Prevent stock components from being promoted to direct final-medium rows unless they are explicitly diluted or modeled as expanded contributions.
- Canonicalize the direct DSMZ 901a and TOGO M3119 branches before merge generation.

## Follow-up Checks

- Regenerate merged YAML and verify DSMZ 901a no longer has top-level 2.5 g/L HCl, undiluted vitamin rows, or a 30 g/L sulfide row.
- Confirm the corrected DSMZ 901a record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `mediadive.medium:901a` and `DSMZ_Medium901a.pdf` to ensure DSMZ 901a has one generated output.

## Additional Notes

None found.

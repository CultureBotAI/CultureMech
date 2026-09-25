# YAML Record Review: Sucrose-Asparagine Medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/sucrose_asparagine_medium.yaml
- Started UTC: 2026-09-25T07:39:42Z
- Finished UTC: 2026-09-25T07:39:42Z
- Verdict: needs curation

## Target
Reviewed generated record `CultureMech:001222` / `sucrose_asparagine_medium` from `data/merge_yaml/merged/sucrose_asparagine_medium.yaml`.

The generated record has one source, direct MediaDive/DSMZ medium 1749.

## Validation
- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed for 1 file with 0 total error rows.
- Reference validation: Passed for 1 file with 0 link checks and all validations passing.
- Term validation: Passed.
- Embedded curation history validation: Not checked; the standalone history validator does not target `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding
The record identity is preserved: the generated YAML cites `mediadive.medium:1749`, links to `DSMZ_Medium1749.pdf`, and carries pH 7.0 from the DSMZ source.

The exact local search found one normalized DSMZ source, one generated merged record, and the expected indexes for `CultureMech:001222` / `mediadive.medium:1749`.

## Evidence
DSMZ medium 1749 is prepared from two solutions. `Mineral Salts Solution with Asparagin (L)` has 0.5 g MgSO4 x 7 H2O, 1.0 g K2HPO4, 2.0 g L-Asparagin, and tap water to 990.0 ml, then is adjusted to pH 7.0 and autoclaved. DSMZ notes that 15.0 g/L agar may be added to solidify the medium.

`Sucrose Solution (10 mL)` contains 20 g sucrose and is autoclaved separately. After autoclaving, the source adds the full 10 ml sucrose solution to the 990 ml mineral-salts solution for a final volume of 1 L.

MediaDive has the same topology: a 1000 ml main solution assembled from 990 ml of solution 3613 and 10 ml of solution 3614.

## Completeness
The generated record preserves pH and the three DSMZ preparation steps, but the concentrations are on mixed bases. The mineral-salt rows come from a 990 ml stock basis, giving MgSO4 x 7 H2O 0.50505 g/L, K2HPO4 1.0101 g/L, L-Asparagin 2.0202 g/L, and agar 15.1515 g/L, when the final 1 L medium should contain 0.5, 1.0, 2.0, and 15.0 g/L after the sucrose stock is added.

The sucrose row is far more severe: 20 g in the 10 ml sucrose stock was converted to 2000 g/L and then exposed as the final concentration. The final medium receives the full 20 g stock in a final 1 L volume, so the final sucrose concentration should be 20 g/L.

The `Tap water` row is another stock-volume artifact: the 990 ml make-up volume should not appear as 990 `G_PER_L`.

## Findings
- The 10 ml sucrose stock concentration was flattened as 2000 g/L instead of the final 20 g/L.
- Mineral-salt and optional agar rows were left on their 990 ml pre-addition denominator instead of the final 1000 ml denominator.
- The tap-water make-up volume was exposed as a mass concentration.
- The recipe needs to retain the two-solution topology or compute all flattened rows after combining 990 ml mineral salts plus 10 ml sucrose stock.

## Recommended Edits
- Fix `data/normalized_yaml/bacterial/sucrose_asparagine_medium.yaml` or the MediaDive import logic, then regenerate `data/merge_yaml/merged/sucrose_asparagine_medium.yaml`; do not hand-edit the generated merged YAML.
- Preserve `Mineral Salts Solution with Asparagin (L)` and `Sucrose Solution (10 mL)` as structured solutions with addition volumes, or flatten to the final 1 L concentrations.
- Represent sucrose as 20 g/L in the final medium if the stock is flattened.
- Represent agar as an optional 15 g/L solidifying addition rather than leaving the 15 g/990 ml concentration.

## Follow-up Checks
- Confirm the regenerated record has sucrose at 20 g/L, not 2000 g/L.
- Confirm MgSO4 x 7 H2O, K2HPO4, and L-Asparagin use 0.5, 1.0, and 2.0 g/L final concentrations.
- Confirm the 990 ml tap-water row is removed from final ingredients or changed to volume metadata.
- Re-run schema, strict, reference, and term validators on the regenerated merged YAML.

## Additional Notes
The exact local search for `mediadive.medium:1749`, `CultureMech:001222`, and `sucrose_asparagine_medium` included ignored and hidden files under `data/normalized_yaml` and `data/merge_yaml/merged`.

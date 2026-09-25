# YAML Record Review: methanosarcina_sp_medium_n2_co2_for_dsm_2834

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanosarcina_sp_medium_n2_co2_for_dsm_2834.yaml
- Started UTC: 2026-09-24T05:04:34Z
- Finished UTC: 2026-09-24T05:04:34Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:009174` for TOGO medium `M2606`, "Methanosarcina SP. Medium (N2/CO2) (for DSM 2834)", derived from DSMZ Medium 141c.

## Validation

- LinkML open schema validation: Passed with "No issues found".
- Strict recipe validation: Passed; `/private/tmp/methanosarcina_sp_medium_n2_co2_for_dsm_2834.strict.tsv` contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

- The TOGO identifier, label, and DSMZ 141c source URL are preserved.
- The recipe is intended to represent the DSM 2834 variant of DSMZ 141c, where trimethylammonium chloride is replaced with 10 ml/l 50% methanol and the completed medium is adjusted to pH 6.8-7.2.
- The generated formula is not source-faithful because the Modified Wolin mineral stock and Wolin vitamin stock are present both as `solutions` stubs and as parent `ingredients`, with duplicate sums and unit conversion errors.
- The generated YAML has no `ph_range`, `ph_value`, or `preparation_steps` top-level keys; an exact `rg --no-ignore --hidden` check against this record returned no matches for those keys.

## Evidence

- DSMZ 141c defines a 1013 ml parent recipe with 1000 ml distilled water, 10 ml Modified Wolin mineral solution, 2 ml 0.1% Fe(NH4)2(SO4)2 x 6 H2O stock, 0.5 ml 0.1% sodium resazurin stock, 1 ml Wolin's vitamin solution (10x), and gram-scale salts and complex components.
- The DSM 2834 variant in the DSMZ PDF replaces trimethylammonium chloride with 10 ml/l of 50% methanol from a sterile anoxic stock and sets the complete-medium pH to 6.8-7.2.
- MediaDive solution 241 and the DSMZ PDF agree that Modified Wolin's mineral solution is a separate 1 L stock; MediaDive solution 242 is a separate 1 L Wolin vitamin stock.
- The generated `Distilled water` row is `3000.0 G_PER_L` with duplicate notes showing that it merged three 1000 ml water rows from the main medium, mineral stock, and vitamin stock.

## Completeness

- Most parent medium rows are present, including the DSM 2834 methanol replacement.
- The stock-solution boundaries are absent from the main ingredient list, despite placeholder `solutions` stubs for the two named Wolin stocks.
- pH, anaerobic sparging, Hungate or serum-vial dispensing, separate sterile anoxic stock preparation, filtration, and post-autoclave addition instructions are absent.

## Findings

1. Major - Stock solution components are flattened into the parent ingredient list at stock strength. `MgSO4 x 7 H2O`, `NaCl`, and `CaCl2 x 2 H2O` show duplicate sums such as `3.45 + 3.0`, `18.0 + 1.0`, and `0.14 + 0.1`, proving that Modified Wolin mineral stock components were added to the main liter instead of being nested under the 10 ml stock addition.
2. Major - Solvents from incompatible scopes were merged. The main medium, Modified Wolin mineral stock, and Wolin vitamin stock each contain 1000 ml distilled water, but the generated record has one parent `Distilled water` ingredient at `3000.0 G_PER_L`.
3. Major - Several ml and mg source amounts became `G_PER_L`. The parent 0.5 ml sodium-resazurin stock, 2 ml ferrous-ammonium-sulfate stock, and 5 ml methanol rows are grams per liter in the generated YAML; vitamin and trace rows such as 2 mg biotin, 0.3 mg selenite, and 0.4 mg tungstate likewise appear as gram-per-liter ingredient concentrations.
4. Major - The two named `solutions` stubs have corrupted addition units and no composition. The source adds 10 ml Modified Wolin mineral stock and an equivalent Wolin vitamin stock volume, while the generated `solutions` entries say `10 G_PER_L` and only point to external MediaDive YAML names.
5. Major - Source preparation and pH requirements were dropped. The record omits DSMZ instructions to make the base anoxic with 80% N2 and 20% CO2, add bicarbonate before the first pH adjustment, autoclave under the gas phase, add trimethylammonium or methanol, cysteine, sulfide, and vitamins from separately sterilized anoxic stocks, and adjust the DSM 2834 complete medium to pH 6.8-7.2.
6. Minor - Some surviving ingredient metadata remains suspect even after validation: `MgSO4 x 7 H2O` has a primary CHEBI heptahydrate term but a generic magnesium sulfate `mediaingredientmech_chebi_term`, and `AIK(SO4)2 x 12 H2O` uses `I` where the source is aluminum potassium sulfate, `AlK(SO4)2 x 12 H2O`.

## Recommended Edits

- Recurate this normalized TOGO record with separate parent, Modified Wolin mineral stock, and Wolin vitamin stock scopes.
- Keep the parent additions as source volumes, including 10 ml mineral stock, 2 ml ferrous-ammonium-sulfate stock, 0.5 ml sodium-resazurin stock, and the DSM 2834 methanol stock replacement.
- Preserve each stock solution's own 1 L water row separately from the parent 1000 ml water row.
- Restore the DSM 2834 pH 6.8-7.2 range and the anaerobic sparging, autoclaving, stock sterilization, filtration, and post-autoclave addition instructions.
- Correct the stale or mistyped ingredient grounding after the formula scopes are repaired.

## Follow-up Checks

- Re-run focused schema, strict, reference, and term validators on the regenerated merged YAML.
- Confirm that regenerated parent salts no longer include Modified Wolin mineral stock addends.
- Confirm that mg and ml source rows preserve their source units or are converted using explicit, solution-aware dilution math.

## Additional Notes

The live MediaDive solution records are useful corroboration for the two stock formulas, but the source of record for this TOGO entry is the DSMZ 141c PDF and its DSM 2834 variant text.

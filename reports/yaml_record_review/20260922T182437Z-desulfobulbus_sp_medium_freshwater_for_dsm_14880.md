# YAML Record Review: desulfobulbus_sp_medium_freshwater_for_dsm_14880

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfobulbus_sp_medium_freshwater_for_dsm_14880.yaml`
- Started UTC: 2026-09-22T18:24:37Z
- Finished UTC: 2026-09-22T18:24:37Z
- Verdict: needs curation

## Target

Generated bacterial `desulfobulbus_sp_medium_freshwater_for_dsm_14880` record for TOGO Medium M2529, sourced from DSMZ Medium 194 for DSM 14880.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is correctly grounded to TOGO Medium M2529, `Desulfobulbus SP. Medium (Freshwater) (For DSM 14880)`, whose original URL is DSMZ Medium 194.

An exact ignored-file search found the same TOGO source plus a KOMODO `for_dsm_14880` strain-variant record that is used by the `DESULFOVIRGA_MEDIUM` merge. This generated record has only the TOGO import in `merged_from`.

The complex/undefined classification is supported by yeast extract in the DSM 14880-specific substrate replacement.

## Evidence

TOGO M2529 describes a final mixture of Solution A 921.5 ml, Solution B 1 ml, Solution C 30 ml, Solution D 10 ml, Solution E 10 ml, and Solution F 10 ml.

Solution A contains 0.5 ml 0.1% Na-resazurin, 920 ml water, basal salts, 1 ml Selenite-tungstate solution, and N2/CO2 handling. Solution B is Trace element solution SL-10. Solution C is the NaHCO3 stock. Solution D carries the DSM 14880 yeast-extract and sodium-pyruvate replacement. Solution E is Wolin's vitamin solution. Solution F is the sulfide reducing solution.

The generated `solutions` array preserves those addition names only as stubs with `G_PER_L` values equal to source addition volumes: Solution A is `921.5`, Solution B is `1`, Solution C is `30`, Solution D is `10`, Solution E is `10`, Solution F is `10`, Selenite-tungstate solution is `1`, Trace element solution SL-10 is `1`, and Wolin's vitamin solution is `10`.

Stock and sub-solution contents were flattened into the top-level ingredient list. Source milligram values became gram-per-liter values, including 3 mg Na2SeO3 as `3`, 4 mg Na2WO4 as `4`, 36 mg Na2MoO4 as `36`, 70 mg ZnCl2 as `70`, 2 mg Biotin as `2`, 5 mg Thiamine-HCl as `5`, and 10 mg Pyridoxine-HCl as `10`.

Water rows from independent stocks were summed into 4950 G_PER_L distilled water, and N2/CO2 atmospheres were modeled as variable-concentration ingredients.

## Completeness

The generated record has no `preparation_steps`.

TOGO M2529 carries preparation comments for sparging Solution A with 80% N2 / 20% CO2 to pH below 6, autoclaving Solution A under the same gas atmosphere, autoclaving Solutions B, D, and F under 100% N2, autoclaving Solution C under 80% N2 / 20% CO2, preparing and filter-sterilizing Solution E under 100% N2, adding Solutions B through F to cooled sterile Solution A in sequence, setting final pH to 7.1-7.4, optional sodium dithionite stimulation, 5-10% inoculum, and the DSM 14880 Na-propionate replacement.

The top-level record also lacks the source pH 7.1-7.4.

## Findings

- Major issue: final-medium Solution A-F additions are represented as `G_PER_L` stubs instead of milliliter solution additions.
- Major issue: SL-10, selenite-tungstate, NaHCO3, DSM 14880 substrate, Wolin vitamin, and sulfide stock contents are flattened into top-level ingredients.
- Major issue: many source milligram quantities are inflated by three orders of magnitude through mg-to-G_PER_L flattening.
- Major issue: water from multiple independent stocks is summed into one 4950 G_PER_L top-level ingredient.
- Major issue: all source preparation, final-pH, optional dithionite, inoculation, and DSM 14880-specific substitution instructions were dropped.
- Minor issue: N2 and CO2 atmospheres are modeled as variable-concentration ingredients rather than atmosphere metadata.

## Recommended Edits

- Rebuild the normalized TOGO M2529 record with a top-level 921.5/1/30/10/10/10 ml mixture of Solution A through Solution F.
- Nest SL-10, selenite-tungstate, NaHCO3, DSM 14880 yeast-extract/pyruvate, Wolin vitamin, and sulfide formulas under `solutions` and keep their water rows local to those stocks.
- Convert milligram source quantities to grams per liter only inside their stock formulas, and compute final concentrations from stock addition volumes if final top-level concentrations are required.
- Restore the 7.1-7.4 pH range and the ordered anaerobic/autoclave/filter-sterilization preparation comments.
- Move N2 and CO2 gas rows into structured atmosphere or preparation metadata.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after restructuring the record.
- Confirm `high_metal: true` disappears once SL-10 and selenite-tungstate source milligram quantities are not inflated.
- Confirm yeast extract and sodium pyruvate remain scoped to the DSM 14880 replacement and do not merge into the base DSMZ 194 propionate variant.
- Compare the repaired TOGO M2529 record against KOMODO `for_dsm_14880` before any later deduplication.

## Additional Notes

TOGO M2529 and MediaDive REST medium 194 were reachable during review. The live MediaDive 194 REST endpoint describes the base DSMZ 194 medium rather than the DSM 14880-specific TOGO variant, but it corroborates the same nested-solution style and shared stock formulas.

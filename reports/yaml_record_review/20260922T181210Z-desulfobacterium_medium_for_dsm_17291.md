# YAML Record Review: desulfobacterium_medium_for_dsm_17291

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfobacterium_medium_for_dsm_17291.yaml`
- Started UTC: 2026-09-22T18:12:10Z
- Finished UTC: 2026-09-22T18:12:10Z
- Verdict: needs curation

## Target

Generated bacterial `desulfobacterium_medium_for_dsm_17291` record for TOGO Medium M2547, sourced from DSMZ Medium 383 for DSM 17291.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is correctly grounded to TOGO Medium M2547, `Desulfobacterium Medium (For DSM 17291)`, whose original URL is DSMZ Medium 383.

An exact ignored-file search found the same TOGO source as `data/normalized_yaml/bacterial/desulfobacterium_medium_for_dsm_17291.yaml` and a related KOMODO strain-variant record at `data/normalized_yaml/bacterial/for_dsm_17291.yaml`; this generated record has only the TOGO import in `merged_from`.

The complex/undefined classification is supported because the DSM 17291 variant uses Casamino acids in Solution D.

## Evidence

TOGO M2547 describes a final mixture of Solution A 961.5 ml, Solution B 1 ml, Solution C 20 ml, Solution D 20 ml, Solution E 10 ml, and Solution F 10 ml.

Solution A contains 0.5 ml 0.1% Na-resazurin, 960 ml water, basal salts, 1 ml Selenite-tungstate solution, and N2/CO2 sparging. Solution B is Trace element solution SL-10. Solution C is the carbonate solution. Solution D is a Casamino acids substrate solution. Solution E is Wolin's vitamin solution. Solution F is the sulfide reducing solution.

The generated `solutions` array preserves those addition names only as stubs with `G_PER_L` values equal to the source addition volumes: Solution A is `961.5`, Solution B is `1`, Solution C is `20`, Solution D is `20`, Solution E is `10`, Solution F is `10`, and Selenite-tungstate solution is `1`.

Most stock contents were flattened into the top-level ingredient list, with source mg quantities promoted to gram-per-liter values. Examples include 3 mg Na2SeO3 as `3` G_PER_L, 4 mg Na2WO4 as `4` G_PER_L, 36 mg Na2MoO4 as `36` G_PER_L, 70 mg ZnCl2 as `70` G_PER_L, and Wolin vitamin mg rows such as 2 mg Biotin, 5 mg Thiamine-HCl, and 10 mg Pyridoxine-HCl as 2, 5, and 10 G_PER_L.

Water rows from multiple separate solutions were merged into a top-level 3040 G_PER_L distilled-water row, and gas atmospheres were modeled as variable-concentration ingredients.

## Completeness

The generated record has no `preparation_steps`.

TOGO M2547 carries several preparation comments that were dropped: Solution A sparging with 80% N2 / 20% CO2 to pH below 6 before anoxic autoclaving, ordered addition of sterile Solutions B through F, Solution B and F autoclaving under 100% N2, Solution C autoclaving under 80% N2 / 20% CO2, Solution D and E preparation under 100% N2 followed by filter sterilization, final pH 7.0-7.2, optional sodium dithionite stimulation, 5-10% inoculum, and dark incubation.

The top-level record also lacks the source pH 7.0-7.2.

## Findings

- Major issue: final-medium Solution A-F additions are represented as `G_PER_L` stubs instead of milliliter solution additions.
- Major issue: SL-10, selenite-tungstate, carbonate, Casamino acids, Wolin vitamin, and sulfide stock contents are flattened as final-medium ingredients.
- Major issue: many source milligram quantities are inflated by three orders of magnitude through mg-to-G_PER_L flattening.
- Major issue: water from multiple independent stocks is summed into one 3040 G_PER_L top-level ingredient, while `Distilled water 960.00` remains a separate ungrounded row.
- Major issue: all source preparation and final-pH instructions were dropped.
- Minor issue: N2 and CO2 atmospheres are modeled as variable-concentration ingredients rather than atmosphere metadata.

## Recommended Edits

- Rebuild the normalized TOGO M2547 record with a top-level 961.5/1/20/20/10/10 ml mixture of Solution A through Solution F.
- Nest SL-10, selenite-tungstate, carbonate, Casamino acids, Wolin vitamin, and sulfide formulas under `solutions` and keep their water rows local to those stocks.
- Convert milligram source quantities to grams per liter only inside their stock formulas, and then compute final concentrations from the stock addition volumes if final top-level concentrations are required.
- Restore the 7.0-7.2 pH range and the ordered anaerobic/autoclave/filter-sterilization preparation comments.
- Move N2 and CO2 gas rows into structured atmosphere or preparation metadata.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after restructuring the record.
- Confirm `high_metal: true` disappears once SL-10 and selenite-tungstate source milligram quantities are not inflated.
- Confirm the final medium still totals approximately 1.0225 L after Solutions A-F are combined.
- Compare the repaired TOGO M2547 record against the KOMODO `for_dsm_17291` record before any later deduplication.

## Additional Notes

TOGO M2547 and MediaDive REST medium 383 were reachable during review. The live MediaDive 383 REST endpoint describes the base DSMZ 383 medium rather than the DSM 17291-specific TOGO variant, but it corroborates the same nested-solution structure and shared stock formulas.

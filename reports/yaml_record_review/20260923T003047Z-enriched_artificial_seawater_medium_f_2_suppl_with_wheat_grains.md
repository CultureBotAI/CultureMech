# YAML Record Review: Enriched Artificial Seawater Medium f/2 suppl. with Wheat Grains

- Repository: CultureMech
- Record: data/merge_yaml/merged/enriched_artificial_seawater_medium_f_2_suppl_with_wheat_grains.yaml
- Started UTC: 2026-09-23T00:26:32Z
- Finished UTC: 2026-09-23T00:30:47Z
- Verdict: needs curation

## Target

`data/merge_yaml/merged/enriched_artificial_seawater_medium_f_2_suppl_with_wheat_grains.yaml` is the generated merge for DSMZ Medium 1723a, Enriched Artificial Seawater Medium f/2 supplemented with Wheat Grains. The maintained owner is `data/normalized_yaml/bacterial/enriched_artificial_seawater_medium_f_2_suppl_with_wheat_grains.yaml`.

The generated file was merged from one DSMZ/MediaDive parent on 2026-08-06. It predates the owner-side 2026-08-07 `apply_cocktail_nesting.py` pass and therefore lacks the partial `solutions:` repair now present in the maintained normalized YAML.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/enriched_1723a.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The record identity and `mediadive.medium:1723a` media term match DSMZ Medium 1723a.

The mapped small-molecule salts and vitamins point to reasonable CHEBI records for the named hydrate or vitamin. `Artificial Sea Salt` and `Wheat Grains` are mixtures rather than single molecules and are not grounded to CHEBI, which is appropriate for this source.

## Evidence

DSMZ 1723a prepares a liter of artificial seawater using 12.4 g/l artificial sea salt, then adds:

- 1 ml/l of 75 g/l NaNO3 stock.
- 1 ml/l of 5 g/l NaH2PO4 x H2O stock.
- 1 ml/l of `f/2 Trace Metal Mix`.
- 1 ml/l of filter-sterilized `Vitamin 3 Mix` after autoclaving and cooling.
- One sterilized wheat grain per 20 ml T25 flask, used as a carbon source for ambient bacteria from the sampling site.

The `f/2 Trace Metal Mix` and `Vitamin 3 Mix` formulas are inherited from DSMZ 1723. They are multi-stage stocks; their primary Fe/EDTA rows are gram-per-liter working-stock rows, and their Mn, Zn, Co, Cu, Mo, thiamine, biotin, and vitamin B12 rows are milliliter additions from primary stock solutions.

## Completeness

The artificial seawater, computed nitrate, computed phosphate, and wheat-grain support are represented. However, the trace-metal and vitamin stock hierarchy is required to reconstruct this medium correctly and was flattened in the generated merge.

No target organisms are imported for this medium. That is not a source mismatch in this file because the DSMZ 1723a recipe is generic and the MediaDive import did not supply a strain list.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Major | `f/2 Trace Metal Mix` was flattened into final-medium ingredients at working-stock or raw milliliter-addition values. | DSMZ adds 1 ml/l of the trace-metal mix; the generated file lists EDTA, Fe, Mn, Zn, Co, Cu, and Mo salts as top-level `G_PER_L` ingredients, including rows such as `45 G_PER_L` MnCl2 x 4 H2O that came from a 45 ml/l addition to the trace mix. | Keep a nested `f/2 Trace Metal Mix` at 1 ml/l and model its primary stocks or computed working-stock concentrations inside that solution. |
| Major | `Vitamin 3 Mix` was flattened into final-medium ingredients at working-stock volume numbers. | DSMZ adds 1 ml/l of the vitamin mix after autoclaving; the generated file lists thiamine HCl, D-biotin, and vitamin B12 as final-medium `G_PER_L` rows, with `0.1 G_PER_L` for biotin and `0.25 G_PER_L` for B12 copied from ml additions into the 100 ml vitamin stock. | Keep a nested `Vitamin 3 Mix` at 1 ml/l and represent its primary stock concentrations inside the solution. |
| Major | The generated merge is stale relative to the maintained owner. | The owner has a 2026-08-07 `apply_cocktail_nesting.py` entry and nested trace-metal plus vitamin solutions; this generated merge was emitted on 2026-08-06 and still has no `solutions:` block. | Repair the owner-side stock models, then regenerate `data/merge_yaml/merged/enriched_artificial_seawater_medium_f_2_suppl_with_wheat_grains.yaml`. |
| Minor | The artificial sea salt ingredient lost its product attribute. | DSMZ and MediaDive specify `hw Marinemix 21010`; the generated YAML keeps only the conductivity and salinity note. | Preserve the product attribute in an ingredient or preparation note if the schema supports it. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/enriched_artificial_seawater_medium_f_2_suppl_with_wheat_grains.yaml`, keep `NaNO3` at `0.075 G_PER_L` and `NaH2PO4 x H2O` at `0.005 G_PER_L`; those rows already reflect DSMZ final concentrations.
2. Expand and correct the nested `f/2 Trace Metal Mix` and `Vitamin 3 Mix` solutions using the DSMZ 1723a/1723 source formula.
3. Correct the shared `mediadive_5854_f_2_Trace_Metal_Mix.yaml` and `mediadive_5855_Vitamin_3_Mix.yaml` solution records so their ml additions are no longer rendered as `PERCENT_V_V` or stock-volume placeholders.
4. Regenerate the generated merge and confirm it retains the wheat-grain preparation text plus two 1 ml/l solutions.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merge.
- Confirm no f/2 trace-metal or vitamin stock components appear as final-medium top-level ingredients.
- Confirm the regenerated record still has a variable or trace wheat-grain row and carries the T25 flask wheat-grain cultivation note.

## Additional Notes

The exact source-owner search used ignored-file-inclusive matching where uniqueness mattered. It found only `data/normalized_yaml/bacterial/enriched_artificial_seawater_medium_f_2_suppl_with_wheat_grains.yaml` for the wheat-grains stem.

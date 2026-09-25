# YAML Record Review: Enriched Artificial Seawater Medium f/2 supplemented with 50 g/l NaCl

- Repository: CultureMech
- Record: data/merge_yaml/merged/enriched_artificial_seawater_medium_f_2_suppl_with_50_g_l_nacl.yaml
- Started UTC: 2026-09-23T00:20:38Z
- Finished UTC: 2026-09-23T00:26:19Z
- Verdict: needs curation

## Target

`data/merge_yaml/merged/enriched_artificial_seawater_medium_f_2_suppl_with_50_g_l_nacl.yaml` is the merged record for DSMZ Medium 1750, Enriched Artificial Seawater Medium f/2 supplemented with 50 g/l NaCl. The maintained source is `data/normalized_yaml/bacterial/enriched_artificial_seawater_medium_f_2_suppl_with_50_g_l_nacl.yaml`.

The generated file was emitted on 2026-08-06 from a single MediaDive/DSMZ parent and is stale relative to its normalized owner. The maintained owner gained an `apply_cocktail_nesting.py` repair on 2026-08-07 that moved five stock-strength rows into `f/2 Trace Metal Mix` and `Vitamin 3 Mix`; the generated merge still has no `solutions:` section.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/enriched_1750.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The record identity, `mediadive.medium:1750` media term, DSMZ PDF note, and imported Villanova et al. Algal Research DOI all match DSMZ Medium 1750.

Most small molecules are acceptably grounded to the named salt or vitamin hydrate in the generated file. `Artificial Sea Salt` is a commercial mixture and is intentionally ungrounded to CHEBI. The generated YAML retains the DSMZ conductivity note but drops the MediaDive/DSMZ attribute naming `hw Marinemix 21010` as the artificial sea salt product, so the salt mix is less precise than the source.

## Evidence

The DSMZ PDF and MediaDive REST payload agree on the stock design:

- Artificial seawater supplemented with 50 g/l NaCl is prepared from 12.4 g artificial sea salt and 50 g NaCl in 1000 ml.
- The final medium receives 1 ml of a 75 g/l NaNO3 stock and 1 ml of a 5 g/l NaH2PO4 x H2O stock per liter.
- The final medium receives 1 ml/l `f/2 Trace Metal Working Stock Solution`.
- `f/2 Trace Metal Working Stock Solution` is a 1000 ml stock containing 4.16 g Na2-EDTA x 2 H2O, 3.15 g FeCl3 x 6 H2O, and ml-scale additions from primary MnCl2, ZnSO4, CoCl2, CuSO4, and Na2MoO4 stocks.
- The final medium receives 1 ml/l filter-sterilized vitamin working stock after autoclaving and cooling.
- The vitamin working stock is a 100 ml stock made from primary thiamine-HCl, d-biotin, and cyanocobalamin stocks.

## Completeness

The generated record is not complete enough to reconstruct DSMZ 1750 because most stock boundaries and stock-addition volumes were lost.

No target organisms or growth conditions are present in the source import, and the DSMZ recipe itself is a formula rather than a strain-specific growth assertion, so their absence is not a record-level defect.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Major | NaNO3 and NaH2PO4 x H2O were converted from milliliter stock additions to 1 g/l final-medium ingredients. | DSMZ adds 1 ml/l of a 75 g/l NaNO3 stock and 1 ml/l of a 5 g/l NaH2PO4 x H2O stock; the generated YAML records both as `1 G_PER_L`. | Model the two additions as stocks or convert them to final concentrations of approximately 0.075 g/l and 0.005 g/l. |
| Major | `f/2 Trace Metal Mix` was flattened into final-medium ingredients at stock strength or at raw milliliter volumes. | DSMZ adds 1 ml/l of the 1000 ml trace-metal working stock; the generated YAML lists Na2-EDTA, FeCl3, MnCl2, ZnSO4, CoCl2, CuSO4, and Na2MoO4 as top-level gram-per-liter final ingredients, including `45 G_PER_L` MnCl2 from a 45 ml stock addition. | Keep a 1 ml/l nested `f/2 Trace Metal Mix` solution and represent its primary stocks or computed working-stock concentrations inside the solution. |
| Major | `Vitamin 3 Mix` was flattened into final-medium ingredients at stock volume numbers. | DSMZ adds 1 ml/l of a 100 ml vitamin working stock assembled from 1.0 ml, 0.1 ml, and 0.25 ml primary stock additions; the generated YAML lists thiamine HCl, D-biotin, and vitamin B12 as top-level `G_PER_L` rows. | Keep a 1 ml/l nested vitamin working stock and represent thiamine, biotin, and vitamin B12 inside it using the primary stock concentrations from DSMZ. |
| Major | The generated merge predates the normalized owner repair and has no `solutions:` block. | `data/normalized_yaml/bacterial/enriched_artificial_seawater_medium_f_2_suppl_with_50_g_l_nacl.yaml` has a 2026-08-07 `apply_cocktail_nesting.py` entry and nested `f/2 Trace Metal Mix` plus `Vitamin 3 Mix`; the generated merge was created on 2026-08-06 and still carries the stock rows under `ingredients`. | Repair the normalized owner, then regenerate `data/merge_yaml/merged/enriched_artificial_seawater_medium_f_2_suppl_with_50_g_l_nacl.yaml`. |
| Minor | The artificial sea salt product attribute was not retained. | MediaDive records `hw Marinemix 21010` as the artificial sea salt attribute; the generated YAML keeps only the conductivity/salinity note. | Preserve the product attribute in ingredient notes or preparation notes if supported. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/enriched_artificial_seawater_medium_f_2_suppl_with_50_g_l_nacl.yaml`, replace the imported `1 G_PER_L` nitrate and phosphate rows with explicit 1 ml/l additions from 75 g/l and 5 g/l stocks, or with computed final concentrations.
2. Keep `f/2 Trace Metal Mix` and `Vitamin 3 Mix` as `ML_PER_L` solutions, and expand their contents from DSMZ 1750 rather than raw MediaDive volume numbers.
3. Correct the standalone `mediadive_5854_f_2_Trace_Metal_Mix.yaml` and `mediadive_5855_Vitamin_3_Mix.yaml` solution records; they still contain volume additions rendered as `PERCENT_V_V` and incomplete source-derived concentrations.
4. Regenerate the merged YAML after normalized stock modeling is complete.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm the regenerated merge has exactly two top-level `ML_PER_L` solutions at 1 ml/l each.
- Confirm no trace-metal or vitamin stock constituents remain as final-medium `G_PER_L` ingredients.
- Spot-check the regenerated final concentrations for nitrate, phosphate, Mn, Zn, Co, Cu, Mo, thiamine, biotin, and vitamin B12 against the two-stage DSMZ recipe.

## Additional Notes

The exact source-owner search used ignored-file-inclusive matching where absence or uniqueness mattered. It found the expected DSMZ 1750 normalized owner plus neighboring f/2 records, and did not reveal another maintained copy for this exact medium.

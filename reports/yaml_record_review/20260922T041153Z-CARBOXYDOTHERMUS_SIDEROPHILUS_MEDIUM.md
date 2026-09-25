# YAML Record Review: CARBOXYDOTHERMUS SIDEROPHILUS MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml`
- Started UTC: 2026-09-22T04:05:40Z
- Finished UTC: 2026-09-22T04:11:53Z
- Verdict: needs curation

## Target

`CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml` is the generated `MediaRecipe` for `CultureMech:001640`, `carboxydothermus_siderophilus_medium`, sourced from DSMZ/MediaDive medium 507a.

The generated recipe was merged on fingerprint `f77092bd388630ed75b83acc7353575a62e19aa38a938753c9bc5394bc784c1b` from nine normalized files:

- `KOMODO_507_CARBOXYDOTHERMUS_medium`
- `carboxydothermus_siderophilus_medium`
- `for_dsm_12326`
- `for_dsm_18923`
- `for_dsm_21278`
- `for_dsm_21830`
- `for_dsm_23698`
- `medium_507_modified_for_dsm_7242`
- `pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521`

The canonical source owner is `data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml`, and the generated record points to `data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml` as a `SOURCE_DUPLICATE` parent.

## Validation

- LinkML validation against `MediaRecipe`: pass.
- `scripts/validate_strict.py`: pass with 0 strict errors.
- `linkml-reference-validator`: pass; 1 file checked, 0 reference checks.
- `linkml-term-validator`: pass.
- Embedded `curation_history`: not checked; the available `just validate-history` target validates standalone files under `history/`, not embedded history events inside merged YAML.

## Identity and Grounding

The canonical identity is internally self-consistent for DSMZ/MediaDive 507a: the record name, original name, source term `mediadive.medium:507a`, pH 6.9, and `CARBOXYDOTHERMUS SIDEROPHILUS MEDIUM` label all point to the DSMZ 507a recipe.

The duplicate merge with KOMODO 507 is not evidence-backed. The maintained KOMODO parent was rewritten by `repair_komodo_507_carboxydothermus_score10.py` to have the exact 27-row ingredient signature used by DSMZ 507a, which in turn made the generated merger collapse DSMZ 507a together with KOMODO 507 and seven KOMODO strain wrappers. The live KOMODO 507 page links to DSMZ Medium 507, not DSMZ Medium 507a, and lists the base Carboxydothermus formula with `Na2S x 9 H2O`, resazurin, CO2, N2, CO, and NaOH rows rather than the `Na2-9,10-anthraquinone-2,6-disulfonate` 507a formula. The DSMZ Medium 507 PDF confirms that 507 is a different recipe with SL-11, 0.1% resazurin, neutralized sulfide, 2 bar CO overpressure, and DSM strain-specific variants, whereas 507a uses SL-4, anthraquinone disulfonate, no sulfide, and 1 bar CO overpressure.

Most small-molecule groundings are present and match hydrated salts correctly, but there are still term-level defects:

- `Na2-9,10-anthraquinone-2,6-disulfonate` has no primary `term`, even though the source solution import maps MediaDive compound 521 to `CHEBI:85112`.
- `NiCl2 x 6 H2O` is grounded to `CHEBI:34887`/nickel dichloride rather than the hexahydrate.
- `Calcium D-(+)-pantothenate` has a primary `CHEBI:31345` term but still lacks the corresponding `mediaingredientmech_chebi_term`.

The `bacterial`, `COMPLEX`, `UNDEFINED`, and `LIQUID` classifications are plausible for this source.

## Evidence

The DSMZ 507a PDF and the MediaDive 507a JSON agree on three nested source recipes:

- a 1011 ml main solution containing KCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, NH4Cl, KH2PO4, 8.25 g `Na2-9,10-anthraquinone-2,6-disulfonate`, 10 ml Trace element solution SL-4, 1 g NaHCO3, 0.2 g yeast extract, 1 ml Wolin's vitamin solution (10x), and 1000 ml distilled water;
- a 1000 ml Trace element solution SL-4 stock;
- a 1000 ml Wolin's vitamin solution (10x) stock.

The generated direct ingredient list flattens the SL-4 and Wolin stock rows at their undiluted stock strengths. For example, DSMZ 507a adds 10 ml of SL-4 to 1011 ml final medium, so 0.5 g/L Na2-EDTA in the stock becomes roughly 0.0049456 g/L in the final medium; the generated record instead publishes `0.5 G_PER_L`. DSMZ 507a adds 1 ml of Wolin's vitamin solution to 1011 ml final medium, so 20 mg/L biotin in the stock becomes roughly 0.0000197824 g/L in the final medium; the generated record instead publishes `0.02 G_PER_L`.

The generated record also drops the explicit solution-addition rows for Trace element solution SL-4 and Wolin's vitamin solution (10x). The generated `preparation_steps` preserve stock-preparation text but there is no `solutions` block or direct solution ingredient tying that text back to a 10 ml or 1 ml addition.

## Completeness

The record has no `target_organisms`, no strain-specific growth rows, no structured atmosphere or pressure condition for the 1 bar sterile carbon monoxide overpressure, and no representation of the anoxic N2 and N2/CO2 stock-gassing conditions beyond free text.

The main 1000 ml distilled water row is not represented in the final generated recipe. The standalone `mediadive_1113_Main_sol_507a.yaml` owner imported that water as `989.1196834817014 PERCENT_V_V`, which is a source-volume normalization artifact rather than a percent v/v concentration.

## Findings

- Needs curation: DSMZ/MediaDive 507a has been falsely merged with KOMODO 507 and seven KOMODO 507 child records. KOMODO 507 and DSMZ 507 point to the base Carboxydothermus sulfide/resazurin medium, not to the DSMZ 507a anthraquinone Carboxydothermus siderophilus medium.
- Needs curation: the imported 507a recipe flattens Trace element solution SL-4 and Wolin's vitamin solution (10x) as if their one-liter stock concentrations were final grams per liter.
- Needs curation: the generated merge omits solution-addition rows for 10 ml/L-equivalent SL-4 and 1 ml/L-equivalent Wolin's vitamin solution and leaves the stock-preparation text detached from modeled solution records.
- Needs curation: the generated record has no 1000 ml water row for the main solution, and the maintained `Main sol. 507a` solution represents that water as a nonsensical `PERCENT_V_V` value.
- Minor: `Na2-9,10-anthraquinone-2,6-disulfonate` lost the `CHEBI:85112` grounding already available in the imported MediaDive solution.
- Minor: `NiCl2 x 6 H2O` is grounded to the anhydrous chloride term.
- Minor: calcium pantothenate lacks its `mediaingredientmech_chebi_term` mirror.

## Recommended Edits

- Undo the September `repair_komodo_507_carboxydothermus_score10.py` rewrite that forced KOMODO 507 and its child records to the DSMZ 507a ingredient signature.
- Rebuild `KOMODO_507_CARBOXYDOTHERMUS_medium.yaml` and its child records from the live KOMODO 507 / DSMZ 507 source formula, keeping DSMZ 507a out of that duplicate set.
- Keep `carboxydothermus_siderophilus_medium.yaml` as a standalone DSMZ/MediaDive 507a recipe unless a true duplicate source with the same recipe is identified.
- Model DSMZ 507a with a main recipe plus solution additions instead of stock-expanded undiluted ingredient rows, or compute final concentrations from the 10/1011 and 1/1011 dilution factors before flattening.
- Restore the 1000 ml distilled-water basis without using `PERCENT_V_V` for a raw 989.119 ml normalized water amount.
- Ground `Na2-9,10-anthraquinone-2,6-disulfonate`, correct the nickel hexahydrate CHEBI mapping, and add the missing calcium pantothenate `mediaingredientmech_chebi_term`.
- Add source-backed target organism and growth evidence for `Carboxydothermus siderophilus` if available.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml` after repairing the normalized owners and verify that its `merged_from` list no longer contains KOMODO Medium 507 records.
- Compare the regenerated 507a direct final concentrations, if flattened, against `https://mediadive.dsmz.de/download/composition/507a/json`.
- Compare the repaired KOMODO 507 normalized records against the live KOMODO Medium 507 table and the DSMZ Medium 507 PDF before re-running `merge_recipes.py`.
- Run the open LinkML, strict, reference, and term validators after the stock/variant repairs.

## Additional Notes

Generated `data/merge_yaml/merged` files are derived. Apply fixes to `data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml`, `data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml`, the affected KOMODO 507 child YAML files, the 507a solution import, or the merge/import logic before regenerating this output.

# YAML Record Review: CARCBOXYDIBRACHIUM MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml`
- Started UTC: 2026-09-22T04:16:00Z
- Finished UTC: 2026-09-22T04:19:30Z
- Verdict: needs curation

## Target

`CARCBOXYDIBRACHIUM_MEDIUM.yaml` is the generated single-source `MediaRecipe` for `CultureMech:002069`, `carcboxydibrachium_medium`, sourced from DSMZ/MediaDive medium 902.

The generated record was merged only from `data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml` on fingerprint `38083464429a9afe27ba2bffd93a9810358fb6cab13a70e51ebb03e9e8b82b0c`.

## Validation

- LinkML validation against `MediaRecipe`: pass.
- `scripts/validate_strict.py`: pass with 0 strict errors.
- `linkml-reference-validator`: pass; 1 file checked, 0 reference checks.
- `linkml-term-validator`: pass.
- Embedded `curation_history`: not checked; the available `just validate-history` target validates standalone files under `history/`, not embedded history events inside merged YAML.

## Identity and Grounding

The generated identity matches the DSMZ/MediaDive 902 source, including the `CARCBOXYDIBRACHIUM` spelling used by DSMZ and MediaDive. Category `bacterial`, `COMPLEX`, `UNDEFINED`, `LIQUID`, and pH 7.0 agree with the imported source metadata.

The first thirteen direct ingredients are the MediaDive main-solution concentrations normalized from 1002 ml. Most of their groundings are present, but `Na2SiO3` lost the `CHEBI:60720` sodium silicate grounding already present on the `Main sol. 902` solution owner, and `Sodium resazurin` has `CHEBI:8806` as a primary term without a `mediaingredientmech_chebi_term` mirror.

The generated rows after `Na2S x 9 H2O` are not final recipe ingredients. They are undiluted components of Trace element solution SL-10 and Wolin's vitamin solution (10x) after the import flattened stock recipes into the parent medium.

## Evidence

MediaDive medium 902 represents three nested recipes:

- a 1002 ml main solution with 1000 ml distilled water, basal salts, yeast extract, 1 ml Trace element solution SL-10, 0.5 ml 0.1% sodium resazurin, bicarbonate, pyruvate, 1 ml Wolin's vitamin solution (10x), L-cysteine, and sulfide;
- a 1000 ml Trace element solution SL-10 stock containing 10 ml 25% HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 990 ml distilled water;
- a 1000 ml Wolin's vitamin solution (10x) stock.

The generated record stores the nine SL-10 components at their one-liter stock concentrations. For example, 1.5 g/L FeCl2 x 4 H2O in a stock added at 1 ml per 1002 ml contributes roughly 0.001497 g/L to the final medium, not `1.5 G_PER_L`.

The generated record also stores the ten Wolin vitamin components at their one-liter stock concentrations. Biotin should be diluted by 1/1002 from a 0.02 g/L stock, not left as `0.02 G_PER_L` in the final medium.

## Completeness

The record preserves DSMZ/MediaDive's anoxic Hungate-vessel preparation in free text, including N2 sparging, separate anoxic pyruvate/vitamin/cysteine/sulfide/bicarbonate stocks, vitamin filtration, an 80% N2 / 20% CO2 bicarbonate stock atmosphere, and final pH adjustment.

No structured solution-addition rows remain for the 1 ml SL-10 or 1 ml Wolin stock additions, and the main 1000 ml water basis is absent from the generated direct ingredient list. The source `mediadive_1855_Main_sol_902.yaml`, `mediadive_595_Trace_element_solution_SL-10.yaml`, and `mediadive_5980_Wolin_s_vitamin_solution_10x.yaml` solution records also encode raw water volumes as `PERCENT_V_V`, which should not be propagated into a fixed formula.

No target organisms or strain-level growth evidence are present.

## Findings

- Needs curation: Trace element solution SL-10 was flattened into final ingredients at undiluted stock concentrations instead of being kept as a 1 ml stock addition or diluted by 1/1002.
- Needs curation: Wolin's vitamin solution (10x) was flattened into final ingredients at undiluted stock concentrations instead of being kept as a 1 ml stock addition or diluted by 1/1002.
- Needs curation: the main recipe water row and both solution-addition rows were dropped, leaving the preparation text to mention sterile stocks without modeled stock links.
- Minor: `Na2SiO3` is ungrounded in the generated recipe despite a `CHEBI:60720` grounding in the imported MediaDive main solution.
- Minor: `NiCl2 x 6 H2O` is grounded to anhydrous `CHEBI:34887` instead of a nickel chloride hexahydrate term.
- Minor: `Sodium resazurin` and `Calcium D-(+)-pantothenate` have primary CHEBI terms but no `mediaingredientmech_chebi_term` mirrors.
- Minor: no source-backed target organism or growth evidence has been curated.

## Recommended Edits

- Rebuild DSMZ/MediaDive 902 with explicit 1 ml/L-equivalent `Trace element solution SL-10` and `Wolin's vitamin solution (10x)` additions, or compute final direct concentrations for all stock components from the 1002 ml source volume.
- Preserve the main 1000 ml distilled-water basis without converting raw source milliliters to `PERCENT_V_V`.
- Propagate the MediaDive `Na2SiO3` sodium silicate grounding into the generated recipe.
- Correct the nickel hexahydrate grounding and add missing CHEBI mirrors for sodium resazurin and calcium pantothenate.
- Add organism-level evidence if growth of a strain on DSMZ 902 is documented.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml` after repairing `data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml`.
- Compare any flattened final concentrations against MediaDive's medium 902 composition endpoint rather than against one-liter stock recipe values.
- Run the LinkML, strict, reference, and term validators after the stock repair.

## Additional Notes

Generated `data/merge_yaml/merged` files are derived. Apply fixes to the normalized DSMZ/MediaDive 902 owner or to MediaDive solution-import logic before regenerating this output.

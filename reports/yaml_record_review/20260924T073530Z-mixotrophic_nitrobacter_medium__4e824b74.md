# YAML Record Review: mixotrophic_nitrobacter_medium__4e824b74

- Repository: CultureMech
- Record: data/merge_yaml/merged/mixotrophic_nitrobacter_medium__4e824b74.yaml
- Started UTC: 2026-09-24T07:35:30Z
- Finished UTC: 2026-09-24T07:36:00Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:008933`
- Generated name: `mixotrophic_nitrobacter_medium`
- Generated source file: `data/merge_yaml/merged/mixotrophic_nitrobacter_medium__4e824b74.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/TOGO_M2349_Mixotrophic_Nitrobacter_Medium.yaml`
- Declared upstream source: TOGO Medium `M2349`, `Mixotrophic Nitrobacter Medium`
- Backing source: DSMZ/MediaDive medium `756a`, `MIXOTROPHIC NITROBACTER MEDIUM`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/mixotrophic_nitrobacter_medium__4e824b74.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated `media_term` points to `TOGO:M2349`; the generated source note cites DSMZ Medium 756a.
- The exact `CultureMech:008933` owner is `data/normalized_yaml/bacterial/TOGO_M2349_Mixotrophic_Nitrobacter_Medium.yaml`.
- The same source formulation also exists as MediaDive/DSMZ record `CultureMech:001889` at `data/normalized_yaml/bacterial/mixotrophic_nitrobacter_medium.yaml`.
- Ammonium molybdate has a primary CHEBI term but lacks a `mediaingredientmech_chebi_term`.
- `MgSO4 x 7 H2O` has a primary heptahydrate term but its `mediaingredientmech_chebi_term` still points to generic magnesium sulfate.

## Evidence

- TOGO `M2349` returned an empty body during review, so the DSMZ formula was checked through MediaDive REST for medium `756a`.
- MediaDive `756a` defines `Main sol. 756a` with 1.5 g yeast extract, 1.5 g peptone, 0.55 g `Na-pyruvate`, 1 ml trace element solution `1545`, 100 ml stock solution `1544`, 2 g `NaNO2`, and 899 ml distilled water.
- MediaDive trace solution `1545` contains stock concentrations of 33.8 mg/L `MnSO4 x H2O`, 49.4 mg/L `H3BO3`, 43.1 mg/L `ZnSO4 x 7 H2O`, 37.1 mg/L `(NH4)6Mo7O24`, 97.3 mg/L `FeSO4 x 7 H2O`, 25 mg/L `CuSO4 x 5 H2O`, and 1 liter of water.
- MediaDive stock solution `1544` contains 0.07 g/L `CaCO3`, 5 g/L NaCl, 0.5 g/L `MgSO4 x 7 H2O`, 1.5 g/L `KH2PO4`, and 1 liter of water.
- The generated `mediadive.solution:6127` link resolves to an unrelated stock solution containing `NaNO3`, `Na2HPO4`, and `K2HPO4`.
- The generated `mediadive.solution:6187` link resolves to the unrelated EDTA/chloride trace solution already seen in another record, not DSMZ solution `1545`.

## Completeness

- The generated top-level water row is `2899.0 G_PER_L`, which sums 899 ml of main-solution water plus 1000 ml water from each stock.
- Trace-solution milligram amounts were imported as gram-per-liter amounts, giving 1000-fold stock concentration errors before accounting for the 1 ml/L final-medium dilution.
- The stock solution added at 100 ml/L was flattened without representing its 10-fold dilution into the final medium.
- The generated `solutions` array points to the wrong MediaDive solutions and does not preserve DSMZ solution IDs `1545` and `1544`.
- The source pH 7.4 adjustment is degraded to a top-level variable `NaOH` row; the source permits NaOH or KOH as the pH adjuster.

## Findings

- High: Both DSMZ stock subrecipes were flattened into top-level ingredients, losing the 1 ml/L and 100 ml/L dilution factors.
- High: Six trace-element stock rows preserve milligram numeric amounts but report them as `G_PER_L`.
- High: The generated `solutions` placeholders are linked to unrelated MediaDive solutions `6187` and `6127` instead of DSMZ `1545` and `1544`.
- High: The top-level water concentration sums water from all three source solutions into `2899.0 G_PER_L`.
- Medium: pH 7.4 adjustment with NaOH or KOH was converted to a required variable `NaOH` ingredient.
- Medium: This TOGO M2349 record duplicates the curated MediaDive/DSMZ 756a record under the same normalized name.
- Low: The magnesium sulfate heptahydrate row has inconsistent primary and MediaIngredientMech CHEBI keys.

## Recommended Edits

- De-duplicate TOGO `M2349` and MediaDive/DSMZ `756a`, preserving both source IDs or source URLs on the surviving record.
- Keep yeast extract, peptone, sodium pyruvate, sodium nitrite, and 899 ml water in the main solution.
- Represent DSMZ trace solution `1545` as a 1 ml/L stock addition, not as direct top-level stock concentrations.
- Represent DSMZ stock solution `1544` as a 100 ml/L stock addition, converting ingredient quantities if the schema requires final-medium concentrations.
- Remove the incorrect `mediadive.solution:6187` and `mediadive.solution:6127` links.
- Represent the pH 7.4 NaOH-or-KOH adjustment as preparation or pH metadata rather than a single variable NaOH nutrient.

## Follow-up Checks

- Re-fetch MediaDive medium `756a` and verify all stock additions and dilution factors are represented.
- Re-run the TOGO M2349 API check before editing in case its empty-body response was transient.
- Confirm only one Mixotrophic Nitrobacter Medium variant with the 1.5/1.5/0.55 g/L organic concentrations remains after de-duplication.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.
- The normalized-owner and duplicate-source lookups used `rg --no-ignore --hidden`; repeat ignored-file-inclusive checks for exact owner and duplicate source paths after the edit.

## Additional Notes

- None found.

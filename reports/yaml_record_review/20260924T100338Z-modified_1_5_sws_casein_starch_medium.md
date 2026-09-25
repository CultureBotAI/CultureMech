# YAML Record Review: Modified 1/5 SWS-Casein Starch Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_1_5_sws_casein_starch_medium.yaml
- Started UTC: 2026-09-24T10:03:38Z
- Finished UTC: 2026-09-24T10:03:38Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_1_5_sws_casein_starch_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:008383` |
| Name | `modified_1_5_sws_casein_starch_medium` |
| Original name | `Modified 1/5 SWS-Casein Starch Medium` |
| Category | `bacterial` |
| Medium source | TOGO `M1812`; original source NBRC `NBRC_M1042` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_1_5_sws_casein_starch_medium.yaml` |
| Generated status | Stale generated merge output from one normalized TOGO record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_1_5_sws_casein_starch_medium.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_1_5_sws_casein_starch_medium.yaml --out /private/tmp/modified_1_5_sws_casein_starch_medium.strict.tsv --workers 1 --quiet` | Passed; `/private/tmp/modified_1_5_sws_casein_starch_medium.strict.tsv` contained only the header line, so no strict errors were reported. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_1_5_sws_casein_starch_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_1_5_sws_casein_starch_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent: `CultureMech:008383`, `TOGO:M1812`, and `NBRC_M1042` all identify Modified 1/5 SWS-Casein Starch Medium.

The generated record is stale for the duplicate-water repair. Its generated water row is `2.0 G_PER_L` with notes showing two flattened `1.0` rows were summed; the normalized owner now has a 2026-09-02 repair event that collapsed that sum back to `1.0`.

The trace-stock identity is not coherent. The record links `Trace element solution*` to `mediadive.solution:6187`, but local `mediadive.solution:6187` is a different trace element solution containing EDTA, FeCl3 x 6H2O, MnCl2 x 4H2O, ZnCl2 x 6H2O, CoCl2 x 6H2O, and Na2MoO4 x 2H2O. NBRC M1042 has a recipe-local stock with Na2MoO4 x 2H2O, MnCl2 x 4H2O, ZnCl2, KI, CuSO4, CoCl2, SnCl2 x 2H2O, LiCl, Fe(III)-EDTA, and water.

## Evidence

TOGO `M1812` and the live NBRC `NO=1042` page support the same stock-based formula:

| Source claim | Record representation | Review |
| --- | --- | --- |
| Main medium uses 1 L distilled water with gram-scale MgSO4 x 7H2O, yeast extract, NaCl, CaCl2 x 2H2O, ferric citrate, HEPES, starch, casein sodium, Bacto Agar, and milligram-scale H3BO3, NaHCO3, KBr, SrCl2, and beta-glycerophosphate-2Na. | Gram rows are mostly correct, but every milligram-scale base additive is represented as the same numeric value in `G_PER_L`; water is `2.0 G_PER_L` in the generated record. | Unsupported units for the source milligram quantities and source final-volume water. |
| Add 0.2 ml Trace element solution to the main medium. | `Trace element solution*` is a `0.2 G_PER_L` solution stub linked to `mediadive.solution:6187`. | Unsupported unit and wrong stock identity. |
| The Trace element solution stock contains 1 L water plus 10 mg Na2MoO4 x 2H2O, 100 mg MnCl2 x 4H2O, 20 mg ZnCl2, 20 mg KI, 10 mg CuSO4, 20 mg CoCl2, 5 mg SnCl2 x 2H2O, 5 mg LiCl, and 8 g Fe(III)-EDTA. | Those nine stock compounds are flattened to top-level `G_PER_L` ingredients in the final medium. | Unsupported stock dilution: trace stock concentrations are not final-medium concentrations. |
| Cyanocobalamin is added after autoclaving as 1 ml of a filter-sterilized 50 mg/100 ml stock. | `Cyanocobalamin**` is an empty solution stub with `0.5 G_PER_L`. | Unsupported unit and missing post-autoclave stock context. |
| The medium is pH 7.2; the trace stock is sterilized by filtration. | No pH or preparation steps are represented. | Incomplete. |

## Completeness

The generated record has all visible NBRC ingredient labels, but several are attached to the wrong compartment or unit. The core issue is not missing row names; it is loss of the recipe-local trace stock, the cyanocobalamin post-autoclave stock, milligram units, and pH/preparation notes.

The generated record is stale relative to the normalized owner's 2026-09-02 duplicate-water repair, but the normalized owner still needs a source-aware fix: the two source water rows belong to different compartments and should not be flattened together before duplicate handling.

Empty target-organism fields were not treated as defects. NBRC M1042 is a medium formulation page, not a growth-evidence page.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Source milligram amounts were promoted to gram-per-liter concentrations. | NBRC lists H3BO3 4 mg, NaHCO3 30 mg, KBr 16 mg, SrCl2 6 mg, beta-glycerophosphate-2Na 2 mg, and multiple trace-stock salts in mg; the generated record stores each numeric value as `G_PER_L`. | `data/normalized_yaml/bacterial/modified_1_5_sws_casein_starch_medium.yaml`; TOGO unit normalization. |
| major | The recipe-local trace stock is flattened and linked to the wrong MediaDive solution. | NBRC says to add 0.2 ml of its own Trace element solution; the record stores 0.2 `G_PER_L`, flattens that stock into top-level rows, and links `mediadive.solution:6187`, whose composition does not match the NBRC trace stock. | `data/normalized_yaml/bacterial/modified_1_5_sws_casein_starch_medium.yaml`; generic solution-name mapping and stock migration. |
| major | Cyanocobalamin post-autoclave handling is lost. | NBRC says to add 1 ml of a filter-sterilized 50 mg/100 ml stock after autoclaving; the record has an empty `Cyanocobalamin**` solution with `0.5 G_PER_L`. | `data/normalized_yaml/bacterial/modified_1_5_sws_casein_starch_medium.yaml`; footnote and stock parsing. |
| major | Distinct water rows from the main medium and trace stock were flattened and merged. | NBRC has 1 L water in the main medium and 1 L water inside the Trace element solution; the generated record has a single `2.0 G_PER_L` water row from duplicate summing. | `data/normalized_yaml/bacterial/modified_1_5_sws_casein_starch_medium.yaml`; duplicate cleanup must preserve compartment boundaries. |
| major | pH 7.2 and filtration/autoclave preparation details are absent. | TOGO carries `ph: 7.2`, the NBRC table displays pH 7.2, the trace stock says to sterilize by filtration, and the cyanocobalamin footnote says it is added after autoclaving. None of those procedural details appear in the record. | `data/normalized_yaml/bacterial/modified_1_5_sws_casein_starch_medium.yaml`; TOGO/NBRC comment import. |

## Recommended Edits

1. Re-curate `data/normalized_yaml/bacterial/modified_1_5_sws_casein_starch_medium.yaml` from NBRC M1042 so all milligram source quantities remain milligram quantities in the correct base medium or stock compartment.
2. Replace the generic `mediadive.solution:6187` link with a recipe-local Trace element solution matching NBRC M1042, and represent its addition as 0.2 ml.
3. Represent the cyanocobalamin footnote as a 1 ml post-autoclave addition from a 50 mg/100 ml filter-sterilized stock.
4. Preserve separate water rows for the main medium and the trace stock instead of flattening them into one duplicate-merged final ingredient.
5. Import pH 7.2 plus the filtration/autoclave preparation notes.
6. Regenerate `data/merge_yaml/merged/modified_1_5_sws_casein_starch_medium.yaml` after the normalized source preserves the recipe-local stocks.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/modified_1_5_sws_casein_starch_medium.yaml` and the regenerated merge output.
2. Manually compare the regenerated record against TOGO `M1812` and NBRC `NO=1042`, checking every mg/g/ml/L unit, the 0.2 ml trace-stock addition, the 1 ml cyanocobalamin addition, pH 7.2, and stock-level water rows.
3. Verify no `mediadive.solution` CURIE remains on the NBRC trace stock unless it is an exact composition match for NBRC M1042.

## Additional Notes

An exact gitignore-independent search for `mediadive.solution:6187` under `data/normalized_yaml` found that the generic solution is reused in many unrelated records; this review inspected `data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml` directly and found a non-matching composition for NBRC M1042.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.

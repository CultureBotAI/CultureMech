# YAML Record Review: Modified Biebl and Penning's Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_biebl_and_pennings_medium.yaml
- Started UTC: 2026-09-24T10:25:23Z
- Finished UTC: 2026-09-24T10:25:23Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_biebl_and_pennings_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:008745` |
| Name | `modified_biebl_and_pennings_medium` |
| Original name | `Modified Biebl and Penning's Medium` |
| Category | `bacterial` |
| Medium source | TOGO `M2150`, mirrored from NBRC `1504` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_biebl_and_pennings_medium.yaml` |
| Generated status | Generated copy of a flattened TOGO/NBRC normalized record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_biebl_and_pennings_medium.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_biebl_and_pennings_medium.yaml --out /private/tmp/modified_biebl_and_pennings_medium.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_biebl_and_pennings_medium.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_biebl_and_pennings_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_biebl_and_pennings_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent at the medium level: `CultureMech:008745`, `TOGO:M2150`, the label, and the NBRC source URL identify NBRC Medium 1504, Modified Biebl and Penning's Medium.

An exact `find data/normalized_yaml -name modified_biebl_and_pennings_medium.yaml` search, which covers ignored files, found one maintained owner at `data/normalized_yaml/bacterial/modified_biebl_and_pennings_medium.yaml`. Exact ignored-inclusive `find` checks also found `data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml` and `data/normalized_yaml/bacterial/mediadive_2739_Trace_element_solution_SL7.yaml`, which are the two MediaDive solutions referenced by generated solution stubs.

The generated stock-solution grounding is not coherent. NBRC 1504 defines its Vitamin solution inline with nine vitamin rows and 1 L distilled water, while `mediadive.solution:6241` contains only three vitamin compounds. NBRC 1504 also defines Trace element solution SL7 inline with 10 ml 25% HCl and 990 ml water; `mediadive.solution:2739` is similar in name but has 1 ml HCl and 1000 ml water.

## Evidence

The TOGO `M2150` API and the live NBRC 1504 page agree on the formulation and pH.

| Source claim | Record representation | Review |
| --- | --- | --- |
| The main solution contains KH2PO4, MgSO4 x 7 H2O, NaCl, NH4Cl, CaCl2 x 2 H2O, sodium pyruvate, yeast extract, peptone, 5 ml 0.1% Ferric citrate solution, 2 ml Vitamin solution, 1 ml Trace element solution SL7, and 1 L distilled water at pH 7. | The simple gram rows are present, but the three solution additions are represented as `5`, `2`, and `1 G_PER_L` solution stubs, the three compartment water rows are merged into one `992 G_PER_L` row, and no `ph_value` is present. | Partial; pH, water, and stock addition units are wrong. |
| The NBRC Vitamin solution is a 1 L stock with nine vitamin rows that is added at 2 ml/L. | Those nine vitamin rows are promoted to top-level final-medium ingredients, for example `Biotin` is `2 G_PER_L`. | Unsupported stock flattening. |
| The NBRC Trace element solution SL7 is a stock with HCl, FeCl2 x 4 H2O, seven trace salts, and 990 ml water that is added at 1 ml/L. | The trace rows are promoted to top-level final-medium ingredients at stock amounts, for example `Na2MoO4 x 2H2O` is `40 G_PER_L`. | Unsupported stock flattening. |
| NBRC instructs to autoclave all ingredients except vitamin solution under an N2 atmosphere and add filter-sterilized vitamin solution aseptically and anaerobically before inoculation. | The record has `N2` as a variable ingredient but no preparation steps. | Incomplete anaerobic and post-autoclave handling. |
| NBRC instructs to dissolve FeCl2 x 4 H2O in 25% HCl first when preparing Trace element solution SL7. | The record flattens both FeCl2 x 4 H2O and HCl as top-level ingredients and drops the stock-preparation order. | Incomplete stock-preparation handling. |
| The source specifies CoCl2 x 6 H2O and NiCl2 x 6 H2O. | Those rows are grounded to generic `cobalt dichloride` and `nickel dichloride`, respectively. | Hydrate-specific source labels are not preserved in grounding. |

## Completeness

The generated record is incomplete because its source formulation has three distinct stock additions, inline Vitamin and Trace element recipes, pH 7, an anaerobic N2 autoclaving instruction, a filter-sterilized post-autoclave vitamin addition, and trace-stock ordering instructions that are not carried in the structured record.

Empty target-organism and growth-evidence fields were not treated as defects. TOGO `M2150` and NBRC 1504 are medium formulation pages, not growth-evidence pages.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Three source stock additions are modeled with grams-per-liter units instead of milliliter addition volumes. | NBRC calls for 5 ml Ferric citrate solution, 2 ml Vitamin solution, and 1 ml Trace element solution SL7; the generated `solutions` entries store `5`, `2`, and `1 G_PER_L`. | `data/normalized_yaml/bacterial/modified_biebl_and_pennings_medium.yaml`; TOGO solution migration. |
| major | Vitamin and trace stock contents are flattened into the final medium. | NBRC puts the vitamin rows in a 1 L Vitamin solution and the trace rows in Trace element solution SL7; the generated record stores them as top-level ingredients at stock amounts. | `data/normalized_yaml/bacterial/modified_biebl_and_pennings_medium.yaml`; TOGO stock migration. |
| major | Water rows from three compartments were duplicate-merged. | The source has 1 L main water, 1 L Vitamin-solution water, and 990 ml Trace-solution water; the record has one `992 G_PER_L` water row with a note that three duplicates were merged. | `data/normalized_yaml/bacterial/modified_biebl_and_pennings_medium.yaml`; duplicate cleanup must preserve compartment boundaries. |
| major | The structured record omits pH 7 and preparation steps. | TOGO and NBRC carry pH 7 plus N2 autoclaving, anaerobic filter-sterilized vitamin addition, and trace-stock FeCl2/HCl ordering instructions; the record has no `ph_value` and no `preparation_steps`. | `data/normalized_yaml/bacterial/modified_biebl_and_pennings_medium.yaml`; TOGO comments import. |
| major | Solution cross-links point to near-miss MediaDive solutions. | `mediadive.solution:6241` is not the nine-component NBRC Vitamin solution, and `mediadive.solution:2739` differs from the NBRC SL7 recipe in HCl and water amounts. | `data/normalized_yaml/bacterial/modified_biebl_and_pennings_medium.yaml`; solution reference matching. |
| major | Hexahydrate trace salts are grounded to generic anhydrous salts. | Source labels `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` are grounded to `cobalt dichloride` and `nickel dichloride`. | `data/normalized_yaml/bacterial/modified_biebl_and_pennings_medium.yaml`; CHEBI grounding. |

## Recommended Edits

1. Re-curate the three solution additions in `data/normalized_yaml/bacterial/modified_biebl_and_pennings_medium.yaml` as 5 ml/L Ferric citrate solution, 2 ml/L Vitamin solution, and 1 ml/L Trace element solution SL7.
2. Move the NBRC inline Vitamin and Trace element components under their stock solutions and preserve main-solution, vitamin-stock, and trace-stock water rows separately.
3. Remove the `mediadive.solution:6241` and `mediadive.solution:2739` links from NBRC-owned solution stubs unless exact equivalence can be demonstrated.
4. Add pH 7 and the TOGO/NBRC preparation comments as structured steps, preserving N2 autoclaving, anaerobic filter-sterilized vitamin addition, and Trace element solution SL7 preparation order.
5. Re-ground `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` to hydrate-specific CHEBI terms or leave them ungrounded until exact hydrate terms are available.
6. Regenerate `data/merge_yaml/merged/modified_biebl_and_pennings_medium.yaml` after the normalized owner is corrected.

## Follow-up Checks

1. Run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/modified_biebl_and_pennings_medium.yaml`.
2. Regenerate `data/merge_yaml/merged/modified_biebl_and_pennings_medium.yaml` and re-run the same validators on the generated record.
3. Manually compare the regenerated output against TOGO `M2150` and NBRC Medium 1504, checking pH, 5/2/1 ml stock addition volumes, separated water rows, N2 autoclaving, filter-sterilized vitamin addition, and FeCl2/HCl ordering in Trace element solution SL7.
4. Verify that no NBRC inline stock solution is linked to a merely same-named MediaDive solution with a different recipe.

## Additional Notes

Both the TOGO API for `M2150` and the NBRC Medium 1504 page still resolve. The exact MediaDive solution records linked by the generated solution stubs were inspected and do not exactly match the NBRC inline stocks.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.

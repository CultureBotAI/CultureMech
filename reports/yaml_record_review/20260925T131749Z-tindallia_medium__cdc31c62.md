# YAML Record Review: tindallia_medium__cdc31c62

- Repository: CultureMech
- Record: `data/merge_yaml/merged/tindallia_medium__cdc31c62.yaml`
- Started UTC: 2026-09-25T13:17:49Z
- Finished UTC: 2026-09-25T13:17:49Z
- Verdict: needs curation

## Target

Reviewed generated merged YAML for DSMZ medium 1148, `TINDALLIA MEDIUM`.

The generated record is a single-source merge from `data/normalized_yaml/bacterial/tindallia_medium.yaml`.

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 errors; the TSV contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed; the only diagnostic was the known eutils/pkg_resources startup warning.
- Embedded curation history: Not checked; the available history validator targets standalone `history/` records, not `MediaRecipe.curation_history`.

## Identity and Grounding

The medium identity is grounded to DSMZ medium 1148 by `media_term.term.id: mediadive.medium:1148`, the DSMZ link in `notes`, and the normalized source recipe.

The DSMZ 1148 source lists the macronutrients per 1000 ml final medium, then instructs adding 1 ml of a 200 ml trace element stock and 2 ml of Wolin's vitamin solution from sterile stocks.

## Evidence

The generated macronutrient rows for NaCl, KCl, K2HPO4, MgCl2 x 6 H2O, NH4Cl, yeast extract, peptone, resazurin, NaHCO3, Na2CO3, and Na2S x 9 H2O are consistent with the DSMZ final amounts.

The trace element and vitamin rows after Na2S are stock-solution contents, not final liter concentrations. The source says the trace recipe is milligrams per 200 ml and that only 1 ml is added to the final medium; the source says the vitamin solution is prepared per 1000 ml and that only 2 ml is added to the final medium.

## Completeness

No target organisms are present; that empty optional field is not a defect in this formulation review.

The record flattens stock recipes into the parent `ingredients` list without dilution factors or subrecipe boundaries, so a consumer cannot reconstruct which concentrations are final and which belong to DSMZ component stocks.

## Findings

- Major issue: the trace element solution is represented at stock concentrations. For example, MnCl2 x 4 H2O is recorded as 3.6 g/L, the concentration of 720 mg in a 200 ml trace stock, but the DSMZ parent medium adds only 1 ml of that stock per 1000 ml.
- Major issue: Wolin's vitamin solution is represented at stock concentrations. Biotin is recorded as 0.002 g/L from the stock recipe rather than as the diluted contribution from 2 ml of stock per liter of parent medium.
- Major issue: `HCl (concentrated)`, a reagent used to make the trace stock, was imported as 5 g/L of final medium. The source gives 5 ml concentrated HCl per 200 ml trace stock and does not support a final free-HCl row at this concentration.
- Minor issue: the record lacks an explicit nested component model that preserves DSMZ "Trace element solution (mg per 200 ml)" and "Wolin's vitamin solution" as additions.

## Recommended Edits

- Move the trace and vitamin formulations into nested stock components or represent their parent-medium contributions with the 1 ml/L and 2 ml/L dilution factors applied.
- Remove `HCl` from the final parent ingredient list unless the trace stock is modeled as its own component recipe.
- Keep the directly supplied parent-medium salts, bicarbonate/carbonate, sulfide, yeast extract, peptone, resazurin, and pH range unchanged unless a newer DSMZ source contradicts them.

## Follow-up Checks

- Recompute final concentrations after preserving the source stock topology and verify that each trace and vitamin row is either clearly nested or properly diluted.
- Re-run schema, strict, reference, and term validation after editing the normalized source YAML and regenerating the merge.

## Additional Notes

The exact source search was limited to normalized and generated filenames for `tindallia_medium`. Ignored files were included for duplicate-report checks with `find`, and no pre-existing ignored report for this generated record was found.

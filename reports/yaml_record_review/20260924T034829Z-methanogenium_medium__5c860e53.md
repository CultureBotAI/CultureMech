# YAML Record Review: methanogenium_medium__5c860e53
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanogenium_medium__5c860e53.yaml
- Started UTC: 2026-09-24T03:46:38Z
- Finished UTC: 2026-09-24T03:48:29Z
- Verdict: needs curation

## Target
- ID: CultureMech:009165
- Name: methanogenium_medium
- Label: Methanogenium Medium
- Category: archaea
- Source: TOGO M2598, imported from ATCC Medium 1439
- Merge fingerprint: 5c860e53171112741f86505145921d336c6ebf42ca96e3ed233487d8d186fcd9
- Merged from: TOGO_M2598_Methanogenium_Medium
- Maintained owner: data/normalized_yaml/archaea/TOGO_M2598_Methanogenium_Medium.yaml

## Validation
- Open schema validation: Passed; no issues found.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; 0 reference checks, all passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The record identity matches TOGO M2598 and ATCC Medium 1439, Methanogenium Medium.
- An exhaustive hidden and ignored search for `TOGO:M2598`, `CultureMech:009165`, and `TOGO_M2598_Methanogenium_Medium` found one maintained normalized owner plus expected generated indexes and the merged output.
- Trypticase is incorrectly grounded to CHEBI:78018 `dodecylphosphocholine`.
- MgCl2 x 7H2O, CoCl2 x 6H2O, and NiCl2 x 6H2O are grounded to generic chloride salts rather than to the hydrated source forms.

## Evidence
- The ATCC source defines ATCC Medium 1439 with 10 ml Trace Elements and 10 ml Vitamin Solution added to the main liter-scale Methanogenium formula.
- ATCC prints the Vitamin Solution and Trace Element Solution SL-6 formulas as local subrecipes, each made with 1000 ml DI Water and each filter sterilized.
- TOGO M2598 preserves those local subrecipes under the same source record; their `reference_media_id` values point back to M2598 rather than to reusable MediaDive solution IDs.
- The YAML flattens all Vitamin Solution and Trace Elements children into top-level final-medium ingredients and keeps only empty `Unknown solution` stubs for the two 10 ml solution additions.
- The empty stubs are linked to `mediadive.solution:6183` and `mediadive.solution:6241`, but those global MediaDive solution records have compositions unrelated to ATCC Medium 1439's local Trace Elements and Vitamin Solution.
- Milligram source quantities were promoted to grams per liter: 2 mg Fe(NH4)2(SO4)2 x 7H2O, 1 mg Resazurin, and every vitamin-stock row are encoded as whole-number `G_PER_L` values.
- The ATCC notes about precipitate-sensitive addition order, separate mg/ml Fe(NH4)2(SO4)2, Resazurin, and Na2S x 9H2O stocks, N2-CO2 gassing, pH adjustment, autoclaving, and filter sterilizing both local stocks are absent from `preparation_steps`.

## Completeness
- The main medium, Vitamin Solution, and Trace Element Solution SL-6 rows are present in flattened form.
- The local 10 ml Vitamin Solution and 10 ml Trace Elements additions are absent structurally.
- The ATCC preparation notes are absent.
- Empty optional fields are acceptable, but these empty solution stubs stand in for required source subrecipes.

## Findings
- Major: `data/normalized_yaml/archaea/TOGO_M2598_Methanogenium_Medium.yaml` flattens the local ATCC Vitamin Solution and Trace Element Solution SL-6 stocks into final-medium ingredients instead of modeling 10 ml solution additions.
- Major: The local ATCC stocks are wrongly linked to `mediadive.solution:6183` and `mediadive.solution:6241`, which are unrelated global MediaDive solution records.
- Major: Source milligram quantities in the main formula and Vitamin Solution are encoded as grams per liter.
- Major: ATCC preparation instructions for addition order, separate mg/ml stocks, N2-CO2 gassing, pH adjustment, autoclaving, and filter sterilization are missing.
- Major: Trypticase is grounded to dodecylphosphocholine, which makes an undefined protein digest look like a defined phosphocholine compound.
- Minor: Several hydrated chloride ingredients need narrower grounding if suitable CHEBI terms are available.

## Recommended Edits
- Re-curate `data/normalized_yaml/archaea/TOGO_M2598_Methanogenium_Medium.yaml` from TOGO M2598 and the ATCC Medium 1439 PDF.
- Model Vitamin Solution and Trace Element Solution SL-6 as local subrecipes with 10 ml additions to the main medium.
- Remove `mediadive.solution:6183` and `mediadive.solution:6241` from this owner unless a source explicitly links ATCC 1439 to those global solutions.
- Keep Fe(NH4)2(SO4)2 x 7H2O, Resazurin, and vitamin quantities as source milligram amounts inside the correct scopes.
- Restore ATCC preparation steps, including precipitate-sensitive addition order, separate mg/ml stocks, N2-CO2 gassing, pH adjustment, autoclaving, and filter sterilization.
- Remove the CHEBI:78018 Trypticase grounding and re-ground hydrated chloride salts where suitable hydrate-specific terms exist.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanogenium_medium__5c860e53.yaml`.
- Confirm that local Vitamin Solution and Trace Element Solution SL-6 replace the empty `Unknown solution` stubs.
- Confirm that `mediadive.solution:6183` and `mediadive.solution:6241` are gone from this ATCC 1439 owner.
- Confirm that milligram source rows are not inflated to grams per liter.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- None found.

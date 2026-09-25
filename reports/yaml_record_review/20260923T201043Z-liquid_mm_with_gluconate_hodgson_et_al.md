# YAML Record Review: Liquid mm with gluconate; hodgson et al

- Repository: CultureMech
- Record: `data/merge_yaml/merged/liquid_mm_with_gluconate_hodgson_et_al.yaml`
- Started UTC: `2026-09-23T20:09:52Z`
- Finished UTC: `2026-09-23T20:10:43Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:007162`
- `name`: `liquid_mm_with_gluconate_hodgson_et_al`
- `original_name`: `Liquid mm with gluconate; hodgson et al`
- `category`: `bacterial`
- `medium_type`: `DEFINED`
- `composition_type`: `DEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `MEDIADB:263`
- `merge_fingerprint`: `e4ab200ef0793c99b848beabb59cde6aa6ce2c667b44661ad5cefd8f0d29c4e7`
- `merged_from`: `liquid_mm_with_gluconate_hodgson_et_al`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/liquid_mm_with_gluconate_hodgson_et_al.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:007162`, `MEDIADB:263`, `Medium ID: 263`, `liquid_mm_with_gluconate_hodgson_et_al`, and the merge fingerprint found one maintained owner, `data/normalized_yaml/bacterial/liquid_mm_with_gluconate_hodgson_et_al.yaml`, plus this generated record. No duplicate generated recipe or archived conflicting owner was found in the checked paths.
- The generated record merges exactly one owner on the recorded fingerprint and preserves the MediaDB medium ID.
- `D-Gluconic acid` is ungrounded in both the maintained owner and generated record even though MediaDB's tab-delimited Medium 263 row provides CHEBI `33198`.

## Evidence

- MediaDB Medium 263 is `Liquid mm with gluconate; hodgson et al`, is marked minimal, and exposes the same seven compounds in the generated recipe.
- MediaDB's tab-delimited compound view for Medium 263 confirms the imported concentrations: `L-Asparagine` 3.78444 mM, `D-Gluconic acid` 10.0 mM, `Ethylene glycol` 0.134257 mM, `Potassium hydroxide` 5.34706 mM, `Potassium dibasic phosphate` 2.87026 mM, `Magnesium sulfate` 0.811458 mM, and `Ferrous sulfate` 0.0359648 mM.
- The same tab-delimited MediaDB row for `D-Gluconic acid` carries KEGG `glcn`, PubChem `10690`, and CHEBI `33198`.
- MediaDB links Medium 263 to `Streptomyces coelicolor J802`, source `Hodgson et al, 1982`, and Growth Data 556.
- Growth Data 556 reports `Streptomyces coelicolor J802` on Medium 263, source `Hodgson et al, 1982`, growth rate `0.301 (1/h)`, no pH, no temperature, and additional notes of `doubling time`.
- MediaDB Source 90 lists the cited article as Hodgson 1982, `Journal Of General Microbiology`, title `Glucose repression of carbon source uptake and metabolism in streptomyces coelicolor a3(2) and its perturbation in mutants resistant to 2-deoxyglucose`.

## Completeness

- The generated ingredient list is complete for MediaDB Medium 263's seven compound rows and preserves MediaDB's mM values.
- The generated record has no structured target organism, growth-data, or source-citation object despite the organism, Growth Data 556, and Source 90 links that MediaDB exposes for this medium.
- The `D-Gluconic acid` ingredient is not CHEBI-grounded despite a source CHEBI ID.
- The three generated preparation steps are generic importer defaults and are not supported by the checked MediaDB medium, text, growth-data, or source pages.

## Findings

1. `D-Gluconic acid` is ungrounded despite source identifiers.
   - Evidence: MediaDB Medium 263's tab-delimited row lists `D-Gluconic acid`, KEGG `glcn`, PubChem `10690`, and CHEBI `33198`; both the maintained owner and generated record retain only the KEGG cross-reference in free text.
   - Impact: downstream CHEBI-based consumers see an avoidable ungrounded carbon-source ingredient.

2. MediaDB organism, growth, and citation links were imported only as loose notes/applications.
   - Evidence: MediaDB links Medium 263 to `Streptomyces coelicolor J802`, Growth Data 556, and Source 90; the generated record has no structured organism, growth-rate, source, or publication field for those facts.
   - Impact: record users cannot query the observed strain, the 0.301 1/h growth value, or the Hodgson 1982 citation from normalized fields.

3. Preparation steps are unsupported importer boilerplate.
   - Evidence: the generated recipe asserts distilled-water dissolve, pH adjustment, and 0.22 um filter sterilization steps; the checked MediaDB pages provide composition, organism, source, and growth metadata but no preparation method.
   - Impact: the generated record may imply pH adjustment and filter sterilization requirements that are absent from the indexed source.

## Recommended Edits

1. Ground `D-Gluconic acid` in `data/normalized_yaml/bacterial/liquid_mm_with_gluconate_hodgson_et_al.yaml` using the MediaDB row and an exact CHEBI term review.
2. Extend the MediaDB import/normalization path to retain structured organism, growth-data, and publication links for Medium 263 / Growth Data 556 / Source 90.
3. Remove the three generic preparation steps from MediaDB-derived records unless source-specific preparation evidence is available.
4. Rebuild `data/merge_yaml/merged/liquid_mm_with_gluconate_hodgson_et_al.yaml` after owner/import changes land.

## Follow-up Checks

- Re-run term validation after grounding `D-Gluconic acid`.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt generated record.
- Re-fetch MediaDB Medium 263 and Growth Data 556 if adding structured growth metadata so the organism and growth-rate fields are populated from the current source pages.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.

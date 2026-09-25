# YAML Record Review: Liquid mm with fructose; hodgson et al

- Repository: CultureMech
- Record: `data/merge_yaml/merged/liquid_mm_with_fructose_hodgson_et_al.yaml`
- Started UTC: `2026-09-23T20:07:52Z`
- Finished UTC: `2026-09-23T20:08:41Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:007160`
- `name`: `liquid_mm_with_fructose_hodgson_et_al`
- `original_name`: `Liquid mm with fructose; hodgson et al`
- `category`: `bacterial`
- `medium_type`: `DEFINED`
- `composition_type`: `DEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `MEDIADB:261`
- `merge_fingerprint`: `19dd4a48a854cb6132450edeff8c28e4e10da7e9c3733222d81a0ccb01132de5`
- `merged_from`: `liquid_mm_with_fructose_hodgson_et_al`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/liquid_mm_with_fructose_hodgson_et_al.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:007160`, `MEDIADB:261`, `Medium ID: 261`, `liquid_mm_with_fructose_hodgson_et_al`, and the merge fingerprint found one maintained owner, `data/normalized_yaml/bacterial/liquid_mm_with_fructose_hodgson_et_al.yaml`, plus this generated record. No duplicate generated recipe or archived conflicting owner was found in the checked paths.
- The generated record merges exactly one owner on the recorded fingerprint and preserves the MediaDB medium ID.
- All seven generated ingredients carry a `term` where the maintained owner carries one. No generated ingredient is less grounded than the maintained owner.

## Evidence

- MediaDB Medium 261 is `Liquid mm with fructose; hodgson et al`, is marked minimal, and exposes the same seven compounds in the generated recipe.
- MediaDB's tab-delimited compound view for Medium 261 confirms the imported concentrations: `D-Fructose` 50.0 mM, `L-Asparagine` 3.78444 mM, `Ethylene glycol` 0.134257 mM, `Potassium hydroxide` 5.34706 mM, `Potassium dibasic phosphate` 2.87026 mM, `Magnesium sulfate` 0.811458 mM, and `Ferrous sulfate` 0.0359648 mM.
- MediaDB links Medium 261 to `Streptomyces coelicolor J802`, source `Hodgson et al, 1982`, and Growth Data 554.
- Growth Data 554 reports `Streptomyces coelicolor J802` on Medium 261, source `Hodgson et al, 1982`, growth rate `0.025 (1/h)`, no pH, no temperature, and additional notes of `doubling time`.
- MediaDB Source 90 lists the cited article as Hodgson 1982, `Journal Of General Microbiology`, title `Glucose repression of carbon source uptake and metabolism in streptomyces coelicolor a3(2) and its perturbation in mutants resistant to 2-deoxyglucose`.

## Completeness

- The generated ingredient list is complete for MediaDB Medium 261's seven compound rows and preserves MediaDB's mM values.
- The generated record has no structured target organism, growth-data, or source-citation object despite the organism, Growth Data 554, and Source 90 links that MediaDB exposes for this medium.
- The three generated preparation steps are generic importer defaults and are not supported by the checked MediaDB medium, text, growth-data, or source pages.

## Findings

1. MediaDB organism, growth, and citation links were imported only as loose notes/applications.
   - Evidence: MediaDB links Medium 261 to `Streptomyces coelicolor J802`, Growth Data 554, and Source 90; the generated record has no structured organism, growth-rate, source, or publication field for those facts.
   - Impact: record users cannot query the observed strain, the 0.025 1/h growth value, or the Hodgson 1982 citation from normalized fields.

2. Preparation steps are unsupported importer boilerplate.
   - Evidence: the generated recipe asserts distilled-water dissolve, pH adjustment, and 0.22 um filter sterilization steps; the checked MediaDB pages provide composition, organism, source, and growth metadata but no preparation method.
   - Impact: the generated record may imply pH adjustment and filter sterilization requirements that are absent from the indexed source.

## Recommended Edits

1. Extend the MediaDB import/normalization path to retain structured organism, growth-data, and publication links for Medium 261 / Growth Data 554 / Source 90.
2. Remove the three generic preparation steps from MediaDB-derived records unless source-specific preparation evidence is available.
3. Rebuild `data/merge_yaml/merged/liquid_mm_with_fructose_hodgson_et_al.yaml` after import changes land.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Re-fetch MediaDB Medium 261 and Growth Data 554 if adding structured growth metadata so the organism and growth-rate fields are populated from the current source pages.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.

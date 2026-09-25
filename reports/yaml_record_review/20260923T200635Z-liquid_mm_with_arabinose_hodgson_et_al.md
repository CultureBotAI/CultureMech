# YAML Record Review: Liquid mm with arabinose; hodgson et al

- Repository: CultureMech
- Record: `data/merge_yaml/merged/liquid_mm_with_arabinose_hodgson_et_al.yaml`
- Started UTC: `2026-09-23T20:05:00Z`
- Finished UTC: `2026-09-23T20:06:35Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:007157`
- `name`: `liquid_mm_with_arabinose_hodgson_et_al`
- `original_name`: `Liquid mm with arabinose; hodgson et al`
- `category`: `bacterial`
- `medium_type`: `DEFINED`
- `composition_type`: `DEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `MEDIADB:259`
- `merge_fingerprint`: `973601f166fd335b230b6b1f2034446bb91cbe1d81de3323f5a96cb1480453a3`
- `merged_from`: `liquid_mm_with_arabinose_hodgson_et_al`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/liquid_mm_with_arabinose_hodgson_et_al.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:007157`, `MEDIADB:259`, `Medium ID: 259`, `liquid_mm_with_arabinose_hodgson_et_al`, and the merge fingerprint found one maintained owner, `data/normalized_yaml/bacterial/liquid_mm_with_arabinose_hodgson_et_al.yaml`, plus this generated record. No duplicate generated recipe or archived conflicting owner was found in the checked paths.
- The generated record merges exactly one owner on the recorded fingerprint and preserves the MediaDB medium ID.
- The generated record is stale relative to its maintained owner: the owner has a 2026-08-20 `apply_mim_groundings.py` event that grounded `L-Arabinose` to `CHEBI:30849`, but the generated recipe still leaves `L-Arabinose` without a `term`.

## Evidence

- MediaDB Medium 259 is `Liquid mm with arabinose; hodgson et al`, is marked minimal, and exposes the same seven compounds in the generated recipe.
- MediaDB's tab-delimited compound view for Medium 259 confirms the imported concentrations: `L-Asparagine` 3.78444 mM, `L-Arabinose` 10.0 mM, `Ethylene glycol` 0.134257 mM, `Potassium hydroxide` 5.34706 mM, `Potassium dibasic phosphate` 2.87026 mM, `Magnesium sulfate` 0.811458 mM, and `Ferrous sulfate` 0.0359648 mM.
- MediaDB links Medium 259 to `Streptomyces coelicolor J802`, source `Hodgson et al, 1982`, and Growth Data 552.
- Growth Data 552 reports `Streptomyces coelicolor J802` on Medium 259, source `Hodgson et al, 1982`, growth rate `0.178 (1/h)`, no pH, no temperature, and additional notes of `doubling time`.
- MediaDB Source 90 lists the cited article as Hodgson 1982, `Journal Of General Microbiology`, title `Glucose repression of carbon source uptake and metabolism in streptomyces coelicolor a3(2) and its perturbation in mutants resistant to 2-deoxyglucose`.

## Completeness

- The generated ingredient list is complete for MediaDB Medium 259's seven compound rows and preserves MediaDB's mM values.
- The generated record has no structured target organism, growth-data, or source-citation object despite the organism, Growth Data 552, and Source 90 links that MediaDB exposes for this medium.
- The generated `L-Arabinose` row is incompletely grounded relative to the maintained owner because the post-merge MIM grounding has not propagated into `data/merge_yaml/merged`.
- The three generated preparation steps are generic importer defaults and are not supported by the checked MediaDB medium, text, growth-data, or source pages.

## Findings

1. Generated snapshot is stale for `L-Arabinose` grounding.
   - Evidence: `data/normalized_yaml/bacterial/liquid_mm_with_arabinose_hodgson_et_al.yaml` records a 2026-08-20 MIM grounding event and has `term: CHEBI:30849` for `L-Arabinose`; `data/merge_yaml/merged/liquid_mm_with_arabinose_hodgson_et_al.yaml` lacks `term` for that same row.
   - Impact: downstream CHEBI-based consumers see an avoidable ungrounded carbon-source ingredient in the generated artifact.

2. MediaDB organism, growth, and citation links were imported only as loose notes/applications.
   - Evidence: MediaDB links Medium 259 to `Streptomyces coelicolor J802`, Growth Data 552, and Source 90; the generated record has no structured organism, growth-rate, source, or publication field for those facts.
   - Impact: record users cannot query the observed strain, the 0.178 1/h growth value, or the Hodgson 1982 citation from normalized fields.

3. Preparation steps are unsupported importer boilerplate.
   - Evidence: the generated recipe asserts distilled-water dissolve, pH adjustment, and 0.22 um filter sterilization steps; the checked MediaDB pages provide composition, organism, source, and growth metadata but no preparation method.
   - Impact: the generated record may imply pH adjustment and filter sterilization requirements that are absent from the indexed source.

## Recommended Edits

1. Rebuild `data/merge_yaml/merged/liquid_mm_with_arabinose_hodgson_et_al.yaml` from the current normalized owner so the 2026-08-20 `L-Arabinose` grounding propagates.
2. Extend the MediaDB import/normalization path to retain structured organism, growth-data, and publication links for Medium 259 / Growth Data 552 / Source 90.
3. Remove the three generic preparation steps from MediaDB-derived records unless source-specific preparation evidence is available.

## Follow-up Checks

- After rebuilding, confirm the generated `L-Arabinose` ingredient carries `CHEBI:30849`.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Re-fetch MediaDB Medium 259 and Growth Data 552 if adding structured growth metadata so the organism and growth-rate fields are populated from the current source pages.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.

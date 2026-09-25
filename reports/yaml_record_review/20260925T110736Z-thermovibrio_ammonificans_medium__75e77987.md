# YAML Record Review: thermovibrio_ammonificans_medium__75e77987

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermovibrio_ammonificans_medium__75e77987.yaml
- Started UTC: 2026-09-25T11:05:01Z
- Finished UTC: 2026-09-25T11:07:36Z
- Verdict: needs curation

## Target

- Generated YAML for JCM Medium J371, THERMOVIBRIO AMMONIFICANS MEDIUM, merged with JCM Medium J440, TB2 MEDIUM.
- The record was merged from `JCM_J371_THERMOVIBRIO_AMMONIFICANS_MEDIUM` and `tb2_medium`.
- The checked sources were MediaDive/JCM J371, MediaDive/JCM J440, and the corresponding JCM medium pages.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The base source record is correctly identified as MediaDive/JCM Medium J371.
- pH 5.5 and the JCM 371 H2/CO2 preparation step are retained.
- JCM J440 is TB2 MEDIUM, a variant of J371, but it was merged as `tb2_medium` under a source-duplicate relationship.

## Evidence

- MediaDive/JCM J371 defines Thermovibrio Ammonificans Medium as 750 ml water plus 250 ml Synthetic seawater (2 x), 10 ml Trace minerals, 6.15 g NaCl, 0.5 g KH2PO4, 0.375 g CaCl2 x 2 H2O, 10 mg ammonium sulfate, 0.025 mg KI, 0.1 mg Na2WO2 x 2 H2O, 2 mg NiCl2 x 6 H2O, 1 g KNO3, 5 g MES, 0.5 g Na2S x 9 H2O, and 1 mg resazurin.
- JCM 371 adjusts pH to 5.5, uses an H2/CO2 gas mixture, and adds separately sterilized KNO3 and MES before pressurizing inoculated bottles to 200 kPa H2/CO2.
- MediaDive/JCM J440 states that TB2 uses Medium 371 supplemented with 30 g/l final NaCl and an additional 4 ml/l neutralized 3% Na2S x 9 H2O solution before inoculation.

## Completeness

- The direct JCM 371 pH and preparation step are present.
- The generated record omits the explicit 750 ml water row.
- The 250 ml/l Synthetic seawater and 10 ml/l Trace minerals stocks are flattened as undiluted top-level stock rows.

## Findings

- The formula has blocking stock-solution flattening. NaCl is 62.48911 g/L because data-quality cleanup summed 6.08911 g/L normalized main NaCl with undiluted 55.4 g/L Synthetic seawater NaCl and undiluted 1 g/L Trace minerals NaCl.
- MgSO4 x 7 H2O, CaCl2 x 2 H2O, KI, H3BO3, and other seawater/trace salts were also expanded at whole-stock strength instead of being diluted from 250 ml/l Synthetic seawater and 10 ml/l Trace minerals.
- JCM J440/TB2 is not an exact source duplicate of JCM J371. It should be a variant with 30 g/l final NaCl and an extra 4 ml/l 3% Na2S x 9 H2O solution.

## Recommended Edits

- Regenerate JCM 371 with Synthetic seawater represented as a 250 ml/l stock and Trace minerals represented as a 10 ml/l stock, or expand them only after applying the proper dilutions.
- Split JCM J440 into a TB2 variant of the JCM 371 parent instead of merging it as a source duplicate.
- Stop summing main-medium salts with undiluted Synthetic seawater and Trace minerals stock rows.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that JCM 371 keeps the base formula and that JCM 440 contributes only a TB2 variant with final 30 g/l NaCl and the additional 3% Na2S x 9 H2O solution.

## Additional Notes

- None found.

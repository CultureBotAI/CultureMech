# YAML Record Review: THERMOANAEROBACTER (KoKo) MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoanaerobacter_koko_medium.yaml
- Started UTC: 2026-09-25T11:42:04Z
- Finished UTC: 2026-09-25T11:45:32Z
- Verdict: needs curation

## Target

- Generated YAML for DSMZ Medium 710, THERMOANAEROBACTER (KoKo) MEDIUM.
- The record was merged from `KOMODO_710_KoKo_medium`, `medium_710_modified_for_dsm_12299`, and `thermoanaerobacter_koko_medium`.
- The checked sources were the normalized DSMZ 710 and KOMODO 710 records, MediaDive 710, and DSMZ Medium 710.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to DSMZ/MediaDive Medium 710.
- The KOMODO 710 records reference DSMZ Medium 710 through `mediadive.medium:710`.
- The merged KOMODO records appear to be same-formulation DSMZ 710 records; recheck the `medium_710_modified_for_dsm_12299` relationship after correcting stock handling.

## Evidence

- DSMZ 710 lists a 1002 ml main recipe with 1 ml Trace element solution SL-11, 1 ml Wolin's vitamin solution (10x), and 1000 ml distilled water.
- Trace element solution SL-11 is a 1 L stock added at 1 ml/L.
- Wolin's vitamin solution (10x) is a 1 L stock added at 1 ml/L.
- DSMZ 710 gives pH 7.0 and instructs the curator to prepare the basal medium under 100% N2, add bicarbonate from an 80% N2 and 20% CO2 stock, and filter-sterilize vitamins prepared under 100% N2.

## Completeness

- pH 7.0 is present.
- DSMZ preparation steps and the MOPS-buffer supplementation note are present.
- The main 1000 ml distilled-water row is missing.
- Trace element solution SL-11 and Wolin's vitamin solution (10x) are flattened at undiluted stock strength.

## Findings

- Trace element solution SL-11 was expanded at full 1 L stock strength instead of as a 1 ml/L addition.
- Wolin's vitamin solution (10x) was expanded at full 1 L stock strength instead of as a 1 ml/L addition.
- The 1000 ml main distilled-water row is missing.
- The `medium_710_modified_for_dsm_12299` child is treated as a source duplicate; that relationship should be rechecked after the stock model is fixed.

## Recommended Edits

- Regenerate DSMZ 710 with Trace element solution SL-11 and Wolin's vitamin solution (10x) retained as stock additions, or expand them only after applying the 1 ml/L and 1 ml/L dilution factors.
- Preserve the main 1000 ml distilled-water row.
- Re-link the corrected direct DSMZ 710, KOMODO 710, and KOMODO `710_12299` records according to their actual base or variant relationship.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that corrected DSMZ 710 no longer carries undiluted SL-11 or Wolin vitamin rows in the main ingredient list.

## Additional Notes

- None found.

# YAML Record Review: THERMOANAEROBACTER (BA) MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoanaerobacter_ba_medium__416883c0.yaml
- Started UTC: 2026-09-25T11:39:15Z
- Finished UTC: 2026-09-25T11:42:03Z
- Verdict: needs curation

## Target

- Generated YAML for DSMZ Medium 671, THERMOANAEROBACTER (BA) MEDIUM.
- The record was merged from `modified_ba_medium`, `modified_ba_medium_replace_cellobiose_with_cellulose`, and `thermoanaerobacter_ba_medium`.
- The checked sources were the normalized DSMZ 671 and KOMODO 671 records, MediaDive 671, DSMZ Medium 671, and the related TOGO 671 transcriptions.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to DSMZ/MediaDive Medium 671.
- The KOMODO 671 records both reference DSMZ Medium 671 through `mediadive.medium:671`.
- The TOGO M2728 and M2730 records point to the same DSMZ 671 recipe but remain a separate generated record.

## Evidence

- DSMZ 671 lists a 1011 ml main recipe with 10 ml Modified Wolin's mineral solution, 1 ml Wolin's vitamin solution (10x), optional 2 g Avicel cellulose, and 1000 ml distilled water.
- Modified Wolin's mineral solution is a 1 L stock added at 10 ml/L.
- Wolin's vitamin solution (10x) is a 1 L stock added at 1 ml/L.
- DSMZ 671 gives pH 7.0, the 80% N2 plus 20% CO2 anaerobic preparation, and a note that some strains can be adapted to 2 g/L Avicel cellulose.

## Completeness

- pH 7.0 is present.
- DSMZ preparation steps and the optional cellulose note are present.
- The 1000 ml distilled-water row is missing.
- Modified Wolin's mineral solution and Wolin's vitamin solution (10x) are flattened at undiluted stock strength.

## Findings

- Modified Wolin's mineral solution was expanded at full 1 L stock strength instead of as a 10 ml/L addition.
- Main-medium NaCl and CaCl2 rows were summed with the NaCl and CaCl2 rows inside Modified Wolin's mineral solution, producing 1.0989119999999999 G_PER_L NaCl and 0.149456 G_PER_L CaCl2.
- Wolin's vitamin solution was expanded at stock strength instead of at its 1 ml/L final dilution.
- The 1000 ml main-medium Distilled water row is missing.
- The KOMODO `671_replace_Cellobiose_with_Cellulose` child is treated as a source duplicate; recheck that relationship after the stock model is fixed because cellobiose-to-cellulose replacement is a carbon-substrate variant rather than an exact formulation duplicate.

## Recommended Edits

- Regenerate DSMZ 671 with Modified Wolin's mineral solution and Wolin's vitamin solution retained as stock additions, or expand them only after applying the 10 ml/L and 1 ml/L dilution factors.
- Keep duplicate ingredient names in separate recipe scopes until stock dilution is applied so NaCl and CaCl2 are not over-summed.
- Preserve the main 1000 ml distilled-water row.
- Re-link the corrected direct DSMZ 671, KOMODO 671, KOMODO replacement variant, and TOGO 671 records according to their actual base or variant relationship.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that corrected DSMZ 671 has one 0.098912 G_PER_L main NaCl row and a diluted trace-stock NaCl contribution, not a summed 1.0989119999999999 G_PER_L row.

## Additional Notes

- None found.

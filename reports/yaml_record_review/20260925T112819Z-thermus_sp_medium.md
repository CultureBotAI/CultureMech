# YAML Record Review: thermus_sp_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermus_sp_medium.yaml
- Started UTC: 2026-09-25T11:24:55Z
- Finished UTC: 2026-09-25T11:28:19Z
- Verdict: needs curation

## Target

- Generated YAML for the direct DSMZ/MediaDive 1045 THERMUS SP. MEDIUM import.
- The record was merged from `thermus_sp_medium`.
- The checked sources were MediaDive 1045, DSMZ Medium 1045, and MediaDive 74.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to DSMZ/MediaDive 1045, THERMUS SP. MEDIUM, at pH 7.0.
- The `kg_microbe_match` field points at `mediadive.medium:74`, which MediaDive identifies as THERMUS THERMOPHILUS MEDIUM rather than DSMZ 1045.
- DSMZ 1045 and DSMZ 74 are distinct records.

## Evidence

- DSMZ/MediaDive 1045 lists 8 g/L peptone, 4 g/L yeast extract, 2 g/L NaCl, 1000 ml Distilled water, and pH adjustment to 7.0.
- DSMZ/MediaDive 74 lists 4 g/L yeast extract, 8 g/L Proteose peptone no. 3, 2 g/L NaCl, 1000 ml Distilled water, and pH adjustment to 7.0.

## Completeness

- The peptone, yeast extract, NaCl, pH 7.0, and pH-adjustment step are present.
- The 1000 ml source water row is missing.
- The external KG-Microbe match is grounded to the wrong DSMZ medium.

## Findings

- `kg_microbe_match: mediadive.medium:74` should not be attached to this DSMZ 1045 record.
- The 1000 ml Distilled water row from DSMZ 1045 is omitted.

## Recommended Edits

- Remove or correct the `kg_microbe_match` field so DSMZ 1045 does not point at DSMZ 74.
- Preserve the 1000 ml Distilled water row from the DSMZ 1045 main solution.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that DSMZ 1045 and DSMZ 74 remain separate exact source records.

## Additional Notes

- None found.

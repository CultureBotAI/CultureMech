# YAML Record Review: thermus_ruber_medium__78ae616b

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermus_ruber_medium__78ae616b.yaml
- Started UTC: 2026-09-25T11:24:54Z
- Finished UTC: 2026-09-25T11:28:18Z
- Verdict: pass with minor issues

## Target

- Generated YAML for TOGO Medium M2303, Thermus Ruber Medium.
- The record was merged from `TOGO_M2303_Thermus_Ruber_Medium`.
- The checked sources were TOGO M2303, DSMZ Medium 256, and MediaDive 256.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The source pointer is grounded to TOGO M2303, which points directly at the DSMZ Medium 256 PDF.
- MediaDive 256 identifies the same Thermus Ruber Medium at pH 8.0.
- The exact source search found a separate KOMODO 256 record grounded to DSMZ 256.

## Evidence

- TOGO M2303 and DSMZ/MediaDive 256 list 5 g Universal peptone, 1 g yeast extract, 1 g soluble starch, 12 g agar, and 1000 ml Distilled water.
- DSMZ/MediaDive 256 specifies pH 8.0.

## Completeness

- All ingredient rows are present at the source amounts.
- Source pH 8.0 and the pH-adjustment preparation step are missing.
- The 1000 ml source water row is represented as 1000 g/L.

## Findings

- No blocking ingredient error was found.
- pH 8.0 and the source adjustment step should be preserved.
- The 1000 ml water row should be modeled as medium make-up water rather than as a 1000 g/L concentration.

## Recommended Edits

- Preserve pH 8.0 from TOGO M2303 and DSMZ/MediaDive 256.
- Preserve the DSMZ `Adjust pH to 8.0` preparation step.
- Represent the 1000 ml Distilled water row as final make-up water.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify whether the KOMODO 256 record should merge or duplicate-link with this TOGO M2303 record.

## Additional Notes

- None found.

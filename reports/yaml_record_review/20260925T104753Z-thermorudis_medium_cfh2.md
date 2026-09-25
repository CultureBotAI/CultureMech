# YAML Record Review: thermorudis_medium_cfh2

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermorudis_medium_cfh2.yaml
- Started UTC: 2026-09-25T10:47:51Z
- Finished UTC: 2026-09-25T10:47:53Z
- Verdict: pass with minor issues

## Target

- Generated YAML for DSMZ Medium 1692, THERMORUDIS MEDIUM (CFH2).
- The record was merged from `thermorudis_medium_cfh2`.
- The main checked source was MediaDive REST entry 1692.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 after the startup line only and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; exited 0 with only the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The recipe identity is correct for MediaDive/DSMZ Medium 1692.
- The pH, physical state, and the main formula rows align with MediaDive 1692.
- No incorrect required CHEBI grounding was found in the checked main ingredients.

## Evidence

- MediaDive 1692 lists glucose, yeast extract, tryptone, soluble starch, casamino acids, sodium pyruvate, K2HPO4, MgSO4 x 7 H2O, agar, and 1000 ml distilled water.
- MediaDive 1692 records final pH 7.0, phosphate adjustment before adding agar, and autoclaving for 15 min at 121 C.
- The record's DSMZ PDF URL currently resolves to a 404 page rather than a PDF, so the live DSMZ PDF could not be used as a second formula check in this pass.

## Completeness

- The main nutrients, agar concentration, pH, and preparation steps are present.
- The generated record omits the 1000 ml distilled-water row from MediaDive 1692.
- No TOGO, KOMODO, or additional MediaDive duplicate for DSMZ 1692 was found by exact source-ID search with ignored and hidden files included.

## Findings

- Minor issue: the formula omits the source water row, even though MediaDive 1692 lists 1000 ml distilled water alongside the agar recipe.
- Minor issue: the source URL in the record points at a DSMZ PDF path that currently returns a 404 page; MediaDive's structured DSMZ 1692 entry still resolves.

## Recommended Edits

- Preserve the existing generated record and add the 1000 ml distilled-water row if the merge/import pipeline models water for DSMZ media.
- Recheck the DSMZ 1692 PDF URL when a current PDF or replacement DSMZ location is available.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation if a regenerated record adds the water row.
- Confirm whether DSMZ has moved or removed the Medium 1692 PDF before treating the broken PDF URL as a permanent source issue.

## Additional Notes

- None found.

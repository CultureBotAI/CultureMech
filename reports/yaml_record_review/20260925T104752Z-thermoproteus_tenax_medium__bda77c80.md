# YAML Record Review: thermoproteus_tenax_medium__bda77c80

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoproteus_tenax_medium__bda77c80.yaml
- Started UTC: 2026-09-25T10:47:51Z
- Finished UTC: 2026-09-25T10:47:52Z
- Verdict: needs curation

## Target

- Generated YAML for JCM Medium J196, THERMOPROTEUS TENAX MEDIUM.
- The record was merged from `thermoproteus_tenax_medium`.
- The main checked sources were the live JCM 196 page and MediaDive REST entry J196.

## Validation

- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; exited 0 with only the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The recipe identity is correct for JCM Medium J196.
- The live JCM table names this medium as THERMOPROTEUS TENAX MEDIUM and lists pH 5.5 in the preparation text.
- Several ingredient identities were inherited from MediaDive import errors rather than the JCM table: JCM lists `KH2PO4` and `Na2MoO4 x 2 H2O`, while the generated record has `KH2PO3` and `Na2MoO7 x 2 H2O`.
- `Sulfur` is grounded to `CHEBI:26833` sulfur atom; the JCM row is sulfur powder and should use the existing elemental sulfur/sulfur-powder grounding pattern.

## Evidence

- JCM 196 lists 1 L distilled water, 22 ug ZnSO4 x 7 H2O, 5 ug CuCl2 x 2 H2O, 3 ug Na2MoO4 x 2 H2O, 1 ug CoSO4 x 7 H2O, 1 mg resazurin, 10 g sulfur powder, and the anaerobic/filter-sterilization preparation.
- MediaDive J196 mirrors most of the recipe but returns `KH2PO3`, `Na2MoO7 x 2 H2O`, and mojibake units for the four ug trace rows.
- The generated record propagates those MediaDive spelling errors and imports the mojibake ug rows as whole grams per liter.
- A separate older TOGO import, `THERMOPROTEUS_TENAX_MEDIUM`, points at the same JCM GRMD 196 source and carries a worse unit conversion for additional mg and ug rows.

## Completeness

- pH 5.5 and the special anaerobic preparation are present.
- The direct record omits the 1 L distilled-water row that appears in both JCM 196 and MediaDive J196.
- The JCM 196 source URL still serves the source formula.

## Findings

- The formula has blocking concentration and compound errors. ZnSO4 x 7 H2O, CuCl2 x 2 H2O, Na2MoO4 x 2 H2O, and CoSO4 x 7 H2O should be microgram additions, not `22`, `5`, `3`, and `1` g/L top-level concentrations.
- The phosphate and molybdate rows should be corrected to `KH2PO4` and `Na2MoO4 x 2 H2O`; the current `KH2PO3` and `Na2MoO7 x 2 H2O` labels disagree with the live JCM 196 table.
- The generated record is source-duplicated by the older TOGO/JCM M189 record and should remain the canonical JCM 196 copy only after its source-level typos and ug conversions are repaired.

## Recommended Edits

- Repair the JCM 196 import using the live JCM table as the authority for `KH2PO4`, `Na2MoO4 x 2 H2O`, ug trace rows, sulfur powder, and 1 L distilled water.
- Remove or fold the stale TOGO M189 duplicate into the repaired JCM 196 generated record.
- Add or refresh CHEBI grounding for the corrected phosphate, corrected sodium molybdate dihydrate, and elemental sulfur rows.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Recheck the corrected record against the JCM 196 table, not only MediaDive J196, because the MediaDive response currently contains two formula typos and mojibake ug units.
- Confirm no generated duplicate keeps the `TOGO:M189` copy after merge regeneration.

## Additional Notes

- None found.

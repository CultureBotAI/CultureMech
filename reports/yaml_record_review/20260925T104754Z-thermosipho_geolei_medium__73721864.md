# YAML Record Review: thermosipho_geolei_medium__73721864

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermosipho_geolei_medium__73721864.yaml
- Started UTC: 2026-09-25T10:47:51Z
- Finished UTC: 2026-09-25T10:47:54Z
- Verdict: pass with minor issues

## Target

- Generated YAML for JCM Medium J288, THERMOSIPHO GEOLEI MEDIUM.
- The record was merged from `thermosipho_geolei_medium`.
- The main checked source was MediaDive REST entry J288; the live JCM GRMD 288 page was also fetched.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The generated record is correctly identified as MediaDive/JCM Medium J288.
- pH 7.0, 1 mg/L resazurin, the anaerobic maltose and sulfide handling, and the listed solutes match MediaDive J288.
- No incorrect required CHEBI grounding was found in the checked direct record.

## Evidence

- MediaDive J288 lists NaCl, MgCl2 x 6 H2O, PIPES, KCl, NH4Cl, CaCl2 x 2 H2O, K2HPO4, KH2PO4, sodium acetate, yeast extract, Trypticase peptone, maltose, Na2S x 9 H2O, and 1 mg resazurin.
- MediaDive J288 lists the JCM URL with GRMD 288 and preserves the pH 7.0 anaerobic preparation step.
- The current JCM page for GRMD 288 now returns `Nothing found`, so the JCM HTML table could not be used as a second source in this pass.
- The older TOGO M282 duplicate points at the same stale JCM URL and imports resazurin as 1 g/L instead of 1 mg/L.

## Completeness

- The generated direct JCM record has the pH and one preparation step expected from MediaDive J288.
- Distilled water is not present in the direct record, but MediaDive J288 also omits an explicit water row.
- The stale TOGO copy is still present as `THERMOSIPHO_GEOLEI_MEDIUM`.

## Findings

- Minor issue: the record's JCM source URL no longer exposes the source table, leaving MediaDive J288 as the only fetched live representation of this JCM formula.
- Minor issue: an older TOGO/JCM duplicate survives with a resazurin mg-to-g conversion error and should be removed or folded into the direct JCM record.

## Recommended Edits

- Keep the direct MediaDive/JCM J288 record as the canonical generated recipe.
- Remove or merge the stale TOGO M282 duplicate after confirming no source-only ingredient is missing from the direct JCM record.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after duplicate cleanup.
- Look for an archived JCM 288 table or a replacement JCM URL before adding a water row that is not present in MediaDive J288.

## Additional Notes

- None found.

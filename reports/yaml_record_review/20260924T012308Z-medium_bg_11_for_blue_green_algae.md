# YAML Record Review: medium_bg_11_for_blue_green_algae
- Repository: CultureMech
- Record: `data/merge_yaml/merged/medium_bg_11_for_blue_green_algae.yaml`
- Started UTC: 2026-09-24T01:22:27Z
- Finished UTC: 2026-09-24T01:23:08Z
- Verdict: needs curation

## Target
- Reviewed generated merged record `CultureMech:008772` / `medium_bg_11_for_blue_green_algae`.
- Current generated record has source term `TOGO:M2178`, an ATCC source URL, `SOLID_AGAR`, and 17 ingredient rows.
- Exact source-ID and owner checks included ignored files. `find data/normalized_yaml -name 'medium_bg_11_for_blue_green_algae*.yaml' -print` found only `data/normalized_yaml/bacterial/medium_bg_11_for_blue_green_algae.yaml`; the exact `TOGO:M2178` scan found only that owner, the generated record, and normalized index entries.
- The generated record is stale relative to the normalized owner. The owner now collapses the duplicated 1000 ml DI Water rows to one 1000 value in a 2026-09-02 `REPAIRED_SUMMED_DUPLICATE_MERGE` history event, while this generated artifact still emits DI Water 2000.0 g/L with `[Merged 2 duplicates: 1000.0, 1000.0]`.

## Validation
- Open schema validation: passed with no issues reported by `linkml-validate`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file and reported 0 ERROR rows.
- Reference validation: passed; the validator reported 0 checks and no failures.
- Term validation: passed.
- Embedded history validation: Not checked; the available history validator targets standalone `history/` files rather than embedded `MediaRecipe.curation_history` entries.

## Identity and Grounding
- The normalized owner is the only exact owner for `TOGO:M2178` under `data/normalized_yaml`.
- The generated `media_term` preserves TOGO identifier `TOGO:M2178` and original name `Medium BG-11 for Blue-green Algae`.
- The source is ATCC Medium 616, `Medium BG-11 for Blue-green Algae`, as mirrored by live TOGO M2178.
- The MgSO4 x 7H2O row has a heptahydrate primary term, `CHEBI:31795`, but its secondary `mediaingredientmech_chebi_term` still points at generic magnesium sulfate, `CHEBI:32599`.

## Evidence
- The ATCC PDF lists Base Medium components for a final 1000 ml medium, including NaNO3 1.5 g, K2HPO4 0.04 g, MgSO4 x 7H2O 0.075 g, CaCl2 x 2H2O 0.036 g, citric acid 6.0 mg, ferric ammonium citrate 6.0 mg, EDTA 1.0 mg, Na2CO3 0.02 g, Trace Metal Mix A5 1.0 ml, agar 12.0 g if needed, and DI Water 1000.0 ml.
- The same ATCC source lists Trace Metal Mix A5 as a separate 1000 ml stock solution containing H3BO3 2.86 g, MnCl2 x 4H2O 1.81 g, ZnSO4 x 7H2O 0.222 g, Na2MoO4 x 2H2O 0.039 g, CuSO4 x 5H2O 0.079 g, and Co(NO3)2 x 6H2O 49.4 mg.
- ATCC instructs adjusting final pH to 7.1, and live TOGO M2178 metadata also records pH 7.1.

## Completeness
- The generated record includes the base-medium rows, the Trace Metal Mix A5 row, and the A5 stock-solution component rows flattened into one ingredient list.
- The generated record has agar state, broad applications, source notes, the TOGO source term, CHEBI grounding for most chemically specific rows, merge provenance, and curation history.
- The generated record is missing the pH 7.1 assertion available in both the live TOGO metadata and the ATCC PDF.

## Findings
- Generated output is stale and overstates DI Water. The normalized owner has already repaired the duplicate water merge to 1000.0, but the generated file still emits the obsolete 2000.0 value.
- The DI Water and Trace Metal Mix A5 volume rows are mis-modeled as `G_PER_L` concentration rows. ATCC specifies 1000 ml base DI Water and 1 ml Trace Metal Mix A5 per 1000 ml final medium.
- Several milligram quantities were imported as gram-per-liter quantities: 6 mg citric acid as 6 g/L, 6 mg ferric ammonium citrate as 6 g/L, 1 mg EDTA as 1 g/L, and 49.4 mg Co(NO3)2 x 6H2O as 49.4 g/L in the stock mix.
- The trace metal stock solution was flattened into the final medium without the 1 ml per 1000 ml dilution encoded on the parent `Trace Metal Mix A5` row.
- The generated Na2MoO4 x 2H2O stock amount is 0.39 g/L, while the ATCC PDF source lists 0.039 g in the 1000 ml A5 stock.
- The source pH 7.1 was dropped.
- The MgSO4 x 7H2O secondary MediaIngredientMech CHEBI link still points at generic magnesium sulfate even though the primary term has been repaired to the heptahydrate.

## Recommended Edits
- Rebuild `data/normalized_yaml/bacterial/medium_bg_11_for_blue_green_algae.yaml` from the ATCC PDF with correct mg-to-g conversion.
- Represent `Trace Metal Mix A5` as a 1 ml/L stock addition with its separate 1000 ml stock recipe and dilution, or pre-dilute each A5 component by 0.001 before flattening.
- Remove DI Water from the final ingredient concentration list or represent it with a volume-preserving water field if the schema supports one.
- Backfill pH 7.1 from TOGO and ATCC evidence.
- Refresh the MgSO4 x 7H2O secondary CHEBI link so it matches the repaired heptahydrate primary term.
- Regenerate merged YAML after the owner fix so the generated record picks up the DI Water repair.

## Follow-up Checks
- Re-run open schema, strict, reference, and term validation on the regenerated merged record.
- Repeat exact owner and source-ID scans with ignored files included after curation.
- Compare the final record line-by-line against ATCC Medium 616, including units for milligram rows and the A5 stock-solution dilution.

## Additional Notes
- Empty optional fields were not treated as defects.
- No GitHub issues, pull requests, or comments were opened as part of this generated-record review.

# YAML Record Review: Thermoclostridium A-G Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoclostridium_a_g_medium.yaml
- Started UTC: 2026-09-25T11:52:30Z
- Finished UTC: 2026-09-25T11:55:04Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M2756, Thermoclostridium A-G Medium.
- The record was generated directly from `TOGO_M2756_Thermoclostridium_A-GO_Medium`.
- The checked sources were TOGO M2756, MediaDive 326, and DSMZ Medium 326.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to TOGO Medium M2756.
- TOGO M2756 cites DSMZ Medium 326 as its source URL and transcribes the THERMOCLOSTRIDIUM A-G DSMZ recipe.
- This is the TOGO transcription of the DSMZ 326 source that is also represented by a separate direct DSMZ/MediaDive generated record.

## Evidence

- TOGO M2756 records pH 6.8-7.2 in source metadata.
- DSMZ 326 lists a main recipe with 1 ml Trace element solution SL-10, 1 ml Wolin's vitamin solution (10x), and 1000 ml Distilled water.
- TOGO M2756 keeps Trace element solution SL-10 as a 1 ml addition and Vitamin solution as a 10 ml addition.
- The trace-element and vitamin recipes are stock solutions, not main-medium gram-per-liter additions.

## Completeness

- TOGO source pH 6.8-7.2 is missing.
- The 1000 ml main water row is present but was merged with the 990 ml Trace element solution water row and the 1000 ml Vitamin solution water row as 2990 G_PER_L.
- Trace element solution SL-10 and Vitamin solution stock references are still present in `solutions`.
- The stock contents were also duplicated into top-level `ingredients` at stock strength with many mg rows stored as G_PER_L.

## Findings

- TOGO source pH 6.8-7.2 was not mapped to `ph_range`.
- The main and stock distilled-water rows were summed to a nonsensical 2990 G_PER_L water ingredient.
- Trace element solution SL-10 appears both as a stock-solution reference and as undiluted top-level mineral rows.
- Main-medium 12 mg CoCl2 x 6 H2O was summed with the 190 mg Trace element solution row, producing 202 G_PER_L cobalt chloride hexahydrate after mg-to-g unit inflation.
- Trace element SL-10 milligram rows such as Na2MoO4 x 2 H2O, H3BO3, MnCl2 x 4 H2O, NiCl2 x 6 H2O, CuCl2 x 2 H2O, and ZnCl2 were imported as G_PER_L.
- Vitamin-solution milligram rows were imported as G_PER_L.
- The 10 ml 25% HCl stock row was converted to 10 G_PER_L.

## Recommended Edits

- Regenerate TOGO M2756 with pH 6.8-7.2 mapped to `ph_range`.
- Keep Trace element solution SL-10 and Vitamin solution as stock additions, or expand their contents only after applying the source addition volumes and unit conversions.
- Preserve main-medium, trace-stock, and vitamin-stock water rows in separate source scopes.
- Convert all source mg rows to G_PER_L only after dividing by 1000 and applying the stock dilution factor.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that the corrected TOGO M2756 record no longer has 2990 G_PER_L water, 202 G_PER_L cobalt chloride hexahydrate, or `high_metal: true`.

## Additional Notes

- None found.

# YAML Record Review: Thermoanaerobacter (KoKo) Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoanaerobacter_koko_medium__f3bb6f3e.yaml
- Started UTC: 2026-09-25T11:45:33Z
- Finished UTC: 2026-09-25T11:49:16Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M2715, Thermoanaerobacter (KoKo) Medium.
- The record was generated directly from `TOGO_M2715_Thermoanaerobacter_KoKo_Medium`.
- The checked sources were TOGO M2715, MediaDive 710, and DSMZ Medium 710.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to TOGO Medium M2715.
- TOGO M2715 cites DSMZ Medium 710 as its source URL and names the same Thermoanaerobacter (KoKo) formulation.
- This is the TOGO transcription of the DSMZ 710 source that is also represented by a separate direct DSMZ/MediaDive generated record.

## Evidence

- TOGO M2715 transcribes the DSMZ 710 main recipe and records pH 7.0 in source metadata.
- TOGO M2715 keeps Trace element solution SL-11 as a 1 ml addition and Vitamin solution as a 10 ml addition.
- DSMZ 710 lists 1000 ml distilled water in the main recipe, 1 ml Trace element solution SL-11, and 1 ml Wolin's vitamin solution (10x).
- The trace-element and vitamin recipes are stock solutions, not main-medium gram-per-liter additions.

## Completeness

- TOGO source pH 7.0 is missing.
- The 1000 ml main water row is present but was merged with two nested stock-water rows as 3000 G_PER_L.
- The Trace element solution SL-11 and Vitamin solution stock references are still present in `solutions`.
- The stock contents were also duplicated into top-level `ingredients` at stock strength with several mg rows stored as G_PER_L.

## Findings

- TOGO source pH 7.0 was not mapped to `ph_value`.
- The main distilled-water row was summed with stock-solution water rows, producing a 3000 G_PER_L water ingredient.
- Trace element solution SL-11 appears both as a stock solution reference and as undiluted top-level metal rows.
- Trace element SL-11 milligram rows such as Na2MoO4 x 2 H2O, H3BO3, MnCl2 x 4 H2O, CoCl2 x 6 H2O, NiCl2 x 6 H2O, CuCl2 x 2 H2O, and ZnCl2 were imported as G_PER_L.
- Vitamin-solution milligram rows such as Biotin, p-Aminobenzoic acid, Thiamine-HCl, Pyridoxine-HCl, Folic acid, Riboflavin, Nicotinic acid, Lipoic acid, D-Ca-pantothenate, and Vitamin B12 were imported as G_PER_L.
- The generated `high_metal: true` flag is an artifact of the milligram-to-gram unit inflation.

## Recommended Edits

- Regenerate TOGO M2715 with pH 7.0 mapped to `ph_value`.
- Keep Trace element solution SL-11 and Vitamin solution as stock additions, or expand their contents only after applying the source addition volumes and unit conversions.
- Preserve the main 1000 ml distilled-water row independently from nested stock water rows.
- Convert all source mg rows to G_PER_L only after dividing by 1000 and applying the stock dilution factor.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that the corrected TOGO M2715 record no longer has 3000 G_PER_L water, 190 G_PER_L cobalt chloride hexahydrate, or 10 G_PER_L pyridoxine hydrochloride.

## Additional Notes

- None found.

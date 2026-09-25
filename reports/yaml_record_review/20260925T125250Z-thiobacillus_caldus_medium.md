# YAML Record Review: thiobacillus_caldus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiobacillus_caldus_medium.yaml
- Started UTC: 2026-09-25T12:54:26Z
- Finished UTC: 2026-09-25T12:54:50Z
- Verdict: needs curation

## Target

- Generated YAML for the KOMODO 150a THIOBACILLUS CALDUS MEDIUM record enriched from DSMZ 150a-related data.
- The record was merged from `KOMODO_150_ACIDIANUS_BRIERLEYI_MEDIUM` and `thiobacillus_caldus_medium`.
- The checked sources were the local KOMODO merge metadata, MediaDive 150, DSMZ Medium 150, and MediaDive 150a.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to KOMODO 150a, THIOBACILLUS CALDUS MEDIUM.
- MediaDive identifies DSMZ 150a as ACIDITHIOBACILLUS CALDUS MEDIUM.
- The generated record also merged `KOMODO_150_ACIDIANUS_BRIERLEYI_MEDIUM`, but DSMZ/MediaDive 150 is ACIDIANUS BRIERLEYI MEDIUM with a different formulation.

## Evidence

- MediaDive 150a lists a 1010 ml Acidithiobacillus caldus final volume containing basal salts, 10 ml trace element solution, 5 g sulfur, and 1000 ml distilled water at pH 2.5.
- MediaDive 150a keeps FeCl3 x 6 H2O, CuSO4 x 5 H2O, H3BO3, MnSO4 x H2O, Na2MoO4 x 2 H2O, CoCl2 x 6 H2O, and ZnSO4 x 7 H2O inside a separate 1 L trace element stock.
- DSMZ/MediaDive 150 is ACIDIANUS BRIERLEYI MEDIUM, contains yeast extract, uses 10 g sulfur, and adjusts pH to 1.5 to 2.5.

## Completeness

- The KOMODO 150a pH 2.5 and scaled main-solution salts match the MediaDive 150a final-volume calculations.
- The 150a trace-element stock ingredients are present but flattened at stock strength rather than diluted from the 10 ml/L addition.
- The record lacks the DSMZ 150a preparation text for separate trace addition and sterile sulfur handling.
- The bacterial KOMODO 150a medium is merged with an archaeal KOMODO 150 synonym even though DSMZ 150 and 150a are not the same medium.

## Findings

- `KOMODO_150_ACIDIANUS_BRIERLEYI_MEDIUM` should not be merged into this KOMODO 150a / Acidithiobacillus caldus record.
- The trace-element ingredients are overstated by about 100-fold because a 10 ml/L stock was expanded at undiluted stock concentrations.
- The curation history says DSMZ Medium 150 ingredients were copied even though the ingredient table follows the DSMZ 150a 1010 ml formula.
- The generated record omits the source preparation instructions for adding filter-sterilized trace elements and sterile sulfur.

## Recommended Edits

- Split KOMODO 150 / DSMZ 150 ACIDIANUS BRIERLEYI MEDIUM from KOMODO 150a / DSMZ 150a ACIDITHIOBACILLUS CALDUS MEDIUM.
- Recompute final 150a trace-element concentrations from a 10 ml addition into the 1010 ml final volume or model the trace solution explicitly.
- Replace the stale DSMZ 150 history note with one that names DSMZ 150a as the formulation source.
- Restore DSMZ 150a preparation steps for autoclaving the basal medium, filter-sterilizing trace elements, and heat-sterilizing sulfur.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify exact-source normalized records for KOMODO 150, DSMZ 150, KOMODO 150a, and DSMZ 150a remain separate.
- Confirm whether `Thiobacillus caldus` should be retained only as a legacy alias of `Acidithiobacillus caldus`.

## Additional Notes

- None found.

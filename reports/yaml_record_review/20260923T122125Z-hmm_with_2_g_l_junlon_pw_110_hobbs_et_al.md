# YAML Record Review: HMM with 2 g/L Junlon PW 110; Hobbs et al
- Repository: CultureMech
- Record: data/merge_yaml/merged/hmm_with_2_g_l_junlon_pw_110_hobbs_et_al.yaml
- Started UTC: 2026-09-23T12:20:14Z
- Finished UTC: 2026-09-23T12:21:25Z
- Verdict: needs curation

## Target

Reviewed the generated MediaDB merge branch for MediaDB Medium 256, `HMM with 2 g/L Junlon PW 110; Hobbs et al`, at `data/merge_yaml/merged/hmm_with_2_g_l_junlon_pw_110_hobbs_et_al.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hmm_with_2_g_l_junlon_pw_110_hobbs_et_al.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The generated record is grounded to `MEDIADB:256`, but its ingredients were merged from four distinct MediaDB records: 253 for 0.5 g/L Junlon PW 110, 254 for 1 g/L, 255 for 1.5 g/L, and 256 for 2 g/L. These are concentration variants, not duplicate recipes.

## Evidence

MediaDB tab-delimited exports show a single intended difference across the four HMM Junlon PW 110 records. `Propenoate` is 6.93866 mM in MEDIADB:253, 13.8773 mM in MEDIADB:254, 20.816 mM in MEDIADB:255, and 27.7546 mM in MEDIADB:256. All other imported ingredient concentrations match across the four source records.

The four maintained normalized YAML files preserve those `Propenoate` concentrations and already annotate the series as concentration variants of the 1 g/L parent. The generated record collapsed those variants into one MEDIADB:256 artifact and kept the 0.5 g/L source's 6.93866 mM `Propenoate` concentration under the 2 g/L label.

## Completeness

The generated record is stale relative to the maintained MediaDB inputs. It still contains the pre-repair truncated preferred term `'''Iron(III'`, lacks the Sodium iodide CHEBI grounding later added to the maintained records, and retains the generic MediaDB `DISSOLVE`, `ADJUST_PH`, and `FILTER_STERILIZE` steps that are not stated on the MediaDB pages.

## Findings

- Four real MediaDB concentration variants were merged into one generated record.
- The generated `MEDIADB:256` record has the 0.5 g/L `Propenoate` concentration, 6.93866 mM, instead of the 2 g/L source value, 27.7546 mM.
- MEDIADB:253, MEDIADB:254, and MEDIADB:255 are downgraded to synonyms with `source: unknown`, which hides real variant identities.
- The generated artifact is stale; the maintained source repaired `Iron(III) chloride` and added the Sodium iodide grounding after this merge artifact was created.
- The three generic preparation steps are unsupported by MediaDB and should not be emitted unless a source supplies preparation text.

## Recommended Edits

- Prevent `merge_recipes.py` from merging records whose only compositional difference is a declared concentration variant.
- Regenerate separate outputs for MediaDB 253, 254, 255, and 256 from their maintained source files.
- Keep the parent and child `CONCENTRATION_VARIANT` links in the regenerated variant records rather than demoting siblings to synonyms.
- Drop unsupported generic MediaDB preparation steps from the normalized source files or replace them with source-backed preparation details if a provider supplies them.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Re-open MediaDB 253-256 and confirm each regenerated record has exactly the source `Propenoate` value for its Junlon PW 110 dose.
- Confirm the 2 g/L generated record has `Propenoate` at 27.7546 mM, not 6.93866 mM.
- Confirm `Iron(III) chloride` and Sodium iodide repairs survive regeneration.

## Additional Notes

None.

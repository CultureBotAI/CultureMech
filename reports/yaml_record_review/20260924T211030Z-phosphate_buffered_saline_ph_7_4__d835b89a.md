# YAML Record Review: phosphate_buffered_saline_ph_7_4

- Repository: CultureMech
- Record: data/merge_yaml/merged/phosphate_buffered_saline_ph_7_4__d835b89a.yaml
- Started UTC: 2026-09-24T21:10:30Z
- Finished UTC: 2026-09-24T21:10:30Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:003233
- Name: phosphate_buffered_saline_ph_7_4
- Source import: phosphate_buffered_saline_ph_7_4, pbs
- Primary external ID: mediadive.medium:J885
- Source URL: `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=885`

This generated record represents direct JCM Medium 885, PHOSPHATE-BUFFERED SALINE (pH 7.4), merged with a CultureBotHT `PBS` alias.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/phosphate_buffered_saline_ph_7_4__d835b89a.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The JCM branch identity matches JCM_M885. Exact ignored-file searches across `data/merge_yaml/merged` and `data/normalized_yaml` found the equivalent TOGO M926 branch at `data/merge_yaml/merged/phosphate_buffered_saline_ph_7_4.yaml`, so this record should merge with TOGO rather than remain a separate CultureMech ID.

The direct record also merged a CultureBotHT `PBS` alias. That alias uses millimolar concentrations for a generic PBS buffer, while the surviving merged ingredient table is the JCM gram-per-liter pH 7.4 recipe. Preserving `PBS` as a synonym is appropriate, but the final normalized record should make the source-specific JCM/TOGO recipe and the generic CultureBot alias relationship explicit.

## Evidence

- TOGO M926 identifies its original source as JCM_M885 and contains the same four non-water ingredients as this direct record: NaCl 8 g/L, Na2HPO4 x 12 H2O 2.9 g/L, KCl 0.2 g/L, and KH2PO4 0.2 g/L.
- TOGO metadata records pH 7.4, and the direct record has the same pH fact as a preparation step saying the unadjusted pH should be 7.4.
- The normalized CultureBotHT `pbs.yaml` source contains a `PBS` buffer definition in millimolar units that maps to the same major salts but with molar source values rather than the JCM hydrate mass table.
- The live JCM GRMD 885 URL returned "Nothing found" on 2026-09-24, so the TOGO snapshot is currently the accessible copy of the JCM-derived recipe.

## Completeness

The JCM non-water ingredient table is complete. Remaining completeness gaps:

- The pH 7.4 fact is not set in structured `ph_value`.
- The equivalent TOGO M926 source remains split.
- The CultureBotHT `PBS` source is collapsed to a synonym without a clear source-variant or alias annotation.

## Findings

1. Direct JCM J885 and TOGO M926 records describe the same PBS recipe but did not merge.
2. The pH 7.4 metadata is stranded in a prose preparation step instead of the structured `ph_value` field.
3. The preparation step action is `MIX` even though the description is a pH assertion, not a mixing instruction.
4. The CultureBotHT `PBS` alias was merged by name/fingerprint, but its molar source values are not preserved in the generated record.

## Recommended Edits

- Normalize the direct JCM, TOGO M926, and CultureBotHT `PBS` branches into one record with `PBS` retained as a synonym.
- Populate `ph_value: 7.4`.
- Remove the pseudo-preparation `MIX` step or convert it to pH metadata.
- Preserve the JCM/TOGO hydrate mass formulation as the source recipe and retain CultureBotHT PBS as an alias or source-specific variant only if its molar values are considered equivalent by curation policy.

## Follow-up Checks

- Regenerate merged YAML and verify that there is one `phosphate_buffered_saline_ph_7_4` record with the `PBS` synonym.
- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `TOGO:M926`, `GRMD=885`, `mediadive.medium:J885`, and `pbs.yaml` with ignored files included to confirm that stale duplicates are gone.

## Additional Notes

None found.

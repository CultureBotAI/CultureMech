# YAML Record Review: phosphate_buffered_saline_ph_7_4

- Repository: CultureMech
- Record: data/merge_yaml/merged/phosphate_buffered_saline_ph_7_4.yaml
- Started UTC: 2026-09-24T21:09:36Z
- Finished UTC: 2026-09-24T21:09:36Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:010347
- Name: phosphate_buffered_saline_ph_7_4
- Source import: TOGO_M926_Phosphate-Buffered_Saline_pH_7.4
- Primary external ID: TOGO:M926
- Source URL: `https://togomedium.org/medium/M926`

This generated record represents TOGO Medium M926, Phosphate-Buffered Saline (pH 7.4), originally from JCM_M885.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/phosphate_buffered_saline_ph_7_4.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The TOGO identity is correct and points back to the expected JCM_M885 source family. Exact ignored-file searches across `data` found this TOGO M926 branch and a direct JCM GRMD 885 branch already merged with the `pbs` alias in `data/merge_yaml/merged/phosphate_buffered_saline_ph_7_4__d835b89a.yaml`.

The four salts are chemically source-consistent and grounded. The only grounding concern is narrowness: `Na2HPO4 x 12H2O` should eventually use a dodecahydrate-specific term if one is available rather than the broader disodium hydrogenphosphate term.

## Evidence

- TOGO M926 lists the PBS formulation as 1 L distilled water, NaCl 8 g, KH2PO4 0.2 g, KCl 0.2 g, and Na2HPO4 x 12H2O 2.9 g.
- TOGO metadata sets pH to 7.4 and its comment says the unadjusted pH should be 7.4.
- The direct JCM-derived sibling has the same four non-water ingredient quantities and a `PBS` synonym, but remains a separate merged record with a separate CultureMech ID.
- The live JCM GRMD 885 endpoint returned "Nothing found" on 2026-09-24, so the TOGO snapshot is currently the accessible JCM-derived source.

## Completeness

The ingredient table itself is complete for PBS. The record is incomplete at the identity and metadata levels:

- It lacks `ph_value: 7.4` even though TOGO carries that value in both metadata and comments.
- It is not merged with the direct MediaDive/JCM representation of JCM Medium 885 or the shorter `pbs` alias.

## Findings

1. The TOGO M926 PBS record and direct JCM/PBS duplicate are equivalent but remain separate.
2. Structured pH is missing from the TOGO record.
3. The JCM source URL embedded in both source branches is stale and no longer serves the recipe.

## Recommended Edits

- Normalize the TOGO M926, direct JCM J885, and `pbs` aliases so they produce one merged Phosphate-Buffered Saline record.
- Populate `ph_value: 7.4` from the TOGO metadata/comment or the direct branch preparation step.
- Preserve the `PBS` synonym from the direct sibling after the merge.
- Keep the existing non-water ingredient amounts; they agree between TOGO and the direct JCM branch.

## Follow-up Checks

- Regenerate merged YAML and verify that only one `phosphate_buffered_saline_ph_7_4` record remains.
- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `TOGO:M926`, `GRMD=885`, and `mediadive.medium:J885` with ignored files included to confirm stale duplicate records are gone.

## Additional Notes

None found.

# YAML Record Review: sphaerotilus_medium__92c6afae

- Repository: CultureMech
- Record: data/merge_yaml/merged/sphaerotilus_medium__92c6afae.yaml
- Started UTC: 2026-09-25T06:02:05Z
- Finished UTC: 2026-09-25T06:03:58Z
- Verdict: needs curation

## Target

Generated merged YAML for DSMZ 51 / KOMODO 51, SPHAEROTILUS MEDIUM.

## Validation

- LinkML open validation: Passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: Passed; `/private/tmp/sphaerotilus_medium__92c6afae.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The DSMZ and KOMODO source-duplicate relationship is valid: KOMODO 51 explicitly points to DSMZ 51 and copied the same ingredient signature.

The generated `kg_microbe_match: mediadive.medium:12` is incorrect. MediaDive medium 12 is SOIL EXTRACT MEDIUM with air-dried garden soil, tap water, and agar at pH 6.8-7.0; it is not SPHAEROTILUS MEDIUM.

## Evidence

DSMZ 51 and MediaDive 51 list 5.0 g beef extract (Lab Lemco, Oxoid), 15.0 g agar if necessary, and 1000 ml distilled water at pH 7.0. The DSMZ source then prepares sterile agar slants by autoclaving, cools the slants in a sloping position, covers the solid slants with 2 ml sterile tap water, inoculates into the covering tap water, and incubates at 20 to 25 C for at least 48 hours.

## Completeness

The generated record preserves beef extract, optional agar, pH 7.0, and the DSMZ/KOMODO duplicate relationship. It omits the 1000 ml distilled-water row and all DSMZ agar-slant handling instructions.

## Findings

- Critical: `Distilled water` at 1000 ml is missing from the generated ingredient list.
- Major: DSMZ's sterile agar-slant preparation, sloping cool-down, 2 ml sterile tap-water overlay, and 20 to 25 C incubation guidance are missing.
- Major: `kg_microbe_match: mediadive.medium:12` points at SOIL EXTRACT MEDIUM and should be removed.
- Minor: the source qualifier `Lab Lemco, Oxoid` is absent from the generated `Beef extract` row.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/sphaerotilus_medium__92c6afae.yaml` from the repaired DSMZ 51 and KOMODO 51 normalized records.
- Remove `kg_microbe_match: mediadive.medium:12` from the normalized source records or merge pipeline output.
- Preserve the 1000 ml distilled-water row, DSMZ agar-slant preparation steps, pH 7.0, and the `Lab Lemco, Oxoid` beef-extract qualifier.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated merged record.
- Confirm the generated record contains 1000 ml distilled water and no `kg_microbe_match: mediadive.medium:12`.
- Confirm no generated row implies SOIL EXTRACT MEDIUM or DSMZ 12 provenance.

## Additional Notes

None found.

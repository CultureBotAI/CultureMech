# YAML Record Review: THERMOCOCCUS MEDIUM (pH 6.0)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermococcus_medium_ph_6_0.yaml`
- Started UTC: 2026-09-25T09:59:10Z
- Finished UTC: 2026-09-25T10:01:04Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002711`
- Merge fingerprint: `ea91bad9e9faca8cb00b599932404ebf0ef8215502c85b975dc5674aed123ac9`
- Merged sources: `JCM_J280_THERMOCOCCUS_MEDIUM`, `thermococcus_medium_ph_6_0`
- Media term: `mediadive.medium:J350`
- Source medium: JCM Medium J350, "THERMOCOCCUS MEDIUM (pH 6.0)"

## Validation

- LinkML schema validation: Passed with `No issues found`.
- Strict schema validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 reference checks and no errors.
- Term validation: Passed. The only stderr output was the expected `eutils` warning about `pkg_resources`.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not the embedded `MediaRecipe.curation_history` array in this merged YAML.

## Identity and Grounding

- JCM 350 is a pH 6.0 variant of JCM 280, not a source duplicate of it. The generated record merged direct JCM J280 and J350 imports as exact duplicates because their flattened ingredient signatures collided.
- MediaDive REST `J350` represents the recipe as 1000 ml of `Main sol. J280` plus the final readjustment to pH 6.0 with 1.0 N H2SO4. The generated record instead materializes J280 and its trace stocks as a single flat ingredient list.
- The flattened trace minerals inflate overlapping main-solution salts: for example MgSO4 x 7 H2O is stored as 6.33333 g/L after summing 3.33333 from the main solution and 3.0 from the trace mineral stock, and FeSO4 x 7 H2O is stored as 0.1245098 g/L after summing 0.0245098 and 0.1.
- The generated `parent_media.path` points to `data/normalized_yaml/bacterial/JCM_J280_THERMOCOCCUS_MEDIUM.yaml`, while the exact ignored-file search found the parent record at `data/normalized_yaml/archaea/JCM_J280_THERMOCOCCUS_MEDIUM.yaml`.

## Evidence

- JCM 350 contains one table row: 1 L Thermococcus medium from JCM 280, followed by "After reduction of the medium, readjust pH to 6.0 with 1.0 N H2SO4."
- MediaDive REST `J350` preserves the J350-to-J280 relationship as a `Main sol. J280` solution reference, then includes the J280 recipe and its `Trace minerals`/`Trace vitamins` stock definitions as nested solutions.
- The generated target has 33 top-level ingredients, including the JCM 280 base salts and all trace stock salts and vitamins, which shows the nested MediaDive solution hierarchy was flattened.
- Exact ignored-file search found `thermococcus_medium_ph_6_0`, direct `JCM_J280_THERMOCOCCUS_MEDIUM`, and the separate repaired TOGO M345 pH wrapper branch; the direct JCM J350 branch is merged with JCM J280, while TOGO M345 remains in a separate stale generated merge.

## Completeness

- Required scalar fields, expanded ingredients, preparation steps, a parent-media link, curation history, synonyms, and `merged_from` are present.
- No organisms or strain links are expected for this medium-level import.
- The record does not preserve the source's parent-medium structure.
- Trace mineral and vitamin stock membership is flattened and over-counted.

## Findings

- High - Nested JCM 280, Trace minerals, and Trace vitamins solutions were flattened into a single ingredient list, causing stock concentrations to be summed into final-medium concentrations.
- High - JCM J350 was merged as a `SOURCE_DUPLICATE` with JCM J280 even though the source defines J350 as a pH 6.0 variant of J280.
- Medium - `parent_media.path` incorrectly points to a `data/normalized_yaml/bacterial/...` path for an archaeal JCM J280 source.
- Medium - Trace stock preparation and membership are not structurally represented, so the final pH 6.0 adjustment cannot be cleanly distinguished from JCM 280 base preparation.

## Recommended Edits

- Keep the JCM J350 import as a pH variant of direct JCM J280 instead of allowing it into source-duplicate fingerprinting with JCM J280.
- Preserve `Main sol. J280`, `Trace minerals`, and `Trace vitamins` as nested solution references or scale the stock additions before any flattening.
- Correct the direct JCM J280 child link to `data/normalized_yaml/archaea/thermococcus_medium_ph_6_0.yaml` and the generated J350 `parent_media.path` to the archaeal JCM J280 path.
- Re-run duplicate detection so JCM J280, JCM J350, TOGO M273, TOGO M274, and TOGO M345 are grouped by variant relationships rather than exact source-duplicate fingerprints.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated direct JCM J350 branch.
- Re-run exact ignored-file search for `mediadive.medium:J350`, `mediadive.medium:J280`, `GRMD=350`, and `GRMD=280` after duplicate reconciliation.
- Compare regenerated J350 hierarchy against MediaDive REST `J350` to ensure JCM 280 remains a parent medium, not a duplicate source.

## Additional Notes

None found.

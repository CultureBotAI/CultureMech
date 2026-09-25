# YAML Record Review: standard_i_malt_agar
- Repository: CultureMech
- Record: data/merge_yaml/merged/standard_i_malt_agar.yaml
- Started UTC: 2026-09-25T07:17:25Z
- Finished UTC: 2026-09-25T07:20:37Z
- Verdict: pass with minor issues

## Target
Reviewed the generated merged record `data/merge_yaml/merged/standard_i_malt_agar.yaml`, a cross-category duplicate merge between `data/normalized_yaml/bacterial/standard_i_malt_agar.yaml` and `data/normalized_yaml/fungal/standard_i_malt_agar.yaml`.

The bacterial source is KOMODO Medium 637 copied from DSMZ Medium 637; the fungal source is the DSMZ Medium 637 import.

## Validation
- LinkML schema validation: Passed with `No issues found`.
- Strict validation: Passed; scanned 1 file and reported 0 `ERROR` rows. The strict TSV contained the header only.
- Reference validation: Passed; 1 file was validated and 0 reference checks were available.
- Term validation: Passed after the known `eutils` `pkg_resources` deprecation warning.
- Embedded `curation_history`: Not checked. The available `just validate-history` target validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding
The recipe identity is correct. MediaDive `/rest/medium/637` returned one DSMZ record named `STANDARD I + MALT AGAR`, pH 7.2, with source `DSMZ`; the KOMODO source says ID 637 was copied from DSMZ Medium 637, `mediadive.medium:637`.

An initial search using an unanchored `mediadive.medium:310` pattern was discarded because it also matched unrelated source ids `3100` through `3109`. A narrower exact search for `mediadive.medium:637`, `komodo.medium:637`, `CultureMech:006156`, and exact-line `kg_microbe_match: mediadive.medium:310` included ignored files and found the two expected normalized `standard_i_malt_agar.yaml` files, the generated merge, and source-index references under `data/normalized_yaml` and `data/merge_yaml/merged`.

## Evidence
DSMZ Medium 637 lists Standard I Broth 25.0 g, Malt extract 10.0 g, CaCO3 2.0 g, Agar 12.0 g, Distilled water 1000.0 ml, and pH 7.2.

MediaDive's REST payload reports the same four non-water ingredient quantities and pH. The generated record preserves those four non-water ingredients and `ph_value: 7.2`.

## Completeness
No target organisms are present in the generated record; no source evidence in the reviewed DSMZ/MediaDive material names organism growth for this recipe, so that is not a defect.

The water row is omitted from the generated record, which is consistent with many other generated records that omit simple 1000 ml solvent rows.

## Findings
- Low: The generated `merged_from` list contains `standard_i_malt_agar` twice, which hides that the two sources are in different normalized category directories.
- Low: The DSMZ normalized source has an explicit `pH 7.2` preparation step that is not preserved after the KOMODO child becomes canonical.
- Low: Both normalized sources and the generated merge carry `kg_microbe_match: mediadive.medium:310`, which points at DSMZ Medium 310 rather than DSMZ Medium 637.

## Recommended Edits
- Make cross-category merge provenance include enough source path or category context to distinguish the bacterial KOMODO 637 source from the fungal DSMZ 637 source.
- Preserve the DSMZ `pH 7.2` preparation step when the KOMODO child is selected as canonical in a duplicate merge.
- Remove or correct `kg_microbe_match: mediadive.medium:310` on the DSMZ 637 records.

## Follow-up Checks
- After regenerating merge output, verify that `merged_from` is no longer an ambiguous two-item list with the same `standard_i_malt_agar` slug repeated twice.
- Re-run schema, strict, reference, and term validators on the regenerated merged record.

## Additional Notes
No ingredient concentration edits are needed for DSMZ Medium 637.

# YAML Record Review: SUCROSE-Peptone-MEDIUM
- Repository: CultureMech
- Record: data/merge_yaml/merged/sucrose_peptone_medium.yaml
- Started UTC: 2026-09-25T07:45:39Z
- Finished UTC: 2026-09-25T07:45:39Z
- Verdict: pass with minor issues

## Target
Reviewed generated record `CultureMech:005464` / `sucrose_peptone_medium` from `data/merge_yaml/merged/sucrose_peptone_medium.yaml`.

The generated record is the KOMODO canonical merge for KOMODO 459 and DSMZ medium 459.

## Validation
- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed for 1 file with 0 total error rows.
- Reference validation: Passed for 1 file with 0 link checks and all validations passing.
- Term validation: Passed.
- Embedded curation history validation: Not checked; the standalone history validator does not target `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding
The generated identity is coherent: KOMODO medium 459 declares DSMZ medium 459 provenance, and the generated record is linked as a `SOURCE_DUPLICATE` of the direct DSMZ `mediadive.medium:459` parent.

The exact local search found only the expected KOMODO 459 source, direct DSMZ 459 source, generated merge, and indexes for `CultureMech:005464` and `CultureMech:001573`.

## Evidence
The DSMZ medium 459 PDF lists a 1 L liquid medium with 20.0 g peptone, 20.0 g sucrose, and 1000.0 ml distilled water.

The MediaDive 459 payload carries the same three-row recipe. There is no pH or sterilization step in the reviewed DSMZ source.

MediaDive 263 is DSMZ `TIBI MEDIUM`, made with 150 g/L sucrose, dried fig, lemon, tap water, and inoculation with Tibi grains; it is not an exact match for Sucrose-Peptone Medium.

## Completeness
The generated formula is correct for DSMZ 459: the final exposed ingredients are only peptone 20 g/L and sucrose 20 g/L, with the 1000 ml water make-up volume omitted rather than miscast as a mass ingredient.

The generated merge is stale relative to a 2026-09-10 normalized repair that added DSMZ source evidence and grounded Peptone in both the KOMODO and direct DSMZ parents.

The generated and normalized records retain `kg_microbe_match: mediadive.medium:263`, which is a false match to Tibi Medium.

## Findings
- Formula review passes against DSMZ medium 459.
- KOMODO 459 and direct DSMZ 459 are correctly treated as source duplicates.
- The generated file predates the September peptone grounding/source-evidence repair.
- The kg-microbe match to MediaDive 263 is false.

## Recommended Edits
- Remove `kg_microbe_match: mediadive.medium:263` from the normalized KOMODO and DSMZ Sucrose-Peptone records if no exact kg-microbe match exists.
- Regenerate `data/merge_yaml/merged/sucrose_peptone_medium.yaml` from the current normalized YAML so the DSMZ 459 reference, Peptone grounding, and September curation history propagate.
- Keep the ingredient formula at 20 g/L peptone and 20 g/L sucrose.

## Follow-up Checks
- Verify MediaDive 263 no longer appears as a kg-microbe match.
- Verify Peptone remains grounded after regeneration.
- Verify the KOMODO and DSMZ records still merge as source duplicates.
- Re-run schema, strict, reference, and term validators on the regenerated merged YAML.

## Additional Notes
The exact local search for `komodo.medium:459`, `mediadive.medium:459`, `CultureMech:005464`, `CultureMech:001573`, `KOMODO_459_SUCROSE-Peptone-MEDIUM`, and `sucrose_peptone_medium` included ignored and hidden files under `data/normalized_yaml` and `data/merge_yaml/merged`.

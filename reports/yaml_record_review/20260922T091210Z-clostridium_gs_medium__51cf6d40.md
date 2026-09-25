# YAML Record Review: clostridium_gs_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/clostridium_gs_medium__51cf6d40.yaml
- Started UTC: 2026-09-22T09:10:30Z
- Finished UTC: 2026-09-22T09:12:10Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/clostridium_gs_medium__51cf6d40.yaml`, a generated `MediaRecipe` for `CultureMech:009292` / `clostridium_gs_medium`.

The record is generated from the single maintained source `data/normalized_yaml/bacterial/TOGO_M2741_Clostridium_GS_Medium.yaml` with merge fingerprint `51cf6d40374b2e6d645a8e549b937868fafa5802b0b289c290b1c1c2b5f172ca`.

The source identity is `TOGO:M2741`, labelled `Clostridium (GS) Medium`, with original URL `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium255.pdf`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/clostridium_gs_medium__51cf6d40.yaml` | Pass |
| `python scripts/validate_strict.py data/merge_yaml/merged/clostridium_gs_medium__51cf6d40.yaml --out /private/tmp/clostridium_gs_medium__51cf6d40.strict.tsv --workers 1 --quiet` | Pass; TSV contained only the header row |
| `linkml-reference-validator validate data data/merge_yaml/merged/clostridium_gs_medium__51cf6d40.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/clostridium_gs_medium__51cf6d40.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass; emitted only the expected NCBI E-utilities deprecation warning |
| Embedded curation-history validation | Not checked: the documented `just validate-history` target validates standalone `history/` records, not embedded `MediaRecipe.curation_history` nodes in generated YAML |

`just` wrapper validators were not used because the project environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails inside setuptools. The equivalent focused LinkML, strict, reference, and term validators were run under `/usr/local/bin/python3.11` with offline cached packages.

## Identity and Grounding

TOGO M2741 is another representation of DSMZ Medium 255, `CLOSTRIDIUM (GS) MEDIUM`. The TOGO API reports `src_url` `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium255.pdf`, and the downloaded DSMZ PDF confirms the same base medium.

The normalized record preserves most dry ingredients at their DSMZ displayed masses, but three source identities are misrepresented:

- 1000 ml distilled water became a `1000` `G_PER_L` solute.
- 0.50 ml of 0.1% w/v sodium resazurin stock and 1.25 ml of 0.1% w/v FeSO4 x 7 H2O in 0.1 N H2SO4 were migrated into empty placeholder solutions with the same numeric values converted to `G_PER_L`.
- 100% N2 gas became a variable-concentration ingredient instead of an atmosphere and preparation claim.

An ignored-inclusive search of `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` for `CultureMech:009292`, `TOGO:M2741`, `M2741`, the merge fingerprint, `TOGO_M2741_Clostridium_GS_Medium.yaml`, the exact label, and `DSMZ_Medium255` found the reviewed TOGO owner and the separate generated TOGO merge. It also found the direct DSMZ/KOMODO GS merge, `data/merge_yaml/merged/clostridium_gs_medium.yaml`, which imports the same DSMZ PDF more completely.

## Evidence

The inspected TOGO JSON supports the parent formula, including the two milliliter stock additions and the DSMZ pH/preparation comments split across paragraphs 2 through 4. The DSMZ PDF supports the same formula plus strain-specific variant notes.

The reviewed YAML does not preserve TOGO's pH or preparation comments. It has no `ph_value`, no preparation steps, no representation of sparging with 100% N2 for 30-45 min, no Hungate/serum-vial autoclaving detail, and no instruction to add filtered anoxic cellobiose stock before inoculation.

The direct DSMZ/KOMODO generated branch for the same PDF already preserves those preparation steps, has correct final resazurin and FeSO4 concentrations, and has merged the direct DSMZ owner with three KOMODO source duplicates. The TOGO owner is the only unmerged branch with the 1000 `G_PER_L` water and placeholder stock-solution defects.

## Completeness

The base dry ingredient list is recoverable and matches TOGO/DSMZ aside from K2HPO4 x 3 H2O being grounded to generic dipotassium hydrogen phosphate.

The record is not complete enough to follow as a medium protocol because it loses the source pH, the anoxic 100% N2 procedure, both milliliter stock additions, and the before-inoculation cellobiose addition.

Empty target-organism, salinity, and light fields are acceptable for the base source. DSMZ's strain-specific replacement and supplement notes should be separate variants, not unconditional parent claims.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | 1000 ml distilled water was imported as 1000 `G_PER_L`, which is already flagged as `WATER_AS_VOLUME` in `data/import_tracking/reports/concentration_plausibility.tsv`. | `data/normalized_yaml/bacterial/TOGO_M2741_Clostridium_GS_Medium.yaml`; likely the TOGO importer |
| Major | The 0.50 ml sodium resazurin and 1.25 ml FeSO4 stock additions were moved to `solutions` with empty `composition` arrays and `G_PER_L` units, erasing the stock identities and milliliter aliquots. | `data/normalized_yaml/bacterial/TOGO_M2741_Clostridium_GS_Medium.yaml`; solution migration for TOGO imports |
| Major | TOGO's pH and anaerobic preparation comments were dropped from structured fields, leaving no pH 7.2, no 100% N2 sparging, no anoxic dispensing/autoclaving, and no filtered cellobiose-stock addition step. | `data/normalized_yaml/bacterial/TOGO_M2741_Clostridium_GS_Medium.yaml` |
| Major | TOGO M2741 and the direct DSMZ Medium 255 merge still publish as separate generated records even though both cite `DSMZ_Medium255.pdf`. | MediaDive/TOGO merge logic |
| Major | `K2HPO4 x 3 H2O` is grounded to generic dipotassium hydrogen phosphate rather than an exact trihydrate term or an unresolved exact hydrate. | `data/normalized_yaml/bacterial/TOGO_M2741_Clostridium_GS_Medium.yaml` |
| Minor | 100% N2 was imported as a variable ingredient by schema defaulting; it should be modeled as the gas atmosphere in preparation rather than a recipe component. | `data/normalized_yaml/bacterial/TOGO_M2741_Clostridium_GS_Medium.yaml` |

No blocker findings were found. The record denotes the intended TOGO/DSMZ GS medium and passes the focused schema, strict, term, and reference validators.

## Recommended Edits

1. Merge TOGO M2741 into the existing DSMZ/KOMODO Medium 255 source-duplicate group instead of maintaining a separate generated record.
2. Preserve 1000 ml distilled water as a preparation/final-volume row, not `1000 G_PER_L`.
3. Restore the Na-resazurin and FeSO4 stock additions as milliliter stock-solution additions with their stated 0.1% w/v concentrations.
4. Add structured pH 7.2 and DSMZ anoxic preparation steps from the TOGO comments or DSMZ PDF.
5. Model 100% N2 as an anoxic gas atmosphere in the preparation step and remove the variable N2 ingredient.
6. Replace or de-ground the generic K2HPO4 x 3 H2O term.

## Follow-up Checks

- Rerun the focused schema, strict, term, and reference validators on the maintained TOGO owner.
- Regenerate merged YAML and confirm `clostridium_gs_medium__51cf6d40.yaml` disappears into the base `clostridium_gs_medium.yaml` merge group.
- Rerun concentration plausibility and confirm the `WATER_AS_VOLUME` warning for `CultureMech:009292` is gone.
- Manually compare the regenerated GS medium against TOGO M2741 JSON and `DSMZ_Medium255.pdf`, including water, both milliliter stock additions, and the 100% N2 preparation comments.

## Additional Notes

The downloaded DSMZ PDF had already been extracted for the direct GS review and was reused here as primary evidence for the TOGO source's `src_url`.

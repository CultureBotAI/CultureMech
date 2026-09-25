# YAML Record Review: acidithiobacillus_thiooxidans_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml
- Started UTC: 2026-09-21T09:27:25Z
- Finished UTC: 2026-09-21T09:29:03Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:001858`
- Label: `acidithiobacillus_thiooxidans_medium`
- Original name: `ACIDITHIOBACILLUS THIOOXIDANS MEDIUM`
- Category: `bacterial`
- Media term: `mediadive.medium:71` / `DSMZ Medium 71`
- Generated status: generated merge from `data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml`, `data/normalized_yaml/bacterial/for_dsm_14366.yaml`, and `data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml --out /private/tmp/acidithiobacillus_thiooxidans.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The canonical DSMZ identity is correct: DSMZ Medium 71 is `ACIDITHIOBACILLUS THIOOXIDANS MEDIUM`, has pH 4.4 - 4.7, and is represented by `mediadive.medium:71`.

The five non-water base-medium ingredients match the live DSMZ Medium 71 PDF and the live KOMODO Medium 71 page:

- 3.00 g KH2PO4
- 0.50 g `MgSO4 x 7 H2O`
- 3.00 g `(NH4)2SO4`
- 0.25 g `CaCl2 x 2 H2O`
- 5.00 g `Na2S2O3 x 5 H2O`

The generated merge is not source-faithful for the DSM 14366 child. DSMZ says DSM 14366 should supplement the medium with 10.00 mg/L `FeSO4 x 7 H2O` and use final pH 4.4. The live KOMODO Medium 71.1 page likewise lists `FeSO4 x 7 H2O` at 0.01 g/L. `data/normalized_yaml/bacterial/for_dsm_14366.yaml` has pH 4.4 but lacks FeSO4, making it fingerprint-identical to the base and allowing it to merge into this generated base record.

## Evidence

Supported:

- DSMZ and KOMODO both support the five gram-based base-medium ingredients, pH 4.4 - 4.7, and the instruction to prepare the medium without thiosulfate, adjust pH, autoclave at 121 degrees C for 15 min, filter-sterilize thiosulfate separately, and add thiosulfate after autoclaving.
- KOMODO Medium 71 has the same five salts and thiosulfate source as DSMZ Medium 71, so treating `thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml` as a source duplicate of the direct DSMZ 71 owner is supported at the composition level.

Unsupported or incomplete:

- The merged base omits the DSMZ `Distilled water` row at 1000.00 ml.
- `for_dsm_14366` is folded into the generated base despite being a strain-specific pH 4.4 / FeSO4-supplemented variant.
- `for_dsm_14366` is listed both in `merged_from` and under `parent_media`, and the generated `parent_media` points from the base record to the child record with `relationship: SOURCE_DUPLICATE`; this inverts the curated normalized relationship where `for_dsm_14366` points to `acidithiobacillus_thiooxidans_medium` as a `STRAIN_SPECIFIC_VARIANT`.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACIDITHIOBACILLUS_THIOOXIDANS*' -print` searched the ignored timestamped-report directory and found no pre-existing ACIDITHIOBACILLUS THIOOXIDANS report.
- Exact `rg --no-ignore --hidden` searches for `DSMZ_Medium71\.pdf`, `mediadive\.medium:71`, `komodo\.medium:71`, `komodo\.medium:71\.1`, `DSM 14366`, `DSM 14887`, and `DSM 103717` covered tracked and ignored files. They found the three expected Medium 71 normalized sources, the separate Medium 72 tetrathionate reconstruction that cites archived DSMZ Medium 71, and no structured DSM 14887 or DSM 103717 variant records.
- DSMZ Medium 71 lists strain notes for DSM 585, DSM 9463, DSM 14366, DSM 14887, and DSM 103717. The target only attempts to link DSM 14366 and the exact KOMODO 71 duplicate; the DSM 585 tetrathionate substitution is maintained separately as KOMODO Medium 72, and the DSM 9463, DSM 14887, and DSM 103717 notes are not children of this direct DSMZ 71 owner.
- Optional organism, growth metric, evidence, and temperature arrays are absent on the source imports; that is not a target-specific defect.

## Findings

### blocker: a FeSO4-supplemented DSM 14366 variant merged into the base medium

`data/normalized_yaml/bacterial/for_dsm_14366.yaml` should differ from DSMZ Medium 71 by adding 10 mg/L, or 0.01 g/L, `FeSO4 x 7 H2O` and pinning the final pH to 4.4. The normalized child is missing FeSO4, so the generated merge treats it as the same five-ingredient recipe as the direct DSMZ base. `data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml` therefore absorbs a strain-specific KOMODO 71.1 source into the base record and emits contradictory `parent_media` / `variant_relationship` metadata.

### major: DSMZ distilled water is missing from the base and KOMODO-derived copies

DSMZ Medium 71 explicitly lists `Distilled water 1000.00 ml`, and the live KOMODO Medium 71 / 71.1 pages both carry H2O in their metabolite tables. The direct DSMZ owner and both KOMODO-derived Medium 71 owners omit a structured water row, so the generated merge has no explicit 1 L final-volume solvent.

### minor: DSMZ 71 strain-note coverage is partial

The live DSMZ Medium 71 PDF has five strain-specific notes. The DSM 14366 path exists but is malformed, the DSM 585 tetrathionate substitution is separate under KOMODO Medium 72, and exact gitignore-independent searches found no child records for the DSM 14887 capnophilic condition or the DSM 103717 elemental-sulfur substitution. This does not change the base five-salt formulation, but it leaves several in-source DSMZ branches unmodeled from the DSMZ 71 parent.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/for_dsm_14366.yaml`, add `FeSO4 x 7 H2O` at 0.01 g/L, keep `ph_value: 4.4`, and keep the `STRAIN_SPECIFIC_VARIANT` parent link to `data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml`.
2. Add DSMZ's `Distilled water 1000.00 ml` row to the direct DSMZ Medium 71 owner and decide whether the KOMODO 71 / 71.1 owners should include the explicit H2O rows that live KOMODO reports.
3. Confirm `data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml` remains a `SOURCE_DUPLICATE` of DSMZ Medium 71 after water handling is aligned.
4. Decide how to represent the remaining DSMZ 71 strain notes: DSM 585, DSM 9463, DSM 14887, and DSM 103717.
5. Regenerate `data/merge_yaml/merged/` with `just merge-recipes`.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml`.
- Re-fetch DSMZ Medium 71 plus KOMODO Medium 71 and 71.1, then confirm that `for_dsm_14366` survives regeneration as a separate child carrying FeSO4 and pH 4.4.
- Search with `rg --no-ignore --hidden 'FeSO4 x 7 H2O|0\\.01|14366' data/normalized_yaml/bacterial/for_dsm_14366.yaml data/merge_yaml/merged` and confirm KOMODO 71.1 no longer appears in `merged_from` for the base DSMZ Medium 71 record.

## Additional Notes

- `data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_tetrathionate.yaml` cites archived DSMZ Medium 72 and archived DSMZ Medium 71 to expand a separate KOMODO 72 tetrathionate formula. It was not reviewed here beyond confirming that it should not be merged into the thiosulfate base target.

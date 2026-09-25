# YAML Record Review: 5_salt_water_growth_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/5_salt_water_growth_medium.yaml
- Started UTC: 2026-09-21T07:10:30Z
- Finished UTC: 2026-09-21T07:11:07Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/5_salt_water_growth_medium.yaml`.
- Stable identifier: `CultureMech:010360`.
- Source identity asserted by the record: Togo `M938`, `5% Salt Water Growth Medium`, from original JCM `JCM_M897`.
- The generated record was merged from one owner, `TOGO_M938_5_Salt_Water_Growth_Medium.yaml`, on fingerprint `07c3b543a92ebe39afa21e7bf5bee6442f538f217a3b7d8469f2256f06b78f56`.
- Current authoritative owner: `data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/5_salt_water_growth_medium.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/5_salt_water_growth_medium.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/5_salt_water_growth_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/5_salt_water_growth_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- The Togo identity is coherent: M938 resolves to `5% Salt Water Growth Medium` and points at original JCM medium 897.
- A gitignore-independent exact search with a digit boundary for `TOGO:M938` found only one active normalized owner, one generated record, the media content manifest, and the targeted repair script.
- M938 references `MDS salt water (see Medium [M578])`; a gitignore-independent exact search with a digit boundary for `TOGO:M578` found its own normalized owner and generated DB Characterization Medium NO. 2 record.

## Evidence

- Togo M938 lists 500 ml distilled water, 0.6 g yeast extract, 3 g peptone, 100 ml `MDS salt water (see Medium [M578])`, and final pH adjustment to 7.5 with 1 M Tris base.
- Togo M578 includes the referenced `MDS salt water` stock with 240 g `NaCl`, 30 g `MgCl2 x 6H2O`, 35 g `MgSO4 x 7H2O`, 7 g `KCl`, 5 ml 1 M `CaCl2`, and 1 L distilled water.
- `data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml` has a 2026-09-11 `repair_togo_m938_score15.py` event that converts the 100 ml MDS salt-water reference to `ML_PER_L`, imports the M578 MDS composition, removes Tris base from the ingredient list, and records pH 7.5.

## Completeness

- The generated target has the old four-row-plus-empty-solution importer output.
- Its MDS salt-water solution has an empty `composition` array, so the salts that define the medium's salt-water fraction are absent.
- The generated target stores 500 ml distilled water as `500 G_PER_L`, keeps Tris base as a `VARIABLE` ingredient, and stores the 100 ml MDS addition as `100 G_PER_L`.
- The current normalized owner has three top-level ingredients, one populated MDS salt-water solution, pH metadata, preparation steps, data-quality flags, and Togo/JCM references for both M938 and M578.

## Findings

- BLOCKER: `data/merge_yaml/merged/5_salt_water_growth_medium.yaml` predates the 2026-09-11 owner repair and still has an empty `MDS salt water` solution shell.
- BLOCKER: source millilitre amounts are encoded as grams per litre in the generated target: `Distilled water` is `500 G_PER_L`, and the MDS salt-water addition is `100 G_PER_L`.
- MAJOR: `Tris base` is a pH adjustment reagent in the source, but the generated target keeps it as a variable-concentration ingredient.
- MAJOR: the generated target omits the pH 7.5 endpoint and the M578/JCM 574 references that justify the imported MDS salt-water stock.

## Recommended Edits

- Do not edit `data/merge_yaml/merged/5_salt_water_growth_medium.yaml` directly; it is generated.
- Regenerate merged YAML from `data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml` so the populated MDS salt-water solution, `ML_PER_L` amounts, pH metadata, and references replace the stale importer output.
- Keep the M578 MDS stock scoped under the M938 solution reference rather than importing the rest of DB Characterization Medium NO. 2.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated `data/merge_yaml/merged/5_salt_water_growth_medium.yaml`.
- Confirm that `MDS salt water` has six composition rows in generated output.
- Confirm that no `VARIABLE` Tris base row remains.
- Confirm that no row in this record uses a millilitre source amount with `G_PER_L`.

## Additional Notes

- `TOGO:M578` itself remains a separate full medium and still needs independent review; M938 only needs its nested `MDS salt water` stock definition.

# YAML Record Review: AEROBIC SULFOLOBALES MEDIUM WITHOUT SULFUR

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
- Started UTC: 2026-09-21T09:46:28Z
- Finished UTC: 2026-09-21T09:48:44Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:003038`
- Label: `aerobic_sulfolobales_medium_without_sulfur`
- Original name: `AEROBIC SULFOLOBALES MEDIUM WITHOUT SULFUR`
- Category: `archaea`
- Media term: `mediadive.medium:J693`
- Generated status: generated merge of `data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml` and `data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml --out /private/tmp/aerobic_sulfolobales_medium_without_sulfur.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target presents JCM Medium 693, `AEROBIC SULFOLOBALES MEDIUM WITHOUT SULFUR`, as its canonical identity. That identity is source-backed: live JCM GRMD 693 identifies medium 693 with that name, and live TOGO M713 reports `Aerobic Sulfolobales Medium Without Sulfur` with `original_media_id: JCM_M693`.

The ingredients are not faithful to that identity. JCM 693 is a delegated recipe that says to use Medium No. 691 without sulfur; TOGO M713 encodes the same delegation as 0.5 g yeast extract plus 1 L Salt base solution from M711. The generated target instead contains the elemental sulfur ingredient copied from JCM 691 and was then merged with the direct JCM 691 parent record as a source duplicate.

## Evidence

Supported:

- The `media_term` correctly identifies `mediadive.medium:J693`, JCM Medium J693, and the `notes` URL points to GRMD 693.
- The seven trace-salt values copied from local JCM 691 are correctly scaled in this target: MnCl2 x 4 H2O `0.0018`, Na2B4O7 x 10 H2O `0.0045`, ZnSO4 x 7 H2O `0.00022`, CuCl2 x 2 H2O `0.00005`, Na2MoO4 x 2 H2O `0.00003`, VOSO4 x n H2O `0.00003`, and CoSO4 x 7 H2O `0.00001` `G_PER_L`.
- The imported record retained the JCM 693 instruction as a `MIX` preparation step: `Use Medium No. 691 without sulfur.`

Unsupported or over-scoped:

- `Sulfur` is present at 1 g/L, directly contradicting the JCM 693 source instruction.
- `JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml` and `aerobic_sulfolobales_medium.yaml` were merged on the same fingerprint even though JCM 693 is an omitted-component variant of JCM 691, not a duplicate of it.
- The target has no `ph_value`, no 10 N H2SO4 row, and no separate autoclaving / pH-adjustment steps inherited from JCM 691, even though JCM 693 delegates to JCM 691 minus sulfur.
- `variant_children` points to `data/normalized_yaml/bacterial/aerobic_sulfolobales_medium.yaml`; a gitignore-independent `find` over `data/normalized_yaml` found no such bacterial path. The actual JCM 691 source record is `data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml`.
- The generated record has no structured `references`, so the reference validator had zero source URLs to check.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR*' -print` searched the ignored timestamped-report directory and found no pre-existing report for this generated record.
- Exact `rg --no-ignore --hidden` searches for `TOGO:M713`, `mediadive.medium:J693`, `mediadive.medium:J691`, `TOGO:M711`, `AEROBIC SULFOLOBALES MEDIUM WITHOUT SULFUR`, `Aerobic Sulfolobales Medium Without Sulfur`, and `KOMODO_1189_AEROBIC_SULFOLOBALES` covered tracked and ignored files. They found the direct JCM M693 source, the repaired TOGO M713 source, the direct JCM M691 source that was wrongly merged as a duplicate, the DSMZ/KOMODO sulfur-free sibling family, and generated outputs for those records.
- Live JCM GRMD 693 was fetched and contains only the instruction to use Medium No. 691 without sulfur; it does not contain any elemental sulfur row of its own.
- Live TOGO M713 was fetched and contains `Yeast extract (BD-Difco)` plus `Salt base solution (see Medium [M711])`; it does not list elemental sulfur.
- `find data/normalized_yaml -path '*aerobic_sulfolobales_medium.yaml' -print` searched ignored files and found no `data/normalized_yaml/bacterial/aerobic_sulfolobales_medium.yaml`, confirming the generated `variant_children.path` is stale or wrong.

## Findings

### blocker: JCM 693 still contains elemental sulfur

The canonical source for JCM 693 says to use Medium No. 691 without sulfur. The generated JCM 693 record nevertheless contains `Sulfur` at `1 G_PER_L`, so the target represents the parent JCM 691 formula while labeling itself as the sulfur-free child.

### blocker: the omitted-component variant was merged as a source duplicate of its parent

The target merged `JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml` with direct JCM 691 `aerobic_sulfolobales_medium.yaml` because sulfur had been copied into the sulfur-free child, giving both records the same ingredient signature. That incorrectly collapses a child medium into its parent and hides the true `OMITTED_COMPONENT_VARIANT` relationship.

### major: inherited pH and preparation context are incomplete

JCM 693 is defined entirely by reference to JCM 691. The target preserved only `Use Medium No. 691 without sulfur` and the copied ingredient rows; it did not carry forward the pH 2.5, the 10 N H2SO4 adjustment, or the JCM 691 separate-autoclave preparation. The repaired TOGO M713 source shows those facts can be curated explicitly.

### major: the generated variant path points to a nonexistent bacterial file

`variant_children.path` points to `data/normalized_yaml/bacterial/aerobic_sulfolobales_medium.yaml`, but the direct JCM 691 source is under `data/normalized_yaml/archaea/`. The path should not be emitted from stale pre-move location data.

### minor: structured references are absent

The generated JCM 693 record has no `references`, so URL validation performs zero checks despite the record relying on JCM 693 and its JCM 691 parent.

## Recommended Edits

1. Fix `data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml`, not the generated merge YAML.
2. Remove the `Sulfur` ingredient copied from JCM 691.
3. Restore the sulfur-free variant relationship to JCM 691 with `relationship: OMITTED_COMPONENT_VARIANT` instead of `SOURCE_DUPLICATE`.
4. Copy or explicitly derive the parent JCM 691 pH and preparation context that JCM 693 requires after sulfur omission.
5. Add a structured JCM GRMD 693 reference and, if the record copies inherited rows, a structured JCM GRMD 691 reference.
6. Regenerate merges and confirm JCM 693 no longer merges with direct JCM 691.
7. Confirm generated relationship paths are rebuilt from current normalized paths and no longer point to `data/normalized_yaml/bacterial/aerobic_sulfolobales_medium.yaml`.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml`.
- Fetch JCM GRMD 693 and TOGO M713 again, then confirm the regenerated JCM 693 target has no `Sulfur` row.
- Search with `rg --no-ignore --hidden 'Sulfur|CHEBI:26833' data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml` and confirm sulfur does not recur in the sulfur-free record.
- Search with `rg --no-ignore --hidden 'mediadive.medium:J693|mediadive.medium:J691|SOURCE_DUPLICATE|OMITTED_COMPONENT_VARIANT' data/normalized_yaml/archaea data/merge_yaml/merged` and confirm JCM 693 is related to JCM 691 as an omitted-component variant, not a source duplicate.
- Search with `rg --no-ignore --hidden 'data/normalized_yaml/bacterial/aerobic_sulfolobales_medium.yaml' data/normalized_yaml data/merge_yaml/merged` and confirm no generated record points at the nonexistent bacterial path.

## Additional Notes

- TOGO M713 is already curated as a sulfur-free child of TOGO M711, but it did not merge with JCM 693 because the direct JCM 693 import still includes sulfur.
- `data/merge_yaml/merged/aerobic_sulfolobales_medium_without_sulfur__451d06cd.yaml` is the separate DSMZ 1189 / KOMODO 1189 sulfur-free family and should be reviewed independently.

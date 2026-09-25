# YAML Record Review: acidobacterium_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACIDOBACTERIUM_MEDIUM.yaml
- Started UTC: 2026-09-21T09:31:10Z
- Finished UTC: 2026-09-21T09:32:28Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACIDOBACTERIUM_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:009515`
- Label: `acidobacterium_medium`
- Original name: `Acidobacterium Medium`
- Category: `bacterial`
- Media term: `TOGO:M2999` / `Acidobacterium Medium`
- Generated status: generated singleton from `data/normalized_yaml/bacterial/TOGO_M2999_Acidobacterium_Medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDOBACTERIUM_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACIDOBACTERIUM_MEDIUM.yaml --out /private/tmp/acidobacterium_medium.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACIDOBACTERIUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACIDOBACTERIUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The source identity is correct: TOGO M2999 is JCM Medium 142 variant `JCM_M142-1`, derived from live JCM `GRMD=142` / `ACIDOBACTERIUM MEDIUM`.

The source formula is two-solution and order-sensitive:

- Solution A: 2.0 g `(NH4)2SO4`, 0.1 g KCl, 0.5 g K2HPO4, 0.5 g `MgSO4.7H2O`, 0.1 g `Yeast extract (BD-Difco)`, and 500.0 ml distilled water
- pH adjustment of Solution A to 3.5 with H2SO4
- Solution B: 1.0 g glucose and 500.0 ml distilled water
- separate autoclaving of Solutions A and B, followed by aseptic mixing

The generated target preserves the dry ingredients, glucose, and H2SO4 labels, but it flattens Solution A and Solution B into the top-level ingredient list, omits structured `ph_value: 3.5`, collapses the two 500 ml solution water rows, and leaves Solution A/B as empty placeholders.

## Evidence

Supported:

- JCM and TOGO both support the target's TOGO/JCM identity, Solution A salt quantities, yeast-extract quantity, Solution B glucose quantity, pH 3.5 adjustment with H2SO4, and two 500 ml water amounts.
- The existing CHEBI groundings for water, K2HPO4, KCl, ammonium sulfate, sulfuric acid, and glucose are chemically compatible with their labels.

Unsupported or incomplete:

- `Distilled water` appears as one 1000.0 `G_PER_L` ingredient in the generated record. Those are two separate 500 ml solution volumes, not one mass concentration.
- Solution A and Solution B appear as two empty `G_PER_L` solution placeholders instead of carrying the source compositions.
- The generated record has no `ph_value: 3.5` even though the TOGO API exposes `ph: "3.5"` and JCM says Solution A is adjusted to pH 3.5.
- The preparation text that Solutions A and B are autoclaved separately and mixed aseptically is absent.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACIDOBACTERIUM*' -print` searched the ignored timestamped-report directory and found no pre-existing ACIDOBACTERIUM report.
- Exact `rg --no-ignore --hidden` searches for `TOGO:M2999`, `M2999`, `JCM_M142-1`, `GRMD=142`, `jcm_grmd\?GRMD=142`, and `Acidobacterium Medium` covered tracked and ignored files. They found the reviewed liquid TOGO M2999 record, the agar TOGO M3000 record for `JCM_M142-2`, a direct JCM J142 import, and no earlier review report.
- `data/normalized_yaml/bacterial/TOGO_M3000_Acidobacterium_Medium.yaml` is the explicit 15 g/L agar form of the same JCM 142 recipe; it is kept as a separate generated record rather than as an agar / physical-state variant.
- `data/normalized_yaml/bacterial/acidobacterium_medium.yaml` is a direct JCM J142 import for the same source. It omits both distilled-water rows, omits H2SO4 as a variable ingredient, omits the separate Solution A/B autoclaving step, and is not linked to either TOGO JCM 142 record.
- Optional organism, growth metric, evidence, and temperature arrays are absent on the source import; that is not a target-specific defect.

## Findings

### blocker: Solution A and Solution B are flattened into one final ingredient list

JCM Medium 142 partitions the recipe into a pH-adjusted Solution A and a glucose-containing Solution B, autoclaves them separately, and then mixes them aseptically. The maintained TOGO M2999 owner instead stores all components as peer top-level ingredients, leaves Solution A and Solution B as empty placeholders, and encodes both 500 ml solution volumes as `500 G_PER_L`. The generated target inherits that structural flattening and further sums the water rows to 1000.0 `G_PER_L`.

### major: pH and sterilization semantics are missing

The TOGO M2999 API and JCM page both require Solution A to be adjusted to pH 3.5 with H2SO4; the JCM page additionally requires Solution A and Solution B to be autoclaved separately before aseptic mixing. The generated target has a variable H2SO4 ingredient but no `ph_value: 3.5`, no `ADJUST_PH` preparation step, and no preparation step for the separate Solution A/B autoclaves.

### major: JCM 142 duplicate and agar-variant topology is absent

Three maintained records point at the same JCM `GRMD=142`: the reviewed liquid TOGO M2999 import, the solid TOGO M3000 import with 15 g/L agar, and the direct JCM J142 import. They currently feed three generated files instead of one base recipe plus an agar / physical-state variant and a source duplicate. That leaves the agar variant unreconciled and leaves the direct JCM copy with less source structure than the TOGO records.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M2999_Acidobacterium_Medium.yaml`, nest the Solution A ingredients plus its 500 ml water row under Solution A, nest glucose plus its 500 ml water row under Solution B, and store the 500 ml addition volumes as volume units rather than `G_PER_L`.
2. Add `ph_value: 3.5` and preparation steps for H2SO4 adjustment, separate autoclaving of Solutions A and B, and aseptic mixing.
3. Apply the same Solution A/Solution B repair to `data/normalized_yaml/bacterial/TOGO_M3000_Acidobacterium_Medium.yaml`, preserving its 15 g/L agar in Solution B as the solid-medium variant.
4. Repair or deprecate `data/normalized_yaml/bacterial/acidobacterium_medium.yaml`, then link the remaining JCM 142 records as a source duplicate plus an agar / physical-state variant.
5. Regenerate `data/merge_yaml/merged/` with `just merge-recipes`.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACIDOBACTERIUM_MEDIUM.yaml`.
- Re-fetch TOGO M2999 and JCM `GRMD=142`, then confirm Solution A, Solution B, the pH 3.5 H2SO4 adjustment, the two 500 ml water rows, and the separate-autoclave instruction are structured.
- Search with `rg --no-ignore --hidden 'JCM_M142|GRMD=142|TOGO:M2999|TOGO:M3000|mediadive.medium:J142' data/normalized_yaml/bacterial data/merge_yaml/merged` and confirm the direct JCM, liquid TOGO, and agar TOGO records have the intended source-duplicate and variant topology.

## Additional Notes

- The MgSO4 hydrate label uses a source-specific middle-dot separator from the TOGO/JCM extraction; the current CHEBI primary term is the correct magnesium sulfate heptahydrate.

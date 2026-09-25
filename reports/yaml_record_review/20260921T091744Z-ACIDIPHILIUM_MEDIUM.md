# YAML Record Review: acidiphilium_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml
- Started UTC: 2026-09-21T09:15:50Z
- Finished UTC: 2026-09-21T09:17:46Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:002462`
- Label: `acidiphilium_medium`
- Original name: `ACIDIPHILIUM MEDIUM`
- Category: `bacterial`
- Media term: `mediadive.medium:J129` / `JCM Medium J129`
- Generated status: generated singleton from `data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml --out /private/tmp/acidiphilium.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The JCM identity is correct: `GRMD=129` is `ACIDIPHILIUM MEDIUM`, and the target's `mediadive.medium:J129` points at that page.

The direct JCM recipe is much smaller and more structured than the generated record:

- Solution A contains 2.0 g `(NH4)2SO4`, 0.1 g `KCl`, 0.5 g `K2HPO4`, 0.5 g `MgSO4 x 7 H2O`, 0.1 g `Trypticase soy broth (BD-BBL)`, and 500 ml distilled water.
- Solution A is adjusted to pH 3.0.
- Solution B contains 1.0 g glucose and 500 ml distilled water.
- Solutions A and B are autoclaved separately and mixed aseptically.
- The solid form adds 15 g/L agar in Solution B before autoclaving.

The generated target keeps the four salts and the 1 g/L glucose, but it also expands 0.1 g/L Trypticase soy broth into full-strength TSB/TSA constituents at 17 g/L pancreatic digest of casein, 3 g/L peptic digest of soybean meal, 2.5 g/L glucose, 5 g/L sodium chloride, 2.5 g/L dipotassium phosphate, and 15 g/L agar. That expansion is not source-faithful to JCM J129 and makes the record denote a different medium.

## Evidence

Supported:

- The JCM J129 source supports the media ID, name, ammonium sulfate, KCl, K2HPO4, MgSO4 x 7 H2O, 0.1 g/L Trypticase soy broth, 1 g/L glucose, pH 3.0, and the optional 15 g/L agar for a solid form.
- The salts and glucose are grounded to appropriate CHEBI terms.

Unsupported or over-scoped:

- The target's `Pancreatic digest of casein`, `Peptic digest of soybean meal`, 2.5 g/L `Glucose`, `Sodium chloride`, 2.5 g/L `Dipotassium phosphate`, and TSA-specific `Agar` rows are product-decomposition artifacts and are not direct JCM J129 ingredients.
- The target is declared `physical_state: LIQUID` but includes a 15 g/L agar row from Tryptic Soy Agar constituent research. In JCM J129, agar is only a solid-medium option in Solution B, not a liquid-medium ingredient.
- The target's preparation omits the Solution A / Solution B structure, 500 ml + 500 ml water split, separate autoclaving, and aseptic mixing.
- The supplier catalog entries point at a generic Tryptic Soy Broth article and do not evidence the JCM-specific 0.1 g/L BD-BBL Trypticase soy broth addition or the injected full-strength ingredient masses.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACIDIPHILIUM_MEDIUM*' -print` searched the ignored timestamped-report directory and found no pre-existing ACIDIPHILIUM MEDIUM report.
- Exact `rg --no-ignore --hidden` searches for `GRMD=129`, `mediadive.medium:J129`, `JCM_J129`, `TOGO_M2997`, `TOGO_M2998`, `mediadive.medium:269`, and `komodo.medium:269` covered `data/merge_yaml`, `data/normalized_yaml`, and the ignored `reports/yaml_record_review` directory. They found the expected JCM J129 target, same-source TOGO J129 split records, and the separate DSMZ 269 Acidiphilium family; they did not find another ACIDIPHILIUM MEDIUM report.
- The DSMZ 269 `ACIDIPHILIUM MEDIUM` family has the same salt base but uses yeast extract instead of JCM J129's Trypticase soy broth and has its own DSMZ strain-specific variants. That family is relevant for later grouping decisions but should not be merged directly into this JCM J129 target.
- Optional organism, growth metric, and evidence arrays are absent on the source import; that is not a target-specific defect.

## Findings

### blocker: Trypticase soy broth was expanded into an unsupported full TSB/TSA formula

JCM J129 specifies one complex ingredient: 0.1 g/L `Trypticase soy broth (BD-BBL)`. `data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml` instead carries a researched full-strength TSB/TSA decomposition with 17 g/L pancreatic digest of casein, 3 g/L peptic digest of soybean meal, 2.5 g/L glucose, 5 g/L sodium chloride, 2.5 g/L dipotassium phosphate, and 15 g/L agar. Those rows are unscaled by the 0.1 g/L JCM dose and duplicate the JCM record's own 1 g/L glucose and 0.5 g/L K2HPO4. This changes the recipe's carbon, salt, phosphate, and solidifying-agent composition by orders of magnitude. The maintained owner is `data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml`; the same enrichment also appears in `data/normalized_yaml/bacterial/TOGO_M2997_Acidiphilium_Medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M2998_Acidiphilium_Medium.yaml`.

### major: the generated record drops the required Solution A / Solution B preparation

The inspected JCM page separates Acidiphilium medium into 500 ml Solution A and 500 ml Solution B, adjusts Solution A to pH 3.0, autoclaves the two solutions separately, then mixes aseptically. The target reduces all of that to one `ADJUST_PH` step. Even after removing the unsupported TSB/TSA constituent expansion, the maintained JCM J129 record needs nested Solution A and Solution B records so glucose and optional solid-medium agar stay in Solution B and the separate sterilization step is machine-readable.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml`, remove the full-strength TSB/TSA constituent rows and restore `Trypticase soy broth (BD-BBL)` as the 0.1 g/L complex ingredient named by JCM.
2. Model JCM J129 as Solution A plus Solution B with 500 ml/L of each, pH 3.0 on Solution A, separate autoclaving, and aseptic mixing.
3. Represent the 15 g/L agar addition as a solid-medium variant or as a Solution B solid-form option, not as a direct ingredient of the liquid parent.
4. Apply the same JCM J129 repair to the TOGO M2997 and M2998 source imports if those generated splits remain in `data/normalized_yaml`.
5. Regenerate `data/merge_yaml/merged/` with `just merge-recipes` and confirm `ACIDIPHILIUM_MEDIUM.yaml` contains only source-supported JCM J129 ingredients.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACIDIPHILIUM_MEDIUM.yaml`.
- Re-fetch JCM `GRMD=129` and the TOGO M2997/M2998 API payloads, then compare Solution A, Solution B, pH, separate autoclaving, and solid agar representation by hand.
- Search with `rg --no-ignore --hidden 'Tryptic Soy Broth \\(TSB\\) / Tryptic Soy Agar \\(TSA\\)' data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml data/normalized_yaml/bacterial/TOGO_M2997_Acidiphilium_Medium.yaml data/normalized_yaml/bacterial/TOGO_M2998_Acidiphilium_Medium.yaml` and confirm the unsupported constituent-enrichment block is gone from the JCM J129 family.

## Additional Notes

- The direct TOGO JCM J129 records are generated from the same JCM source and currently split the liquid and solid forms into M2997 and M2998. They retain `Solution A` and `Solution B` objects but store both as empty 500 `G_PER_L` solutions and inherit the same unsupported TSB/TSA decomposition reviewed here.
- DSMZ Medium 269 is also named `ACIDIPHILIUM MEDIUM`, but the inspected DSMZ PDF uses 0.3 g/L yeast extract and 1.0 g/L D-glucose rather than JCM J129's 0.1 g/L Trypticase soy broth. It should remain a distinct sibling or variant family until a curator explicitly reconciles the JCM and DSMZ recipes.

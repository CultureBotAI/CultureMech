# YAML Record Review: activated_carbon_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml
- Started UTC: 2026-09-21T09:42:00Z
- Finished UTC: 2026-09-21T09:43:07Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:001956`
- Label: `activated_carbon_medium`
- Original name: `ACTIVATED CARBON MEDIUM`
- Category: `bacterial`
- Media term: `mediadive.medium:811` / `ACTIVATED CARBON MEDIUM`
- Generated status: generated single-source record from `data/normalized_yaml/bacterial/activated_carbon_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml --out /private/tmp/activated_carbon.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target identity is coherent: live DSMZ Medium 811 is `ACTIVATED CARBON MEDIUM`, and the generated file is a single-source output from the corresponding normalized DSMZ record.

The main-medium rows are mostly faithful, but the trace elements are flattened. DSMZ Medium 811 lists Na2HPO4 x 12 H2O, KH2PO4, NH4Cl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, ferric ammonium citrate, 5 g activated carbon, 15 g agar, bidistilled water to 1000 ml, and 1 ml of Trace element solution TS2. The generated record instead puts all TS2 stock components directly in the final `ingredients` list at their stock g/L values.

## Evidence

Supported:

- Live DSMZ Medium 811 supports the target's DSMZ Medium 811 identity, pH 7.5, 9.0 g/L Na2HPO4 x 12 H2O, 1.5 g/L KH2PO4, 1.5 g/L NH4Cl, 0.2 g/L MgSO4 x 7 H2O, 0.02 g/L CaCl2 x 2 H2O, 0.0012 g/L ferric ammonium citrate, 5 g/L activated carbon, 15 g/L agar, and 1000 ml/L bidistilled water.
- Live DSMZ Medium 811 supports Trace element solution TS2 as a 1000 ml stock containing ZnSO4 x 7 H2O, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, Na2SeO3, and distilled water.
- Live DSMZ Medium 811 supports adding 1 ml/L of TS2 before autoclaving, dissolving all ingredients before adding activated carbon, then autoclaving.
- `data/normalized_yaml/bacterial/mediadive_1647_Main_sol_811.yaml` contains only the main-medium rows, which confirms that the extra metal, borate, molybdate, and selenite rows in the `MediaRecipe` are TS2 stock contents rather than main solution rows.

Unsupported or over-scoped:

- The generated ZnSO4, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, Na2MoO4, and Na2SeO3 ingredients are TS2 stock-strength rows treated as final medium rows, making the final trace-element salts 1000x too concentrated.
- The generated record does not preserve the Trace element solution TS2 boundary, its 1000 ml distilled-water row, or the 1 ml/L stock addition.
- The bidistillated-water row is represented as `1000` `G_PER_L` even though DSMZ lists it as a 1000 ml preparation volume.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACTIVATED_CARBON*' -print` searched the ignored timestamped-report directory and found no pre-existing ACTIVATED CARBON report.
- Exact `rg --no-ignore --hidden` searches for `ACTIVATED CARBON`, `activated_carbon`, `mediadive\.medium:811`, `mediadive\.solution:1647`, `DSMZ Medium: 811`, and `Main sol\. 811` covered tracked and ignored files. They found the single normalized DSMZ parent, the generated target, the companion MediaDive main-solution record, and index or plausibility-report references.
- Optional organism, growth metric, evidence, and temperature arrays are absent on the source import; that is not a target-specific defect.

## Findings

### blocker: Trace element solution TS2 is flattened at stock strength

DSMZ Medium 811 adds 1 ml/L Trace element solution TS2. The generated record lists the TS2 components as direct ingredients with their stock concentrations: for example 0.1 g/L ZnSO4 x 7 H2O, 0.3 g/L H3BO3, 0.2 g/L CoCl2 x 6 H2O, and 0.9 g/L Na2MoO4 x 2 H2O. Those concentrations belong to the 1000 ml TS2 stock and should be nested under a 1 ml/L solution addition rather than published as final medium grams per liter.

### major: water volume is typed as mass concentration

DSMZ Medium 811 specifies 1000 ml bidistilled water for the main recipe and 1000 ml distilled water for TS2. The generated record has only the main water row and stores it as `1000` `G_PER_L`, while the TS2 water is absent because the whole TS2 stock boundary was flattened away.

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/activated_carbon_medium.yaml` so Trace element solution TS2 is nested at 1 ml/L with the eight DSMZ stock components and its 1000 ml distilled-water preparation volume.
2. Keep `data/normalized_yaml/bacterial/mediadive_1647_Main_sol_811.yaml` as the main DSMZ 811 solution and use it to avoid mixing TS2 stock rows into the main ingredient list.
3. Represent the main `Double distilled water` amount as a 1000 ml/L preparation volume rather than a `1000` `G_PER_L` concentration.
4. Regenerate `data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml` from the repaired normalized record.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml`.
- Re-fetch DSMZ Medium 811 and confirm the generated record has exactly one 1 ml/L Trace element solution TS2 addition.
- Search with `rg --no-ignore --hidden 'preferred_term: ZnSO4 x 7 H2O|preferred_term: Na2MoO4 x 2 H2O|Trace element solution TS2' data/normalized_yaml/bacterial/activated_carbon_medium.yaml data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml` and confirm TS2 components live only under a nested stock solution.
- Search with `rg --no-ignore --hidden 'Double distilled water\\n  term:|unit: G_PER_L' data/normalized_yaml/bacterial/activated_carbon_medium.yaml data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml` and confirm water is no longer modeled as a gram-per-liter pseudo-concentration.

## Additional Notes

- The ungrounded `Activated carbon` row is acceptable; previous project curation explicitly de-grounded it rather than forcing it to an unrelated ChEBI term.

# YAML Record Review: ALGORIPHAGUS ALKALIPHILUS medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml
- Started UTC: 2026-09-21T10:09:27Z
- Finished UTC: 2026-09-21T10:10:56Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:003999`
- Label: `algoriphagus_alkaliphilus_medium`
- Original name: `ALGORIPHAGUS ALKALIPHILUS medium`
- Category: `bacterial`
- Media term: `komodo.medium:1242`
- Generated status: generated merge of `data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml` and `data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml --out /private/tmp/algoriphagus_alkaliphilus_medium.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target is a valid source-duplicate merge of KOMODO 1242 and direct DSMZ 1242. DSMZ Medium 1242 is `ALGORIPHAGUS ALKALIPHILUS MEDIUM`, lists the pH as 8.0 plus or minus 0.2, and gives a solid medium with agar.

The basal yeast extract, proteose peptone no. 3, casamino acids, glucose, pyruvic acid, direct MgSO4 x 7 H2O, K2HPO4, Tris buffer, and agar rows are supported by the DSMZ 1242 PDF. The remaining mineral and trace-element rows come from nested stocks: DSMZ 1242 adds 50 ml/L of its own `Mineralsolution 1`, and it adds 5 ml/L of the `Traceelements solution` defined in DSMZ 1033.

## Evidence

Supported:

- KOMODO 1242 and DSMZ 1242 are source duplicates with the same local ingredient signature.
- Yeast extract 1 g/L, proteose peptone no. 3 1 g/L, casamino acids 1 g/L, glucose 1 g/L, pyruvic acid 0.05 g/L, direct MgSO4 x 7 H2O 0.10 g/L, K2HPO4 0.60 g/L, Tris buffer at 100 ml/L of 1 M pH 8.0 stock, agar 15 g/L, and pH 7.8-8.2 are supported by DSMZ 1242.

Unsupported or over-scoped:

- The generated NTA, CaSO4 x 2 H2O, NaCl, KNO3, NaNO3, and Na2HPO4 rows are `Mineralsolution 1` stock concentrations, not final-medium concentrations.
- The generated MgSO4 x 7 H2O row sums DSMZ 1242's direct 0.10 g/L MgSO4 with an undiluted 1.0 g/L mineral-stock MgSO4 row; the final concentration should include only 5% of that stock row.
- The generated MnSO4 x H2O, ZnSO4 x 7 H2O, H3BO3, CuSO4 x 5 H2O, Na2MoO4 x 2 H2O, and CoCl2 x 6 H2O rows are DSMZ 1033 Traceelements Solution stock concentrations, not final-medium concentrations.
- DSMZ 1242's 845 ml distilled water row and autoclave instruction are absent from the generated target, and the pH instruction from the direct DSMZ normalized parent was dropped when the generated merge copied the KOMODO wrapper.
- No structured DSMZ 1242 or DSMZ 1033 references are present, so `linkml-reference-validator` performed zero checks.
- The KNO3 and NaNO3 rows still have stale `MediaIngredientMech:000170` and `MediaIngredientMech:000171` links.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ALGORIPHAGUS_ALKALIPHILUS_MEDIUM*' -print` searched the ignored timestamped-report directory and found no pre-existing ALGORIPHAGUS ALKALIPHILUS report.
- Exact `rg --no-ignore --hidden` searches for `komodo.medium:1242\b`, `mediadive.medium:1242\b`, `DSMZ Medium 1242`, `DSMZ_Medium1242`, `KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium`, and `^name: algoriphagus_alkaliphilus_medium$` covered tracked and ignored files. They found the KOMODO 1242 and DSMZ 1242 source-duplicate parents, their generated merge, derived index rows, and historical validation/report rows.
- The DSMZ 1242 and DSMZ 1033 PDFs were fetched live and extracted locally with `mutool`; together they confirm DSMZ 1242's 50 ml/L mineral-stock addition, 5 ml/L DSMZ 1033 trace-element-stock addition, direct 0.10 g/L MgSO4 row, pH text, and autoclave text.

## Findings

### blocker: Mineralsolution 1 was flattened 20-fold too high

DSMZ 1242 adds 50 ml/L of Mineralsolution 1. The target emits the mineral stock's NTA, CaSO4 x 2 H2O, MgSO4 x 7 H2O, NaCl, KNO3, NaNO3, and Na2HPO4 rows at stock strength. Those stock-derived contributions must be diluted 1:20 in the final medium; the current MgSO4 x 7 H2O row also combines direct and stock MgSO4 without applying that dilution.

### blocker: DSMZ 1033 Traceelements Solution was flattened 200-fold too high

DSMZ 1242 adds 5 ml/L of the Traceelements Solution from DSMZ 1033. The target publishes MnSO4 x H2O, ZnSO4 x 7 H2O, H3BO3, CuSO4 x 5 H2O, Na2MoO4 x 2 H2O, and CoCl2 x 6 H2O at their 1000 ml stock concentrations, so each generated trace-element row is 200 times the DSMZ 1242 final concentration.

### major: source preparation and water rows were dropped

The direct DSMZ parent retains `Adjust pH 7.8-8.2` and `Autoclave at 121C for 15 minutes`; the generated KOMODO-wrapper output has no preparation steps. It also lacks DSMZ 1242's explicit 845 ml distilled-water row, which completes the medium volume after 50 ml Mineralsolution 1, 5 ml trace-element solution, and 100 ml Tris buffer are added.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml` and `data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml`; do not edit the generated merge YAML directly.
2. Represent DSMZ 1242 Mineralsolution 1 as a 50 ml/L stock addition, or dilute NTA, CaSO4 x 2 H2O, MgSO4 x 7 H2O, NaCl, KNO3, NaNO3, and Na2HPO4 by 0.05 when flattening.
3. Represent DSMZ 1033 Traceelements Solution as a 5 ml/L stock addition, or dilute MnSO4 x H2O, ZnSO4 x 7 H2O, H3BO3, CuSO4 x 5 H2O, Na2MoO4 x 2 H2O, and CoCl2 x 6 H2O by 0.005 when flattening.
4. Preserve the direct 0.10 g/L DSMZ 1242 MgSO4 row separately or add it to only the diluted 0.05 g/L mineral-stock MgSO4 contribution.
5. Restore the DSMZ 1242 distilled-water and preparation text, including pH 7.8-8.2 adjustment and 121C autoclaving for 15 minutes.
6. Add structured DSMZ 1242 and DSMZ 1033 references and replace stale KNO3/NaNO3 MediaIngredientMech links with CHEBI-keyed links.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml`.
- Fetch DSMZ Medium 1242 and DSMZ Medium 1033 again and compare the regenerated target against both PDFs.
- Search with `rg --no-ignore --hidden 'Mineralsolution 1|Traceelements Solution|MediaIngredientMech:000170|MediaIngredientMech:000171|mediadive.medium:1242|komodo.medium:1242' data/normalized_yaml/bacterial data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml` and confirm the mineral and trace stocks are represented with the correct dilution factors.

## Additional Notes

- Optional organism and growth metric data are absent from the available DSMZ 1242 evidence and were not treated as defects.

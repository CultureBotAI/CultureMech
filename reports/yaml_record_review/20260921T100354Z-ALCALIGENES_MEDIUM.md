# YAML Record Review: ALCALIGENES MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml
- Started UTC: 2026-09-21T10:01:35Z
- Finished UTC: 2026-09-21T10:03:54Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:006238`
- Label: `alcaligenes_medium`
- Original name: `ALCALIGENES MEDIUM`
- Category: `bacterial`
- Media term: `komodo.medium:660`
- Generated status: generated merge of `data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml` and `data/normalized_yaml/bacterial/alcaligenes_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml --out /private/tmp/alcaligenes_medium.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The generated record is a legitimate DSMZ/KOMODO 660 source-duplicate merge for DSMZ Medium 660 / `ALCALIGENES MEDIUM`. The two normalized parents intentionally share the same ingredient signature, and the live DSMZ 660 PDF matches the major basal salts and the post-autoclave CuSO4 and sodium succinate additions.

The trace-element solution was flattened incorrectly before the two parents merged. DSMZ Medium 660 adds 1 ml/L Trace element solution SL-7 to the final medium; SL-7 itself contains HCl 25%, ZnCl2 70 mg/L, MnCl2 x 4 H2O 100 mg/L, H3BO3 60 mg/L, CoCl2 x 6 H2O 200 mg/L, CuCl2 x 2 H2O 20 mg/L, NiCl2 x 6 H2O 20 mg/L, Na2MoO4 x 2 H2O 40 mg/L, and 1000 ml distilled water. The generated target represents those stock rows as final-medium `G_PER_L` rows at stock strength.

## Evidence

Supported:

- The source-duplicate relationship between the KOMODO 660 record and direct DSMZ 660 record is locally coherent.
- Tris 6.06 g/L, NaCl 4.68 g/L, KCl 1.49 g/L, NH4Cl 1.07 g/L, Na2SO4 0.43 g/L, MgCl2 x 6 H2O 0.2 g/L, CaCl2 x 2 H2O 0.03 g/L, Na2HPO4 x 12 H2O 0.23 g/L, and Fe(III)(NH4)citrate 0.005 g/L agree with the live DSMZ PDF.
- CuSO4 0.399025 g/L and sodium succinate 4 g/L are plausible conversions of the source post-autoclave additions, 2.5 ml 1.0 M CuSO4 and 10 ml 40% Na-succinate solution per liter.

Unsupported or over-scoped:

- Trace element solution SL-7 is not represented as a 1 ml/L stock addition.
- Seven SL-7 metal and borate rows are about 1000-fold too concentrated in the final recipe: ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O.
- `HCl` is a 1 ml 25% component of the 1 L SL-7 stock, but the generated target stores `0.25 G_PER_L` as a final ingredient.
- The generated target omits the preparation instruction that CuSO4 and Na-succinate are filter-sterilized and added after autoclaving. That text is present in the direct DSMZ normalized parent but was lost when the generated canonical record copied the KOMODO wrapper.
- The target has no structured `references`, so the DSMZ Medium 660 PDF URL is not checkable by reference validation.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ALCALIGENES_MEDIUM*' -print` searched the ignored timestamped-report directory and found no pre-existing ALCALIGENES report.
- Exact `rg --no-ignore --hidden` searches for `komodo.medium:660\b`, `mediadive.medium:660\b`, `DSMZ Medium 660`, and `KOMODO_660_ALCALIGENES_MEDIUM` covered tracked and ignored files. They found only the KOMODO 660 and DSMZ 660 source-duplicate parents, their generated merge, and index references.
- The DSMZ 660 PDF was fetched live and extracted locally with `mutool`; it confirms the basal formula, 1 ml/L SL-7 stock addition, SL-7 composition, and filter-sterilized post-autoclave CuSO4/Na-succinate additions.

## Findings

### blocker: Trace element solution SL-7 was flattened at stock strength

Only 1 ml/L of SL-7 belongs in the final medium. The generated YAML publishes the SL-7 internal metal/borate salts as direct final ingredients at the stock's mg/L numeric values converted to g/L, making each of those trace salts roughly 1000-fold too concentrated.

### major: the HCl stock component is represented as a final mass concentration

DSMZ lists 1 ml 25% HCl inside the 1000 ml SL-7 stock. The target emits a final `HCl` row at `0.25 G_PER_L`, which has neither the stock dilution nor the source's volume/percent semantics.

### major: post-autoclave filtration instructions were dropped

DSMZ Medium 660 requires adding 2.5 ml 1.0 M CuSO4 and 10 ml of a 40% Na-succinate solution after autoclaving, with both additions sterilized by filtration. The direct DSMZ parent preserved that step, but the generated merge omitted it.

### minor: structured references are absent

Neither normalized parent has a `references` entry for the DSMZ 660 PDF, and the generated target therefore gives `linkml-reference-validator` zero URLs to check.

## Recommended Edits

1. Fix both `data/normalized_yaml/bacterial/alcaligenes_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml`; do not edit the generated merge YAML directly.
2. Represent Trace element solution SL-7 as a stock solution added at 1 ml/L, or scale every SL-7 internal component by the 1:1000 final dilution if the recipe must be flattened.
3. Preserve 25% HCl as a volume/percent stock component instead of `0.25 G_PER_L` final HCl.
4. Preserve the DSMZ post-autoclave, filter-sterilized CuSO4 and sodium succinate preparation step in the canonical generated output.
5. Add structured DSMZ 660 references to both normalized source records.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml`.
- Fetch the DSMZ Medium 660 PDF again and compare the regenerated target against the basal salts, 1 ml/L SL-7 stock addition, and the filtered CuSO4/Na-succinate additions.
- Search with `rg --no-ignore --hidden 'Trace element solution SL|ZnCl2|Na2MoO4|HCl|FILTER' data/normalized_yaml/bacterial data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml` and confirm the trace metals are no longer stock-strength final ingredients and the filtered-addition instruction survives.

## Additional Notes

- Optional pH, organism, and growth metric fields are absent from the available DSMZ 660 evidence and were not treated as defects.

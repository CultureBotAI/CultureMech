# YAML Record Review: acidiphilium_acidophilum_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml
- Started UTC: 2026-09-21T09:13:25Z
- Finished UTC: 2026-09-21T09:15:41Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:000521`
- Label: `acidiphilium_acidophilum_medium`
- Original name: `ACIDIPHILIUM ACIDOPHILUM MEDIUM`
- Category: `bacterial`
- Media term: `mediadive.medium:108` / `DSMZ Medium 108`
- Generated status: generated singleton from `data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml --out /private/tmp/acidiphilium_acidophilum.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target identity is correct: the inspected DSMZ Medium 108 PDF is `ACIDIPHILIUM ACIDOPHILUM MEDIUM`, and the record's `mediadive.medium:108`, label, category, bulk ingredient list, glucose addition instruction, and pH note point to that same DSMZ recipe.

The salts and glucose are grounded to chemically appropriate CHEBI terms:

- `(NH4)2SO4` -> ammonium sulfate
- `KH2PO4` -> potassium dihydrogen phosphate
- `MgSO4 x 7 H2O` -> magnesium sulfate heptahydrate
- `KCl` -> potassium chloride
- `Ca(NO3)2 x 4 H2O` -> calcium nitrate tetrahydrate
- `FeSO4 x 7 H2O` -> iron(2+) sulfate heptahydrate
- `D-Glucose` -> D-glucose
- `Agar` -> agar

The record nevertheless flattens DSMZ's acidified FeSO4 stock and represents DSMZ's liquid and solid forms as a single solid-agar recipe with an optional agar row.

## Evidence

Supported:

- DSMZ Medium 108 source-supports 3 g/L ammonium sulfate, 0.5 g/L KH2PO4, 1 g/L MgSO4 x 7 H2O, 0.1 g/L KCl, 18 mg/L Ca(NO3)2 x 4 H2O, 15 g/L optional agar for solid medium, 10 g/L D-glucose, and 1 L distilled water.
- The target's `ph_value: 4.5` is supported for the solid form after autoclaving.
- The target preparation step preserves both DSMZ pH conditions in prose: pH 3.5 for liquid medium and pH 4.5 for solid medium after autoclaving.
- DSMZ also supports sterilizing glucose separately and adding it to the sterile medium.

Unsupported or over-scoped:

- DSMZ expresses FeSO4 x 7 H2O as `0.01 ml` of a `0.1% w/v in 0.1 N H2SO4` stock. The target stores the arithmetically equivalent 0.00001 g/L FeSO4 x 7 H2O final concentration but loses the 0.1 N H2SO4 stock carrier and the fact that this is a stock-volume addition.
- The singleton generated target is not linked to the KOMODO 108 sibling even though `data/normalized_yaml/bacterial/thiobacillus_acidophilus_medium.yaml` says it was copied from the same DSMZ Medium 108 source under the historical `THIOBACILLUS ACIDOPHILUS MEDIUM` name.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACIDIPHILIUM_ACIDOPHILUM*' -print` searched the ignored timestamped-report directory and found no pre-existing ACIDIPHILIUM ACIDOPHILUM report.
- Exact `rg --no-ignore --hidden` searches for `ACIDIPHILIUM_ACIDOPHILUM`, `acidiphilium_acidophilum`, `mediadive.medium:108`, `komodo.medium:108`, `TOGO:M108`, and `DSMZ_Medium108.pdf` covered `data/merge_yaml`, `data/normalized_yaml`, and the ignored `reports/yaml_record_review` directory. The search found this MediaDive/DSMZ target, a KOMODO 108 DSMZ sibling, and an unrelated JCM/TOGO `M108` record; it did not find another ACIDIPHILIUM ACIDOPHILUM report.
- Optional organism, growth metric, and evidence arrays are absent on the source import; that is not a target-specific defect.

## Findings

### major: acidified FeSO4 stock chemistry is flattened into a final mass row

The inspected DSMZ source adds 0.01 ml of a 0.1% w/v FeSO4 x 7 H2O stock in 0.1 N H2SO4, but `data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml` stores only `FeSO4 x 7 H2O` at `1e-05` `G_PER_L`. The mass conversion is arithmetically plausible, but the stock concentration, 0.1 N sulfuric-acid carrier, and 0.01 ml/L volume are no longer represented. The maintained DSMZ/MediaDive record should either model this as a stock-solution addition or keep a source note proving why the final-mass-only representation is intentionally sufficient.

### major: the DSMZ 108 recipe's liquid and solid variants are collapsed into one solid record

DSMZ Medium 108 explicitly has a liquid-medium pH of 3.5 and a solid-medium pH of 4.5 after autoclaving. The target sets `physical_state: SOLID_AGAR`, keeps agar as an optional ingredient, sets `ph_value: 4.5`, and preserves the liquid pH only as prose. `data/normalized_yaml/bacterial/thiobacillus_acidophilus_medium.yaml` separately imports the same DSMZ Medium 108 family from KOMODO as pH 3.5 under the historical Thiobacillus acidophilus name, but the generated corpus does not connect that sibling to the ACIDIPHILIUM record as a duplicate, source alias, or liquid/solid variant.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml`, model the FeSO4 x 7 H2O addition as a 0.01 ml/L stock addition from a 0.1% w/v FeSO4 x 7 H2O solution in 0.1 N H2SO4, or preserve the stock calculation explicitly in the row notes.
2. Split or annotate DSMZ Medium 108 so the liquid pH 3.5 and solid pH 4.5 agar form are machine-readable variants rather than one solid recipe with liquid-only prose.
3. Reconcile `data/normalized_yaml/bacterial/thiobacillus_acidophilus_medium.yaml` with the DSMZ/MediaDive 108 record. If KOMODO 108 is the same DSMZ recipe under a historical name, make it a duplicate or variant of the Acidiphilium source instead of leaving a disconnected `thiobacillus_acidophilus_medium` singleton.
4. Regenerate `data/merge_yaml/merged/` with `just merge-recipes`.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACIDIPHILIUM_ACIDOPHILUM_MEDIUM.yaml`.
- Reinspect DSMZ Medium 108 and confirm the regenerated output preserves the FeSO4 stock, separate glucose sterilization, liquid pH 3.5, and solid pH 4.5 conditions.
- Search with `rg --no-ignore --hidden 'mediadive\\.medium:108|komodo\\.medium:108' data/merge_yaml data/normalized_yaml` and confirm the MediaDive and KOMODO DSMZ 108 imports are no longer disconnected singletons.

## Additional Notes

- `data/normalized_yaml/bacterial/togo_medium_m108.yaml` is not evidence for this DSMZ recipe. It uses the same `108` number in the TOGO namespace, but its provenance is JCM `GRMD=116` and the formula is potato/glucose/yeast extract rather than DSMZ 108 mineral salts plus glucose.
- The target is a generated singleton today: `merged_from` contains only `acidiphilium_acidophilum_medium`, so the source-fidelity defects are inherited directly from `data/normalized_yaml/bacterial/acidiphilium_acidophilum_medium.yaml`.

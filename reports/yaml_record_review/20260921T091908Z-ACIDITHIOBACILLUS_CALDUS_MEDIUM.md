# YAML Record Review: acidithiobacillus_caldus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml
- Started UTC: 2026-09-21T09:18:05Z
- Finished UTC: 2026-09-21T09:19:10Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:000981`
- Label: `acidithiobacillus_caldus_medium`
- Original name: `ACIDITHIOBACILLUS CALDUS MEDIUM`
- Category: `bacterial`
- Media term: `mediadive.medium:150a` / `DSMZ Medium 150a`
- Generated status: generated merged record from `data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml` and `data/normalized_yaml/bacterial/for_dsm_18786.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml --out /private/tmp/acidithiobacillus_caldus.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target's DSMZ 150a identity is correct: the inspected DSMZ PDF is `ACIDITHIOBACILLUS CALDUS MEDIUM`, pH 2.5, and the generated record points at `mediadive.medium:150a`.

Several source details are not represented correctly:

- DSMZ 150a adds 10 ml of a separately prepared trace-element solution per liter of medium. The record places FeCl3 x 6 H2O, CuSO4 x 5 H2O, H3BO3, MnSO4 x H2O, Na2MoO4 x 2 H2O, CoCl2 x 6 H2O, and ZnSO4 x 7 H2O directly in `ingredients` at their stock-solution concentrations instead of at 1/100 of those values in a nested stock.
- The maintained normalized layer now marks `for_dsm_18786.yaml` as a `PH_VARIANT` of DSMZ Medium 150a with pH 0.8. The generated target still says `for_dsm_18786` is a `SOURCE_DUPLICATE` and lists it in `merged_from`, so the merge output contradicts the current maintained parent/child relationship.

Most direct CHEBI groundings match their labels. `Sulfur` is grounded to `CHEBI:26833` / `sulfur atom`, which is weaker than the source's powdered elemental sulfur but still points at sulfur rather than an unrelated molecule.

## Evidence

Supported:

- DSMZ 150a source-supports the `ACIDITHIOBACILLUS CALDUS MEDIUM` name, pH 2.5, 3 g ammonium sulfate, 0.5 g K2HPO4 x 3 H2O, 0.5 g MgSO4 x 7 H2O, 0.1 g KCl, 0.02 g Ca(NO3)2 x 4 H2O, 5 g powdered sulfur, 1 L distilled water, and the trace-element stock formula.
- DSMZ source-supports the preparation prose about dissolving ingredients except trace elements and sulfur, adjusting to pH 2.5 with 6 N H2SO4, autoclaving, adding filter-sterilized trace elements and sterile sulfur after autoclaving, and sterilizing sulfur by the three-day water-bath process.
- The current maintained normalized records support a parent/child PH_VARIANT relationship from DSMZ 150a to KOMODO 150.1 / `for_dsm_18786`.

Unsupported or over-scoped:

- The target's trace-element rows are over-concentrated by 100x if read as final g/L values. DSMZ gives those masses for a 1 L stock solution and adds only 10 ml/L of that stock to the medium.
- The target's `merged_from` assertion that the pH 0.8 `for_dsm_18786` child is a duplicate of the pH 2.5 parent is contradicted by the maintained `PH_VARIANT` relationship added on 2026-09-13.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACIDITHIOBACILLUS_CALDUS*' -print` searched the ignored timestamped-report directory and found no pre-existing ACIDITHIOBACILLUS CALDUS report.
- Exact `rg --no-ignore --hidden` searches for `ACIDITHIOBACILLUS_CALDUS`, `acidithiobacillus_caldus`, `mediadive.medium:150a`, `komodo.medium:150.1`, `DSMZ_Medium150a`, and `for_dsm_18786` covered `data/merge_yaml`, `data/normalized_yaml`, and the ignored `reports/yaml_record_review` directory. They found the expected DSMZ parent, the KOMODO 150.1 pH child, related generated records, and no earlier ACIDITHIOBACILLUS CALDUS review report.
- Optional organism, growth metric, and evidence arrays are absent on the source import; that is not a target-specific defect.

## Findings

### blocker: DSMZ trace-element stock concentrations were flattened as final ingredient concentrations

DSMZ Medium 150a says to add 10 ml/L trace-element solution after autoclaving, and the FeCl3 x 6 H2O through ZnSO4 x 7 H2O masses are the formula for 1 L of that stock. `data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml` puts those seven stock components directly into the final ingredient list at stock strength, which makes each trace metal 100x too high and loses the filter-sterilized stock addition. The maintained DSMZ parent owns this fix.

### blocker: the generated record merges an explicit pH variant as a duplicate

`data/normalized_yaml/bacterial/for_dsm_18786.yaml` currently reciprocates a `PH_VARIANT` relationship to the DSMZ 150a parent and records `ph_value: 0.8`; `data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml` records that same child under `variant_children`. The generated `ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml` was produced before that semantic repair and still lists `for_dsm_18786` as a `SOURCE_DUPLICATE`, a synonym, and a merged source. Regeneration, and likely a merge rule that excludes explicit variants from duplicate groups, is needed to make `data/merge_yaml/merged/` match `data/normalized_yaml/`.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml`, restore a nested `Trace element solution` containing the seven trace salts at the DSMZ stock concentrations and represent the parent medium's 10 ml/L addition of that stock.
2. Keep sulfur as a post-autoclave sterile powder addition rather than an ordinary fully dissolved direct ingredient, preserving the existing three-day water-bath sterilization instruction.
3. Regenerate `data/merge_yaml/merged/` with `just merge-recipes` after ensuring the merger does not collapse records linked by `PH_VARIANT`.
4. Verify that regenerated `ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml` no longer lists `for_dsm_18786` in `merged_from` and no longer emits it as a synonym.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml`.
- Reinspect DSMZ Medium 150a and confirm that trace-element stock concentrations, the 10 ml/L stock-addition volume, pH 2.5, sulfur sterilization, and post-autoclave additions are represented in the correct maintained fields.
- Search with `rg --no-ignore --hidden 'for_dsm_18786|komodo\\.medium:150\\.1' data/merge_yaml/merged data/normalized_yaml/bacterial` and confirm the KOMODO 150.1 record remains a pH variant rather than a duplicate merge source.

## Additional Notes

- The generated `data/merge_yaml/merged/thiobacillus_caldus_medium.yaml` also cites `mediadive.medium:150a` through KOMODO 150a and inherits the same flattened trace-element stock concentrations; it was not fully reviewed here.
- The generated `ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml` has a 2026-08-06 merge event, while the maintained normalized files have a 2026-09-13 pH-variant repair. This exact target is therefore a clear example where the generated layer is older than a normalized-layer curation event.

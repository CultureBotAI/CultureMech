# YAML Record Review: Alicyclobacillus Ferrooxydans Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALICYCLOBACILLUS_FERROOXYDANS_MEDIUM.yaml
- Started UTC: 2026-09-21T10:15:08Z
- Finished UTC: 2026-09-21T10:18:40Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ALICYCLOBACILLUS_FERROOXYDANS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:003030`
- Label: `alicyclobacillus_ferrooxydans_medium`
- Original name: `ALICYCLOBACILLUS FERROOXYDANS MEDIUM`
- Category: `bacterial`
- Media term: `mediadive.medium:J685`
- Generated status: generated merge of one source record, `data/normalized_yaml/bacterial/JCM_J685_ALICYCLOBACILLUS_FERROOXYDANS_MEDIUM.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALICYCLOBACILLUS_FERROOXYDANS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALICYCLOBACILLUS_FERROOXYDANS_MEDIUM.yaml --out /private/tmp/ALICYCLOBACILLUS_FERROOXYDANS_MEDIUM.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALICYCLOBACILLUS_FERROOXYDANS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALICYCLOBACILLUS_FERROOXYDANS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target denotes the direct JCM Medium 685 import. The current JCM `GRMD=685` page confirms medium 685 is `ALICYCLOBACILLUS FERROOXYDANS MEDIUM`, with Solution A, Solution B, pH 2.5, and optional solid-medium handling.

The generated record is source-identifiable but topologically flattened. JCM puts MgSO4 x 7 H2O, ammonium sulfate, K2HPO4, K2S4O6, KCl, yeast extract, and 1.0 L distilled water in Solution A; separately it puts 20.0 g FeSO4 x 7 H2O in a final 100 ml of 0.2 N H2SO4 as Solution B and calls for 70 ml of Solution B to be added to 1.0 L Solution A. The target instead places Solution A salts and the Solution B ferrous sulfate row in the same top-level ingredient list, omits both distilled water and H2SO4, and records FeSO4 x 7 H2O as `20 G_PER_L`, which is neither the 20 g in 100 ml stock basis nor the 70 ml/L final-medium addition.

The exact ignored-inclusive corpus search found adjacent same-label records:

- `TOGO_M704_Alicyclobacillus_Ferrooxydans_Medium.yaml` is TOGO M704 / `JCM_M685`, points at the same JCM `GRMD=685` URL, and should be a source duplicate of the liquid JCM 685 record after curation.
- `TOGO_M705_Alicyclobacillus_Ferrooxydans_Medium.yaml` is TOGO M705 / `JCM_M685-2`, points at the same JCM page, and captures the solid gellan-gum branch. It should be a solid variant, not merged with the liquid M704 copy.
- `alicyclobacillus_ferrooxydans_medium.yaml` and `KOMODO_1201_ALICYCLOBACILLUS_FERROOXYDANS_medium.yaml` are local DSMZ/KOMODO Medium 1201 siblings with the same label but a distinct `mediadive.medium:1201` / `komodo.medium:1201` identity.

## Evidence

Supported:

- The `mediadive.medium:J685` identity, JCM 685 label, pH 2.5, five defined Solution A salts, yeast extract, distilled-water volume, Solution B recipe, 70 ml/L Solution B addition, and solid-gellan branch are supported by the live JCM `GRMD=685` HTML page.
- MgSO4 x 7 H2O is correctly grounded to magnesium sulfate heptahydrate, ammonium sulfate to `CHEBI:62946`, K2HPO4 to dipotassium hydrogen phosphate, K2S4O6 to potassium tetrathionate, KCl to potassium chloride, and FeSO4 x 7 H2O to iron(2+) sulfate heptahydrate.

Unsupported or over-scoped:

- The target flattens Solution A and Solution B into one top-level list, losing the stock boundary that makes the FeSO4 x 7 H2O amount interpretable.
- Distilled water, the 0.2 N H2SO4 solvent for Solution B, and the H2SO4 used for pH adjustment are not represented.
- The FeSO4 x 7 H2O row is `20 G_PER_L`; the source row is 20.0 g brought to a final 100 ml as Solution B, and only 70 ml of that stock is added per 1.0 L of Solution A.
- The `FILTER_STERILIZE` preparation step has lost the FeSO4 context and now says only to dissolve an unstated material in 0.2 N H2SO4.
- The final preparation step is typed as `AUTOCLAVE` even though it describes post-autoclave addition of filter-sterilized Solution B and, for solid medium, mixing separately autoclaved double-strength Solution A with 1.4% gellan solution before adding Solution B.
- No structured JCM 685 reference is present, so `linkml-reference-validator` performed zero checks.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ALICYCLOBACILLUS_FERROOXYDANS_MEDIUM.md'` searched the ignored timestamped-report directory and found no pre-existing ALICYCLOBACILLUS FERROOXYDANS report.
- Exact `rg --no-ignore --hidden` searches for `mediadive.medium:J685`, `JCM_J685_ALICYCLOBACILLUS_FERROOXYDANS_MEDIUM`, `GRMD=685`, `ALICYCLOBACILLUS FERROOXYDANS MEDIUM`, and `alicyclobacillus_ferrooxydans_medium` covered tracked and ignored files outside `.git`. They found the target direct-JCM generated record, the normalized direct-JCM parent, the DSMZ/KOMODO Medium 1201 sibling pair, the TOGO M704 and M705 copies of JCM 685, import-tracking diagnostics, and the generated sibling outputs.
- The TOGO M704 and TOGO M705 APIs and the JCM `GRMD=685` HTML page were fetched live. TOGO confirms that M704 maps to `JCM_M685` and M705 maps to `JCM_M685-2`; both cite the same source URL, with M705 adding a gellan-gum solution branch for the solid version.
- Exact ignored-inclusive checks for `mediadive.solution:5342`, `mediadive.solution:5343`, `mediadive_5342_Solution_A`, and `mediadive_5343_Solution_B` showed that the TOGO imports' Solution A/B references point at generic reused solution identifiers with unrelated local compositions, not JCM 685-local stocks.

## Findings

### blocker: Solution B stock was flattened into a wrong final FeSO4 concentration

JCM 685 stores FeSO4 x 7 H2O as Solution B: 20.0 g in a final 100 ml of 0.2 N H2SO4, filter-sterilized, with 70 ml added to 1.0 L of Solution A. The generated target drops the 100 ml stock volume, the 0.2 N H2SO4 solvent, and the 70 ml/L addition when it records FeSO4 x 7 H2O as `20 G_PER_L`.

### major: Solution A water and Solution B acid are missing

The JCM page has 1.0 L distilled water in Solution A and 0.2 N H2SO4 as the solvent for Solution B. Neither appears as a structured water, solvent, solution, or pH-adjustment component in the target, so the recipe cannot be reconstructed from the ingredient rows alone.

### major: the M704 duplicate and M705 solid variant are split from the direct JCM 685 import

TOGO M704 is a copy of the same liquid JCM 685 recipe, while TOGO M705 captures the same page's solid gellan-gum branch. Both are generated separately in `data/merge_yaml/merged/alicyclobacillus_ferrooxydans_medium__4d207a4d.yaml`, where M704 and M705 are merged even though M705 has a distinct solid formulation.

### minor: preparation step typing is too coarse

The JCM source has one autoclave phase for Solution A, one filter-sterilization phase for Solution B, and a final aseptic combination/solid-medium pouring phase. The target preserves much of the prose but types the last phase as `AUTOCLAVE`.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/JCM_J685_ALICYCLOBACILLUS_FERROOXYDANS_MEDIUM.yaml`; do not edit `data/merge_yaml/merged/ALICYCLOBACILLUS_FERROOXYDANS_MEDIUM.yaml` directly.
2. Represent JCM 685 Solution A and Solution B as scoped solution structures so the 1.0 L Solution A basis, 20 g per 100 ml Solution B stock, 0.2 N H2SO4 solvent, and 70 ml/L Solution B addition are not flattened into one top-level final `G_PER_L` ingredient list.
3. Preserve the H2SO4 pH-adjustment instruction explicitly instead of dropping H2SO4 from the record.
4. Split the final preparation step into non-autoclave mixing and solid-medium handling after the actual autoclave and filter-sterilization steps.
5. Add a structured JCM 685 source reference.
6. Repair `data/normalized_yaml/bacterial/TOGO_M704_Alicyclobacillus_Ferrooxydans_Medium.yaml` as the TOGO copy of the liquid JCM 685 recipe and `data/normalized_yaml/bacterial/TOGO_M705_Alicyclobacillus_Ferrooxydans_Medium.yaml` as the solid variant; avoid `mediadive.solution:5342` / `mediadive.solution:5343` unless those IDs become JCM 685-local solutions.
7. Regenerate merge YAML and pages, then mark M704 as a source duplicate of the direct JCM 685 import while keeping M705 as a distinct solid variant.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ALICYCLOBACILLUS_FERROOXYDANS_MEDIUM.yaml`.
- Fetch JCM `GRMD=685` and TOGO M704/M705 again and confirm liquid Solution A/B topology, the 0.2 N H2SO4 Solution B solvent, the 70 ml/L Solution B addition, and the M705-only gellan branch all round-trip into the normalized source records.
- Search with `rg --no-ignore --hidden 'mediadive.medium:J685\b|TOGO:M704\b|TOGO:M705\b|mediadive.solution:5342|mediadive.solution:5343' data/normalized_yaml/bacterial data/merge_yaml/merged` and confirm the direct JCM/M704 duplicates and M705 variant no longer point at the unrelated generic Solution A/B records.
- Verify that `data/merge_yaml/merged/alicyclobacillus_ferrooxydans_medium__4d207a4d.yaml` disappears or contains only a correctly distinct solid formulation after the M704/M705 relationship is curated.

## Additional Notes

- The direct JCM 685 source does not name organisms, growth metrics, or incubation temperature; those empty optional slots were not treated as defects.

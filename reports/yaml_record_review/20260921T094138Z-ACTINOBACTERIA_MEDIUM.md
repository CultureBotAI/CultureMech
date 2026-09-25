# YAML Record Review: actinobacteria_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACTINOBACTERIA_MEDIUM.yaml
- Started UTC: 2026-09-21T09:40:17Z
- Finished UTC: 2026-09-21T09:41:38Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACTINOBACTERIA_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:001170`
- Label: `actinobacteria_medium`
- Original name: `ACTINOBACTERIA MEDIUM`
- Category: `bacterial`
- Media term: `mediadive.medium:1688` / `ACTINOBACTERIA MEDIUM`
- Generated status: generated merge from `data/normalized_yaml/bacterial/acidibacter_medium.yaml` and `data/normalized_yaml/bacterial/actinobacteria_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACTINOBACTERIA_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACTINOBACTERIA_MEDIUM.yaml --out /private/tmp/actinobacteria.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACTINOBACTERIA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACTINOBACTERIA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target identity is internally inconsistent. Its identifier and `media_term` say DSMZ Medium 1688 `ACTINOBACTERIA MEDIUM`, but its `synonyms` and `merged_from` collapse DSMZ Medium 1627 `ACIDIBACTER MEDIUM` into the same record. DSMZ 1688 and DSMZ 1627 are different source recipes with different names, medium numbers, pH values, yeast concentrations, Na2SO4 amounts, and water/stock structure.

The generated ingredient list is mostly the Acidibacter source, not Actinobacteria. DSMZ 1688 directly lists 0.150 g/L Na2SO4, 0.450 g/L ammonium sulfate, 0.050 g/L KCl, 0.500 g/L MgSO4 x 7 H2O, 0.050 g/L KH2PO4, 0.015 g/L calcium nitrate tetrahydrate, 0.100 g/L yeast extract, 0.900 g/L glucose, and distilled water to 1000 ml at pH 3.0. DSMZ 1627 instead adds 0.900 g glucose, 0.200 g yeast extract, 20 ml of Salt solution, and 980 ml distilled water at pH 5.0; its six salts are defined inside a 100 ml stock. The generated record carries the 0.200 g/L Acidibacter yeast amount and the DSMZ 1627 stock-strength salt rows under a DSMZ 1688 identity.

## Evidence

Supported:

- Live DSMZ Medium 1688 supports the target's `ACTINOBACTERIA MEDIUM` identity, DSMZ Medium 1688 source, 0.900 g/L glucose, and pH 3.0.
- Live DSMZ Medium 1627 supports the `ACIDIBACTER MEDIUM` synonym and shows why that source has a 20 ml/L Salt solution with a separate 100 ml stock composition.
- The local source set already contains separate `data/normalized_yaml/bacterial/acidibacter_medium.yaml` and `data/normalized_yaml/bacterial/actinobacteria_medium.yaml` records with distinct DSMZ media terms.
- `reports/media_variant_link_proposals.tsv` previously proposed `acidibacter_medium` and `actinobacteria_medium` as a high-confidence `CONCENTRATION_VARIANT`, not as a source duplicate.

Unsupported or over-scoped:

- DSMZ 1688 does not support the generated 0.200 g/L yeast extract; it lists 0.100 g/L.
- DSMZ 1688 does not support final salt concentrations of 3.5 g/L Na2SO4, 22.5 g/L ammonium sulfate, 2.5 g/L KCl, 25 g/L MgSO4 x 7 H2O, 2.5 g/L KH2PO4, or 0.7 g/L calcium nitrate.
- DSMZ 1627 does not support treating those six salts as final medium concentrations; they belong to a 100 ml Salt solution that is added at 20 ml/L.
- DSMZ 1688 does not support `ACIDIBACTER MEDIUM` as a synonym.
- The generated record lost the Acidibacter pH 5.0 preparation note while keeping Acidibacter ingredients.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACTINOBACTERIA*' -print` searched the ignored timestamped-report directory and found no pre-existing ACTINOBACTERIA report.
- Exact `rg --no-ignore --hidden` searches for `mediadive\.medium:1627`, `mediadive\.medium:1688`, `DSMZ Medium: 1627`, `DSMZ Medium: 1688`, `ACIDIBACTER`, `ACTINOBACTERIA`, `acidibacter_medium`, and `actinobacteria_medium` covered tracked and ignored files. They found the two normalized DSMZ parents, the generated target, and earlier variant-link reports that also classified these records as concentration variants.
- Optional organism, growth metric, evidence, and temperature arrays are absent on the source imports; that is not a target-specific defect.

## Findings

### blocker: two distinct DSMZ media are merged as synonyms

`ACTINOBACTERIA_MEDIUM.yaml` merges DSMZ Medium 1627 `ACIDIBACTER MEDIUM` into DSMZ Medium 1688 `ACTINOBACTERIA MEDIUM`. The sources have different medium numbers and different target pH values, and one is a pH 5.0 Acidibacter recipe with a Salt solution while the other is a pH 3.0 Actinobacteria direct recipe. They may be related enough to link as concentration variants, but they are not duplicate names for one generated record.

### blocker: Acidibacter salt-stock concentrations are published under the Actinobacteria identity

The generated ingredient list uses the DSMZ 1627 Salt solution composition as if it were the final medium: 22.5 g/L ammonium sulfate, 25 g/L MgSO4 x 7 H2O, 3.5 g/L Na2SO4, 2.5 g/L KCl, 2.5 g/L KH2PO4, and 0.7 g/L calcium nitrate. DSMZ 1627 adds only 20 ml/L of that stock, and DSMZ 1688 lists separate direct salt amounts. The generated row concentrations therefore match neither final source recipe.

### major: preparation semantics were mixed across parents

The generated record kept the Actinobacteria pH 3.0 adjustment and dropped the Acidibacter pH 5.0 before-autoclave instruction, even though most generated ingredient concentrations are from the Acidibacter import. This is a merge artifact, not a valid hybrid recipe.

## Recommended Edits

1. Remove `acidibacter_medium` from `data/merge_yaml/merged/ACTINOBACTERIA_MEDIUM.yaml` by repairing the normalized variant topology and regenerating the merge output.
2. Keep `data/normalized_yaml/bacterial/actinobacteria_medium.yaml` as a direct DSMZ Medium 1688 record with the DSMZ 1688 direct concentrations and pH 3.0.
3. Repair `data/normalized_yaml/bacterial/acidibacter_medium.yaml` so DSMZ Medium 1627 represents `Salt solution` as a 20 ml/L nested stock rather than stock-strength final salt rows.
4. Preserve DSMZ Medium 1627 as a separate Acidibacter pH 5.0 medium and, if appropriate, link it to ACTINOBACTERIA MEDIUM only as a concentration or source-family variant.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACTINOBACTERIA_MEDIUM.yaml`.
- Re-fetch DSMZ Medium 1688 and confirm the generated record has 0.150 g/L Na2SO4, 0.450 g/L ammonium sulfate, 0.050 g/L KCl, 0.500 g/L MgSO4 x 7 H2O, 0.050 g/L KH2PO4, 0.015 g/L calcium nitrate, 0.100 g/L yeast extract, and pH 3.0.
- Re-fetch DSMZ Medium 1627 and confirm `data/normalized_yaml/bacterial/acidibacter_medium.yaml` has a 20 ml/L Salt solution with the six high-concentration stock rows nested below it.
- Search with `rg --no-ignore --hidden 'acidibacter_medium|mediadive\\.medium:1627|ACIDIBACTER' data/merge_yaml/merged/ACTINOBACTERIA_MEDIUM.yaml` and confirm the Actinobacteria generated record no longer mentions Acidibacter.

## Additional Notes

- No generated `ACIDIBACTER_MEDIUM.yaml` exists after this merge; the Acidibacter source identity is currently available only as a synonym in `ACTINOBACTERIA_MEDIUM.yaml`.

# YAML Record Review: Alicycobacillus Pohliae Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALICYCOBACILLUS_POHLIAE_MEDIUM.yaml
- Started UTC: 2026-09-21T10:21:36Z
- Finished UTC: 2026-09-21T10:23:04Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ALICYCOBACILLUS_POHLIAE_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:003957`
- Label: `alicycobacillus_pohliae_medium`
- Original name: `ALICYCOBACILLUS POHLIAE medium`
- Category: `bacterial`
- Media term: `komodo.medium:1209`
- Generated status: generated merge of two source records, `data/normalized_yaml/bacterial/KOMODO_1209_ALICYCOBACILLUS_POHLIAE_medium.yaml` and `data/normalized_yaml/bacterial/alicycobacillus_pohliae_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALICYCOBACILLUS_POHLIAE_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALICYCOBACILLUS_POHLIAE_MEDIUM.yaml --out /private/tmp/ALICYCOBACILLUS_POHLIAE_MEDIUM.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALICYCOBACILLUS_POHLIAE_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALICYCOBACILLUS_POHLIAE_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target's canonical source is KOMODO Medium 1209, which locally maps to DSMZ Medium 1209. The fetched DSMZ `DSMZ_Medium1209.pdf` confirms medium 1209 is `ALICYCOBACILLUS POHLIAE MEDIUM` with tryptone, D-glucose, ammonium sulfate, FeSO4 x 7 H2O, optional agar, 1000 ml distilled water, and pH 5.5.

The direct DSMZ parent and the KOMODO copy have matching ingredient and concentration signatures, and the exact ignored-inclusive search found no other normalized or generated `mediadive.medium:1209` / `komodo.medium:1209` recipe. The merge itself is therefore a plausible source duplicate merge; the issues are inherited from the two maintained parents.

The DSMZ source itself spells the title as `ALICYCOBACILLUS`, so the record's `Alicycobacillus` label is source-faithful even though the organism name is normally spelled `Alicyclobacillus`.

## Evidence

Supported:

- Tryptone 5 g/L, D-glucose 0.5 g/L, ammonium sulfate 0.1 g/L, FeSO4 x 7 H2O 0.07 g/L, optional agar 15 g/L, 1000 ml distilled water, and pH 5.5 are supported by DSMZ Medium 1209.
- D-glucose, ammonium sulfate, FeSO4 x 7 H2O, and agar are grounded to CHEBI terms matching the source ingredient forms.
- The direct DSMZ and KOMODO 1209 records have the same local composition, pH, physical state, and source cross-reference and are valid source duplicates.

Unsupported or over-scoped:

- DSMZ marks agar as optional with an "if required" parenthetical, but the target is unconditionally typed as `SOLID_AGAR`.
- The 1000 ml distilled-water row in DSMZ Medium 1209 is omitted.
- Tryptone has no primary term or `mediaingredientmech_chebi_term` grounding.
- No structured DSMZ 1209 or KOMODO 1209 reference is present, so `linkml-reference-validator` performed zero checks.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ALICYCOBACILLUS_POHLIAE_MEDIUM.md'` searched the ignored timestamped-report directory and found no pre-existing ALICYCOBACILLUS POHLIAE report.
- Exact `rg --no-ignore --hidden` searches for `mediadive.medium:1209`, `komodo.medium:1209`, `DSMZ Medium: 1209`, `KOMODO_1209_ALICYCOBACILLUS_POHLIAE_medium`, `ALICYCOBACILLUS POHLIAE`, and `alicycobacillus_pohliae_medium` covered `data/normalized_yaml`, `data/merge_yaml`, and `data/import_tracking` while including ignored files. They found only the direct DSMZ parent, the KOMODO 1209 copy, the generated two-source merge, generated indexes, and import-tracking report rows.
- DSMZ Medium 1209 was fetched live and confirmed that no solution nesting or hidden stock medium is needed for this recipe.

## Findings

### major: optional agar is represented as mandatory physical state

DSMZ lists the agar row parenthetically with "if required", so the same base medium can be prepared with or without agar. The generated record includes agar as a normal final ingredient and sets `physical_state: SOLID_AGAR`, erasing the optional liquid form.

### major: the DSMZ water row is missing

DSMZ Medium 1209 explicitly brings the recipe to 1000 ml with distilled water. The generated target omits that row entirely, so the total volume and solvent basis are no longer structured.

### minor: source provenance is only a notes string

The record has a `notes` string naming KOMODO 1209 and DSMZ 1209 but no structured DSMZ or KOMODO reference objects.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/alicycobacillus_pohliae_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_1209_ALICYCOBACILLUS_POHLIAE_medium.yaml`; do not edit `data/merge_yaml/merged/ALICYCOBACILLUS_POHLIAE_MEDIUM.yaml` directly.
2. Represent the agar row as an optional solidifying addition or split the liquid base and solid agar formulation into explicit variants.
3. Restore the 1000 ml distilled-water solvent row.
4. Add a structured DSMZ Medium 1209 reference and, for the KOMODO copy, a structured KOMODO 1209 reference.
5. Leave tryptone unresolved if no exact ontology term is available; otherwise ground it to an exact mixture term rather than a simple peptide or amino-acid proxy.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ALICYCOBACILLUS_POHLIAE_MEDIUM.yaml`.
- Fetch DSMZ Medium 1209 again and confirm the regenerated record preserves the optional agar semantics, 1000 ml water basis, and pH 5.5.
- Search with `rg --no-ignore --hidden 'mediadive.medium:1209\b|komodo.medium:1209\b|ALICYCOBACILLUS_POHLIAE' data/normalized_yaml/bacterial data/merge_yaml/merged` and confirm the DSMZ/KOMODO duplicate pair still merges after both maintained parents are repaired.

## Additional Notes

- Optional target-organism and growth-metric slots were not treated as defects because the inspected DSMZ recipe does not provide strain-specific growth evidence.

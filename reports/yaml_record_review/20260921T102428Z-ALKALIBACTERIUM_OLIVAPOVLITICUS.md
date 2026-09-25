# YAML Record Review: Alkalibacterium Olivapovliticus

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
- Started UTC: 2026-09-21T10:23:05Z
- Finished UTC: 2026-09-21T10:24:28Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:006829`
- Label: `alkalibacterium_olivapovliticus`
- Original name: `ALKALIBACTERIUM OLIVAPOVLITICUS`
- Category: `bacterial`
- Media term: `komodo.medium:923`
- Generated status: generated merge of two source records, `data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml` and `data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml --out /private/tmp/ALKALIBACTERIUM_OLIVAPOVLITICUS.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target's canonical source is KOMODO Medium 923, which locally maps to DSMZ Medium 923. The fetched DSMZ `DSMZ_Medium923.pdf` confirms medium 923 is `ALKALIBACTERIUM OLIVAPOVLITICUS`, with sodium glutamate, yeast extract, Na2CO3, K2HPO4, MgSO4 x 7 H2O, ammonium sulfate, 1000 ml distilled water, and special handling for high-pH Na2CO3 and agar-solidified preparations.

The direct DSMZ parent and the KOMODO copy have matching ingredient and concentration signatures, and the exact ignored-inclusive search found no other normalized or generated `mediadive.medium:923` / `komodo.medium:923` recipe. The merge itself is therefore a plausible source duplicate merge; the issues are inherited from the maintained parents and from the KOMODO record being chosen as the generated canonical record.

## Evidence

Supported:

- Sodium glutamate 10 g/L, yeast extract 5 g/L, sodium carbonate 10 g/L, K2HPO4 0.15 g/L, MgSO4 x 7 H2O 0.025 g/L, ammonium sulfate 1 g/L, and distilled water 1000 ml are supported by DSMZ Medium 923.
- Na glutamate, Na2CO3, K2HPO4, MgSO4 x 7 H2O, ammonium sulfate, and agar are grounded to CHEBI terms matching the supplied forms.
- The direct DSMZ and KOMODO 923 records have the same local formula and source cross-reference and are valid source duplicates.

Unsupported or over-scoped:

- The source mentions agar only in a solidified-media handling note; it is not part of the base ingredient table. The target promotes agar 20 g/L to a normal final ingredient and sets `physical_state: SOLID_AGAR`.
- The 1000 ml distilled-water row in DSMZ Medium 923 is omitted.
- The generated merge drops the DSMZ parent preparation note warning to autoclave Na2CO3 separately for liquid media, to keep agar separate from Na2CO3 for solid media, and to cool components before mixing solid medium.
- No structured DSMZ 923 or KOMODO 923 reference is present, so `linkml-reference-validator` performed zero checks.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ALKALIBACTERIUM_OLIVAPOVLITICUS.md'` searched the ignored timestamped-report directory and found no pre-existing ALKALIBACTERIUM OLIVAPOVLITICUS report.
- Exact `rg --no-ignore --hidden` searches for `mediadive.medium:923`, `komodo.medium:923`, `DSMZ Medium: 923`, `KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS`, `ALKALIBACTERIUM OLIVAPOVLITICUS`, and `alkalibacterium_olivapovliticus` covered `data/normalized_yaml`, `data/merge_yaml`, and `data/import_tracking` while including ignored files. They found only the direct DSMZ parent, the KOMODO 923 copy, the generated two-source merge, generated indexes, and import-tracking report rows.
- DSMZ Medium 923 was fetched live and confirmed that no hidden stock medium or pH value is needed for this recipe.

## Findings

### major: optional agar handling was promoted to mandatory solid medium

DSMZ 923 does not list agar in the base ingredient table; it mentions agar only in a handling note for solidified medium. The target records agar 20 g/L as a normal ingredient and sets `physical_state: SOLID_AGAR`, erasing the liquid preparation.

### major: the separate-autoclave preparation warning was dropped

DSMZ 923 explicitly warns that high pH will drive ammonia loss if Na2CO3 is autoclaved with the other liquid components, and that agar will hydrolyze if it is autoclaved with Na2CO3. The direct DSMZ normalized record still has that warning, but the generated target chose the KOMODO record and lost the preparation step.

### major: the DSMZ water row is missing

DSMZ Medium 923 brings the formula to 1000 ml with distilled water. The generated target omits that row, so the solvent basis is no longer structured.

### minor: source provenance is only a notes string

The record has a `notes` string naming KOMODO 923 and DSMZ 923 but no structured DSMZ or KOMODO reference objects.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml` and `data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml`; do not edit `data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml` directly.
2. Represent agar as an optional 20 g/L solidifying addition or split the base liquid and agar-solidified formulation into explicit variants.
3. Restore the 1000 ml distilled-water solvent row.
4. Preserve the Na2CO3 and agar separate-autoclaving warnings from DSMZ Medium 923 in the KOMODO copy, or ensure the merger keeps the direct DSMZ preparation text when the direct DSMZ record is part of the duplicate set.
5. Add structured DSMZ Medium 923 and KOMODO 923 references.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml`.
- Fetch DSMZ Medium 923 again and confirm the regenerated record preserves the liquid base formula, optional agar semantics, 1000 ml water basis, and separate-autoclaving warnings.
- Search with `rg --no-ignore --hidden 'mediadive.medium:923\b|komodo.medium:923\b|ALKALIBACTERIUM_OLIVAPOVLITICUS' data/normalized_yaml/bacterial data/merge_yaml/merged` and confirm only the repaired DSMZ/KOMODO duplicate pair remains.

## Additional Notes

- Optional target-organism and growth-metric slots were not treated as defects because the inspected DSMZ recipe does not provide strain-specific growth evidence.

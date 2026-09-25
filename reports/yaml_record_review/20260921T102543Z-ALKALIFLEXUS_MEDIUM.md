# YAML Record Review: Alkaliflexus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALKALIFLEXUS_MEDIUM.yaml
- Started UTC: 2026-09-21T10:24:29Z
- Finished UTC: 2026-09-21T10:25:43Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ALKALIFLEXUS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:003895`
- Label: `alkaliflexus_medium`
- Original name: `ALKALIFLEXUS medium`
- Category: `bacterial`
- Media term: `komodo.medium:1175`
- Generated status: generated merge of two source records, `data/normalized_yaml/bacterial/KOMODO_1175_ALKALIFLEXUS_medium.yaml` and `data/normalized_yaml/bacterial/alkaliflexus_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALKALIFLEXUS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALKALIFLEXUS_MEDIUM.yaml --out /private/tmp/ALKALIFLEXUS_MEDIUM.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALKALIFLEXUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALKALIFLEXUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target's canonical source is KOMODO Medium 1175, which locally maps to DSMZ Medium 1175. The fetched DSMZ `DSMZ_Medium1175.pdf` confirms `ALKALIFLEXUS MEDIUM`, the pH 10.0 recipe, carbonate/bicarbonate additions after cooling, nitrogen handling, and sterile anaerobic stock additions of sodium sulfide, cellobiose, and yeast extract.

The direct DSMZ parent and the KOMODO copy have matching ingredient and concentration signatures, and the exact ignored-inclusive search found no other normalized or generated `mediadive.medium:1175` / `komodo.medium:1175` recipe. The merge itself is therefore a plausible source duplicate merge; the issues are inherited from the maintained parents and from the KOMODO record being chosen as the generated canonical record.

## Evidence

Supported:

- NH4Cl 0.2 g/L, MgCl2 x 6 H2O 0.05 g/L, KH2PO4 0.2 g/L, Na2CO3 7.4 g/L, NaHCO3 18.5 g/L, Na2S x 9 H2O 0.5 g/L, yeast extract 0.2 g/L, cellobiose 3 g/L, distilled water 1000 ml, and pH 10.0 are supported by DSMZ Medium 1175.
- All defined ingredients are grounded to CHEBI terms matching the source ingredient forms.
- The direct DSMZ and KOMODO 1175 records have the same local formula, pH, and source cross-reference and are valid source duplicates.

Unsupported or over-scoped:

- The source requires nitrogen handling and sterile anaerobic additions, but the generated target carries KOMODO's `Aerobic: Yes` note and no preparation steps.
- The 1000 ml distilled-water row in DSMZ Medium 1175 is omitted.
- Na2CO3 and NaHCO3 need to be added to the cooled boiled base before dispensing under nitrogen; Na2S x 9 H2O, cellobiose, and yeast extract need to be added from sterile anaerobic stock solutions after autoclaving. Those stock-addition boundaries are missing.
- No structured DSMZ 1175 or KOMODO 1175 reference is present, so `linkml-reference-validator` performed zero checks.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ALKALIFLEXUS_MEDIUM.md'` searched the ignored timestamped-report directory and found no pre-existing ALKALIFLEXUS MEDIUM report.
- Exact `rg --no-ignore --hidden` searches for `mediadive.medium:1175`, `komodo.medium:1175`, `DSMZ Medium: 1175`, `KOMODO_1175_ALKALIFLEXUS_medium`, `ALKALIFLEXUS medium`, and `alkaliflexus_medium` covered `data/normalized_yaml`, `data/merge_yaml`, and `data/import_tracking` while including ignored files. They found only the direct DSMZ parent, the KOMODO 1175 copy, the generated two-source merge, generated indexes, and import-tracking report rows.
- DSMZ Medium 1175 was fetched live and confirmed that no hidden stock-medium formula is needed for this recipe; the post-autoclave additions are defined by stock percentage rather than by separate DSMZ medium numbers.

## Findings

### major: anaerobic preparation was lost and contradicted by KOMODO's aerobic note

DSMZ 1175 says to boil and cool the base under nitrogen, dispense under nitrogen, seal under nitrogen gas, and add sulfide/cellobiose/yeast extract from sterile anaerobic stock solutions. The generated merge is based on the KOMODO copy, keeps a `| Aerobic: Yes` note, and drops the direct DSMZ record's preparation steps.

### major: post-cooling and post-autoclave stock additions are not structured

Na2CO3 and NaHCO3 must be added to the cooled boiled base before autoclaving, while Na2S x 9 H2O, cellobiose, and yeast extract are added from 10%, 5%, and 10% sterile anaerobic stocks after autoclaving. The target stores all of them as ordinary top-level ingredients with no timing, stock concentration, or anaerobic handling.

### major: the DSMZ water row is missing

DSMZ Medium 1175 brings the formula to 1000 ml with distilled water. The generated target omits that row, so the solvent basis is no longer structured.

### minor: source provenance is only a notes string

The record has a `notes` string naming KOMODO 1175 and DSMZ 1175 but no structured DSMZ or KOMODO reference objects.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/alkaliflexus_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_1175_ALKALIFLEXUS_medium.yaml`; do not edit `data/merge_yaml/merged/ALKALIFLEXUS_MEDIUM.yaml` directly.
2. Preserve the DSMZ nitrogen handling and the pre-autoclave carbonate/bicarbonate additions plus post-autoclave sulfide, cellobiose, and yeast-extract stock additions.
3. Remove or correct KOMODO's imported `Aerobic: Yes` assertion for this DSMZ 1175 copy.
4. Restore the 1000 ml distilled-water solvent row.
5. Add structured DSMZ Medium 1175 and KOMODO 1175 references.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ALKALIFLEXUS_MEDIUM.yaml`.
- Fetch DSMZ Medium 1175 again and confirm the regenerated record preserves the pH 10.0 formula, nitrogen handling, carbonate/bicarbonate cooling step, post-autoclave stock additions, and 1000 ml water basis.
- Search with `rg --no-ignore --hidden 'mediadive.medium:1175\b|komodo.medium:1175\b|ALKALIFLEXUS' data/normalized_yaml/bacterial data/merge_yaml/merged` and confirm only the repaired DSMZ/KOMODO duplicate pair remains.

## Additional Notes

- Optional target-organism and growth-metric slots were not treated as defects because the inspected DSMZ recipe does not provide strain-specific growth evidence.

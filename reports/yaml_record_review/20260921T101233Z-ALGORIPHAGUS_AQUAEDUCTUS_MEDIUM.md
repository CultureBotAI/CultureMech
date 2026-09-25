# YAML Record Review: ALGORIPHAGUS AQUAEDUCTUS medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALGORIPHAGUS_AQUAEDUCTUS_MEDIUM.yaml
- Started UTC: 2026-09-21T10:11:07Z
- Finished UTC: 2026-09-21T10:12:33Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ALGORIPHAGUS_AQUAEDUCTUS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:004095`
- Label: `algoriphagus_aquaeductus_medium`
- Original name: `ALGORIPHAGUS AQUAEDUCTUS medium`
- Category: `bacterial`
- Media term: `komodo.medium:1332`
- Generated status: generated merge of `data/normalized_yaml/bacterial/KOMODO_1332_ALGORIPHAGUS_AQUAEDUCTUS_medium.yaml` and `data/normalized_yaml/bacterial/algoriphagus_aquaeductus_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALGORIPHAGUS_AQUAEDUCTUS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALGORIPHAGUS_AQUAEDUCTUS_MEDIUM.yaml --out /private/tmp/algoriphagus_aquaeductus_medium.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALGORIPHAGUS_AQUAEDUCTUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALGORIPHAGUS_AQUAEDUCTUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target is a valid source-duplicate merge of KOMODO 1332 and direct DSMZ 1332. DSMZ Medium 1332 is `ALGORIPHAGUS AQUAEDUCTUS MEDIUM`, gives basal meat extract, NH4Cl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, KH2PO4, 996 ml distilled water, 3 ml/L Seven vitamins solution, and 1 ml/L Trace element solution SL-8. It sets pH 8.0 before autoclaving and says solid medium may be prepared with 15 g/L agar.

The generated target is stale relative to both normalized parents. `apply_cocktail_nesting.py` nested four vitamin rows and FeSO4 x 7 H2O into stock solutions in the normalized files on 2026-08-07, but the generated merge was last emitted on 2026-08-06 and still keeps all vitamin and trace rows at top level.

## Evidence

Supported:

- KOMODO 1332 and DSMZ 1332 are source duplicates.
- Meat extract 20 g/L, NH4Cl 1 g/L, MgSO4 x 7 H2O 0.2 g/L, CaCl2 x 2 H2O 0.01 g/L, KH2PO4 0.5 g/L, pH 8.0, and optional agar 15 g/L are supported by DSMZ 1332.
- DSMZ 1332 supports Trace element solution SL-8 as a 1 ml/L stock and Seven vitamins solution as a 3 ml/L stock.

Unsupported or over-scoped:

- The generated target still has no `solutions`, even though both current normalized parents now contain partial `Seven vitamins solution` and `Trace element solution SL-8` entries.
- Na2-EDTA, CoCl2 x 6 H2O, MnCl2 x 2 H2O, ZnSO4 x 7 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, H3BO3, and CuCl2 x 2 H2O belong in 1 ml/L Trace element solution SL-8, not directly in the final medium at stock strength.
- Vitamin B12, p-aminobenzoic acid, D-(+)-biotin, nicotinic acid, calcium pantothenate, pyridoxine hydrochloride, and thiamine-HCl x 2 H2O belong in 3 ml/L Seven vitamins solution, not directly in the final medium at stock strength.
- The target lacks DSMZ 1332's 996 ml distilled-water row and preparation text for pH 8.0 before autoclaving, pH 6.8 for SL-8, filter sterilization of vitamins, and post-autoclave vitamin addition.
- No structured DSMZ 1332 references are present, so `linkml-reference-validator` performed zero checks.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ALGORIPHAGUS_AQUAEDUCTUS_MEDIUM*' -print` searched the ignored timestamped-report directory and found no pre-existing ALGORIPHAGUS AQUAEDUCTUS report.
- Exact `rg --no-ignore --hidden` searches for `komodo.medium:1332\b`, `mediadive.medium:1332\b`, `DSMZ Medium 1332`, `DSMZ_Medium1332`, `KOMODO_1332_ALGORIPHAGUS_AQUAEDUCTUS_medium`, and `^name: algoriphagus_aquaeductus_medium$` covered tracked and ignored files. They found the KOMODO 1332 and DSMZ 1332 source-duplicate parents, their generated merge, derived index rows, and historical validation/report rows.
- The DSMZ 1332 PDF was fetched live and extracted locally with `mutool`; it confirms the 1 ml/L SL-8 stock, 3 ml/L Seven vitamins stock, 996 ml distilled water row, pH adjustment, and filter-sterile post-autoclave vitamin addition.

## Findings

### blocker: the generated merge is stale and still flattens every SL-8 and vitamin stock row

Both normalized parents were partially repaired by `apply_cocktail_nesting.py` on 2026-08-07, one day after this generated merge was emitted. Regeneration would at least move FeSO4 x 7 H2O into `Trace element solution SL-8` and Vitamin B12, nicotinic acid, pyridoxine hydrochloride, and thiamine-HCl x 2 H2O into `Seven vitamins solution`.

### blocker: stock-solution nesting remains incomplete in both normalized parents

The normalized repair left Na2-EDTA, CoCl2 x 6 H2O, MnCl2 x 2 H2O, ZnSO4 x 7 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, H3BO3, and CuCl2 x 2 H2O as direct ingredients, but all eight are Trace element solution SL-8 rows that DSMZ 1332 adds at only 1 ml/L. The same partial repair left p-aminobenzoic acid, D-(+)-biotin, and calcium pantothenate as direct ingredients, but they belong inside Seven vitamins solution, which DSMZ 1332 adds at 3 ml/L.

### major: DSMZ preparation and water semantics are missing or misclassified

The generated target has no preparation steps, no 996 ml distilled-water row, and no filter-sterile post-autoclave vitamin addition. The direct DSMZ parent still misclassifies `Filter sterilise and add to the medium after it has been autoclaved` as `action: AUTOCLAVE`, so even regeneration after the current normalized YAML would not recover source-faithful preparation semantics.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/KOMODO_1332_ALGORIPHAGUS_AQUAEDUCTUS_medium.yaml` and `data/normalized_yaml/bacterial/algoriphagus_aquaeductus_medium.yaml`; do not edit the generated merge YAML directly.
2. Move every SL-8 component into `Trace element solution SL-8` at 1 ml/L: Na2-EDTA, FeSO4 x 7 H2O, CoCl2 x 6 H2O, MnCl2 x 2 H2O, ZnSO4 x 7 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, H3BO3, and CuCl2 x 2 H2O.
3. Move every vitamin component into `Seven vitamins solution` at 3 ml/L: Vitamin B12, p-aminobenzoic acid, D-(+)-biotin, nicotinic acid, calcium pantothenate, pyridoxine hydrochloride, and thiamine-HCl x 2 H2O.
4. Restore DSMZ 1332's 996 ml distilled-water row and preparation steps, including pH 8.0 before autoclaving, pH 6.8 for SL-8, filter sterilization of the vitamin stock, and post-autoclave vitamin addition.
5. Add a structured DSMZ 1332 reference.
6. Regenerate the merge so the generated record is no longer older than the normalized cocktail repair.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ALGORIPHAGUS_AQUAEDUCTUS_MEDIUM.yaml`.
- Fetch DSMZ Medium 1332 again and compare the regenerated target against its basal rows, Trace element solution SL-8, Seven vitamins solution, and preparation text.
- Search with `rg --no-ignore --hidden 'Trace element solution SL-8|Seven vitamins solution|mediadive.medium:1332|komodo.medium:1332' data/normalized_yaml/bacterial data/merge_yaml/merged/ALGORIPHAGUS_AQUAEDUCTUS_MEDIUM.yaml` and confirm no SL-8 or vitamin stock components remain as final direct ingredients.

## Additional Notes

- The NiCl2 x 6 H2O row is currently grounded to anhydrous `CHEBI:34887` / nickel dichloride and should be audited while the SL-8 stock is repaired.

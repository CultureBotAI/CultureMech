# YAML Record Review: ALCALIPHILIC AMPHIBACILLUS STRAINS medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALCALIPHILIC_AMPHIBACILLUS_STRAINS_MEDIUM.yaml
- Started UTC: 2026-09-21T10:06:19Z
- Finished UTC: 2026-09-21T10:08:27Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ALCALIPHILIC_AMPHIBACILLUS_STRAINS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:006851`
- Label: `alcaliphilic_amphibacillus_strains_medium`
- Original name: `ALCALIPHILIC AMPHIBACILLUS STRAINS medium`
- Category: `bacterial`
- Media term: `komodo.medium:931`
- Generated status: generated merge of `data/normalized_yaml/bacterial/KOMODO_931_ALCALIPHILIC_AMPHIBACILLUS_STRAINS_medium.yaml` and `data/normalized_yaml/bacterial/alcaliphilic_amphibacillus_strains_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALCALIPHILIC_AMPHIBACILLUS_STRAINS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALCALIPHILIC_AMPHIBACILLUS_STRAINS_MEDIUM.yaml --out /private/tmp/alcaliphilic_amphibacillus_strains_medium.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALCALIPHILIC_AMPHIBACILLUS_STRAINS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALCALIPHILIC_AMPHIBACILLUS_STRAINS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target is a valid source-duplicate merge of KOMODO 931 and direct DSMZ 931, both copies of `ALCALIPHILIC AMPHIBACILLUS STRAINS MEDIUM`. The pH range 9.5-10.0 and the direct final rows for KH2PO4, MgCl2, NH4Cl, KCl, Na2CO3, NaHCO3, Na2S x 9 H2O, yeast extract, sucrose, and resazurin match the DSMZ 931 PDF.

The referenced DSMZ 141 stocks were not handled correctly. DSMZ 931 says to add 1 ml/L Trace elements from DSM Medium 141 and 10 ml/L Vitamin solution from DSM Medium 141. DSMZ 141 defines those as Modified Wolin's mineral solution and Wolin's vitamin solution. The generated target flattened the mineral solution at its stock concentrations and omitted every vitamin component.

## Evidence

Supported:

- KOMODO 931 and DSMZ 931 are source duplicates with the same local ingredient signature.
- The basal mineral salts, carbonate/bicarbonate, sulfide, sucrose, yeast extract, resazurin, and pH range are supported by the live DSMZ 931 PDF.
- The flattened MgSO4/MnSO4/NaCl/FeSO4/CoSO4/CaCl2/ZnSO4/CuSO4/AlK(SO4)2/H3BO3/Na2MoO4/NiCl2/Na2SeO3/Na2WO4 rows all occur in DSMZ 141's Modified Wolin mineral stock, not directly in DSMZ 931.

Unsupported or over-scoped:

- The DSMZ 141 mineral-stock components were not diluted by the 1 ml/L final addition, so every stock ingredient is 1000-fold too concentrated.
- Wolin's vitamin solution is absent: the generated record lacks biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium D-(+)-pantothenate, Vitamin B12, p-aminobenzoic acid, and (DL)-alpha-Lipoic acid.
- The target omits DSMZ 931's anaerobic/N2 preparation, post-autoclave stock additions, and filter sterilization of the vitamin solution under N2.
- The merged target copied the KOMODO source, so it omitted the direct DSMZ preparation steps even though the direct DSMZ normalized source carried them.
- No structured DSMZ 931 or DSMZ 141 references are present, so `linkml-reference-validator` performed zero checks.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ALCALIPHILIC_AMPHIBACILLUS_STRAINS_MEDIUM*' -print` searched the ignored timestamped-report directory and found no pre-existing ALCALIPHILIC AMPHIBACILLUS report.
- Exact `rg --no-ignore --hidden` searches for `komodo.medium:931\b`, `mediadive.medium:931\b`, `DSMZ Medium 931`, and `KOMODO_931_ALCALIPHILIC_AMPHIBACILLUS_STRAINS` covered tracked and ignored files. They found only the KOMODO 931 and DSMZ 931 source-duplicate parents, their generated merge, and index references.
- The DSMZ 931 and DSMZ 141 PDFs were fetched live and extracted locally with `mutool`; together they confirm the 1 ml/L Modified Wolin mineral stock, 10 ml/L Wolin vitamin stock, anaerobic preparation text, and vitamin solution formula.

## Findings

### blocker: DSMZ 141 mineral stock was flattened 1000-fold too high

DSMZ 931 adds 1 ml/L of Modified Wolin's mineral solution. The target publishes that stock's salts directly at stock strength, so nitrilotriacetic acid, MgSO4 x 7 H2O, MnSO4 x H2O, NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2 x 12 H2O, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O are all over-concentrated in the final medium.

### blocker: the referenced Wolin vitamin solution is missing

DSMZ 931 requires 10 ml/L of Wolin's vitamin solution from DSMZ 141. None of the ten vitamin rows from that stock are represented in the generated record.

### major: anaerobic post-autoclave preparation was dropped

DSMZ 931 instructs curators to prepare the medium anaerobically under nitrogen, withhold vitamins, sucrose, yeast extract, NH4Cl, Na2CO3, and NaHCO3 initially, add NH4Cl/carbonate/bicarbonate after cooling if the medium was boiled, and add filter-sterilized vitamins plus anaerobic sterile stocks of sucrose, yeast extract, and Na2S x 9 H2O after autoclaving. The generated record has no preparation steps.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/KOMODO_931_ALCALIPHILIC_AMPHIBACILLUS_STRAINS_medium.yaml` and `data/normalized_yaml/bacterial/alcaliphilic_amphibacillus_strains_medium.yaml`; do not edit the generated merge YAML directly.
2. Represent DSMZ 141 Modified Wolin's mineral solution as a 1 ml/L stock addition, or scale each mineral-stock row by 1:1000 if the record must be flattened.
3. Add DSMZ 141 Wolin's vitamin solution as a 10 ml/L stock addition with its biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium D-(+)-pantothenate, Vitamin B12, p-aminobenzoic acid, and (DL)-alpha-Lipoic acid rows.
4. Restore the anaerobic DSMZ 931 preparation steps, including the N2 handling and post-autoclave stock additions.
5. Add structured DSMZ 931 and DSMZ 141 references.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ALCALIPHILIC_AMPHIBACILLUS_STRAINS_MEDIUM.yaml`.
- Fetch DSMZ Medium 931 and DSMZ Medium 141 again and compare the regenerated target against both PDFs.
- Search with `rg --no-ignore --hidden 'Wolin|Biotin|Vitamin B12|Na2WO4|Modified Wolin|anaerobic' data/normalized_yaml/bacterial data/merge_yaml/merged/ALCALIPHILIC_AMPHIBACILLUS_STRAINS_MEDIUM.yaml` and confirm the mineral stock, vitamin stock, and preparation instructions are represented.

## Additional Notes

- Optional organism and growth metric data are absent from the available DSMZ 931 evidence and were not treated as defects.

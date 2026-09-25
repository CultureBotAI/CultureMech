# YAML Record Review: METHANOBACTERIUM THERMOAUTOTROPHICUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_thermoautotrophicum_medium__bf0d1fab.yaml
- Started UTC: 2026-09-24T03:08:12Z
- Finished UTC: 2026-09-24T03:09:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:002592 |
| Label | methanobacterium_thermoautotrophicum_medium |
| Original label | METHANOBACTERIUM THERMOAUTOTROPHICUM MEDIUM |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_thermoautotrophicum_medium__bf0d1fab.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/methanobacterium_thermoautotrophicum_medium.yaml` |
| Merge lineage | `methanobacterium_thermoautotrophicum_medium` |
| Source identity | MediaDive `J231`; JCM Medium 231 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_thermoautotrophicum_medium__bf0d1fab.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_thermoautotrophicum_medium__bf0d1fab.yaml --out /private/tmp/methanobacterium_thermoautotrophicum_medium__bf0d1fab.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_thermoautotrophicum_medium__bf0d1fab.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_thermoautotrophicum_medium__bf0d1fab.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

This generated record is the MediaDive import of JCM Medium 231. The source identity is grounded: MediaDive `J231` and the live JCM page both describe `METHANOBACTERIUM THERMOAUTOTROPHICUM MEDIUM` with the same main formula, pH 7.2, a 10 ml trace-vitamin addition, a 10 ml trace-element addition, and a 980 ml water base.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `mediadive.medium:J231`, `TOGO:M224`, `JCM_M231`, and `GRMD=231` found the expected MediaDive J231 owner and generated file plus the duplicate TOGO M224 owner and generated file. A same-name KOMODO `131` owner also exists, but it is a repaired archived DSMZ formulation and has different reductant amounts, so it should not be forced into this JCM 231 source duplicate.

## Evidence

MediaDive `J231` keeps a 1000 ml main solution plus two 10 ml stock additions: trace vitamins `3861` and trace element solution `3909`. The trace-element solution is prepared separately by dissolving EDTA x 2Na first in 500 ml water, adding the remaining salts, and adjusting to 1000 ml.

The generated record has no `solutions` array and flattens both stocks into final-medium ingredients. Trace-element solution `3909` contains Na2-EDTA, MgSO4 x 7 H2O, MnSO4 x n H2O, NaCl, FeSO4 x 7 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2 x 12 H2O, H3BO3, Na2MoO4 x 2 H2O, and NiCl2 x 6 H2O; every stock member appears as a top-level final ingredient.

Stock-local grams per liter were added directly to main-medium grams per liter for repeated salts. The source main medium contains 0.6 g/L NaCl, 0.12 g/L MgSO4 x 7 H2O, 0.08 g/L CaCl2 x 2 H2O, and 0.004 g/L FeSO4 x 7 H2O before adding 10 ml trace-element stock, but the generated record publishes `1.6 G_PER_L`, `6.32 G_PER_L`, `0.21000000000000002 G_PER_L`, and `0.10400000000000001 G_PER_L`.

The stock-only trace salts are also 100-fold too high for a 10 ml/L stock addition. For example, the generated record stores Na2-EDTA `0.64 G_PER_L`, MnSO4 `0.55 G_PER_L`, CoCl2 x 6 H2O `0.17 G_PER_L`, and ZnSO4 x 7 H2O `0.18 G_PER_L`; those are one-liter stock amounts from solution `3909`, not final-medium concentrations.

Trace vitamins `3861` were flattened the same way. MediaDive stores the vitamin stock as 2 mg/L biotin, 2 mg/L folic acid, 10 mg/L pyridoxine hydrochloride, 5 mg/L thiamine HCl, 5 mg/L riboflavin, 5 mg/L nicotinic acid, 5 mg/L calcium pantothenate, 0.1 mg/L vitamin B12, 5 mg/L p-Aminobenzoic acid, and 5 mg/L lipoic acid, with 10 ml added to the final medium. The generated recipe copies those stock g/L values directly as final ingredients.

The trace-element stock preparation has been promoted to a second top-level preparation step. It should be scoped to solution `3909`; as written, the generated recipe makes the stock's "adjust volume to 1000 ml" instruction look like another main-medium operation.

## Completeness

The empty optional organism-target and growth-evidence slots were not treated as defects. JCM 231 and MediaDive J231 are formulation sources, not primary growth studies.

This record has good source coverage for the MediaDive formulation, pH, anaerobic handling text, and the two stock recipes. The missing structure is the defect: preserving the two stock additions would avoid the inflated final concentrations and the duplicate summation of NaCl, MgSO4, CaCl2, and FeSO4.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The trace-element stock was flattened into final-medium ingredients. | MediaDive main solution `3908` adds 10 ml of solution `3909`; the generated record has no `solutions` array and publishes all 13 solution `3909` members as top-level `ingredients`. | `data/normalized_yaml/archaea/methanobacterium_thermoautotrophicum_medium.yaml` |
| blocker | Main-medium salts were summed with undiluted trace-element stock concentrations. | The source has main NaCl 0.6 g/L, MgSO4 x 7 H2O 0.12 g/L, CaCl2 x 2 H2O 0.08 g/L, and FeSO4 x 7 H2O 0.004 g/L plus 10 ml/L stock; the generated values are 1.6, 6.32, 0.21000000000000002, and 0.10400000000000001 g/L. | `data/normalized_yaml/archaea/methanobacterium_thermoautotrophicum_medium.yaml` |
| blocker | The trace-vitamin stock was flattened at stock strength. | MediaDive main solution `3908` adds 10 ml of vitamin solution `3861`; biotin 0.002 g/L, folic acid 0.002 g/L, pyridoxine hydrochloride 0.01 g/L, thiamine HCl 0.005 g/L, riboflavin 0.005 g/L, nicotinic acid 0.005 g/L, calcium pantothenate 0.005 g/L, vitamin B12 0.0001 g/L, p-Aminobenzoic acid 0.005 g/L, and lipoic acid 0.005 g/L are stock values copied into the final ingredient list. | `data/normalized_yaml/archaea/methanobacterium_thermoautotrophicum_medium.yaml` |
| major | The trace-element stock preparation is scoped as a main-medium step. | The "Dissolve EDTA x 2Na first in 500 ml..." instruction prepares solution `3909`, not the final medium, but it appears as `preparation_steps[1]` on the generated recipe. | MediaDive stock importer for `data/normalized_yaml/archaea/methanobacterium_thermoautotrophicum_medium.yaml` |
| minor | The generated MediaDive and TOGO imports of the same JCM 231 source remain separate generated records. | `mediadive.medium:J231` and `TOGO:M224` both point at JCM `GRMD=231`; exact hidden/ignored search found both owners and their generated files. | De-duplication between MediaDive and TOGO JCM imports. |

## Recommended Edits

1. Restore trace element solution `3909` and trace vitamins `3861` as structured stock additions used at 10 ml/L.
2. Keep every trace-element and trace-vitamin concentration inside the correct stock, not as a top-level final ingredient.
3. Stop summing undiluted trace-stock NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and FeSO4 x 7 H2O with the main-medium rows.
4. Scope the EDTA-first dissolution instruction to the trace-element stock.
5. Reconcile the corrected MediaDive J231 and TOGO M224 records as source duplicates, while keeping KOMODO 131 separate unless an explicit DSMZ-vs-JCM equivalence decision is curated.
6. Regenerate `data/merge_yaml/merged/methanobacterium_thermoautotrophicum_medium__bf0d1fab.yaml` from the corrected normalized owner.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected normalized owner and regenerated merged file.
2. Compare the regenerated MediaDive record against MediaDive `J231` to confirm solutions `3861` and `3909` remain structured 10 ml/L additions.
3. Compare final NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and FeSO4 x 7 H2O values against the source main recipe and the 10 ml/L trace-element addition to confirm stock values were not added undiluted.
4. Re-run exact searches for `mediadive.medium:J231`, `TOGO:M224`, `JCM_M231`, and `GRMD=231` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.

## Additional Notes

None found.

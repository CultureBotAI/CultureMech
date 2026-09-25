# YAML Record Review: AZOSPIRILLUM_AMAZONENSE_MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AZOSPIRILLUM_AMAZONENSE_MEDIUM.yaml
- Started UTC: 2026-09-21T17:00:05Z
- Finished UTC: 2026-09-21T17:01:28Z
- Verdict: needs curation

## Target

| Field | Observed |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:005068 |
| name | azospirillum_amazonense_medium |
| original_name | AZOSPIRILLUM AMAZONENSE MEDIUM |
| category | bacterial |
| media_term | komodo.medium:352, AZOSPIRILLUM AMAZONENSE MEDIUM |
| generated status | Generated merge artifact in data/merge_yaml/merged |
| maintained owners | data/normalized_yaml/bacterial/KOMODO_352_AZOSPIRILLUM_AMAZONENSE_MEDIUM.yaml and data/normalized_yaml/bacterial/azospirillum_amazonense_medium.yaml |

The target is the generated merge for two source-duplicate records,
`KOMODO_352_AZOSPIRILLUM_AMAZONENSE_MEDIUM` and
`azospirillum_amazonense_medium`, with merge fingerprint
`f36c7e6d01d11abc5bf48d72447d5eb8a5b6f3a3b38b216cfe8e5b2c5fd3affa`.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AZOSPIRILLUM_AMAZONENSE_MEDIUM.yaml` completed with no errors. |
| Strict validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AZOSPIRILLUM_AMAZONENSE_MEDIUM.yaml --out /private/tmp/AZOSPIRILLUM_AMAZONENSE_MEDIUM.strict.tsv --workers 1 --quiet` completed with no errors. |
| Reference validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AZOSPIRILLUM_AMAZONENSE_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 checks. |
| Term validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AZOSPIRILLUM_AMAZONENSE_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed with no errors, aside from a non-fatal `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused embedded `MediaRecipe.curation_history` validator for one merge record. |
| Direct `just` validators | Not checked: the project-level `uv` environment currently fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13, with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project LinkML validator workaround above exercised the target schema, strict, reference, and term checks. |

## Identity and Grounding

- The record identity is supported. The KOMODO record explicitly maps to DSMZ Medium 352, and the sibling `data/normalized_yaml/bacterial/azospirillum_amazonense_medium.yaml` owner directly cites the live DSMZ Medium 352 PDF titled `AZOSPIRILLUM AMAZONENSE MEDIUM`.
- The source-duplicate merge is sound at the identity level. Both maintained owners have the same DSMZ Medium 352 salts and concentrations, and their `SOURCE_DUPLICATE` relationship is appropriate.
- `SOLID_AGAR`, `DEFINED`, and pH 6.0 agree with DSMZ Medium 352.

## Evidence

Supported by inspected source text:

- DSMZ Medium 352 lists K2HPO4 0.200 g/L, KH2PO4 0.600 g/L, CaCl2 x 2 H2O 0.020 g/L, MgSO4 x 7 H2O 0.200 g/L, Na2MoO4 x 2 H2O 0.002 g/L, FeCl3 0.010 g/L, sucrose 5.000 g/L, agar 1.750 g/L, and distilled water 1000.000 ml.
- DSMZ Medium 352 adds 5.000 ml of bromothymol blue prepared as 0.5% in 0.2 N KOH.
- DSMZ Medium 352 says to adjust pH to 6.0.

Unsupported or incomplete claims:

- Both maintained owners and the generated merge omit the 1000 ml distilled-water row.
- The 5 ml bromothymol-blue-in-KOH stock is represented only as `0.025 G_PER_L` direct bromothymol blue. That amount is arithmetically compatible with 5 ml of a 0.5% stock, but the 0.2 N KOH stock solvent and the 5 ml/L solution boundary are not represented.
- The generated merge selected the KOMODO record as canonical and thereby dropped the explicit `preparation_steps` entry from the DSMZ owner. `ph_value: 6.0` is still present, so this is a traceability loss rather than a missing condition.

## Completeness

- Source provenance is enough to recover the original formulation: the KOMODO owner cites DSMZ Medium 352 indirectly, and the DSMZ owner names the exact PDF URL.
- Empty organism/growth slots are acceptable for this source recipe. DSMZ Medium 352 establishes the medium recipe and does not assert growth for a specific strain in the inspected PDF.
- Gitignore-independent search covered `data/normalized_yaml`, `data/merge_yaml`, `reports/yaml_record_review`, `history`, and `.claude` for `DSMZ_Medium352`, `mediadive.medium:352`, `KOMODO Medium 352`, `DSMZ Medium 352`, `AZOSPIRILLUM_AMAZONENSE`, `Azospirillum Amazonense`, `azospirillum_amazonense`, and `Azospirillum amazonense`; no prior Markdown report for this exact uppercase generated record was found.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The source water row is missing. | DSMZ Medium 352 uses 1000 ml distilled water; neither normalized owner nor the generated merge contains a water ingredient. | `data/normalized_yaml/bacterial/azospirillum_amazonense_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_352_AZOSPIRILLUM_AMAZONENSE_MEDIUM.yaml`. |
| Major | The bromothymol-blue stock boundary is flattened away. | DSMZ Medium 352 adds 5 ml of 0.5% bromothymol blue in 0.2 N KOH; the generated record keeps only the equivalent bromothymol blue mass and omits the KOH-containing stock solution. | Both normalized owners or the DSMZ/KOMODO importer. |
| Minor | The duplicate merge drops the one-step pH preparation instruction from the DSMZ owner. | The DSMZ owner has `Adjust pH to 6.0.` as a preparation step; the generated canonical copy keeps `ph_value: 6.0` but loses the preparation step. | `merge_recipes.py` duplicate field reconciliation. |

## Recommended Edits

1. Add `Distilled water` at 1000 ml/L to both DSMZ Medium 352 owners.
2. Represent `Bromothymol blue (0.5% in 0.2N KOH)` as a 5 ml/L stock solution rather than a bare final bromothymol-blue mass.
3. Preserve the pH 6.0 adjustment through the source-duplicate merge when regenerating `data/merge_yaml/merged/AZOSPIRILLUM_AMAZONENSE_MEDIUM.yaml`.

## Follow-up Checks

- `just validate-strict data/normalized_yaml/bacterial/azospirillum_amazonense_medium.yaml` and `just validate-strict data/normalized_yaml/bacterial/KOMODO_352_AZOSPIRILLUM_AMAZONENSE_MEDIUM.yaml` after the maintained source duplicates are repaired.
- `just validate-terms` on any explicit bromothymol-blue/KOH stock solution.
- `just verify-merges` after regenerating the merge layer.
- Manual comparison with DSMZ Medium 352 to verify the regenerated merge has the water row, 5 ml/L bromothymol-blue stock, and pH 6.0.

## Additional Notes

- The same file stem appears in `azospirillum_amazonense_medium__911e8407.yaml`, but that target is a separate TOGO/NBRC M1186 formulation and was not judged here.
- `linkml-reference-validator` performed zero checks because this generated record has no `references` block.

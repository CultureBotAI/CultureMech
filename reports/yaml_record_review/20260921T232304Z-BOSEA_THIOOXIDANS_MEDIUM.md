# YAML Record Review: BOSEA THIOOXIDANS medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml
- Started UTC: 2026-09-21T23:23:04Z
- Finished UTC: 2026-09-21T23:23:46Z
- Verdict: needs curation

## Target

- Reviewed generated merged record `data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml`.
- Target class: `MediaRecipe`
- Stable ID: `CultureMech:006418`
- Name and source label: `bosea_thiooxidans_medium` / `BOSEA THIOOXIDANS medium`
- Source grounding: `komodo.medium:763`, with source duplicate parent `mediadive.medium:763`
- Maintained owners: `data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml` and `data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml`
- Merge status: two-source merge from `KOMODO_763_BOSEA_THIOOXIDANS_medium` and `bosea_thiooxidans_medium` with fingerprint `1ba558cba7a7702a0621de64e18c25e510c068884195611d9d106694ba4be61d`

This is a derived Layer 4 source-duplicate merge. Future formulation fixes belong in both normalized DSMZ/KOMODO 763 owners, followed by merge regeneration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml --out /private/tmp/BOSEA_THIOOXIDANS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator found 0 record-level reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BOSEA_THIOOXIDANS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the only output was the known `pkg_resources` warning from `eutils`. |
| Embedded `curation_history` | Not checked: this repository documents `just validate-history` for standalone history files, and no focused embedded `MediaRecipe.curation_history` validator is exposed for one merged record. |

The direct `just validate-schema`, `just validate-strict`, and `just validate-terms` wrappers were not rerun for this one-record report because the project environment currently fails while trying to build `llvmlite==0.46.0` under Python 3.13. The table above uses the same focused validators through an offline Python 3.11 no-project environment.

## Identity and Grounding

- DSMZ Medium 763 is BOSEA THIOOXIDANS MEDIUM, and the generated KOMODO/DSMZ source-duplicate merge correctly points to KOMODO/DSMZ medium number 763.
- A gitignore-independent exact search for `komodo.medium:763`, `mediadive.medium:763`, `DSMZ Medium: 763`, `CultureMech:006418`, `CultureMech:001896`, fingerprint `1ba558cba7a7702a0621de64e18c25e510c068884195611d9d106694ba4be61d`, `KOMODO_763_BOSEA`, `BOSEA THIOOXIDANS`, and `bosea_thiooxidans_medium` covered `data`, `src`, and `scripts`. It found exactly the two maintained source owners for DSMZ/KOMODO 763, the generated merge and indexes, and import diagnostics.
- The source-duplicate relation is structurally coherent: the KOMODO owner points to the DSMZ owner with `relationship: SOURCE_DUPLICATE`, and both owners carry the same DSMZ 763 ingredient signature.

## Evidence

The inspected DSMZ 763 PDF supports most current ingredients:

- Na2HPO4 4.0 g/L, KH2PO4 1.5 g/L, MgCl2 0.1 g/L, Na-glutamate 0.5 g/L, yeast extract 0.1 g/L, Na2S2O3 x 5 H2O 5.0 g/L, Na-succinate 5.0 g/L, and final pH 7.5-8.5 all agree with the source.
- `composition_type: SEMI_DEFINED` is appropriate because the record contains yeast extract alongside chemically defined salts and carbon sources.

The maintained inputs and generated merge are still missing supported source details:

- DSMZ 763 lists 1000 ml distilled water; neither normalized owner nor the generated merge represents water.
- Neither normalized owner has a structured `references` entry for DSMZ Medium 763, so the reference validator had no URL to check.

## Completeness

- Required schema shape is complete enough to validate, but the formulation is incomplete without the 1000 ml distilled water row.
- Empty optional sterilization and temperature fields are acceptable; the inspected DSMZ 763 PDF does not provide those details.
- Empty optional organism growth evidence is acceptable for this source recipe; the DSMZ PDF provides a formulation, not strain-level growth tests.
- No duplicate active owner beyond the intended KOMODO/DSMZ source-duplicate pair was found by the exact, gitignore-independent search over `data`, `src`, and `scripts` described above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Both DSMZ/KOMODO 763 normalized owners omit source-listed distilled water. | DSMZ Medium 763 lists `Distilled water 1000.0 ml`; the generated merge and both normalized source owners have no water component. | `data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml`. |
| Minor | DSMZ 763 is only present as a URL embedded in `notes`. | The maintained records have no `references` entry for `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium763.pdf`, which leaves record-level reference validation with 0 checks. | Both normalized DSMZ/KOMODO 763 owners. |

## Recommended Edits

1. Add the DSMZ-listed 1000 ml distilled water row to both normalized source-duplicate owners.
2. Add a structured DSMZ 763 reference to both normalized owners.
3. Regenerate the merged corpus after both maintained inputs are corrected.

## Follow-up Checks

- Rerun focused open-schema, strict, term, and reference validators on both normalized owners after curation.
- Confirm the regenerated merge contains a 1000 ml/L water row in addition to the seven existing DSMZ ingredients.
- Run `just verify-merges` and `just audit-merge-freshness` after merge regeneration.
- Re-run the exact ignored-file-inclusive search for `komodo.medium:763`, `mediadive.medium:763`, `DSMZ Medium: 763`, `CultureMech:006418`, `CultureMech:001896`, fingerprint `1ba558cba7a7702a0621de64e18c25e510c068884195611d9d106694ba4be61d`, and `bosea_thiooxidans_medium` under `data`, `src`, and `scripts` after regeneration to confirm there are still exactly two active normalized owners for this source duplicate.

## Additional Notes

- The exact gitignore-independent search included ignored files and found no active BOSEA THIOOXIDANS owner beyond the KOMODO/DSMZ 763 pair.
- The KOMODO note `Aerobic: No` was not independently checked against a live KOMODO page; the source formulation was verified against DSMZ Medium 763.

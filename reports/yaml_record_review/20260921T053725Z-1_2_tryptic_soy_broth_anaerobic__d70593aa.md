# YAML Record Review: 1_2_tryptic_soy_broth_anaerobic

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml`
- Started UTC: 20260921T053659Z
- Finished UTC: 20260921T053725Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:015334` |
| Slug | `1_2_tryptic_soy_broth_anaerobic` |
| Original name | `1/2 TRYPTIC SOY BROTH (ANAEROBIC)` |
| Category | `specialized` |
| Generated or maintained | Generated merge artifact |
| Maintained owner | `data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml` |
| Source accession | `mediadive.medium:1205`, DSMZ Medium 1205 |
| Merge fingerprint | `d70593aa17440d537b1df96c6780f81b531b01b19cd3e172156803bb605b30d7` |

Reviewed the singleton generated merge for MediaDive/DSMZ Medium 1205. A gitignore-independent exact search for `CultureMech:015334`, `mediadive.medium:1205`, and the merge fingerprint found only this generated record, its normalized owner, catalog/index rows, historical aggregate reports, the direct DSMZ inventory entry, the filename-collision report for bacterial and specialized `1_2_tryptic_soy_broth_anaerobic.yaml`, and prior review notes on the KOMODO and TOGO imports of the same DSMZ recipe.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml` | Passed with no output |
| Strict validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml --out /private/tmp/1_2_tryptic_soy_broth_anaerobic__d70593aa.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 `ERROR` rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `curation_history` | Not checked | Not checked: no focused validator is documented for generated merge-file `MediaRecipe.curation_history`; the repository's `validate-history` target validates standalone history files under `history/`. |

The documented `just` validator wrappers remain blocked by the project `llvmlite==0.46.0` build under Python 3.13; the no-project `uv` commands above were used as focused equivalents.

## Identity and Grounding

- The record correctly denotes DSMZ Medium 1205, `1/2 TRYPTIC SOY BROTH (ANAEROBIC)`.
- The inspected DSMZ Medium 1205 PDF lists Trypticase soy broth 13.75 g, yeast extract 1.00 g, NaCl 2.50 g, D-glucose 3.60 g, DL-Dithiothreitol 0.15 g, and distilled water 1000.00 ml.
- The generated record correctly preserves the five non-water DSMZ ingredient rows and pH 7.2.
- The generated record omits DSMZ's 1000 ml distilled-water row.
- The anaerobic preparation step is compressed into one `AUTOCLAVE` action, but it preserves the material source sequence: dissolve ingredients except glucose and DTT, sparge with 100% N2 for 30 to 45 min, adjust pH to 7.2 with HCl, dispense under N2 into anoxic Hungate-type tubes or serum vials, autoclave at 121 C for 20 min, and add filter-sterilized glucose and DTT stocks under N2.
- `Trypticase soy broth` is reasonably ungrounded: the packaged label index includes the exact label as `UNMAPPED_0252` and no approved CHEBI/MICRO identifier.

## Evidence

- The inspected DSMZ 1205 PDF supports the five represented ingredient rows, the missing distilled-water row, pH 7.2, and the represented anaerobic preparation details.
- `src/culturemech/data/mediaingredientmech/label_index.csv` maps `Yeast extract` to `FOODON:03315426`, but the ingredient is still ungrounded.
- A gitignore-independent exact search over the normalized owner and generated record found no top-level `references` or `reference` entries; the DSMZ URL is preserved only as free text in `notes`.
- A gitignore-independent exact search for sibling DSMZ Medium 1205 accessions found the TOGO M2766 import and the KOMODO 1205 import as separate generated records that do not list this direct MediaDive owner in `merged_from`.

## Completeness

- Consequential gap: the 1000 ml water row is missing.
- Consequential gap: DSMZ Medium 1205 is split across at least three generated records: this direct MediaDive record, TOGO M2766, and KOMODO 1205.
- Non-blocking grounding gap: Yeast extract has an exact packaged mapping but lacks a primary `term`.
- Non-blocking provenance gap: the record has no structured DSMZ reference, so focused reference validation has no source object to traverse.
- The record has no target-organism evidence; that is acceptable because the inspected DSMZ recipe page makes no organism-specific growth claim.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Distilled water is missing. | DSMZ Medium 1205 lists 1000.00 ml distilled water; the normalized owner has no water row. | `data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml` |
| Major | DSMZ Medium 1205 exists as separate KOMODO and TOGO generated records. | `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobe.yaml` and `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml` both point at DSMZ Medium 1205, but neither is listed in this generated record's `merged_from`. | Duplicate reconciliation across the MediaDive, TOGO, and KOMODO DSMZ 1205 owners |
| Minor | The DSMZ source is not represented as a structured reference. | The DSMZ URL appears only in top-level `notes`, so reference validation performed 0 checks. | `data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml` |
| Minor | Yeast extract is ungrounded even though an exact mapping exists. | The packaged label index maps `Yeast extract` to `FOODON:03315426`; the ingredient has no primary `term`. | `data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml` |

## Recommended Edits

1. Add the DSMZ `Distilled water` row to `data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml` as `1000 ML_PER_L`.
2. Ground `Yeast extract` to `FOODON:03315426`.
3. Add a structured reference for `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1205.pdf`.
4. Reconcile this direct DSMZ owner with the TOGO M2766 and KOMODO 1205 imports so merge generation emits one DSMZ Medium 1205 recipe.

## Follow-up Checks

- Re-run strict, term, and reference validation for `data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml`.
- Re-run merge generation and verify `data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml` carries the water row and structured DSMZ reference.
- Re-run merge generation and verify the MediaDive, TOGO, and KOMODO DSMZ-1205 owners either merge together or have a documented source-level reason to remain separate.

## Additional Notes

- The previous two reports cover the sibling KOMODO and TOGO DSMZ 1205 imports; those two normalized owners need more extensive formulation cleanup before they can collapse onto this direct DSMZ representation.

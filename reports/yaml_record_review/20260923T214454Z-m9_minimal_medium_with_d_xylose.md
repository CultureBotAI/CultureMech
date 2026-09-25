# YAML Record Review: m9_minimal_medium_with_d_xylose

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/m9_minimal_medium_with_d_xylose.yaml
- Started UTC: 2026-09-23T21:44:09Z
- Finished UTC: 2026-09-23T21:45:29Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:007422` for `M9 minimal medium with d-xylose`.

| Field | Value |
|---|---|
| Generated path | `data/merge_yaml/merged/m9_minimal_medium_with_d_xylose.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/m9_minimal_medium_with_d_xylose.yaml` |
| Category | `bacterial` |
| Type | `DEFINED` |
| Composition | `DEFINED` |
| Physical state | `LIQUID` |
| Source medium | `MEDIADB:74`, `M9 minimal medium with d-xylose` |
| Merge fingerprint | `cdc3109a1a5fcc1ea1ea70b93f72f22965a88790a6d01b1ff2efe5d56b2d887e` |

The generated merge contains one maintained source record, `m9_minimal_medium_with_d_xylose.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/m9_minimal_medium_with_d_xylose.yaml` | Passed; no issues reported. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/m9_minimal_medium_with_d_xylose.yaml --out /private/tmp/m9_minimal_medium_with_d_xylose.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/m9_minimal_medium_with_d_xylose.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/m9_minimal_medium_with_d_xylose.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | `just validate-history` | Not checked: this project validator checks standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record identity is coherent. `CultureMech:007422`, normalized name `m9_minimal_medium_with_d_xylose`, original name `M9 minimal medium with d-xylose`, and `media_term` `MEDIADB:74` all identify MediaDB medium 74.

MediaDB medium 74 names `M9 minimal medium with d-xylose`, marks it as minimal, lists seven compounds, links MediaDB source 17, and links growth data row 148 for *Klebsiella pneumoniae* on the same medium. The MediaDB text endpoint supports the seven YAML ingredient names and millimolar concentrations: D-xylose 13.0, calcium chloride anhydrous 0.1, dibasic sodium phosphate 49.0, sodium chloride 8.6, potassium dihydrogen phosphate 22.0, magnesium sulfate 2.0, and ammonium chloride 19.0.

The narrow source provenance is incomplete. MediaDB source 17 resolves to Liao et al. 2011, PubMed `21296962`, DOI `10.1128/JB.01218-10`, but the record only carries a generic MediaDB note and a `curation_history` note for Mazumdar et al. 2014.

An ignored-file-inclusive exact search of `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:007422`, `m9_minimal_medium_with_d_xylose`, `MEDIADB:74`, and the merge fingerprint found only the maintained owner, this generated record, generated indexes, and historical validation reports; no duplicate record was found in that bounded scope.

## Evidence

The seven ingredient names and concentrations are supported by MediaDB medium 74.

Two source cross-references need curator review: the MediaDB text endpoint links `D-Xylose` to CHEBI `15936,53455` while the YAML records `CHEBI:65327`, and MediaDB links `Magnesium sulfate` to CHEBI `31795` while the YAML records `CHEBI:32599`. The local term validator accepts the YAML terms, but the imported record does not preserve these source CHEBI cross-references.

The defined, liquid, minimal, and bacterial filing is plausible for this M9 *Klebsiella* medium and is not contradicted by MediaDB 74, which marks the medium as minimal. The `applications` values remain broad inherited MediaDB import boilerplate rather than exact claims from source 17.

The record is missing the narrow source that supports this formulation. MediaDB points medium 74 to Liao et al. 2011 via source 17; Mazumdar et al. 2014 documents the MediaDB database, not this specific M9 xylose formulation.

The three preparation steps are unsupported by inspected MediaDB evidence. MediaDB 74 supplies ingredient rows and source/growth metadata, but the reviewed pages did not supply instructions to dissolve all ingredients in distilled water, adjust pH only if specified in the original formulation, or filter sterilize through a 0.22 um filter.

## Completeness

The ingredient list is complete relative to MediaDB medium 74 by names and concentrations, subject to resolving the D-xylose and magnesium sulfate CHEBI cross-reference mismatches.

The record is incomplete for recoverable source provenance because it lacks a structured reference for MediaDB source 17, PMID `21296962`, and DOI `10.1128/JB.01218-10`.

The record is incomplete for organism support. MediaDB exposes growth data row 148 for *Klebsiella pneumoniae* on `M9 minimal medium with d-xylose` with growth rate 0.481 1/h, temperature 37.0 C, and D-xylose uptake rate 6.006 mmol/gDW/h, but the YAML has no `target_organisms` entry or equivalent structured growth assertion.

Optional solution slots, discussion fields, and strain subfields are correctly absent for this simple MediaDB ingredient import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | MediaDB's organism growth row is omitted. | MediaDB growth data 148 records *Klebsiella pneumoniae* growth on `M9 minimal medium with d-xylose` with growth rate, temperature, and D-xylose uptake metadata, but the YAML carries no structured target organism or uptake claim. | `data/normalized_yaml/bacterial/m9_minimal_medium_with_d_xylose.yaml` |
| Major | The imported MediaDB preparation protocol is unsupported and may over-prescribe filtration. | Inspected MediaDB pages for medium 74 expose the formula, source, and growth row, but not a three-step protocol requiring distilled water, conditional pH adjustment, or 0.22 um filtration. The same boilerplate is produced for MediaDB imports, so the likely durable fix belongs in the importer. | `src/culturemech/import/mediadb_importer.py`; then regenerate `data/normalized_yaml/bacterial/m9_minimal_medium_with_d_xylose.yaml` |
| Minor | Some source ingredient cross-references are changed during import/enrichment. | MediaDB's tabular export for medium 74 lists D-xylose with CHEBI `15936,53455` and magnesium sulfate with CHEBI `31795`; the YAML uses `CHEBI:65327` and `CHEBI:32599`. | `data/normalized_yaml/bacterial/m9_minimal_medium_with_d_xylose.yaml` |
| Minor | Source provenance points to the MediaDB publication instead of the narrow formula source. | MediaDB source 17 identifies Liao et al. 2011 with PubMed `21296962` and DOI `10.1128/JB.01218-10`; the normalized record only names MediaDB and Mazumdar et al. 2014. | `data/normalized_yaml/bacterial/m9_minimal_medium_with_d_xylose.yaml` |

## Recommended Edits

1. Add the MediaDB 148 *Klebsiella pneumoniae* growth observation, including 0.481 1/h, 37.0 C, and 6.006 mmol/gDW/h D-xylose uptake metadata, to `data/normalized_yaml/bacterial/m9_minimal_medium_with_d_xylose.yaml`.
2. Remove unsupported generic preparation steps from this record, or change `src/culturemech/import/mediadb_importer.py` so MediaDB imports do not emit a synthetic filtration and pH-adjustment protocol when MediaDB has no recipe text supporting those steps.
3. Check whether the D-xylose and magnesium sulfate ingredients should preserve their MediaDB CHEBI cross-references or use the normalized CHEBI IDs, then document the decision in `data/normalized_yaml/bacterial/m9_minimal_medium_with_d_xylose.yaml`.
4. Add structured narrow source provenance for MediaDB source 17, PubMed `21296962`, and DOI `10.1128/JB.01218-10` in `data/normalized_yaml/bacterial/m9_minimal_medium_with_d_xylose.yaml`.
5. Regenerate `data/merge_yaml/merged/m9_minimal_medium_with_d_xylose.yaml` after normalized curation rather than editing the generated file directly.

## Follow-up Checks

Run these after future curation:

1. `just validate-schema data/merge_yaml/merged/m9_minimal_medium_with_d_xylose.yaml` or the focused `linkml-validate` command above.
2. `python scripts/validate_strict.py data/merge_yaml/merged/m9_minimal_medium_with_d_xylose.yaml --out /tmp/m9_minimal_medium_with_d_xylose.strict.tsv --workers 1 --quiet`.
3. `linkml-reference-validator validate data data/merge_yaml/merged/m9_minimal_medium_with_d_xylose.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`.
4. `linkml-term-validator validate-data data/merge_yaml/merged/m9_minimal_medium_with_d_xylose.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`.
5. Manually re-open MediaDB medium 74, MediaDB text 74, MediaDB source 17, MediaDB growth data 148, and PubMed `21296962` to confirm the regenerated YAML still preserves the formula and the added source and growth metadata.

## Additional Notes

No record edits were made during this read-only review. The generated file should stay derived from `data/normalized_yaml/bacterial/m9_minimal_medium_with_d_xylose.yaml`.

# YAML Record Review: m9_minimal_medium_with_myo_inositol

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/m9_minimal_medium_with_myo_inositol.yaml
- Started UTC: 2026-09-23T21:45:48Z
- Finished UTC: 2026-09-23T21:46:35Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:007429` for `M9 minimal medium with myo-inositol`.

| Field | Value |
|---|---|
| Generated path | `data/merge_yaml/merged/m9_minimal_medium_with_myo_inositol.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/m9_minimal_medium_with_myo_inositol.yaml` |
| Category | `bacterial` |
| Type | `DEFINED` |
| Composition | `DEFINED` |
| Physical state | `LIQUID` |
| Source medium | `MEDIADB:80`, `M9 minimal medium with myo-inositol` |
| Merge fingerprint | `23ad91e069e4a6655149e651586db2cf4f0cb1f4f35a2b388ce1d009738c4961` |

The generated merge contains one maintained source record, `m9_minimal_medium_with_myo_inositol.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/m9_minimal_medium_with_myo_inositol.yaml` | Passed; no issues reported. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/m9_minimal_medium_with_myo_inositol.yaml --out /private/tmp/m9_minimal_medium_with_myo_inositol.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/m9_minimal_medium_with_myo_inositol.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/m9_minimal_medium_with_myo_inositol.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | `just validate-history` | Not checked: this project validator checks standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record identity is coherent. `CultureMech:007429`, normalized name `m9_minimal_medium_with_myo_inositol`, original name `M9 minimal medium with myo-inositol`, and `media_term` `MEDIADB:80` all identify MediaDB medium 80.

MediaDB medium 80 names `M9 minimal medium with myo-inositol`, marks it as minimal, lists seven compounds, links MediaDB source 17, and links growth data rows 191 and 192 for *Klebsiella pneumoniae* on the same medium. The MediaDB text endpoint supports the seven YAML ingredient names and millimolar concentrations: myo-inositol 11.0, calcium chloride anhydrous 0.1, dibasic sodium phosphate 49.0, sodium chloride 8.6, potassium dihydrogen phosphate 22.0, magnesium sulfate 2.0, and ammonium chloride 19.0.

The narrow source provenance is incomplete. MediaDB source 17 resolves to Liao et al. 2011, PubMed `21296962`, DOI `10.1128/JB.01218-10`, but the record only carries a generic MediaDB note and a `curation_history` note for Mazumdar et al. 2014.

An ignored-file-inclusive exact search of `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:007429`, `m9_minimal_medium_with_myo_inositol`, `MEDIADB:80`, and the merge fingerprint found only the maintained owner, this generated record, generated indexes, and historical validation reports; no duplicate record was found in that bounded scope.

## Evidence

The seven ingredient names and concentrations are supported by MediaDB medium 80.

One source cross-reference needs curator review: the MediaDB text endpoint links `Magnesium sulfate` to CHEBI `31795`, while the YAML records `CHEBI:32599`. The local term validator accepts `CHEBI:32599` as magnesium sulfate, but the imported record does not preserve the source CHEBI cross-reference.

The defined, liquid, minimal, and bacterial filing is plausible for this M9 *Klebsiella* medium and is not contradicted by MediaDB 80, which marks the medium as minimal. The `applications` values remain broad inherited MediaDB import boilerplate rather than exact claims from source 17.

The record is missing the narrow source that supports this formulation. MediaDB points medium 80 to Liao et al. 2011 via source 17; Mazumdar et al. 2014 documents the MediaDB database, not this specific M9 myo-inositol formulation.

The three preparation steps are unsupported by inspected MediaDB evidence. MediaDB 80 supplies ingredient rows and source/growth metadata, but the reviewed pages did not supply instructions to dissolve all ingredients in distilled water, adjust pH only if specified in the original formulation, or filter sterilize through a 0.22 um filter.

## Completeness

The ingredient list is complete relative to MediaDB medium 80 by names and concentrations, subject to resolving the magnesium sulfate CHEBI cross-reference mismatch.

The record is incomplete for recoverable source provenance because it lacks a structured reference for MediaDB source 17, PMID `21296962`, and DOI `10.1128/JB.01218-10`.

The record is incomplete for organism support. MediaDB exposes growth rows 191 and 192 for *Klebsiella pneumoniae* on `M9 minimal medium with myo-inositol`; row 191 has growth rate 0.57 1/h, 37.0 C, and myo-inositol uptake 13.802 mmol/gDW/h, while row 192 is an adaptive growth observation with rate 0.76 1/h and myo-inositol uptake 11.024 mmol/gDW/h. The YAML has no `target_organisms` entry or equivalent structured growth assertion for either row.

Optional solution slots, discussion fields, and strain subfields are correctly absent for this simple MediaDB ingredient import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | MediaDB's organism growth rows are omitted. | MediaDB growth data 191 and 192 record distinct *Klebsiella pneumoniae* growth observations, including an adaptive-growth row, but the YAML carries no structured target organism or uptake claim. | `data/normalized_yaml/bacterial/m9_minimal_medium_with_myo_inositol.yaml` |
| Major | The imported MediaDB preparation protocol is unsupported and may over-prescribe filtration. | Inspected MediaDB pages for medium 80 expose the formula, source, and growth rows, but not a three-step protocol requiring distilled water, conditional pH adjustment, or 0.22 um filtration. The same boilerplate is produced for MediaDB imports, so the likely durable fix belongs in the importer. | `src/culturemech/import/mediadb_importer.py`; then regenerate `data/normalized_yaml/bacterial/m9_minimal_medium_with_myo_inositol.yaml` |
| Minor | The magnesium sulfate source cross-reference changed during import/enrichment. | MediaDB's tabular export for medium 80 lists `Magnesium sulfate` with CHEBI `31795`; the YAML uses `CHEBI:32599`. | `data/normalized_yaml/bacterial/m9_minimal_medium_with_myo_inositol.yaml` |
| Minor | Source provenance points to the MediaDB publication instead of the narrow formula source. | MediaDB source 17 identifies Liao et al. 2011 with PubMed `21296962` and DOI `10.1128/JB.01218-10`; the normalized record only names MediaDB and Mazumdar et al. 2014. | `data/normalized_yaml/bacterial/m9_minimal_medium_with_myo_inositol.yaml` |

## Recommended Edits

1. Add MediaDB growth rows 191 and 192 for *Klebsiella pneumoniae*, including growth rates, 37.0 C, myo-inositol uptake rates, and the adaptive-growth note for row 192, to `data/normalized_yaml/bacterial/m9_minimal_medium_with_myo_inositol.yaml`.
2. Remove unsupported generic preparation steps from this record, or change `src/culturemech/import/mediadb_importer.py` so MediaDB imports do not emit a synthetic filtration and pH-adjustment protocol when MediaDB has no recipe text supporting those steps.
3. Check whether the magnesium sulfate ingredient should preserve the MediaDB CHEBI `31795` cross-reference or use the normalized generic `CHEBI:32599`, then document the decision in `data/normalized_yaml/bacterial/m9_minimal_medium_with_myo_inositol.yaml`.
4. Add structured narrow source provenance for MediaDB source 17, PubMed `21296962`, and DOI `10.1128/JB.01218-10` in `data/normalized_yaml/bacterial/m9_minimal_medium_with_myo_inositol.yaml`.
5. Regenerate `data/merge_yaml/merged/m9_minimal_medium_with_myo_inositol.yaml` after normalized curation rather than editing the generated file directly.

## Follow-up Checks

Run these after future curation:

1. `just validate-schema data/merge_yaml/merged/m9_minimal_medium_with_myo_inositol.yaml` or the focused `linkml-validate` command above.
2. `python scripts/validate_strict.py data/merge_yaml/merged/m9_minimal_medium_with_myo_inositol.yaml --out /tmp/m9_minimal_medium_with_myo_inositol.strict.tsv --workers 1 --quiet`.
3. `linkml-reference-validator validate data data/merge_yaml/merged/m9_minimal_medium_with_myo_inositol.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`.
4. `linkml-term-validator validate-data data/merge_yaml/merged/m9_minimal_medium_with_myo_inositol.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`.
5. Manually re-open MediaDB medium 80, MediaDB text 80, MediaDB source 17, MediaDB growth data 191 and 192, and PubMed `21296962` to confirm the regenerated YAML still preserves the formula and the added source and growth metadata.

## Additional Notes

No record edits were made during this read-only review. The generated file should stay derived from `data/normalized_yaml/bacterial/m9_minimal_medium_with_myo_inositol.yaml`.

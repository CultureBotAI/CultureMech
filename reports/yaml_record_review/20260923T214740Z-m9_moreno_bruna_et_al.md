# YAML Record Review: m9_moreno_bruna_et_al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml
- Started UTC: 2026-09-23T21:46:55Z
- Finished UTC: 2026-09-23T21:48:24Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:007178` for `M9; moreno-bruna et al`.

| Field | Value |
|---|---|
| Generated path | `data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/m9_moreno_bruna_et_al.yaml` |
| Category | `bacterial` |
| Type | `DEFINED` |
| Composition | `DEFINED` |
| Physical state | `LIQUID` |
| Source medium | `MEDIADB:278`, `M9; moreno-bruna et al` |
| Merge fingerprint | `e41f0d1c85b99645ef526d4ad7206edc8bff902616fc9cff8d976bb43941a6db` |

The generated merge contains one maintained source record, `m9_moreno_bruna_et_al.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml` | Passed; no issues reported. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml --out /private/tmp/m9_moreno_bruna_et_al.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | `just validate-history` | Not checked: this project validator checks standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record identity is coherent. `CultureMech:007178`, normalized name `m9_moreno_bruna_et_al`, original name `M9; moreno-bruna et al`, and `media_term` `MEDIADB:278` all identify MediaDB medium 278.

MediaDB medium 278 names `M9; moreno-bruna et al`, marks it as minimal, lists seven compounds, links MediaDB source 71, and links growth data rows 594, 595, 596, and 597 for *Escherichia coli* BL21-derived strains on the same medium. The MediaDB text endpoint supports the seven YAML ingredient names and millimolar concentrations: beta-D-glucose 50.0, calcium chloride anhydrous 0.1, dibasic sodium phosphate 96.0, sodium chloride 15.0, potassium dihydrogen phosphate 44.0, magnesium sulfate 2.0, and ammonium chloride 35.0.

The generated record is stale relative to its maintained owner. The generated YAML leaves beta-D-glucose ungrounded, while `data/normalized_yaml/bacterial/m9_moreno_bruna_et_al.yaml` already contains an `apply_mim_groundings.py` curation event and grounds beta-D-glucose to `CHEBI:15903`, the same CHEBI cross-reference exposed by MediaDB.

The narrow source provenance is incomplete. MediaDB source 71 resolves to Moreno-Bruna et al. 2001, PubMed `11416161`, DOI `10.1073/pnas.131214098`, but the record only carries a generic MediaDB note and a `curation_history` note for Mazumdar et al. 2014.

An ignored-file-inclusive exact search of `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:007178`, `m9_moreno_bruna_et_al`, `MEDIADB:278`, and the merge fingerprint found only the maintained owner, this generated record, generated indexes, and historical validation reports; no duplicate record was found in that bounded scope.

## Evidence

The seven ingredient names and concentrations are supported by MediaDB medium 278.

One source cross-reference needs curator review: the MediaDB text endpoint links `Magnesium sulfate` to CHEBI `31795`, while the YAML records `CHEBI:32599`. The local term validator accepts `CHEBI:32599` as magnesium sulfate, but the imported record does not preserve the source CHEBI cross-reference.

The defined, liquid, minimal, and bacterial filing is plausible for this M9 *E. coli* medium and is not contradicted by MediaDB 278, which marks the medium as minimal. The `applications` values remain broad inherited MediaDB import boilerplate rather than exact claims from source 71.

The record is missing the narrow source that supports this formulation. MediaDB points medium 278 to Moreno-Bruna et al. 2001 via source 71; Mazumdar et al. 2014 documents the MediaDB database, not this specific M9 formulation.

The three preparation steps are unsupported by inspected MediaDB evidence. MediaDB 278 supplies ingredient rows and source/growth metadata, but the reviewed pages did not supply instructions to dissolve all ingredients in distilled water, adjust pH only if specified in the original formulation, or filter sterilize through a 0.22 um filter.

## Completeness

The ingredient list is complete relative to MediaDB medium 278 by names and concentrations. Regeneration is still needed to carry the maintained beta-D-glucose term into merged YAML.

The record is incomplete for recoverable source provenance because it lacks a structured reference for MediaDB source 71, PMID `11416161`, and DOI `10.1073/pnas.131214098`.

The record is incomplete for organism support. MediaDB exposes four growth rows for this medium: 594 for *Escherichia coli* BL21(DE3), 595 for BL21[pET-ASPP], 596 for BL21[pET-28b(+)], and 597 for BL21_aspP-. All four include 37.0 C and distinct growth rates, but the YAML has no `target_organisms` entry or equivalent structured growth assertion for any row.

Optional solution slots, discussion fields, and uptake/secretion fields are correctly absent for this simple MediaDB ingredient import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated record is stale and still leaves beta-D-glucose ungrounded. | MediaDB 278 lists CHEBI `15903` for `beta-D-Glucose`, and `data/normalized_yaml/bacterial/m9_moreno_bruna_et_al.yaml` already adopted `CHEBI:15903`, but `data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml` has no term on the beta-D-glucose row. | Regenerate `data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml` from `data/normalized_yaml/bacterial/m9_moreno_bruna_et_al.yaml` |
| Major | MediaDB's organism growth rows are omitted. | MediaDB growth data 594, 595, 596, and 597 record four BL21-derived growth observations for this medium, but the YAML carries no structured target organism or growth-condition claim. | `data/normalized_yaml/bacterial/m9_moreno_bruna_et_al.yaml` |
| Major | The imported MediaDB preparation protocol is unsupported and may over-prescribe filtration. | Inspected MediaDB pages for medium 278 expose the formula, source, and growth rows, but not a three-step protocol requiring distilled water, conditional pH adjustment, or 0.22 um filtration. The same boilerplate is produced for MediaDB imports, so the likely durable fix belongs in the importer. | `src/culturemech/import/mediadb_importer.py`; then regenerate `data/normalized_yaml/bacterial/m9_moreno_bruna_et_al.yaml` |
| Minor | The magnesium sulfate source cross-reference changed during import/enrichment. | MediaDB's tabular export for medium 278 lists `Magnesium sulfate` with CHEBI `31795`; the YAML uses `CHEBI:32599`. | `data/normalized_yaml/bacterial/m9_moreno_bruna_et_al.yaml` |
| Minor | Source provenance points to the MediaDB publication instead of the narrow formula source. | MediaDB source 71 identifies Moreno-Bruna et al. 2001 with PubMed `11416161` and DOI `10.1073/pnas.131214098`; the normalized record only names MediaDB and Mazumdar et al. 2014. | `data/normalized_yaml/bacterial/m9_moreno_bruna_et_al.yaml` |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml` from the current `data/normalized_yaml/bacterial/m9_moreno_bruna_et_al.yaml` so beta-D-glucose carries `CHEBI:15903`.
2. Add MediaDB growth rows 594, 595, 596, and 597 to `data/normalized_yaml/bacterial/m9_moreno_bruna_et_al.yaml`, including their strain-specific organism labels, 37.0 C, and growth rates.
3. Remove unsupported generic preparation steps from this record, or change `src/culturemech/import/mediadb_importer.py` so MediaDB imports do not emit a synthetic filtration and pH-adjustment protocol when MediaDB has no recipe text supporting those steps.
4. Check whether the magnesium sulfate ingredient should preserve the MediaDB CHEBI `31795` cross-reference or use the normalized generic `CHEBI:32599`, then document the decision in `data/normalized_yaml/bacterial/m9_moreno_bruna_et_al.yaml`.
5. Add structured narrow source provenance for MediaDB source 71, PubMed `11416161`, and DOI `10.1073/pnas.131214098` in `data/normalized_yaml/bacterial/m9_moreno_bruna_et_al.yaml`.

## Follow-up Checks

Run these after future curation:

1. Re-open `data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml` and confirm beta-D-glucose carries `CHEBI:15903`.
2. `just validate-schema data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml` or the focused `linkml-validate` command above.
3. `python scripts/validate_strict.py data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml --out /tmp/m9_moreno_bruna_et_al.strict.tsv --workers 1 --quiet`.
4. `linkml-reference-validator validate data data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`.
5. `linkml-term-validator validate-data data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`.
6. Manually re-open MediaDB medium 278, MediaDB text 278, MediaDB source 71, MediaDB growth data 594 through 597, and PubMed `11416161` to confirm the regenerated YAML preserves the formula and the added source and growth metadata.

## Additional Notes

No record edits were made during this read-only review. The generated file should stay derived from `data/normalized_yaml/bacterial/m9_moreno_bruna_et_al.yaml`; a direct patch to `data/merge_yaml/merged/m9_moreno_bruna_et_al.yaml` would be overwritten.

# YAML Record Review: m9_medium_fischer_et_al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/m9_medium_fischer_et_al.yaml
- Started UTC: 2026-09-23T21:42:15Z
- Finished UTC: 2026-09-23T21:43:54Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:007037` for `M9 medium; Fischer et al`.

| Field | Value |
|---|---|
| Generated path | `data/merge_yaml/merged/m9_medium_fischer_et_al.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml` |
| Category | `bacterial` |
| Type | `DEFINED` |
| Composition | `DEFINED` |
| Physical state | `LIQUID` |
| Source medium | `MEDIADB:147`, `M9 medium; fischer et al` |
| Merge fingerprint | `4ea888e13fbdb1b00fc100c3ef044c6c003f4c597075e69e4b2eeba2958e7ad1` |

The generated merge contains one maintained source record, `m9_medium_fischer_et_al.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/m9_medium_fischer_et_al.yaml` | Passed; no issues reported. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/m9_medium_fischer_et_al.yaml --out /private/tmp/m9_medium_fischer_et_al.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/m9_medium_fischer_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/m9_medium_fischer_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | `just validate-history` | Not checked: this project validator checks standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record identity is coherent. `CultureMech:007037`, normalized name `m9_medium_fischer_et_al`, original name `M9 medium; Fischer et al`, and `media_term` `MEDIADB:147` all identify MediaDB medium 147.

MediaDB medium 147 names `M9 medium; fischer et al`, marks it as minimal, lists 14 compounds, links MediaDB source 49, and links ten growth data rows for this medium. The MediaDB text endpoint supports the 14 ingredient names and concentrations in the maintained owner: D-glucose 16.6518 mM, calcium chloride anhydrous 0.1 mM, dibasic sodium phosphate 52.9727 mM, sodium chloride 8.55578 mM, thiamine HCl 0.0033132 mM, potassium dihydrogen phosphate 22.0449 mM, magnesium sulfate 2.0 mM, manganese sulfate 0.00709975 mM, ammonium chloride 14.9558 mM, cobalt chloride 0.00756525 mM, zinc sulfate 0.00626022 mM, cupric chloride 0.00703894 mM, Iron(III) chloride 0.616722 mM, and sodium EDTA 0.597736 mM.

The generated record is stale relative to its maintained owner. The generated YAML still has the iron chloride ingredient as `"'Iron(III"`, while `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml` already contains a `repair_mediadb_names.py` history entry and restores the ingredient to `Iron(III) chloride`.

The narrow source provenance is incomplete. MediaDB source 49 resolves to Fischer et al. 2003, PubMed `12603321`, DOI `10.1046/j.1432-1033.2003.03448.x`, but the record only carries a generic MediaDB note and a `curation_history` note for Mazumdar et al. 2014.

An ignored-file-inclusive exact search of `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:007037`, `m9_medium_fischer_et_al`, `MEDIADB:147`, and the merge fingerprint found only the maintained owner, this generated record, generated indexes, and historical validation reports; no duplicate record was found in that bounded scope.

## Evidence

The generated formula is not fully source-supported because the iron chloride row is truncated to `"'Iron(III"`. MediaDB medium 147 and the normalized owner both show that ingredient should be `Iron(III) chloride`.

The other 13 ingredient names and all 14 concentrations are supported by MediaDB medium 147.

Several ontology cross-references need curator review. MediaDB links `Magnesium sulfate` to CHEBI `31795`, while the YAML records `CHEBI:32599`; MediaDB supplies no CHEBI for `Manganese sulfate`, while the YAML records the monohydrate-specific `CHEBI:86364`; MediaDB supplies CHEBI `30808` for `Iron(III) chloride` and CHEBI `64734` for `Sodium EDTA`, while the YAML lacks terms for both rows.

The defined, liquid, and bacterial filing is plausible for this M9 bacterial medium and is not contradicted by MediaDB 147, which marks the medium as minimal. The `applications` values remain broad inherited MediaDB import boilerplate rather than exact claims from source 49.

The three preparation steps are unsupported by inspected MediaDB evidence. MediaDB 147 supplies ingredient rows and source/growth metadata, but the reviewed pages did not supply instructions to dissolve all ingredients in distilled water, adjust pH only if specified in the original formulation, or filter sterilize through a 0.22 um filter.

## Completeness

The generated ingredient list is incomplete relative to MediaDB medium 147 until it is regenerated from the repaired maintained owner.

The record is incomplete for recoverable source provenance because it lacks a structured reference for MediaDB source 49, PMID `12603321`, and DOI `10.1046/j.1432-1033.2003.03448.x`.

The record is incomplete for organism support. MediaDB exposes ten growth data rows for this medium, but the YAML has no `target_organisms` entries or equivalent structured growth assertions. The omitted rows are 299 for *Escherichia coli* MG1655, 300 for W3110, 301 for JM101, 302 for K-10_Zwf-, 303 for W3110_Pgi-, 304 for K-10_PfkA-, 305 for JM101_PykAF-, 306 for K-12_Mae-_Pck-, 307 for MG1655_SdhA-_Mdh-, and 308 for K-12_FumA-.

Optional solution slots and discussion fields are correctly absent for this simple MediaDB ingredient import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated record is stale and still has a truncated iron chloride ingredient. | MediaDB 147 lists `Iron(III) chloride`, and `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml` already repaired the row, but `data/merge_yaml/merged/m9_medium_fischer_et_al.yaml` still says `"'Iron(III"`. | Regenerate `data/merge_yaml/merged/m9_medium_fischer_et_al.yaml` from `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml` |
| Major | The manganese sulfate term is over-specific. | MediaDB medium 147 lists `Manganese sulfate` and gives no CHEBI cross-reference; the YAML maps the ingredient to `CHEBI:86364`, manganese(II) sulfate monohydrate, without inspected source support for the monohydrate form. | `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml` |
| Major | MediaDB's ten organism growth rows are omitted. | MediaDB growth data 299 through 308 record strain-specific growth rates, temperatures, and D-glucose uptake rates for this medium, but the YAML carries no structured target organism or uptake claim. | `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml` |
| Major | The imported MediaDB preparation protocol is unsupported and may over-prescribe filtration. | Inspected MediaDB pages for medium 147 expose the formula, source, and growth rows, but not a three-step protocol requiring distilled water, conditional pH adjustment, or 0.22 um filtration. The same boilerplate is produced for MediaDB imports, so the likely durable fix belongs in the importer. | `src/culturemech/import/mediadb_importer.py`; then regenerate `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml` |
| Minor | Some source ingredient cross-references are dropped or changed. | MediaDB's tabular export for medium 147 links magnesium sulfate, Iron(III) chloride, and Sodium EDTA to CHEBI IDs that are changed or absent in the YAML. | `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml` |
| Minor | Source provenance points to the MediaDB publication instead of the narrow formula source. | MediaDB source 49 identifies Fischer et al. 2003 with PubMed `12603321` and DOI `10.1046/j.1432-1033.2003.03448.x`; the normalized record only names MediaDB and Mazumdar et al. 2014. | `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml` |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/m9_medium_fischer_et_al.yaml` from the repaired `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml` so the iron row is `Iron(III) chloride`.
2. Replace or justify the manganese sulfate grounding in `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml`; the imported MediaDB row supports manganese sulfate, not a specific monohydrate.
3. Add MediaDB growth rows 299, 300, 301, 302, 303, 304, 305, 306, 307, and 308 to `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml`, including growth rates, 37.0 C temperatures, and D-glucose uptake rates.
4. Remove unsupported generic preparation steps from this record, or change `src/culturemech/import/mediadb_importer.py` so MediaDB imports do not emit a synthetic filtration and pH-adjustment protocol when MediaDB has no recipe text supporting those steps.
5. Check the magnesium sulfate, Iron(III) chloride, and sodium EDTA CHEBI mappings against MediaDB 147 and document any intentional normalization.
6. Add structured narrow source provenance for MediaDB source 49, PubMed `12603321`, and DOI `10.1046/j.1432-1033.2003.03448.x` in `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml`.

## Follow-up Checks

Run these after future curation:

1. Re-open `data/merge_yaml/merged/m9_medium_fischer_et_al.yaml` and confirm it contains `Iron(III) chloride`, not `"'Iron(III"`.
2. `just validate-schema data/merge_yaml/merged/m9_medium_fischer_et_al.yaml` or the focused `linkml-validate` command above.
3. `python scripts/validate_strict.py data/merge_yaml/merged/m9_medium_fischer_et_al.yaml --out /tmp/m9_medium_fischer_et_al.strict.tsv --workers 1 --quiet`.
4. `linkml-reference-validator validate data data/merge_yaml/merged/m9_medium_fischer_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`.
5. `linkml-term-validator validate-data data/merge_yaml/merged/m9_medium_fischer_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`.
6. Manually re-open MediaDB medium 147, MediaDB text 147, MediaDB source 49, MediaDB growth data 299 through 308, and PubMed `12603321` to confirm the regenerated YAML preserves the formula and the added source and growth metadata.

## Additional Notes

No record edits were made during this read-only review. The generated file should stay derived from `data/normalized_yaml/bacterial/m9_medium_fischer_et_al.yaml`; a direct patch to `data/merge_yaml/merged/m9_medium_fischer_et_al.yaml` would be overwritten.

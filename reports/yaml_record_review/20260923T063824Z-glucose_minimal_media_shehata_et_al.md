# YAML Record Review: glucose_minimal_media_shehata_et_al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glucose_minimal_media_shehata_et_al.yaml
- Started UTC: 2026-09-23T06:36:47Z
- Finished UTC: 2026-09-23T06:38:27Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:007035` |
| Name | `glucose_minimal_media_shehata_et_al` |
| Original name | `Glucose minimal media; Shehata et al` |
| Category | `bacterial` |
| Media term | `MEDIADB:145` |
| Maintained parent | `data/normalized_yaml/bacterial/glucose_minimal_media_shehata_et_al.yaml` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glucose_minimal_media_shehata_et_al.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glucose_minimal_media_shehata_et_al.yaml --out /private/tmp/glucose_minimal_media_shehata_et_al.strict.tsv --workers 1 --quiet` | Passed; TSV had only the header row and 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glucose_minimal_media_shehata_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glucose_minimal_media_shehata_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated single-source record denotes MediaDB medium 145, `Glucose minimal media; shehata et al`. A gitignore-independent exact search for `MEDIADB:145`, `MediaDB.*Medium ID: 145`, and `glucose_minimal_media_shehata_et_al` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found only the maintained parent, the generated merge, and normalized indexes.

Most ingredient identities agree with the live MediaDB row labels: D-glucose, L-methionine, thymine, calcium chloride anhydrous, potassium dibasic phosphate, sodium sulfate, potassium chloride, potassium dihydrogen phosphate, ammonium chloride, and ferrous sulfate.

Magnesium chloride is over-grounded. MediaDB 145 labels the compound `Magnesium chloride` and its tab-delimited ChEBI column contains `6636`, but the generated record assigns `CHEBI:86345` / magnesium dichloride hexahydrate.

## Evidence

The live MediaDB HTML page and tab-delimited view support all 11 stored millimolar concentrations:

| Ingredient | Generated mM |
|---|---:|
| D-Glucose | 11.1012 |
| L-Methionine | 0.26807 |
| Thymine | 0.031717 |
| Magnesium chloride | 0.983719 |
| Calcium chloride anhydrous | 0.0901024 |
| Potassium dibasic phosphate | 48.7944 |
| Sodium sulfate | 1.40805 |
| Potassium chloride | 13.4136 |
| Potassium dihydrogen phosphate | 30.8628 |
| Ammonium chloride | 14.0211 |
| Ferrous sulfate | 0.0017982 |

The source page does not state any pH value, filtration pore size, or heat-sensitivity warning. The three generated preparation steps are therefore importer templates or inferences rather than source-backed steps, and one is explicitly placeholder text: `Adjust pH if specified in original formulation`.

MediaDB 145 names four growth organisms for this medium: Escherichia coli K-12, Escherichia coli ML30G, Escherichia coli TS689, and Salmonella enterica Typhimurium LT2. None are represented under `target_organisms`.

The MediaDB source attached to this medium is Shehata et al., 1970, Journal of Bacteriology, PMID 4919993. The generated record name matches that source, but its import history says `Reference: Mazumdar et al. (2014) PLOS One`.

## Completeness

The ingredient concentration table is complete for MediaDB's 11 compounds and the recipe is correctly classified as defined and liquid.

Preparation evidence is incomplete and partly unsupported because MediaDB exposes concentrations but no dissolve, pH-adjustment, or filter-sterilization protocol. Growth metadata is also incomplete because the MediaDB growth-data links were not imported.

Empty optional fields such as `references` and `discussion` are not defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated preparation steps are not source-backed and include a placeholder pH instruction. | MediaDB 145 exposes only the concentration table, organism links, and source links; no inspected MediaDB page states 0.22 um filtration or a pH adjustment for this recipe. | MediaDB importer or `data/normalized_yaml/bacterial/glucose_minimal_media_shehata_et_al.yaml`. |
| Major | `Magnesium chloride` is over-grounded as a hexahydrate. | The MediaDB HTML and TSV rows say `Magnesium chloride`; the TSV row's ChEBI column is `6636`, while the generated record uses `CHEBI:86345` with label `magnesium dichloride hexahydrate`. | `data/normalized_yaml/bacterial/glucose_minimal_media_shehata_et_al.yaml` or MediaDB chemical mapping. |
| Minor | The import history cites the wrong paper for MediaDB 145. | MediaDB source 47 for this medium is Shehata et al., 1970, PMID 4919993; the import history says Mazumdar et al. (2014) PLOS One. | MediaDB importer history construction or the maintained parent. |
| Minor | MediaDB growth-organism links are absent. | The MediaDB 145 page lists three Escherichia coli strains and Salmonella enterica Typhimurium LT2 with growth-data records 293-296; the generated recipe has no `target_organisms`. | MediaDB importer if growth data are in scope for MediaDB records. |

## Recommended Edits

1. Remove the generic preparation steps from `glucose_minimal_media_shehata_et_al.yaml`, or replace them with source-backed steps from Shehata et al. if the original article supplies a protocol.
2. Reground Magnesium chloride to the generic anhydrous MediaDB ChEBI cross-reference instead of the hexahydrate.
3. Correct the MediaDB import history to cite Shehata et al., 1970 / PMID 4919993 for medium 145.
4. Decide whether MediaDB growth-data records should populate `target_organisms`; if yes, import the four MediaDB 145 organism links with evidence scoped to the MediaDB growth-data records.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated merged record.
- Re-fetch the MediaDB HTML and tab-delimited pages for medium 145 and verify all 11 millimolar concentrations still match.
- Re-run the exact gitignore-independent search for `MEDIADB:145`, `MediaDB.*Medium ID: 145`, and `glucose_minimal_media_shehata_et_al` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify no additional duplicates were introduced.

## Additional Notes

The record uses `CHEBI:75832` for Ferrous sulfate, matching MediaDB's tab-delimited ChEBI cross-reference for that compound.

# YAML Record Review: glucose_minimal_media_zhao_zhu

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glucose_minimal_media_zhao_zhu.yaml
- Started UTC: 2026-09-23T06:40:10Z
- Finished UTC: 2026-09-23T06:41:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Stale generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:007021` |
| Name | `glucose_minimal_media_zhao_zhu` |
| Original name | `'''glucose minimal media (zhao/zhu` |
| Category | `bacterial` |
| Media term | `MEDIADB:132` |
| Maintained parent | `data/normalized_yaml/bacterial/glucose_minimal_media_zhao_zhu.yaml` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glucose_minimal_media_zhao_zhu.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glucose_minimal_media_zhao_zhu.yaml --out /private/tmp/glucose_minimal_media_zhao_zhu.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glucose_minimal_media_zhao_zhu.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glucose_minimal_media_zhao_zhu.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This record denotes MediaDB medium 132, `Glucose minimal media (zhao/zhu)`. A gitignore-independent exact search for `MEDIADB:132`, `Medium ID: 132`, and `glucose_minimal_media_zhao_zhu` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found only the maintained parent, this generated merge, and normalized index references.

The generated file is stale relative to its single maintained parent. The maintained parent repaired the medium name, the MediaDB label, the beta-D-glucose grounding, and the `Iron(III) chloride` label on August 20 and August 31, 2026. None of those repairs appear in the generated merge, whose latest history row is the August 6, 2026 merge event.

Most source labels are retained, but `Manganese sulfate` is grounded as `CHEBI:86364` / manganese(II) sulfate monohydrate even though the MediaDB label does not specify a hydrate and the MediaDB TSV has no ChEBI cross-reference for that compound.

## Evidence

The live MediaDB HTML page and tab-delimited view support all 14 millimolar concentrations:

| Ingredient | Generated mM |
|---|---:|
| beta-D-Glucose | 55.506 |
| Calcium chloride anhydrous | 0.01163 |
| Potassium dibasic phosphate | 41.9058 |
| Sodium sulfate | 14.0449 |
| Magnesium sulfate | 3.0 |
| Manganese sulfate | 0.001775 |
| Ammonium chloride | 9.3474 |
| Cobalt chloride | 0.00227 |
| Zinc sulfate | 0.001878 |
| Sodium dihydrogen phosphate | 30.005 |
| Ammonium sulfate | 18.919 |
| Cupric sulfate | 0.0019223 |
| Iron(III) chloride | 0.18535 |
| Sodium EDTA | 0.18828 |

The source page lists two sources, Zhao et al. 2004 and Zhu et al. 2005, and eight growth-data records for seven Escherichia coli BW25113 strains. The generated import history instead says `Reference: Mazumdar et al. (2014) PLOS One`, and no MediaDB growth organisms are represented under `target_organisms`.

The MediaDB source does not state a pH value, filtration pore size, or heat-sensitivity warning. The three generated preparation steps are generic importer text rather than MediaDB 132 protocol evidence.

## Completeness

The generated record is complete for the 14 MediaDB millimolar concentrations, but it is missing maintained upstream repairs for display names and one CHEBI grounding. It is also incomplete for MediaDB source attribution and growth metadata.

Empty optional fields such as `references` and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated record is stale and still contains name parsing damage that was already repaired upstream. | `data/normalized_yaml/bacterial/glucose_minimal_media_zhao_zhu.yaml` has `original_name: glucose minimal media (zhao/zhu)`, `media_term.term.label: glucose minimal media (zhao/zhu)`, `preferred_term: Iron(III) chloride`, and a beta-D-glucose CHEBI grounding; the generated merge has the old stray quotes, truncated `'''Iron(III`, and no beta-D-glucose term. | Regenerate `data/merge_yaml/merged/glucose_minimal_media_zhao_zhu.yaml` from the maintained parent. |
| Major | The generated preparation steps are not source-backed and include a placeholder pH instruction. | MediaDB 132 exposes the concentration table, organism links, and source links, but no inspected MediaDB page states 0.22 um filtration or a pH adjustment for this recipe. | MediaDB importer or `data/normalized_yaml/bacterial/glucose_minimal_media_zhao_zhu.yaml`. |
| Major | `Manganese sulfate` is over-grounded to a monohydrate. | MediaDB labels the compound `Manganese sulfate` and has no ChEBI ID in the tab-delimited row; the generated record assigns `CHEBI:86364`, manganese(II) sulfate monohydrate. | MediaDB chemical mapping in `data/normalized_yaml/bacterial/glucose_minimal_media_zhao_zhu.yaml`. |
| Minor | The import history cites the wrong paper for MediaDB 132. | MediaDB 132 lists Zhao et al. 2004 and Zhu et al. 2005 as its sources; the import history says Mazumdar et al. (2014) PLOS One. | MediaDB importer history construction or the maintained parent. |
| Minor | MediaDB growth-organism links are absent. | MediaDB 132 lists eight growth-data records for seven Escherichia coli BW25113 strains; the generated recipe has no `target_organisms`. | MediaDB importer if growth data are in scope for MediaDB records. |

## Recommended Edits

1. Regenerate the generated merge from `data/normalized_yaml/bacterial/glucose_minimal_media_zhao_zhu.yaml` so the August 2026 MediaDB name repairs and beta-D-glucose grounding reach `data/merge_yaml/merged/`.
2. Remove the generic MediaDB preparation steps from the maintained parent, or replace them with source-backed steps if the Zhao or Zhu papers supply a protocol.
3. Deground `Manganese sulfate` from the monohydrate unless MediaDB source evidence identifies that hydrate.
4. Correct the MediaDB import history to cite Zhao et al. 2004 and Zhu et al. 2005 for medium 132.
5. Decide whether MediaDB growth-data records should populate `target_organisms`; if yes, import the seven organism labels or eight growth links from MediaDB 132.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated merged record.
- Re-fetch the MediaDB HTML and tab-delimited pages for medium 132 and compare all 14 ingredient rows, the medium label, and the linked Zhao/Zhu sources.
- Re-run the exact gitignore-independent search for `MEDIADB:132`, `Medium ID: 132`, and `glucose_minimal_media_zhao_zhu` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify no additional duplicates were introduced.

## Additional Notes

`Iron(III) chloride` and `Sodium EDTA` remain ungrounded in the maintained parent even though the MediaDB TSV has ChEBI cross-references for both. They should be candidates for future exact-source grounding once the generated merge is refreshed.

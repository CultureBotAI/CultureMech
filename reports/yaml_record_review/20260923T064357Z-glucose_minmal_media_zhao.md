# YAML Record Review: glucose_minmal_media_zhao

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glucose_minmal_media_zhao.yaml
- Started UTC: 2026-09-23T06:42:29Z
- Finished UTC: 2026-09-23T06:44:05Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Stale generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:007016` |
| Name | `glucose_minmal_media_zhao` |
| Original name | `'''Glucose minmal media (zhao` |
| Category | `bacterial` |
| Canonical media term | `MEDIADB:128` |
| Merged sources | `data/normalized_yaml/bacterial/glucose_minmal_media_zhao.yaml`, `data/normalized_yaml/bacterial/glucose_m9_medium_peng_zhao.yaml` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glucose_minmal_media_zhao.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glucose_minmal_media_zhao.yaml --out /private/tmp/glucose_minmal_media_zhao.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glucose_minmal_media_zhao.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glucose_minmal_media_zhao.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

The generated record is nominally MediaDB 128, `Glucose minmal media (zhao)`, but it also merged MediaDB 130, `Glucose m9 medium (peng/zhao)`. These are adjacent MediaDB recipes, not exact source duplicates.

A gitignore-independent exact search for `MEDIADB:128`, `MEDIADB:130`, `Medium ID: 128`, `Medium ID: 130`, `glucose_minmal_media_zhao`, and `glucose_m9_medium_peng_zhao` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found only the two maintained parents, normalized indexes, and this generated merge.

The generated file is stale relative to both maintained parents. The parents now have complete medium labels, beta-D-glucose groundings, and `Iron(III) chloride` labels from August 2026 repairs, but the generated merge still has stray quotes, a truncated `'''Iron(III` ingredient, and no beta-D-glucose term.

## Evidence

MediaDB 128 and 130 agree on 13 of 14 ingredient concentrations and differ in ammonium sulfate:

| Source | Medium label | Ammonium sulfate |
|---|---|---:|
| `MEDIADB:128` | Glucose minmal media (zhao) | 10.0 mM |
| `MEDIADB:130` | Glucose m9 medium (peng/zhao) | 30.0 mM |

The generated record is labeled `MEDIADB:128` but contains 30.0 mM ammonium sulfate from `MEDIADB:130`.

Both MediaDB source pages show beta-D-glucose, Calcium chloride anhydrous, Dibasic sodium phosphate, Sodium molybdate, Sodium chloride, Thiamine HCl, Potassium dihydrogen phosphate, Magnesium sulfate, Cobalt chloride, Manganese chloride, Cupric chloride, Iron(III) chloride, and Zinc Chloride at the same concentrations in both recipes.

Both source pages list linked growth data: MediaDB 128 lists Escherichia coli BW25113 and Escherichia coli BW25113_zwf-, while MediaDB 130 lists Escherichia coli BW25113, Escherichia coli BW25113_gnd-, Escherichia coli BW25113_ppc-, and Escherichia coli BW25113_zwf-. None are represented under `target_organisms`.

The MediaDB sources do not state a pH value, filtration pore size, or heat-sensitivity warning. The three generated preparation steps are generic importer text rather than source-backed steps.

## Completeness

The generated record is not complete enough to serve either MediaDB 128 or MediaDB 130 because it conflates their only concentration difference. It also predates maintained repairs to medium and ingredient names.

Empty optional fields such as `references` and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | MediaDB 128 and MediaDB 130 were merged despite a threefold ammonium sulfate difference. | MediaDB 128 has 10.0 mM ammonium sulfate; MediaDB 130 has 30.0 mM. The generated `MEDIADB:128` record stores 30.0 mM and lists `MEDIADB:130` as a synonym. | Duplicate grouping in `scripts/merge_recipes.py` or MediaDB merge overlays. |
| Major | The generated record is stale and still contains parser-truncated names that were repaired upstream. | Both maintained parents have complete labels and `Iron(III) chloride`; the generated merge still has `'''Glucose minmal media (zhao`, `'''Iron(III`, and lacks beta-D-glucose grounding. | Regenerate `data/merge_yaml/merged/glucose_minmal_media_zhao.yaml` after splitting MediaDB 128 and 130. |
| Major | The generated preparation steps are not source-backed and include a placeholder pH instruction. | MediaDB 128 and 130 expose concentration tables, organism links, and source links, but no inspected MediaDB page states 0.22 um filtration or a pH adjustment for either recipe. | MediaDB importer or the two maintained MediaDB parents. |
| Minor | The import history cites a generic Mazumdar 2014 reference for both MediaDB records. | MediaDB 128 lists Zhao et al. 2004; MediaDB 130 lists Peng et al. 2004 and Zhao et al. 2003. | MediaDB importer history construction or the maintained parents. |
| Minor | MediaDB growth-organism links are absent. | The MediaDB pages list two growth records for 128 and five growth records for 130; the generated recipe has no `target_organisms`. | MediaDB importer if growth data are in scope for MediaDB records. |

## Recommended Edits

1. Split MediaDB 128 and MediaDB 130 into separate generated records so their 10.0 mM versus 30.0 mM ammonium sulfate difference is preserved.
2. After the split, regenerate both records from the maintained parents so the August 2026 MediaDB name repairs and beta-D-glucose grounding propagate into `data/merge_yaml/merged/`.
3. Remove unsupported generic preparation steps from the two maintained parents, or replace them with source-backed protocol text if the Zhao or Peng papers supply protocols.
4. Correct the import histories to cite the MediaDB-listed source papers for MediaDB 128 and 130.
5. Decide whether MediaDB growth-data links should populate `target_organisms`; if yes, import them per MediaDB accession after the split.

## Follow-up Checks

- Re-run `scripts/merge_recipes.py` and confirm `glucose_minmal_media_zhao` and `glucose_m9_medium_peng_zhao` no longer share a `merge_fingerprint`.
- Re-run open LinkML, strict, reference, and term validation on both regenerated MediaDB records.
- Re-fetch MediaDB 128 and 130 HTML and TSV pages and compare all 14 ingredient rows, especially ammonium sulfate, against their respective regenerated records.
- Repeat the exact gitignore-independent search for `MEDIADB:128`, `MEDIADB:130`, `Medium ID: 128`, `Medium ID: 130`, `glucose_minmal_media_zhao`, and `glucose_m9_medium_peng_zhao` across `data/normalized_yaml/` and `data/merge_yaml/merged/`.

## Additional Notes

The string `minmal` is present on the live MediaDB 128 page and appears to be source spelling rather than a CultureMech truncation artifact. The parenthesis truncation after `zhao` was a CultureMech import artifact that the maintained parent has already repaired.

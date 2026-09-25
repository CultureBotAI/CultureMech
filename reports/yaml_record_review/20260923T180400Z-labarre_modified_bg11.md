# YAML Record Review: labarre_modified_bg11

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/labarre_modified_bg11.yaml
- Started UTC: 2026-09-23T18:02:35Z
- Finished UTC: 2026-09-23T18:04:00Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/labarre_modified_bg11.yaml`, generated `MediaRecipe` record `CultureMech:007221` for MediaDB medium 321.

- Maintained owner: `data/normalized_yaml/bacterial/labarre_modified_bg11.yaml`.
- Merge provenance: `merged_from: labarre_modified_bg11`; generated merge fingerprint `60cf59ed55ff30990f898a51448e9b5f57998c31fd1ad03127368ea698d29984`.
- Source claim: MediaDB medium 321 / `MEDIADB:321`.
- Current generated identity: `medium_type: DEFINED`, `composition_type: DEFINED`, `physical_state: LIQUID`.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/labarre_modified_bg11.yaml`; the command exited 0 with no output. |
| Strict schema | Passed with `python scripts/validate_strict.py data/merge_yaml/merged/labarre_modified_bg11.yaml --out /private/tmp/labarre_modified_bg11.strict.tsv --workers 1 --quiet`. |
| Reference integrity | Passed with `linkml-reference-validator validate data data/merge_yaml/merged/labarre_modified_bg11.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; there were 0 checks. |
| Term integrity | Passed with `linkml-term-validator validate-data data/merge_yaml/merged/labarre_modified_bg11.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

MediaDB medium 321 resolves to `Labarre (modified bg11)` and lists the same 16 compounds and millimolar concentrations as the maintained normalized owner. An exact ignored-file-inclusive search of `data/normalized_yaml` and `data/merge_yaml` for `CultureMech:007221`, `MEDIADB:321`, and MediaDB medium ID 321 found one maintained YAML owner and the reviewed generated merge.

The generated YAML is stale relative to its owner. `data/normalized_yaml/bacterial/labarre_modified_bg11.yaml` repaired the medium label to `Labarre (Modified BG11)` and the iron compound to `Fe(III)dicitrate` on 2026-08-31, but the generated `data/merge_yaml/merged/labarre_modified_bg11.yaml` still has the truncated `'''Labarre (Modified BG11` label and `'''Fe(III` ingredient. That stale artifact leaves a consequential source ingredient malformed even though the current maintained owner has already fixed it.

## Evidence

The MediaDB text view for medium 321 supports every compound amount in the current maintained owner: citrate 0.03123 mM, EDTA 0.003422 mM, Fe(III)dicitrate 0.0245 mM, calcium chloride anhydrous 0.2433 mM, boric acid 0.04626 mM, potassium dibasic phosphate 0.2239 mM, sodium molybdate 0.001616 mM, magnesium sulfate 0.3043 mM, zinc sulfate 0.0007721 mM, manganese chloride 0.009145 mM, cupric sulfate 0.0003164 mM, cobalt nitrate 0.0001697 mM, HEPES 6.0 mM, sodium carbonate 1.887 mM, sodium nitrate 10.03 mM, and sodium silicate 0.2041 mM.

The MediaDB medium page links the formulation to source record 134, organism record 188, and growth record 652. Source 134 identifies PMID 3115962, and NCBI E-utilities verified that PMID as Labarre, Thuriaux, and Chauvat's 1987 `J Bacteriol` paper on amino acid transport in `Synechocystis` sp. strain 6803. The growth-data page ties MediaDB 321 to `Synechocystis pcc6803`, source 134, pH 7.5, and temperature 30.0.

The MediaDB pages do not provide the three preparation steps currently stored in the YAML. In particular, no inspected source page says to adjust a pH, and no inspected source page says to filter-sterilize through a 0.22 um filter.

## Completeness

The 16 compound rows are complete for MediaDB medium 321 in the maintained owner. Empty pH and target organism slots are not safe to leave empty, however:

- The source-specific pH 7.5 and temperature 30.0 from growth record 652 are absent.
- The `Synechocystis pcc6803` association from MediaDB medium 321, organism 188, and growth data 652 is absent.
- Structured source metadata for MediaDB source 134 and PMID 3115962 is absent; the curation history mentions Mazumdar et al. 2014 for the MediaDB database, not the Labarre et al. 1987 source that MediaDB associates with this medium.

No additional maintained YAML duplicates were found by the exact ignored-inclusive search over `data/normalized_yaml` and `data/merge_yaml`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated record is stale and still contains MediaDB parser truncation artifacts. | The reviewed merge has `'''Labarre (Modified BG11` and `'''Fe(III`; the maintained owner repaired those to `Labarre (Modified BG11)` and `Fe(III)dicitrate` after the merge timestamp. | Regenerate from `data/normalized_yaml/bacterial/labarre_modified_bg11.yaml` |
| Major | Preparation steps are unsupported generic placeholders. | MediaDB medium 321, source 134, organism 188, and growth-data 652 do not assert pH adjustment or 0.22 um filtration, but the record instructs both. | `data/normalized_yaml/bacterial/labarre_modified_bg11.yaml` |
| Major | The MediaDB organism and growth-condition evidence is not represented. | MediaDB growth data 652 associates medium 321 with `Synechocystis pcc6803`, pH 7.5, temperature 30.0, and source 134. | `data/normalized_yaml/bacterial/labarre_modified_bg11.yaml` |
| Minor | Primary literature provenance is not structured. | The record only stores `MEDIADB:321`; MediaDB source 134 and PMID 3115962 are absent from the maintained YAML. | `data/normalized_yaml/bacterial/labarre_modified_bg11.yaml` |

## Recommended Edits

1. Regenerate the merged YAML so the repaired MediaDB name and `Fe(III)dicitrate` ingredient from `data/normalized_yaml/bacterial/labarre_modified_bg11.yaml` reach `data/merge_yaml/merged/labarre_modified_bg11.yaml`.
2. Remove or qualify the generic `ADJUST_PH` and `FILTER_STERILIZE` preparation steps unless a source is added that actually supports those instructions.
3. Curate the MediaDB growth-data 652 association to `Synechocystis pcc6803`, including source-scoped pH 7.5 and temperature 30.0 if the schema can represent them without implying those are formula pH values.
4. Add structured references for MediaDB source 134 and PMID 3115962 alongside `MEDIADB:321`.
5. Regenerate the merged record and affected rendered pages.

## Follow-up Checks

- Rerun the open-schema, strict, reference, and term validators against the regenerated merged record.
- Compare all 16 compound names and mM values against `/defined_media/media_text/321/` after regeneration.
- Reopen MediaDB growth-data 652 and source 134 to confirm any `target_organisms` or growth metrics remain scoped to the `Synechocystis pcc6803` row.
- Search with `rg --no-ignore --hidden` for `'''Fe(III` and `'''Labarre` after regeneration to confirm the stale parser output is gone from ignored and hidden generated artifacts too.

## Additional Notes

This generated record demonstrates why stale merge artifacts need review in addition to maintained YAML: the August `repair_mediadb_names.py` changes fixed the normalized owner, but the generated record retained the old parse defect.

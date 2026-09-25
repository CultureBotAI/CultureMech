# YAML Record Review: batch_cultivation_medium_for_a28

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/batch_cultivation_medium_for_a28.yaml
- Started UTC: 2026-09-21T18:55:56Z
- Finished UTC: 2026-09-21T18:57:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path reviewed | `data/merge_yaml/merged/batch_cultivation_medium_for_a28.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/batch_cultivation_medium_for_a28.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007247` |
| Name | `batch_cultivation_medium_for_a28` |
| Original name | Generated: `'''Batch Cultivation Medium (for A28`; normalized: `Batch Cultivation Medium (for A28)` |
| Source | MediaDB Medium `346` |
| Merge status | Generated one-source merge from `batch_cultivation_medium_for_a28` |

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with the no-project LinkML invocation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`, and the generated MediaDB 346 merge. |
| Strict schema | Passed with the no-project invocation of `scripts/validate_strict.py`: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | Passed with 0 reference checks because this MediaDB import has no populated `references` list or evidence objects. |
| Term validator | Passed with `linkml-term-validator validate-data` against the generated MediaDB 346 merge. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for the standalone `history/` tree, not a focused one-record `MediaRecipe.curation_history` check. |
| Project `just` wrappers | Not rerun here: direct `just validate-schema`, `just validate-strict`, and `just validate-terms` fail before target-specific validation in this checkout while the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13. The equivalent no-project Python 3.11 validators above exercised the target record. |

## Identity and Grounding

- MediaDB Medium 346 denotes `Batch cultivation medium (for a28)` for `Aspergillus nidulans A28`, not a bacterial medium. MediaDB's organism page for organism 159 labels `Aspergillus nidulans A28` as `eukaryote`.
- The generated merge is stale relative to `data/normalized_yaml/bacterial/batch_cultivation_medium_for_a28.yaml`: the normalized owner has an Aug 31, 2026 `repair_mediadb_names.py` event that restores `Batch Cultivation Medium (for A28)`, while the generated merge still has the truncated `'''Batch Cultivation Medium (for A28` string.
- Exact gitignore-independent searches for `CultureMech:007247`, `MEDIADB:346`, and `batch_cultivation_medium_for_a28` covered `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`. They found the normalized owner, generated merge, generated indexes, registry rows, and import/report metadata for this record.
- The source-provided component amounts are otherwise present, but two groundings disagree with the MediaDB export: `4-Aminobenzoate` uses `CHEBI:17836` instead of MediaDB's `CHEBI:30753`, and `Magnesium sulfate` uses generic `CHEBI:32599` instead of MediaDB's `CHEBI:31795`.

## Evidence

- The live MediaDB Medium 346 page and its tab-delimited export support all 12 component labels and mM amounts in the CultureMech record.
- MediaDB Medium 346 links to organism `Aspergillus nidulans A28`, source `Prathumpai w et al, 2003`, and growth-data record 704. The CultureMech record omits the organism association, growth evidence, and primary source.
- MediaDB growth-data record 704 reports `Aspergillus nidulans A28 on Batch cultivation medium (for a28)`, pH `6.0`, temperature `30.0`, and no numeric growth rate; the YAML carries neither pH nor temperature.
- The MediaDB source page identifies a 2003 Biotechnology Progress article, `Metabolic control analysis of xylose catabolism in Aspergillus.`, and links PubMed term `12892473`; the YAML curation event names the umbrella Mazumdar 2014 MediaDB paper instead and has no per-medium reference.
- The MediaDB Medium 346 page and tab-delimited export did not expose any pH-adjustment or filter-sterilization preparation protocol.

## Completeness

- Consequential gaps:
  - The record is in `data/normalized_yaml/bacterial` and `category: bacterial` despite having only a fungal/eukaryotic source organism.
  - The generated merge should be regenerated from the Aug 31 normalized owner before the label is rechecked.
  - The primary MediaDB source, organism, pH, and temperature are missing.
  - The 4-aminobenzoate and magnesium sulfate groundings should be reviewed against MediaDB's own ChEBI IDs.
  - The three generated preparation steps need removal or replacement with source-backed preparation detail.
- Correctly empty optional slots:
  - `solutions` is absent because MediaDB Medium 346 lists all 12 components directly.
  - Growth rate is absent; the inspected MediaDB growth-data page reports `None` for that measurement.
- Bounded negative searches:
  - Exact gitignore-independent searches found no local raw MediaDB dump or Medium 346 export under `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`; only normalized/generated YAML and index/report rows are locally present.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The record is filed as bacterial even though its source organism is fungal/eukaryotic. | MediaDB Medium 346 and growthdata 704 link the recipe to `Aspergillus nidulans A28`; MediaDB organism 159 labels that organism `eukaryote`. | `data/normalized_yaml/bacterial/batch_cultivation_medium_for_a28.yaml`, the category/indexes, and likely the MediaDB importer category mapping. |
| Major | The generated merge is stale and retains the old truncated MediaDB name. | The normalized owner restored `Batch Cultivation Medium (for A28)` on 2026-08-31; the generated merge still has `'''Batch Cultivation Medium (for A28` in `original_name` and the MediaDB term label. | Regenerate `data/merge_yaml/merged/batch_cultivation_medium_for_a28.yaml` after moving/fixing the normalized owner. |
| Major | The record omits MediaDB's own primary source and growth-condition context. | MediaDB Medium 346 links source 117, organism 159, and growthdata 704; growthdata 704 reports A. nidulans A28, pH 6.0, and 30.0 C, while the YAML has no `target_organisms`, `references`, pH, temperature, or growth evidence. | The normalized owner; broad repeats may require `src/culturemech/import/mediadb_importer.py`. |
| Major | The MediaDB importer inserted unsupported generic preparation steps. | The YAML says to dissolve all ingredients, adjust pH if specified, and filter-sterilize at 0.22 um, but the inspected MediaDB Medium 346 page and tab-delimited export contain no preparation protocol. | The normalized owner; broad repeats may require `src/culturemech/import/mediadb_importer.py`. |
| Major | Two ingredient groundings disagree with MediaDB's exported ChEBI IDs. | MediaDB exports `4-Aminobenzoate` with `CHEBI:30753` and `Magnesium sulfate` with `CHEBI:31795`; the YAML uses `CHEBI:17836` and `CHEBI:32599`. | The normalized owner. |

## Recommended Edits

1. Move this record to the fungal/eukaryotic category or otherwise repair MediaDB category assignment so `Aspergillus nidulans A28` media are not indexed as bacterial.
2. Preserve the repaired `Batch Cultivation Medium (for A28)` name from the normalized owner when regenerating the merge.
3. Add the MediaDB primary source for Prathumpai W et al. 2003, PubMed `12892473`, and the linked Medium 346/Growth Data 704 evidence.
4. Add the MediaDB growth assertion for `Aspergillus nidulans A28` with pH 6.0 and 30.0 C; leave growth rate empty because MediaDB reports `None`.
5. Replace unsupported generic preparation steps with source-backed preparation only.
6. Re-ground 4-aminobenzoate and magnesium sulfate, or document why the MediaDB ChEBI IDs should not be adopted.

## Follow-up Checks

- Rerun open-schema LinkML validation, `scripts/validate_strict.py`, `linkml-term-validator`, and the reference validator on the moved/repaired normalized owner.
- Regenerate the generated merge and run `just verify-merges` plus `just audit-merge-freshness`.
- Rebuild category indexes and confirm `CultureMech:007247` is no longer under `data/normalized_yaml/bacterial_index.json`.
- Re-fetch MediaDB `/defined_media/media/346/`, `/defined_media/media_text/346/`, `/defined_media/sources/117/`, and `/defined_media/growthdata/704/` and manually compare the normalized ingredients, source, organism, pH, and temperature.

## Additional Notes

- This is a one-source generated merge; merge output adds only `merge_recipes.py`, `merge_fingerprint`, and `merged_from` to the normalized scientific content.
- Exact gitignore-independent searches included ignored files where present.

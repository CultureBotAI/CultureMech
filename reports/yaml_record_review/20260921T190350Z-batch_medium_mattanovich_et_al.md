# YAML Record Review: batch_medium_mattanovich_et_al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/batch_medium_mattanovich_et_al.yaml
- Started UTC: 2026-09-21T19:01:01Z
- Finished UTC: 2026-09-21T19:03:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path reviewed | `data/merge_yaml/merged/batch_medium_mattanovich_et_al.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007250` |
| Name | `batch_medium_mattanovich_et_al` |
| Original name | `Batch medium; mattanovich et al` |
| Source | MediaDB Medium `34` |
| Merge status | Generated one-source merge from `batch_medium_mattanovich_et_al` |

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with the no-project LinkML invocation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`, and the generated MediaDB 34 merge. |
| Strict schema | Passed with the no-project invocation of `scripts/validate_strict.py`: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | Passed with 0 reference checks because this MediaDB import has no populated `references` list or evidence objects. |
| Term validator | Passed with `linkml-term-validator validate-data` against the generated MediaDB 34 merge. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for the standalone `history/` tree, not a focused one-record `MediaRecipe.curation_history` check. |
| Project `just` wrappers | Not rerun here: direct `just validate-schema`, `just validate-strict`, and `just validate-terms` fail before target-specific validation in this checkout while the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13. The equivalent no-project Python 3.11 validators above exercised the target record. |

## Identity and Grounding

- MediaDB Medium 34 denotes `Batch medium; mattanovich et al` for `Komagataella pastoris DSMZ 70382`, not a bacterial medium. MediaDB's organism page for organism 13 labels `Komagataella pastoris DSMZ 70382` as `eukaryote`.
- The generated merge is stale relative to `data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml`: the normalized owner has an Aug 20, 2026 `apply_mim_groundings.py` event that grounded `Sulfate` to `CHEBI:16189` and `Sodium iodide` to `CHEBI:33167`, while the generated merge still leaves both terms empty.
- Exact gitignore-independent searches for `CultureMech:007250`, `MEDIADB:34` with a numeric boundary, `Batch medium; mattanovich et al`, and `batch_medium_mattanovich_et_al` covered `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`. They found the normalized owner, generated merge, generated indexes, registry rows, and import/report metadata for this record.
- The source-provided component amounts are all present in the generated record, but three ingredients are unresolved or over-specific relative to MediaDB's export: `Citrate` uses `CHEBI:16947` instead of MediaDB's `CHEBI:30769`, `Magnesium sulfate` uses generic `CHEBI:32599` instead of MediaDB's `CHEBI:31795`, and `Ammonium phosphate` is ungrounded despite MediaDB's `CHEBI:63051`.
- `Manganese sulfate` is grounded to `CHEBI:86364` / `manganese(II) sulfate monohydrate`, but the inspected MediaDB label and export do not specify a hydrate and the MediaDB ChEBI column is `None`.

## Evidence

- The live MediaDB Medium 34 page and its tab-delimited export support all 16 component labels and mM amounts in the CultureMech record.
- MediaDB Medium 34 links to organism `Komagataella pastoris DSMZ 70382`, source `Mattanovich et al, 2009`, and growth-data record 80. The CultureMech record omits the organism association, growth evidence, and primary source.
- MediaDB growth-data record 80 reports `Komagataella pastoris DSMZ 70382 on Batch medium; mattanovich et al`, a growth rate of `0.2 (1/h)`, pH `5.0`, temperature `25.0`, and oxygen uptake of `4.14 mmol/gDW/h`; the YAML carries none of that condition or rate context.
- The MediaDB source page identifies a 2009 Microbial Cell Factories article, `Genome, secretome and glucose transport highlight unique features of the protein production host pichia pastoris`, and links PubMed term `19490607`; the NCBI E-utilities PubMed record verifies PMID `19490607` and DOI `10.1186/1475-2859-8-29`. The YAML curation event names the umbrella Mazumdar 2014 MediaDB paper instead and has no per-medium reference.
- The MediaDB Medium 34 page and tab-delimited export did not expose any pH-adjustment or filter-sterilization preparation protocol.

## Completeness

- Consequential gaps:
  - The record is in `data/normalized_yaml/bacterial` and `category: bacterial` despite having only a fungal/eukaryotic source organism.
  - The generated merge should be regenerated from the Aug 20 normalized owner before the sulfate and sodium iodide groundings are rechecked.
  - The primary MediaDB source, organism, pH, temperature, growth rate, and oxygen uptake are missing.
  - Citrate, magnesium sulfate, manganese sulfate, and ammonium phosphate need grounding review against MediaDB's own ChEBI IDs or missing ChEBI value.
  - The three generated preparation steps need removal or replacement with source-backed preparation detail.
- Correctly empty optional slots:
  - `solutions` is absent because MediaDB Medium 34 lists all 16 components directly.
- Bounded negative searches:
  - Exact gitignore-independent searches found no local raw MediaDB dump or Medium 34 export under `data/raw` or `data/import_tracking`. There is no top-level `data/raw_yaml` directory in this checkout.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The record is filed as bacterial even though its source organism is fungal/eukaryotic. | MediaDB Medium 34 and growthdata 80 link the recipe to `Komagataella pastoris DSMZ 70382`; MediaDB organism 13 labels that organism `eukaryote`. | `data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml`, the category/indexes, and likely the MediaDB importer category mapping. |
| Major | The generated merge is stale and omits two groundings already present in the normalized owner. | The normalized owner adopted MIM groundings for `Sulfate` and `Sodium iodide` on 2026-08-20; the generated merge from 2026-08-06 still leaves both ungrounded. | Regenerate `data/merge_yaml/merged/batch_medium_mattanovich_et_al.yaml` after moving/fixing the normalized owner. |
| Major | The record omits MediaDB's own primary source and growth-condition context. | MediaDB Medium 34 links source 11, organism 13, and growthdata 80; growthdata 80 reports K. pastoris DSMZ 70382, 0.2 1/h growth, pH 5.0, 25.0 C, and oxygen uptake while the YAML has no `target_organisms`, `growth_metrics`, `references`, pH, or temperature. | The normalized owner; broad repeats may require `src/culturemech/import/mediadb_importer.py`. |
| Major | The MediaDB importer inserted unsupported generic preparation steps. | The YAML says to dissolve all ingredients, adjust pH if specified, and filter-sterilize at 0.22 um, but the inspected MediaDB Medium 34 page and tab-delimited export contain no preparation protocol. | The normalized owner; broad repeats may require `src/culturemech/import/mediadb_importer.py`. |
| Major | Four ingredient groundings are missing, stale, or over-specific relative to the MediaDB export. | MediaDB exports `Citrate` with `CHEBI:30769`, `Magnesium sulfate` with `CHEBI:31795`, and `Ammonium phosphate` with `CHEBI:63051`; the YAML uses `CHEBI:16947`, `CHEBI:32599`, and no term, respectively. MediaDB's `Manganese sulfate` row has no ChEBI ID and no hydrate label. | The normalized owner. |

## Recommended Edits

1. Move this record to the fungal/eukaryotic category or otherwise repair MediaDB category assignment so `Komagataella pastoris DSMZ 70382` media are not indexed as bacterial.
2. Preserve the Aug 20 sulfate and sodium iodide groundings from the normalized owner when regenerating the merge.
3. Add the MediaDB primary source for Mattanovich et al. 2009, PubMed `19490607`, DOI `10.1186/1475-2859-8-29`, and the linked Medium 34/Growth Data 80 evidence.
4. Add the MediaDB growth assertion for `Komagataella pastoris DSMZ 70382` with growth rate 0.2 1/h, pH 5.0, temperature 25.0 C, and oxygen uptake 4.14 mmol/gDW/h if the schema can represent uptake rates.
5. Replace unsupported generic preparation steps with source-backed preparation only.
6. Re-ground citrate, magnesium sulfate, manganese sulfate, and ammonium phosphate, or document why the MediaDB ChEBI IDs and hydrate ambiguity should not be adopted.

## Follow-up Checks

- Rerun open-schema LinkML validation, `scripts/validate_strict.py`, `linkml-term-validator`, and the reference validator on the moved/repaired normalized owner.
- Regenerate the generated merge and run `just verify-merges` plus `just audit-merge-freshness`.
- Rebuild category indexes and confirm `CultureMech:007250` is no longer under `data/normalized_yaml/bacterial_index.json`.
- Re-fetch MediaDB `/defined_media/media/34/`, `/defined_media/media_text/34/`, `/defined_media/sources/11/`, and `/defined_media/growthdata/80/` and manually compare the normalized ingredients, source, organism, pH, temperature, and growth rate.

## Additional Notes

- This is a one-source generated merge; merge output adds only `merge_recipes.py`, `merge_fingerprint`, and `merged_from` to the normalized scientific content.
- Exact gitignore-independent searches included ignored files where present.

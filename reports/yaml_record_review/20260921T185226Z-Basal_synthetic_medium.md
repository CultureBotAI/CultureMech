# YAML Record Review: Basal synthetic medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Basal_synthetic_medium.yaml
- Started UTC: 2026-09-21T18:50:54Z
- Finished UTC: 2026-09-21T18:52:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path reviewed | `data/merge_yaml/merged/Basal_synthetic_medium.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/basal_synthetic_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007204` |
| Name | `basal_synthetic_medium` |
| Original name | `Basal synthetic medium` |
| Source | MediaDB Medium `301` |
| Merge status | Generated one-source merge from `basal_synthetic_medium` |

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with the no-project LinkML invocation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`, and `data/merge_yaml/merged/Basal_synthetic_medium.yaml`. |
| Strict schema | Passed with the no-project invocation of `scripts/validate_strict.py`: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | Passed with 0 reference checks because this MediaDB import has no populated `references` list or evidence objects. |
| Term validator | Passed with `linkml-term-validator validate-data` against the generated MediaDB 301 merge. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for the standalone `history/` tree, not a focused one-record `MediaRecipe.curation_history` check. |
| Project `just` wrappers | Not rerun here: direct `just validate-schema`, `just validate-strict`, and `just validate-terms` fail before target-specific validation in this checkout while the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13. The equivalent no-project Python 3.11 validators above exercised the target record. |

## Identity and Grounding

- The generated record denotes MediaDB Medium 301, `Basal synthetic medium`, and has the permanent ID `CultureMech:007204`.
- Exact gitignore-independent searches for `CultureMech:007204`, `MEDIADB:301`, and `Basal synthetic medium` covered `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`. They found the normalized owner, generated merge, generated indexes, registry rows, and import/report metadata for this record.
- The generated merge is a direct derivative of `data/normalized_yaml/bacterial/basal_synthetic_medium.yaml`; it only adds merge metadata and one merge-history event.
- Lactose, potassium dihydrogen phosphate, ferrous sulfate, sodium molybdate, and cupric sulfate have source-supported CHEBI IDs.
- `Ammonium phosphate` is ungrounded despite MediaDB exporting ChEBI `63051`, and `Magnesium sulfate` is grounded to generic `CHEBI:32599` even though the MediaDB export gives ChEBI `31795`.

## Evidence

- The live MediaDB Medium 301 page and its tab-delimited export support all seven component labels and mM amounts in the CultureMech record.
- MediaDB Medium 301 links to organism `Bacillus amyloliquefaciens B20`, source `Hewitt et al, 1996`, and growth-data record 622. The CultureMech record omits the organism association, growth evidence, and primary source.
- MediaDB growth-data record 622 reports `Bacillus amyloliquefaciens B20 on Basal synthetic medium`, growth rate `0.074 (1/h)`, pH `None`, and temperature `37.0`; the YAML carries none of those condition or growth-measurement details.
- The MediaDB source page identifies a Hewitt Journal of Industrial Microbiology article from 1996 and links it to both Basal synthetic medium and Basal synthetic medium with vitamins; the YAML curation event names the umbrella Mazumdar 2014 MediaDB paper instead and has no per-medium reference.
- The MediaDB Medium 301 page and tab-delimited export did not expose any pH-adjustment or filter-sterilization preparation protocol.

## Completeness

- Consequential gaps:
  - The primary MediaDB source, organism, growth rate, and temperature are missing.
  - Ammonium phosphate needs the MediaDB-provided ChEBI grounding, and magnesium sulfate needs correction to the MediaDB-provided ChEBI hydrate.
  - The three generated preparation steps need removal or replacement with source-backed preparation detail.
- Correctly empty optional slots:
  - `solutions` is absent because MediaDB Medium 301 lists all seven components directly.
  - `variants` is absent on this record; MediaDB models the vitamin-supplemented sibling as separate Medium 302.
- Bounded negative searches:
  - Exact gitignore-independent searches found no local raw MediaDB dump or Medium 301 export under `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`; only normalized/generated YAML and index/report rows are locally present.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record omits MediaDB's own primary source and growth-data context. | MediaDB Medium 301 links source 111, organism 153, and growthdata 622; growthdata 622 reports B. amyloliquefaciens B20, growth rate 0.074 1/h, and 37.0 C, while the YAML has no `target_organisms`, `references`, temperature, or growth evidence. | `data/normalized_yaml/bacterial/basal_synthetic_medium.yaml`; broad repeats may require `src/culturemech/import/mediadb_importer.py`. |
| Major | The MediaDB importer inserted unsupported generic preparation steps. | The YAML says to dissolve all ingredients, adjust pH if specified, and filter-sterilize at 0.22 um, but the inspected MediaDB Medium 301 page and tab-delimited export contain no preparation protocol. | `data/normalized_yaml/bacterial/basal_synthetic_medium.yaml`; broad repeats may require `src/culturemech/import/mediadb_importer.py`. |
| Major | Two source-provided ingredient groundings are missing or overbroad. | The Medium 301 tab-delimited export gives `Ammonium phosphate` ChEBI `63051` and `Magnesium sulfate` ChEBI `31795`; the YAML leaves ammonium phosphate ungrounded and uses generic magnesium sulfate `CHEBI:32599`. | `data/normalized_yaml/bacterial/basal_synthetic_medium.yaml`. |

## Recommended Edits

1. Add the MediaDB primary source for Hewitt et al. 1996 and the linked Medium 301/Growth Data 622 evidence.
2. Add the MediaDB growth assertion for `Bacillus amyloliquefaciens B20` with 37.0 C and growth rate 0.074 1/h if the schema can represent the measurement; otherwise preserve these details in a source-scoped evidence note.
3. Remove the three generic preparation steps unless an inspected primary source supports them.
4. Ground `Ammonium phosphate` to `CHEBI:63051` and re-ground `Magnesium sulfate` from `CHEBI:32599` to `CHEBI:31795` if those MediaDB source IDs are accepted as exact for this record.
5. Regenerate `data/merge_yaml/merged/Basal_synthetic_medium.yaml` from the normalized owner.

## Follow-up Checks

- Rerun open-schema LinkML validation, `scripts/validate_strict.py`, `linkml-term-validator`, and the reference validator on `data/normalized_yaml/bacterial/basal_synthetic_medium.yaml` after edits.
- Regenerate the generated merge and run `just verify-merges` plus `just audit-merge-freshness`.
- Re-fetch MediaDB `/defined_media/media/301/`, `/defined_media/media_text/301/`, `/defined_media/sources/111/`, and `/defined_media/growthdata/622/` and manually compare the normalized ingredients, source, organism, growth rate, and temperature.
- If the MediaDB importer is changed, inspect several other MediaDB records to confirm generic preparation steps are not being added without source backing.

## Additional Notes

- `data/import_tracking/reports/ungrounded_ingredients.tsv` already lists `Ammonium phosphate` for `CultureMech:007204`.
- Exact gitignore-independent searches included ignored files where present.

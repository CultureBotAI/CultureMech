# YAML Record Review: basal_solution_p

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/basal_solution_P.yaml
- Started UTC: 2026-09-21T18:48:32Z
- Finished UTC: 2026-09-21T18:50:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path reviewed | `data/merge_yaml/merged/basal_solution_P.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/basal_solution_p.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007026` |
| Name | `basal_solution_p` |
| Original name | `basal solution P` |
| Source | MediaDB Medium `137` |
| Merge status | Generated one-source merge from `basal_solution_p` |

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with the no-project LinkML invocation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`, and `data/merge_yaml/merged/basal_solution_P.yaml`. |
| Strict schema | Passed with the no-project invocation of `scripts/validate_strict.py`: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | Passed with 0 reference checks because this MediaDB import has no populated `references` list or evidence objects. |
| Term validator | Passed with `linkml-term-validator validate-data` against the generated MediaDB 137 merge. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for the standalone `history/` tree, not a focused one-record `MediaRecipe.curation_history` check. |
| Project `just` wrappers | Not rerun here: direct `just validate-schema`, `just validate-strict`, and `just validate-terms` fail before target-specific validation in this checkout while the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13. The equivalent no-project Python 3.11 validators above exercised the target record. |

## Identity and Grounding

- The generated record denotes MediaDB Medium 137, `Basal solution p`, and has the permanent ID `CultureMech:007026`.
- Exact gitignore-independent searches for `CultureMech:007026`, `MEDIADB:137`, and `basal solution P` covered `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`. They found the normalized owner, generated merge, generated indexes, registry rows, and import/report metadata for this record.
- A gitignore-independent `find data -maxdepth 5 -iname '*mediadb*'` found normalized MediaDB-derived YAML records but no MediaDB SQL dump, TSV export, or raw Medium 137 capture in this checkout.
- `D-Glucose`, calcium chloride anhydrous, dibasic sodium phosphate, and potassium dihydrogen phosphate have source-supported CHEBI IDs.
- The `Magnesium sulfate` row is under-grounded: MediaDB's tab-delimited export for Medium 137 reports ChEBI `31795`, magnesium sulfate heptahydrate, while the YAML stores `CHEBI:32599`, generic magnesium sulfate.

## Evidence

- The live MediaDB Medium 137 page and its tab-delimited export support all five component labels and mM amounts in the CultureMech record.
- The MediaDB detail page links Medium 137 to organism `Escherichia coli K-10`, source `Eidlic et al, 1965`, and growth-data record 275. The CultureMech record omits all three narrow source associations.
- MediaDB growth-data record 275 reports `Escherichia coli K-10 on Basal solution p`, growth rate `0.69 (1/h)`, pH `6.5`, and temperature `37.0`; none of those growth-condition fields are represented in the YAML.
- The MediaDB source page identifies the primary article as an Eidlic Journal of Bacteriology paper from 1965 and links PubMed term `14273649`; the YAML curation event names the umbrella Mazumdar 2014 MediaDB paper instead and has no per-medium reference.
- The MediaDB pages and tab-delimited export did not expose any pH-adjustment or filter-sterilization preparation protocol for Medium 137.

## Completeness

- Consequential gaps:
  - The primary MediaDB source, organism, growth rate, pH, and temperature are missing.
  - Magnesium sulfate needs the exact MediaDB-provided ChEBI grounding.
  - The three generated preparation steps need removal or replacement with source-backed preparation detail.
- Correctly empty optional slots:
  - `solutions` is absent because MediaDB Medium 137 lists all five components directly.
  - `variants` is absent because the inspected MediaDB Medium 137 page lists a single formulation.
- Bounded negative searches:
  - Exact gitignore-independent searches found no local raw MediaDB dump or Medium 137 export under `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`; only the normalized/generated YAML and index/report rows are locally present.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record omits MediaDB's own primary source and growth-data context. | MediaDB Medium 137 links source 43, organism 56, and growthdata 275; growthdata 275 reports E. coli K-10, growth rate 0.69 1/h, pH 6.5, and 37.0 C, while the YAML has no `target_organisms`, `references`, pH, temperature, or growth evidence. | `data/normalized_yaml/bacterial/basal_solution_p.yaml`; broad repeats may require `src/culturemech/import/mediadb_importer.py`. |
| Major | The MediaDB importer inserted unsupported generic preparation steps. | The YAML says to dissolve all ingredients, adjust pH if specified, and filter-sterilize at 0.22 um, but the inspected MediaDB Medium 137 page and tab-delimited export contain no preparation protocol. | `data/normalized_yaml/bacterial/basal_solution_p.yaml`; broad repeats may require `src/culturemech/import/mediadb_importer.py`. |
| Major | Magnesium sulfate is grounded to a generic term instead of the source-provided exact hydrate. | MediaDB's tab-delimited export for Medium 137 gives the Magnesium sulfate row ChEBI ID `31795`; the YAML stores `CHEBI:32599`. | `data/normalized_yaml/bacterial/basal_solution_p.yaml`. |
| Minor | The top-level `high_metal: true` flag is not explained by a source or curation note. | The flag is present in YAML and `data/metal_ree_analysis.yaml` summarizes Medium 137 as Ca 0.09, Na 94.0, K 100.0, Mg 0.001, but no YAML evidence explains what threshold or assertion `high_metal` denotes for this medium. | `data/normalized_yaml/bacterial/basal_solution_p.yaml` or the maintained metal-analysis generator. |

## Recommended Edits

1. Add the MediaDB primary source for Eidlic et al. 1965, PubMed `14273649`, and the linked Medium 137/Growth Data 275 evidence.
2. Add the MediaDB growth assertion for `Escherichia coli K-10` with pH 6.5, 37.0 C, and growth rate 0.69 1/h if the schema can represent the measurement; otherwise keep these details in a source-scoped evidence note.
3. Remove the three generic preparation steps unless an inspected primary source supports them.
4. Re-ground Magnesium sulfate from `CHEBI:32599` to `CHEBI:31795` or leave the exact hydrate unresolved if the source-to-CHEBI mapping cannot be trusted.
5. Either remove `high_metal: true` or attach a source-independent curation note explaining the derived threshold that this flag satisfies.
6. Regenerate `data/merge_yaml/merged/basal_solution_P.yaml` from the normalized owner.

## Follow-up Checks

- Rerun open-schema LinkML validation, `scripts/validate_strict.py`, `linkml-term-validator`, and the reference validator on `data/normalized_yaml/bacterial/basal_solution_p.yaml` after edits.
- Regenerate the generated merge and run `just verify-merges` plus `just audit-merge-freshness`.
- Re-fetch MediaDB `/defined_media/media/137/`, `/defined_media/media_text/137/`, `/defined_media/sources/43/`, and `/defined_media/growthdata/275/` and manually compare the normalized ingredients, source, organism, growth, pH, and temperature.
- If the MediaDB importer is changed, inspect several other MediaDB records to confirm generic preparation steps are not being added without source backing.

## Additional Notes

- The generated merge only adds the `merge_recipes.py` curation event, `merge_fingerprint`, and `merged_from`; scientific rows are inherited from the normalized owner.
- Exact gitignore-independent searches included ignored files where present.

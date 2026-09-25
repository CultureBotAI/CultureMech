# YAML Record Review: basal_synthetic_medium_vitamins

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/basal_synthetic_medium_vitamins.yaml
- Started UTC: 2026-09-21T18:52:26Z
- Finished UTC: 2026-09-21T18:54:21Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path reviewed | `data/merge_yaml/merged/basal_synthetic_medium_vitamins.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/basal_synthetic_medium_vitamins.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007205` |
| Name | `basal_synthetic_medium_vitamins` |
| Original name | `Basal Synthetic Medium + vitamins` |
| Source | MediaDB Medium `302` |
| Merge status | Generated one-source merge from `basal_synthetic_medium_vitamins` |

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with the no-project LinkML invocation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`, and the generated MediaDB 302 merge. |
| Strict schema | Passed with the no-project invocation of `scripts/validate_strict.py`: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | Passed with 0 reference checks because this MediaDB import has no populated `references` list or evidence objects. |
| Term validator | Passed with `linkml-term-validator validate-data` against the generated MediaDB 302 merge. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for the standalone `history/` tree, not a focused one-record `MediaRecipe.curation_history` check. |
| Project `just` wrappers | Not rerun here: direct `just validate-schema`, `just validate-strict`, and `just validate-terms` fail before target-specific validation in this checkout while the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13. The equivalent no-project Python 3.11 validators above exercised the target record. |

## Identity and Grounding

- The generated record denotes MediaDB Medium 302, `Basal synthetic medium + vitamins`, and has the permanent ID `CultureMech:007205`.
- Exact gitignore-independent searches for `CultureMech:007205`, `MEDIADB:302`, and `basal_synthetic_medium_vitamins` covered `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`. They found the normalized owner, generated merge, generated indexes, registry rows, and import/report metadata for this record.
- The generated merge is stale relative to `data/normalized_yaml/bacterial/basal_synthetic_medium_vitamins.yaml`: the normalized owner contains an August 20, 2026 `apply_mim_groundings.py` event and a `CHEBI:18240` term on `4-Hydroxy-L-proline` that are absent from the generated merge.
- The amino acids, lactose, potassium dihydrogen phosphate, ferrous sulfate, sodium molybdate, cupric sulfate, and the normalized owner's 4-hydroxy-L-proline row have source-supported CHEBI IDs.
- `Ammonium phosphate` is ungrounded despite MediaDB exporting ChEBI `63051`, and `Magnesium sulfate` is grounded to generic `CHEBI:32599` even though the MediaDB export gives ChEBI `31795`.

## Evidence

- The live MediaDB Medium 302 page and its tab-delimited export support all 13 component labels and mM amounts in the CultureMech record.
- MediaDB Medium 302 links to organism `Bacillus amyloliquefaciens B20`, source `Hewitt et al, 1996`, and growth-data record 623. The CultureMech record omits the organism association, growth evidence, and primary source.
- MediaDB growth-data record 623 reports `Bacillus amyloliquefaciens B20 on Basal synthetic medium + vitamins`, growth rate `0.22 (1/h)`, pH `None`, and temperature `37.0`; the YAML carries none of those condition or growth-measurement details.
- The MediaDB source page for `Hewitt et al, 1996` links that primary source to both Basal synthetic medium and Basal synthetic medium with vitamins; the YAML curation event names the umbrella Mazumdar 2014 MediaDB paper instead and has no per-medium reference.
- The MediaDB Medium 302 page and tab-delimited export did not expose any pH-adjustment or filter-sterilization preparation protocol.

## Completeness

- Consequential gaps:
  - The generated merge should be regenerated from the Aug 20 normalized owner before the 4-hydroxy-L-proline row is rechecked.
  - The primary MediaDB source, organism, growth rate, and temperature are missing.
  - Ammonium phosphate needs the MediaDB-provided ChEBI grounding, and magnesium sulfate needs correction to the MediaDB-provided ChEBI hydrate.
  - The three generated preparation steps need removal or replacement with source-backed preparation detail.
- Correctly empty optional slots:
  - `solutions` is absent because MediaDB Medium 302 lists all 13 components directly.
  - The record is compositionally defined; `medium_type: DEFINED` and `composition_type: DEFINED` are appropriate.
- Bounded negative searches:
  - Exact gitignore-independent searches found no local raw MediaDB dump or Medium 302 export under `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`; only normalized/generated YAML and index/report rows are locally present.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale and lacks the normalized owner's Aug 20 4-hydroxy-L-proline grounding. | The generated merge contains no `term` for `4-Hydroxy-L-proline`; the normalized owner now has `CHEBI:18240` and an `apply_mim_groundings.py` curation event dated 2026-08-20. | Regenerate `data/merge_yaml/merged/basal_synthetic_medium_vitamins.yaml` from `data/normalized_yaml/bacterial/basal_synthetic_medium_vitamins.yaml`. |
| Major | The record omits MediaDB's own primary source and growth-data context. | MediaDB Medium 302 links source 111, organism 153, and growthdata 623; growthdata 623 reports B. amyloliquefaciens B20, growth rate 0.22 1/h, and 37.0 C, while the YAML has no `target_organisms`, `references`, temperature, or growth evidence. | `data/normalized_yaml/bacterial/basal_synthetic_medium_vitamins.yaml`; broad repeats may require `src/culturemech/import/mediadb_importer.py`. |
| Major | The MediaDB importer inserted unsupported generic preparation steps. | The YAML says to dissolve all ingredients, adjust pH if specified, and filter-sterilize at 0.22 um, but the inspected MediaDB Medium 302 page and tab-delimited export contain no preparation protocol. | `data/normalized_yaml/bacterial/basal_synthetic_medium_vitamins.yaml`; broad repeats may require `src/culturemech/import/mediadb_importer.py`. |
| Major | Two source-provided ingredient groundings are missing or overbroad. | The Medium 302 tab-delimited export gives `Ammonium phosphate` ChEBI `63051` and `Magnesium sulfate` ChEBI `31795`; the YAML leaves ammonium phosphate ungrounded and uses generic magnesium sulfate `CHEBI:32599`. | `data/normalized_yaml/bacterial/basal_synthetic_medium_vitamins.yaml`. |

## Recommended Edits

1. Ground `Ammonium phosphate` to `CHEBI:63051`, re-ground `Magnesium sulfate` from `CHEBI:32599` to `CHEBI:31795`, and keep the normalized owner's `4-Hydroxy-L-proline` exact term.
2. Add the MediaDB primary source for Hewitt et al. 1996 and the linked Medium 302/Growth Data 623 evidence.
3. Add the MediaDB growth assertion for `Bacillus amyloliquefaciens B20` with 37.0 C and growth rate 0.22 1/h if the schema can represent the measurement; otherwise preserve these details in a source-scoped evidence note.
4. Remove the three generic preparation steps unless an inspected primary source supports them.
5. Regenerate `data/merge_yaml/merged/basal_synthetic_medium_vitamins.yaml` from the normalized owner.

## Follow-up Checks

- Rerun open-schema LinkML validation, `scripts/validate_strict.py`, `linkml-term-validator`, and the reference validator on `data/normalized_yaml/bacterial/basal_synthetic_medium_vitamins.yaml` after edits.
- Regenerate the generated merge and run `just verify-merges` plus `just audit-merge-freshness`.
- Re-fetch MediaDB `/defined_media/media/302/`, `/defined_media/media_text/302/`, `/defined_media/sources/111/`, and `/defined_media/growthdata/623/` and manually compare the normalized ingredients, source, organism, growth rate, and temperature.
- Confirm the regenerated merge carries `CHEBI:18240` for 4-hydroxy-L-proline and no longer lags the normalized owner's August 2026 curation.

## Additional Notes

- The Medium 302 record is the vitamin-supplemented sibling of MediaDB Medium 301; MediaDB links both to `Hewitt et al, 1996`.
- Exact gitignore-independent searches included ignored files where present.

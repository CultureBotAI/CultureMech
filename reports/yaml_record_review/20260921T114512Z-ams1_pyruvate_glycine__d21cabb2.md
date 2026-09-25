# YAML Record Review: 'AMS1 (Pyruvate+Glycine

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ams1_pyruvate_glycine__d21cabb2.yaml
- Started UTC: 2026-09-21T11:43:55Z
- Finished UTC: 2026-09-21T11:45:12Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:007390 |
| Source | MEDIADB:482 |
| Generated path | data/merge_yaml/merged/ams1_pyruvate_glycine__d21cabb2.yaml |
| Maintained owner | data/normalized_yaml/bacterial/MEDIADB_482_AMS1_Pyruvate_Glycine.yaml |
| Merge fingerprint | d21cabb222b6ac71ccda848aa3e0d60b6f198000729ea1c2414384012f55f252 |
| Merge source | MEDIADB_482_AMS1_Pyruvate_Glycine.yaml |

`data/merge_yaml/merged/ams1_pyruvate_glycine__d21cabb2.yaml` is a generated singleton merge from `MEDIADB_482_AMS1_Pyruvate_Glycine.yaml`; curation fixes belong in the normalized owner or in the merge regeneration path, not in this merged artifact.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ams1_pyruvate_glycine__d21cabb2.yaml` under the cached Python 3.11 no-project environment. |
| Strict schema | Passed with `scripts/validate_strict.py data/merge_yaml/merged/ams1_pyruvate_glycine__d21cabb2.yaml --workers 1 --quiet`; the TSV contained 0 ERROR rows. |
| Reference validator | Passed with `linkml-reference-validator validate data ...`; no reference checks were emitted for this file. |
| Term validator | Passed with `linkml-term-validator validate-data ... --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: this repository exposes `just validate-history` for standalone records under `history/`; no documented focused validator targets embedded `MediaRecipe.curation_history` inside one merge record. |

The project-level `just validate-schema`, `just validate-strict`, and `just validate-terms` routes were not usable for this target because project installation currently attempts to build `llvmlite==0.46.0` on Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The equivalent LinkML validators passed through an offline `uv run --no-project` invocation against `/usr/local/bin/python3.11`.

## Identity and Grounding

- The stable CultureMech ID, source ID `MEDIADB:482`, and merge fingerprint identify a singleton MediaDB import.
- A gitignore-independent search across `data`, `src`, `scripts`, `history`, `conf`, `reports`, `.claude`, `justfile`, and `CLAUDE.md` found this ID in the normalized owner, generated merge, indexes, registry, archived reports, and the ungrounded-ingredient report; it found no second authoritative normalized owner for `CultureMech:007390`.
- The generated `original_name` and `media_term.term.label` are truncated to `'''AMS1 (Pyruvate+Glycine`; the live MediaDB 482 page titles the source medium as `Ams1 (pyruvate+glycine) + thiamin + methylphosphonic acid`.
- The maintained normalized owner has already repaired `original_name` and `media_term.term.label` to `AMS1 (Pyruvate+Glycine) + Thiamin + Methylphosphonic acid` with August 31 `REPAIRED_MEDIADB_TRUNCATED_NAME` curation events; the generated merge has not incorporated those repairs.
- `Methylphosphonic acid` is present at `0.001 MILLIMOLAR` and matches the variant-distinguishing compound shown on the MediaDB 482 page, but it remains ungrounded.

## Evidence

- The 20 mM-scale ingredient rows in the generated merge match the inspected MediaDB 482 compound table at a name-and-amount level, including `Methylphosphonic acid` at `0.001`, `Iron(III) chloride` at `0.000117`, and shared AMS1 basal ingredients.
- The generated row for iron is imported at the right concentration, but the generated `preferred_term` is truncated to `'''Iron(III` while MediaDB and the normalized owner both say `Iron(III) chloride`.
- The MediaDB page lists one growth-data record for `Pelagibacter sp HTCC7211 on Ams1 (pyruvate+glycine) + thiamin + methylphosphonic acid`; no target-organism assertion has been imported into this generated recipe.
- The record's generic preparation steps are unsupported by the inspected MediaDB page. The page lists the compound table and growth-data link, but it does not describe dissolving in distilled water, conditional pH adjustment, or 0.22 micron filtration for this formulation.

## Completeness

- Consequentially incomplete: the generated merge is stale relative to the repaired normalized owner, so users of `data/merge_yaml/merged` and generated pages will still see a wrong medium label and the truncated iron ingredient.
- Consequentially incomplete: the imported `Methylphosphonic acid` row has no ontology grounding despite being the distinguishing additive for this MediaDB variant.
- Consequentially incomplete: the MediaDB growth-data relationship is not represented as a scoped `target_organisms` entry, and the generated record has no source evidence attached at ingredient or growth-claim granularity.
- Empty optional slots for pH, temperature, incubation atmosphere, salinity, and storage are acceptable here; the inspected MediaDB 482 page did not provide those conditions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | The generated medium identity is stale and wrong because both `original_name` and `media_term.term.label` remain parser-truncated. | The generated merge says `'''AMS1 (Pyruvate+Glycine`; MediaDB 482 says `Ams1 (pyruvate+glycine) + thiamin + methylphosphonic acid`; the normalized owner already stores the repaired title and matching repair history. | Regenerate `data/merge_yaml/merged` from `data/normalized_yaml/bacterial/MEDIADB_482_AMS1_Pyruvate_Glycine.yaml` with `just merge-recipes`; if this file does not refresh, debug `src/culturemech/merge/merge_recipes.py`. |
| Major | The iron ingredient's preferred term is stale and parser-truncated to `'''Iron(III`. | MediaDB 482 lists `Iron(III) chloride` at `0.000117`; the normalized owner already stores `preferred_term: Iron(III) chloride`; the reviewed merge still stores the truncated string. | Same merge regeneration path as above. |
| Major | The distinguishing `Methylphosphonic acid` ingredient remains ungrounded. | The source page lists the ingredient at `0.001`, and the record preserves that name and amount but has no `term`, `mediaingredientmech_chebi_term`, or other grounded chemical ID for that ingredient. | Resolve the exact chemical in `data/normalized_yaml/bacterial/MEDIADB_482_AMS1_Pyruvate_Glycine.yaml` with the packaged MediaIngredientMech label index or leave it explicitly unresolved with a quality flag. |
| Major | The generated preparation steps are generic assertions not supported by the inspected MediaDB page. | MediaDB 482 exposes a compound table and growth-data link only; it does not state the water, pH-adjustment, or filter-sterilization procedure encoded under `preparation_steps`. | Fix the MediaDB importer or source-owned normalized records so unsupported generic protocol steps are omitted unless the source actually states them. |
| Minor | The thiamine row still carries a legacy `mediaingredientmech_term` identifier. | Other rows migrated from the old `MediaIngredientMech:NNNNNN` IDs to `mediaingredientmech_chebi_term`; thiamine still stores `MediaIngredientMech:000898`. | Refresh the authoritative normalized row with the current CHEBI-keyed MediaIngredientMech mapping if an exact mapping is available. |

## Recommended Edits

1. Regenerate merge YAML with `just merge-recipes` so `data/merge_yaml/merged/ams1_pyruvate_glycine__d21cabb2.yaml` reflects the repaired `original_name`, `media_term.term.label`, `Iron(III) chloride` preferred term, and August 31 normalized curation history from `data/normalized_yaml/bacterial/MEDIADB_482_AMS1_Pyruvate_Glycine.yaml`.
2. If merge regeneration still emits the stale strings, fix `src/culturemech/merge/merge_recipes.py` or the merge input selection so the generated singleton is rebuilt from the current normalized source.
3. Ground `Methylphosphonic acid` only if an exact MediaIngredientMech or ontology term is verified; otherwise add a concrete unresolved-ingredient quality flag to the normalized MediaDB 482 owner.
4. Remove or gate the generic MediaDB `DISSOLVE`, `ADJUST_PH`, and `FILTER_STERILIZE` steps unless a MediaDB source or primary publication explicitly supports them for this formulation.
5. Revisit the lingering `mediaingredientmech_term` on thiamine and migrate it to the CHEBI-keyed MediaIngredientMech field only after verifying exact identity.

## Follow-up Checks

1. Run `just merge-recipes`, then confirm the regenerated `data/merge_yaml/merged/ams1_pyruvate_glycine__d21cabb2.yaml` contains `AMS1 (Pyruvate+Glycine) + Thiamin + Methylphosphonic acid`, `Iron(III) chloride`, and the August 31 curation events.
2. Run `just verify-merges` and `just audit-merge-freshness --fail-on-drift` to prove the merged corpus is current relative to `data/normalized_yaml`.
3. Run the focused schema, strict, term, and reference validators on the regenerated merge record.
4. Re-inspect MediaDB 482 or the MediaDB SQL source after any `Methylphosphonic acid` grounding to ensure the added ontology term denotes the exact compound string imported by MediaDB.

## Additional Notes

- The bounded identity search used `rg --no-ignore --hidden`; ignored paths were included for the searched roots.
- The generated record has 20 ingredients, matching the MediaDB 482 page's `20 Compounds` table.
- The MediaDB source page was fetched directly from `https://mediadb.systemsbiology.net/defined_media/media/482/` during this review.

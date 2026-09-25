# YAML Record Review: 'AMS1 (Pyruvate+Serine

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ams1_pyruvate_serine__5ccdd830.yaml
- Started UTC: 2026-09-21T11:46:27Z
- Finished UTC: 2026-09-21T11:47:47Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:007384 |
| Source | MEDIADB:477 |
| Generated path | data/merge_yaml/merged/ams1_pyruvate_serine__5ccdd830.yaml |
| Maintained owner | data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml |
| Merge fingerprint | 5ccdd8305c7a6acd04fe8148e51b04e0538cca75b668f6d109a27ce5c16b2c9c |
| Merge source | ams1_pyruvate_serine.yaml |

`data/merge_yaml/merged/ams1_pyruvate_serine__5ccdd830.yaml` is a generated singleton merge from `data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml`; curation fixes belong in the normalized owner or in the merge regeneration path, not in this merged artifact.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ams1_pyruvate_serine__5ccdd830.yaml` under the cached Python 3.11 no-project environment. |
| Strict schema | Passed with `scripts/validate_strict.py data/merge_yaml/merged/ams1_pyruvate_serine__5ccdd830.yaml --workers 1 --quiet`; the TSV contained 0 ERROR rows. |
| Reference validator | Passed with `linkml-reference-validator validate data ...`; no reference checks were emitted for this file. |
| Term validator | Passed with `linkml-term-validator validate-data ... --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: this repository exposes `just validate-history` for standalone records under `history/`; no documented focused validator targets embedded `MediaRecipe.curation_history` inside one merge record. |

The project-level `just validate-schema`, `just validate-strict`, and `just validate-terms` routes were not usable for this target because project installation currently attempts to build `llvmlite==0.46.0` on Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The equivalent LinkML validators passed through an offline `uv run --no-project` invocation against `/usr/local/bin/python3.11`.

## Identity and Grounding

- The stable CultureMech ID, source ID `MEDIADB:477`, and merge fingerprint identify a singleton MediaDB import.
- A gitignore-independent search across `data`, `src`, `scripts`, `history`, `conf`, `reports`, `.claude`, `justfile`, and `CLAUDE.md` found this ID in the registry-owned normalized owner, generated merge, indexes, registry, and archived reports; it found no second authoritative normalized owner for `CultureMech:007384`.
- The generated `original_name` and `media_term.term.label` are truncated to `'''AMS1 (Pyruvate+Serine`; the live MediaDB 477 page titles the source medium as `Ams1 (pyruvate+serine)`.
- The maintained normalized owner has already repaired `original_name` and `media_term.term.label` to `AMS1 (Pyruvate+Serine)` with August 31 `REPAIRED_MEDIADB_TRUNCATED_NAME` curation events; the generated merge has not incorporated those repairs.
- `4-Amino-5-hydroxymethyl-2-methylpyrimidine` is present at `1e-05 MILLIMOLAR` and matches the distinguishing compound shown on the MediaDB 477 page, but it remains ungrounded.

## Evidence

- The 20 mM-scale ingredient rows in the generated merge match the inspected MediaDB 477 compound table at a name-and-amount level, including `4-Amino-5-hydroxymethyl-2-methylpyrimidine` at `1e-05`, `L-Serine` at `0.05`, and `Iron(III) chloride` at `0.000117`.
- The generated row for iron is imported at the right concentration, but the generated `preferred_term` is truncated to `'''Iron(III` while MediaDB and the normalized owner both say `Iron(III) chloride`.
- The MediaDB page lists two growth-data records: `Pelagibacter sp HTCC7211 on Ams1 (pyruvate+serine)` and `Pelagibacter ubique HTCC1062 on Ams1 (pyruvate+serine)`; no target-organism assertion has been imported into this generated recipe.
- The record's generic preparation steps are unsupported by the inspected MediaDB page. The page lists the compound table and growth-data links, but it does not describe dissolving in distilled water, conditional pH adjustment, or 0.22 micron filtration for this formulation.

## Completeness

- Consequentially incomplete: the generated merge is stale relative to the repaired normalized owner, so users of `data/merge_yaml/merged` and generated pages will still see a wrong medium label and the truncated iron ingredient.
- Consequentially incomplete: the imported `4-Amino-5-hydroxymethyl-2-methylpyrimidine` row has no ontology grounding despite being the distinguishing additive for this MediaDB variant.
- Consequentially incomplete: the MediaDB growth-data relationships are not represented as scoped `target_organisms` entries, and the generated record has no source evidence attached at ingredient or growth-claim granularity.
- Empty optional slots for pH, temperature, incubation atmosphere, salinity, and storage are acceptable here; the inspected MediaDB 477 page did not provide those conditions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | The generated medium identity is stale and wrong because both `original_name` and `media_term.term.label` remain parser-truncated. | The generated merge says `'''AMS1 (Pyruvate+Serine`; MediaDB 477 says `Ams1 (pyruvate+serine)`; the normalized owner already stores the repaired title and matching repair history. | Regenerate `data/merge_yaml/merged` from `data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml` with `just merge-recipes`; if this file does not refresh, debug `src/culturemech/merge/merge_recipes.py`. |
| Major | The iron ingredient's preferred term is stale and parser-truncated to `'''Iron(III`. | MediaDB 477 lists `Iron(III) chloride` at `0.000117`; the normalized owner already stores `preferred_term: Iron(III) chloride`; the reviewed merge still stores the truncated string. | Same merge regeneration path as above. |
| Major | The distinguishing `4-Amino-5-hydroxymethyl-2-methylpyrimidine` ingredient remains ungrounded. | The source page lists the ingredient at `1e-05`, and the record preserves that name and amount but has no `term`, `mediaingredientmech_chebi_term`, or other grounded chemical ID for that ingredient. | Resolve the exact chemical in `data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml` with the packaged MediaIngredientMech label index or leave it explicitly unresolved with a quality flag. |
| Major | The generated preparation steps are generic assertions not supported by the inspected MediaDB page. | MediaDB 477 exposes a compound table and growth-data links only; it does not state the water, pH-adjustment, or filter-sterilization procedure encoded under `preparation_steps`. | Fix the MediaDB importer or source-owned normalized records so unsupported generic protocol steps are omitted unless the source actually states them. |
| Major | MediaDB growth-data links are omitted from `target_organisms`. | The source page links growth data for `Pelagibacter sp HTCC7211` and `Pelagibacter ubique HTCC1062`; the generated record has no scoped target-organism entries. | Import growth-data records into the normalized MediaDB owner with evidence scoped to each tested strain and medium variant. |

## Recommended Edits

1. Regenerate merge YAML with `just merge-recipes` so `data/merge_yaml/merged/ams1_pyruvate_serine__5ccdd830.yaml` reflects the repaired `original_name`, `media_term.term.label`, `Iron(III) chloride` preferred term, and August 31 normalized curation history from `data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml`.
2. If merge regeneration still emits the stale strings, fix `src/culturemech/merge/merge_recipes.py` or the merge input selection so the generated singleton is rebuilt from the current normalized source.
3. Ground `4-Amino-5-hydroxymethyl-2-methylpyrimidine` only if an exact MediaIngredientMech or ontology term is verified; otherwise add a concrete unresolved-ingredient quality flag to the normalized MediaDB 477 owner.
4. Import the MediaDB 477 growth-data rows only as variant-scoped `target_organisms`; do not generalize them to other AMS1 pyruvate/serine or pyruvate/glycine formulations.
5. Remove or gate the generic MediaDB `DISSOLVE`, `ADJUST_PH`, and `FILTER_STERILIZE` steps unless a MediaDB source or primary publication explicitly supports them for this formulation.

## Follow-up Checks

1. Run `just merge-recipes`, then confirm the regenerated `data/merge_yaml/merged/ams1_pyruvate_serine__5ccdd830.yaml` contains `AMS1 (Pyruvate+Serine)`, `Iron(III) chloride`, and the August 31 curation events.
2. Run `just verify-merges` and `just audit-merge-freshness --fail-on-drift` to prove the merged corpus is current relative to `data/normalized_yaml`.
3. Run the focused schema, strict, term, and reference validators on the regenerated merge record.
4. Re-inspect the two MediaDB 477 growth-data pages before adding target-organism evidence so each growth claim is scoped to the correct strain and outcome.
5. Re-inspect MediaDB 477 or the MediaDB SQL source after any `4-Amino-5-hydroxymethyl-2-methylpyrimidine` grounding to ensure the added ontology term denotes the exact compound string imported by MediaDB.

## Additional Notes

- The bounded identity search used `rg --no-ignore --hidden`; ignored paths were included for the searched roots.
- The generated record has 20 ingredients, matching the MediaDB 477 page's `20 Compounds` table.
- The MediaDB source page was fetched directly from `https://mediadb.systemsbiology.net/defined_media/media/477/` during this review.

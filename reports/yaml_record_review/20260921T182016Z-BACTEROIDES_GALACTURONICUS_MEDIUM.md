# YAML Record Review: BACTEROIDES GALACTURONICUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACTEROIDES_GALACTURONICUS_MEDIUM.yaml
- Started UTC: 2026-09-21T18:20:15Z
- Finished UTC: 2026-09-21T18:20:15Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:004022 |
| Name | bacteroides_galacturonicus_medium |
| Original name | BACTEROIDES GALACTURONICUS medium |
| Maintained canonical input | data/normalized_yaml/bacterial/KOMODO_1265_BACTEROIDES_GALACTURONICUS_medium.yaml |
| Merge participant | data/normalized_yaml/bacterial/bacteroides_galacturonicus_medium.yaml |
| Primary checked source | DSMZ Medium 1265 PDF |
| Generated status | Generated merge under data/merge_yaml/merged; future fixes belong in normalized inputs or source/import and merge rules |

The generated record is the KOMODO Medium 1265 copy of DSMZ Medium 1265, merged with the DSMZ normalized duplicate.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACTEROIDES_GALACTURONICUS_MEDIUM.yaml` | Passed with exit 0 |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BACTEROIDES_GALACTURONICUS_MEDIUM.yaml --out /private/tmp/BACTEROIDES_GALACTURONICUS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 ERROR rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BACTEROIDES_GALACTURONICUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BACTEROIDES_GALACTURONICUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented; `just validate-history` targets standalone `history/` files. |

The repository `just` validators were not used for this target because the project environment currently fails while syncing the Python 3.13 dependency set. The equivalent no-project validators above ran against the checked-in schema and target file.

## Identity and Grounding

The KOMODO and DSMZ records agree on DSMZ Medium 1265, and DSMZ identifies that source as `BACTEROIDES GALACTURONICUS MEDIUM`. The quantities for sodium polygalacturonate, Trypticase, yeast extract, `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, `FeSO4 x 7 H2O`, `(NH4)2SO4`, L-cysteine, resazurin, and `NaHCO3` match DSMZ after milligrams are expressed as grams per liter.

Grounding is incomplete or wrong for the complex ingredients:

- `Trypticase` is grounded to `CHEBI:78018` / dodecylphosphocholine, which is unrelated to the DSMZ ingredient. The row still carries a legacy `MediaIngredientMech:000263` label for Trypticase, and the packaged MediaIngredientMech label index now maps exact `Trypticase` to `MICRO:0000175`.
- `Yeast extract` is ungrounded even though the packaged label index contains exact `Yeast extract` / `Yeast Extract` rows mapped to `FOODON:03315426`.
- `Sodium polygalacturonate` is explicit but ungrounded. An ignored-inclusive search of the packaged label index for `Sodium polygalacturonate|sodium polygalacturonate` found no exact local mapping, so this absence is a bounded unresolved gap rather than a defect by itself.

## Evidence

DSMZ Medium 1265 supports all ten non-water rows and their amounts: 4 g sodium polygalacturonate, 5 g Trypticase, 2.5 g yeast extract, 2.5 g magnesium sulfate heptahydrate, 0.15 g calcium chloride dihydrate, 20 mg ferrous sulfate heptahydrate, 1.4 g ammonium sulfate, 1 g L-cysteine, 1 mg resazurin, and 2 g sodium bicarbonate per liter.

DSMZ also supports pH 7.1 and explicitly prepares the medium under 100% N2. The generated KOMODO canonical lacks preparation steps and instead leaves only a `notes` suffix that says `Aerobic: Yes`, which conflicts with the DSMZ gas context.

No inspected source supports dodecylphosphocholine as a synonym, component, or grounding for Trypticase in this medium.

## Completeness

- DSMZ includes 1000 ml distilled water; the generated record omits water.
- DSMZ says to adjust to pH 7.1 and use a 100% N2 gas atmosphere; this is only present in the DSMZ normalized duplicate and is lost from the generated canonical.
- DSMZ prepares NaHCO3 as a 5% w/v filter-sterilized solution added after autoclaving; this preparation step is present in `data/normalized_yaml/bacterial/bacteroides_galacturonicus_medium.yaml` and absent from the generated record.
- Empty organism, strain, growth-evidence, stock-solution, and publication-reference fields are not automatically defects for this source-derived medium; DSMZ 1265 is sufficient evidence for the recipe but not for taxon-specific growth claims.

A gitignore-independent search of `reports/yaml_record_review` for `BACTEROIDES_GALACTURONICUS_MEDIUM|bacteroides_galacturonicus_medium` found no existing report for this target before this report was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Trypticase has a wrong CHEBI grounding. | DSMZ lists Trypticase, not dodecylphosphocholine. The packaged label index maps exact Trypticase to `MICRO:0000175`, while both normalized owners carry `term.id: CHEBI:78018`. | Ingredient grounding in the KOMODO and DSMZ normalized records, using the packaged MediaIngredientMech label index |
| Major | DSMZ preparation and anaerobic gas context are dropped from the generated canonical record. | DSMZ says to prepare the medium under 100% N2 and to add filter-sterilized 5% w/v NaHCO3 after autoclaving. The DSMZ normalized duplicate preserves both steps; the KOMODO canonical and generated merge have none. | KOMODO DSMZ enrichment or merge canonicalization so exact source duplicates preserve preparation steps |
| Major | The generated record contradicts DSMZ by retaining `Aerobic: Yes`. | DSMZ Medium 1265 uses a 100% N2 gas atmosphere. The generated record's only atmosphere cue is a KOMODO note saying the medium is aerobic. | KOMODO import notes or DSMZ enrichment for cited DSMZ media |
| Major | Distilled water is missing. | DSMZ lists distilled water 1000 ml, but neither normalized owner nor the generated record has a water ingredient row. | DSMZ/KOMODO import and normalization |
| Major | Yeast extract is missing an available exact grounding. | The record leaves Yeast extract ungrounded; the packaged label index maps exact Yeast extract to `FOODON:03315426`. | Ingredient grounding in the KOMODO and DSMZ normalized records, using the packaged label index |

## Recommended Edits

1. Replace the dodecylphosphocholine grounding on Trypticase with the exact packaged `MICRO:0000175` mapping, preserving Trypticase as the supplied ingredient text.
2. Add or merge-preserve the DSMZ preparation steps for pH 7.1, 100% N2 preparation, and post-autoclave filter-sterilized 5% w/v NaHCO3 addition.
3. Remove or correct the KOMODO `Aerobic: Yes` note when DSMZ-cited anaerobic instructions are present.
4. Add the DSMZ 1000 ml distilled-water row to the maintained representation.
5. Link Yeast extract to the exact `FOODON:03315426` mapping from `src/culturemech/data/mediaingredientmech/label_index.csv`.
6. Leave Sodium polygalacturonate explicitly ungrounded unless a curated exact term is added to the packaged mapping workflow.
7. Regenerate `data/merge_yaml/merged/BACTEROIDES_GALACTURONICUS_MEDIUM.yaml` and generated pages from the corrected normalized data.

## Follow-up Checks

- Rerun the open-schema, strict, reference, and term validators on both normalized inputs and the regenerated merge record.
- Rerun `just verify-merges` and `just audit-merge-freshness` after regeneration to confirm the exact KOMODO/DSMZ duplicate still merges and no preparation data is lost.
- Inspect the regenerated ingredient rows to confirm Trypticase has no CHEBI dodecylphosphocholine term and no stale legacy `mediaingredientmech_term`.
- Compare the regenerated preparation steps against DSMZ 1265 to confirm NaHCO3 remains scoped as a separately prepared 5% solution rather than a second top-level ingredient.

## Additional Notes

- `FeSO4 x 7 H2O` is correct at 0.02 g/L because DSMZ gives that row as 20 mg.
- The exact ignored-inclusive pre-report search covered `reports/yaml_record_review`; no prior report for this target was present.
- `Sodium polygalacturonate` should not be forced to a broader pectin or polygalacturonate term without explicit curation, because the sodium salt identity is part of the source label.

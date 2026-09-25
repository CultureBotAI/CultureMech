# YAML Record Review: BEIJERINCKIA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml
- Started UTC: 2026-09-21T19:40:55Z
- Finished UTC: 2026-09-21T19:42:20Z
- Verdict: needs curation

## Target

- Reviewed `data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml`.
- Class: `MediaRecipe`.
- ID: `CultureMech:003822`.
- Name: `beijerinckia_medium`.
- Original name: `BEIJERINCKIA MEDIUM`.
- Source identity: `komodo.medium:111`, label `BEIJERINCKIA MEDIUM`; the KOMODO owner cites DSMZ Medium 111.
- Generated status: derived merge output under `data/merge_yaml/merged/`; future curation belongs in the normalized duplicate owners followed by merge regeneration.
- Maintained owners:
  - `data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml`, `CultureMech:003822`, `komodo.medium:111`.
  - `data/normalized_yaml/bacterial/beijerinckia_medium.yaml`, `CultureMech:000556`, `mediadive.medium:111`.
- Merge metadata: `SOURCE_DUPLICATE` merge of `KOMODO_111_BEIJERINCKIA_MEDIUM` and `beijerinckia_medium` on fingerprint `4d3f3ad5f9242ef2a21b4778100b39da12423332e0294080c3c5e5140c591bcf`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml` via the no-project Python 3.11 workaround | Passed |
| Closed-schema strict validation, `scripts/validate_strict.py data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml --out /private/tmp/BEIJERINCKIA_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were applicable |
| `linkml-term-validator validate-data data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `MediaRecipe.curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not a focused embedded-history validator for one merged record |

The documented `just` commands were not run directly because the project runtime currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` before target-specific validation.

## Identity and Grounding

- `CultureMech:003822` resolves in `data/culturemech_id_registry.tsv` to `data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml`; the merged DSMZ duplicate `CultureMech:000556` resolves to `data/normalized_yaml/bacterial/beijerinckia_medium.yaml`.
- MediaDive JSON, the rendered MediaDive page, and the linked DSMZ PDF all identify DSMZ Medium 111 as `BEIJERINCKIA MEDIUM`, source DSMZ, pH 6.5.
- KOMODO Medium 111 explicitly cites DSMZ Medium 111 and has the same ingredient and concentration signatures as the DSMZ owner, so the source-duplicate merge is plausible.
- The record should not be confused with `BEIJERINCKIA MEDIUM (LMG 18)` or `Beijerinckia medium for isolation`; those similarly named normalized and merged records carry different slugs and sources.

## Evidence

- DSMZ/MediaDive Medium 111 lists 10 g glucose, 0.8 g K2HPO4, 0.2 g KH2PO4, 0.1 g magnesium sulfate heptahydrate, 20 mg ferrous sulfate heptahydrate, 2 mg manganese sulfate hexahydrate, 5 mg zinc sulfate hexahydrate, 4 mg copper sulfate hexahydrate, 5 mg sodium molybdate dihydrate, and 15 g agar.
- DSMZ/MediaDive lists 950 ml distilled water in the table and then explains that glucose is sterilized separately as 10 g in 50 ml water and mixed after cooling. The 950 ml main volume plus 50 ml glucose solution makes a 1000 ml final medium.
- Both normalized owners converted the source rows through the 950 ml MediaDive solution volume, yielding values such as `10.5263` g/L glucose and `15.7895` g/L agar. Those values are correct per 950 ml but too high for the final 1000 ml medium specified by the source procedure.
- DSMZ/MediaDive says to adjust pH to 6.5 and sterilize glucose separately. The DSMZ owner preserves that instruction, but the KOMODO owner and the generated KOMODO-canonical merge omit `preparation_steps`.
- A gitignore-independent search over `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` for the exact CultureMech IDs, digit-bounded KOMODO/MediaDive 111 source IDs, digit-bounded `DSMZ Medium 111`, and the source owner slugs found the two normalized owners, generated indexes, the generated merge, distinct LMG 18 and isolation Beijerinckia records, organism curation candidates, and import-priority reports. It did not find a repository-owned raw KOMODO or MediaDive capture for the reviewed Medium 111 records.

## Completeness

- Consequentially incomplete: the source's 950 ml distilled-water row and separate 50 ml glucose solution are not represented, so the record cannot express why the source table uses 950 ml water.
- Consequentially incomplete: every concentration has been scaled to the 950 ml main solution, not the 1000 ml final medium after the glucose solution is mixed in.
- Consequentially incomplete in the generated KOMODO-canonical merge: the DSMZ preparation step is absent even though the DSMZ duplicate owner carries it.
- Empty target-organism, growth-evidence, storage, and variant slots are acceptable here; DSMZ Medium 111 gives no strain-specific growth result, storage condition, or variant recipe in the inspected source.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | All ingredient rows are scaled to the 950 ml main solution rather than the source's final 1000 ml medium. The source's table amounts should either be preserved with the 950 ml water plus 50 ml glucose-solution boundary, or normalized against 1000 ml final volume. | `data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml` and `data/normalized_yaml/bacterial/beijerinckia_medium.yaml` |
| Major | The 950 ml distilled-water row and separately sterilized 10 g/50 ml glucose solution are not machine-readable. | `data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml` and `data/normalized_yaml/bacterial/beijerinckia_medium.yaml` |
| Major | The generated KOMODO-canonical record lacks the pH/glucose sterilization preparation step, so it drops the instruction to adjust to pH 6.5, sterilize glucose separately, and mix after cooling. | `data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml`, then merge regeneration |

## Recommended Edits

1. In both normalized duplicate owners, represent the DSMZ 950 ml water component and the separate 10 g glucose in 50 ml water preparation boundary.
2. Correct the ingredient concentration values so they are not computed as final g/L over 950 ml. Either preserve the source table amounts with explicit solution volumes, or normalize the rows to the 1000 ml final volume after glucose is mixed in.
3. Copy or regenerate the DSMZ pH/glucose sterilization preparation step into the KOMODO owner.
4. Regenerate `data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml` after both owners are corrected.

## Follow-up Checks

- Rerun the open schema validator, `scripts/validate_strict.py`, `linkml-term-validator`, and `linkml-reference-validator` on both normalized owners and the regenerated merged record.
- Rerun the repository merge verifier documented for duplicate-owner changes to prove `data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml` reflects the corrected owners.
- Manually compare the regenerated record against the DSMZ Medium 111 PDF or MediaDive 111 JSON and verify 950 ml distilled water, 10 g glucose in 50 ml water, pH 6.5, and post-cooling glucose mixing are all represented without 950 ml rescaling.

## Additional Notes

- MediaDive JSON, the MediaDive rendered page, and the DSMZ PDF agreed for every inspected ingredient, amount, final-volume clue, and preparation instruction.
- Reports are read-only review artifacts; no normalized recipe, generated merge, page, history entry, or GitHub issue was edited for this review.

# YAML Record Review: BEIJERINCKIA DOEBEREINERAE MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
- Started UTC: 2026-09-21T19:39:18Z
- Finished UTC: 2026-09-21T19:40:44Z
- Verdict: needs curation

## Target

- Reviewed `data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml`.
- Class: `MediaRecipe`.
- ID: `CultureMech:003966`.
- Name: `beijerinckia_doebereinerae_medium`.
- Original name: `BEIJERINCKIA DOEBEREINERAE MEDIUM`.
- Source identity: `komodo.medium:1215`, label `BEIJERINCKIA DOEBEREINERAE MEDIUM`; the KOMODO owner cites DSMZ Medium 1215.
- Generated status: derived merge output under `data/merge_yaml/merged/`; future curation belongs in the normalized duplicate owners followed by merge regeneration.
- Maintained owners:
  - `data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml`, `CultureMech:003966`, `komodo.medium:1215`.
  - `data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml`, `CultureMech:000673`, `mediadive.medium:1215`.
- Merge metadata: `SOURCE_DUPLICATE` merge of `KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM` and `beijerinckia_doebereinerae_medium` on fingerprint `de031d8f4f56beff5dcfa863c52273e92f7f7c9113757f3658d41c30b012eb1d`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml` via the no-project Python 3.11 workaround | Passed |
| Closed-schema strict validation, `scripts/validate_strict.py data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml --out /private/tmp/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were applicable |
| `linkml-term-validator validate-data data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `MediaRecipe.curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not a focused embedded-history validator for one merged record |

The documented `just` commands were not run directly because the project runtime currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` before target-specific validation.

## Identity and Grounding

- `CultureMech:003966` resolves in `data/culturemech_id_registry.tsv` to `data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml`; the merged DSMZ duplicate `CultureMech:000673` resolves to `data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml`.
- MediaDive JSON, the rendered MediaDive page, and the linked DSMZ PDF all identify DSMZ Medium 1215 as `BEIJERINCKIA DOEBEREINERAE MEDIUM`, source DSMZ, pH 6.5.
- KOMODO Medium 1215 explicitly cites DSMZ Medium 1215 and has the same pH, ingredient list, physical state, and concentration signatures as the DSMZ owner, so the source-duplicate merge is plausible.
- The curated salt and glucose ingredient groundings match the exact hydrates and salts named by DSMZ, including `Na2MoO4 x 7 H2O` at 5 mg/L.

## Evidence

- DSMZ/MediaDive Medium 1215 supports the seven non-agar, non-water ingredient rows in the current record: 0.8 g KH2PO4, 0.2 g K2HPO4, 0.5 g magnesium sulfate heptahydrate, 0.1 g ferric chloride hexahydrate, 0.05 g calcium chloride dihydrate, 5 mg sodium molybdate heptahydrate, and 20 g glucose per 1000 ml.
- DSMZ/MediaDive supports pH 6.5 and `15` `G_PER_L` agar for solid media.
- DSMZ/MediaDive also lists 1000 ml distilled water, which is absent from both normalized duplicate owners and from the generated merge.
- DSMZ/MediaDive contains the preparation step `Final pH is 6.5. Add 15.0 g/l agar for solid media.` The DSMZ owner preserves that instruction, but the KOMODO owner and the KOMODO-canonical generated merge omit `preparation_steps`.
- A gitignore-independent search over `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` for the exact CultureMech IDs, digit-bounded KOMODO/MediaDive 1215 source IDs, digit-bounded `DSMZ Medium 1215`, and both owner slugs found the two normalized owners, the generated merge, generated indexes, organism-review candidates, and import-priority reports. It did not find a repository-owned raw KOMODO or MediaDive capture for the reviewed Medium 1215 records.

## Completeness

- Consequentially incomplete: the source's 1000 ml distilled-water solvent row is absent from machine-readable composition in both normalized owners.
- Consequentially incomplete in the generated KOMODO-canonical merge: the DSMZ preparation step is absent even though the DSMZ duplicate owner carries it.
- The agar condition is complete enough for this import: the record has a 15 g/L agar row marked `for solid medium`, matching DSMZ's conditional agar instruction.
- Empty target-organism, growth-evidence, storage, and variant slots are acceptable here; DSMZ Medium 1215 gives no strain-specific growth result, storage condition, or variant recipe in the inspected source.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | The 1000 ml distilled-water row from DSMZ Medium 1215 is missing. | `data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml` and `data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml` |
| Major | The generated KOMODO-canonical record lacks the source preparation step. The generated row has `ph_value: 6.5` and the 15 g/L agar row, but drops DSMZ's explicit final-pH/solid-agar instruction. | `data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml`, then merge regeneration |

## Recommended Edits

1. Add the DSMZ 1000 ml distilled-water component to both normalized duplicate owners so the final-volume basis is explicit.
2. Copy or regenerate the DSMZ final-pH/agar preparation step into the KOMODO owner instead of relying on the DSMZ duplicate owner to hold that instruction.
3. Regenerate `data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml` after both owners are corrected.

## Follow-up Checks

- Rerun the open schema validator, `scripts/validate_strict.py`, `linkml-term-validator`, and `linkml-reference-validator` on both normalized owners and the regenerated merged record.
- Rerun the repository merge verifier documented for duplicate-owner changes to prove `data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml` reflects the corrected owners.
- Manually compare the regenerated record against the DSMZ Medium 1215 PDF or MediaDive 1215 JSON and verify 1000 ml distilled water, pH 6.5, and 15 g/L agar for solid media are all represented.

## Additional Notes

- MediaDive JSON, the MediaDive rendered page, and the DSMZ PDF agreed for every inspected ingredient, amount, physical-state qualifier, and preparation instruction.
- Reports are read-only review artifacts; no normalized recipe, generated merge, page, history entry, or GitHub issue was edited for this review.

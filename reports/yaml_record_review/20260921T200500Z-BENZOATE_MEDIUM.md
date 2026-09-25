# YAML Record Review: Benzoate Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BENZOATE_MEDIUM.yaml
- Started UTC: 2026-09-21T20:03:00Z
- Finished UTC: 2026-09-21T20:05:00Z
- Verdict: needs curation

## Target

- Reviewed `data/merge_yaml/merged/BENZOATE_MEDIUM.yaml`.
- Class: `MediaRecipe`.
- ID: `CultureMech:007662`.
- Name: `benzoate_medium`.
- Original name: `Benzoate Medium`.
- Source identity: `TOGO:M113`, label `Benzoate Medium`; TOGO metadata says `original_media_id: JCM_M121` and links JCM GRMD 121.
- Generated status: derived merge output under `data/merge_yaml/merged/`; the maintained owner is `data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml`.
- Merge metadata: one source record, `TOGO_M113_Benzoate_Medium`, on fingerprint `372c17805e8d0b0edfc2a3c04b96bb08494371bfb218acd8e810c038fd2d204a`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BENZOATE_MEDIUM.yaml` via the no-project Python 3.11 workaround | Passed |
| Closed-schema strict validation, `scripts/validate_strict.py data/merge_yaml/merged/BENZOATE_MEDIUM.yaml --out /private/tmp/BENZOATE_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/BENZOATE_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were applicable |
| `linkml-term-validator validate-data data/merge_yaml/merged/BENZOATE_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `MediaRecipe.curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not a focused embedded-history validator for one merged record |

The documented `just` commands were not run directly because the project runtime currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` before target-specific validation.

## Identity and Grounding

- `CultureMech:007662` resolves in `data/culturemech_id_registry.tsv` to `data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml`.
- TOGO M113, JCM GRMD 121, the source URL, and the imported label all denote JCM Benzoate Medium.
- Sodium benzoate correctly distinguishes this recipe from adjacent benzoate-free mineral media and is represented as a defined 3 g/L organic component.
- Magnesium sulfate heptahydrate, sodium chloride, potassium dihydrogen phosphate, diammonium hydrogen phosphate, sodium benzoate, and water are correctly grounded to the exact supplied forms; yeast extract and Noble agar are mixture/source-product rows that should not be forced to a small-molecule ChEBI term.

## Evidence

- TOGO M113 supports 1 L distilled water, 0.2 g MgSO4 x 7H2O, 0.5 g yeast extract, 5 g NaCl, 1.2 g KH2PO4, 3 g (NH4)2HPO4, 20 g Noble agar from BD-Difco, and 3 g sodium benzoate.
- JCM GRMD 121 agrees with TOGO M113 on the source identity, all eight component names, and all eight amounts.
- JCM GRMD 121 says sodium benzoate is filter-sterilized separately and aseptically added to the medium. The current record has no `preparation_steps`, so the sodium-benzoate addition is indistinguishable from the main autoclaved mixture.
- The maintained owner stores TOGO's 1 L distilled water item as `value: '1'` with `unit: G_PER_L`; this is neither the source unit nor a dimensionally meaningful final water concentration.
- A gitignore-independent exact search over the maintained owner, generated merge, ID registry, recipe catalog, and TOGO indexes found the expected `CultureMech:007662` owner and generated record references. It did not find a raw TOGO M113 or JCM 121 source payload committed for this source record.

## Completeness

- The non-water formulation is complete and source-supported.
- Consequentially incorrect: distilled water has the wrong unit.
- Consequentially incomplete: sodium benzoate's separate filtration and aseptic addition are absent from preparation.
- Empty target-organism and growth-evidence slots are acceptable here; TOGO M113 and JCM GRMD 121 do not name a strain-specific growth result.
- Empty `ph_value` is acceptable; the inspected TOGO and JCM records do not state a pH.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | TOGO's `1 L` distilled water row was normalized as `1` `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml` |
| Major | The JCM instruction to filter-sterilize sodium benzoate separately and aseptically add it is missing. | `data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml` |

## Recommended Edits

1. Correct the distilled-water amount to source-faithful `1 L` or omit water consistently if this importer treats solvent water as implied.
2. Add preparation steps that keep the main autoclaved mixture separate from filter sterilization and aseptic addition of sodium benzoate.
3. Regenerate `data/merge_yaml/merged/BENZOATE_MEDIUM.yaml` after the normalized owner is corrected.

## Follow-up Checks

- Rerun the open schema validator, `scripts/validate_strict.py`, `linkml-term-validator`, and `linkml-reference-validator` on `data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml` and the regenerated merged record.
- Manually compare the regenerated record against the TOGO M113 JSON and JCM GRMD 121 to verify all eight TOGO component rows and the filtered sodium-benzoate addition survive with source-faithful units.

## Additional Notes

- Reports are read-only review artifacts; no normalized recipe, generated merge, page, history entry, or GitHub issue was edited for this review.

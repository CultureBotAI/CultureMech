# YAML Record Review: BENZOATE MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/benzoate_medium__fda674fb.yaml
- Started UTC: 2026-09-21T20:07:20Z
- Finished UTC: 2026-09-21T20:08:40Z
- Verdict: pass with minor issues

## Target

- Reviewed `data/merge_yaml/merged/benzoate_medium__fda674fb.yaml`.
- Class: `MediaRecipe`.
- ID: `CultureMech:002388`.
- Name: `benzoate_medium`.
- Original name: `BENZOATE MEDIUM`.
- Source identity: `mediadive.medium:J121`, label `BENZOATE MEDIUM`, with a JCM GRMD 121 link in `notes`.
- Generated status: derived merge output under `data/merge_yaml/merged/`; the maintained owner is `data/normalized_yaml/bacterial/benzoate_medium.yaml`.
- Merge metadata: one source record, `benzoate_medium.yaml`, on fingerprint `fda674fbebd08f4a9d2c3db7eaa8fe0e1ebf7da26bddb15ae0b7122e6c03fc10`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/benzoate_medium__fda674fb.yaml` via the no-project Python 3.11 workaround | Passed |
| Closed-schema strict validation, `scripts/validate_strict.py data/merge_yaml/merged/benzoate_medium__fda674fb.yaml --out /private/tmp/benzoate_medium__fda674fb.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/benzoate_medium__fda674fb.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were applicable |
| `linkml-term-validator validate-data data/merge_yaml/merged/benzoate_medium__fda674fb.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `MediaRecipe.curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not a focused embedded-history validator for one merged record |

The documented `just` commands were not run directly because the project runtime currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` before target-specific validation.

## Identity and Grounding

- `CultureMech:002388` resolves in `data/culturemech_id_registry.tsv` to `data/normalized_yaml/bacterial/benzoate_medium.yaml`.
- MediaDive/JCM `J121`, JCM GRMD 121, the source URL, and the imported label all denote JCM Benzoate Medium.
- This record is the MediaDive/JCM sibling of the TOGO M113 JCM import; it keeps the source's final 3 g/L sodium benzoate amount and the filter-sterilization instruction.
- Diammonium hydrogen phosphate, potassium dihydrogen phosphate, sodium chloride, magnesium sulfate heptahydrate, sodium benzoate, and agar are correctly grounded to the exact supplied forms; yeast extract is a mixture row and should remain without a ChEBI small-molecule term.

## Evidence

- JCM GRMD 121 supports 3 g/L (NH4)2HPO4, 1.2 g/L KH2PO4, 5 g/L NaCl, 0.2 g/L MgSO4 x 7 H2O, 0.5 g/L yeast extract, 3 g/L sodium benzoate, 20 g/L Noble agar, and 1 L distilled water.
- The current record's seven non-water ingredient amounts agree with the source. Omission of distilled water as an explicit ingredient is acceptable because JCM uses water to bring the final medium to 1 L.
- The preparation step preserves JCM's instruction to filter-sterilize sodium benzoate separately and add it aseptically to the medium.
- JCM's page-level default says to autoclave media at 121 deg C for 15 minutes unless the recipe says otherwise; the record does not separately represent autoclaving of the base mixture before the filtered benzoate addition.
- A gitignore-independent exact search over the maintained owner, generated merge, ID registry, recipe catalog, and MediaDive indexes found the expected `CultureMech:002388` owner and generated record references. It did not find a raw MediaDive or JCM 121 source payload committed for this source record.

## Completeness

- The final non-water formulation is complete and source-supported.
- Consequential sodium-benzoate filtration handling is represented in prose.
- Empty `ph_value`, target-organism, and growth-evidence slots are acceptable here; the inspected JCM recipe source does not state a pH or strain-specific growth result.
- Minor gap: JCM's global autoclave default and the BD-Difco supplier detail for Noble agar are not fully represented.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Minor | The recipe preserves the filtered sodium-benzoate addition but not the JCM default autoclave condition for the base medium. | `data/normalized_yaml/bacterial/benzoate_medium.yaml` |
| Minor | `Agar, Noble (BD-Difco)` is represented as generic `Agar` with `notes: ' ( Noble)'`, losing the BD-Difco supplier and leaving a malformed parenthetical. | `data/normalized_yaml/bacterial/benzoate_medium.yaml` |

## Recommended Edits

1. Add a preparation step for autoclaving the base medium at 121 deg C for 15 minutes before the filtered sodium-benzoate addition.
2. Preserve `Agar, Noble (BD-Difco)` as a source-faithful product label or a clean product note on the agar row.
3. Regenerate `data/merge_yaml/merged/benzoate_medium__fda674fb.yaml` after the normalized owner is corrected.

## Follow-up Checks

- Rerun the open schema validator, `scripts/validate_strict.py`, `linkml-term-validator`, and `linkml-reference-validator` on `data/normalized_yaml/bacterial/benzoate_medium.yaml` and the regenerated merged record.
- Manually compare the regenerated record against JCM GRMD 121 to verify all seven non-water ingredients, the Noble agar source detail, the base autoclave, and the filtered sodium-benzoate addition survive.

## Additional Notes

- The reviewed JCM/MediaDive record is much closer to JCM GRMD 121 than the parallel TOGO M113 import because it already omits the solvent water row and keeps the benzoate filtration instruction.
- Reports are read-only review artifacts; no normalized recipe, generated merge, page, history entry, or GitHub issue was edited for this review.

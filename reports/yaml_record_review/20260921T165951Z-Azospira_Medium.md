# YAML Record Review: Azospira_Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Azospira_Medium.yaml
- Started UTC: 2026-09-21T16:58:25Z
- Finished UTC: 2026-09-21T16:59:51Z
- Verdict: needs curation

## Target

| Field | Observed |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009571 |
| name | azospira_medium |
| original_name | Azospira Medium |
| category | bacterial |
| media_term | TOGO:M3057, Azospira Medium |
| generated status | Generated merge artifact in data/merge_yaml/merged |
| maintained owner | data/normalized_yaml/bacterial/azospira_medium.yaml |

The target is the generated merge for one TOGO/NBRC source record,
`azospira_medium`, with merge fingerprint
`e96b5d2006f95c075e13f96e228816f642c98dbc85c2d39610b2189849c6dd6e`.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Azospira_Medium.yaml` completed with no errors. |
| Strict validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Azospira_Medium.yaml --out /private/tmp/Azospira_Medium.strict.tsv --workers 1 --quiet` completed with no errors. |
| Reference validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Azospira_Medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 checks. |
| Term validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Azospira_Medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed with no errors, aside from a non-fatal `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused embedded `MediaRecipe.curation_history` validator for one merge record. |
| Direct `just` validators | Not checked: the project-level `uv` environment currently fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13, with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project LinkML validator workaround above exercised the target schema, strict, reference, and term checks. |

## Identity and Grounding

- The record identity is supported. TOGO API data for `M3057` names `Azospira Medium`, records `NBRC_M1620` as the original medium ID, and points to the NBRC Medium 1620 page.
- The live NBRC Medium 1620 page renders `Azospira Medium` with the same final salts and `*trace elements solution`.
- `medium_type: COMPLEX` and `composition_type: UNDEFINED` are unsupported; the NBRC recipe lists only defined salts, sodium acetate, citric acid, and water.
- `citric acid` has the correct primary `CHEBI:30769` term but a stale `mediaingredientmech_chebi_term` for sodium citrate.

## Evidence

Supported by inspected source text:

- NBRC Medium 1620 lists CH3COONa 200 mg, KH2PO4 100 mg, NaCl 6.6 mg, MgSO4*7H2O 8.2 mg, KCl 13.4 mg, NH4Cl 115 mg, NaHCO3 188 mg, 1 ml `*trace elements solution`, and 1 L distilled water.
- The trace-elements stock contains FeSO4*7H2O 10 g, FeCl3*6H2O 9.38 g, ZnSO4*7H2O 2 g, CuSO4*7H2O 4 g, NaMoO4*2H2O 0.5 g, MnCl2*4H2O 0.1 g, H3BO4 0.1 g, Na2SeO3 0.3 g, citric acid 10 g, and 1 L distilled water.
- TOGO M3057 preserves the same main recipe, the same 1 ml trace-stock addition, and the same trace-stock members from NBRC.

Unsupported or stale in the generated target:

- The NBRC final-medium milligram salts are imported as gram-per-liter concentrations. For example, 100 mg KH2PO4 becomes `100 G_PER_L`, 115 mg NH4Cl becomes `115 G_PER_L`, and 188 mg NaHCO3 becomes `188 G_PER_L`.
- The final 1 L distilled water row is stored as `1 G_PER_L` instead of a volume.
- The 1 ml trace-elements-stock addition is an empty solution with `1 G_PER_L`.
- All trace-stock components are flattened into final-medium ingredients at stock strength.
- The trace-stock 1 L distilled-water row is absent from the solution.

## Completeness

- Source provenance is sufficient to recover the source formulation: TOGO points to NBRC Medium 1620, and that page was live and substantive during review.
- Empty organism/growth slots are acceptable for this source recipe. The inspected TOGO/NBRC source establishes a formulation, not a growth claim for a specific strain.
- The `high_metal: true` flag may be an artifact of the flattened trace-elements stock and should be recomputed after the stock boundary is restored.
- Gitignore-independent search covered `data/normalized_yaml`, `data/merge_yaml`, `reports/yaml_record_review`, `history`, and `.claude` for `Azospira_Medium`, `Azospira Medium`, `azospira_medium`, and `AZOSPIRA`; no prior Markdown report for this generated record was found.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Final-medium milligram quantities are inflated to gram-per-liter concentrations. | NBRC Medium 1620 lists MgSO4*7H2O, NaCl, KH2PO4, NH4Cl, KCl, NaHCO3, and CH3COONa in milligrams for a 1 L final recipe; the generated record stores the same numeric values as `G_PER_L`. | `data/normalized_yaml/bacterial/azospira_medium.yaml` or the TOGO/NBRC unit importer. |
| Major | The trace-elements stock is flattened into direct final-medium ingredients at full stock strength. | NBRC adds `*trace elements solution` at 1 ml/L. The generated record moves the molybdate, borate, iron, manganese, zinc, copper, selenite, and citric-acid stock components to top-level ingredients. | `data/normalized_yaml/bacterial/azospira_medium.yaml` or `solution-migrator-v1.0`. |
| Major | The explicit water and trace-stock volume context is missing or malformed. | NBRC has 1 L distilled water in the final medium and 1 L distilled water in the trace stock; the generated record has a single `Distilled water` row at `1 G_PER_L` and an empty `*trace elements solution` row at `1 G_PER_L`. | `data/normalized_yaml/bacterial/azospira_medium.yaml` and duplicate-water cleanup for source-local stocks. |
| Major | The medium is classified as complex and undefined despite a defined NBRC formulation. | Every inspected NBRC component is a defined chemical or water; the record has no yeast extract, peptone, casamino acids, or other undefined component. | `data/normalized_yaml/bacterial/azospira_medium.yaml`. |
| Minor | Citric acid has a stale MediaIngredientMech CHEBI mapping. | The primary term is `CHEBI:30769` citric acid, but `mediaingredientmech_chebi_term` points at sodium citrate. | CHEBI/MIM enrichment for `data/normalized_yaml/bacterial/azospira_medium.yaml`. |

## Recommended Edits

1. Convert the final-medium NBRC milligram rows to g/L values, e.g. KH2PO4 `0.1 G_PER_L`, NH4Cl `0.115 G_PER_L`, NaHCO3 `0.188 G_PER_L`, and CH3COONa `0.2 G_PER_L`.
2. Represent `*trace elements solution` as a 1 ml/L solution addition with the molybdate, borate, iron, manganese, zinc, copper, selenite, citric acid, and stock-water rows nested inside the solution.
3. Restore `Distilled water` as a final-medium 1 L volume and a separate trace-stock 1 L volume.
4. Change the medium and composition classifications to defined unless additional source evidence supports an undefined component.
5. Recompute `high_metal` and refresh the citric-acid MediaIngredientMech CHEBI link after the trace stock is nested.

## Follow-up Checks

- `just validate-strict data/normalized_yaml/bacterial/azospira_medium.yaml` after the maintained record is repaired.
- `just validate-terms data/normalized_yaml/bacterial/azospira_medium.yaml` after the citric-acid mapping is refreshed.
- `just verify-merges` after regenerating the merge layer.
- Manual comparison with TOGO M3057 and NBRC Medium 1620 to verify the final milligram quantities, 1 L final water, 1 ml/L trace-stock addition, and 1 L trace-stock water.

## Additional Notes

- `linkml-reference-validator` performed zero checks because this generated record has no `references` block.

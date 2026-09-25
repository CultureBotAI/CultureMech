# YAML Record Review: azospirillum_amazonense_medium__911e8407

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/azospirillum_amazonense_medium__911e8407.yaml
- Started UTC: 2026-09-21T17:01:45Z
- Finished UTC: 2026-09-21T17:03:02Z
- Verdict: needs curation

## Target

| Field | Observed |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008501 |
| name | azospirillum_amazonense_medium |
| original_name | Azospirillum amazonense medium |
| category | bacterial |
| media_term | TOGO:M1922, Azospirillum amazonense medium |
| generated status | Generated merge artifact in data/merge_yaml/merged |
| maintained owner | data/normalized_yaml/bacterial/TOGO_M1922_Azospirillum_amazonense_medium.yaml |

The target is the generated merge for one TOGO/NBRC source record,
`TOGO_M1922_Azospirillum_amazonense_medium`, with merge fingerprint
`911e84072ce9d4b0dc9d3c7b8b6d80ce2a89a5e6d9288e0bf20bb279bb902b9c`.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/azospirillum_amazonense_medium__911e8407.yaml` completed with no errors. |
| Strict validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/azospirillum_amazonense_medium__911e8407.yaml --out /private/tmp/azospirillum_amazonense_medium__911e8407.strict.tsv --workers 1 --quiet` completed with no errors. |
| Reference validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/azospirillum_amazonense_medium__911e8407.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 checks. |
| Term validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/azospirillum_amazonense_medium__911e8407.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed with no errors, aside from a non-fatal `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused embedded `MediaRecipe.curation_history` validator for one merge record. |
| Direct `just` validators | Not checked: the project-level `uv` environment currently fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13, with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project LinkML validator workaround above exercised the target schema, strict, reference, and term checks. |

## Identity and Grounding

- The record identity is supported. TOGO API data for `M1922` names `Azospirillum amazonense medium`, records `NBRC_M1186` as the original medium ID, and points to the NBRC Medium 1186 page.
- The live NBRC Medium 1186 page renders the same Azospirillum amazonense recipe.
- `medium_type: COMPLEX` and `composition_type: UNDEFINED` are unsupported; the inspected NBRC recipe lists only defined salts, sucrose, bromophenol-blue solution, and water.
- `Bromophenol blue (0.5% in 0.2N KOH)` is ungrounded, but the mixture label should remain explicit rather than being collapsed to bare bromophenol blue because the KOH stock solvent is part of the source row.

## Evidence

Supported by inspected source text:

- NBRC Medium 1186 lists K2HPO4 0.2 g, KH2PO4 0.6 g, CaCl2*2H2O 0.02 g, MgSO4*7H2O 0.2 g, Na2MoO4*2H2O 2 mg, FeCl3 0.01 g, sucrose 5 g, Bromophenol blue at 5 ml of a 0.5% solution in 0.2 N KOH, and 1 L distilled water.
- NBRC and TOGO both report pH 6.0.

Unsupported or stale in the generated target:

- Na2MoO4*2H2O is `2 G_PER_L`; NBRC lists 2 mg.
- `Bromophenol blue (0.5% in 0.2N KOH)` is `5 G_PER_L`; NBRC lists a 5 ml solution addition.
- `Distilled water` is `1 G_PER_L`; NBRC lists 1 L.
- The pH 6.0 source field is missing from the generated record.

## Completeness

- Source provenance is sufficient to recover the source formulation: TOGO points to NBRC Medium 1186, and that page was live and substantive during review.
- Empty organism/growth slots are acceptable for this source recipe. The inspected TOGO/NBRC source establishes a formulation, not a growth claim for a specific strain.
- Gitignore-independent search covered `data/normalized_yaml`, `data/merge_yaml`, `reports/yaml_record_review`, `history`, and `.claude` for `AZOSPIRILLUM_AMAZONENSE`, `Azospirillum Amazonense`, `azospirillum_amazonense`, and `Azospirillum amazonense`; no prior Markdown report for this exact generated record was found.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Source milligram, milliliter, and liter rows are all imported as gram-per-liter concentrations. | NBRC has 2 mg Na2MoO4*2H2O, 5 ml bromophenol-blue/KOH stock, and 1 L distilled water. The record stores those as `2`, `5`, and `1` `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1922_Azospirillum_amazonense_medium.yaml` or the TOGO/NBRC importer. |
| Major | The pH 6.0 field is missing. | TOGO M1922 has `ph: 6.0`, and NBRC prints pH 6.0. The generated record has no `ph_value` or preparation step. | `data/normalized_yaml/bacterial/TOGO_M1922_Azospirillum_amazonense_medium.yaml`. |
| Major | The medium is classified as complex and undefined despite a defined NBRC formulation. | Every inspected component is a defined chemical, defined indicator stock, sucrose, or water. | `data/normalized_yaml/bacterial/TOGO_M1922_Azospirillum_amazonense_medium.yaml`. |

No blocker or minor findings found.

## Recommended Edits

1. Correct the three malformed source rows in `data/normalized_yaml/bacterial/TOGO_M1922_Azospirillum_amazonense_medium.yaml`: Na2MoO4*2H2O to `0.002 G_PER_L`, Bromophenol blue stock to a 5 ml/L solution, and Distilled water to 1 L.
2. Add `ph_value: 6.0`.
3. Reclassify the medium as defined, then regenerate `data/merge_yaml/merged/azospirillum_amazonense_medium__911e8407.yaml`.

## Follow-up Checks

- `just validate-strict data/normalized_yaml/bacterial/TOGO_M1922_Azospirillum_amazonense_medium.yaml` after the maintained TOGO record is repaired.
- `just validate-terms data/normalized_yaml/bacterial/TOGO_M1922_Azospirillum_amazonense_medium.yaml` after any bromophenol-blue stock modeling change.
- `just verify-merges` after regenerating the merge layer.
- Manual comparison with TOGO M1922 and NBRC Medium 1186 to verify sodium molybdate, bromophenol blue, distilled water, pH, and classification.

## Additional Notes

- `AZOSPIRILLUM_AMAZONENSE_MEDIUM.yaml` is a separate DSMZ/KOMODO Medium 352 source-duplicate merge and should not be used as the maintained owner for this TOGO/NBRC record.
- `linkml-reference-validator` performed zero checks because this generated record has no `references` block.

# YAML Record Review: AZOARCUS_TAIWANENSIS_MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AZOARCUS_TAIWANENSIS_MEDIUM.yaml
- Started UTC: 2026-09-21T16:56:55Z
- Finished UTC: 2026-09-21T16:58:08Z
- Verdict: needs curation

## Target

| Field | Observed |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001123 |
| name | azoarcus_taiwanensis_medium |
| original_name | AZOARCUS TAIWANENSIS MEDIUM |
| category | bacterial |
| media_term | mediadive.medium:1639, AZOARCUS TAIWANENSIS MEDIUM |
| generated status | Generated merge artifact in data/merge_yaml/merged |
| maintained owner | data/normalized_yaml/bacterial/azoarcus_taiwanensis_medium.yaml |

The target is the generated merge for one MediaDive/DSMZ source record,
`azoarcus_taiwanensis_medium`, with merge fingerprint
`85cf3d6f4b3a952fdda9ac164e2277f39655d2a49f2eadf77d7398d66f97c1bc`.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AZOARCUS_TAIWANENSIS_MEDIUM.yaml` completed with no errors. |
| Strict validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AZOARCUS_TAIWANENSIS_MEDIUM.yaml --out /private/tmp/AZOARCUS_TAIWANENSIS_MEDIUM.strict.tsv --workers 1 --quiet` completed with no errors. |
| Reference validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AZOARCUS_TAIWANENSIS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 checks. |
| Term validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AZOARCUS_TAIWANENSIS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed with no errors, aside from a non-fatal `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused embedded `MediaRecipe.curation_history` validator for one merge record. |
| Direct `just` validators | Not checked: the project-level `uv` environment currently fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13, with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project LinkML validator workaround above exercised the target schema, strict, reference, and term checks. |

## Identity and Grounding

- The record identity is supported. The maintained owner identifies `mediadive.medium:1639`, and the cited DSMZ Medium 1639 PDF is live and titled `AZOARCUS TAIWANENSIS MEDIUM`.
- Category `bacterial`, liquid physical state, defined medium type, and pH 8.5-9.0 agree with the DSMZ formulation.
- `KNO3` still has a legacy `mediaingredientmech_term` while every other grounded direct ingredient uses `mediaingredientmech_chebi_term`; this conflicts with the June 2026 curation-history claim that 15 legacy links were replaced.
- `NiCl2 x 6 H2O` is grounded to generic `CHEBI:34887` nickel dichloride even though DSMZ Medium 1639 specifies nickel chloride hexahydrate in SL-11.

## Evidence

Supported by inspected source text:

- DSMZ Medium 1639 has final volume 1001 ml and final pH 8.5-9.0.
- The final medium contains NaCl, KNO3, NH4Cl, K2HPO4, Na-acetate, NaHCO3, Na-pyruvate, 1000 ml distilled water, and 1 ml Trace element solution SL-11.
- The preparation step for the final medium is represented: dissolve everything except bicarbonate and pyruvate, sparge with 100% N2 for 30-45 min, add bicarbonate, adjust pH to 8.5-9.0, dispense under 100% N2, autoclave, then add pyruvate from a sterile anoxic filtered stock and readjust pH if necessary.
- DSMZ Medium 1639 defines Trace element solution SL-11 as a 1000 ml stock with Na2-EDTA x 2 H2O, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and distilled water, with pH adjustments to 7 and 6.0.

Unsupported or over-scoped claims:

- The generated record has no 1 ml/L `Trace element solution SL-11` addition; every SL-11 solute is instead flattened into a top-level final-medium ingredient at stock strength.
- The record omits both source water rows: 1000 ml in the final medium and 1000 ml in the SL-11 stock.
- SL-11 preparation appears as top-level `preparation_steps[1]`, but it is not attached to an explicit SL-11 solution object.
- `NiCl2 x 6 H2O` loses its hexahydrate in the CHEBI grounding.

## Completeness

- Source provenance is sufficient to recover the authoritative formulation: the record names DSMZ Medium 1639 and the live PDF URL.
- Empty organism/growth slots are acceptable for this source recipe. DSMZ Medium 1639 is a medium formulation and does not assert a tested target strain in the inspected recipe PDF.
- Gitignore-independent search covered `data/normalized_yaml`, `data/merge_yaml`, `reports/yaml_record_review`, `history`, and `.claude` for `AZOARCUS_TAIWANENSIS_MEDIUM`, `Azoarcus taiwanensis`, `AZOARCUS TAIWANENSIS`, and `azoarcus_taiwanensis`; no prior Markdown report for this generated record was found.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Trace element solution SL-11 is flattened into final-medium ingredients at full stock strength. | DSMZ Medium 1639 adds 1 ml/L SL-11. The record has no SL-11 solution addition and exposes Na2-EDTA x 2 H2O, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O as direct rows. | `data/normalized_yaml/bacterial/azoarcus_taiwanensis_medium.yaml` or the MediaDive stock-solution importer. |
| Major | Distilled water from the final medium and the trace stock is missing. | DSMZ lists 1000 ml distilled water in the 1001 ml final medium and 1000 ml distilled water in the SL-11 stock. The generated record has no distilled-water ingredient or solution component. | `data/normalized_yaml/bacterial/azoarcus_taiwanensis_medium.yaml`. |
| Major | SL-11 stock preparation is represented at the wrong level. | The EDTA pH 7, ferrous-chloride addition, final pH 6.0, and 1000 ml makeup step belong to Trace element solution SL-11, not the final medium. | MediaDive stock-solution importer and solution modeling. |
| Minor | Legacy and generic ontology links remain on two hydrated salts. | `KNO3` still carries `mediaingredientmech_term`; `NiCl2 x 6 H2O` points to generic nickel dichloride instead of the hexahydrate. | CHEBI/MIM enrichment for `data/normalized_yaml/bacterial/azoarcus_taiwanensis_medium.yaml`. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/azoarcus_taiwanensis_medium.yaml`, move Na2-EDTA x 2 H2O, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O into an explicit Trace element solution SL-11 added at 1 ml/L.
2. Restore both distilled-water rows with their correct contexts: 1000 ml final-medium water and 1000 ml SL-11 water.
3. Attach the EDTA/FeCl2/pH 6.0 preparation instructions to the SL-11 stock rather than to the final-medium preparation.
4. Remove the remaining legacy `MediaIngredientMech:000170` KNO3 link and re-ground `NiCl2 x 6 H2O` to a hydrate-specific CHEBI term if one is available.

## Follow-up Checks

- `just validate-strict data/normalized_yaml/bacterial/azoarcus_taiwanensis_medium.yaml` after the maintained record is repaired.
- `just validate-terms data/normalized_yaml/bacterial/azoarcus_taiwanensis_medium.yaml` after the KNO3 and NiCl2 grounding cleanup.
- `just verify-merges` after regenerating the merge layer.
- Manual comparison with DSMZ Medium 1639 to verify the generated record preserves the 1001 ml final volume, 1 ml/L SL-11 addition, two water rows, final pH 8.5-9.0, and SL-11 pH 6.0 stock preparation.

## Additional Notes

- The direct salt values are divided by DSMZ's explicit 1001 ml final volume; that unit conversion is dimensionally consistent for the final-medium ingredients.
- `linkml-reference-validator` performed zero checks because this generated record has no `references` block.

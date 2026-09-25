# YAML Record Review: HYDROGENOBACTER HALOPHILUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogenobacter_halophilus_medium__d2e10f9e.yaml
- Started UTC: 2026-09-23T13:36:00Z
- Finished UTC: 2026-09-23T13:38:01Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:000292 |
| Name | hydrogenobacter_halophilus_medium |
| Original name | HYDROGENOBACTER HALOPHILUS MEDIUM |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | DEFINED |
| Composition type | DEFINED |
| Physical state | LIQUID |
| Source identity | MediaDive/JCM Medium J128 |
| Generated path reviewed | data/merge_yaml/merged/hydrogenobacter_halophilus_medium__d2e10f9e.yaml |
| Maintained owner | data/normalized_yaml/bacterial/JCM_J128_HYDROGENOBACTER_HALOPHILUS_MEDIUM.yaml |

The reviewed file is generated from the maintained MediaDive/JCM input above.
Future edits should restore JCM 128 stock-solution scope in that normalized
record and the MediaDive import logic, then regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogenobacter_halophilus_medium__d2e10f9e.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hydrogenobacter_halophilus_medium__d2e10f9e.yaml --out /private/tmp/hydrogenobacter_halophilus_medium__d2e10f9e.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hydrogenobacter_halophilus_medium__d2e10f9e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hydrogenobacter_halophilus_medium__d2e10f9e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is coherent: `CultureMech:000292` denotes JCM Medium
  J128, `HYDROGENOBACTER HALOPHILUS MEDIUM`.
- The inspected MediaDive J128 REST payload matches the live JCM 128 page: a
  1002 ml final solution with 1 L water, eight direct salts, 0.6 mg NiSO4 x
  7H2O, and 2 ml Trace element solution; the trace stock itself is 1 L.
- An ignored-inclusive exact search for `CultureMech:000292` across
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found only
  this JCM-owned normalized record, generated indexes, generated merged YAML,
  and archival reports for the same stable ID.
- A gitignore-independent slug search over `data/normalized_yaml`,
  `data/merge_yaml/merged`, and `reports` found sibling DSMZ 744, KOMODO 744,
  and TOGO M120 records with the same normalized name. TOGO M120 mirrors the
  same JCM Medium 128 formula; DSMZ/KOMODO 744 are related but distinct
  Hydrogenobacter halophilus formulations.
- Ingredient grounding is exact for the fixed-hydration salts. `MnSO4 x nH2O`
  is necessarily grounded to generic manganese sulfate because the source
  itself leaves the hydration variable.

## Evidence

- The final-medium phosphate, ammonium sulfate, NaCl, MgSO4, CaCl2, FeSO4, and
  NiSO4 rows match MediaDive's normalized 1002 ml final volume.
- The trace stock members are unsupported as direct final-medium ingredients.
  MediaDive/JCM add 2 ml of Trace element solution per 1002 ml final medium,
  while the YAML emits MoO3, ZnSO4 x 7H2O, CuSO4 x 5H2O, H3BO3,
  MnSO4 x nH2O, and CoCl2 x 6H2O as direct final rows at their 1 L stock
  concentrations.
- The source water rows are both absent: Main sol. J128 has 1000 ml distilled
  water, and the Trace element solution has another 1000 ml distilled water.
- The source does not state a pH, gas phase, or special preparation comment, so
  those optional fields are correctly absent from the JCM-derived MediaDive
  record.

## Completeness

- The `solutions` array is missing the 2 ml/L trace-stock addition and the
  trace-stock composition.
- The trace-stock and final-medium water rows are missing.
- The record does not need target organisms, synonyms, or standalone
  publication references to represent this imported JCM provider recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | JCM 128 Trace element solution was flattened into final-medium rows. | The source adds 2 ml trace solution, but the YAML lists all six trace compounds directly at the 1 L stock concentrations. | `data/normalized_yaml/bacterial/JCM_J128_HYDROGENOBACTER_HALOPHILUS_MEDIUM.yaml`; MediaDive import should preserve solution 3769 as a stock. |
| Major | Source water rows are absent. | MediaDive has a 1000 ml distilled-water row in Main sol. J128 and another in the Trace element solution; neither is represented in the YAML. | `data/normalized_yaml/bacterial/JCM_J128_HYDROGENOBACTER_HALOPHILUS_MEDIUM.yaml`. |
| Minor | The same JCM 128 recipe is also represented by TOGO M120. | Ignored-inclusive search found `TOGO_M120_Hydrogenobacter_Halophilus_Medium.yaml`, a separate TOGO import of JCM Medium 128 with the same label and a different trace-stock flattening artifact. | Cross-provider MediaDive/JCM and TOGO deduplication. |

## Recommended Edits

1. Move MoO3, ZnSO4 x 7H2O, CuSO4 x 5H2O, H3BO3, MnSO4 x nH2O, and CoCl2 x
   6H2O into a nested Trace element solution and add that stock to the final
   medium at 2 ml per 1 L base medium.
2. Restore the 1000 ml distilled-water rows for both Main sol. J128 and the
   Trace element solution.
3. Keep the MediaDive 1002 ml final-volume normalization for the eight
   non-stock salts or document any future decision to store provider table
   masses instead.
4. Reconcile the MediaDive/JCM J128 and TOGO M120 records once both imports
   preserve the same trace-stock structure.
5. Regenerate `data/merge_yaml/merged/` from the corrected normalized record.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  JCM J128 merged record.
- Manually compare every base and trace-stock row against the live MediaDive
  J128 REST payload and the JCM Medium 128 page.
- Verify no trace-stock member appears as a direct final-medium ingredient
  except through the 2 ml Trace element solution addition.
- Search ignored files for `hydrogenobacter_halophilus_medium`,
  `mediadive.medium:J128`, and `TOGO:M120` to verify the duplicate JCM 128
  imports are reconciled or explicitly preserved with source provenance.

## Additional Notes

- The current generated JCM J128 record is cleaner than the TOGO M120 sibling
  because it already converts milligram main-medium rows to g/L correctly; the
  remaining blocker is the loss of the trace-stock boundary.

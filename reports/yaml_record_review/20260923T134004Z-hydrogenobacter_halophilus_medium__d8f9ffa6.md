# YAML Record Review: Hydrogenobacter Halophilus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogenobacter_halophilus_medium__d8f9ffa6.yaml
- Started UTC: 2026-09-23T13:38:20Z
- Finished UTC: 2026-09-23T13:39:58Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:007737 |
| Name | hydrogenobacter_halophilus_medium |
| Original name | Hydrogenobacter Halophilus Medium |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| Source identity | TOGO Medium M120; original source JCM Medium 128 |
| Generated path reviewed | data/merge_yaml/merged/hydrogenobacter_halophilus_medium__d8f9ffa6.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M120_Hydrogenobacter_Halophilus_Medium.yaml |

The reviewed file is generated from the maintained TOGO input above. Future
fixes should correct that normalized file and the TOGO importer/solution
migrator, then regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogenobacter_halophilus_medium__d8f9ffa6.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hydrogenobacter_halophilus_medium__d8f9ffa6.yaml --out /private/tmp/hydrogenobacter_halophilus_medium__d8f9ffa6.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hydrogenobacter_halophilus_medium__d8f9ffa6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hydrogenobacter_halophilus_medium__d8f9ffa6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is resolved: `CultureMech:007737` is the TOGO M120 import
  of JCM Medium 128, both named Hydrogenobacter Halophilus Medium.
- The inspected TOGO M120 payload and live JCM 128 page agree on the direct
  salts, 2 ml Trace element solution, 1 L final water, and 1 L trace-stock
  water.
- A gitignore-independent exact search for `CultureMech:007737` over
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found only
  this TOGO-owned normalized file, generated indexes, generated merged YAML,
  and archival validation reports for the same stable ID.
- Magnesium sulfate heptahydrate, sodium chloride, phosphate salts, ammonium
  sulfate, calcium chloride, ferrous sulfate heptahydrate, boric acid, zinc
  sulfate heptahydrate, copper sulfate pentahydrate, manganese sulfate,
  molybdenum trioxide, and water are grounded acceptably. NiSO4 x 7H2O is
  grounded to generic nickel sulfate, and CoCl2 x 6H2O is grounded to generic
  cobalt dichloride.

## Evidence

- The gram-scale final-medium salts match JCM 128.
- FeSO4 x 7H2O and CaCl2 are source 10 mg rows but appear as `10 G_PER_L`.
- NiSO4 x 7H2O is a source 0.6 mg row but appears as `0.6 G_PER_L`.
- The trace-stock milligram quantities appear as direct gram-per-liter final
  rows: H3BO3, CoCl2 x 6H2O, MnSO4 x nH2O, and MoO3 are `1 G_PER_L`;
  ZnSO4 x 7H2O is `7 G_PER_L`; CuSO4 x 5H2O is `0.5 G_PER_L`.
- The source 2 ml Trace element solution is present only as an empty solution
  with `2 G_PER_L`.
- The generated file has a `2.0 G_PER_L` water row after summing one final 1 L
  water row and one trace-stock 1 L water row; the maintained source was later
  collapsed to `1.0 G_PER_L`, but both representations still lose the final
  versus stock boundary.

## Completeness

- The trace solution is empty even though M120/JCM 128 carries its definition
  inline below the main recipe table.
- Source volumes are dimensionally incomplete: both 1 L water rows and the
  2 ml trace-stock addition need volume representation, not `G_PER_L`.
- Empty optional fields for pH, preparation steps, target organisms, synonyms,
  and publication references are not defects because JCM 128 does not supply
  those claims.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Every milligram row was imported as grams per liter. | JCM 128 source rows of 10 mg, 0.6 mg, 1 mg, 7 mg, and 0.5 mg retain their numeric values but use `G_PER_L` in the YAML. | `data/normalized_yaml/bacterial/TOGO_M120_Hydrogenobacter_Halophilus_Medium.yaml`; audit TOGO `mg` unit handling. |
| Major | The inline trace solution is empty and its 2 ml addition has the wrong unit. | JCM 128 defines a seven-row Trace element solution table, while the YAML has `composition: []` and `2 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M120_Hydrogenobacter_Halophilus_Medium.yaml`; repair TOGO subcomponent migration. |
| Major | Water rows cross solution boundaries. | Final and trace-stock water were merged to `2.0 G_PER_L` in the generated file and later collapsed to `1.0 G_PER_L` in the normalized source; neither keeps the two 1 L solvent rows in their source scopes. | `data/normalized_yaml/bacterial/TOGO_M120_Hydrogenobacter_Halophilus_Medium.yaml`; duplicate repair should preserve scope. |
| Minor | Hydrated Ni and Co salts lost exact grounding. | The source labels are NiSO4 x 7H2O and CoCl2 x 6H2O; the YAML grounds them to generic nickel sulfate and cobalt dichloride. | `data/normalized_yaml/bacterial/TOGO_M120_Hydrogenobacter_Halophilus_Medium.yaml`; hydrate-aware CHEBI mapping. |
| Minor | JCM 128 also exists as a MediaDive/JCM import. | The reviewed TOGO M120 record and the MediaDive J128 record both represent JCM Medium 128. | Cross-provider TOGO/MediaDive deduplication. |

## Recommended Edits

1. Convert all direct and trace-stock milligram rows to `MG_PER_L` or correct
   gram-per-liter equivalents with the source `mg` units preserved in notes.
2. Move the six trace elements plus 1 L distilled water into a nested Trace
   element solution and add that stock to the main medium at 2 ml/L.
3. Restore the final-medium 1 L distilled-water row separately from the
   trace-stock 1 L distilled-water row.
4. Re-ground NiSO4 x 7H2O and CoCl2 x 6H2O to exact hydrated CHEBI terms where
   available.
5. Reconcile TOGO M120 with MediaDive/JCM J128 after both imports express the
   same JCM formulation with the same solution boundary.
6. Regenerate `data/merge_yaml/merged/` from the corrected normalized record.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  TOGO M120 merged record.
- Manually compare all direct and trace-stock rows against the TOGO M120 API
  payload and the live JCM 128 page.
- Verify the trace elements are present only inside the Trace element solution
  stock and the final medium uses that stock at 2 ml/L.
- Re-run duplicate cleanup and the merge generator to ensure generated water
  stays separated by final-medium and trace-stock scopes.

## Additional Notes

- The September duplicate repair correctly recognized that the generated
  `2.0` water concentration was a sum of two equal rows, but it could not
  recover the missing solution boundary without source-aware curation.

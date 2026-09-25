# YAML Record Review: Hydrogenobacter Thermophilus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogenobacter_thermophilus_medium__0fd91ccf.yaml
- Started UTC: 2026-09-23T13:40:30Z
- Finished UTC: 2026-09-23T13:42:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:008001 |
| Name | hydrogenobacter_thermophilus_medium |
| Original name | Hydrogenobacter Thermophilus Medium |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| Source identity | TOGO Medium M145; original source JCM Medium 154 |
| Generated path reviewed | data/merge_yaml/merged/hydrogenobacter_thermophilus_medium__0fd91ccf.yaml |
| Maintained owner | data/normalized_yaml/bacterial/hydrogenobacter_thermophilus_medium.yaml |

The reviewed file is generated from the maintained TOGO input above. Future
fixes should update the normalized source and the shared TOGO mg/solution
migration that also affects nearby Hydrogenobacter records, then regenerate
`data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogenobacter_thermophilus_medium__0fd91ccf.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hydrogenobacter_thermophilus_medium__0fd91ccf.yaml --out /private/tmp/hydrogenobacter_thermophilus_medium__0fd91ccf.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hydrogenobacter_thermophilus_medium__0fd91ccf.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hydrogenobacter_thermophilus_medium__0fd91ccf.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is coherent: `CultureMech:008001` is the TOGO M145 import
  of JCM Medium 154, both named Hydrogenobacter Thermophilus Medium.
- The inspected TOGO M145 JSON lists `original_media_id: JCM_M154`, and the
  live JCM 154 page confirms the same main-medium rows, 2 ml Trace element
  solution cross-reference to JCM Medium 128, and 1 L distilled water.
- JCM Medium 128 is mirrored locally as TOGO M120 and supplies the trace stock
  that M145 references.
- A gitignore-independent exact search for `CultureMech:008001` over
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found the
  maintained renamed TOGO file, generated indexes, generated merged YAML, and
  archival reports for this stable ID.
- Magnesium sulfate heptahydrate, NaCl, KH2PO4, FeSO4 x 7H2O, CaCl2,
  Na2HPO4, and NH4NO3 are grounded exactly enough. NiSO4 x 7H2O is grounded to
  generic nickel sulfate.

## Evidence

- The gram-scale Na2HPO4, KH2PO4, NH4NO3, NaCl, and MgSO4 x 7H2O rows match
  JCM 154.
- FeSO4 x 7H2O and CaCl2 are source 10 mg rows but appear as `10 G_PER_L`.
- NiSO4 x 7H2O is a source 0.06 mg row but appears as `0.06 G_PER_L`.
- The source has 2 ml `Trace element solution (see Medium No. 128)`, but the
  YAML has an empty M120 solution recorded as `2 G_PER_L`.
- The source has 1 L distilled water, represented in YAML as `1 G_PER_L`.
- The source has no pH or preparation details besides JCM's generic default
  autoclaving statement, so no record-specific pH or preparation claim is
  missing.

## Completeness

- The M120/JCM 128 trace stock needs to be resolved as a populated stock
  addition rather than an empty solution.
- Milligram units and the 1 L water volume need dimensional repair.
- Empty optional fields for pH, preparation, target organisms, synonyms, and
  publication references are acceptable for this provider import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Milligram final rows are represented as grams per liter. | JCM 154 lists 10 mg FeSO4 x 7H2O, 10 mg CaCl2, and 0.06 mg NiSO4 x 7H2O; the YAML records 10, 10, and 0.06 `G_PER_L`. | `data/normalized_yaml/bacterial/hydrogenobacter_thermophilus_medium.yaml`; audit TOGO `mg` unit handling. |
| Major | The 2 ml trace stock is empty and has the wrong unit. | JCM 154 points to JCM Medium 128 / TOGO M120 for a 2 ml trace-element stock; the YAML has `Trace element solution (see Medium [M120])` with no composition and `2 G_PER_L`. | `data/normalized_yaml/bacterial/hydrogenobacter_thermophilus_medium.yaml`; repair referenced-medium solution migration. |
| Major | The 1 L water row is represented as mass concentration. | Distilled water is a 1 L source row but appears as `1 G_PER_L`. | `data/normalized_yaml/bacterial/hydrogenobacter_thermophilus_medium.yaml`; TOGO volume handling should preserve liters as volume. |
| Minor | Nickel sulfate heptahydrate lost exact hydrate grounding. | The source has NiSO4 x 7H2O, but the YAML grounds it to generic CHEBI:53001 nickel sulfate. | `data/normalized_yaml/bacterial/hydrogenobacter_thermophilus_medium.yaml`; hydrate-aware CHEBI mapping. |

## Recommended Edits

1. Convert FeSO4 x 7H2O, CaCl2, and NiSO4 x 7H2O from source milligram rows to
   correct `MG_PER_L` or gram-per-liter values.
2. Replace the empty M120 solution with a 2 ml/L reference to the populated
   TOGO M120 / JCM 128 trace-element stock.
3. Represent the 1 L distilled-water row as solvent volume, not `G_PER_L`.
4. Re-ground NiSO4 x 7H2O to an exact hydrated term if CHEBI exposes one.
5. Regenerate `data/merge_yaml/merged/` from the corrected normalized record.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  TOGO M145 merged record.
- Manually compare all M145 rows against the TOGO API payload and live JCM 154
  page.
- Verify the M120/JCM 128 stock is referenced at 2 ml/L and contains the trace
  stock composition from the JCM 128 source.

## Additional Notes

- This record intentionally references TOGO M120 because M120 mirrors JCM
  Medium 128, the trace-element stock linked from the JCM 154 source table.

# YAML Record Review: Hydrogenobacter Acidophilus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__860e8ba3.yaml
- Started UTC: 2026-09-23T13:27:05Z
- Finished UTC: 2026-09-23T13:29:46Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:008108 |
| Name | hydrogenobacter_acidophilus_medium |
| Original name | Hydrogenobacter Acidophilus Medium |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| Source identity | TOGO Medium M155; original source JCM Medium 164 |
| Generated path reviewed | data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__860e8ba3.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M155_Hydrogenobacter_Acidophilus_Medium.yaml |

The reviewed file is generated from the maintained TOGO import at
`data/normalized_yaml/bacterial/TOGO_M155_Hydrogenobacter_Acidophilus_Medium.yaml`.
Future corrections should update that normalized input and the TOGO importer or
solution migrator that turned a 2 ml referenced trace stock into an empty
`G_PER_L` solution before regenerating `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__860e8ba3.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__860e8ba3.yaml --out /private/tmp/hydrogenobacter_acidophilus_medium__860e8ba3.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__860e8ba3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__860e8ba3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is resolved: `CultureMech:008108` is the TOGO M155 import
  of JCM Medium 164, both named Hydrogenobacter Acidophilus Medium.
- The inspected TOGO M155 JSON lists `original_media_id: JCM_M164`, the JCM
  164 source URL, and pH 3.0. The inspected live JCM 164 page has the same
  ingredient masses, a 2 ml trace-element reference to JCM Medium 128, 1 L
  distilled water, pH adjustment to 3.0 with HCl, and separate sterilization
  for sulfur.
- The TOGO API normalizes JCM Medium 128 to TOGO M120. Fetching TOGO M120
  confirmed it is Hydrogenobacter Halophilus Medium / JCM Medium 128 and has
  the trace-element solution subtable needed by M155.
- A gitignore-independent exact search for `CultureMech:008108` over
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found this
  TOGO-owned normalized file, its generated merged file, generated indexes,
  and archival validation reports for the same stable ID.
- Magnesium sulfate heptahydrate, sodium chloride, dipotassium hydrogen
  phosphate, ferrous sulfate heptahydrate, ammonium sulfate, calcium chloride,
  sulfur, and hydrogen chloride grounding are exact enough. `NiSO4 x 6H2O` is
  grounded to generic nickel sulfate.

## Evidence

- The record carries the correct source label, TOGO accession, JCM URL,
  bacterial category, and liquid physical state.
- The gram-scale MgSO4, NaCl, K2HPO4, ammonium sulfate, and sulfur quantities
  match TOGO M155/JCM 164.
- The 1 mg FeSO4 x 7H2O, 1 mg CaCl2, and 0.06 mg NiSO4 x 6H2O source rows are
  all represented with the same numeric values but `G_PER_L`, making them
  1000-fold too concentrated.
- The 1 L distilled-water row is represented as `1 G_PER_L` instead of as
  final volume or solvent volume.
- The source 2 ml trace-element solution is present only as an empty solution
  with `concentration.value: 2` and `unit: G_PER_L`; the referenced TOGO M120 /
  JCM 128 trace stock members are absent.
- The source pH and preparation comments are missing from `ph_value` and
  `preparation_steps`; HCl survives only as a variable ingredient from schema
  defaulting.

## Completeness

- The M155 record is incomplete until it either references TOGO M120/JCM 128
  trace solution as a non-empty stock or inlines that stock with the correct
  2 ml/L addition boundary.
- The YAML lacks source pH 3.0 despite TOGO's structured `ph` value.
- The YAML lacks the JCM preparation requirements to adjust with HCl and
  sterilize sulfur separately.
- Empty optional slots for organisms, synonyms, and standalone publication
  references are not defects for this provider recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Milligram final-medium rows are imported as grams per liter. | TOGO M155/JCM 164 list 1 mg FeSO4 x 7H2O, 1 mg CaCl2, and 0.06 mg NiSO4 x 6H2O; the YAML records values of 1, 1, and 0.06 `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M155_Hydrogenobacter_Acidophilus_Medium.yaml`; audit TOGO unit conversion for `mg`. |
| Major | The trace-element stock addition is empty and has the wrong unit. | JCM 164 adds 2 ml trace element solution from JCM 128, represented in TOGO as M120; the YAML has an empty `Trace element solution (see Medium [M120])` with `2 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M155_Hydrogenobacter_Acidophilus_Medium.yaml`; fix solution migration for referenced TOGO media. |
| Major | Source pH and preparation comments were dropped. | TOGO and JCM specify pH 3.0, pH adjustment with HCl, and separate sulfur sterilization, but the YAML has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M155_Hydrogenobacter_Acidophilus_Medium.yaml`; TOGO comments and `ph` import should populate structured fields. |
| Major | The 1 L water row is dimensionally wrong. | JCM 164 lists 1 L distilled water; the YAML records water with value `1` and `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M155_Hydrogenobacter_Acidophilus_Medium.yaml`; TOGO volume handling should preserve liters as volume. |
| Minor | Nickel sulfate hexahydrate lost exact hydrate grounding. | The source has `NiSO4 x 6H2O`, while the YAML grounds it to generic CHEBI:53001 nickel sulfate. | `data/normalized_yaml/bacterial/TOGO_M155_Hydrogenobacter_Acidophilus_Medium.yaml`; update hydrate-aware CHEBI mapping. |

## Recommended Edits

1. Convert FeSO4 x 7H2O, CaCl2, and NiSO4 x 6H2O from source milligram
   quantities to the correct final concentrations or preserve them as mg/L
   quantities rather than `G_PER_L`.
2. Replace the empty solution with a 2 ml/L reference to the TOGO M120 / JCM
   128 trace-element stock, including that stock's 1 L distilled water and its
   MoO3, ZnSO4 x 7H2O, CuSO4 x 5H2O, H3BO3, MnSO4 x nH2O, and CoCl2 x 6H2O
   rows at the stock quantities.
3. Represent the 1 L distilled-water row as water/solvent volume, not
   `1 G_PER_L`.
4. Populate `ph_value: 3.0` and structured preparation steps for HCl
   adjustment and separate sulfur sterilization.
5. Re-ground NiSO4 x 6H2O to an exact hexahydrate term if CHEBI provides one,
   or leave the exact source label visible with a documented unresolved
   grounding if not.
6. Regenerate `data/merge_yaml/merged/` from the corrected TOGO normalized
   input.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  TOGO M155 merged record.
- Manually compare M155 against both the TOGO API payload and the live JCM
  Medium 164 page.
- Verify the M120/JCM 128 trace-element stock is populated and added at 2 ml/L,
  with no trace-stock members flattened into the M155 final ingredient list.
- Run an ignored-inclusive search for `Trace element solution (see Medium
  [M120])` and ensure the same empty-solution defect is absent from
  `hydrogenobacter_thermophilus_medium`.

## Additional Notes

- TOGO M155 intentionally refers to TOGO M120 because M120 mirrors JCM Medium
  128, the trace-stock medium linked from the JCM 164 HTML.
- The source formula is fully defined once M120's trace stock is resolved;
  the current `COMPLEX` and `UNDEFINED` classification appears to be an
  artifact of the unresolved cross-medium solution.

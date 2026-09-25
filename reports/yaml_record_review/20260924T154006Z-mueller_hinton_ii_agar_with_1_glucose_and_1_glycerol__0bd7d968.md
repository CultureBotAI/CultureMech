# YAML Record Review: mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol__0bd7d968

- Repository: CultureMech
- Record: data/merge_yaml/merged/mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol__0bd7d968.yaml
- Started UTC: 2026-09-24T15:40:06Z
- Finished UTC: 2026-09-24T15:41:02Z
- Verdict: needs curation

## Target

Reviewed
`data/merge_yaml/merged/mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol__0bd7d968.yaml`.

The generated record is the single-source direct JCM owner for JCM Medium 505:

- `id`: `CultureMech:002855`
- `media_term`: `mediadive.medium:J505`
- `name`: `mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol`
- `original_name`: `MUELLER HINTON II AGAR WITH 1% GLUCOSE AND 1% GLYCEROL`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `ingredients`: 3
- `merged_from`: `mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol`

## Validation

- Open schema validation: Passed; exited 0 with no diagnostics.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated record preserves the maintained direct JCM owner
`data/normalized_yaml/bacterial/mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol.yaml`
exactly. It correctly points at JCM `GRMD=505`, the same recipe that TOGO
imports as M506.

An exact ignored-file-inclusive search for `CultureMech:002855`,
`CultureMech:009896`, `TOGO:M506`, and `GRMD=505` found two active normalized
owners for JCM Medium 505:

- `CultureMech:002855`:
  `data/normalized_yaml/bacterial/mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol.yaml`
- `CultureMech:009896`:
  `data/normalized_yaml/bacterial/TOGO_M506_Mueller_Hinton_II_Agar_With_1_Glucose_And_1_Glycerol.yaml`

Those owners currently generate two separate YAML files,
`mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol__0bd7d968.yaml` and
`mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol.yaml`, with no
source-duplicate relationship.

`Glucose` and `Glycerol` are grounded correctly. `Mueller Hinton II agar` is
not: the JCM source row is a commercial Mueller Hinton II agar medium mixture,
not pure agar, but the direct JCM owner grounds it to `CHEBI:2509` / `agar`.

## Evidence

The current JCM Medium 505 page lists four rows: 38.0 g
`Mueller Hinton II agar (BD-BBL)`, 10.0 g `Glucose`, 10.0 g `Glycerol`, and
1.0 L `Distilled water`.

The current TOGO M506 API points back to the same JCM page as `JCM_M505` and
reports the same four rows. Unlike the direct JCM owner, the TOGO owner leaves
`Mueller Hinton II agar (BD-BBL)` ungrounded and marks it as an undefined
component.

The generated direct JCM record preserves the three mass rows from JCM 505 at
their final 1 L values but omits the 1 L distilled-water row.

## Completeness

The generated record covers the three non-water ingredients from the source
recipe and is missing only the 1 L water row. That is acceptable if
final-volume solvent rows are intentionally omitted, but it must be reconciled
with the TOGO owner, which currently keeps the water row with the wrong unit.

The JCM page has no medium-specific pH, temperature, organism, or preparation
instructions other than the general page notice to autoclave media at 121 C
for 15 min unless otherwise stated. Their absence from this generated record
was not treated as a defect.

## Findings

- `Mueller Hinton II agar` is over-grounded to `CHEBI:2509` / `agar`; the
  source row names the undefined commercial medium mixture
  `Mueller Hinton II agar (BD-BBL)`.
- The direct JCM 505 owner and TOGO M506 owner are active duplicate
  representations of the same recipe, yet they are not linked with a
  `SOURCE_DUPLICATE` relationship and generate two separate records.

## Recommended Edits

- De-ground `Mueller Hinton II agar` in
  `data/normalized_yaml/bacterial/mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol.yaml`
  or replace it with an ontology term for the complete commercial mixture if
  one exists.
- Add a source-duplicate relationship between the direct JCM owner and
  `data/normalized_yaml/bacterial/TOGO_M506_Mueller_Hinton_II_Agar_With_1_Glucose_And_1_Glycerol.yaml`.
- Decide once whether the 1 L distilled-water row should be omitted as a final
  solvent or retained as a volume row, and make the TOGO and direct-JCM owners
  consistent.
- Regenerate the merged YAML so JCM 505 appears once instead of as separate
  direct-JCM and TOGO generated records.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the
  regenerated YAML.
- Run an ignored-file-inclusive exact search for `GRMD=505` after repair and
  confirm both JCM-derived owners point at one canonical generated record.
- Confirm `Mueller Hinton II agar (BD-BBL)` is not grounded to pure agar in the
  regenerated record.

## Additional Notes

The TOGO M506 generated record was reviewed immediately before this sibling.

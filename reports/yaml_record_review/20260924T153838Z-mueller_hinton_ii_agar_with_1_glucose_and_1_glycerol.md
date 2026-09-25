# YAML Record Review: mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol

- Repository: CultureMech
- Record: data/merge_yaml/merged/mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol.yaml
- Started UTC: 2026-09-24T15:38:38Z
- Finished UTC: 2026-09-24T15:40:05Z
- Verdict: needs curation

## Target

Reviewed
`data/merge_yaml/merged/mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol.yaml`.

The generated record is the single-source TOGO import for JCM Medium 505:

- `id`: `CultureMech:009896`
- `media_term`: `TOGO:M506`
- `name`: `mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol`
- `original_name`: `Mueller Hinton II Agar With 1% Glucose And 1% Glycerol`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `ingredients`: 4
- `merged_from`:
  `TOGO_M506_Mueller_Hinton_II_Agar_With_1_Glucose_And_1_Glycerol`

## Validation

- Open schema validation: Passed with `No issues found`.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated record preserves the maintained TOGO owner
`data/normalized_yaml/bacterial/TOGO_M506_Mueller_Hinton_II_Agar_With_1_Glucose_And_1_Glycerol.yaml`
exactly. Its TOGO identity is grounded correctly: TOGO `M506` is sourced from
JCM Medium `505`, whose public JCM URL uses `GRMD=505`.

An exact ignored-file-inclusive search for `CultureMech:009896`,
`CultureMech:002855`, `TOGO:M506`, and `GRMD=505` found two active normalized
owners for the same JCM recipe:

- `CultureMech:009896`:
  `data/normalized_yaml/bacterial/TOGO_M506_Mueller_Hinton_II_Agar_With_1_Glucose_And_1_Glycerol.yaml`
- `CultureMech:002855`:
  `data/normalized_yaml/bacterial/mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol.yaml`

Those owners currently generate two separate YAML files,
`mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol.yaml` and
`mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol__0bd7d968.yaml`, with no
source-duplicate relationship.

Ingredient grounding is mostly source-faithful. `Glucose`, `Glycerol`, and
`Distilled water` are grounded to appropriate simple CHEBI terms, while the
commercial `Mueller Hinton II agar (BD-BBL)` mixture is intentionally left
ungrounded.

## Evidence

The current TOGO M506 API reports the original medium ID as `JCM_M505` and the
source URL as JCM `GRMD=505`. Its component list contains 38 g
`Mueller Hinton II agar (BD-BBL)`, 10 g `Glucose`, 10 g `Glycerol`, and
1 L `Distilled water`.

The current JCM Medium 505 page confirms the same recipe in the same units:
38.0 g `Mueller Hinton II agar (BD-BBL)`, 10.0 g `Glucose`, 10.0 g
`Glycerol`, and 1.0 L `Distilled water`.

The generated TOGO record stores the three mass components as g/L values that
match a 1 L final recipe: 38 g/L commercial Mueller Hinton II agar, 10 g/L
glucose, and 10 g/L glycerol. It stores the water row as `1 G_PER_L`, which
comes from the source quantity `1 L` but is not a correct unit conversion.

## Completeness

The generated record covers all source rows from the TOGO/JCM recipe, including
the 1 L water row. The only completeness problem is that water is represented
as 1 g/L instead of a volume, or omitted if final-volume solvent rows are not
modeled.

The JCM page has no medium-specific pH, temperature, organism, or preparation
instructions other than the general page notice to autoclave media at 121 C
for 15 min unless otherwise stated. Their absence from this generated record
was not treated as a defect.

## Findings

- `Distilled water` is imported with `value: '1'` and `unit: G_PER_L`, but the
  TOGO and JCM sources both specify 1 L water.
- The TOGO M506 owner and the direct JCM 505 owner are active duplicate
  representations of the same recipe, yet they are not linked with a
  `SOURCE_DUPLICATE` relationship and generate two separate records.

## Recommended Edits

- Repair
  `data/normalized_yaml/bacterial/TOGO_M506_Mueller_Hinton_II_Agar_With_1_Glucose_And_1_Glycerol.yaml`
  by representing the 1 L water row with an appropriate volume unit or by
  omitting it as final-volume solvent if that matches the curation standard.
- Add a source-duplicate relationship between the TOGO M506 owner and
  `data/normalized_yaml/bacterial/mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol.yaml`.
- Keep `Mueller Hinton II agar (BD-BBL)` ungrounded as an undefined commercial
  mixture; do not collapse it to pure CHEBI agar.
- Regenerate the merged YAML so JCM 505 appears once instead of as separate
  TOGO and direct-JCM generated records.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the
  regenerated YAML.
- Run an ignored-file-inclusive exact search for `GRMD=505` after repair and
  confirm both JCM-derived owners point at one canonical generated record.
- Confirm the regenerated recipe keeps 10 g/L glucose, 10 g/L glycerol, and
  38 g/L `Mueller Hinton II agar (BD-BBL)`.

## Additional Notes

The sibling generated record
`data/merge_yaml/merged/mueller_hinton_ii_agar_with_1_glucose_and_1_glycerol__0bd7d968.yaml`
will be reviewed separately in sorted order.

# YAML Record Review: mueller_hinton_mh_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/mueller_hinton_mh_agar.yaml
- Started UTC: 2026-09-24T15:45:20Z
- Finished UTC: 2026-09-24T15:46:41Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/mueller_hinton_mh_agar.yaml`.

The generated record is the single-source TOGO M2942 record:

- `id`: `CultureMech:009472`
- `media_term`: `TOGO:M2942`
- `name`: `mueller_hinton_mh_agar`
- `original_name`: `Mueller Hinton (MH) agar`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `ingredients`: 4
- `merged_from`: `mueller_hinton_mh_agar`

## Validation

- Open schema validation: Passed with `No issues found`.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated record preserves the active maintained owner
`data/normalized_yaml/bacterial/mueller_hinton_mh_agar.yaml` exactly. An exact
ignored-file-inclusive search for `CultureMech:009472` and `TOGO:M2942` found
only this active normalized owner, this generated merge, and registry/catalog
entries in current `data/` scope.

The TOGO identity and solid-agar state are correct, but the source row is
misquantified. TOGO M2942 describes 1 L of the complex component
`Mueller Hinton (MH) agar`; the generated YAML stores the row as
`1 G_PER_L`.

The three gas rows are source-supported but incomplete. TOGO's paper comment
specifies 5% `O2`, 10% `CO2`, and 85% `N2`; the generated record stores those
gases as `VARIABLE` ingredients and does not preserve the proportions or the
42 C incubation temperature. `Carbon dioxide gas` and `Nitrogen gas` are
grounded to CHEBI, while `Oxygen gas` is ungrounded.

## Evidence

The current TOGO M2942 API has no original source URL. It lists four
components: 1 L `Mueller Hinton (MH) agar`, `Carbon dioxide gas`,
`Nitrogen gas`, and `Oxygen gas`. Its first comment says bacterial cultures
were routinely grown on Mueller Hinton agar in anaerobic jars under
microaerobic conditions of 5% oxygen, 10% carbon dioxide, and 85% nitrogen at
42 C.

The generated YAML keeps the complex agar component and three gas identities
but omits the atmosphere percentages and temperature.

## Completeness

The generated record is not complete enough to reconstruct the source
cultivation condition because the quantified atmosphere is reduced to three
unqualified variable gas rows. It also carries non-English source labels for
the gas property in user-visible notes.

## Findings

- The 1 L `Mueller Hinton (MH) agar` source component is represented as
  1 g/L.
- The source atmosphere of 5% `O2`, 10% `CO2`, and 85% `N2` is collapsed into
  three `VARIABLE` concentration gas rows.
- `Oxygen gas` is ungrounded even though the neighboring gas molecules are
  grounded.
- All three gas rows carry non-English source labels for the `Gas` property in
  their notes.
- The 42 C incubation temperature from the TOGO comment is not preserved.

## Recommended Edits

- Re-curate
  `data/normalized_yaml/bacterial/mueller_hinton_mh_agar.yaml` from TOGO M2942.
- Represent the 1 L `Mueller Hinton (MH) agar` row as a final volume or omit it
  as a complete medium component rather than converting it to 1 g/L.
- Preserve the 5% `O2`, 10% `CO2`, and 85% `N2` atmosphere and 42 C
  incubation temperature in an appropriate structured field or source note.
- Ground `Oxygen gas` to an exact CHEBI oxygen molecule term.
- Normalize the gas `Properties` notes to English.
- Regenerate the merged YAML from the repaired owner.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the
  regenerated YAML.
- Confirm the regenerated record preserves the TOGO M2942 atmosphere
  percentages and no longer contains a bogus 1 g/L Mueller Hinton agar
  concentration.

## Additional Notes

None.

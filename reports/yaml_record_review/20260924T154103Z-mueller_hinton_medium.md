# YAML Record Review: mueller_hinton_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/mueller_hinton_medium.yaml
- Started UTC: 2026-09-24T15:41:03Z
- Finished UTC: 2026-09-24T15:42:18Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/mueller_hinton_medium.yaml`.

The generated record is the single-source merge for TOGO M2929:

- `id`: `CultureMech:009463`
- `media_term`: `TOGO:M2929`
- `name`: `mueller_hinton_medium`
- `original_name`: `Mueller-Hinton medium`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `ingredients`: 8
- `merged_from`: `mueller_hinton_medium`

## Validation

- Open schema validation: Passed with `No issues found`.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated record preserves the maintained owner
`data/normalized_yaml/bacterial/mueller_hinton_medium.yaml` exactly. An exact
ignored-file-inclusive search for `CultureMech:009463` and `TOGO:M2929` found
only this active normalized owner, this generated merge, and registry/catalog
entries in current `data/` scope.

The TOGO identity is correct, but the recipe content is over-specific for the
source. TOGO M2929 names a generic 1 L `Mueller-Hinton medium`; it does not
break that complex medium into beef extract, casein hydrolysate, starch, and
agar. The four gas rows are traceable to the source comment for a
microaerophilic atmosphere, but the generated record stores them as variable
ingredients and drops the explicit proportions: 83% `N2`, 4% `H2`, 8% `O2`,
and 5% `CO2`.

Ingredient grounding is partially complete. `Carbon dioxide gas`,
`Nitrogen gas`, and `Hydrogen gas` are grounded to CHEBI gas molecules, but
`Oxygen gas` is not grounded. The nitrogen row also preserves the TOGO
Japanese label for `Gas` in a user-visible note where neighboring gas rows use
English.

## Evidence

The current TOGO M2929 API has no original source URL and lists one medium row:
1 L `Mueller-Hinton medium`, labeled `Mueller-Hinton agar` by GMO and marked
as an undefined complex component. Its only comment says two
`C. jejuni` strains were cultured in Mueller-Hinton medium and incubated at
37 C under microaerophilic conditions of 83% `N2`, 4% `H2`, 8% `O2`, and
5% `CO2`.

The generated record instead contains a manually researched commercial
Mueller-Hinton Agar decomposition: 2.0 g/L `Beef extract`, 17.5 g/L
`Acid hydrolysate of casein`, 1.5 g/L `Starch`, and 17.0 g/L `Agar`, all
carrying supplier notes that cite a Microbe Notes page accessed on
2026-03-28.

## Completeness

The source-supported gas ingredients are incomplete because their percentages
are replaced by `variable`. If the schema has no better atmosphere model, the
percentages should still survive in notes or preparation context.

The expanded commercial agar formulation may be useful as an interpretation,
but it is not complete source evidence for this TOGO record. It changes the
source from a 1 L undefined Mueller-Hinton medium into a solidifying agar
recipe while the record remains `physical_state: LIQUID`.

## Findings

- The generated record over-specifies the source by replacing TOGO M2929's
  1 L undefined `Mueller-Hinton medium` with a manually researched
  Mueller-Hinton Agar constituent list.
- `physical_state: LIQUID` conflicts with the 17 g/L `Agar` row that came from
  the commercial Mueller-Hinton Agar interpretation.
- The microaerophilic atmosphere is represented as four `VARIABLE`
  concentration ingredients, losing the source percentages of 83% `N2`,
  4% `H2`, 8% `O2`, and 5% `CO2`.
- `Oxygen gas` is ungrounded even though CHEBI has a dioxygen term analogous
  to the existing `carbon dioxide`, `dinitrogen`, and `dihydrogen` groundings.
- The `Nitrogen gas` note carries a non-English source label for the `Gas`
  property, unlike the neighboring gas rows.

## Recommended Edits

- Re-curate TOGO M2929 from the TOGO payload as a 1 L undefined
  `Mueller-Hinton medium` record unless there is direct evidence that the paper
  used the exact commercial Mueller-Hinton Agar formulation now encoded here.
- If the agar formulation is kept, either change the physical state to
  `SOLID_AGAR` with supporting evidence or remove the 17 g/L agar for a liquid
  Mueller-Hinton medium.
- Preserve the microaerophilic gas proportions from the TOGO comment in an
  atmosphere/preparation field or in source notes instead of collapsing them
  to unqualified `VARIABLE` ingredient rows.
- Ground `Oxygen gas` to an exact CHEBI oxygen molecule term.
- Normalize the nitrogen `Properties` note to English.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the
  regenerated YAML.
- Confirm the regenerated record no longer mixes `LIQUID` state with a
  solidifying agar concentration.
- Confirm the 83% `N2`, 4% `H2`, 8% `O2`, and 5% `CO2` values survive the
  repair if atmosphere gases remain in scope.

## Additional Notes

Name-based searches also find TOGO Mueller-Hinton records supplemented with
rabbit serum; those are distinct records and were not treated as duplicates of
TOGO M2929.

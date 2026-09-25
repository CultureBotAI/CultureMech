# YAML Record Review: mueller_hinton_mh_broth

- Repository: CultureMech
- Record: data/merge_yaml/merged/mueller_hinton_mh_broth.yaml
- Started UTC: 2026-09-24T15:46:42Z
- Finished UTC: 2026-09-24T15:48:17Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/mueller_hinton_mh_broth.yaml`.

The generated record is the single-source TOGO M2937 broth record:

- `id`: `CultureMech:009468`
- `media_term`: `TOGO:M2937`
- `name`: `mueller_hinton_mh_broth`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `ingredients`: 2
- `merged_from`: `mueller_hinton_mh_broth`

## Validation

- Open schema validation: Passed with `No issues found`.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated record preserves the pre-repair TOGO M2937 owner content and is
stale relative to
`data/normalized_yaml/bacterial/mueller_hinton_mh_broth.yaml`, which was
repaired on 2026-09-07 to correct the broth and ciprofloxacin quantities,
ground ciprofloxacin, add `temperature_value: 42.0`, add source fields, and
add a TOGO reference.

An exact ignored-file-inclusive search for `CultureMech:009468` and
`TOGO:M2937` found only this active normalized owner, this generated merge,
and registry/catalog entries in current `data/` scope.

## Evidence

The current TOGO M2937 API has no original source URL. It lists
`ciprofloxacin (if needed)` at 4 ug/ml and 1 L
`Mueller-Hinton (MH) broth`. Its comment says the Campylobacter strains were
grown routinely in Mueller-Hinton broth or on MH agar plates at 42 C under
microaerophilic conditions, and that culture medium was supplemented with
ciprofloxacin at 4 ug/ml when needed.

The generated YAML converts the 1 L complex broth row to `1 G_PER_L` and the
4 ug/ml ciprofloxacin row to `4 G_PER_L`. The maintained owner now stores the
broth as 1000 ml/L and ciprofloxacin as 4 mg/L, which is the correct
equivalent of 4 ug/ml.

## Completeness

The generated record lists both source components but omits source-supported
context that the maintained owner now carries:

- ciprofloxacin is optional, not part of every MH broth culture;
- ciprofloxacin is an antimicrobial inhibitor;
- cultures were grown at 42 C.

The broader microaerophilic atmosphere is mentioned in the source comment but
not quantified in the TOGO payload for M2937.

## Findings

- The generated YAML is stale. The maintained owner was repaired on
  2026-09-07, but this generated file still reflects the older TOGO import.
- `Mueller-Hinton (MH) broth` is represented as 1 g/L instead of the source
  value 1 L, now curated as 1000 ml/L.
- `ciprofloxacin (if needed)` is represented as 4 g/L instead of the source
  value 4 ug/ml, now curated as 4 mg/L.
- The generated ciprofloxacin row is ungrounded and lacks the maintained
  owner's antimicrobial/inhibitor role.
- The 42 C incubation temperature from the TOGO comment is not preserved.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/mueller_hinton_mh_broth.yaml` from the
  already repaired maintained owner.
- Confirm the regenerated file preserves 1000 ml/L `Mueller-Hinton broth`,
  4 mg/L `Ciprofloxacin`, `temperature_value: 42.0`, source fields, quality
  flags, and the TOGO reference.
- Preserve in notes that ciprofloxacin is added only when needed unless an
  optional-ingredient field is available.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the
  regenerated YAML.
- Confirm there is no remaining 4 g/L ciprofloxacin concentration.
- Confirm the regenerated record carries the 2026-09-07 curation-history
  repair entry.

## Additional Notes

None.

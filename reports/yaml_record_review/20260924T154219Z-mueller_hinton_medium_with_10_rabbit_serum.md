# YAML Record Review: mueller_hinton_medium_with_10_rabbit_serum

- Repository: CultureMech
- Record: data/merge_yaml/merged/mueller_hinton_medium_with_10_rabbit_serum.yaml
- Started UTC: 2026-09-24T15:42:19Z
- Finished UTC: 2026-09-24T15:44:08Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/mueller_hinton_medium_with_10_rabbit_serum.yaml`.

The generated record is the single-source TOGO M2583 broth recipe:

- `id`: `CultureMech:009151`
- `media_term`: `TOGO:M2583`
- `name`: `mueller_hinton_medium_with_10_rabbit_serum`
- `original_name`: `Mueller Hinton Medium with 10% Rabbit Serum`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `ingredients`: 3
- `merged_from`: `mueller_hinton_medium_with_10_rabbit_serum`

## Validation

- Open schema validation: Passed; exited 0 with no diagnostics.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated record preserves the pre-repair TOGO M2583 owner content and is
stale relative to
`data/normalized_yaml/bacterial/mueller_hinton_medium_with_10_rabbit_serum.yaml`,
which was repaired on 2026-09-10 to correct liquid volumes, add source fields,
add preparation steps, add a TOGO reference, and add curation quality flags.

An exact ignored-file-inclusive search for `CultureMech:009151`,
`TOGO:M2583`, `M2583`, and the ATCC PDF slug found only this active normalized
broth owner, this generated broth YAML, the separate solid-media sibling, and
registry/catalog entries in current `data/` scope.

The generated record intentionally leaves the complex commercial
`Mueller Hinton Broth (BD 211443)` and `Rabbit serum` components ungrounded.
That is appropriate for the source. The maintained owner has also grounded
`DI Water` to CHEBI water, but that post-repair grounding has not reached the
generated YAML.

## Evidence

The current TOGO M2583 API lists `DI Water` 900 ml,
`Mueller Hinton Broth (BD 211443)` 22 g, and a separate 100 ml `Rabbit serum`
component. Its comment says to autoclave at 121 C, let cool, aseptically add
100 ml sterile rabbit serum, and dispense into an appropriate vessel.

The original ATCC Medium 1452 PDF confirms the same broth formulation:
22.0 g `Mueller Hinton Broth (BD 211443)`, 900 ml `DI Water`, then
autoclave, cool, aseptically add 100 ml sterile rabbit serum, and dispense.

The generated YAML instead stores the two source volumes as mass
concentrations: `DI Water` at 900 g/L and `Rabbit serum` at 100 g/L. The
maintained owner now stores these correctly as 900 ml/L and 100 ml/L.

## Completeness

The generated record carries all three source ingredients but is missing the
source preparation sequence that was added to the maintained owner:

- Prepare 900 ml DI water with 22 g Mueller Hinton Broth.
- Autoclave at 121 C and let cool.
- Aseptically add 100 ml sterile rabbit serum.
- Dispense into an appropriate vessel.

The generated record also lacks the maintained owner's `sterilization`,
`data_quality_flags`, per-ingredient `source` fields, and structured TOGO
reference because it predates the owner repair.

## Findings

- The generated YAML is stale. The maintained owner was repaired on
  2026-09-10, but this generated file still reflects the older TOGO import.
- `DI Water` is represented as 900 g/L instead of the source value
  900 ml/L.
- `Rabbit serum` is represented as 100 g/L instead of the source value
  100 ml/L.
- The generated record is missing the ATCC/TOGO preparation steps for
  autoclaving, cooling, aseptically adding sterile rabbit serum, and
  dispensing.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/mueller_hinton_medium_with_10_rabbit_serum.yaml`
  from the already repaired maintained owner.
- Confirm the regenerated file preserves 900 ml/L `DI Water`, 22 g/L
  `Mueller Hinton Broth (BD 211443)`, and 100 ml/L `Rabbit serum`.
- Confirm the regenerated file keeps the 2026-09-10 curation history entry,
  preparation steps, `sterilization`, `data_quality_flags`, and TOGO
  reference.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the
  regenerated YAML.
- Compare this broth record with the solid
  `mueller_hinton_medium_with_10_rabbit_serum_agar` sibling and confirm they
  remain separate because one uses BD 211443 Mueller Hinton Broth and the
  other uses BD 225250 Mueller Hinton Agar.

## Additional Notes

The fetched ATCC Medium 1452 PDF also includes the solid-media formulation
covered by the next generated YAML in sorted order.

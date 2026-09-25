# YAML Record Review: mueller_hinton_medium_with_10_rabbit_serum_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/mueller_hinton_medium_with_10_rabbit_serum_agar.yaml
- Started UTC: 2026-09-24T15:44:09Z
- Finished UTC: 2026-09-24T15:45:19Z
- Verdict: needs curation

## Target

Reviewed
`data/merge_yaml/merged/mueller_hinton_medium_with_10_rabbit_serum_agar.yaml`.

The generated record is the single-source TOGO M2584 solid-media recipe:

- `id`: `CultureMech:009152`
- `media_term`: `TOGO:M2584`
- `name`: `mueller_hinton_medium_with_10_rabbit_serum_agar`
- `original_name`: `Mueller Hinton Medium with 10% Rabbit Serum (Agar)`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `ingredients`: 6
- `merged_from`: `mueller_hinton_medium_with_10_rabbit_serum_agar`

## Validation

- Open schema validation: Passed; exited 0 with no diagnostics.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated record preserves
`data/normalized_yaml/bacterial/mueller_hinton_medium_with_10_rabbit_serum_agar.yaml`
exactly, so the required curation belongs in the maintained owner before
regeneration.

An exact ignored-file-inclusive search for `CultureMech:009152`,
`TOGO:M2584`, `M2584`, the ATCC PDF slug, and `BD 225250` found only this
active normalized solid-media owner, this generated solid-media YAML, the
separate broth sibling that shares the same ATCC PDF, and registry/catalog
entries in current `data/` scope.

The source identity is correct: TOGO M2584 points at the solid-media block in
ATCC Medium 1452. The ingredient grounding is over-specific. The ATCC/TOGO
source asks for the commercial undefined mixture
`Mueller Hinton Agar (BD 225250)`; the record decomposes that product into
`Beef extract`, `Acid hydrolysate of casein`, `Starch`, and `Agar` with
supplier notes for a different catalog set.

## Evidence

The current TOGO M2584 API lists `DI Water` 900 ml,
`Mueller Hinton Agar (BD 225250)` 38 g, and a separate 100 ml `Rabbit serum`
component. Its comment says this is the solid-media recipe and instructs the
curator to autoclave at 121 C, cool to 48 C, aseptically add 100 ml sterile
rabbit serum, and dispense into an appropriate vessel.

The original ATCC Medium 1452 PDF confirms the same solid-media formulation:
38.0 g `Mueller Hinton Agar (BD 225250)`, 900 ml `DI Water`, then autoclave,
cool to 48 C, aseptically add 100 ml sterile rabbit serum, and dispense.

The generated YAML instead stores 900 ml `DI Water` and 100 ml `Rabbit serum`
as 900 g/L and 100 g/L, and it replaces the single 38 g commercial agar
component with four inferred constituents. Those inferred constituents are
tagged with Microbe Notes supplier metadata for BD 211443 and Sigma 70191,
while the source calls specifically for BD 225250.

## Completeness

The generated record has the right TOGO identity and solid-agar state, but it
is missing the source commercial agar component and preparation sequence:

- Combine 900 ml DI water with 38 g Mueller Hinton Agar BD 225250.
- Autoclave at 121 C and cool to 48 C.
- Aseptically add 100 ml sterile rabbit serum.
- Dispense into an appropriate vessel.

The generated record also lacks structured references and a TOGO-source
quality flag.

## Findings

- `DI Water` is represented as 900 g/L instead of the source value
  900 ml/L.
- `Rabbit serum` is represented as 100 g/L instead of the source value
  100 ml/L.
- The source ingredient `Mueller Hinton Agar (BD 225250)` is missing; it was
  replaced with a manual beef/casein/starch/agar breakdown that the ATCC and
  TOGO sources do not provide.
- The supplier catalog evidence is mismatched: the source uses BD 225250, but
  the generated constituent notes cite BD 211443, Sigma 70191, and HiMedia via
  an external Microbe Notes page.
- The ATCC/TOGO preparation steps for autoclaving, cooling to 48 C,
  aseptically adding sterile rabbit serum, and dispensing are missing.

## Recommended Edits

- Re-curate
  `data/normalized_yaml/bacterial/mueller_hinton_medium_with_10_rabbit_serum_agar.yaml`
  from TOGO M2584 and the ATCC Medium 1452 PDF.
- Replace the inferred beef/casein/starch/agar components with the single
  source component `Mueller Hinton Agar (BD 225250)` at 38 g/L unless direct
  BD 225250 formulation evidence is added.
- Correct `DI Water` to 900 ml/L and `Rabbit serum` to 100 ml/L.
- Add the ATCC preparation steps and a structured TOGO reference.
- Regenerate the merged YAML from the repaired owner.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the
  regenerated YAML.
- Confirm the regenerated record no longer cites BD 211443 or the Microbe
  Notes commercial-product decomposition.
- Compare this solid record with the liquid
  `mueller_hinton_medium_with_10_rabbit_serum` sibling and confirm they remain
  separate because the ATCC source lists distinct broth and solid formulations.

## Additional Notes

None.

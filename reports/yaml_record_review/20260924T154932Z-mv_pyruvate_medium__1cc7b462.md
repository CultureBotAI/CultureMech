# YAML Record Review: mv_pyruvate_medium__1cc7b462

- Repository: CultureMech
- Record: data/merge_yaml/merged/mv_pyruvate_medium__1cc7b462.yaml
- Started UTC: 2026-09-24T15:49:32Z
- Finished UTC: 2026-09-24T15:51:04Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/mv_pyruvate_medium__1cc7b462.yaml`.

The generated record is a merge of JCM Medium 541 with its referenced JCM
Medium 388 parent:

- canonical `id`: `CultureMech:002890`
- canonical `media_term`: `mediadive.medium:J541`
- canonical `name`: `mv_pyruvate_medium`
- canonical `original_name`: `MV/PYRUVATE MEDIUM`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `ingredients`: 29
- `merged_from`: `mv_lactate_medium` and `mv_pyruvate_medium`

## Validation

- Open schema validation: Passed with `No issues found`.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated record incorrectly treats JCM 541 and JCM 388 as exact source
duplicates. JCM 541 is not an exact duplicate: the JCM source explicitly says
to use JCM Medium 388 with 1.0 g/L sodium pyruvate instead of sodium lactate.
The direct JCM 541 owner copied the referenced JCM 388 composition on
2026-04-04 but retained `Sodium lactate`, so it acquired the same ingredient
signature as the lactate parent and was merged with `mv_lactate_medium`.

An exact ignored-file-inclusive search for `CultureMech:002890`, `GRMD=541`,
`TOGO:M543`, and `CultureMech:009936` found two active normalized owners for
JCM 541:

- `CultureMech:002890`:
  `data/normalized_yaml/bacterial/mv_pyruvate_medium.yaml`
- `CultureMech:009936`:
  `data/normalized_yaml/bacterial/TOGO_M543_MV_Pyruvate_Medium.yaml`

Those owners generate two separate records. The TOGO M543 owner does contain a
`sodium pyruvate` ingredient, though it has its own unit and placeholder
solution issues. The direct JCM owner reviewed here contains `Sodium lactate`
instead.

`NiCl2 x 6 H2O` is also over-broadened to generic `CHEBI:34887` / `nickel
dichloride`; the hydrate-specific source label should not resolve to generic
nickel dichloride.

## Evidence

The current JCM 541 page for `MV/PYRUVATE MEDIUM` says to use Medium No. 388
with 1.0 g/L sodium pyruvate instead of sodium lactate, and otherwise prepare
the medium as described in the recipe for Medium No. 388.

The current JCM 388 page for `MV/LACTATE MEDIUM` lists 1.0 g sodium lactate in
its 1 L base recipe, plus 1 ml FeCl2 solution, 1 ml trace element solution,
and 10 ml trace vitamins from other JCM stock recipes. The local generated
JCM 541 record contains the lactate ingredient from this parent rather than
the pyruvate replacement.

The current TOGO M543 API also points back to JCM 541 and lists `sodium
pyruvate`, confirming that the pyruvate replacement is part of the source
identity.

## Completeness

The generated JCM 541 record is not complete enough to represent the source
because the one required variant substitution was not applied. It also flattens
the FeCl2, trace element, and trace vitamin stock additions inherited from JCM
388 into individual stock solutes in top-level final ingredients. For example,
it lists SL-10-like trace salts such as `FeCl2 x 4 H2O`, `ZnCl2`,
`MnCl2 x 4 H2O`, and `NiCl2 x 6 H2O` at stock g/L concentrations rather than
representing the 1 ml/L trace-element addition from the JCM 388 parent.

## Findings

- The generated record contains `Sodium lactate`, but JCM 541 specifically
  replaces the JCM 388 lactate source with 1.0 g/L sodium pyruvate.
- JCM 541 was merged with JCM 388 as a `SOURCE_DUPLICATE`, erasing the actual
  pyruvate-vs-lactate variant relationship.
- The JCM 388 stock solutions were flattened into final ingredients. The
  generated YAML lists stock-strength trace metal and vitamin concentrations
  instead of preserving the 1 ml/L and 10 ml/L stock additions.
- `NiCl2 x 6 H2O` is grounded to generic `CHEBI:34887` / `nickel dichloride`.
- The active TOGO M543 owner for the same JCM 541 source is unlinked to the
  direct JCM 541 owner, so the same provider recipe generates two records.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/mv_pyruvate_medium.yaml` by replacing
  `Sodium lactate` with 1.0 g/L sodium pyruvate when copying JCM 388 into JCM
  541.
- Change the relationship to `mv_lactate_medium` from `SOURCE_DUPLICATE` to a
  variant relationship that records the lactate-to-pyruvate substitution.
- Preserve inherited JCM 388 stock additions as stock additions if the schema
  can model them, or scale their components into final concentrations before
  generation.
- Ground `NiCl2 x 6 H2O` to a hydrate-specific CHEBI term.
- Link the direct JCM 541 owner to the TOGO M543 owner for deduplication after
  both are corrected.
- Regenerate the merged YAML after repairing the maintained owners.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the
  regenerated YAML.
- Confirm the regenerated JCM 541 record contains sodium pyruvate and no sodium
  lactate.
- Confirm JCM 388 and JCM 541 no longer share the same merge fingerprint.
- Confirm an ignored-file-inclusive exact search for `GRMD=541` shows the
  direct JCM and TOGO owners linked to a single corrected generated record.

## Additional Notes

The TOGO M543 generated record was found during this review but had sorted
earlier than this lowercase JCM-derived generated record, so it was not
reviewed here.

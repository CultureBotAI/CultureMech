# YAML Record Review: mueller_hinton

- Repository: CultureMech
- Record: data/merge_yaml/merged/mueller_hinton.yaml
- Started UTC: 2026-09-24T15:37:22Z
- Finished UTC: 2026-09-24T15:38:37Z
- Verdict: pass

## Target

Reviewed `data/merge_yaml/merged/mueller_hinton.yaml`.

The generated record is the single-source merge for DSMZ/MediaDive Medium
1709:

- `id`: `CultureMech:001190`
- `media_term`: `mediadive.medium:1709`
- `name`: `mueller_hinton`
- `original_name`: `MUELLER-HINTON`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `ph_value`: 7.3
- `ingredients`: 4
- `merged_from`: `mueller_hinton`

## Validation

- Open schema validation: Passed; exited 0 with no diagnostics.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated record preserves the active maintained owner
`data/normalized_yaml/bacterial/mueller_hinton.yaml`: same `CultureMech:001190`
identifier, DSMZ/MediaDive 1709 term, medium name, solid-agar state, pH, four
ingredients, concentrations, beef-infusion and agar notes, and pH adjustment
step.

An exact ignored-file-inclusive search for `CultureMech:001190` and
`mediadive.medium:1709` found only this active normalized owner, this generated
merge, and registry/catalog entries in current `data/` scope.

The defined additives that have CHEBI terms, `Starch` and `Agar`, are grounded
to exact local terms. `Beef` and `Casein hydrolysate` are complex/undefined
ingredients and are intentionally ungrounded in the imported owner and the
generated record.

## Evidence

MediaDive REST and HTML for medium 1709 currently describe DSMZ
`MUELLER-HINTON` as a complex medium with pH 7.3. The 1000 ml recipe contains
2 g `Beef` with the condition `dehydrated infusion from 300g`, 17.5 g
`Casein hydrolysate`, 1.5 g `Starch`, 15 g `Agar` for solid medium, 1000 ml
distilled water, and the preparation step `Adjust pH to 7.3.`.

The generated record preserves the non-water ingredients and concentrations
from that recipe: `Beef` at 2 g/L with the dehydrated-infusion note,
`Casein hydrolysate` at 17.5 g/L, `Starch` at 1.5 g/L, and `Agar` at 15 g/L
with the solid-medium note.

## Completeness

No missing required or source-supported recipe fields were found.

`target_organisms` and structured `references` are absent. They are useful
future enrichment targets but were not treated as defects for this generated
single-source record because the imported MediaDive payload already encodes
the medium identity and source URL.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation after any
  future regeneration.
- If the maintained owner gains target organisms or structured references,
  confirm the generated record preserves them.

## Additional Notes

None.

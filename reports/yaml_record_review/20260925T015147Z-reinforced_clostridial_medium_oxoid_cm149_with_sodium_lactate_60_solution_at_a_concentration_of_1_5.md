# YAML Record Review: reinforced_clostridial_medium_oxoid_cm149_with_sodium_lactate_60_solution_at_a_concentration_of_1_5

- Repository: CultureMech
- Record: `data/merge_yaml/merged/reinforced_clostridial_medium_oxoid_cm149_with_sodium_lactate_60_solution_at_a_concentration_of_1_5.yaml`
- Started UTC: 2026-09-25T01:50:28Z
- Finished UTC: 2026-09-25T01:51:47Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:009180` for TOGO Medium M2613 / `TOGO:M2613`, generated from `data/normalized_yaml/bacterial/reinforced_clostridial_medium_oxoid_cm149_with_sodium_lactate_60_solution_at_a_concentration_of_1_5.yaml`.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

TOGO M2613 imports ATCC Medium 1252, and exact ignored-inclusive searches found `TOGO:M2613` only on this owner and generated target among the searched owner, target, and manifest paths. The ATCC PDF URL in the TOGO metadata still resolves and identifies the same reinforced clostridial medium with 1.5% sodium lactate.

## Evidence

TOGO M2613 lists 1000 ml distilled water, 1.5% sodium lactate 60% solution, 38 g Reinforced Clostridial medium (Oxoid CM149), and a comment to adjust final pH to 7.0. The ATCC Medium 1252 PDF confirms the medium title and final pH 7.0. The current normalized owner has already flattened sodium lactate from `solutions` into an ingredient, records the pH, adds source notes, and keeps the Oxoid base opaque because ATCC 1252 does not disclose its full commercial composition.

## Completeness

The current generated target is a stale pre-repair snapshot. It still lacks the sodium lactate ingredient and the pH despite both being the defining additions in the source title and ATCC sheet.

## Findings

- The generated target leaves `Sodium lactate (60% solution)` under `solutions` with an empty `composition: []` and `name: Unknown solution` instead of emitting it as the 1.5% ingredient listed by TOGO M2613 and ATCC Medium 1252.
- The generated target records distilled water as `1000 G_PER_L`, while TOGO states `1000 ml` and the September owner repair converted it to a volume unit.
- The generated target is stale relative to `data/normalized_yaml/bacterial/reinforced_clostridial_medium_oxoid_cm149_with_sodium_lactate_60_solution_at_a_concentration_of_1_5.yaml`: it lacks `ph_value: 7.0`, source-scoped ingredient notes, the sodium lactate CHEBI grounding and carbon-source role, the ATCC pH preparation step, `data_quality_flags`, and both TOGO and ATCC references.

## Recommended Edits

- Regenerate `data/merge_yaml/merged` from the repaired normalized owner so the generated target includes the corrected water row, sodium lactate as an ingredient, pH 7.0, source notes, and references.
- Keep Oxoid CM149 as an opaque unmapped commercial component unless a product specification for that exact catalog item is added as a separate evidence source.

## Follow-up Checks

- Confirm the regenerated target has exactly three top-level ingredients: distilled water, sodium lactate 60% solution at 1.5%, and Reinforced Clostridial medium (Oxoid CM149) at 38 g/L.
- Confirm no `Unknown solution` entry remains for sodium lactate.
- Re-run open schema, strict, reference, and term validation for the regenerated target.

## Additional Notes

No additional normalized-YAML correction is required for the September repair as inspected here; this generated record needs to be refreshed from that owner.

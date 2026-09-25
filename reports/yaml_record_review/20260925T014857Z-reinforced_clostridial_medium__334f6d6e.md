# YAML Record Review: reinforced_clostridial_medium__334f6d6e

- Repository: CultureMech
- Record: `data/merge_yaml/merged/reinforced_clostridial_medium__334f6d6e.yaml`
- Started UTC: 2026-09-25T01:47:15Z
- Finished UTC: 2026-09-25T01:48:57Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002960` for JCM Medium J612 / `mediadive.medium:J612`, generated from `data/normalized_yaml/bacterial/reinforced_clostridial_medium.yaml`.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

MediaDive J612 and the JCM GRMD 612 page both identify this target as `REINFORCED CLOSTRIDIAL MEDIUM`. An exact ignored-inclusive search for `mediadive.medium:J612` found the source ID in one normalized owner, this generated target, source indexes, and the manifest row.

## Evidence

The JCM page lists 38.0 g Reinforced clostridial medium (BD-Difco), 15.0 g agar, and 1.0 L distilled water. MediaDive J612 carries the same three rows as its only solution. JCM also states that media should be autoclaved at 121 C for 15 min unless otherwise stated.

## Completeness

The underlying JCM recipe is complete and intentionally simple. The maintained normalized owner has already been repaired to include the BD-Difco qualifier, distilled water, a source note per ingredient, a JCM preparation step, autoclave sterilization, and the JCM reference. The generated target still reflects the pre-repair two-ingredient form.

## Findings

- The generated target is stale relative to `data/normalized_yaml/bacterial/reinforced_clostridial_medium.yaml`: it lacks the curated `Reinforced clostridial medium (BD-Difco)` label, the 1000 ml/L distilled water row, source notes, preparation steps, sterilization, `data_quality_flags`, and the direct JCM reference added by `repair_official_simple_score20.py`.
- Both the current normalized owner and generated target carry `kg_microbe_match: mediadive.medium:12`, but MediaDive medium 12 is DSMZ `SOIL EXTRACT MEDIUM`, not JCM Medium J612. This is a false KG-Microbe match that should be removed or replaced before regeneration.

## Recommended Edits

- Remove or correct `kg_microbe_match: mediadive.medium:12` in `data/normalized_yaml/bacterial/reinforced_clostridial_medium.yaml`.
- Regenerate `data/merge_yaml/merged` so the generated JCM J612 target inherits the September JCM repair.

## Follow-up Checks

- Confirm the regenerated target contains exactly the three JCM recipe components: 38.0 g/L Reinforced clostridial medium (BD-Difco), 15.0 g/L agar, and 1000 ml/L distilled water.
- Confirm the stale generated two-ingredient record is gone and no record for JCM 612 still points at `mediadive.medium:12`.
- Re-run open schema, strict, reference, and term validation for the regenerated target.

## Additional Notes

This is not a hand-editing issue in `data/merge_yaml/merged`; the retained false KG-Microbe match must be corrected in normalized YAML before the target is regenerated.

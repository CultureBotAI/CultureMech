# YAML Record Review: reinforced_clostridial_medium_rcm

- Repository: CultureMech
- Record: `data/merge_yaml/merged/reinforced_clostridial_medium_rcm.yaml`
- Started UTC: 2026-09-25T01:52:00Z
- Finished UTC: 2026-09-25T01:53:02Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:009353` for TOGO Medium M2805 / `TOGO:M2805`, generated from `data/normalized_yaml/bacterial/reinforced_clostridial_medium_rcm.yaml`.

## Validation

- Open schema validation: passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

Exact ignored-inclusive searches for `TOGO:M2805` within the owner, generated target, and manifest found only `data/normalized_yaml/bacterial/reinforced_clostridial_medium_rcm.yaml`, this generated target, and the manifest row. TOGO M2805 has no external `src_url`; its comment cites routine 37 C cultivation in reinforced clostridial medium with all media supplied by Oxoid.

## Evidence

The TOGO M2805 API payload lists one component, `Reinforced clostridial medium (Oxoid)`, with volume `1` and unit `L`. The current normalized owner converts that to 1000 `ML_PER_L`, preserves the commercial Oxoid RCM as an opaque component, adds the 37 C culture temperature, and adds the TOGO reference.

## Completeness

The generated target contains the right TOGO ID and Oxoid RCM component label, but it still carries the obsolete import that recorded 1 L of commercial RCM as 1 g/L.

## Findings

- The generated target records `Reinforced clostridial medium (Oxoid)` as `1 G_PER_L`. TOGO M2805 states `1 L`, not 1 g; the maintained owner has already repaired this to 1000 `ML_PER_L`.
- The generated target is stale relative to `data/normalized_yaml/bacterial/reinforced_clostridial_medium_rcm.yaml`: it lacks the source note, the 37 C `temperature_value`, `data_quality_flags`, and the TOGO reference added by `repair_togo_products_more_score40.py`.

## Recommended Edits

- Regenerate `data/merge_yaml/merged` from the repaired normalized owner so TOGO M2805 emits the 1000 ml/L Oxoid RCM amount and retained temperature/reference metadata.
- Keep the Oxoid RCM component opaque unless a source that discloses the exact Oxoid product formula is added later.

## Follow-up Checks

- Confirm the regenerated target contains `Reinforced clostridial medium (Oxoid)` at 1000 `ML_PER_L`, not 1 `G_PER_L`.
- Confirm the regenerated target includes `temperature_value: 37.0` and the TOGO M2805 reference.
- Re-run open schema, strict, reference, and term validation for the regenerated target.

## Additional Notes

No additional normalized-YAML edit is needed for the inspected TOGO import; the generated output just needs to be refreshed.

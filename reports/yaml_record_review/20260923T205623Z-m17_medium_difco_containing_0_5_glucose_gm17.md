# YAML Record Review: M17 medium (Difco) containing 0.5% glucose (GM17)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/m17_medium_difco_containing_0_5_glucose_gm17.yaml`
- Started UTC: 2026-09-23T20:55:40Z
- Finished UTC: 2026-09-23T20:56:23Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/m17_medium_difco_containing_0_5_glucose_gm17.yaml`
- Maintained owner: `data/normalized_yaml/bacterial/m17_medium_difco_containing_0_5_glucose_gm17.yaml`
- CultureMech ID: `CultureMech:009417`
- Media term: `TOGO:M2882`
- Merge fingerprint: `7a06030d84740119984589c42182a6810bbe5c9d559541a19b9629e4ac3e7126`
- Merge sources: `m17_medium_difco_containing_0_5_glucose_gm17`
- Ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found the maintained TOGO owner, generated indexes, the generated one-source merge, unrelated `kg_microbe_match: mediadive.medium:21` uses, and historical validation rows.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows in `/private/tmp/m17_medium_difco_containing_0_5_glucose_gm17.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history` entries were not checked as standalone history records.

## Identity and Grounding

The record identifies TOGO `M2882`, `M17 medium (Difco) containing 0.5% glucose (GM17)`. The TOGO API payload has no upstream `src_url`; it contains a source text comment that cells were grown at 30 C in Difco M17 medium containing 0.5% glucose without agitation or in the same medium with 1.5% agar for 18 h. The structured liquid-medium components are `Glucose` at `0.5 %` plus `M17 broth (Difco)` at `1 L`.

The maintained owner was repaired after this generated YAML was emitted. The maintained file now stores M17 broth as `1000 ML_PER_L`, captures the 30 C static 18 h cultivation context, adds two preparation steps, sets curation flags, and has a structured TOGO reference; the generated record still stores `M17 broth (Difco)` as `1 G_PER_L` and has none of those later corrections.

## Evidence

- TOGO API record `M2882` confirms the 0.5% glucose and 1 L Difco M17 broth wrapper.
- `data/normalized_yaml/bacterial/m17_medium_difco_containing_0_5_glucose_gm17.yaml` has a `2026-09-10` `RESOLVED_TOGO_M17_BHI_SCORE20` curation event that is absent from the generated YAML.
- MediaDive REST for medium 21 resolves to `SARCINA MEDIUM`, pH 6.0, with glucose, peptone, yeast extract, and water; it is not Difco M17 broth or GM17.

## Completeness

The generated record is incomplete because it is stale relative to its maintained owner and because it misrepresents 1 L of M17 broth as `1 G_PER_L`. The maintained owner is closer to the TOGO source but still retains a false `kg_microbe_match` to DSMZ Sarcina medium.

## Findings

1. The generated YAML is stale relative to the maintained source record. It was last merged on `2026-08-06`, but the maintained owner has a `2026-09-10` repair that corrected `M17 broth (Difco)` to `1000 ML_PER_L`, added structured preparation steps, restored 30 C static 18 h cultivation context, and added a structured TOGO reference. None of those repairs appear in `data/merge_yaml/merged/m17_medium_difco_containing_0_5_glucose_gm17.yaml`.

2. `M17 broth (Difco)` is quantitatively wrong in the generated record. TOGO lists 1 L of the broth base, but the generated YAML records `1 G_PER_L`, turning a broth base volume into a gram-scale ingredient.

3. The `kg_microbe_match` is false. The generated and maintained records both carry `mediadive.medium:21`, but MediaDive medium 21 is DSMZ `SARCINA MEDIUM`, a pH 6.0 glucose/peptone/yeast extract recipe. It is not M17 or GM17.

4. The source is a growth-condition sentence, not a complete Difco M17 formulation. TOGO discloses glucose at final 0.5% and M17 broth at 1 L, but not the internal M17 broth recipe. The opaque complex base should not be grounded to DSMZ 21.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/m17_medium_difco_containing_0_5_glucose_gm17.yaml` from the repaired maintained owner so `M17 broth (Difco)` remains `1000 ML_PER_L`, the preparation steps are present, and the TOGO reference is retained.
- Remove `kg_microbe_match: mediadive.medium:21` unless a source can prove DSMZ Sarcina medium is the intended GM17 base.
- Preserve the TOGO semantics: 1 L Difco M17 broth plus glucose at 0.5% final concentration, cultivated without agitation at 30 C for 18 h.
- Keep the `M17 broth (Difco)` component unmapped unless a source-backed Difco M17 broth formulation is curated separately and linked as a stock or base medium.
- Rerun open schema, strict, reference, and term validation after regeneration.

## Follow-up Checks

- Search ignored files exactly for `kg_microbe_match: mediadive.medium:21` and audit the other score-20 matches to DSMZ Sarcina medium.
- Check whether GM17 should become a variant of an unresolved Difco M17 broth base record after the false MediaDive match is removed.

## Additional Notes

None found.

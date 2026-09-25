# YAML Record Review: M17 broth (containing glucose)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/m17_broth_containing_glucose.yaml`
- Started UTC: 2026-09-23T20:53:30Z
- Finished UTC: 2026-09-23T20:54:23Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/m17_broth_containing_glucose.yaml`
- Maintained owner: `data/normalized_yaml/bacterial/m17_broth_containing_glucose.yaml`
- CultureMech ID: `CultureMech:009066`
- Media term: `TOGO:M2492`
- Merge fingerprint: `27febafa35cbb3bf42148121ff2d191d417340175d01ffc32418ab32b2c60cea`
- Merge sources: `m17_broth_containing_glucose`
- Ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found the maintained TOGO owner, generated indexes, the generated one-source merge, historical validation rows, and several unrelated `kg_microbe_match: mediadive.medium:21` uses.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows in `/private/tmp/m17_broth_containing_glucose.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history` entries were not checked as standalone history records.

## Identity and Grounding

The record identifies TOGO `M2492`, `M17 broth (containing glucose)`. The TOGO API payload has no upstream `src_url`; it contains a source text comment that strains were grown overnight at 37 C on M17 broth containing glucose or lactose at a final concentration of 1% in an anaerobic atmosphere, and the structured components are `glucose` at `1 %` plus `M17 broth` at `1 L`.

The maintained owner was repaired after this generated YAML was emitted. The maintained file now stores M17 broth as `1000 ML_PER_L`, captures the 37 C anaerobic context, adds two preparation steps, sets curation flags, and has a structured TOGO reference; the generated record still stores `M17 broth` as `1 G_PER_L` and has none of those later corrections.

## Evidence

- TOGO API record `M2492` confirms the 1% glucose and 1 L M17 broth wrapper.
- `data/normalized_yaml/bacterial/m17_broth_containing_glucose.yaml` has a `2026-09-10` `RESOLVED_TOGO_M17_BHI_SCORE20` curation event that is absent from the generated YAML.
- MediaDive REST for medium 21 resolves to `SARCINA MEDIUM`, pH 6.0, with glucose, peptone, yeast extract, and water; it is not M17 broth.

## Completeness

The generated record is incomplete because it is stale relative to its maintained owner and because it misrepresents 1 L of M17 broth as `1 G_PER_L`. The maintained owner is closer to the TOGO source but still retains a false `kg_microbe_match` to DSMZ Sarcina medium.

## Findings

1. The generated YAML is stale relative to the maintained source record. It was last merged on `2026-08-06`, but the maintained owner has a `2026-09-10` repair that corrected `M17 broth` to `1000 ML_PER_L`, added structured preparation steps, restored 37 C anaerobic cultivation context, and added a structured TOGO reference. None of those repairs appear in `data/merge_yaml/merged/m17_broth_containing_glucose.yaml`.

2. `M17 broth` is quantitatively wrong in the generated record. TOGO lists 1 L of M17 broth, but the generated YAML records `1 G_PER_L`, turning a broth base volume into a gram-scale ingredient.

3. The `kg_microbe_match` is false. The generated and maintained records both carry `mediadive.medium:21`, but MediaDive medium 21 is DSMZ `SARCINA MEDIUM`, with glucose, peptone, yeast extract, distilled water, and pH 6.0. It is not a M17 broth record and should not be used to ground TOGO `M2492`.

4. The source is a growth-condition sentence, not a complete M17 base formulation. TOGO discloses glucose at final 1% and M17 broth at 1 L, but not the internal M17 broth recipe. If the recipe keeps M17 broth as an opaque complex base, it should clearly mark that the base formulation is unresolved instead of mapping it to DSMZ 21.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/m17_broth_containing_glucose.yaml` from the repaired maintained owner so `M17 broth` remains `1000 ML_PER_L`, the preparation steps are present, and the TOGO reference is retained.
- Remove `kg_microbe_match: mediadive.medium:21` unless a source can prove DSMZ Sarcina medium is the intended M17 broth base.
- Preserve the TOGO semantics: 1 L M17 broth plus glucose at 1% final concentration, cultivated anaerobically at 37 C.
- Keep the `M17 broth` component unmapped unless a source-backed M17 broth formulation is curated separately and linked as a stock or base medium.
- Rerun open schema, strict, reference, and term validation after regeneration.

## Follow-up Checks

- Search ignored files exactly for `kg_microbe_match: mediadive.medium:21` and audit the other score-20 matches to DSMZ Sarcina medium.
- Re-run an ignored-inclusive exact search for `TOGO:M2492` after regeneration to verify this TOGO wrapper still has a single maintained owner.

## Additional Notes

The maintained owner already fixes the most severe generated-record error. The next curation pass can likely remove the false KG-Microbe match and regenerate rather than recurate the glucose wrapper from scratch.

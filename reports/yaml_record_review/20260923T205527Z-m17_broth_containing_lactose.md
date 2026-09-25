# YAML Record Review: M17 broth (containing lactose)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/m17_broth_containing_lactose.yaml`
- Started UTC: 2026-09-23T20:54:35Z
- Finished UTC: 2026-09-23T20:55:27Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/m17_broth_containing_lactose.yaml`
- Maintained owner: `data/normalized_yaml/bacterial/m17_broth_containing_lactose.yaml`
- CultureMech ID: `CultureMech:009067`
- Media term: `TOGO:M2493`
- Merge fingerprint: `9b50c9e2ba2500aaf56d366b9f759f421a65304a9c07ce8a983ebb7e3bb5ffd7`
- Merge sources: `m17_broth_containing_lactose`
- Ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found the maintained TOGO owner, generated indexes, the generated one-source merge, the JCM `J697` GAM broth record, the generated GAM broth record, and historical validation rows.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows in `/private/tmp/m17_broth_containing_lactose.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history` entries were not checked as standalone history records.

## Identity and Grounding

The record identifies TOGO `M2493`, `M17 broth (containing lactose)`. The TOGO API payload has no upstream `src_url`; it contains a source text comment that strains were grown overnight at 37 C on M17 broth containing glucose or lactose at a final concentration of 1% in an anaerobic atmosphere, and the structured components are `lactose` at `1 %` plus `M17 broth` at `1 L`.

The maintained owner was repaired after this generated YAML was emitted. The maintained file now stores M17 broth as `1000 ML_PER_L`, captures the 37 C anaerobic context, adds two preparation steps, sets curation flags, and has a structured TOGO reference; the generated record still stores `M17 broth` as `1 G_PER_L` and has none of those later corrections.

## Evidence

- TOGO API record `M2493` confirms the 1% lactose and 1 L M17 broth wrapper.
- `data/normalized_yaml/bacterial/m17_broth_containing_lactose.yaml` has a `2026-09-10` `RESOLVED_TOGO_M17_BHI_SCORE20` curation event that is absent from the generated YAML.
- MediaDive REST for `J697` resolves to `GAM BROTH WITH 1% LACTOSE`, made from 59 g/L GAM broth and 10 g/L lactose; it is not M17 broth.

## Completeness

The generated record is incomplete because it is stale relative to its maintained owner and because it misrepresents 1 L of M17 broth as `1 G_PER_L`. The maintained owner is closer to the TOGO source but still retains a false `kg_microbe_match` to JCM GAM broth with lactose.

## Findings

1. The generated YAML is stale relative to the maintained source record. It was last merged on `2026-08-06`, but the maintained owner has a `2026-09-10` repair that corrected `M17 broth` to `1000 ML_PER_L`, added structured preparation steps, restored 37 C anaerobic cultivation context, and added a structured TOGO reference. None of those repairs appear in `data/merge_yaml/merged/m17_broth_containing_lactose.yaml`.

2. `M17 broth` is quantitatively wrong in the generated record. TOGO lists 1 L of M17 broth, but the generated YAML records `1 G_PER_L`, turning a broth base volume into a gram-scale ingredient.

3. The `kg_microbe_match` is false. The generated and maintained records both carry `mediadive.medium:J697`, but J697 is `GAM BROTH WITH 1% LACTOSE`, a 59 g/L GAM broth recipe from JCM. Shared 1% lactose is not enough to ground an M17 broth wrapper to a GAM broth formula.

4. The source is a growth-condition sentence, not a complete M17 base formulation. TOGO discloses lactose at final 1% and M17 broth at 1 L, but not the internal M17 broth recipe. If the recipe keeps M17 broth as an opaque complex base, it should mark that the base formulation is unresolved instead of mapping it to JCM J697.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/m17_broth_containing_lactose.yaml` from the repaired maintained owner so `M17 broth` remains `1000 ML_PER_L`, the preparation steps are present, and the TOGO reference is retained.
- Remove `kg_microbe_match: mediadive.medium:J697` unless a source can prove JCM GAM broth with lactose is the intended M17 broth base.
- Preserve the TOGO semantics: 1 L M17 broth plus lactose at 1% final concentration, cultivated anaerobically at 37 C.
- Keep the `M17 broth` component unmapped unless a source-backed M17 broth formulation is curated separately and linked as a stock or base medium.
- Rerun open schema, strict, reference, and term validation after regeneration.

## Follow-up Checks

- Re-run an ignored-inclusive exact search for `TOGO:M2493`, `mediadive.medium:J697`, and `M17 broth` after regeneration to verify that the M17 and GAM lactose records are no longer conflated.
- Check whether the glucose and lactose M17 wrappers should become variants of the same unresolved M17 broth base record.

## Additional Notes

The generated GAM broth `J697` record should be reviewed independently under its own file; this M17 wrapper should only remove the false cross-link to it.

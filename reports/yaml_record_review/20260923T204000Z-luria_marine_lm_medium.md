# YAML Record Review: Luria Marine (LM) Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/luria_marine_lm_medium.yaml`
- Started UTC: `2026-09-23T20:38:42Z`
- Finished UTC: `2026-09-23T20:40:00Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:009483`
- `name`: `luria_marine_lm_medium`
- `original_name`: `Luria Marine (LM) medium`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `TOGO:M2959`
- `merge_fingerprint`: `33735f42ed1dda12bcf89b7f55ee81e6edc4cb41d63f8c337552f41bd59e9aaa`
- `merged_from`: `TOGO_M2897_LB_medium`, `luria_bertani_lb_medium`, `luria_marine_lm_medium`, `polymorhobacter_medium`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/luria_marine_lm_medium.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:009483`, `TOGO:M2959`, `TOGO:M2897`, `TOGO:M3236`, `mediadive.medium:1620`, `luria_marine_lm_medium`, `polymorhobacter_medium`, and the merge fingerprint found the maintained M2959 owner, the generated M2959 record, and the normalized records collapsed into this generated merge.
- TOGO M2959 identifies the reviewed target as `Luria Marine (LM) medium` with pH 7.8.
- MediaDive 1620 resolves the merged `polymorhobacter_medium` sibling as DSMZ `POLYMORHOBACTER MEDIUM`, with a distinct 2.5 g/L tryptone, 1.3 g/L yeast extract, and 5 g/L NaCl recipe.
- The maintained `luria_bertani_lb_medium` owner is explicitly a `SALINITY_VARIANT` of `TOGO_M2897_LB_medium`, not a source duplicate.

## Evidence

- TOGO M2959 lists 1 L distilled water, 5 g/L yeast extract, 20 g/L NaCl, and 10 g/L tryptone.
- The generated M2959 record stores 1 `G_PER_L` distilled water, 5 g/L yeast extract, 0.5 g/L NaCl, and 10 g/L tryptone.
- TOGO M2897, one of the merged siblings, carries the 0.5 g/L NaCl value that appears in the generated M2959 target.
- TOGO M3236 uses 10 g/L NaCl, and DSMZ 1620 uses 2.5 g/L tryptone, 1.3 g/L yeast extract, 5 g/L NaCl, and tap water.
- TOGO M2959 source comments name the medium `Luria Marine (LM)` and specify pH 7.8 for `V. campbellii`.

## Completeness

- The generated M2959 record has the right yeast-extract and tryptone amounts.
- The generated M2959 record has the wrong NaCl amount.
- The generated M2959 record omits pH 7.8.
- The generated M2959 record has no structured source references.
- The generated M2959 record turns the 1 L water row into a mass concentration.

## Findings

1. A false duplicate merge replaced the Luria Marine salinity.
   - Evidence: the reviewed target is TOGO M2959, whose source and maintained owner use 20 g/L NaCl, but the generated record stores 0.5 g/L NaCl from TOGO M2897 and names M2897, M3236, and DSMZ 1620 as merge sources.
   - Impact: users asking for Luria Marine receive a low-salt LB formulation instead of the marine 20 g/L NaCl formulation.

2. DSMZ Polymorhobacter medium was merged into an unrelated LB family.
   - Evidence: MediaDive 1620 uses 2.5 g/L tryptone, 1.3 g/L yeast extract, 5 g/L NaCl, and tap water; none of those three nutrient/salt amounts match TOGO M2959.
   - Impact: `polymorhobacter_medium` becomes a synonym for Luria Marine even though its composition differs materially.

3. The pH 7.8 specification was dropped.
   - Evidence: TOGO M2959 provides `ph: "7.8"` and repeats pH 7.8 in the source comment, while the generated record has no `ph_value`.
   - Impact: the generated Luria Marine recipe loses a source-level final pH.

4. The source solvent row has the wrong dimension.
   - Evidence: TOGO lists distilled water as 1 L, while the generated record stores it as 1 `G_PER_L`.
   - Impact: final volume is represented as a mass concentration.

## Recommended Edits

1. Keep TOGO M2959 separate from TOGO M2897, TOGO M3236, and DSMZ 1620, with relationships no stronger than salinity or formula variants.
2. Rebuild Luria Marine with 20 g/L NaCl and pH 7.8.
3. Restore DSMZ 1620 as its own Polymorhobacter medium with the 2.5/1.3/5 g/L source signature.
4. Represent the 1 L distilled-water source row as final volume, not 1 `G_PER_L`.
5. Add structured references for TOGO M2959, TOGO M2897, TOGO M3236, and DSMZ 1620 to their respective records.

## Follow-up Checks

- Re-fetch TOGO M2959 and MediaDive 1620, then confirm the regenerated records retain distinct tryptone, yeast-extract, NaCl, pH, and water-source values.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt Luria Marine record.
- Run an ignored-inclusive exact search for `luria_marine_lm_medium`, `TOGO:M2959`, and `mediadive.medium:1620` to confirm the false synonym has been removed.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.

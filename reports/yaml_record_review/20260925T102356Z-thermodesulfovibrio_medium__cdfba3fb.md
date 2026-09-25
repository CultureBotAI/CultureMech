# YAML Record Review: thermodesulfovibrio_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfovibrio_medium__cdfba3fb.yaml
- Started UTC: 2026-09-25T10:20:00Z
- Finished UTC: 2026-09-25T10:23:56Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermodesulfovibrio_medium__cdfba3fb`, which represents direct MediaDive/JCM medium `J479` as `CultureMech:002828`.

## Validation

- Schema: Passed with `No issues found`.
- Strict validation: Passed; the strict TSV had only its header row and no error rows.
- Reference validation: Passed with 0 checks reported.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

The generated target is stale relative to `data/normalized_yaml/bacterial/thermodesulfovibrio_medium.yaml`. The normalized record has a 2026-09-10 `RESOLVED_JCM_479_SCORE20_GRAPH` repair grounded to live JCM 479 and JCM 284 pages, but the generated target still only contains the old MediaDive J479 Solution B and Solution C solutes. An exact ignored-inclusive search for `mediadive.medium:J479` and `GRMD=479` also found `TOGO_M480_Thermodesulfovibrio_Medium`, which remains separately generated as `THERMODESULFOVIBRIO_MEDIUM.yaml`.

## Evidence

JCM 479 says to use Solution A of JCM Medium 284 without yeast extract, add 0.05 volume each of Solution B and Solution C, and add 0.01 volume each of 3% L-cysteine hydrochloride hydrate and 3% sodium sulfide nonahydrate before inoculation. The repaired normalized record carries JCM 284 Solution A salts, 2 ml/L Trace vitamins, 1 ml/L Trace element solution, 1 ml/L Se/W solution, 50 ml/L Solution B, 50 ml/L Solution C, and the two 10 ml/L reductant stocks.

## Completeness

The generated target lacks Solution A entirely and has no trace vitamins, trace elements, Se/W solution, cysteine stock, sulfide stock, bicarbonate, resazurin, basal salts, water, or repaired JCM 284 reference.

## Findings

- High: the generated record is stale relative to the repaired normalized JCM 479 graph. It lacks the 2026-09-10 repair, the added JCM 284 reference, and every repaired ingredient or solution from JCM 284 Solution A.
- High: Solution B and Solution C were kept as their 50 ml stock strengths rather than modeled as 0.05-volume additions. The target lists 44 g/L sodium lactate and 56 g/L `Na2SO4`, while JCM 479 adds 0.05 volume of each 50 ml stock to culture vessels containing Solution A.
- Medium: the TOGO M480 import of the same JCM 479 source is unmerged with this direct MediaDive/JCM branch.

## Recommended Edits

- Regenerate merged YAML from the repaired `data/normalized_yaml/bacterial/thermodesulfovibrio_medium.yaml` so the 2026-09-10 JCM 479 graph repair reaches `data/merge_yaml/merged/thermodesulfovibrio_medium__cdfba3fb.yaml`.
- Verify the merge path does not prefer the stale two-solute MediaDive import over the repaired normalized record for the same source.
- Canonicalize TOGO M480 and direct MediaDive/JCM J479 before merge generation.

## Follow-up Checks

- Regenerate merged YAML and verify J479 contains JCM 284 Solution A salts, Trace vitamins, Trace element solution, Se/W solution, Solution B, Solution C, and both 3% reductant stocks.
- Confirm the regenerated J479 record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `mediadive.medium:J479` and `GRMD=479` to ensure JCM 479 has one generated target.

## Additional Notes

None found.

# YAML Record Review: PYGV MARINE MEDIUM (A)

- Repository: CultureMech
- Record: data/merge_yaml/merged/pygv_marine_medium_a__405d6e69.yaml
- Started UTC: 2026-09-24T23:10:37Z
- Finished UTC: 2026-09-24T23:11:05Z
- Verdict: needs curation

## Target

- Generated file: data/merge_yaml/merged/pygv_marine_medium_a__405d6e69.yaml
- Stable ID: CultureMech:015399
- Maintained owner: data/normalized_yaml/specialized/pygv_marine_medium_a.yaml
- Merge sources: pygv_marine_medium_a
- Merge fingerprint: 405d6e697516b6467fcbfd50bc0c89f0979c6648c71d19c03399eb2da41e7b9b
- Source grounding: JCM Medium 304 / MediaDive J304 PYGV MARINE MEDIUM (A)

## Validation

| Check | Result |
| --- | --- |
| LinkML open schema | Passed with `No issues found`. |
| Strict schema | Passed with 0 errors. `/private/tmp/pygv_marine_medium_a__405d6e69.strict.tsv` contains only the header line. |
| Reference validation | Passed 1 file with 0 reference checks. |
| Term validation | Passed after the known `eutils` / `pkg_resources` warning. |
| Embedded history validation | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record is correctly identified as JCM Medium 304 / MediaDive J304, PYGV MARINE MEDIUM (A), but it does not model the source structure. JCM 304 has a main medium with 20 ml Mineral salt solution, 10 ml 2.5% Glucose solution, 10 ml Vitamin solution, 15 g Agar, and 960 ml Artificial seawater, plus nested Mineral salt solution, Vitamin solution, Artificial seawater, and Metals 44 stock recipes.

The direct MediaDive import flattened every nested stock into top-level `ingredients`. MediaDive J304 expands Metals 44, so the direct branch flattened Metals 44 internals as well. This makes source-level stock concentrations look like final-medium concentrations and merges duplicate chemicals across unrelated stocks, such as CaCl2 x 2 H2O from Mineral salt solution plus Artificial seawater and FeSO4 x 7 H2O from Mineral salt solution plus Metals 44.

An exact ignored-file search for `mediadive.medium:J304`, `GRMD=304`, `TOGO:M299`, and `pygv_marine_medium_a` under the direct specialized owner, the TOGO bacterial owner, the exact generated records, and `data/normalized_yaml/specialized_index.json` found this direct JCM J304 branch and the parallel TOGO M299 branch.

## Evidence

- MediaDive J304 and JCM Medium 304 list 20 ml/L Mineral salt solution, 10 ml/L 2.5% Glucose solution, 10 ml/L Vitamin solution, and 960 ml/L Artificial seawater in the main recipe.
- MediaDive J304 exposes Mineral salt solution, Vitamin solution, Artificial seawater, and Metals 44 as separate nested solutions.
- `data/merge_yaml/merged/pygv_marine_medium_a__405d6e69.yaml` has no `solutions` section.
- The generated top-level ingredient list includes mineral-stock ingredients, vitamin-stock ingredients, artificial-seawater ingredients, and Metals 44 ingredients.
- The generated top-level list has `CaCl2 x 2 H2O: 4.442 G_PER_L`, which is the sum of 3.34 g/L CaCl2 from the Mineral salt solution and 1.102 g/L CaCl2 from Artificial seawater.
- The generated top-level list has `FeSO4 x 7 H2O: 0.599 G_PER_L`, which is the sum of 0.099 g/L FeSO4 from the Mineral salt solution and 0.5 g/L FeSO4 from Metals 44.
- The owner has pH 7.2, but the exact JCM page says to adjust the final medium to pH 7.5 with sterile KOH if necessary; pH 7.2 belongs to the Mineral salt solution readjustment.

## Completeness

The record preserves the JCM J304 identity and two source preparation strings. It is incomplete as a recipe because all solution boundaries, all source aliquot volumes, all stock-local water rows, and the 2.5% glucose stock are absent. It is also separated from the equivalent TOGO M299 branch until both owners are repaired to the same nested formulation.

## Findings

- Major: the direct MediaDive import flattened Mineral salt solution, Vitamin solution, Artificial seawater, and Metals 44 into final top-level ingredients.
- Major: duplicate ingredient merging summed the same chemical across unrelated stocks, producing CaCl2 x 2 H2O 4.442 g/L and FeSO4 x 7 H2O 0.599 g/L values that do not occur in any JCM 304 solution.
- Major: 10 ml of 2.5% Glucose solution was represented as a top-level 10 g/L Glucose ingredient instead of a 10 ml/L solution aliquot with 2.5% w/v glucose composition.
- Major: the record uses final pH 7.2, but the source final medium pH is 7.5.
- Minor: the equivalent TOGO M299 source branch remains separate and broken in a slightly different way.

## Recommended Edits

1. Re-resolve `data/normalized_yaml/specialized/pygv_marine_medium_a.yaml` from MediaDive J304 and the exact JCM Medium 304 page.
2. Restore top-level ingredients to Bacto peptone, Yeast extract, Agar, 20 ml/L Mineral salt solution, 10 ml/L 2.5% Glucose solution, 10 ml/L Vitamin solution, 960 ml/L Artificial seawater, and variable KOH for final pH adjustment.
3. Move the mineral salts, vitamin ingredients, artificial seawater salts, and Metals 44 ingredients into the four nested source stocks.
4. Prevent duplicate merging from summing chemicals that live in separate stock solutions.
5. Store final pH 7.5 and keep pH 6.5 / 7.2 only as Mineral salt solution preparation context.
6. Regenerate and verify whether the direct JCM J304 branch merges with the repaired TOGO M299 branch.

## Follow-up Checks

- Re-run open, strict, reference, and term validators on regenerated `pygv_marine_medium_a__405d6e69`.
- Compare the regenerated direct branch against MediaDive J304 and the exact JCM Medium 304 page.
- Repeat the exact ignored-file search for `mediadive.medium:J304`, `GRMD=304`, `TOGO:M299`, and `pygv_marine_medium_a` to confirm duplicate J304 branches are reconciled or intentionally separated.
- Confirm all hydrated salts keep hydrated CHEBI terms inside nested stock solutions.

## Additional Notes

None.

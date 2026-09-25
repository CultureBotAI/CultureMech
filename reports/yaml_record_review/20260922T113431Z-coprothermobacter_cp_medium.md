# YAML Record Review: COPROTHERMOBACTER (CP) MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/coprothermobacter_cp_medium.yaml`
- Started UTC: 2026-09-22T11:32:30Z
- Finished UTC: 2026-09-22T11:34:31Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:001817`
- Normalized source: `data/normalized_yaml/bacterial/coprothermobacter_cp_medium.yaml`
- Canonical KOMODO parent: `data/normalized_yaml/bacterial/cp_medium.yaml`
- Source identity: DSMZ Medium 678, `COPROTHERMOBACTER (CP) MEDIUM`
- Current generated merge: DSMZ 678, KOMODO 678, and KOMODO 678.1

## Validation

- Open schema validation: pass.
- Strict validation: pass.
- Reference validation: pass with 0 checks.
- Term validation: pass.
- Embedded `curation_history`: not checked by the standalone history validator.

## Identity and Grounding

- DSMZ Medium 678 adds 10 ml Modified Wolin's mineral solution to the final medium.
- The DSMZ PDF lists the Modified Wolin's mineral solution stock recipe below the final recipe.
- DSMZ states that DSM 9219 uses 5 g/l D-glucose as a substrate replacing gelatine.
- The normalized KOMODO parent changed `for_dsm_9219.yaml` from `SOURCE_DUPLICATE` to `STRAIN_SPECIFIC_VARIANT` on September 13, 2026, but this generated record still merges `for_dsm_9219` into the canonical recipe.

## Evidence

- DSMZ source checked: `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium678.pdf`.
- Local DSMZ owner checked: `data/normalized_yaml/bacterial/coprothermobacter_cp_medium.yaml`.
- Local KOMODO parent checked: `data/normalized_yaml/bacterial/cp_medium.yaml`.
- Local DSM 9219 child checked: `data/normalized_yaml/bacterial/for_dsm_9219.yaml`.

## Completeness

- The bacterial category, liquid state, pH 7.0, main CP medium ingredients, and anaerobic preparation text are appropriate.
- Sodium resazurin at `0.0005 G_PER_L` is consistent with adding 0.50 ml of a 0.1% w/v stock to one liter.
- Modified Wolin's mineral solution is not represented as a final-medium stock addition.

## Findings

1. The generated record omits `Modified Wolin's mineral solution` at `10 ML_PER_L`.
2. Modified Wolin's mineral constituents are flattened into final-medium `ingredients` at stock strength instead of being nested under a `solutions` entry.
3. Calcium chloride is overmerged: the final recipe's 0.40 g/l `CaCl2 x 2 H2O` and the mineral stock's 0.10 g/l `CaCl2 x 2 H2O` became one `0.5 G_PER_L` final-medium ingredient.
4. The DSM 9219 strain-specific replacement of gelatine with 5 g/l D-glucose is lost because the generated record still merges `for_dsm_9219` as a source duplicate.

## Recommended Edits

1. In both `coprothermobacter_cp_medium.yaml` and `cp_medium.yaml`, keep Modified Wolin's mineral solution as a 10 ml/l final ingredient and move its formula under `solutions`.
2. Restore the final-recipe calcium chloride concentration to the DSMZ-supported `0.4 G_PER_L`.
3. Preserve `for_dsm_9219.yaml` as a `STRAIN_SPECIFIC_VARIANT` of KOMODO 678 when regenerating merged output.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalizing the stock solution and regenerating.
- Confirm the regenerated canonical record no longer includes `for_dsm_9219` in `merged_from`.
- Confirm no Modified Wolin stock-only ingredient remains as a final-medium ingredient.

## Additional Notes

- No LinkML structural defect was found.
- The generated source graph is stale relative to the September 2026 KOMODO 678.1 relationship repair.

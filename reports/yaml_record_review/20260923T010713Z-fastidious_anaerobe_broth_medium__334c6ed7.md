# YAML Record Review: FASTIDIOUS ANAEROBE BROTH MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/fastidious_anaerobe_broth_medium__334c6ed7.yaml
- Started UTC: 2026-09-23T01:07:13Z
- Finished UTC: 2026-09-23T01:07:13Z
- Verdict: needs curation

## Target

`data/merge_yaml/merged/fastidious_anaerobe_broth_medium__334c6ed7.yaml` is the generated JCM/MediaDive J1045 FASTIDIOUS ANAEROBE BROTH MEDIUM record. The maintained owner is `data/normalized_yaml/bacterial/fastidious_anaerobe_broth_medium.yaml`.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/fastidious_anaerobe_broth_medium_334c6ed7.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `mediadive.medium:J1045` media term and JCM GRMD 1045 link identify the intended FASTIDIOUS ANAEROBE BROTH MEDIUM source. The pH 7.1 midpoint is consistent with the terminal JCM instruction to readjust the culture vessels to pH 7.0-7.2.

Most chemically defined components are grounded plausibly. Bacto peptone remains unmapped, which is acceptable for a commercial peptone product; soluble starch is mapped to starch but loses the source attribute; dithiothreitol is grounded to the right CHEBI term but has the wrong quantitative model.

## Evidence

JCM GRMD 1045 prints this basal recipe in 1 L distilled water: 23 g BD-Difco Bacto peptone, 5 g NaCl, 1 g soluble starch, 0.4 g NaHCO3, 1 g glucose, 1 g sodium pyruvate, 0.5 g L-cysteine HCl hydrate, 0.25 g sodium pyrophosphate, 1 g L-arginine, and 0.01 g hemin.

After mixing, adjusting to pH 7.2, autoclaving, and cooling under N2-CO2 gas, JCM adds 4 ml of filter-sterilized 250 mM dithiothreitol solution anaerobically, then distributes the medium under the same gas mixture and readjusts to pH 7.0-7.2.

MediaDive J1045 represents the main solution with a 1004 ml total volume: the 1 L basal recipe plus a 4 ml, 250 mM Dithiothreitol addition.

## Completeness

The generated record preserves the basal ingredient set and anaerobic handling steps, but it is not complete enough to reconstruct the source because the filter-sterilized dithiothreitol stock addition is stored as `4 G_PER_L`, distilled water is absent, and source attributes for BD-Difco Bacto peptone and soluble starch were dropped.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Major | The dithiothreitol post-autoclave stock addition has the wrong unit and amount. | JCM adds 4 ml of 250 mM dithiothreitol solution after autoclaving under anaerobic gas; the generated record stores Dithiothreitol as `4 G_PER_L`. | Replace the final DTT row with a 4 ml 250 mM post-autoclave stock addition and preserve the filter-sterilized anaerobic addition semantics. |
| Minor | Distilled water is omitted. | JCM includes 1.0 L distilled water in the basal table; MediaDive has a 1000 ml `Distilled water` row before the 4 ml DTT addition. | Add distilled water as the aqueous basis. |
| Minor | Source attributes were flattened away. | JCM specifies Bacto peptone as BD-Difco and starch as soluble; MediaDive carries those as attributes. The generated record has plain `Bacto peptone` and `Starch`. | Preserve the BD-Difco and soluble attributes in product/source metadata or preferred labels. |

## Recommended Edits

1. Rework `data/normalized_yaml/bacterial/fastidious_anaerobe_broth_medium.yaml` so dithiothreitol is a 4 ml addition of 250 mM stock instead of `4 G_PER_L`.
2. Add the 1 L distilled-water basis.
3. Restore the BD-Difco Bacto peptone and soluble-starch source attributes.
4. Regenerate `data/merge_yaml/merged/fastidious_anaerobe_broth_medium__334c6ed7.yaml`.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm Dithiothreitol is not represented as `4 G_PER_L`.
- Confirm distilled water is present.
- Confirm the JCM post-autoclave anaerobic DTT addition remains explicit in `preparation_steps` or stock metadata.

## Additional Notes

None found.

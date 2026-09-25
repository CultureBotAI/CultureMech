# YAML Record Review: f/2 + Si for heterotrophic growth

- Repository: CultureMech
- Record: data/merge_yaml/merged/f_2_si_for_heterotrophic_growth__66acc108.yaml
- Started UTC: 2026-09-23T01:04:00Z
- Finished UTC: 2026-09-23T01:04:15Z
- Verdict: needs curation

## Target

`data/merge_yaml/merged/f_2_si_for_heterotrophic_growth__66acc108.yaml` is the generated bacterial CCAP/MediaDive C38 f/2 + Si for heterotrophic growth record. The maintained owner is `data/normalized_yaml/bacterial/f_2_si_for_heterotrophic_growth.yaml`.

The separate `data/merge_yaml/merged/f_2_si_for_heterotrophic_growth.yaml` file is the direct algae CCAP import for the same PDF source.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/f_2_si_for_heterotrophic_growth_66acc108.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `mediadive.medium:C38` media term correctly identifies CCAP f/2 + Si for heterotrophic growth. The pH 8.0 value also matches the CCAP preparation text.

Most ingredients are grounded to plausible CHEBI terms. The first NaNO3 row still carries a deprecated `mediaingredientmech_term` link instead of the later `mediaingredientmech_chebi_term` form used by the rest of the imported rows.

## Evidence

MediaDive C38 mirrors the CCAP MR_f2Si_heterotrophic PDF and prints a 1000 ml main solution with:

- 1 ml of a 75 g/l NaNO3 stock.
- 1 ml of a 5.65 g/l NaH2PO4 x 2 H2O stock.
- 1 ml of Trace elements (chelated).
- 1 ml of Vitamin mix.
- 1 ml of a 30 g/l Na2SiO3 x 9 H2O stock.
- 1000 ml filtered natural seawater.

The CCAP PDF also instructs curators to add either 0.5 g/l yeast extract plus 5 g/l glucose, or 0.5 g/l yeast extract plus 3 g/l sodium acetate, for heterotrophic growth in the dark.

## Completeness

The generated file is not complete enough to reconstruct f/2 + Si for heterotrophic growth. It keeps the main solution names and the heterotrophic-growth instruction, but it records stock additions as top-level gram-per-liter rows, flattens nested Trace elements and Vitamin mix recipes, and omits the actual yeast extract, glucose, and sodium acetate alternatives.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Major | The nitrate, phosphate, and silicate stock additions use the wrong unit. | MediaDive C38 says to add 1 ml each of the nitrate, phosphate, and silicate stock solutions; the generated record stores NaNO3, NaH2PO4 x 2 H2O, and Na2SiO3 x 9 H2O at `1 G_PER_L`. | Model these as stock additions with their source stock strengths, or compute final use concentrations from 1 ml/l additions. |
| Major | Trace elements and Vitamin mix are flattened into final ingredients. | The main solution adds 1 ml Trace elements and 1 ml Vitamin mix; EDTA, FeCl3, trace salts, cyanocobalamin, thiamine, and biotin appear directly under `ingredients` at stock strength. | Add nested Trace elements and Vitamin mix solution recipes instead of final-medium constituent rows. |
| Major | Filtered natural seawater has the wrong unit. | MediaDive C38 adds 1000 ml filtered natural seawater; the generated file stores `Natural sea water` as `1000 G_PER_L`. | Change the seawater basis to `1000 ML_PER_L` or a preparation step that makes the recipe to 1 L with filtered seawater. |
| Major | The dark-growth supplements are only unstructured prose. | CCAP gives two explicit options for heterotrophic growth: yeast extract plus glucose, or yeast extract plus sodium acetate. The generated file retains that sentence as a `MIX` step but adds none of the three compounds as recipe ingredients. | Represent both alternatives as structured ingredients in separate variants or an explicit alternative group. |
| Minor | The duplicate CCAP import was not merged with the algae record. | This record and `data/merge_yaml/merged/f_2_si_for_heterotrophic_growth.yaml` both describe the same CCAP PDF, but they remain separate generated records because their ingredient fingerprints diverged. | After repairing both normalized owners, deduplicate or merge them so there is one generated record for the CCAP C38 formula. |

## Recommended Edits

1. Rework `data/normalized_yaml/bacterial/f_2_si_for_heterotrophic_growth.yaml` around the MediaDive C38 main solution.
2. Change NaNO3, NaH2PO4 x 2 H2O, and Na2SiO3 x 9 H2O from `1 G_PER_L` rows to stock additions.
3. Nest Trace elements and Vitamin mix under their 1 ml/l addition rows.
4. Correct filtered natural seawater from `1000 G_PER_L` to a litre basis.
5. Represent the two CCAP dark-growth options as structured variants.
6. Deduplicate against the direct algae CCAP record and regenerate.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm NaNO3, NaH2PO4 x 2 H2O, and Na2SiO3 x 9 H2O are no longer `1 G_PER_L` final ingredients.
- Confirm Trace elements and Vitamin mix constituents are nested under stock additions.
- Confirm filtered natural seawater is not represented as `G_PER_L`.
- Confirm yeast extract, glucose, and sodium acetate are represented in the heterotrophic alternatives.

## Additional Notes

None found.

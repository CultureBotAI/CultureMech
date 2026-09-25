# YAML Record Review: f/2 + Si for heterotrophic growth

- Repository: CultureMech
- Record: data/merge_yaml/merged/f_2_si_for_heterotrophic_growth.yaml
- Started UTC: 2026-09-23T01:02:25Z
- Finished UTC: 2026-09-23T01:02:43Z
- Verdict: needs curation

## Target

`data/merge_yaml/merged/f_2_si_for_heterotrophic_growth.yaml` is the generated algae CCAP `f2Si_heterotrophic` record for f/2 + Si for heterotrophic growth. The maintained owner is `data/normalized_yaml/algae/f_2_si_for_heterotrophic_growth.yaml`.

The separate `data/merge_yaml/merged/f_2_si_for_heterotrophic_growth__66acc108.yaml` file is the bacterial CCAP/MediaDive C38 import for the same formula.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/f_2_si_for_heterotrophic_growth.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The record is grounded to `CCAP:f2Si_heterotrophic` and the CCAP heterotrophic PDF URL. The generated merge is stale relative to the algae owner because it lacks the 2026-08-25 repair that removed a preparation sentence from `ingredients` and the 2026-09-13 repair that restored structured CCAP `sources`.

Most mapped stock constituents are grounded to plausible CHEBI terms. Sodium metasilicate nonahydrate, iron trichloride hexahydrate, EDTA disodium salt, the trace salts, and the vitamins all point to the intended compounds, but the generated representation flattens stock formulas instead of modeling the final medium.

## Evidence

The CCAP MR_f2Si_heterotrophic PDF prints these stock strengths and use volumes:

- NaNO3 stock: 75 g/l, add 1.0 ml per litre.
- NaH2PO4.2H2O stock: 5.65 g/l, add 1.0 ml per litre.
- Chelated trace elements stock: EDTA, FeCl3.6H2O, CuSO4.5H2O, ZnSO4.7H2O, CoCl2.6H2O, MnCl2.4H2O, and Na2MoO4.2H2O per litre, add 1.0 ml per litre.
- Vitamin mix stock: cyanocobalamin, thiamine HCl, and biotin per litre, add 1.0 ml per litre.
- Sodium metasilicate stock: 30 g Na2SiO3.9H2O per litre, add 1.0 ml per litre while stirring.
- Bring the medium to 1 litre with filtered natural seawater, adjust to pH 8.0 with 1 M NaOH or HCl, and autoclave at 15 psi for 15 minutes.
- For heterotrophic growth in the dark, add either 0.5 g/l yeast extract plus 5 g/l glucose, or 0.5 g/l yeast extract plus 3 g/l sodium acetate.

MediaDive C38 mirrors the same source as a main solution with 1 ml additions of nitrate, phosphate, trace, vitamin, and silicate stocks plus 1000 ml filtered natural seawater.

## Completeness

The generated record is not complete enough to reconstruct the CCAP heterotrophic recipe. It includes trace, vitamin, and silicate stock components at their stock concentrations, but omits nitrate stock, phosphate stock, filtered natural seawater, and both heterotrophic carbon/nitrogen supplementation options.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Major | The base nitrate and phosphate additions are missing. | The CCAP source adds 1 ml/l each of a 75 g/l NaNO3 stock and a 5.65 g/l NaH2PO4.2H2O stock; neither ingredient appears in the generated algae merge. | Add the nitrate and phosphate stock additions or compute their final concentrations before regeneration. |
| Major | Trace elements, vitamins, and silicate are represented at stock strength as if they were final-medium concentrations. | CCAP adds 1 ml/l of each stock; the generated record stores chelated trace components, vitamin components, and 30 g/l sodium metasilicate directly under `ingredients`. | Model the three stock additions and their child solution recipes, preserving source stock strengths separately from per-litre use volumes. |
| Major | The heterotrophic growth additions are omitted. | The source requires either 0.5 g/l yeast extract plus 5 g/l glucose, or 0.5 g/l yeast extract plus 3 g/l sodium acetate for dark heterotrophic growth. The generated record has none of those ingredients. | Represent the two alternative heterotrophic supplementation options or split them into explicit variants. |
| Major | The seawater basis is absent. | CCAP says to make the medium to 1 litre with filtered natural seawater; the generated record has no seawater ingredient or equivalent preparation volume. | Add filtered natural seawater as the litre basis or as a preparation step that carries its filtration attribute. |
| Minor | The generated merge predates owner repairs. | `data/normalized_yaml/algae/f_2_si_for_heterotrophic_growth.yaml` removed the bogus molar preparation row on 2026-08-25 and added structured CCAP sources on 2026-09-13, but the generated file still ends at the 2026-08-06 merge event. | Regenerate after curation so the merged artifact reflects the maintained owner. |

## Recommended Edits

1. Rework `data/normalized_yaml/algae/f_2_si_for_heterotrophic_growth.yaml` around the CCAP source's five stock additions.
2. Add missing nitrate, phosphate, and filtered-natural-seawater rows.
3. Preserve Trace elements, Vitamin mix, and Sodium metasilicate as stocks rather than final `G_PER_L` rows.
4. Add the two heterotrophic dark-growth alternatives as variants, alternatives, or separate generated records.
5. Regenerate `data/merge_yaml/merged/f_2_si_for_heterotrophic_growth.yaml`.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm NaNO3 and NaH2PO4 x 2 H2O are present.
- Confirm no trace, vitamin, or silicate stock constituent remains as a top-level final concentration.
- Confirm the recipe contains filtered natural seawater.
- Confirm both yeast extract plus glucose and yeast extract plus sodium acetate dark-growth options are represented.

## Additional Notes

None found.

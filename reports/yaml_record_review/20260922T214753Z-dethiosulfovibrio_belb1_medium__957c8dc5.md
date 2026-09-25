# YAML Record Review: dethiosulfovibrio_belb1_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dethiosulfovibrio_belb1_medium__957c8dc5.yaml`
- Started UTC: 2026-09-22T21:46:02Z
- Finished UTC: 2026-09-22T21:47:53Z
- Verdict: needs curation

## Target

`CultureMech:003230` represents MediaDive JCM Medium J882, `DETHIOSULFOVIBRIO BELB1 MEDIUM`. The generated record is a single-source merge from `data/normalized_yaml/bacterial/dethiosulfovibrio_belb1_medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

JCM J882 is represented twice: this MediaDive J882 record and a TOGO M923 record that points back to `JCM_M882`. A gitignore-independent, case-insensitive `find` over `data/` found both `dethiosulfovibrio_belb1_medium` generated records plus neighboring `Dethiosulfovibrio` media that should stay separate unless their sources match exactly.

## Evidence

- MediaDive JCM J882 defines `Main sol. J882` as a 1008 ml recipe with direct salts, 10 ml Trace minerals, sodium acetate, yeast extract, sodium thiosulfate, L-cysteine, 1 mg resazurin, 915 ml distilled water, 25 ml 8% NaHCO3, 30 ml 10% MgCl2, 20 ml 1.0 M sodium acetate, and 8 ml 5% Na2S.
- Trace minerals is a 1000 ml stock with nitrilotriacetic acid, MgSO4, MnSO4, NaCl, FeSO4, CoSO4, CaCl2, ZnSO4, CuSO4, AlK(SO4)2, H3BO3, Na2MoO4, and distilled water.
- The JCM/MediaDive preparation text separates post-cooling additions of bicarbonate, magnesium chloride, and acetate from the pre-inoculation sodium sulfide stock.
- TOGO M923 preserves the same JCM source as three component groups and five cross-referenced or milliliter solution rows, but its normalized YAML moved those solution rows into empty `Unknown solution` definitions.

## Completeness

The record is incomplete because the 10 ml Trace minerals stock and the four milliliter stock additions were flattened into top-level final ingredients. The generated YAML has no `solutions` block and omits both the 915 ml main water row and the Trace minerals water row.

## Findings

- Trace minerals stock contents were flattened at stock strength; nitrilotriacetic acid, MgSO4, MnSO4, FeSO4, CoSO4, ZnSO4, CuSO4, AlK(SO4)2, H3BO3, and Na2MoO4 all appear as direct final-medium ingredients.
- Main-medium `NaCl` was merged with the trace-minerals NaCl row into `30.7619 G_PER_L`, and main-medium `CaCl2 x 2 H2O` was merged with trace-minerals calcium into `0.1992064 G_PER_L`.
- The 20 ml 1.0 M sodium acetate addition was converted to `20 G_PER_L` and merged with the direct 0.05 g sodium acetate row, producing `20.0496032 G_PER_L`.
- The 25 ml 8% NaHCO3, 30 ml 10% MgCl2, and 8 ml 5% Na2S stock additions were converted to `25`, `30`, and `8` `G_PER_L` top-level concentrations.
- The Trace minerals pH-adjustment instruction was appended as a generic top-level preparation step instead of remaining attached to that stock.
- The MediaDive J882 and TOGO M923 source views are still split into separate generated records.

## Recommended Edits

- Rebuild J882 with a 1008 ml main recipe containing 10 ml Trace minerals, 25 ml 8% NaHCO3, 30 ml 10% MgCl2, 20 ml 1.0 M sodium acetate, and 8 ml 5% Na2S as milliliter additions.
- Move all Trace minerals rows, including water and the pH 6.5/7.0 preparation note, under a 1000 ml Trace minerals stock.
- Keep the direct NaCl, CaCl2, and sodium acetate rows separate from their same-named stock-solution rows.
- Preserve the timing difference between the post-cooling stocks and the pre-inoculation sodium sulfide stock.
- Reconcile the MediaDive J882 and TOGO M923 records as duplicate views of the same JCM formula or add a source-backed reason for leaving them separate.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no Trace minerals component remains as a top-level ingredient.
- Verify that no milliliter stock addition is represented as a grams-per-liter concentration.
- Verify that the JCM J882 and TOGO M923 source views merge or carry an intentional duplicate relationship.

## Additional Notes

The live JCM `GRMD=882` page currently returns no recipe, but both MediaDive and TOGO still preserve the formula and cite JCM 882.

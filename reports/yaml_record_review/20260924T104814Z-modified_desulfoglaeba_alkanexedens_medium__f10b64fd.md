# YAML Record Review: modified_desulfoglaeba_alkanexedens_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_desulfoglaeba_alkanexedens_medium__f10b64fd.yaml
- Started UTC: 2026-09-24T10:47:08Z
- Finished UTC: 2026-09-24T10:48:14Z
- Verdict: needs curation

## Target

Generated record `CultureMech:002872` for JCM/MediaDive medium `J521`, `MODIFIED DESULFOGLAEBA ALKANEXEDENS MEDIUM`.

The generated record merges `modified_desulfoglaeba_alkanexedens_medium` from `data/normalized_yaml/bacterial/modified_desulfoglaeba_alkanexedens_medium.yaml`. The generated YAML was compared with that maintained owner, the JCM 521 page, MediaDive medium `J521`, and TOGO `M522`, which imports the same JCM medium.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed with no error rows.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct JCM/MediaDive medium identity and preserves the top-level pH 7.3 from MediaDive.

The stock hierarchy has been flattened into direct ingredients. JCM 521 first prepares a `Mineral medium`, boils it under `N2-CO2 (4:1, v/v)`, dispenses 9.0 ml aliquots, then adds 0.4 ml 8.5% NaHCO3, 0.5 ml 2% sodium pyruvate solution, 0.1 ml trace vitamins, 0.01 ml decane, 0.05 ml 1% yeast extract solution, and 0.08 ml reducing-agent solution from sterile anoxic stocks.

## Evidence

JCM 521 and MediaDive `J521` list the `Mineral medium` stock as 25 g Sea salts (Sigma), 0.25 g NH4Cl, 3.5 g Na2SO4, 1 mg resazurin, and 900 ml distilled water. MediaDive normalizes those gram and milligram rows to the 901 ml stock volume, and the generated record carries those stock-strength values.

The final recipe is not just that stock. The JCM page adds six milliliter-scale post-autoclave stocks per 9.0 ml `Mineral medium`, and the generated record turns the 0.4 ml, 0.5 ml, 0.1 ml, 0.01 ml, and 0.05 ml additions into direct `G_PER_L` ingredient rows.

The 0.08 ml `Reducing agent solution` addition is more distorted: its 12.5 g Na2S x 9 H2O and 12.5 g L-Cysteine HCl x H2O per 1 L stock formula are emitted directly as 12.5 g/L final-medium rows, with the 0.08 ml addition volume and 1 L water row absent.

## Completeness

The generated YAML preserves the MediaDive identity, pH, most named chemical rows, and JCM procedural prose.

It is incomplete for the main recipe and nested stock topology. It also omits the distilled-water rows for both stocks, loses the `Sea salts (Sigma)` product qualifier on the JCM/MediaDive path, and does not link the sibling TOGO `M522` import that describes the same JCM 521 recipe.

## Findings

- High: The milliliter-scale post-autoclave additions are stored as direct gram-per-liter ingredient rows, losing their stock strengths and addition volumes.
- High: `Reducing agent solution` is flattened at full stock strength, so both reducing-agent chemicals are far above their final diluted amounts.
- Medium: The `Mineral medium` and `Reducing agent solution` water rows are absent from the generated record.
- Medium: The record is not deduplicated or source-linked with TOGO `M522`, which imports the same JCM 521 source page.
- Low: The generated MediaDive branch loses the Sigma qualifier from the sea-salts row.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/modified_desulfoglaeba_alkanexedens_medium.yaml` against the JCM 521 source formula with explicit `Mineral medium`, `Reducing agent solution`, and final assembly structure.
- Preserve the JCM final assembly as 9.0 ml `Mineral medium` plus 0.4 ml 8.5% NaHCO3, 0.5 ml 2% sodium pyruvate solution, 0.1 ml trace vitamins, 0.01 ml decane, 0.05 ml 1% yeast extract solution, and 0.08 ml reducing-agent solution.
- Preserve 25 g Sea salts (Sigma), 0.25 g NH4Cl, 3.5 g Na2SO4, 1 mg resazurin, and 900 ml distilled water in the `Mineral medium` stock and 12.5 g Na2S x 9 H2O, 12.5 g L-Cysteine HCl x H2O, and 1 L distilled water in the reducing-agent stock.
- Reconcile this MediaDive/JCM owner with the TOGO `M522` import so the two generated records do not continue to represent the same JCM source as disconnected recipes.
- Regenerate `data/merge_yaml/merged/modified_desulfoglaeba_alkanexedens_medium__f10b64fd.yaml` after the maintained owner is repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated record against JCM 521 and MediaDive `J521` to verify both stock recipes, the 9.0 ml final-medium assembly, the six post-autoclave addition volumes, the pH range, and the `N2-CO2` and `N2` gas-handling steps.
- Confirm that the TOGO `M522` sibling is either linked as a source duplicate or merged through a shared repaired owner.

## Additional Notes

None found.

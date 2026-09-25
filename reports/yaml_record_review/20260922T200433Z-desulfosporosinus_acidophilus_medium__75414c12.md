# YAML Record Review: desulfosporosinus_acidophilus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/desulfosporosinus_acidophilus_medium__75414c12.yaml
- Started UTC: 2026-09-22T20:02:41Z
- Finished UTC: 2026-09-22T20:04:33Z
- Verdict: needs curation

## Target

Generated MediaRecipe `CultureMech:009101`, `desulfosporosinus_acidophilus_medium`, from TOGO medium M2531.

The generated record has `media_term.id` `TOGO:M2531` and cites the DSMZ Medium 1250 PDF as the original URL.

## Validation

- LinkML open validation: passed.
- Strict validation: passed with 0 error rows.
- LinkML reference validation: passed with 0 checks.
- LinkML term validation: passed.
- Embedded history validation: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged records.

## Identity and Grounding

TOGO M2531 is a DSMZ Medium 1250 representation for Desulfosporosinus acidophilus. The source identity is therefore the same DSMZ 1250 recipe already present in `desulfosporosinus_acidophilus_medium__62d0f824.yaml` from MediaDive and KOMODO.

The target was not merged with the MediaDive/KOMODO DSMZ 1250 canonical because the TOGO import has a different fingerprint. That fingerprint difference is an artifact of unit and stock-solution modeling errors, not a true recipe distinction.

## Evidence

The TOGO M2531 API reports a main recipe with 1000 ml distilled water, ordinary salts and nutrients, 0.5 ml of 0.1% Na-resazurin solution, 1 ml of `Trace element solution SL-10`, 1 ml of `Selenite-tungstate solution`, and 10 ml of `Vitamin solution`. It then reports separate subcomponents for the trace-element, selenite-tungstate, and vitamin stock formulas.

The generated record sums the main and stock solvent volumes into one top-level water row, `3990.0` `G_PER_L`. It also keeps top-level rows for the stock constituents while adding four empty `solutions` stubs for Na-resazurin, SL-10, selenite-tungstate, and vitamins.

## Completeness

The target preserves the DSMZ 1250 source URL and many source ingredient names, but it does not preserve the nested recipe.

All generated `solutions` entries have `composition: []` and `name: Unknown solution`, so the SL-10, selenite-tungstate, vitamin, and Na-resazurin stock recipes are unusable as structured subrecipes.

The generated top-level formula is also not the DSMZ 1250 final medium: water from three one-liter stock formulas was added to the main solvent, stock milligram amounts such as 36 mg Na2MoO4 and 190 mg CoCl2 were copied as 36 g/L and 190 g/L final rows, and the 1 ml or 10 ml stock additions were copied as `G_PER_L` solution amounts.

## Findings

1. **Solvent water from independent recipes was summed into one final-medium row.**

   The generated `Distilled water` row is `3990.0` `G_PER_L` with notes showing a merge of `1000.0`, `990.0`, `1000.0`, and `1000.0`. Those volumes come from the main DSMZ 1250 formula and three stock recipes and must not be summed.

2. **Milligram stock masses were promoted to gram-per-liter final concentrations.**

   Several stock solutes were copied numerically into `G_PER_L` rows without unit conversion, including `Na2MoO4 x 2 H2O` at 36, `MnCl2 x 4 H2O` at 100, `CoCl2 x 6 H2O` at 190, and `Na2SeO3 x 5 H2O` at 3. Each source value is a milligram-scale stock recipe mass, not a final-medium gram-per-liter concentration.

3. **Solution references are empty and use milliliter additions as grams per liter.**

   The Na-resazurin, trace-element, selenite-tungstate, and vitamin solution entries have no composition. Their `concentration.value` entries, `0.5`, `1`, `1`, and `10`, are the source addition volumes in milliliters.

4. **Gas-atmosphere instructions were turned into ingredients.**

   TOGO exposes N2 and carbon dioxide from the recipe text. In this record they appear as variable top-level ingredients even though the source uses them to describe sparging and anaerobic stock preparation.

5. **The same DSMZ 1250 recipe is duplicated under a different fingerprint.**

   M2531 should collapse with the MediaDive/DSMZ 1250 plus KOMODO 1250 generated record once its stock-solution topology and units are normalized.

## Recommended Edits

Regenerate TOGO M2531 from the source hierarchy instead of flattening all subcomponents into the top-level `ingredients` list.

Model the 0.5 ml Na-resazurin, 1 ml SL-10, 1 ml selenite-tungstate, and 10 ml vitamin additions as solution additions and put each referenced stock recipe under `solutions` with the correct component units.

Keep N2 and CO2 in preparation or atmosphere metadata rather than top-level formula ingredients.

Add an equivalence link from TOGO M2531 to DSMZ 1250 / MediaDive 1250 so the regenerated record merges with the existing DSMZ 1250 canonical.

## Follow-up Checks

After regeneration, compare the TOGO M2531 output against both the TOGO M2531 API and MediaDive DSMZ 1250 and confirm that no stock solvent or stock solute remains as a top-level final-medium ingredient.

Regenerate the DSMZ 1250 provider family and confirm that TOGO M2531, MediaDive 1250, and KOMODO 1250 collapse into one record.

Run the focused LinkML open, strict, reference, and term validators on the regenerated record.

## Additional Notes

No source YAML was edited during this review. The exact duplicate check for the DSMZ 1250 family included ignored files.

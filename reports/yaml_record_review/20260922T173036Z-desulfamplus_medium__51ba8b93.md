# YAML Record Review: desulfamplus_medium__51ba8b93

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfamplus_medium__51ba8b93.yaml`
- Started UTC: 2026-09-22T17:30:36Z
- Finished UTC: 2026-09-22T17:30:36Z
- Verdict: needs curation

## Target

Generated bacterial `desulfamplus_medium` record for MediaDive/DSMZ Medium 1665.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to DSMZ Medium 1665 and keeps the DSMZ PDF URL in `notes`. MediaDive REST and the live DSMZ Medium 1665 PDF agree on a 1015 ml main solution containing 2 ml Wolfe's mineral elixir, 2 ml 0.5 M K-phosphate buffer, 10 ml FeCl2 stock in 0.02 N HCl, and 1 ml Wolin's vitamin solution.

The complex/undefined classification is supported by yeast extract.

## Evidence

The generated record predates the 2026-08-07 partial stock repair in `data/normalized_yaml/bacterial/desulfamplus_medium.yaml`. That repair moved four Wolfe mineral rows and one Wolin vitamin row into two `solutions`; the generated record still has no `solutions` block at all.

Wolfe's mineral elixir was flattened into final-medium ingredients at stock strength. This also merged stock salts with same-named main-solution salts: NaCl is `29.7044 G_PER_L` from final-basis main NaCl plus `10.0 G_PER_L` Wolfe stock NaCl, and CaCl2 x 2 H2O is `1.197044 G_PER_L` from final-basis main CaCl2 plus `1.0 G_PER_L` Wolfe stock CaCl2.

Other Wolfe stock components are top-level rows at their stock concentrations, including `30 G_PER_L` MgSO4 x 7 H2O, `5 G_PER_L` MnSO4 x H2O, `1 G_PER_L` FeSO4 x 7 H2O, `1.8 G_PER_L` CoCl2 x 6 H2O, `1.8 G_PER_L` ZnSO4 x 7 H2O, `2.8 G_PER_L` ammonium nickel sulfate hexahydrate, and `0.1 G_PER_L` each CuSO4 x 5 H2O, H3BO3, Na2MoO4 x 2 H2O, Na2WO4 x 2 H2O, and Na2SeO4.

Wolin's vitamin solution is likewise flattened at stock strength: Biotin and Folic acid are `0.02 G_PER_L`, Pyridoxine is `0.1 G_PER_L`, Thiamine, Riboflavin, Nicotinic acid, Calcium pantothenate, p-Aminobenzoic acid, and Lipoic acid are `0.05 G_PER_L`, and Vitamin B12 is `0.001 G_PER_L`.

The 2 ml 0.5 M K-phosphate buffer addition is represented only as `2 G_PER_L`, so the molarity and pH 7.0 stock attribute are not captured structurally.

`Na2SeO4` still carries a legacy `mediaingredientmech_term` instead of a `mediaingredientmech_chebi_term`.

## Completeness

The generated `preparation_steps` preserve the main anoxic preparation and the Wolfe mineral acidification note.

The stock-water rows for Wolfe's mineral elixir and Wolin's vitamin solution are absent, and no generated solution records preserve their 2 ml/L and 1 ml/L addition volumes.

## Findings

- Needs curation: Wolfe's mineral elixir and Wolin's vitamin solution are flattened into top-level final ingredients.
- Needs curation: stock-strength salts and vitamins are modeled as final-medium concentrations.
- Needs curation: bulk NaCl and CaCl2 are summed with Wolfe stock NaCl and CaCl2.
- Needs curation: K-phosphate buffer is represented as `2 G_PER_L` rather than a 2 ml addition of a 0.5 M pH 7.0 stock.
- Needs curation: the generated record lacks the partial Aug 7 stock nesting now present in normalized YAML.
- Needs curation: the normalized Aug 7 repair only nested 5 Wolfe/Wolin components and should be completed against DSMZ 1665 before regeneration.
- Minor issue: `Na2SeO4` retains a legacy MediaIngredientMech link.

## Recommended Edits

- Complete stock nesting in `data/normalized_yaml/bacterial/desulfamplus_medium.yaml` for all Wolfe's mineral elixir and Wolin's vitamin solution components.
- Preserve Wolfe and Wolin addition volumes of 2 ml/L and 1 ml/L in nested solution records.
- Keep bulk main-solution NaCl and CaCl2 separate from stock-internal Wolfe NaCl and CaCl2.
- Model the K-phosphate buffer as a 2 ml addition of 0.5 M pH 7.0 stock, not as `2 G_PER_L`.
- Regenerate the merged record only after the normalized DSMZ 1665 source has complete stock nesting.
- Replace the legacy `mediaingredientmech_term` on `Na2SeO4` with a CHEBI-keyed link.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after repair.
- Compare generated stock boundaries against both MediaDive REST medium 1665 and the DSMZ Medium 1665 PDF.
- Confirm no Wolfe or Wolin stock component remains as a top-level final-medium ingredient.
- Confirm main NaCl and CaCl2 are no longer merged with same-named Wolfe stock rows.

## Additional Notes

MediaDive REST medium 1665 and the linked DSMZ Medium 1665 PDF were both reachable during review.

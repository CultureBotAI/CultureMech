# YAML Record Review: fermentative_cellulolytic_anaerobes_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/fermentative_cellulolytic_anaerobes_medium__716d014a.yaml
- Started UTC: 2026-09-23T02:49:10Z
- Finished UTC: 2026-09-23T02:50:29Z
- Verdict: needs curation

## Target

CultureMech:003166 is the generated merged record for JCM Medium J822, `FERMENTATIVE CELLULOLYTIC ANAEROBES MEDIUM`.

The JCM 822 page defines a basal solution with KCl, NH4Cl, MgSO4 x 7 H2O, NaCl, CaCl2 x 2 H2O, trace minerals from Medium 151, yeast extract, resazurin, 1.0 M phosphate buffer, MOPS, and 910 ml distilled water. It then adds 40 ml 10% cellobiose solution, 10 ml Trace vitamins from Medium 197, 10 ml 5% NaHCO3 solution, 10 ml 5% Na2S x 9 H2O solution, and 10 ml 5% L-Cysteine HCl x H2O solution per liter from anaerobic stocks.

## Validation

- LinkML open-schema validation: pass; `linkml-validate` reported `No issues found`.
- Strict schema validation: pass; `scripts/validate_strict.py` reported 0 files with errors and 0 total error rows.
- Reference validation: pass; the reference validator scanned the file and reported 0 checks.
- Term validation: pass; `linkml-term-validator` exited 0 and reported `Validation passed`.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded history entries in generated MediaRecipe YAML.

## Identity and Grounding

The CultureMech identifier, normalized name, complex/undefined typing, JCM medium identifier, label, and source link all point to the intended JCM 822 recipe.

The generated CHEBI groundings are mostly plausible for the simple salts and specific hydrated salts. `Yeast extract` is a mixture and `Trace vitamins (see Medium No. 197)` is a named stock solution, so their lack of single-compound CHEBI grounding is appropriate.

`MnSO4 x n H2O` carries a broad manganese(II) sulfate term, which is the best available grounding for an explicitly variable hydrate.

## Evidence

The MediaDive REST payload for JCM J822 preserves the same main JCM 822 solution and a nested `Trace minerals` solution. JCM Medium 151 defines that Trace minerals stock as a 1 L stock; JCM 822 adds only 10 ml of it. The generated record instead flattens the full-strength Trace minerals stock into the top-level ingredient list and merges stock MgSO4 x 7 H2O, NaCl, and CaCl2 x 2 H2O into the basal-salt rows, yielding notes such as `Merged 2 duplicates: 0.599401, 3.0`.

The generated record also promotes several JCM 822 stock-solution volumes directly to `G_PER_L` concentrations: 40 ml 10% cellobiose becomes 40 g/L, 10 ml Trace vitamins becomes 10 g/L, and each 10 ml 5% NaHCO3, Na2S x 9 H2O, and L-Cysteine HCl x H2O addition becomes 10 g/L. Those source rows are volume additions of prepared stocks, not gram-per-liter masses.

JCM 822 describes its 1.0 M phosphate buffer as an equal-volume mixture of KH2PO4 and Na2HPO4. The generated `preparation_steps` use a different 28 ml plus 78 ml recipe, and the same text is present in the imported MediaDive REST payload, so this appears to be an upstream MediaDive transcription mismatch against the linked JCM page.

## Completeness

The generated record is not composition-complete for the JCM 822 hierarchy because it loses the basal-solution versus stock-solution boundaries and omits the explicit 1.0 M phosphate buffer as an added 1 ml stock.

It also overstates multiple stock-derived ingredients by recording stock concentrations or stock volumes as if they were final `G_PER_L` amounts.

## Findings

1. The 10 ml Medium 151 Trace minerals stock is flattened at full stock strength and merged into basal salts instead of being represented as a 10 ml/L stock addition or as 0.01x-scaled final concentrations.
2. The 40 ml 10% cellobiose, 10 ml Trace vitamins, and three 10 ml 5% reductant/bicarbonate stock additions are recorded as `40`, `10`, `10`, `10`, and `10` `G_PER_L` ingredients even though those source values are milliliter additions of prepared stocks.
3. The generated record drops the explicit 1 ml 1.0 M phosphate buffer addition from the ingredient list.
4. The phosphate-buffer preparation text says to mix 28 ml KH2PO4 with 78 ml Na2HPO4, but the linked JCM 822 page says to mix 50 ml plus 50 ml; the imported MediaDive REST payload carries the same 28/78 mismatch.

## Recommended Edits

1. Recurate JCM 822 with stock solutions preserved as distinct solution additions or scale each stock recipe to its actual contribution per liter.
2. Keep the direct basal ingredients separate from Medium 151 Trace minerals so MgSO4 x 7 H2O, NaCl, and CaCl2 x 2 H2O are not merged with unscaled stock rows.
3. Represent 10% Cellobiose solution, 5% NaHCO3 solution, 5% Na2S x 9 H2O solution, and 5% L-Cysteine HCl x H2O solution as stock additions or calculate their final solute mass concentrations from the percentage and added volume.
4. Correct the JCM 822 phosphate-buffer preparation text to the equal-volume recipe shown on the JCM page.

## Follow-up Checks

- Re-run open-schema, strict-schema, reference, and term validation after recurating the nested-stock structure.
- Confirm the post-fix record still resolves to `mediadive.medium:J822` and retains the JCM 822 link.
- Confirm the stock-derived ingredient quantities are either explicit volume additions or scaled final concentrations, never unscaled stock formula values.

## Additional Notes

The exact search for the suspect 28 ml KH2PO4 / 78 ml Na2HPO4 step included ignored files by using `rg --no-ignore --hidden` over the reviewed data and report paths.

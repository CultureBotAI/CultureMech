# YAML Record Review: dehalogenimonas_medium__6a926cbc

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dehalogenimonas_medium__6a926cbc.yaml`
- Started UTC: 2026-09-22T17:00:35Z
- Finished UTC: 2026-09-22T17:00:35Z
- Verdict: needs curation

## Target

Generated bacterial `dehalogenimonas_medium` record for MediaDive / JCM Medium J679.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to `mediadive.medium:J679` and points to the historical JCM GRMD 679 URL. A live lookup of that JCM URL now returns "Nothing found", so current primary confirmation was limited to the MediaDive REST J679 payload that the YAML was imported from.

The defined classification is plausible; no complex substrate appears in the MediaDive J679 formula.

Most hydrate salts and small molecules are plausibly grounded, but `NiCl2 x 6 H2O` is still grounded to CHEBI:34887, whose label is nickel dichloride rather than a hexahydrate. `Vancomycin x HCl` remains ungrounded.

## Evidence

MediaDive J679 has a 1006 ml main solution containing base salts, acetate, cysteine, resazurin, and 910 ml water. After autoclaving, it adds 30 ml 8% NaHCO3, 1 ml Trace element solution, 1 ml Selenite-tungstate solution, 10 ml Vitamin solution from Medium 403, 10 ml Thiamine solution from Medium 403, 10 ml Vitamin B12 solution from Medium 403, 10 ml 0.1 g/ml ampicillin, 10 ml 10 mg/ml vancomycin x HCl, 8 ml 5% Na2S x 9 H2O, and finally 6 ml 10 mg/ml 1,2-dichloropropane in methanol.

The two named inorganic stocks are flattened. One milliliter of Trace element solution contributes HCl, FeSO4 x 7 H2O, H3BO3, MnCl2 x 4 H2O, CoCl2 x 6 H2O, NiCl2 x 6 H2O, CuCl2 x 2 H2O, ZnSO4 x 7 H2O, and Na2MoO4 x 2 H2O, but the generated record stores those 1 liter stock concentrations as top-level final ingredients. The same flattening is present for the 1 ml Selenite-tungstate solution.

Several liquid additions are represented as if the milliliter amount itself were grams per liter: 30 ml of 8% NaHCO3 is `30 G_PER_L`, 10 ml of 0.1 g/ml ampicillin is `10 G_PER_L`, 10 ml of 10 mg/ml vancomycin is `10 G_PER_L`, 8 ml of 5% Na2S is `8 G_PER_L`, and 6 ml of 10 mg/ml 1,2-dichloropropane in methanol is `6 G_PER_L`.

The Medium 403 vitamin references have been migrated to `solutions`, but their compositions are empty and their 10 ml additions are encoded as `10 G_PER_L`.

## Completeness

The generated record has only three empty vitamin solutions; it lacks explicit Trace element and Selenite-tungstate stock records despite flattening their components.

The Medium 403 vitamin, thiamine, and vitamin B12 stocks need to be resolved and expanded or linked as stock additions so their composition is not lost.

The two preparation steps preserve the broad anaerobic workflow but do not structure which additions are autoclaved, filter-sterilized, pH-adjusted, and added after gas replacement.

## Findings

- Needs curation: 1 ml Trace element and 1 ml Selenite-tungstate stock components are flattened at stock strength as final ingredients.
- Needs curation: NaHCO3, ampicillin, vancomycin, Na2S, and 1,2-dichloropropane liquid additions use `G_PER_L` values derived from milliliter volumes, not final solute concentrations.
- Needs curation: the three 10 ml Medium 403 vitamin solution additions are empty and typed as `G_PER_L`.
- Needs curation: the generated record lacks non-empty stock models for all five stock additions.
- Minor: `Vancomycin x HCl` is ungrounded and `NiCl2 x 6 H2O` is grounded to an anhydrous nickel dichloride label.

## Recommended Edits

- Preserve `Main sol. J679` as the final recipe and nest Trace element solution, Selenite-tungstate solution, Vitamin solution, Thiamine solution, and Vitamin B12 solution under `solutions`.
- Keep trace and selenite/tungstate stock concentrations inside their stock compositions and represent each stock dose as a 1 ml final-medium addition.
- Resolve the three referenced Medium 403 vitamin stocks and populate their compositions, or link them explicitly to shared stock records.
- Convert the 8% NaHCO3, 0.1 g/ml ampicillin, 10 mg/ml vancomycin, 5% Na2S, and 10 mg/ml 1,2-dichloropropane additions from stock volume into correct final concentrations.
- Ground `Vancomycin x HCl`; ground `NiCl2 x 6 H2O` to the hydrated nickel chloride term if an appropriate CHEBI class exists.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after curation.
- Confirm `solutions` contains non-empty Trace element, Selenite-tungstate, Vitamin, Thiamine, and Vitamin B12 entries.
- Confirm HCl, trace metals, NaOH, selenite, and tungstate no longer appear as top-level final-medium ingredients.
- Confirm the antibiotic, bicarbonate, sulfide, and chlorosolvent concentrations are computed from the stock strengths and 1006 ml final volume.

## Additional Notes

`curl -L https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=679` currently returns a JCM "Nothing found" page; MediaDive REST medium J679 was available and matched the JCM identity stored in the generated record.

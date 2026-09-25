# YAML Record Review: dehalococcoides_medium__9ce6016b

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dehalococcoides_medium__9ce6016b.yaml`
- Started UTC: 2026-09-22T16:58:02Z
- Finished UTC: 2026-09-22T16:58:02Z
- Verdict: needs curation

## Target

Generated bacterial `dehalococcoides_medium` record for MediaDive / JCM Medium J827.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to `mediadive.medium:J827` and points to the historical JCM GRMD 827 URL. A live lookup of that JCM URL now returns "Nothing found", so current primary confirmation was limited to the MediaDive REST J827 payload that the YAML was imported from.

The defined classification is plausible because the formula has no complex substrate after the stocks are expanded.

Most ingredient groundings match their printed names, but `NiCl2 x 6 H2O` is still grounded to CHEBI:34887, whose label is nickel dichloride rather than a hexahydrate.

## Evidence

MediaDive J827 is not a flat recipe. Its `Main sol. J827` adds NaCl, MgCl2 x 6 H2O, NH4Cl, KCl, CaCl2 x 2 H2O, KH2PO4, sodium acetate, resazurin, water, and then five stocks: 1 ml FeCl2 solution, 1 ml Trace element solution, 1 ml Selenite-tungstate solution, 20 ml 25 mM Ti(III) NTA solution, and 1 ml Vitamin solution. It also adds liquid stock reagents: 1 ml 5% L-cysteine HCl x H2O, 1 ml 5% Na2S x 9 H2O, 10 ml 8% NaHCO3, 20 ml 1.0 M MOPS, and 0.7 ml of 10 mg/ml trichloroethylene in methanol.

The generated record flattened all nested stock components as if their stock-strength `g_l` values were final-medium concentrations. Examples include 2.5 g/L HCl and 1.5 g/L FeCl2 x 4 H2O from the 1 ml FeCl2 stock, 0.07 g/L ZnCl2 and other trace-metal stock concentrations from a 1 ml trace stock, 0.4 g/L NaOH plus selenite/tungstate from a 1 ml selenite-tungstate stock, and all vitamin stock concentrations from a 1 ml vitamin solution.

The volume additions were also encoded as mass concentrations: 1 ml 5% L-cysteine became `1 G_PER_L`, 1 ml 5% Na2S became `1 G_PER_L`, 10 ml 8% NaHCO3 became `10 G_PER_L`, 20 ml 1.0 M MOPS became `20 G_PER_L`, and 0.7 ml of a 10 mg/ml trichloroethylene-in-methanol solution became `0.7 G_PER_L`.

The generated record has `ph_value: 9.0`, inherited from MediaDive `min_pH/max_pH`, but the imported preparation step says to check final pH at about 7.2. The pH 9.0 adjustment belongs to the 25 mM Ti(III) NTA stock preparation, not the final medium.

## Completeness

No `solutions` section is present, so the five named stock additions and their nested compositions are unrecoverable as stock records.

The 25 mM Ti(III) NTA stock is especially incomplete: the stock recipe contains nitrilotriacetic acid in 300 ml anaerobic water and the preparation adds 9.6 ml of 20% TiCl3, but the generated ingredient list contains only NTA and generic NaOH pH adjustment.

The generic preparation steps preserve useful prose, but they are too broad to identify which ingredients are autoclaved in the initial medium, which anaerobic stocks are added after cooling, and which chlorosolvent addition completes the medium.

## Findings

- Needs curation: all FeCl2, trace-element, selenite-tungstate, vitamin, and Ti(III) NTA stock components are flattened into top-level final-medium ingredients.
- Needs curation: stock-strength `g_l` values are used as final `G_PER_L` concentrations for every flattened stock component.
- Needs curation: multiple milliliter stock additions are represented as grams per liter.
- Needs curation: `ph_value: 9.0` conflicts with the source final-medium pH note of about 7.2.
- Needs curation: the Ti(III) NTA stock omits TiCl3 as a structured component.
- Minor: `NiCl2 x 6 H2O` is grounded to an anhydrous nickel dichloride label.

## Recommended Edits

- Preserve `Main sol. J827` as the final recipe and nest FeCl2 solution, Trace element solution, Selenite-tungstate solution, Vitamin solution, and 25 mM Ti(III) NTA solution under `solutions`.
- Keep stock component concentrations inside their stock compositions and represent each stock dose in the final medium as a milliliter addition.
- Convert the 5% cysteine, 5% sulfide, 8% bicarbonate, 1.0 M MOPS, and 10 mg/ml trichloroethylene additions from volume additions into correct final quantities or structured stock additions.
- Move the main-medium pH to 7.2 and retain pH 9.0 only inside the Ti(III) NTA stock preparation.
- Add TiCl3 from the Ti(III) NTA preparation step as a source-backed stock component or explicitly flag it as a reagent that cannot yet be represented.
- Ground `NiCl2 x 6 H2O` to the hydrated nickel chloride term if an appropriate CHEBI class exists.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after curation.
- Confirm the generated record has a non-empty `solutions` section.
- Confirm stock-internal FeCl2, trace metals, selenite/tungstate, vitamins, NTA, and TiCl3 are no longer top-level final-medium ingredients.
- Confirm `ph_value` reflects the final medium rather than the Ti(III) NTA stock adjustment.

## Additional Notes

`curl -L https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=827` currently returns a JCM "Nothing found" page; MediaDive REST medium J827 was available and matched the JCM identity stored in the generated record.

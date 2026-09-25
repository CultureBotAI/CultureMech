# YAML Record Review: CLOSTRIDIUM SWELLFUNIANUM MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_swellfunianum_medium__003670e0.yaml`
- Started UTC: `2026-09-22T09:37:22Z`
- Finished UTC: `2026-09-22T09:37:41Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:002193` for JCM Medium `J1009`, generated from `data/normalized_yaml/bacterial/clostridium_swellfunianum_medium.yaml` on merge fingerprint `003670e092c32c8e7de1591ffc2d3f7761202b1457f50b96f29723e508df5d13`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_swellfunianum_medium__003670e0.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The JCM identity is correct: the record cites JCM `GRMD=1009`, names `CLOSTRIDIUM SWELLFUNIANUM MEDIUM`, and preserves pH 7.3.

The same JCM 1009 source is emitted separately from the TOGO import as `data/merge_yaml/merged/CLOSTRIDIUM_SWELLFUNIANUM_MEDIUM.yaml` through TOGO `M1066`; the two branches should converge after stock aliquots are modeled consistently.

Most hydrated salts in this branch are grounded specifically. `NiCl2 x 6 H2O` remains grounded to generic nickel dichloride.

## Evidence

The JCM Medium 1009 page lists a one-liter base with 0.33 g each of NH4Cl, KCl, and KH2PO4; 0.5 g yeast extract; 3.0 g tryptone; 1.0 ml Trace element solution SL-10; 10.0 ml Trace vitamins; 33.0 ml 1% CaCl2 x 2H2O; 16.5 ml 2% MgCl2 x 6H2O; 0.5 g L-Cysteine HCl x H2O; 1.0 ml 1% resazurin; and 1.0 l water. It then adjusts pH to 7.3 and prepares the medium anaerobically under an N2-CO2 4:1 gas mixture.

After autoclaving, JCM instructs adding three anaerobic stocks per 5.0 ml culture volume: 0.05 ml of 3% Na2S x 9H2O, 0.05 ml of 10% NaHCO3, and 0.1 ml of 20% glucose.

The ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found both the direct JCM branch and the TOGO `M1066` branch for exact JCM 1009 URL tokens; ignored files were included.

## Completeness

The record carries pH and some preparation text, but the stock structure is absent:

- Trace element solution SL-10 is flattened into top-level final ingredients.
- Trace vitamins are flattened into top-level final ingredients.
- 1% CaCl2, 2% MgCl2, and 1% resazurin solution aliquots are stored as plain ingredients.
- The three per-5-ml post-autoclave additions are top-level ingredients instead of post-autoclave stock aliquots.

## Findings

- Milliliter aliquots of pre-autoclave stocks are stored as grams per liter with the source volume as the numeric value: `CaCl2 x 2 H2O` is `33 G_PER_L`, `MgCl2 x 6 H2O` is `16.5 G_PER_L`, and `Resazurin` is `1 G_PER_L`.
- The post-autoclave 3%, 10%, and 20% stock additions are also stored from source milliliter values rather than concentrations. `Na2S x 9 H2O` is `0.05 G_PER_L`, `NaHCO3` is `0.05 G_PER_L`, and `Glucose` is `0.1 G_PER_L`, even though each amount is defined per 5 ml of final medium.
- Trace element solution SL-10 internals are flattened at one-liter stock strength, including `HCl` `2.5 G_PER_L`, `FeCl2 x 4 H2O` `1.5 G_PER_L`, `ZnCl2` `0.07 G_PER_L`, `MnCl2 x 4 H2O` `0.1 G_PER_L`, and `NiCl2 x 6 H2O` `0.024 G_PER_L`.
- Trace vitamin internals are flattened as top-level ingredients and need to remain under the referenced Trace vitamins stock.
- The TOGO `M1066` generated branch keeps several solution shells, but those shells are empty and still store source milliliter amounts as `G_PER_L`, so neither import branch is a faithful stock representation yet.
- The main anaerobic preparation step text ends just before the three after-autoclave additions, leaving the reader to infer the stock rows from already-flattened ingredients.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/clostridium_swellfunianum_medium.yaml`, `data/normalized_yaml/bacterial/TOGO_M1066_Clostridium_Swellfunianum_Medium.yaml`, or the JCM/TOGO import logic, then regenerate; generated `data/merge_yaml/merged/*.yaml` outputs are derived.
- Represent Trace element solution SL-10 and Trace vitamins as explicit stock solutions.
- Model 1% CaCl2, 2% MgCl2, 1% resazurin, 3% Na2S, 10% NaHCO3, and 20% glucose as stock aliquots with their source volume additions.
- Preserve the post-autoclave per-5-ml instruction in structured preparation metadata.
- Re-ground `NiCl2 x 6 H2O` to a nickel chloride hexahydrate term.
- Reconcile the direct JCM and TOGO `M1066` branches once both imports preserve the same stock boundaries.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm CaCl2, MgCl2, resazurin, Na2S, NaHCO3, and glucose no longer use raw milliliter aliquots as gram-per-liter amounts.
- Confirm no SL-10 or Trace vitamins internal appears as a top-level final ingredient.
- Confirm direct JCM and TOGO `M1066` branches either merge or have a documented source-level reason to remain separate.

## Additional Notes

Empty optional fields are not defects. This record's main issue is that JCM has two aliquot scales, per liter and per 5 ml, and both need to survive import for the final concentrations to be meaningful.

# YAML Record Review: CR1+ Diatom Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/cr1_diatom_medium.yaml`
- Started UTC: 2026-09-22T11:53:47Z
- Finished UTC: 2026-09-22T11:53:47Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:000152` / `cr1_diatom_medium`, generated from a 10-way merge of unrelated or partly related UTEX algae recipes:

- `2x_soil_seawater_medium`
- `Ag_Diatom_Medium`
- `CR1+_Diatom_Medium`
- `CR1_Diatom_Medium`
- `Combo_Diatom_Medium`
- `Polytomella_Medium`
- `Soilwater_Peat_Medium`
- `cr1_s_diatom_medium`
- `soil_extract_sodium_metasilicate_medium`
- `soilwater_gr_medium`

## Validation

- Open schema validation passed for `MediaRecipe`.
- Strict validation passed and wrote `/private/tmp/cr1_diatom_medium.strict.tsv`.
- LinkML reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded `curation_history` was not separately checked because the available `validate-history` target validates standalone files under `history/`, not history entries embedded in generated `MediaRecipe` YAML.

## Identity and Grounding

The generated identity points at UTEX CR1+ Diatom Medium, but the generated composition is the stale ordinal table from the original UTEX import:

- ingredient `1` with `Original amount: Green House Soil`
- ingredient `2` with `Original amount: CaCO3(Fisher C 64)`
- ingredient `3` with `Original amount: Supplemented Seawater`

Those rows actually describe `2X Soil+Seawater Medium`, not CR1+ Diatom Medium. Current UTEX CR1+ lists `CR1 Soil`, 12 mL `dH2O`, and 1 drop `Pasteurized Seawater` per 15 mL tube. Current UTEX CR1 lists `CR1 Soil`, `MgCO3 (MCIB CB486)` at 0.5 mg/12 mL with 0.5 mM final concentration, and 12 mL `dH2O`. Current UTEX Ag Diatom lists `CR1 Soil`, the same `MgCO3` amount, and 12 mL `Modified Bold 3N Medium`.

## Evidence

Primary source checks:

- `https://utex.org/products/cr1-plus-diatom-medium` was fetched to `/private/tmp/utex_cr1_plus_diatom.html` and lists CR1 Soil, 12 mL dH2O, and 1 drop Pasteurized Seawater.
- `https://utex.org/products/cr1-diatom-medium` was fetched to `/private/tmp/utex_cr1_diatom.html` and lists CR1 Soil, 0.5 mg/12 mL MgCO3, and 12 mL dH2O.
- `https://utex.org/products/ag-diatom-medium` was fetched to `/private/tmp/utex_ag_diatom.html` and lists CR1 Soil, 0.5 mg/12 mL MgCO3, and 12 mL Modified Bold 3N Medium.

Local normalized record checks:

- `CR1+_Diatom_Medium.yaml` has CR1 Soil, 1000 mL/L dH2O, and variable Pasteurized Seawater.
- `CR1_Diatom_Medium.yaml` has CR1 Soil, 0.5 mM MgCO3, and 1000 mL/L dH2O.
- `Ag_Diatom_Medium.yaml` and `Combo_Diatom_Medium.yaml` are distinct supplemented variants of Modified Bold 3N Medium and Modified COMBO Medium.
- `cr1_s_diatom_medium.yaml` is a substituted-component child of CR1 Diatom Medium.
- `2x_soil_seawater_medium.yaml`, `Polytomella_Medium.yaml`, `Soilwater_Peat_Medium.yaml`, `soil_extract_sodium_metasilicate_medium.yaml`, and `soilwater_gr_medium.yaml` have source-specific recipes and should not be aliases of CR1+.

## Completeness

The generated record is complete only in the sense that it preserves the three placeholder rows produced by the broken UTEX table import. It is stale relative to the August 30 and September 6 normalized repairs that restored real UTEX component names, amounts, stock relationships, and parent-child variant links.

## Findings

1. Needs curation: the generated record uses row ordinals as ingredient names.

   `1`, `2`, and `3` are table row numbers, not medium components. The generated notes also carry the component labels in the wrong field and assign `G_PER_L` to all three variable soil/seawater rows.

2. Needs curation: the generated record overmerges 10 UTEX recipes that are not source duplicates.

   The shared broken fingerprint came from the same three ordinal ingredient names, not from equivalent chemistry. `Polytomella_Medium`, for example, is a water, yeast extract, tryptone, and sodium acetate recipe; `Ag_Diatom_Medium` is a CR1 Soil + MgCO3 + Modified Bold 3N Medium recipe; `2x_soil_seawater_medium` is a 60 ppt Green House Soil + CaCO3 + Supplemented Seawater recipe. Treating all of these as synonyms of CR1+ destroys recipe identity.

3. Needs curation: the generated record has not incorporated repaired UTEX variant relationships.

   The normalized CR1-S record is explicitly linked as a substituted-component child of CR1 Diatom Medium; Ag Diatom and COMBO Diatom point to their own prepared-media parents; Soil Extract + Sodium Metasilicate points to Soil Extract Medium. None of those relationships can be represented correctly while the generated 10-way merge flattens every source into one CR1+ record.

## Recommended Edits

- Regenerate merge output after the repaired UTEX ingredients are in the merge input set, and confirm the ordinal-only fingerprint `7ee74ca6db4b367eec57934b47ce1e5b6df3bec871194875b45bb7de23168c0b` no longer drives a merge.
- Keep CR1+ and CR1 as separate UTEX recipes because CR1+ uses Pasteurized Seawater while CR1 uses MgCO3.
- Keep CR1-S as a `SUBSTITUTED_COMPONENT_VARIANT` child of CR1 Diatom Medium.
- Keep Ag Diatom and COMBO Diatom as supplemented variants of their prepared-media parents rather than aliases of CR1+.
- Keep 2X Soil+Seawater, Polytomella, Soilwater Peat, Soilwater GR+, and Soil Extract + Sodium Metasilicate as separate recipes or as variants of their own local parents.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regenerating the affected UTEX algae records.
- Search generated merge output for the ten `merged_from` names listed above with ignored files included and verify they no longer share a single generated YAML record.
- Confirm no generated algae medium still has placeholder ingredients named only `1`, `2`, or `3`.
- Confirm generated CR1, CR1+, CR1-S, Ag Diatom, and COMBO Diatom records still carry the September 2026 parent-child links from their normalized owners.

## Additional Notes

The local search that inspected the CR1 family used `rg --no-ignore --hidden`, so ignored report files and generated outputs were included.

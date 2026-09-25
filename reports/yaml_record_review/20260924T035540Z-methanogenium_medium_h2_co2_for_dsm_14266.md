# YAML Record Review: methanogenium_medium_h2_co2_for_dsm_14266
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanogenium_medium_h2_co2_for_dsm_14266.yaml
- Started UTC: 2026-09-24T03:53:41Z
- Finished UTC: 2026-09-24T03:55:40Z
- Verdict: needs curation

## Target
- ID: CultureMech:009125
- Name: methanogenium_medium_h2_co2_for_dsm_14266
- Label: Methanogenium Medium (H2/CO2) (For DSM 14266)
- Category: archaea
- Source: TOGO M2556, imported from DSMZ 141
- Merge fingerprint: 443b6247e7ce5c1734209fe69a2649a9b7f780a4695edca79235047f6f52b2e4
- Merged from: methanogenium_medium_h2_co2_for_dsm_14266
- Maintained owner: data/normalized_yaml/archaea/methanogenium_medium_h2_co2_for_dsm_14266.yaml

## Validation
- Open schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; 0 reference checks, all passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The record identity matches TOGO M2556, Methanogenium Medium (H2/CO2) (For DSM 14266), a DSMZ 141 strain-specific variant.
- An exhaustive hidden and ignored search for `TOGO:M2556`, `CultureMech:009125`, and `methanogenium_medium_h2_co2_for_dsm_14266` found one maintained normalized owner plus expected generated indexes and merged output.
- NiCl2 x 6 H2O is grounded to generic nickel dichloride.

## Evidence
- DSMZ 141 lists DSM 14266 in the group that should use one atmosphere overpressure of sterile 80% H2 and 20% CO2 gas mixture.
- TOGO M2556 carries that one-atmosphere DSM 14266 comment and carries Trace element solution and Vitamin solution as local subcomponents of the M2556 recipe.
- The YAML has no `preparation_steps`; the one-atmosphere DSM 14266 pressure and the base DSMZ 141 anoxic preparation workflow are absent.
- The Trace element solution and Vitamin solution children are flattened into top-level final-medium ingredients at full stock strength.
- Those local subrecipes are also retained as empty `Unknown solution` stubs and are incorrectly linked to unrelated `mediadive.solution:6187` and `mediadive.solution:6241` records.
- Source milliliter and milligram amounts are inflated into grams per liter: 0.5 ml Na-resazurin solution, 2 ml Fe(NH4)2(SO4)2 solution, 0.3 mg Na2SeO3 x 5 H2O, 0.4 mg Na2WO4 x 2 H2O, and all vitamin amounts are affected.
- KOH solution and the N2/H2/CO2 gas handling are preparation context in DSMZ/TOGO, but they appear as unscoped components in the YAML.

## Completeness
- The main medium, local trace solution, local vitamin solution, and DSM 14266 variant signal are present in flattened or note form.
- The one-atmosphere pressure instruction, stock hierarchy, stock dilution, and base DSMZ preparation steps are absent.
- Empty optional fields are acceptable, but these empty solution stubs stand in for required source subrecipes.

## Findings
- Major: `data/normalized_yaml/archaea/methanogenium_medium_h2_co2_for_dsm_14266.yaml` loses the one-atmosphere overpressure condition that distinguishes DSM 14266 from base DSMZ 141.
- Major: Trace element solution and Vitamin solution are flattened at full stock strength and also remain as empty `Unknown solution` placeholders.
- Major: The local stock placeholders are linked to unrelated global MediaDive solutions `mediadive.solution:6187` and `mediadive.solution:6241`.
- Major: Multiple source ml and mg rows are imported as grams per liter.
- Major: DSMZ/TOGO preparation comments are not represented as preparation steps, and KOH plus gas handling were turned into unscoped medium components.
- Minor: NiCl2 x 6 H2O needs hydrate-specific grounding if a suitable CHEBI term is available.

## Recommended Edits
- Re-curate `data/normalized_yaml/archaea/methanogenium_medium_h2_co2_for_dsm_14266.yaml` from TOGO M2556 and DSMZ 141.
- Preserve the DSM 14266 one-atmosphere H2/CO2 overpressure as a scoped incubation condition.
- Model Trace element solution and Vitamin solution as local 10 ml stock additions rather than linking to `mediadive.solution:6187` or `mediadive.solution:6241`.
- Keep trace minerals and vitamins inside their 1 L stock scopes.
- Represent Na-resazurin and Fe(NH4)2(SO4)2 as 0.1% w/v milliliter additions.
- Move KOH and N2/H2/CO2 gas mentions into preparation or atmosphere fields and restore the DSMZ 141 preparation workflow.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanogenium_medium_h2_co2_for_dsm_14266.yaml`.
- Confirm that the one-atmosphere DSM 14266 condition appears in the regenerated record.
- Confirm that `Unknown solution`, `mediadive.solution:6187`, and `mediadive.solution:6241` are gone from this owner.
- Confirm that source ml and mg values are not inflated to grams per liter.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- The base DSMZ 141 owner and TOGO M2641 need parallel stock-hierarchy fixes before this variant can be linked cleanly to a repaired parent medium.

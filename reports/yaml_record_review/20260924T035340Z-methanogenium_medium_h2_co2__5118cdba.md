# YAML Record Review: methanogenium_medium_h2_co2__5118cdba
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanogenium_medium_h2_co2__5118cdba.yaml
- Started UTC: 2026-09-24T03:51:43Z
- Finished UTC: 2026-09-24T03:53:40Z
- Verdict: needs curation

## Target
- ID: CultureMech:009198
- Name: methanogenium_medium_h2_co2
- Label: Methanogenium Medium (H2/CO2)
- Category: archaea
- Source: TOGO M2641, imported from DSMZ 141
- Merge fingerprint: 5118cdba234f6b1f25d677f5eb2cd00c1c8cc53e1da6af4688a2e860d5937e73
- Merged from: TOGO_M2641_Methanogenium_Medium_H2_CO2
- Maintained owner: data/normalized_yaml/archaea/TOGO_M2641_Methanogenium_Medium_H2_CO2.yaml

## Validation
- Open schema validation: Passed; no issues found.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; 0 reference checks, all passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The record identity matches TOGO M2641, a TOGO extraction of DSMZ Medium 141, METHANOGENIUM MEDIUM (H2/CO2).
- An exhaustive hidden and ignored search for `TOGO:M2641`, `CultureMech:009198`, and `TOGO_M2641_Methanogenium_Medium_H2_CO2` found one maintained normalized owner plus expected generated indexes and the merged output.
- AIK(SO4)2 x 12 H2O is an OCR or normalization error for source AlK(SO4)2 x 12 H2O and has no ontology grounding.
- NiCl2 x 6 H2O is grounded to generic nickel dichloride.

## Evidence
- DSMZ 141 defines a 1013 ml main medium with 10 ml Modified Wolin's mineral solution, 10 ml Wolin's vitamin solution, 2 ml Fe(NH4)2(SO4)2 x 6 H2O 0.1% w/v, and 0.5 ml sodium resazurin 0.1% w/v.
- TOGO M2641 keeps Modified Wolin's mineral solution and Wolin's vitamin solution as local subcomponents of M2641.
- The YAML flattens every Modified Wolin mineral ingredient and every Wolin vitamin ingredient into the top-level final ingredient list at full stock strength.
- The YAML also leaves empty `Unknown solution` stubs for 10 ml Modified Wolin's mineral solution and 10 ml Wolin's vitamin solution, with those volumes encoded as `10 G_PER_L`.
- Source solution amounts are dimensionally wrong: 0.5 ml Sodium resazurin and 2 ml Fe(NH4)2(SO4)2 stock are encoded as `0.5 G_PER_L` and `2 G_PER_L`, while 0.3 mg Na2SeO3 x 5 H2O, 0.4 mg Na2WO4 x 2 H2O, and all Wolin vitamin milligram values are promoted to grams per liter.
- KOH solution, N2, H2, and CO2 are mentioned only as preparation or gas-phase context in the source but appear as medium components or an empty solution placeholder.
- The DSMZ preparation text is absent from `preparation_steps`.

## Completeness
- The main medium, Modified Wolin's mineral solution, and Wolin's vitamin solution are all present in flattened form.
- The required stock-solution hierarchy, source milliliter additions, and DSMZ anoxic preparation workflow are absent.
- Empty optional fields are acceptable, but these empty solution stubs stand in for required source subrecipes.

## Findings
- Major: `data/normalized_yaml/archaea/TOGO_M2641_Methanogenium_Medium_H2_CO2.yaml` flattens Modified Wolin's mineral solution and Wolin's vitamin solution at full stock strength.
- Major: The solution additions for Modified Wolin and Wolin vitamin stocks are empty `Unknown solution` placeholders with milliliters encoded as `G_PER_L`.
- Major: Source milliliter and milligram values are repeatedly asserted as grams per liter.
- Major: DSMZ preparation instructions for H2-CO2 sparging, bicarbonate addition, autoclaving, filter-sterilized vitamins, anoxic cysteine and sulfide stocks, pH adjustment, and incubation pressure are missing.
- Major: KOH, N2, H2, and CO2 are unscoped preparation or atmosphere details that became medium components.
- Minor: AIK(SO4)2 x 12 H2O needs correction to AlK(SO4)2 x 12 H2O, and NiCl2 x 6 H2O needs hydrate-specific grounding if a suitable term is available.

## Recommended Edits
- Re-curate `data/normalized_yaml/archaea/TOGO_M2641_Methanogenium_Medium_H2_CO2.yaml` from TOGO M2641 and DSMZ 141.
- Model Modified Wolin's mineral solution and Wolin's vitamin solution as local 10 ml stock additions.
- Keep Modified Wolin trace minerals and Wolin vitamins inside their stock scopes with 1 L stock volumes.
- Represent sodium resazurin and Fe(NH4)2(SO4)2 as 0.1% w/v milliliter additions rather than gram-per-liter rows.
- Move KOH and the N2/H2/CO2 gas mentions into preparation or atmosphere fields.
- Restore DSMZ 141 preparation text.
- Correct AIK(SO4)2 x 12 H2O and re-ground NiCl2 x 6 H2O where possible.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanogenium_medium_h2_co2__5118cdba.yaml`.
- Confirm that `Unknown solution` is gone from the TOGO M2641 owner.
- Confirm that Modified Wolin and Wolin vitamin children are no longer top-level final-medium rows.
- Confirm that source ml and mg values are no longer inflated to grams per liter.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- DSMZ 141 has a direct MediaDive owner and a KOMODO owner that should be source-duplicate candidates once the TOGO M2641 stock structure is repaired.

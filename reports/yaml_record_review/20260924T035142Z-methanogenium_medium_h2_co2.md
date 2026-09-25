# YAML Record Review: methanogenium_medium_h2_co2
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanogenium_medium_h2_co2.yaml
- Started UTC: 2026-09-24T03:50:20Z
- Finished UTC: 2026-09-24T03:51:42Z
- Verdict: needs curation

## Target
- ID: CultureMech:000254
- Name: methanogenium_medium_h2_co2
- Label: METHANOGENIUM MEDIUM (H2/CO2)
- Category: archaea, bacterial
- Source: 23 merged DSMZ 141 base and variant imports
- Merge fingerprint: ae6b426bcf618604aa970ec3128e9600c25adaa91f6f4edb96027d44eb8b2403
- Merged from: KOMODO_141_METHANOGENIUM_medium, methanogenium_medium_h2_co2, and 21 DSMZ 141 variant owners
- Maintained owners: the normalized records named in `merged_from`, including `data/normalized_yaml/archaea/methanogenium_medium_h2_co2.yaml` and `data/normalized_yaml/archaea/KOMODO_141_METHANOGENIUM_medium.yaml`

## Validation
- Open schema validation: Passed; no issues found.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The generated record is grounded to DSMZ 141 / mediadive.medium:141, METHANOGENIUM MEDIUM (H2/CO2), but it also merged DSMZ 141 strain-specific variants such as DSM 4254, DSM 15558, DSM 16458, and DSM 14266 into the same recipe.
- An exhaustive hidden and ignored search for `CultureMech:000254`, `mediadive.medium:141`, and `komodo.medium:141` found the direct DSMZ owner, the KOMODO 141 owner, generated indexes, the merged output, and several DSMZ 141 variant owners that already share the same CultureMech ID.
- The merged output classifies a yeast-extract and Trypticase-containing medium as `medium_type: DEFINED` and `composition_type: DEFINED`, which conflicts with the complex DSMZ base recipe.
- NiCl2 x 6 H2O is grounded to generic nickel dichloride.

## Evidence
- DSMZ 141 defines a 1013 ml main medium containing 10 ml Modified Wolin's mineral solution and 10 ml Wolin's vitamin solution.
- Modified Wolin's mineral solution and Wolin's vitamin solution are 1 L stocks with their own formulas and preparation constraints; they are not final-medium gram-per-liter rows.
- `data/normalized_yaml/archaea/methanogenium_medium_h2_co2.yaml` already scales the stock ingredients by their 10 ml additions, but it still flattens them into top-level rows and has no structural `solutions` array.
- The generated merged YAML is stale or contaminated by unrepaired sibling owners: MgSO4 x 7 H2O, CaCl2 x 2 H2O, and NaCl are duplicate-summed with full-strength Modified Wolin stock values, and all trace-mineral and vitamin rows appear at full stock strength.
- DSMZ 141 lists strain-specific modifications for pH, trypticase concentration, methanol, L-histidine, coenzyme M, and gas overpressure. The merged YAML reduces modified DSMZ 141 records to `synonyms` and `merged_from` entries without preserving those variant instructions.
- DSMZ preparation steps for H2-CO2 sparging, Hungate tubes or serum vials, anoxic cysteine and sulfide stocks, filter-sterilized vitamin stock, pH adjustment, and two-atmosphere incubation are present in the merged output.

## Completeness
- The base DSMZ 141 formulation is present, but Modified Wolin's mineral solution and Wolin's vitamin solution are flattened.
- Strain-specific DSMZ 141 variant changes are not structurally represented.
- The direct DSMZ 141 owner no longer carries the full-strength stock rows seen in the merged output, so at least one sibling normalized input in the 23-way merge still needs the same stock-scope repair before regeneration.
- Empty optional fields are acceptable; no optional-field omission was counted as a defect.

## Findings
- Major: The generated `data/merge_yaml/merged/methanogenium_medium_h2_co2.yaml` sums final-medium salts with full-strength Modified Wolin stock salts, which makes NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O too high.
- Major: The 10 ml Modified Wolin mineral stock and 10 ml Wolin vitamin stock are flattened across the maintained DSMZ 141 owners instead of being modeled as stock solutions.
- Major: DSMZ 141 strain-specific variants were merged into one base record and demoted to synonyms, erasing changes such as 6.00 g/l trypticase for DSM 2373, 50% methanol for DSM 4103, L-histidine for DSM 4254, and one-atmosphere gas handling for DSM 14266.
- Major: `medium_type` and `composition_type` in the merged output conflict with the source medium's yeast extract and Trypticase peptone.
- Minor: NiCl2 x 6 H2O needs hydrate-specific grounding if a suitable CHEBI term is available.

## Recommended Edits
- Repair every DSMZ 141 normalized owner named in `merged_from` that still emits full-strength Modified Wolin or Wolin vitamin stock rows.
- Model Modified Wolin's mineral solution and Wolin's vitamin solution as 10 ml solution additions in `data/normalized_yaml/archaea/methanogenium_medium_h2_co2.yaml` and sibling 141 owners.
- Represent DSMZ 141 strain-specific recipes as MediaVariant records or separate child recipes so variant additives, pH values, and gas pressures are not folded into base-recipe synonyms.
- Keep the base DSMZ 141 record `COMPLEX` and `UNDEFINED` or otherwise classify it consistently with yeast extract and Trypticase peptone.
- Re-ground NiCl2 x 6 H2O if a hydrate-specific term is available.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanogenium_medium_h2_co2.yaml`.
- Confirm that NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O are not duplicate-summed across main and Modified Wolin scopes.
- Confirm that full-strength Modified Wolin and Wolin vitamin rows no longer appear as final-medium ingredients.
- Confirm that DSMZ 141 variant records keep their strain-specific modifications instead of only appearing as synonyms.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- The DSMZ PDF also lists variants for DSM 1498, DSM 22353, DSM 15219, DSM 18860, DSM 21220, and DSM 22026 that are not represented among the 23 merged inputs; those may need follow-up MediaVariant curation if the corpus tracks DSMZ strain-specific variants comprehensively.

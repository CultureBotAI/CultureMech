# YAML Record Review: Sulfuricurvum MBM Medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfuricurvum_mbm_medium.yaml` (`CultureMech:000442`)
- Started UTC: `2026-09-25T08:29:05Z`
- Finished UTC: `2026-09-25T08:29:05Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfuricurvum_mbm_medium.yaml` |
| Normalized sources | `data/normalized_yaml/bacterial/sulfuricurvum_mbm_medium.yaml`, `data/normalized_yaml/bacterial/mbm_medium_modified.yaml` |
| CultureMech ID | `CultureMech:000442` |
| Media terms | `mediadive.medium:1020`, `komodo.medium:1020` |
| Original source | DSMZ Medium 1020, SULFURICURVUM (MBM) MEDIUM |
| Merge fingerprint | `4393eaf9b1726a8511a3e974eda746707d004190f8bf4d184a911bf9158e9312` |
| Merged from | `mbm_medium_modified`, `sulfuricurvum_mbm_medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` exited 0 with no diagnostics for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected canonical `CultureMech:000442` identifier, `mediadive.medium:1020` source term, linked `komodo.medium:1020` duplicate, and merge fingerprint. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:000442`, `mediadive.medium:1020`, `komodo.medium:1020`, the merge fingerprint, `sulfuricurvum_mbm_medium.yaml`, and `mbm_medium_modified.yaml` found the expected normalized sources, generated merge, duplicate link, and normalized indexes.

The MediaDive/DSMZ source and KOMODO DSMZ 1020 duplicate have the same ingredient signature, so the source-duplicate merge is defensible. Most basal ingredients are plausibly grounded, but Trace element solution SL-4 is not correctly scoped and `NiCl2 x 6 H2O` is grounded to generic nickel dichloride rather than a hydrate-specific term.

## Evidence

The DSMZ Medium 1020 PDF and MediaDive 1020 list the main solution as 0.20 g NaNO3, 0.20 g KH2PO4, 0.20 g NH4Cl, 0.40 g MgCl2 x 6 H2O, 0.20 g KCl, 0.10 g CaCl2 x 2 H2O, 2 ml Trace element solution SL-4, 2.50 g Na2S2O3 x 5 H2O, and 1000 ml distilled water. MediaDive represents the main solution as 1002 ml, so its generated basal `g_l` concentrations are slightly lower than the DSMZ nominal grams per liter because of the 2 ml SL-4 addition.

DSMZ and MediaDive instruct dissolving all ingredients except sodium thiosulfate, sparging with 80% N2 and 20% CO2 for 30-45 min, adjusting pH to 7.0, distributing the medium under the same gas mixture, autoclaving, adding thiosulfate from an anoxic 100% N2 stock sterilized by filtration before inoculation, and pressurizing inoculated culture vessels to 0.5 bar overpressure with sterile 100% H2.

Trace element solution SL-4 is a separate 1 L stock from DSMZ Medium 14. It contains 0.50 g Na2-EDTA, 0.20 g FeSO4 x 7 H2O, 0.10 g ZnSO4 x 7 H2O, 0.03 g MnCl2 x 4 H2O, 0.30 g H3BO3, 0.20 g CoCl2 x 6 H2O, 0.01 g CuCl2 x 2 H2O, 0.02 g NiCl2 x 6 H2O, 0.03 g Na2MoO4 x 2 H2O, and 1000 ml distilled water.

The generated YAML preserves the basal ingredients, thiosulfate, pH 7.0, and the three MediaDive preparation steps. It omits the explicit 2 ml/L Trace element solution SL-4 addition and flattens SL-4 ingredients into the final medium at stock concentrations.

## Completeness

The generated record is incomplete because it lacks the 2 ml/L SL-4 stock addition and the distinct 1 L SL-4 water row. It is also over-complete as a final-medium representation because the SL-4 stock internals are duplicated at top level.

`target_organisms` is absent. The DSMZ and MediaDive recipe metadata reviewed here do not assert growth observations, so no growth target was inferred.

## Findings

- The 2 ml/L Trace element solution SL-4 addition is absent from `ingredients`.
- SL-4 stock ingredients are flattened into top-level final-medium rows at stock `G_PER_L` values.
- The 1 L SL-4 water row is absent.
- `NiCl2 x 6 H2O` lost hydrate-specific grounding.
- The legacy `mediaingredientmech_term` on NaNO3 remains while peer ChEBI-grounded ingredients have `mediaingredientmech_chebi_term`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/sulfuricurvum_mbm_medium.yaml`, `data/normalized_yaml/bacterial/mbm_medium_modified.yaml`, or the DSMZ/KOMODO source resolver, then regenerate `data/merge_yaml/merged/sulfuricurvum_mbm_medium.yaml`.
- Keep DSMZ and KOMODO 1020 merged as source duplicates unless a source difference is found.
- Preserve Trace element solution SL-4 as a nested 1 L stock added to the final medium at 2 ml/L.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific term if one is available.
- Replace the lingering NaNO3 legacy MediaIngredientMech link with the ingredient's own ChEBI link.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:000442`, `mediadive.medium:1020`, `komodo.medium:1020`, `4393eaf9b1726a8511a3e974eda746707d004190f8bf4d184a911bf9158e9312`, `sulfuricurvum_mbm_medium.yaml`, and `mbm_medium_modified.yaml`.
- Recompare the regenerated record against both MediaDive 1020 and the DSMZ Medium 1020 PDF to ensure SL-4 is preserved as a 2 ml/L stock addition.

## Additional Notes

Empty optional fields that are unrelated to source identity, SL-4 stock structure, and source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the MediaDive/DSMZ resolver, KOMODO resolver, and normalized duplicate sources.

# YAML Record Review: Sulfuriflexus Medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfuriflexus_medium__89898fd1.yaml` (`CultureMech:001119`)
- Started UTC: `2026-09-25T08:30:39Z`
- Finished UTC: `2026-09-25T08:30:39Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfuriflexus_medium__89898fd1.yaml` |
| Normalized source | `data/normalized_yaml/bacterial/sulfuriflexus_medium.yaml` |
| CultureMech ID | `CultureMech:001119` |
| Media term | `mediadive.medium:1635` |
| Original source | DSMZ Medium 1635, SULFURIFLEXUS MEDIUM |
| Merge fingerprint | `89898fd1d81b39de5d36c43e176c99be26e65c29737f18fe1c821fa891353cbe` |
| Merged from | `sulfuriflexus_medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` exited 0 with no diagnostics for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` exited 0 after starting validation of the generated YAML. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected `CultureMech:001119` identifier, `mediadive.medium:1635` source term, DSMZ 1635 identity, pH 7.2 value, and merge fingerprint. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:001119`, `mediadive.medium:1635`, the merge fingerprint, and `sulfuriflexus_medium.yaml` found this normalized source and generated merge as the only direct recipe records, with the expected normalized indexes also referencing the same ID and source term.

Several main-solution salts are plausibly grounded, but the stock hierarchy is not represented. Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x) are absent as final-medium additions while their internal ingredients are flattened at top level. `NiCl2 x 6 H2O` is grounded to generic nickel dichloride despite its hydrate-specific source string.

## Evidence

The DSMZ Medium 1635 PDF and MediaDive 1635 list the main solution as 20 g NaCl, 3 g MgCl2 x 6 H2O, 0.3 g MgSO4 x 7 H2O, 0.1 g CaCl2, 0.1 g NH4Cl, 0.1 g KH2PO4, 0.1 g KCl, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, 5 g Na2S2O3 x 5 H2O, 0.4 g NaHCO3, 1 ml Wolin's vitamin solution (10x), and 1000 ml distilled water. MediaDive represents the main solution as 1003 ml, so its generated basal `g_l` concentrations are slightly lower than DSMZ's nominal grams per liter because of the three 1 ml stock additions.

DSMZ and MediaDive instruct dissolving all ingredients except thiosulfate, bicarbonate, and vitamins, adjusting pH to 6.0, dispensing the medium under air into serum vials to 20% volume, closing with rubber septa, autoclaving, adding thiosulfate, vitamins, and bicarbonate from filtered sterile stocks, and adjusting the complete medium to pH 7.2.

DSMZ defines three referenced 1 L stocks: Trace element solution SL-10 with 10 ml 25% HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 990 ml water; Selenite-tungstate solution with 0.50 g NaOH, 3 mg Na2SeO3 x 5 H2O, 4 mg Na2WO4 x 2 H2O, and 1000 ml water; and Wolin's vitamin solution (10x) with milligram-scale vitamins in 1000 ml water.

The generated YAML preserves the basal ingredients, thiosulfate, bicarbonate, pH 7.2, the main preparation step, and the SL-10 preparation step. It omits all three explicit 1 ml/L stock additions and flattens SL-10, Selenite-tungstate, and Wolin's vitamin stock ingredients into final-medium rows at stock concentrations.

## Completeness

The generated record is incomplete because it lacks the 1 ml/L stock additions for SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x), the 1 L stock water rows, and the Selenite-tungstate and vitamin stock preparation scopes. It is over-complete as a final-medium representation because stock internals are duplicated as top-level final ingredients.

`target_organisms` is absent. The DSMZ and MediaDive recipe metadata reviewed here do not assert growth observations, so no growth target was inferred.

## Findings

- The 1 ml/L Trace element solution SL-10 addition is absent from `ingredients`.
- SL-10 stock ingredients are flattened into top-level final-medium rows at stock `G_PER_L` values.
- The 1 ml/L Selenite-tungstate solution addition is absent and its stock ingredients are flattened into top-level final-medium rows.
- The 1 ml/L Wolin's vitamin solution (10x) addition is absent and its vitamin ingredients are flattened into top-level final-medium rows.
- The main 1 L water row and the three stock water rows are all absent.
- Selenite-tungstate and vitamin stock preparation scopes are absent.
- `NiCl2 x 6 H2O` lost hydrate-specific grounding.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/sulfuriflexus_medium.yaml` or the MediaDive/DSMZ resolver, then regenerate `data/merge_yaml/merged/sulfuriflexus_medium__89898fd1.yaml`.
- Keep SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x) as nested 1 L stocks added to the final medium at 1 ml/L each.
- Preserve stock-specific water rows and stock-specific preparation text instead of converting stock internals to final top-level ingredients.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific term if one is available.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:001119`, `mediadive.medium:1635`, `89898fd1d81b39de5d36c43e176c99be26e65c29737f18fe1c821fa891353cbe`, and `sulfuriflexus_medium.yaml`.
- Recompare the regenerated record against both MediaDive 1635 and the DSMZ Medium 1635 PDF to ensure all three nested stock recipes are scoped under the correct 1 ml/L main-solution additions.

## Additional Notes

Empty optional fields that are unrelated to source identity, stock hierarchy, and source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the MediaDive/DSMZ import and normalized source.

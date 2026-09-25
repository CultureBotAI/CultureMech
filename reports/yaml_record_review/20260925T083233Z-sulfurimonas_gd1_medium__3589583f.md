# YAML Record Review: Sulfurimonas GD1 Medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfurimonas_gd1_medium__3589583f.yaml` (`CultureMech:003153`)
- Started UTC: `2026-09-25T08:32:33Z`
- Finished UTC: `2026-09-25T08:32:33Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfurimonas_gd1_medium__3589583f.yaml` |
| Normalized source | `data/normalized_yaml/bacterial/sulfurimonas_gd1_medium.yaml` |
| CultureMech ID | `CultureMech:003153` |
| Media term | `mediadive.medium:J808` |
| Original source | JCM Medium J808, SULFURIMONAS GD1 MEDIUM |
| Merge fingerprint | `3589583f740dd4a59eb98a4e249dc379ea702e77938c28469540d4b70446e665` |
| Merged from | `sulfurimonas_gd1_medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected `CultureMech:003153` identifier, `mediadive.medium:J808` source term, JCM 808 identity, pH 7.3 value, and merge fingerprint. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:003153`, `mediadive.medium:J808`, the merge fingerprint, and `sulfurimonas_gd1_medium.yaml` found this normalized source and generated merge as the only direct recipe records, with the expected normalized indexes also referencing the same ID and source term.

Several basal sea-salt ingredients are plausibly grounded, but the post-autoclave stock hierarchy is not represented. FeCl2 solution, Trace element solution, Trace vitamins, Selenite-tungstate solution, 10% KNO3 solution, and 10% Na2S2O3 x 5 H2O solution are absent as stock additions while their internal ingredients are flattened at top level. `KNO3` still carries a legacy `MediaIngredientMech` link, and `NiCl2 x 6 H2O` is grounded to generic nickel dichloride despite its hydrate-specific source string.

## Evidence

The live JCM 808 page and MediaDive J808 list a 1 L basal solution with 5.5 g NaCl, 2.28 g MgCl2 x 6 H2O, 0.34 g CaCl2 x 2 H2O, 0.15 g KCl, 0.91 g Na2SO4, 0.20 g NaHCO3, 0.023 g KBr, 5.7 mg H3BO3, 9.1 mg SrCl2 x 6 H2O, 4.9 mg NH4Cl, 1.2 mg KH2PO4, 0.67 mg NaF, 2.38 g HEPES, and 1 L distilled water. MediaDive represents the final solution as 1033 ml after stock additions, so its generated basal `g_l` values are lower than the source table's nominal amounts.

JCM's second table adds 1 ml FeCl2 solution, 1 ml Trace element solution, 10 ml Trace vitamins, 1 ml Selenite-tungstate solution, 10 ml 10% KNO3 solution, and 10 ml 10% Na2S2O3 x 5 H2O solution from anaerobic filter-sterilized stocks after the basal medium is bubbled with N2, sealed with butyl rubber stoppers, autoclaved, and cooled.

MediaDive expands FeCl2 solution as a 1 L stock containing 10 ml 25% HCl, 1.5 g FeCl2 x 4 H2O, and 990 ml distilled water; Trace element solution as a 1 L stock with milligram-scale ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O; Trace vitamins as a 1 L stock with milligram-scale vitamins; and Selenite-tungstate as a 1 L stock with 0.4 g NaOH, 6 mg Na2SeO3 x 5 H2O, and 8 mg Na2WO4 x 2 H2O.

The generated YAML preserves the basal rows, pH 7.3, and the start of the JCM preparation text. It flattens the six post-autoclave additions into top-level final-medium ingredients, represents the two 10 ml 10% stock additions as `10 G_PER_L`, sums the basal and trace-stock H3BO3 into one row, and truncates the preparation text before the source's post-autoclave addition table.

## Completeness

The generated record is incomplete because it lacks the six post-autoclave stock-addition rows, the stock water rows, and the full anaerobic-stock addition table. It is over-complete as a final-medium representation because FeCl2, trace-element, trace-vitamin, selenite-tungstate, KNO3, and thiosulfate stock internals are duplicated at top level.

`target_organisms` is absent. The MediaDive and JCM recipe metadata reviewed here do not assert growth observations, so no growth target was inferred.

## Findings

- The post-autoclave 1 ml FeCl2 solution addition is absent and its internal HCl and FeCl2 x 4 H2O stock rows are flattened.
- The 1 ml Trace element solution addition is absent and its internal trace rows are flattened.
- The 10 ml Trace vitamins addition is absent and its internal vitamin rows are flattened.
- The 1 ml Selenite-tungstate solution addition is absent and its internal NaOH, selenite, and tungstate rows are flattened.
- The 10 ml 10% KNO3 and 10 ml 10% Na2S2O3 x 5 H2O stock additions are absent and are represented as `10 G_PER_L` final rows.
- The basal H3BO3 row and trace-stock H3BO3 row are merged into one top-level ingredient.
- The basal and stock water rows are absent.
- The preparation step is truncated before the JCM post-autoclave stock table.
- `KNO3` still has a legacy MediaIngredientMech link.
- `NiCl2 x 6 H2O` lost hydrate-specific grounding.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/sulfurimonas_gd1_medium.yaml` or the JCM/MediaDive resolver, then regenerate `data/merge_yaml/merged/sulfurimonas_gd1_medium__3589583f.yaml`.
- Keep the FeCl2 solution, Trace element solution, Trace vitamins, Selenite-tungstate solution, 10% KNO3, and 10% Na2S2O3 x 5 H2O additions as stock rows rather than flattening their internals into the final medium.
- Preserve source-scoped water and H3BO3 rows instead of summing basal and stock scopes.
- Preserve the full JCM post-autoclave stock-addition table in preparation or structured solution metadata.
- Replace the lingering KNO3 legacy MediaIngredientMech link with the ingredient's own ChEBI link.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific term if one is available.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:003153`, `mediadive.medium:J808`, `3589583f740dd4a59eb98a4e249dc379ea702e77938c28469540d4b70446e665`, and `sulfurimonas_gd1_medium.yaml`.
- Recompare the regenerated record against both MediaDive J808 and the live JCM 808 page to ensure the six anaerobic post-autoclave additions remain distinct.

## Additional Notes

Empty optional fields that are unrelated to source identity, stock hierarchy, and source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the JCM/MediaDive import and normalized source.

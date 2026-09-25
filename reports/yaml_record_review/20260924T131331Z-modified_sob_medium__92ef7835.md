# YAML Record Review: modified_sob_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_sob_medium__92ef7835.yaml
- Started UTC: 2026-09-24T13:12:41Z
- Finished UTC: 2026-09-24T13:13:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| CultureMech ID | CultureMech:002770 |
| Name | modified_sob_medium |
| Original name | MODIFIED SOB MEDIUM |
| Category | bacterial |
| Source identity | mediadive.medium:J414, JCM Medium 414 |
| Generated status | Generated canonical merge under `data/merge_yaml/merged/`; future fixes belong in `data/normalized_yaml/bacterial/modified_sob_medium.yaml` or the JCM/MediaDive import rules. |

An ignored-file-inclusive exact search for `CultureMech:002770`, `mediadive.medium:J414`, `modified_sob_medium`, `GRMD=414`, and `JCM Medium J414` under `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found this generated merge, its maintained JCM owner, catalog/index rows, aggregate QA rows, and a separate TOGO M412 branch that cites the same JCM `GRMD=414` page. The reviewed generated record is a singleton merge from `modified_sob_medium`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, Python 3.11 `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_sob_medium__92ef7835.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator, Python 3.11 `scripts/validate_strict.py data/merge_yaml/merged/modified_sob_medium__92ef7835.yaml --out /private/tmp/modified_sob_medium__92ef7835.strict.tsv --workers 1 --quiet` | Passed. TSV contained only the header row, so there were 0 strict errors. |
| Reference validator, Python 3.11 `linkml-reference-validator validate data data/merge_yaml/merged/modified_sob_medium__92ef7835.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the checker reported 0 reference checks. |
| Term validator, Python 3.11 `linkml-term-validator validate-data data/merge_yaml/merged/modified_sob_medium__92ef7835.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone YAML under `history/`, not inline `MediaRecipe.curation_history` entries. |

## Identity and Grounding

The record identity is correct: the inspected JCM page for medium 414 is titled `MODIFIED SOB MEDIUM` and is the source linked from the YAML. The category and liquid/defined classification are reasonable for this mineral recipe.

The ingredient identity is only partially grounded to the source. Main-medium salts, the NaHCO3 addition, and the named trace-metal solution all appear on the JCM page, but the generated record treats stock-solution components as final-medium rows. Hydrated forms for calcium chloride, magnesium chloride, zinc sulfate, cobalt chloride, iron sulfate, and copper sulfate are grounded exactly. `(NH4)6Mo7O24 x 4 H2O` has a primary term for generic ammonium molybdate, so the tetrahydrate form is not yet fully exact.

## Evidence

The JCM page supports a main recipe containing 1.0 g KH2PO4, 1.0 g K2HPO4, 1.0 g NH4Cl, 0.1 g CaCl2 x 2 H2O, 0.2 g MgCl2 x 6 H2O, 1.55 g Na2S2O3 x 5 H2O, 1.0 ml trace metal solution, and 2.0 g NaHCO3. The YAML inflates each main-recipe gram amount by 1000 when storing it as `G_PER_L`: for example, KH2PO4 is `1000 G_PER_L`, Na2S2O3 x 5 H2O is `1550 G_PER_L`, and NaHCO3 is `2000 G_PER_L`.

The JCM page defines `Trace metal solution` separately in 1 L water. The YAML flattens that stock recipe into final-medium ingredients and then sums CaCl2 x 2 H2O and MgCl2 x 6 H2O across the final medium and the stock recipe.

The final medium is adjusted to pH 7.0 with HCl if necessary. The trace metal solution is adjusted to pH 6.0, but the YAML promotes that stock pH to top-level `ph_value: 6.0` and appends an `ADJUST_PH` step that is no longer scoped to the trace stock.

## Completeness

The main consequential gap is structural: the record is missing a trace-metal stock solution with its own 1 L basis and pH 6.0 adjustment. Without that boundary, the record cannot represent the 1 ml/l trace-metal solution addition or keep stock concentrations out of the final medium.

The JCM page does not assert strain-specific growth evidence, so the empty `target_organisms` and `growth_evidence` slots are acceptable. No record-local discussion flags are required beyond the stock-solution import defects listed below.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Main-medium gram quantities are inflated by 1000x. | JCM 414 lists KH2PO4, K2HPO4, and NH4Cl as 1.0 g each, CaCl2 x 2 H2O as 0.1 g, MgCl2 x 6 H2O as 0.2 g, Na2S2O3 x 5 H2O as 1.55 g, and NaHCO3 as 2.0 g; the YAML stores those as 1000, 1000, 1000, 100, 200, 1550, and 2000 g/l before duplicate merging. | `data/normalized_yaml/bacterial/modified_sob_medium.yaml`; JCM/MediaDive unit normalization. |
| major | The trace metal solution was flattened into final-medium ingredients. | JCM adds `Trace metal solution (see below)` at 1.0 ml, then separately defines a 1 L trace stock containing Na2-EDTA, ZnSO4 x 7 H2O, CaCl2 x 2 H2O, MgCl2 x 6 H2O, CoCl2 x 6 H2O, ammonium molybdate tetrahydrate, FeSO4 x 7 H2O, CuSO4 x 5 H2O, and NaOH. All stock components are top-level YAML ingredients. | `data/normalized_yaml/bacterial/modified_sob_medium.yaml`; JCM trace-solution extraction. |
| major | Same-named final-medium and trace-stock salts were summed across stock boundaries. | Import QA flags `CaCl2 x 2 H2O` as 107.3 g/l from 100.0 and 7.3, and `MgCl2 x 6 H2O` as 202.5 g/l from 200.0 and 2.5. The smaller parts come from the trace metal solution, not the final medium. | `data/normalized_yaml/bacterial/modified_sob_medium.yaml`; duplicate-row cleanup should respect solution scope. |
| major | The top-level pH value belongs to the trace stock, not the final medium. | JCM says to adjust the final medium to pH 7.0 with HCl if necessary and separately says to adjust the trace metal solution to pH 6.0. The YAML has top-level `ph_value: 6.0` and an unscoped `Adjust pH to 6.0` preparation step. | `data/normalized_yaml/bacterial/modified_sob_medium.yaml`; JCM pH/preparation extraction. |
| minor | `(NH4)6Mo7O24 x 4 H2O` is under-grounded. | The source names ammonium molybdate tetrahydrate, while the YAML primary term label is generic `ammonium molybdate` and the row has no `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/modified_sob_medium.yaml`; ChEBI enrichment or manual ingredient grounding. |

No blocker findings.

## Recommended Edits

1. Re-import the JCM 414 main recipe with gram amounts preserved as grams per liter rather than multiplied by 1000.
2. Model `Trace metal solution` as a stock solution added at `1 ML_PER_L`, with EDTA, ZnSO4 x 7 H2O, CaCl2 x 2 H2O, MgCl2 x 6 H2O, CoCl2 x 6 H2O, ammonium molybdate tetrahydrate, FeSO4 x 7 H2O, CuSO4 x 5 H2O, NaOH, and 1 L water scoped to that stock.
3. Undo the cross-scope CaCl2 x 2 H2O and MgCl2 x 6 H2O duplicate sums after the stock solution boundary is restored.
4. Move the pH 6.0 adjustment into the trace-metal stock preparation and represent the final-medium pH as 7.0, scoped to the HCl adjustment note.
5. Ground `(NH4)6Mo7O24 x 4 H2O` to an exact tetrahydrate ChEBI term or leave it explicitly unresolved if no exact term exists.
6. Compare this JCM/MediaDive branch with TOGO M412 after correction; both cite `GRMD=414` and should be reconciled as source duplicates if their corrected formulations match.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the corrected normalized branch and regenerated `data/merge_yaml/merged/modified_sob_medium__92ef7835.yaml`.
- Re-run the duplicate-ingredient QA that emits `data/import_tracking/reports/merged_duplicates.tsv` and confirm `CultureMech:002770` no longer has `DIFFERING_PARTS` rows for CaCl2 x 2 H2O or MgCl2 x 6 H2O.
- Re-run concentration plausibility QA and confirm the 1000x main salts and trace-metal stock rows no longer appear as final-medium outliers.
- Re-inspect the regenerated YAML against the JCM 414 page and verify only eight main-medium rows remain at top level, the trace-metal stock is nested, and the pH 6.0 instruction is scoped to that stock.

## Additional Notes

`data/normalized_yaml/bacterial/TOGO_M412_Modified_SOB_Medium.yaml` is another `modified_sob_medium` import from the same JCM `GRMD=414` page, but it has a different fingerprint and was generated separately as `data/merge_yaml/merged/MODIFIED_SOB_MEDIUM.yaml`. I did not review that sibling as part of this singleton MediaDive merge.

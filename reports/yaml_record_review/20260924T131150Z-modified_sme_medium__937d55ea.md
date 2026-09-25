# YAML Record Review: modified_sme_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_sme_medium__937d55ea.yaml
- Started UTC: 2026-09-24T13:10:50Z
- Finished UTC: 2026-09-24T13:11:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| CultureMech ID | CultureMech:001664 |
| Name | modified_sme_medium |
| Original name | MODIFIED SME MEDIUM |
| Category | bacterial |
| Source identity | mediadive.medium:534, DSMZ Medium 534 |
| Generated status | Generated canonical merge under `data/merge_yaml/merged/`; future fixes belong in `data/normalized_yaml/bacterial/modified_sme_medium.yaml`, its MediaDive importer, or stock-solution import/merge logic. |

An ignored-file-inclusive exact search for `937d55ea`, `CultureMech:001664`, `CultureMech:005912`, `mediadive.medium:534`, `komodo.medium:534`, and `KOMODO_534_MODIFIED_SME_MEDIUM` under `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found this MediaDive-derived generated record, its maintained normalized owner, and a separate KOMODO 534 branch generated as `data/merge_yaml/merged/MODIFIED_SME_MEDIUM.yaml`. The current reviewed record is a singleton merge from `modified_sme_medium`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, Python 3.11 `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_sme_medium__937d55ea.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator, Python 3.11 `scripts/validate_strict.py data/merge_yaml/merged/modified_sme_medium__937d55ea.yaml --out /private/tmp/modified_sme_medium__937d55ea.strict.tsv --workers 1 --quiet` | Passed. TSV contained only the header row, so there were 0 strict errors. |
| Reference validator, Python 3.11 `linkml-reference-validator validate data data/merge_yaml/merged/modified_sme_medium__937d55ea.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the checker reported 0 reference checks. |
| Term validator, Python 3.11 `linkml-term-validator validate-data data/merge_yaml/merged/modified_sme_medium__937d55ea.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone YAML under `history/`, not inline `MediaRecipe.curation_history` entries. |

## Identity and Grounding

The record denotes the right medium: DSMZ Medium 534 is `MODIFIED SME MEDIUM`, a liquid defined recipe adjusted to pH 6.5-6.8. The source PDF supports the main salts, 10 ml/l DSMZ trace element solution 141, post-autoclave solution A and solution B additions, the H2/CO2/O2 headspace, and the basic anaerobic preparation sequence.

Most hydrated-salt ChEBI groundings that are present match the labels. `NiCl2 x 6 H2O` is over-broadly grounded to generic `CHEBI:34887` / nickel dichloride instead of a hexahydrate. `Na2SeO4` still carries a deprecated legacy `mediaingredientmech_term` even though the row's primary ChEBI term is sodium selenate.

## Evidence

The inspected DSMZ PDF states the main salts directly, then adds `Trace element solution (see medium 141)` at 10 ml/l. It does not list the complete medium-141 trace solution as top-level final-medium material, so the flattened trace rows and duplicate sums are not source-faithful.

The PDF also defines two concentrated post-autoclave supplements: solution A is 2 g NaHCO3 in 30 ml water, and solution B is 2 g Na2S2O3 x 5 H2O in 30 ml water. The protocol adds only 0.3 ml of each stock to 10 ml medium. The YAML instead stores both stock concentrations, `66.6667 G_PER_L`, as top-level final-medium concentrations.

The preparation steps preserve much of the DSMZ protocol, including nitrogen sparging, pH adjustment, serum-bottle filling, autoclaving, filter-sterilized solution additions, gas exchange, and a trace-solution note. The top-level `ph_value: 6.6` is less exact than the DSMZ pH range of 6.5-6.8.

## Completeness

The record is missing explicit stock-solution structure for DSMZ trace element solution 141, solution A, and solution B. That omission causes the inflated final-medium ingredient list and loses the dilution boundary around the post-autoclave additions.

`target_organisms`, `growth_evidence`, and `discussion` are empty. Those empty optional fields are acceptable here: DSMZ Medium 534 is a source recipe, and the source PDF does not assert a target organism for this particular CultureMech record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | DSMZ trace element solution 141 was flattened into the final medium and merged with same-named main-medium salts. | DSMZ 534 adds 10 ml/l trace element solution 141. The YAML instead has top-level rows for medium-141 constituents and already sums `NaCl` 30.0 + 1.0 into 31.0 g/l, `MgSO4 x 7 H2O` 7.0 + 3.0 into 10.0 g/l, and `CaCl2 x 2 H2O` 0.5 + 0.1 into 0.6 g/l. | `data/normalized_yaml/bacterial/modified_sme_medium.yaml`; MediaDive solution import and duplicate-row cleanup. |
| major | Solution A and solution B are modeled as final-medium grams per liter rather than as 0.3 ml/10 ml stock additions. | The DSMZ PDF defines each stock as 2 g in 30 ml water and adds 0.3 ml of stock to 10 ml medium. The YAML rows `NaHCO3` and `Na2S2O3 x 5 H2O` both use the stock concentration, `66.6667 G_PER_L`, as if it were the final concentration. | `data/normalized_yaml/bacterial/modified_sme_medium.yaml`; MediaDive stock-solution extraction. |
| major | Trace-solution additives for medium 141 are attached at stock strength to the final medium. | DSMZ says to add `(NH4)2Ni(SO4)2`, `Na2WO4`, and `Na2SeO4` to 1000 ml trace element solution in medium 141; the final recipe adds only 10 ml/l of that trace solution. The YAML stores those additives as top-level final-medium rows. | `data/normalized_yaml/bacterial/modified_sme_medium.yaml`; MediaDive nested-stock modeling. |
| major | `NiCl2 x 6 H2O` is grounded to generic nickel dichloride. | The ingredient label explicitly names a hexahydrate, but both primary `term` and `mediaingredientmech_chebi_term` point to `CHEBI:34887` / nickel dichloride. | `data/normalized_yaml/bacterial/modified_sme_medium.yaml`; ChEBI enrichment or manual ingredient grounding. |
| minor | The DSMZ pH range was collapsed to an unsupported scalar. | DSMZ gives an adjustment range of pH 6.5-6.8; the YAML has `ph_value: 6.6`. | `data/normalized_yaml/bacterial/modified_sme_medium.yaml`; MediaDive pH extraction. |
| minor | `Na2SeO4` still uses a deprecated legacy MediaIngredientMech identifier field. | The row has correct primary grounding to `CHEBI:77775` but keeps `mediaingredientmech_term: MediaIngredientMech:000198` after the 2026-06-05 migration replaced 23 other legacy links. | `data/normalized_yaml/bacterial/modified_sme_medium.yaml`; MediaIngredientMech-to-ChEBI migration. |

No blocker findings.

## Recommended Edits

1. Model DSMZ trace element solution 141 as a stock reference/addition instead of flattening medium 141 into the final ingredient list.
2. Model solution A and solution B as separately prepared stocks dosed at 0.3 ml per 10 ml medium; do not keep their 66.6667 g/l stock strengths as final-medium `NaHCO3` and `Na2S2O3 x 5 H2O` concentrations.
3. Keep the three additions to trace element solution 141 within that trace-stock scope, then recalculate or preserve the correct 10 ml/l final addition boundary.
4. Correct `NiCl2 x 6 H2O` to an exact hexahydrate ChEBI term or leave it explicitly unresolved if no exact ChEBI class is available.
5. Represent pH as a 6.5-6.8 range.
6. Migrate the `Na2SeO4` MediaIngredientMech link to `mediaingredientmech_chebi_term` keyed to `CHEBI:77775`.
7. Compare the MediaDive and KOMODO DSMZ-534 branches after correction; if they still describe the same source recipe, mark the KOMODO record as a source duplicate or merge the generated output.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the corrected normalized branch and regenerated `data/merge_yaml/merged/modified_sme_medium__937d55ea.yaml`.
- Re-run the duplicate-ingredient QA that emits `data/import_tracking/reports/merged_duplicates.tsv` and confirm `CultureMech:001664` no longer has `DIFFERING_PARTS` rows for `NaCl`, `MgSO4 x 7 H2O`, or `CaCl2 x 2 H2O`.
- Re-inspect the regenerated record against the DSMZ PDF and verify only the main salts are top-level final-medium ingredients, solution A/B doses are explicit, and trace element solution 141 remains separated from final-medium quantities.
- Re-check `data/merge_yaml/merged/MODIFIED_SME_MEDIUM.yaml` so the KOMODO DSMZ-534 duplicate is not left as an independent generated recipe when its source is the same DSMZ formulation.

## Additional Notes

The maintained KOMODO 534 branch carries the same flattened DSMZ composition and the same duplicate-salt sums, plus a variable `H2SO4` ingredient extracted from the pH-adjustment note. It has the same scientific ownership problem as this MediaDive branch, but it is not part of the `937d55ea` singleton merge.

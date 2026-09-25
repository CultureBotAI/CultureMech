# YAML Record Review: korthofs_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/korthofs_medium.yaml
- Started UTC: 2026-09-23T17:53:49Z
- Finished UTC: 2026-09-23T17:54:31Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:010421`, the generated `korthofs_medium` record merged from `data/normalized_yaml/bacterial/TOGO_M993_Korthof_s_Medium.yaml`. The record represents TOGO `M993`, JCM `M946`, "Korthof's Medium", as a bacterial, complex, undefined, liquid medium.

## Validation

- LinkML open schema validation passed for `data/merge_yaml/merged/korthofs_medium.yaml`.
- Strict validation passed with 0 error rows in `/private/tmp/korthofs_medium.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` entries were not checked: the available history validator validates standalone files under `history/`, not embedded generated YAML history.

## Identity and Grounding

An ignored-inclusive exact search for `CultureMech:010421`, `TOGO:M993`, `TOGO_M993_Korthof_s_Medium`, `JCM_M946`, and `GRMD=946` found the TOGO owner plus a direct JCM duplicate at `data/normalized_yaml/bacterial/korthofs_medium.yaml` and `data/merge_yaml/merged/korthofs_medium__bfaea4a7.yaml`.

Both records are grounded to JCM 946 and should be reconciled after their 10x basal-stock representation is repaired.

## Evidence

JCM 946 lists the final medium as 50 ml 10x Korthof's basal medium, 50 ml rabbit serum heat-inactivated at 56 C for 30 min, and 400 ml distilled water. Distilled water is autoclaved, cooled, and aseptically combined with filter-sterilized heat-inactivated rabbit serum and the 10x Korthof basal medium. The 10x basal stock is made from NaCl, Na2HPO4, Polypeptone peptone, KH2PO4, NaHCO3, KCl, 0.2 g CaCl2.2H2O prepared in a separate 50 ml filtered solution, and 450 ml distilled water.

## Completeness

The generated record has the final serum and basal-medium labels plus the basal salts, but it does not preserve the two nested solution boundaries or either source preparation step.

## Findings

- Distinct water amounts from the final medium, 10x basal stock, and CaCl2 stock were summed into one `Distilled water` row with `900.0 G_PER_L`. `data/import_tracking/reports/merged_duplicates.tsv` independently flags this as a `DIFFERING_PARTS` water merge.
- `Rabbit serum heat--inactivated at 56&#8451; for 30 min` is 50 ml in the 500 ml final recipe, but the generated row stores `50 G_PER_L`.
- `10 x Korthof's basal medium` is a 50 ml final-medium addition, but it is stored as a mass concentration and the stock itself is not structured.
- The 10x basal ingredients are flattened into top-level final-medium rows without the 10x dilution. For example, the 7 g NaCl stock row is stored as `7 G_PER_L` final medium rather than being scoped to the 10x basal stock.
- `CaCl2 solution` is an empty `Unknown solution` with `50 G_PER_L`, and its 0.2 g CaCl2.2H2O stock solute is also flattened as a top-level ingredient.
- The source autoclaving, cooling, filter sterilization, and post-autoclave serum/CaCl2 additions are absent.
- The direct JCM duplicate should not be merged mechanically; it is grounded to the same JCM page but computes basal-salt concentrations over the 450 ml basal-water volume rather than preserving the 10x basal stock.

## Recommended Edits

- Rebuild `TOGO_M993_Korthof_s_Medium.yaml` around the final 500 ml assembly, the 10x Korthof basal stock, and the 50 ml filtered CaCl2 solution.
- Store rabbit serum as a 50 ml addition with its heat-inactivation and filter-sterilization requirements.
- Keep the CaCl2 stock inside the 10x basal medium, not as a top-level final-medium ingredient.
- Restore the JCM preparation sequence for autoclaving water, separately preparing the 10x basal stock, and adding sterile CaCl2 and rabbit serum after cooling.
- Repair and deduplicate the direct JCM owner after both imports preserve the same source structure.

## Follow-up Checks

- Re-run the open schema, strict, reference, and term validators against regenerated Korthof.
- Confirm the `DIFFERING_PARTS` water row for `TOGO_M993_Korthof_s_Medium.yaml` disappears from import tracking after repair.
- Confirm the TOGO and direct JCM owners for JCM 946 produce one generated Korthof's Medium record.

## Additional Notes

The exact search included ignored files and hidden files.

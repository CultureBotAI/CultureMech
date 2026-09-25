# YAML Record Review: korthofs_medium__bfaea4a7

- Repository: CultureMech
- Record: data/merge_yaml/merged/korthofs_medium__bfaea4a7.yaml
- Started UTC: 2026-09-23T17:55:10Z
- Finished UTC: 2026-09-23T17:55:31Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:003294`, the generated `korthofs_medium__bfaea4a7` record merged from `data/normalized_yaml/bacterial/korthofs_medium.yaml`. The record represents MediaDive/JCM `J946`, "KORTHOF'S MEDIUM", as a bacterial, complex, undefined, liquid medium.

## Validation

- LinkML open schema validation passed for `data/merge_yaml/merged/korthofs_medium__bfaea4a7.yaml`.
- Strict validation passed with 0 error rows in `/private/tmp/korthofs_medium__bfaea4a7.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` entries were not checked: the available history validator validates standalone files under `history/`, not embedded generated YAML history.

## Identity and Grounding

An ignored-inclusive exact search for `CultureMech:003294`, `mediadive.medium:J946`, and `GRMD=946` found the direct JCM owner, this generated record, and the TOGO/JCM duplicate at `data/normalized_yaml/bacterial/TOGO_M993_Korthof_s_Medium.yaml` and `data/merge_yaml/merged/korthofs_medium.yaml`.

Both records are grounded to JCM 946 and should be reconciled after their 10x basal-stock representation is repaired.

## Evidence

JCM 946 lists the final medium as 50 ml 10x Korthof's basal medium, 50 ml rabbit serum heat-inactivated at 56 C for 30 min, and 400 ml distilled water. Distilled water is autoclaved, cooled, and aseptically combined with filter-sterilized heat-inactivated rabbit serum and the 10x Korthof basal medium. The 10x basal stock is made from 450 ml distilled water, NaCl, Na2HPO4, Polypeptone peptone, KH2PO4, NaHCO3, KCl, and 0.2 g CaCl2.2H2O prepared as a separate 50 ml filtered solution.

## Completeness

This generated record has preparation text from both the final medium and the basal stock, but it drops the final 400 ml water row, the 10x basal-medium addition, the basal-water row, and the calcium chloride stock boundary.

## Findings

- The 10x Korthof basal stock was flattened into final-medium ingredients. `NaCl`, `Na2HPO4`, `Polypeptone`, `KH2PO4`, `NaHCO3`, `KCl`, and `CaCl2 x 2 H2O` should be scoped to the 10x basal stock instead of the final recipe.
- The basal ingredient concentrations appear to be computed over the 450 ml basal-water row, producing values such as `15.5556 G_PER_L` NaCl from 7 g NaCl divided by 0.45 L; those are neither the source's stock rows nor final-medium concentrations.
- The 50 ml heat-inactivated rabbit serum addition is represented as `50 G_PER_L` rather than a volume addition.
- The 400 ml final-water row, 450 ml basal-water row, and 50 ml CaCl2-stock water row are all absent.
- The separate filtered CaCl2 stock solution is lost even though the JCM preparation text requires CaCl2 to be filter-sterilized and added after basal-stock autoclaving.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/korthofs_medium.yaml` around the final 500 ml assembly, the 10x Korthof basal stock, and the 50 ml filtered CaCl2 solution.
- Preserve rabbit serum as a 50 ml heat-inactivated, filter-sterilized addition.
- Keep basal stock concentrations scoped to the 10x Korthof basal solution.
- Repair and deduplicate the TOGO owner after both imports preserve the same JCM 946 structure.

## Follow-up Checks

- Re-run the open schema, strict, reference, and term validators against regenerated Korthof.
- Confirm the generated JCM and TOGO Korthof owners have matching structured fingerprints.
- Confirm only one generated Korthof's Medium record remains for JCM 946 after deduplication.

## Additional Notes

The exact search included ignored files and hidden files.

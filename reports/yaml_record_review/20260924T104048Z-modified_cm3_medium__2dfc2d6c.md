# YAML Record Review: modified_cm3_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_cm3_medium__2dfc2d6c.yaml
- Started UTC: 2026-09-24T10:39:59Z
- Finished UTC: 2026-09-24T10:40:48Z
- Verdict: needs curation

## Target

Generated record `CultureMech:003170` for JCM/MediaDive medium `J826`, `MODIFIED CM3 MEDIUM`.

The generated record merges `modified_cm3_medium` from `data/normalized_yaml/bacterial/modified_cm3_medium.yaml`. The generated YAML was compared with the maintained owner, JCM medium 826, MediaDive medium `J826`, and JCM medium 187 for the FeCl2 and trace-element stock formulae.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed; `/private/tmp/modified_cm3_medium__2dfc2d6c.strict.tsv` contained only the header row.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct JCM/MediaDive medium identity and final pH 7.0.

The source itself prints `(NH4)2S4`, but the generated row grounds that label to `CHEBI:62946` ammonium sulfate, which corresponds to `(NH4)2SO4` and is not textually compatible with the source label. `NiCl2 x 6 H2O` is also grounded only to generic `CHEBI:34887` nickel dichloride.

## Evidence

JCM 826 lists 1 ml `FeCl2 solution` and 1 ml `Trace element solution` from JCM 187 in the main pre-autoclave recipe, followed by 950 ml distilled water. JCM 187 defines FeCl2 solution as 10 ml 25% HCl, 1.5 g `FeCl2 x 4 H2O`, and 990 ml distilled water, and defines Trace element solution as milligram-scale zinc, manganese, borate, cobalt, copper, nickel, and molybdate salts in 1 L distilled water.

JCM 826 then instructs the curator to adjust the base to pH 6.0, autoclave under N2, and after cooling add 50 ml of a 10% glucose solution that was filter-sterilized and stored under N2. The generated record instead has a direct 50 g/L glucose row and only a prose note that says a solution is added.

The generated record omits the 950 ml main distilled-water row and both stock water rows, flattens the FeCl2 solution and Trace element solution into top-level final-medium ingredients at stock concentrations, and preserves MediaDive's `Na2CO2` typo in the final pH adjustment where JCM 826 prints `Na2CO3`.

## Completeness

The record preserves the JCM 826 identity, final pH, most main medium salt rows, the N2 autoclave context, and the pH 6.0 and pH 7.0 prose.

It is incomplete for nested stocks, water rows, and the post-autoclave glucose addition. It also carries incompatible chemical grounding for `(NH4)2S4` and a carbonate typo in the final preparation step.

## Findings

- High: FeCl2 solution and Trace element solution are flattened into final-medium rows instead of being represented as two 1 ml stock additions.
- High: The 50 ml post-autoclave 10% glucose solution is represented as 50 g/L direct glucose.
- Medium: The 950 ml main water row, the 990 ml FeCl2-solution water row, and the 1 L trace-element water row are missing.
- Medium: The final pH adjustment says `Na2CO2` even though the JCM source says `Na2CO3`.
- Low: `(NH4)2S4` is grounded to ammonium sulfate despite the formula mismatch, and `NiCl2 x 6 H2O` is grounded only to generic nickel dichloride.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/modified_cm3_medium.yaml` or the MediaDive importer so JCM 826 keeps FeCl2 solution and Trace element solution as separate stock recipes with 1 ml additions.
- Restore all three distilled-water rows from JCM 826 and JCM 187.
- Replace the direct 50 g/L glucose row with a 50 ml addition of 10% glucose solution after autoclaving under N2.
- Correct the final pH adjustment to 5% `Na2CO3` solution.
- Review `(NH4)2S4` against the underlying source and remove the ammonium sulfate grounding unless the source label is confirmed to be a typo.
- Ground `NiCl2 x 6 H2O` to a hydrate-specific term when an exact public identifier is available.
- Regenerate `data/merge_yaml/merged/modified_cm3_medium__2dfc2d6c.yaml` after the maintained owner or importer is repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated record against JCM 826 and JCM 187 to verify the two 1 ml stock additions, the 50 ml glucose addition, water rows, and the final 5% `Na2CO3` text.
- Confirm that top-level final ingredients no longer contain `HCl`, `FeCl2 x 4 H2O`, `ZnCl2`, `MnCl2 x 4 H2O`, `H3BO3`, `CoCl2 x 6 H2O`, `CuCl2 x 2 H2O`, `NiCl2 x 6 H2O`, or `Na2MoO4 x 2 H2O` rows from the trace stocks.

## Additional Notes

None found.

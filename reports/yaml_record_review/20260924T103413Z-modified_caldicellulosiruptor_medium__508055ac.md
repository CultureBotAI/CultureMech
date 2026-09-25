# YAML Record Review: modified_caldicellulosiruptor_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_caldicellulosiruptor_medium__508055ac.yaml
- Started UTC: 2026-09-24T10:33:19Z
- Finished UTC: 2026-09-24T10:34:13Z
- Verdict: needs curation

## Target

Generated record `CultureMech:003316` for JCM/MediaDive medium `J968`, `MODIFIED CALDICELLULOSIRUPTOR MEDIUM`.

The generated record merges `modified_caldicellulosiruptor_medium` from `data/normalized_yaml/bacterial/modified_caldicellulosiruptor_medium.yaml`. The maintained owner was compared with the generated record, JCM medium 968, MediaDive REST medium `J968`, MediaDive REST solution `4178`, and JCM medium 433, which is the upstream JCM page for Trace element solution SL-10.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed; `/private/tmp/modified_caldicellulosiruptor_medium__508055ac.strict.tsv` contained only the header row.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The media identity is grounded to `mediadive.medium:J968` and matches JCM medium 968.

Most small-molecule rows are compatible with the JCM and MediaDive labels, but `NiCl2 x 6 H2O` is grounded to generic `CHEBI:34887` nickel dichloride rather than a hexahydrate-specific term. The source qualifiers for `Trypticase peptone (BD-BBL)` and `Yeast extract (BD-Difco)` were also dropped during import.

## Evidence

JCM medium 968 and MediaDive `J968` list a main solution containing 1.0 ml `Trace element solution SL-10`, 2.5 mg `FeCl3 x 6 H2O`, 1.0 g `Xylose`, 0.75 g `L-Cysteine HCl x H2O`, 0.5 mg `Resazurin`, and 1.0 L distilled water. The generated record has direct ingredient rows for `FeCl3 x 6 H2O`, xylose, cysteine, and resazurin, but it omits the 1.0 ml SL-10 addition and the 1.0 L distilled-water row.

JCM medium 433 and MediaDive solution `4178` define Trace element solution SL-10 as a separate 1000 ml stock with 10 ml `HCl (25%, 7.7 M)`, 1.5 g `FeCl2 x 4 H2O`, milligram-scale zinc, manganese, borate, cobalt, copper, nickel, and molybdate salts, and 990 ml distilled water. Those stock rows are flattened into the generated top-level `ingredients` list with stock concentrations, so 1 ml of SL-10 per liter is represented as if the final medium contained 2.5 g/L HCl and 1.5 g/L ferrous chloride tetrahydrate.

The JCM and MediaDive preparation text says to mix everything except xylose, adjust to pH 7.2, distribute under 100% N2, seal with butyl rubber stoppers, autoclave, and add xylose afterward from a filtered anoxic stock prepared under N2. The generated `preparation_steps` retain that prose, but xylose remains a plain ingredient row and the filtered anoxic stock addition is not modeled structurally.

## Completeness

The record preserves the JCM/MediaDive medium identifier, name, pH 7.2, the main non-stock chemical rows, the SL-10 preparation prose, and the overall anaerobic/autoclave/xylose-addition prose.

It is incomplete for nested solution boundaries and explicit waters. The main distilled water and SL-10 distilled water rows are absent, the 1.0 ml SL-10 addition is absent, the SL-10 stock recipe is promoted to the final medium, and xylose loses its post-autoclave stock/addition context.

## Findings

- High: Trace element solution SL-10 is flattened into final-medium ingredients. This changes a nested 1.0 ml stock addition into undiluted stock concentrations in the final medium.
- Medium: The 1.0 L main distilled-water row and 990 ml SL-10 distilled-water row are missing.
- Medium: Xylose is listed as an ordinary top-level ingredient even though the source requires adding it after autoclaving from an anoxic, filtered stock.
- Low: `NiCl2 x 6 H2O` is grounded only to generic nickel dichloride, and the BD-BBL/BD-Difco source attributes for peptone and yeast extract are not retained.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/modified_caldicellulosiruptor_medium.yaml` or the MediaDive import path so SL-10 remains a nested stock recipe and the main formula keeps a structured 1.0 ml addition to that stock.
- Preserve both distilled-water rows with their source amounts: 1.0 L for the JCM 968 main solution and 990 ml for the SL-10 stock.
- Represent xylose as a post-autoclave, filter-sterilized, anoxic stock addition or otherwise capture that the direct xylose row is excluded from the autoclaved base.
- Ground `NiCl2 x 6 H2O` to a hydrate-specific term when an exact public identifier is available, and preserve the BD-BBL and BD-Difco attributes as source qualifiers.
- Regenerate `data/merge_yaml/merged/modified_caldicellulosiruptor_medium__508055ac.yaml` after the maintained owner or importer is repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Confirm that top-level ingredients include a 1.0 ml SL-10 addition, not direct `HCl`, `FeCl2 x 4 H2O`, `ZnCl2`, `MnCl2 x 4 H2O`, `H3BO3`, `CoCl2 x 6 H2O`, `CuCl2 x 2 H2O`, `NiCl2 x 6 H2O`, or `Na2MoO4 x 2 H2O` rows from the stock.
- Compare the regenerated formula against JCM 968 and JCM 433 to verify the two water rows, pH 7.2, 100% N2 handling, and the filtered post-autoclave xylose addition.

## Additional Notes

None found.

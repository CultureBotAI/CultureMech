# YAML Record Review: modified_cellulolytic_haloarchaea_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_cellulolytic_haloarchaea_medium__51fd74be.yaml
- Started UTC: 2026-09-24T10:36:40Z
- Finished UTC: 2026-09-24T10:37:31Z
- Verdict: needs curation

## Target

Generated record `CultureMech:002353` for JCM/MediaDive medium `J1181`, `MODIFIED CELLULOLYTIC HALOARCHAEA MEDIUM`.

The generated record merges `modified_cellulolytic_haloarchaea_medium` from `data/normalized_yaml/archaea/modified_cellulolytic_haloarchaea_medium.yaml`. The generated YAML was compared with the maintained owner, JCM medium 1181, MediaDive medium `J1181`, and the referenced JCM stock pages 574, 1079, and 197.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed; `/private/tmp/modified_cellulolytic_haloarchaea_medium__51fd74be.strict.tsv` contained only the header row.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The medium identity, JCM/MediaDive grounding, pH 7.0, and reusable-stock labels line up with JCM 1181.

The ingredient rows do not preserve that structure. Nearly every row after yeast extract is an undiluted stock component or a volume of a molar stock. `NiCl2 x 6 H2O` is also grounded to generic `CHEBI:34887` nickel dichloride, and the source `BD-Difco` qualifier on yeast extract is absent.

## Evidence

JCM 1181 lists a main pre-autoclave mix of 833 ml MDS salt water, 1 ml Trace element solution, and 0.1 g yeast extract, then instructs the curator to bring volume to 958 ml with distilled water and optionally add 20 g/L agar for solid medium. After autoclaving and cooling, it adds 5 ml of 1 M `NH4Cl`, 2 ml potassium phosphate buffer, 5 ml filter-sterilized Trace vitamins, and 30 ml of 0.2 M Cellobiose solution; pH is readjusted to 7.0 with sterile 10% `Na2CO3` if necessary.

JCM 574 and MediaDive solution `4404` define MDS salt water as a 1 L stock containing 240 g NaCl, 30 g `MgCl2 x 6 H2O`, 35 g `MgSO4 x 7 H2O`, 7 g KCl, and 5 ml of 1 M `CaCl2`; JCM 574 and MediaDive solution `4405` define potassium phosphate buffer from 83.4 ml of 1 M `K2HPO4` plus 16.6 ml of 1 M `KH2PO4`, followed by an equal volume of water. JCM 1079 and MediaDive solution `5146` define a 1 L trace-element stock that is dosed at 1 ml. JCM 197 and MediaDive solution `3861` define a 1 L trace-vitamin stock that is dosed at 5 ml.

The generated record promotes all MDS salts, trace elements, phosphate-buffer components, and trace vitamins to top-level ingredients at their stock concentrations. It also converts 5 ml of 1 M `NH4Cl` into `5` `G_PER_L`, converts 30 ml of 0.2 M cellobiose into `30` `G_PER_L`, and omits the main 958 ml distilled-water fill plus the explicit water rows in the trace-element and trace-vitamin stocks.

## Completeness

The record preserves the JCM 1181 identifier, pH, stock preparation prose, autoclave and post-cooling prose, and the pH 7.0 readjustment instruction.

It is incomplete for every structured stock addition: MDS salt water, Trace element solution, Potassium phosphate buffer, Trace vitamins, 1 M `NH4Cl`, and 0.2 M Cellobiose solution. The optional agar instruction is only embedded in prose, the stock water rows are absent, and stock component concentrations are not distinguished from final-medium additions.

## Findings

- High: MDS salt water, Trace element solution, Potassium phosphate buffer, and Trace vitamins are flattened into final-medium ingredients instead of being modeled as volume additions of named stocks.
- High: Molar solution additions are numerically corrupted; for example, 5 ml of 1 M `NH4Cl` becomes 5 g/L and 30 ml of 0.2 M cellobiose becomes 30 g/L.
- Medium: The main distilled-water fill to 958 ml and the explicit distilled-water rows in the trace-element and trace-vitamin stocks are missing.
- Medium: Potassium phosphate buffer has lost its equal-volume dilution with water.
- Low: `NiCl2 x 6 H2O` is grounded only to generic nickel dichloride, and the BD-Difco yeast-extract qualifier is not retained.

## Recommended Edits

- Recurate `data/normalized_yaml/archaea/modified_cellulolytic_haloarchaea_medium.yaml` or the MediaDive importer so JCM 1181 keeps named stock additions instead of promoting every stock component to a final-medium ingredient.
- Preserve MDS salt water as an 833 ml addition, Trace element solution as a 1 ml addition, Potassium phosphate buffer as a 2 ml addition, Trace vitamins as a 5 ml filter-sterilized post-autoclave addition, 1 M `NH4Cl` as a 5 ml post-autoclave addition, and 0.2 M Cellobiose as a 30 ml post-autoclave addition.
- Preserve the 958 ml main-water fill, the trace-element and trace-vitamin water rows, and the equal-volume dilution in the potassium phosphate buffer.
- Keep the optional 20 g/L agar instruction conditional for solid medium.
- Ground `NiCl2 x 6 H2O` to a hydrate-specific term when an exact public identifier is available, and preserve the BD-Difco yeast-extract qualifier.
- Regenerate `data/merge_yaml/merged/modified_cellulolytic_haloarchaea_medium__51fd74be.yaml` after the maintained owner or importer is repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated record against JCM 1181 and the referenced stock formulae from JCM 574, 1079, and 197.
- Confirm that final-medium top-level ingredients no longer include undiluted trace-element, trace-vitamin, MDS, or potassium-buffer component rows.

## Additional Notes

None found.

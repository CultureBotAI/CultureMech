# YAML Record Review: Stetteria Medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/stetteria_medium__0a06dac3.yaml
- Started UTC: 2026-09-25T07:31:34Z
- Finished UTC: 2026-09-25T07:31:34Z
- Verdict: needs curation

## Target
Reviewed generated record `CultureMech:008954` / `stetteria_medium` from `data/merge_yaml/merged/stetteria_medium__0a06dac3.yaml`.

The generated record has one source, `TOGO:M236`, imported from JCM medium 244 as Stetteria Medium.

## Validation
- Schema validation: Passed with `No issues found`.
- Strict validation: Passed for 1 file with 0 total error rows.
- Reference validation: Passed for 1 file with 0 link checks and all validations passing.
- Term validation: Passed.
- Embedded curation history validation: Not checked; the standalone history validator does not target `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding
The source identity is preserved: the generated file cites TOGO medium M236, records original source `JCM_M244`, and links back to the JCM medium 244 page.

The exact local search found only the normalized TOGO source, the generated merged record, and source indexes for `CultureMech:008954`, `TOGO:M236`, and `JCM_M244`. An initial search for `TOGO:M236` was too broad because it also matched longer IDs such as `TOGO:M2360`; that output was discarded and rerun with a digit boundary on the source id.

## Evidence
The JCM medium 244 page and TOGO M236 payload identify the target pH as 6.0. The main recipe contains 500 ml distilled water, 500 ml 2x Synthetic seawater, 15 ml Trace minerals, 10 ml Ni-Se-W solution, 0.16 g NaHCO3, 0.5 g KH2PO4, 2 g Bacto peptone, 1 g yeast extract, 0.75 mg resazurin, 0.5 g Na2S*9H2O, and 10 g sulfur powder.

The 2x Synthetic seawater stock is a liter-scale stock containing 55.4 g NaCl, 14 g MgSO4*7H2O, 11 g MgCl2*6H2O, 1.5 g CaCl2*2H2O, 1.3 g KCl, 0.2 g NaBr, 0.06 g H3BO3, 0.03 g SrCl2*6H2O, and 0.1 mg KI in 1 L water. The main recipe uses 500 ml of this 2x stock.

The Ni-Se-W stock is also a liter-scale stock. JCM lists 25 mg NiCl2*6H2O, 2 g ammonium nickel sulfate hexahydrate, 0.3 mg Na2SeO3, 10 mg Na2SeO4, and 10 mg Na2WO4*2H2O in 1 L water, while the main recipe uses only 10 ml of that stock.

JCM also gives preparation instructions that matter to the final recipe: mix everything except sulfur and Na2S*9H2O, adjust to pH 6.0 with H2SO4, filter sterilize the medium, steam sulfur for 3 hours on each of 3 successive days, neutralize Na2S*9H2O as a 5% solution, autoclave under N2, dispense under H2-CO2 at 4:1, add sterile sulfide before inoculation, readjust pH to 6.0 with sterile 1 N H2SO4, and pressurize inoculated bottles to 200 kPa H2-CO2.

## Completeness
The generated formula is not a usable final medium formula. It keeps `Synthetic seawater (2 x, see below)` as a 500 `G_PER_L` pseudo-ingredient and keeps `Trace minerals` and `Ni-Se-W solution` as empty solution rows with 15 and 10 `G_PER_L`, although all three values are addition volumes.

The synthetic seawater components are present at 2x stock strength instead of being halved by the 500 ml addition into a 1 L main recipe. The Ni-Se-W components are present as unscaled stock entries, and several stock `mg` quantities were imported with the same numeric value in `G_PER_L`; for example, 25 mg/L NiCl2*6H2O became 25 `G_PER_L`, and 10 mg/L Na2WO4*2H2O became 10 `G_PER_L`.

The main-recipe resazurin row has the same mg-to-g problem: 0.75 mg in the final liter became 0.75 `G_PER_L` instead of 0.00075 `G_PER_L`. The generated water value of 502 `G_PER_L` is a summed duplicate artifact from the 500 ml main water row plus 1 L water rows inside two stock recipes.

The explicit pH 6.0 target is present in JCM and TOGO but absent from the generated `MediaRecipe`; sulfur steaming, sulfide neutralization, anaerobic gas handling, H2SO4 readjustment, and 200 kPa pressurization are also only represented as variable chemicals or gases instead of as preparation metadata.

## Findings
- Nested stocks were flattened into final ingredients without applying the 500 ml synthetic seawater addition or 10 ml Ni-Se-W addition.
- Stock solution names and volumes were migrated to empty `solutions` rows with `G_PER_L` units.
- TOGO/JCM `mg` rows were converted to numeric `G_PER_L` rows without dividing by 1000.
- Distinct water rows from the main recipe and subsolutions were merged into 502 `G_PER_L`, which is not chemically meaningful.
- The pH 6.0 adjustment and sterilization/gassing sequence were lost from the structured record.

## Recommended Edits
- Fix `data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml` or the TOGO import pipeline, then regenerate `data/merge_yaml/merged/stetteria_medium__0a06dac3.yaml`; do not hand-edit the generated merged YAML.
- Preserve 2x Synthetic seawater, Trace minerals, and Ni-Se-W as structured stock additions with volume semantics instead of final mass ingredients.
- Scale synthetic seawater salts by the 500 ml addition and Ni-Se-W contents by the 10 ml stock addition, and convert all `mg` source quantities to grams before any final `G_PER_L` calculation.
- Restore `ph_value: 6.0` from the TOGO metadata or JCM page.
- Move H2SO4, N2, H2, and CO2 to preparation context unless the schema can represent them as pH-adjustment and headspace-gas operations.

## Follow-up Checks
- Verify the regenerated record has no final ingredient named `Synthetic seawater (2 x, see below)`, `Trace minerals`, or `Ni-Se-W solution` with a `G_PER_L` concentration copied from a volume.
- Confirm resazurin is represented as 0.00075 g/L, not 0.75 g/L.
- Confirm the generated record captures pH 6.0 and no longer sums water from stock recipes into a 502 g/L row.
- Re-run schema, strict, reference, and term validators on the regenerated merged YAML.

## Additional Notes
The final exact local search for `TOGO:M236`, `JCM_M244`, `CultureMech:008954`, and `Stetteria Medium` included ignored and hidden files under `data/normalized_yaml` and `data/merge_yaml/merged`.

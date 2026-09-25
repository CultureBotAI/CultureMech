# YAML Record Review: STEROIDOBACTER MEDIUM
- Repository: CultureMech
- Record: data/merge_yaml/merged/steroidobacter_medium__de686c12.yaml
- Started UTC: 2026-09-25T07:30:08Z
- Finished UTC: 2026-09-25T07:30:08Z
- Verdict: needs curation

## Target
Reviewed generated record `CultureMech:003818` / `steroidobacter_medium` from `data/merge_yaml/merged/steroidobacter_medium__de686c12.yaml`.

The generated record is the canonical merged record for three DSMZ/KOMODO medium 1116 imports: `KOMODO_1116_STEROIDOBACTER_MEDIUM`, direct DSMZ `steroidobacter_medium`, and KOMODO `steroidobacter_medium_replace_testosterone_with_heptanoate`.

## Validation
- Schema validation: Passed with `No issues found`.
- Strict validation: Passed for 1 file with 0 total error rows.
- Reference validation: Passed for 1 file with 0 link checks and all validations passing.
- Term validation: Passed.
- Embedded curation history validation: Not checked; the standalone history validator does not target `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding
The medium identity is coherent for DSMZ medium 1116: the direct MediaDive/DSMZ normalized parent has source id `mediadive.medium:1116`, the KOMODO parent cites `komodo.medium:1116` with the same DSMZ medium number, and the heptanoate KOMODO child is a declared variant of DSMZ 1116.

The generated merged record kept the KOMODO medium as canonical, points back to the direct DSMZ parent through `parent_media`, carries a `SOURCE_DUPLICATE` variant relationship, and lists the heptanoate KOMODO source as a synonym.

An exact search found a separate generated `STEROIDOBACTER_MEDIUM.yaml` from JCM medium 862. That JCM record has the same label but a different source id and a different solution topology, so it should not be deduplicated with the DSMZ 1116 record solely by name.

## Evidence
The DSMZ medium 1116 PDF and the MediaDive REST payload agree on the base recipe: pH 7.2, final base volume 1000 ml, and a base liter containing NaCl 1 g, MgCl2 x 6 H2O 0.4 g, KH2PO4 0.2 g, KCl 0.5 g, NH4Cl 0.25 g, CaCl2 x 2 H2O 0.15 g, Na2SO4 0.07 g, NaNO3 0.42 g, and distilled water 1000 ml.

The source then gives two substrate workflows. For testosterone growth it uses a 20 mg/ml testosterone-in-acetone solution, dispenses 0.1 ml per 10 ml medium, evaporates the solvent, gasses with N2/CO2 at 80:20, closes the vessels, autoclaves, and sonicates the vessels to suspend testosterone. For heptanoate growth it omits testosterone and adds 325 mg/L heptanoic acid from a pH-adjusted, 20-fold, filter-sterilized anaerobic stock after cooling.

After autoclaving, the source adds, per 10 ml, 0.3 ml of 84 g/L NaHCO3 solution, 100 ul Trace element solution SL-10, 100 ul Selenite-tungstate solution, and 100 ul Vitamin solution before adjusting pH to 7.2.

The DSMZ stock formulae are stock formulae: SL-10 has HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O in 1 L; the selenite-tungstate stock has NaOH, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O in 1 L; the vitamin stock has mg-per-liter vitamin concentrations in 1 L.

## Completeness
The generated record correctly carries the pH 7.2 value and the DSMZ/KOMODO medium 1116 source identity, but the displayed formula is not the final medium formula. It flattens 1000 ml stock recipes into top-level final `G_PER_L` ingredients even though only 100 ul of each stock is added per 10 ml of basal medium.

The generated record omits both DSMZ growth-substrate alternatives from the structured formula. It has no testosterone or heptanoic acid final ingredient, and it has no NaHCO3 final ingredient despite the mandatory 0.3 ml addition of an 84 g/L NaHCO3 stock per 10 ml medium.

The direct DSMZ normalized parent still retains the preparation text that describes testosterone handling, heptanoate replacement, NaHCO3 addition, stock addition volumes, pH adjustment, and vitamin solution sterilization. The generated canonical record came from the KOMODO parent and does not carry those `preparation_steps`, so the generated merge loses information that is needed to interpret the flattened ingredient rows.

## Findings
- SL-10, selenite-tungstate, and vitamin compounds are exposed at stock strength; the final medium should scale those stocks by the 100 ul per 10 ml addition rate before surfacing them as final concentrations.
- The NaHCO3 addition is present in DSMZ and MediaDive but absent from the generated final ingredient list.
- The testosterone workflow is procedural and substrate-specific; acetone evaporation, N2/CO2 gassing, autoclaving, and sonication cannot be recovered from the generated top-level ingredient list.
- The heptanoate variant was merged as a duplicate because its normalized ingredients match the testosterone recipe, but the source variant should differ by omitting testosterone and adding heptanoic acid.
- The generated record names the duplicate relationship correctly enough for provenance, but the relationship is being driven by an incomplete fingerprint rather than a fully curated final-medium formula.

## Recommended Edits
- Fix the DSMZ/KOMODO normalized records or the MediaDive/KOMODO import logic, then regenerate `data/merge_yaml/merged/steroidobacter_medium__de686c12.yaml`; do not hand-edit the generated merged YAML.
- Preserve the direct DSMZ preparation steps when selecting a KOMODO duplicate as canonical, or promote the MediaDive parent as canonical when it carries richer preparation metadata for the same DSMZ medium number.
- Represent stock additions as structured solutions with `volume_added` semantics, or scale their internal concentrations by 100 ul per 10 ml before exposing final concentrations.
- Split the heptanoate workflow from the testosterone workflow unless the schema can encode conditional substrate alternatives inside one recipe without hiding heptanoic acid.
- Add the NaHCO3 stock addition as a structured component so bicarbonate is not silently omitted.

## Follow-up Checks
- Recompute the ingredient fingerprint after fixing stock scaling and verify the testosterone and heptanoate alternatives no longer collapse merely because both lost their substrate-specific additions.
- Confirm all SL-10, selenite-tungstate, and vitamin entries are scaled to final-medium amounts or moved under stock solutions.
- Confirm `ph_value: 7.2` survives regeneration.
- Re-run schema, strict, reference, and term validators on the regenerated merged YAML.

## Additional Notes
The exact local search for `CultureMech:003818`, `komodo.medium:1116`, `mediadive.medium:1116`, `STEROIDOBACTER MEDIUM`, and `steroidobacter_medium_replace_testosterone_with_heptanoate` included ignored and hidden files under `data/normalized_yaml` and `data/merge_yaml/merged`.

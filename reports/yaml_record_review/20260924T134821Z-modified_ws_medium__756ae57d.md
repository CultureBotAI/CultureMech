# YAML Record Review: modified_ws_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_ws_medium__756ae57d.yaml
- Started UTC: 2026-09-24T13:47:48Z
- Finished UTC: 2026-09-24T13:48:21Z
- Verdict: needs curation

## Target

Reviewed merged generated record `CultureMech:008371`, `modified_ws_medium`, a liquid semi-defined bacterial recipe imported from TOGO `M1801` / NBRC `M1027`.

## Validation

The generated record passed the focused open schema validator; it exited 0 with no diagnostics.

Strict validation passed with 0 errors. The TSV output contained only its header row.

Reference validation passed. The checker executed 0 reference checks for this record.

Term validation passed. The validator emitted the known `eutils` / `pkg_resources` warning before reporting success.

Embedded `curation_history` entries were not checked: `just validate-history` validates standalone `history/` content, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The medium identity is correct. TOGO `M1801` resolves to `Modified WS medium` and points at NBRC medium 1027.

The two solution identities are incorrect. NBRC medium 1027 defines recipe-local `Vitamin solution*` and `Trace elements solution**` stocks, but the generated record links them to `mediadive.solution:6241` and `mediadive.solution:6187`. MediaDive solution 6241 contains a 100 ml vitamin recipe with cyanocobalamine, thiamine HCl, and biotin; MediaDive solution 6187 is an EDTA/FeCl3 trace solution. Neither composition matches the NBRC M1027 local stocks.

The hydrate groundings for `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` are too generic because both point at anhydrous chloride CHEBI terms. `Cysteine-HCl` still carries a legacy `mediaingredientmech_term` id even after the record history claims legacy MediaIngredientMech links were refreshed to CHEBI keying.

## Evidence

The live NBRC medium 1027 page and the TOGO `M1801` API list the same final-medium rows: KH2PO4 0.136 g, NH4Cl 0.54 g, MgCl2 x 6 H2O 3.05 g, CaCl2 x 2 H2O 0.147 g, NaCl 20 g, Bacto Yeast Extract (Difco) 0.1 g, sodium acetate 0.08 g, NaHCO3 2.52 g, 2 ml vitamin solution, 1 ml trace element solution, resazurin 1 mg, Cysteine-HCl 0.3 g, Na2S x 9 H2O 0.3 g, and distilled water 1 L.

NBRC and TOGO define `*Vitamin solution` as a one-liter stock containing 2 mg biotin, 2 mg folic acid, 10 mg Pyridoxine-HCl, 5 mg Thiamine-HCl, 5 mg riboflavin, 5 mg nicotinic acid, 5 mg Ca-pantothenate, 1 mg p-Aminobenzoic acid, 0.01 mg Vitamin B12, and water.

NBRC and TOGO define `**Trace elements solution` as a one-liter stock containing nitrilotriacetic acid 12.8 g, FeCl3 x 6 H2O 1.35 g, MnCl2 x 4 H2O 0.1 g, CoCl2 x 6 H2O 0.024 g, CaCl2 x 2 H2O 0.1 g, ZnCl2 0.1 g, CuCl2 x 2 H2O 0.025 g, H3BO3 0.01 g, Na2MoO4 x 2 H2O 0.024 g, NaCl 1 g, NiCl2 x 6 H2O 0.12 g, Na2SeO4 0.004 g, Na2WO4 0.004 g, and distilled water.

The source preparation instructions say to autoclave the main ingredients under an H2/CO2 atmosphere of 80/20, separately autoclave 3 percent cysteine-HCl and Na2S x 9 H2O solutions under N2, add filter-sterile vitamin solution, cysteine-HCl, and Na2S x 9 H2O before inoculation, and pressurize inoculated vessels to 150 kPa with H2/CO2. The trace stock has an additional instruction to dissolve NTA first, adjust to pH 6.5 with NaOH, then add minerals; final pH is 7.0.

## Completeness

The final-medium amounts for the main salts and yeast extract match the source except for `Resazurin`, which is 1 mg in NBRC/TOGO but `1 G_PER_L` in the generated record.

The generated record is incomplete because the vitamin and trace stock compositions are both duplicated into the final ingredient list at stock concentration. The stock solvent rows were also merged into final-medium water, and the local stock doses were encoded as `2 G_PER_L` and `1 G_PER_L` instead of 2 ml/L and 1 ml/L.

Anaerobic handling, 3 percent reducing-agent stocks, the H2/CO2 and N2 atmospheres, the 150 kPa pressure, and the trace-stock pH instructions are not structured. Gas rows with variable concentrations do not preserve this procedural context.

## Findings

1. The generated artifact is stale relative to the 2026-09-02 normalized repair: `Distilled water` is still the erroneous sum of three source-local one-liter water rows.

2. `NaCl` and `CaCl2 x 2 H2O` are still summed across the main recipe and the local trace stock. They should be 20 g/L and 0.147 g/L in the final medium, with the trace-stock salt amounts nested under `Trace elements solution**`.

3. All vitamin and trace-stock components were flattened into final ingredients at stock concentrations. The final recipe should add only 2 ml of vitamin stock and 1 ml of trace stock per liter.

4. The source `1 mg` resazurin row was converted to `1 G_PER_L`, a 1000-fold unit error.

5. The local NBRC `Vitamin solution*` and `Trace elements solution**` are incorrectly linked to unrelated MediaDive solutions 6241 and 6187 by generic label.

6. The preparation instructions are absent: anaerobic autoclaving under H2/CO2, separate 3 percent Cysteine-HCl and Na2S x 9 H2O solutions under N2, post-autoclave filter-sterile additions, 150 kPa pressurization, and the trace-stock pH workflow are all lost.

7. `Cysteine-HCl` still uses the deprecated `mediaingredientmech_term` field, and `CoCl2 x 6 H2O` / `NiCl2 x 6 H2O` are grounded to generic anhydrous CHEBI terms.

## Recommended Edits

Regenerate the merged artifact from the normalized owner after its 2026-09-02 duplicate-water repair, and keep source-local solvent rows scoped to their own stock solutions during merging.

Replace the two MediaDive solution references with local `Vitamin solution*` and `Trace elements solution**` definitions copied from NBRC M1027, then model the final additions as 2 ml/L and 1 ml/L.

Remove all vitamin-stock and trace-stock compounds from the final ingredient list except through their nested local solutions.

Convert resazurin from 1 mg/L to `0.001 G_PER_L` or an explicit `MG_PER_L` value.

Add structured preparation steps for the H2/CO2 autoclave, 3 percent cysteine-HCl and Na2S x 9 H2O stocks under N2, filter-sterile vitamin addition, post-inoculation 150 kPa H2/CO2 pressurization, and trace-stock pH sequence.

Migrate the remaining `Cysteine-HCl` legacy MediaIngredientMech link to CHEBI keying and re-ground the cobalt and nickel hexahydrates to hydrate-specific CHEBI terms if available.

## Follow-up Checks

After editing `data/normalized_yaml/bacterial/modified_ws_medium.yaml` or the TOGO import and merge logic, regenerate the merged YAML and rerun open schema, strict, reference, and term validation.

Recompare the regenerated recipe against TOGO `M1801` and NBRC `M1027`: the final medium should have 20 g NaCl, 0.147 g CaCl2 x 2 H2O, 1 mg resazurin, 2 ml vitamin solution, 1 ml trace element solution, and no stock-only vitamins or trace salts at top level.

Audit other records with `mediadive.solution:6241` or `mediadive.solution:6187` links for the same name-only match to recipe-local NBRC stocks.

## Additional Notes

An exact, ignored-file-inclusive search for `TOGO:M1801`, `M1801`, `NBRC_M1027`, and `NO=1027` under `data/normalized_yaml` and `data/merge_yaml/merged` found only this TOGO branch for the NBRC 1027 source.

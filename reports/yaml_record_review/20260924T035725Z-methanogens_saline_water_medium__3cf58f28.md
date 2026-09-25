# YAML Record Review: methanogens_saline_water_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanogens_saline_water_medium__3cf58f28.yaml
- Started UTC: 2026-09-24T03:57:25Z
- Finished UTC: 2026-09-24T04:00:05Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:007607` / `methanogens_saline_water_medium`, produced from one normalized TOGO import:

- `data/normalized_yaml/archaea/TOGO_M1090_Methanogens_Saline_Water_Medium.yaml`
- `merged_from`: `TOGO_M1090_Methanogens_Saline_Water_Medium`
- `merge_fingerprint`: `3cf58f286edd6964e160635bcca1667bfab5b40e469035510bc4fcdfa2d7a0c1`
- Upstream identity: TOGO Medium `M1090`, original source `JCM_M1027-2`, original JCM URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1027`

## Validation

- LinkML open validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 error rows in `/private/tmp/methanogens_saline_water_medium__3cf58f28.strict.tsv`.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The generated record keeps the expected CultureMech identifier, TOGO `M1090` medium term, original medium name, source URL, JCM source key, and one-source merge fingerprint. The normalized owner is byte-for-byte identical to the generated record except for the generated merge history block, so the import defects described below must be fixed in `data/normalized_yaml/archaea/TOGO_M1090_Methanogens_Saline_Water_Medium.yaml` or in shared import/solution migration code before regeneration.

The upstream TOGO API for `M1090` returns the full `Methanogens Saline Water Medium` recipe for `JCM_M1027-2`; the old JCM `GRMD=1027` URL now returns a "Nothing found" page. The TOGO response is therefore the recoverable evidence source for this import, with cross-referenced stock formulas in TOGO `M888` and `M278`.

## Evidence

- TOGO `M1090` main solution lists 1 L distilled water, 5 g NaCl, 0.15 g `CaCl2 x 2 H2O`, 0.14 g `KH2PO4`, 0.54 g `NH4Cl`, 0.3 g `K2HPO4`, 1 mg resazurin, 3.5 g `MgCl2 x 6 H2O`, 2.52 g `NaHCO3`, 1 ml Trace mineral solution from Medium `M888`, 1 ml Se/W solution from Medium `M888`, 1 ml Trace vitamins solution from Medium `M278`, and gas annotations for carbon dioxide, nitrogen, and hydrogen.
- TOGO `M1090` comments instruct mixing and dispensing the medium under an `H2-CO2` 80:20 stream, sealing with butyl rubber stoppers, autoclaving, standing overnight, adding yeast extract from a sterile anaerobic stock under `N2`, and adding 10 ml/L each of 5% `Na2S x 9H2O` and 5% `L-Cysteine x HCl x H2O` solutions before inoculation.
- TOGO `M1090` also carries strain-specific source context: for strain JCM 19935, replace trimethylamine with yeast extract at a final 0.1 g/L and pressurize to 100 kPa `H2-CO2` 80:20; for strain JCM 19936, prepare the medium without trimethylamine and pressurize inoculated vessels to the same gas mix and pressure.
- TOGO `M888` defines the referenced Trace mineral solution with 1 L water plus `Na2MoO4 x 2 H2O`, `H3BO3`, `MnCl2 x 4 H2O`, `CoCl2 x 6 H2O`, `NiCl2 x 6 H2O`, `CuCl2 x 2 H2O`, `ZnCl2`, `AlCl3`, and `FeCl2 x 4 H2O`; it also defines the referenced Se/W solution with 1 L water plus `Na2SeO3 x 5 H2O` and `Na2WO4 x 2 H2O`.
- TOGO `M278` defines the referenced Trace vitamins solution with 1 L water plus biotin, p-aminobenzoic acid, thiamine HCl, pyridoxine HCl, folic acid, vitamin B12, riboflavin, nicotinic acid, lipoic acid, and DL-calcium pantothenate.

## Completeness

The scalar medium metadata and simple base salts survived the import. The record is not complete enough for culture reconstruction because every stock solution in the source is represented as an empty `Unknown solution`, the source preparation comments are absent from the YAML, and milliliter additions and milligram masses have been coerced into gram-per-liter concentrations.

## Findings

- Stock formulas were dropped. The three cross-referenced stocks, `Trace mineral solution (see Medium [M888])`, `Se/W solution (see Medium [M888])`, and `Trace vitamins solution (see Medium [M278])`, all have `composition: []` and `name: Unknown solution`, even though TOGO `M888` and `M278` expose their component formulas. The two 5% reducing-agent additions also became empty `Unknown solution` records, so neither their 5% stock strength nor their final 10 ml/L addition is computable.
- Multiple amounts have the wrong dimensionality. `Distilled water` is stored as `1 G_PER_L` from a source `1 L`, resazurin is stored as `1 G_PER_L` from a source `1 mg`, the 1 ml trace-stock additions are stored as `1 G_PER_L`, and the 10 ml reducing-stock additions are stored as `10 G_PER_L`. These are unit-conversion defects rather than acceptable default concentrations.
- Anaerobic gas and preparation context was flattened away. The source distinguishes `H2-CO2` 80:20 dispensing/pressurization from `N2` stock storage and reducing-solution storage; the generated record only contains top-level carbon dioxide, nitrogen, and hydrogen ingredients with `VARIABLE` concentration and no ratio, timing, pressure, or storage context.
- The strain-specific scope is ambiguous. The TOGO `M1090` record is the yeast-extract `JCM_M1027-2` variant and includes comments about strain JCM 19935 versus JCM 19936, but the generated YAML only has a single unannotated 0.1 g/L yeast-extract component and no indication of which variant it represents.

## Recommended Edits

- In the normalized `TOGO_M1090_Methanogens_Saline_Water_Medium.yaml` record, reconstruct the five source stock additions as structured solutions or source-preserving cross references:
  - `Trace mineral solution` from TOGO `M888`, added at 1 ml/L.
  - `Se/W solution` from TOGO `M888`, added at 1 ml/L.
  - `Trace vitamins solution` from TOGO `M278`, added at 1 ml/L.
  - 5% `Na2S x 9H2O`, added at 10 ml/L.
  - 5% `L-Cysteine x HCl x H2O`, added at 10 ml/L.
- Fix amount normalization so source volumes remain volumes and source milligram quantities remain milligram-derived masses instead of being coerced to `G_PER_L`.
- Preserve the source procedural text in notes or a structured preparation field: `H2-CO2` 80:20 dispensing, anaerobic sterile stock handling under `N2`, autoclaving/standing overnight, reducing-stock addition before inoculation, and the 100 kPa pressurization notes.
- Record whether this YAML is intended to model only JCM 19935's yeast-extract variant or should be split from the JCM 19936 no-trimethylamine variant context.
- Regenerate `data/merge_yaml/merged/methanogens_saline_water_medium__3cf58f28.yaml` from the curated normalized owner.

## Follow-up Checks

- Re-run open, strict, reference, and term validation after regeneration.
- Diff the regenerated record against the TOGO `M1090`, `M888`, and `M278` API responses and confirm that no source mass/volume is converted to an unrelated gram-per-liter amount.
- Confirm that the old JCM URL still fails before citing TOGO as the sole formula evidence; if JCM restores `GRMD=1027`, compare the original page against TOGO for drift.

## Additional Notes

None found

# YAML Record Review: Nitrosotalea (AOA) Fresh Water Medium (FW)

- Repository: CultureMech
- Record: data/merge_yaml/merged/nitrosotalea_aoa_fresh_water_medium_fw.yaml
- Started UTC: 2026-09-24T17:37:06Z
- Finished UTC: 2026-09-24T17:37:06Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:001267`
- Name: `nitrosotalea_aoa_fresh_water_medium_fw`
- Original name: `Nitrosotalea (AOA) Fresh Water Medium (FW)`
- Media term: `mediadive.medium:1844`, DSMZ Medium 1844
- Category: `archaea`
- Source owner: `data/normalized_yaml/archaea/nitrosotalea_aoa_fresh_water_medium_fw.yaml`
- Merge state: singleton, `merged_from: nitrosotalea_aoa_fresh_water_medium_fw`

## Validation

- Open LinkML schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed; `/private/tmp/nitrosotalea_aoa_fresh_water_medium_fw.strict.tsv` contained only the TSV header.
- Reference validation: passed.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

- Identity is correctly grounded to DSMZ/MediaDive medium 1844. The live MediaDive 1844 API and the DSMZ 1844 PDF both identify the recipe as `Nitrosotalea (AOA) Fresh Water Medium (FW)` with final pH 5.1.
- The exact hidden, no-ignore singleton search for `mediadive.medium:1844`, `DSMZ Medium 1844`, `Nitrosotalea (AOA) Fresh Water Medium (FW)`, and `nitrosotalea_aoa_fresh_water_medium_fw` found only the normalized owner, its index entries, and this generated merged record. Ignored files were included.
- The record is not the result of a bad cross-provider merge. The defect is within the singleton MediaDive import and its loss of stock-solution boundaries.

## Evidence

- DSMZ 1844 defines the final liter as FW basal salts, 0.5 ml NH4Cl 1 M, 2 ml NaHCO3 1 M, 1 ml trace element solution, 1 ml FeNaEDTA 7.5 mM, and 1.95 g MES Hydrat, adjusted to strain-specific pH and filter sterilized through 0.2 um units.
- The FW basal salts are a 10x stock containing, per liter of stock, 10 g NaCl, 4 g MgCl2 x 6 H2O, 1 g CaCl2 x 2 H2O, 2 g KH2PO4, and 5 g KCl. DSMZ then instructs to add 100 ml of this 10x stock to 800 ml sterile double distilled water for the 1x final medium.
- DSMZ 1844 also defines four separate stock recipes: 2.67 g NH4Cl in 50 ml water, 4.20 g NaHCO3 in 50 ml water, an iron-free trace element solution made in 1 liter water plus HCl and trace salts, and 2.753 g FeNa-EDTA in 1 liter water.
- The generated `ingredients` list instead contains the 10x FW basal salts at their stock-strength gram-per-liter values, the 1 M NH4Cl and NaHCO3 stocks at 53.4 and 84 g/L, all trace stock constituents at their stock strengths, FeNa-EDTA at 2.753 g/L, and a merged `Double distilled water` row of 2100 g/L.
- The generated `preparation_steps` kept both the final-medium instructions and the individual stock-preparation instructions, but appended every stock step into one flat final-medium sequence rather than representing FW basal salts, NH4Cl, NaHCO3, trace elements, and FeNaEDTA as subordinate solutions.

## Completeness

- The source capture is complete enough to reconstruct the medium: the final pH, final volume, all final stock additions, all stock recipes, filter/autoclave steps, clean-container warning, aliquoting instruction, and dark 4 deg C storage instructions are present in DSMZ/MediaDive.
- The generated YAML is compositionally incomplete because it has no way to tell that most rows are stock contents dosed into the final liter in milliliter quantities.

## Findings

- Critical: stock-solution contents were flattened into final-liter ingredients. The final medium should receive 100 ml/L of 10x FW basal salts, 0.5 ml/L of NH4Cl 1 M, 2 ml/L of NaHCO3 1 M, 1 ml/L of trace elements, and 1 ml/L of FeNaEDTA; it should not list those stock recipes as full-strength final ingredients.
- Critical: waters from four stock recipes were merged into one top-level `Double distilled water` ingredient of 2100 g/L. Those waters belong to NH4Cl, NaHCO3, trace elements, and FeNaEDTA stock preparation, not to the final liter.
- Major: stock preparation steps 8 through 16 are mixed into the final recipe's linear preparation sequence, so the record no longer encodes which ingredients and sterilization/storage steps belong to FW basal salt solution, NH4Cl, NaHCO3, trace element solution, or FeNaEDTA.

## Recommended Edits

- Recurate `data/normalized_yaml/archaea/nitrosotalea_aoa_fresh_water_medium_fw.yaml` from DSMZ/MediaDive 1844.
- Encode the final recipe around stock additions: 100 ml/L 10x FW basal salt solution, 0.5 ml/L NH4Cl 1 M, 2 ml/L NaHCO3 1 M, 1 ml/L trace element solution, 1 ml/L FeNaEDTA 7.5 mM, and 1.95 g/L MES Hydrat.
- Keep FW basal salt solution, NH4Cl, NaHCO3, trace element solution, and FeNaEDTA as nested subordinate solutions with their own ingredient lists and preparation steps.
- Preserve stock waters within the corresponding stock solutions so duplicate-water merge logic cannot aggregate them into the final medium.
- Rebuild the merged YAML after the normalized source is fixed.

## Follow-up Checks

- Confirm the regenerated final record no longer lists 10x basal salts, 1 M NH4Cl, 1 M NaHCO3, trace elements, or FeNaEDTA as top-level stock-strength gram-per-liter rows.
- Confirm the final record still preserves pH 5.1, the clean-glassware/no-rubber warning, filter sterilization with 0.2 um units, aliquoting into GREINER PS containers, and dark storage at 4 deg C.
- Run open schema, strict, reference, and term validation on the regenerated target.

## Additional Notes

- None found.

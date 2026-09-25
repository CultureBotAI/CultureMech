# YAML Record Review: sporosalibacterium_medium__1bbbff55

- Repository: CultureMech
- Record: data/merge_yaml/merged/sporosalibacterium_medium__1bbbff55.yaml
- Started UTC: 2026-09-25T06:59:53Z
- Finished UTC: 2026-09-25T07:01:13Z
- Verdict: pass with minor issues

## Target

Reviewed the generated record for `SPOROSALIBACTERIUM MEDIUM`, a DSMZ Medium 1106 / KOMODO Medium 1106 source-duplicate merge assigned `CultureMech:003806`.

## Validation

- LinkML validation: Passed; no issues found.
- Strict validation: Passed; the TSV contained only the header, with 0 error rows.
- LinkML reference validation: Passed; 0 reference checks were run and all passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The generated record uses the KOMODO Medium 1106 extraction as canonical and records DSMZ Medium 1106 as `parent_media` with `relationship: SOURCE_DUPLICATE`. The DSMZ parent and KOMODO child have matching medium numbers and matching ingredient/concentration signatures, so the duplicate relationship is supported.

MediaDive identifies medium 1106 as `SPOROSALIBACTERIUM MEDIUM`, source `DSMZ`, pH 6.8 to 7.0, and links it to the DSMZ Medium 1106 PDF. The generated record preserves the pH range and carries appropriate CHEBI groundings for salts, glucose, water-derived redox/reducing components, and other defined rows.

## Evidence

DSMZ and MediaDive list a 1000 ml main solution containing 40 g NaCl, 1 g NH4Cl, 0.5 g KCl, 0.2 g CaCl2 x 2 H2O, 2 g yeast extract, 2 g Trypticase peptone, 0.5 ml 0.1 percent sodium resazurin, 3 g MgCl2 x 6 H2O, 1 g Na2CO3, 3.6 g D-glucose, 0.5 g L-cysteine HCl x H2O, and 0.5 g Na2S x 9 H2O. The generated target carries the same non-water formula as gram-per-liter rows and correctly omits the distilled-water row.

## Completeness

The chemical formula and pH range are complete relative to DSMZ Medium 1106. No nested DSMZ stock solution needed expansion for this source recipe.

The generated output is less complete than the DSMZ normalized parent because it uses the KOMODO child as canonical. `data/normalized_yaml/bacterial/sporosalibacterium_medium.yaml` has the full DSMZ preparation step describing N2-CO2 sparging, Hungate or serum-vial autoclaving, sterile anoxic additions, glucose filtration, and final pH adjustment; the generated merge has no `preparation_steps`.

## Findings

- Low: The source-duplicate merge drops DSMZ preparation text by selecting `data/normalized_yaml/bacterial/KOMODO_1106_SPOROSALIBACTERIUM_medium.yaml` as the canonical source. The DSMZ parent already has the correct preparation step and should contribute it to the generated merged record.

## Recommended Edits

- Adjust duplicate merging so a KOMODO child can inherit preparation steps from its DSMZ parent when both records have a `SOURCE_DUPLICATE` relationship and matching recipe fingerprint.
- Regenerate `data/merge_yaml/merged/sporosalibacterium_medium__1bbbff55.yaml` after merge logic can preserve the DSMZ Medium 1106 preparation step.

## Follow-up Checks

- After regeneration, confirm that the generated target still keeps `CultureMech:003806` and records `CultureMech:000539` as its DSMZ source duplicate rather than creating two independent records for the same formula.

## Additional Notes

None found

# YAML Record Review: methanocella_conradii_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanocella_conradii_medium__1b8eb0c4.yaml`
- Started UTC: 2026-09-24T03:27:05Z
- Finished UTC: 2026-09-24T03:27:05Z
- Verdict: needs curation

## Target

- Stable ID: `CultureMech:010380`
- Label: `methanocella_conradii_medium`
- Category: `archaea`
- Maintained owner: `data/normalized_yaml/archaea/TOGO_M956_Methanocella_Conradii_Medium.yaml`
- Source identity: TOGO medium M956, original source JCM medium 911

## Validation

- Open schema: Passed; `linkml-validate` reported no issues.
- Strict validator: Passed; 1 file scanned, 0 files with errors, and 0 error rows.
- Reference validator: Passed; 0 reference checks were applicable.
- Term validator: Passed.
- Embedded history: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

- `media_term` grounds this record to `TOGO:M956`, whose API payload identifies original medium `JCM_M911`.
- Exact ignored-file search for `CultureMech:010380`, `TOGO_M956_Methanocella_Conradii_Medium`, `TOGO:M956`, `JCM_M911`, and `jcm_grmd?GRMD=911` found a single TOGO M956 owner for this generated fingerprint.
- The same search also found `data/normalized_yaml/archaea/JCM_J911_METHANOCELLA_CONRADII_MEDIUM.yaml`, a direct JCM 911 import of the same formula that should be reconciled with the TOGO M956 import after both records are structured correctly.
- The live JCM 911 endpoint now returns no formula, but TOGO preserves the JCM 911 main recipe and the referenced TOGO M180 and M401 stock recipes.

## Evidence

- TOGO M956 lists 1 L water; 0.2 g yeast extract; 0.1 g `CaCl2 x 2 H2O`; 0.2 g KH2PO4; 0.1 g NH4Cl; 0.5 mg resazurin; 0.4 g `MgCl2 x 6 H2O`; 0.5 g KCl; 0.082 g sodium acetate trihydrate; 0.3 g `L-Cysteine HCl x H2O`; 1 ml FeCl2 solution; 1 ml trace element solution; 1 ml tungstate solution; and gas handling with CO2 and N2.
- The same TOGO source lists post-autoclave additions of 30 ml 8% NaHCO3 solution, 1 ml vitamin solution, 1 ml thiamine solution, 1 ml vitamin B12 solution, a 5 ml 5% `Na2S x 9H2O` stock, N2/CO2 and H2/CO2 gas handling, and a local 1 L tungstate stock containing 7 mg `Na2WO4 x 2 H2O` and 0.4 g NaOH.
- TOGO M180 supplies the referenced `FeCl2 solution` and `Trace element solution`; TOGO M401 supplies the referenced `Vitamin solution`, `Thiamine solution`, and `Vitamin B12 solution`.

## Completeness

- The TOGO M956, M180, and M401 API payloads provide enough ingredient and stock details to resolve all seven migrated stock stubs.
- Empty `target_organisms` and `growth_data` are optional-field omissions, not review findings for this record.

## Findings

- Blocker: all seven source stock additions are empty `Unknown solution` stubs. The record preserves FeCl2, trace element, tungstate, bicarbonate, vitamin, thiamine, and vitamin B12 stock names but loses every nested component.
- Blocker: every solution stub records the source volume as `G_PER_L`. Six 1 ml additions are stored as `1` g/L, and the 30 ml 8% NaHCO3 stock is stored as `30` g/L.
- Blocker: the 5 ml 5% `Na2S x 9H2O` stock is not a solution at all in the record; it is flattened to a top-level `5% Na2S-9H2O` ingredient with concentration `5` g/L.
- Major: the source-local tungstate stock is partially flattened into top-level `Na2WO4 x 2 H2O` and NaOH ingredients. `Na2WO4 x 2 H2O` is also recorded as `7` g/L even though the source stock contains 7 mg in 1 L and only 1 ml is added to the final medium.
- Major: source resazurin is 0.5 mg but is recorded as `0.5` g/L.
- Major: gas composition and pressure are not preserved. CO2, N2, and H2 are defaulted to variable top-level ingredients instead of encoding the N2/CO2 4:1 handling gas, H2/CO2 4:1 replacement gas, and 150 kPa H2/CO2 final pressurization that the direct JCM import still retains in text.
- Minor: generated output predates the owner-level September duplicate repair; it still reports `Distilled water` as `2.0` g/L from two merged `1.0` entries even though the current TOGO owner has collapsed that row to `1.0`.
- Minor: TOGO M956 and direct JCM 911 should collapse to one canonical generated recipe once the stock hierarchy is restored.

## Recommended Edits

- In `data/normalized_yaml/archaea/TOGO_M956_Methanocella_Conradii_Medium.yaml`, populate the FeCl2 and trace-element stocks from TOGO M180 and the vitamin, thiamine, and vitamin B12 stocks from TOGO M401.
- Move the local tungstate components under `Tungstate solution (see below)` with the source stock concentrations and a 1 ml final-medium addition.
- Convert 8% NaHCO3 and 5% `Na2S x 9H2O` into structured stock additions at 30 ml and 5 ml respectively.
- Convert resazurin from 0.5 mg to the corresponding g/L final concentration.
- Move CO2, N2, and H2 out of top-level ingredients and encode the N2/CO2 and H2/CO2 atmosphere steps with their 4:1 ratios and 150 kPa pressurization.
- Regenerate merged YAML so the September water duplicate repair appears in the generated file.
- Reconcile the TOGO M956 import with the direct JCM 911 import to avoid publishing the same source medium twice.

## Follow-up Checks

- Rerun open-schema, strict, reference, and term validation after the seven stocks are populated.
- Search the regenerated record for `Unknown solution` and confirm no stock stubs remain.
- Confirm regenerated output no longer records `5% Na2S x 9H2O`, `Na2WO4 x 2 H2O`, or NaOH as top-level ingredients for this record.
- Compare regenerated TOGO M956 and direct JCM 911 outputs and verify a single canonical JCM 911 formula remains active.

## Additional Notes

None found.

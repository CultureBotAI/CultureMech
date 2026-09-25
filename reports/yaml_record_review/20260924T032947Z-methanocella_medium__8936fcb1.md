# YAML Record Review: methanocella_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanocella_medium__8936fcb1.yaml`
- Started UTC: 2026-09-24T03:29:47Z
- Finished UTC: 2026-09-24T03:29:47Z
- Verdict: needs curation

## Target

- Stable ID: `CultureMech:009898`
- Label: `methanocella_medium`
- Category: `archaea`
- Maintained owner: `data/normalized_yaml/archaea/TOGO_M508_Methanocella_Medium.yaml`
- Source identity: TOGO medium M508, original source JCM medium 507

## Validation

- Open schema: Passed; `linkml-validate` reported no issues.
- Strict validator: Passed; 1 file scanned, 0 files with errors, and 0 error rows.
- Reference validator: Passed; 0 reference checks were applicable.
- Term validator: Passed.
- Embedded history: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

- `media_term` grounds the record to `TOGO:M508`, whose API payload identifies original medium `JCM_M507`.
- Exact ignored-file search for `CultureMech:009898`, `TOGO_M508_Methanocella_Medium`, `TOGO:M508`, `JCM_M507`, `jcm_grmd?GRMD=507`, and `Methanocella Medium` found a single TOGO M508 owner for this generated fingerprint.
- The same search found `data/normalized_yaml/archaea/JCM_J507_METHANOCELLA_MEDIUM.yaml`, a direct JCM 507 import of the same source medium that should be reconciled with this TOGO record after both records have structured stocks.

## Evidence

- The live JCM 507 page states that the medium uses Solution A of JCM medium 284, is supplemented with 0.1 g sodium acetate, and is brought to 1 L final volume.
- TOGO M508 captures the Solution A composition: 1 L water, 0.15 g `CaCl2 x 2 H2O`, 0.14 g KH2PO4, 0.54 g NH4Cl, 1 mg resazurin, 0.2 g `MgCl2 x 6 H2O`, 2.5 g NaHCO3, 0.1 g yeast extract, 2 ml trace vitamins, 1 ml trace element solution, and 1 ml Se/W solution.
- TOGO M278 provides the referenced trace-vitamin, trace-element, and Se/W stock compositions used by Solution A.
- The live JCM 507 page also instructs replacing the gas phase with H2/CO2 at 80:20 and pressurizing an inoculated bottle to 150 kPa with the same gas mixture.

## Completeness

- TOGO M508 plus the M278 cross-reference preserve enough evidence to populate all three stock additions and the resazurin final concentration.
- Empty `target_organisms` and `growth_data` are optional-field omissions, not review findings for this record.

## Findings

- Blocker: all three stock additions are empty `Unknown solution` stubs. `Trace vitamins solution`, `Trace element solution`, and `Se/W solution` point to M278 but have no nested composition.
- Blocker: the three source stock volumes are recorded with `G_PER_L` units. The 2 ml trace-vitamin addition is stored as `2` g/L, while the 1 ml trace-element and Se/W additions are stored as `1` g/L.
- Major: source resazurin is 1 mg per 1 L but is recorded as `1` g/L.
- Major: the H2 and CO2 handling gases are stored as variable top-level ingredients, losing the JCM 507 instruction to replace the gas phase with H2/CO2 at 80:20 and pressurize the inoculated bottle to 150 kPa.
- Minor: TOGO M508 and direct JCM 507 are separate active imports for the same source medium and need deduplication after the stock hierarchy is corrected.

## Recommended Edits

- In `data/normalized_yaml/archaea/TOGO_M508_Methanocella_Medium.yaml`, populate the M278 `Trace vitamins solution`, `Trace element solution`, and `Se/W solution` stocks with their referenced TOGO M278 compositions.
- Preserve the final-medium dosing of those three stocks as 2 ml, 1 ml, and 1 ml per litre instead of storing those volumes as `G_PER_L`.
- Convert the 1 mg resazurin source amount to `0.001` g/L.
- Move H2 and CO2 out of top-level ingredients and encode the H2/CO2 80:20, 150 kPa gas handling from JCM 507.
- Compare the repaired TOGO M508 record against direct JCM 507 and keep a single canonical generated recipe for this medium.

## Follow-up Checks

- Rerun open-schema, strict, reference, and term validation after populating all three M278 stocks.
- Search the regenerated record for `Unknown solution` and confirm none remain for the three M278 cross-references.
- Confirm regenerated M508 output records resazurin at `0.001` g/L, not `1` g/L.
- Compare regenerated TOGO M508 and direct JCM J507 output and verify a single active generated recipe remains for JCM 507.

## Additional Notes

None found.

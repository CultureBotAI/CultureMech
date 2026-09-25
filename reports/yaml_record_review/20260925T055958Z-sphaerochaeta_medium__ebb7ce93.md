# YAML Record Review: sphaerochaeta_medium__ebb7ce93

- Repository: CultureMech
- Record: data/merge_yaml/merged/sphaerochaeta_medium__ebb7ce93.yaml
- Started UTC: 2026-09-25T05:58:50Z
- Finished UTC: 2026-09-25T06:00:00Z
- Verdict: needs curation

## Target

Generated merged YAML for DSMZ 1204, SPHAEROCHAETA MEDIUM, merged with the KOMODO 1204 `spirochaeta_coccoides_medium` branch as a SOURCE_DUPLICATE.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/sphaerochaeta_medium__ebb7ce93.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The DSMZ identity is correct, and the KOMODO duplicate is plausibly a source duplicate because it explicitly points to DSMZ Medium 1204 and carries the same ingredient signature.

Most simple salts are grounded to reasonable CHEBI terms. Sodium resazurin is grounded only on `term` to CHEBI:8806 labelled `Resazurin`; that is acceptable but less specific than the source label `Sodium resazurin (0.1% w/v)`.

## Evidence

DSMZ Medium 1204 and MediaDive 1204 agree on a 1000 ml final recipe containing NaCl, KCl, NH4Cl, KH2PO4, Na2SO4, MgCl2 x 6 H2O, CaCl2 x 2 H2O, yeast extract, casein peptone, 0.50 ml sodium resazurin at 0.1% w/v, Na2CO3, maltose monohydrate, DL-Dithiothreitol, and distilled water. The source directs sparging with 100% N2 for 30-45 minutes, autoclaving at 121 C for 20 minutes, adding maltose and DTT from sterile anoxic stocks, adding carbonate from a sterile stock under 80% N2 and 20% CO2, and checking final pH 7.4.

## Completeness

The generated record preserves the source pH, salts, complex nutrients, post-autoclave carbonate/maltose/DTT handling, and anoxic gas instructions. It omits the final 1000 ml distilled-water row.

## Findings

- Major: the generated ingredient list omits `Distilled water` at 1000 ml.
- Minor: the KOMODO duplicate note says `Aerobic: Yes` even though DSMZ 1204 makes the medium anoxic with N2 and uses N2/CO2 for the carbonate stock. Do not let that KOMODO note override the DSMZ anaerobic handling if the duplicate branch is repaired.
- Minor: `Sodium resazurin` should preserve the source 0.1% w/v stock context, not only the final 0.0005 g/L calculated concentration.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/sphaerochaeta_medium.yaml` and `data/normalized_yaml/bacterial/spirochaeta_coccoides_medium.yaml` to restore the 1000 ml distilled-water row from DSMZ 1204.
- Preserve the 0.50 ml/L addition of 0.1% w/v sodium resazurin stock, or keep a note that explains how the final 0.0005 g/L concentration was calculated.
- Regenerate `data/merge_yaml/merged/sphaerochaeta_medium__ebb7ce93.yaml` from the repaired normalized source records.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated merged record.
- Confirm the regenerated ingredient list includes 1000 ml distilled water.
- Confirm the KOMODO duplicate stays linked as a source duplicate but does not introduce aerobic cultivation semantics.

## Additional Notes

None found.

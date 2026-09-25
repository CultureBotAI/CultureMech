# YAML Record Review: sse_hd_1_10_medium_hepes
- Repository: CultureMech
- Record: data/merge_yaml/merged/sse_hd_1_10_medium_hepes.yaml
- Started UTC: 2026-09-25T07:11:10Z
- Finished UTC: 2026-09-25T07:12:22Z
- Verdict: needs curation

## Target
Reviewed the generated merged record `data/merge_yaml/merged/sse_hd_1_10_medium_hepes.yaml`, a single-source DSMZ/MediaDive import from `data/normalized_yaml/bacterial/sse_hd_1_10_medium_hepes.yaml`.

The record is identified as DSMZ Medium 1425, `SSE/HD 1:10 MEDIUM (HEPES)`, with MediaDive source id `mediadive.medium:1425`.

## Validation
- LinkML schema validation: Passed with `No issues found`.
- Strict validation: Passed; scanned 1 file and reported 0 `ERROR` rows. The strict TSV contained the header only.
- Reference validation: Passed; 1 file was validated and 0 reference checks were available.
- Term validation: Passed after the known `eutils` `pkg_resources` deprecation warning.
- Embedded `curation_history`: Not checked. The available `just validate-history` target validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding
The media identity is correct. MediaDive `/rest/medium/1425` returned one DSMZ record named `SSE/HD 1:10 MEDIUM (HEPES)`, pH 7.0, with source `DSMZ` and a DSMZ Medium 1425 PDF link. The generated YAML carries the matching `mediadive.medium:1425` term and the DSMZ PDF URL.

An exact source/id search for `mediadive.medium:1425` and `CultureMech:000889` included ignored files and found only the expected normalized DSMZ file, generated merged file, and index references under `data/normalized_yaml` and `data/merge_yaml/merged`.

## Evidence
DSMZ Medium 1425 builds the final 1 L HEPES medium from Peptone 0.50 g, Yeast extract 0.25 g, Glucose 0.10 g, HEPES 1.95 g, 500 ml SSE double-concentrated solution, 1 ml Trace Element Solution SL-10, 500 ml distilled water, and 1 ml Vitamin Solution after autoclaving.

The source SSE stock is explicitly double concentrated and is added at 500 ml/L, so its solutes should contribute one half of their stock g/L values to the final medium. The SL-10 and vitamin solutions are 1 L stocks added at 1 ml/L, so their solutes should contribute 1/1000 of their stock g/L values if expanded into the final medium.

## Completeness
No target organisms are present in the generated record; no source evidence in the reviewed DSMZ/MediaDive material names organism growth for this recipe, so that is not a defect.

The record preserves pH 7.0, the HEPES buffer, and the HEPES-specific 0.07 g KH2PO4 stock amount, but it drops the explicit 500 ml final-medium water row.

## Findings
- High: The generated record flattens the 500 ml/L SSE double-concentrated solution at full stock strength. `CaCl2 x 2 H2O`, `NH4Cl`, `MgCl2 x 6 H2O`, `(NH4)2SO4`, `MgSO4 x 7 H2O`, `CaSO4 x 2 H2O`, `Ca(NO3)2 x 4 H2O`, `Na NO3`, `KH2PO4`, `FeSO4 x 7 H2O`, and `K2SO4` are therefore 2x too high as final-medium concentrations.
- High: The generated record flattens the 1 ml/L SL-10 and vitamin stocks at full stock strength. The HCl, FeCl2, ZnCl2, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, Na2MoO4, biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, D-calcium pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid rows are therefore 1000x too high if read as final-medium concentrations.
- Medium: The generated record drops the explicit 500 ml distilled water contribution from the final medium.

## Recommended Edits
- Fix nested-stock expansion for DSMZ 1425 so the generated final medium either preserves the three stock additions or dilutes stock solutes into final-medium equivalents: 0.5x for SSE and 0.001x for SL-10/vitamins.
- Preserve the 500 ml final-medium distilled water row where the schema allows.
- Regenerate merged YAML after editing the normalized source or MediaDive import; do not patch `data/merge_yaml/merged/sse_hd_1_10_medium_hepes.yaml` by hand.

## Follow-up Checks
- After regeneration, verify that `KH2PO4` is no longer 0.07 g/L and that `CoCl2 x 6 H2O` is no longer 0.19 g/L in the final generated formula.
- Run schema, strict, reference, and term validators on the regenerated merged record.

## Additional Notes
DSMZ 1425 and DSMZ 1426 share the same nested-stock dilution problem, but the HEPES record should remain a distinct medium because its pH and buffer differ from the MES version.

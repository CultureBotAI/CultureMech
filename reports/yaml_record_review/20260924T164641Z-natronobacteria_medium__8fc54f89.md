# YAML Record Review: Natronobacteria medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/natronobacteria_medium__8fc54f89.yaml
- Started UTC: 2026-09-24T16:46:02Z
- Finished UTC: 2026-09-24T16:46:41Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:008962` for TOGO M2378, an ATCC 1590 solid-agar `Natronobacteria medium` import.

## Validation

Open schema validation passed; it exited 0 with no diagnostics.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to TOGO M2378 and its original ATCC 1590 PDF for `Natronobacteria medium`.

An exact repository search including ignored and hidden files for `TOGO:M2378`, `TOGO:M2322`, `CultureMech:008962`, `CultureMech:008910`, `8386F32049764A12AC1B1893925E9DF9`, and the Natronobacteria slugs found this generated record plus its normalized TOGO M2378 owner, an active TOGO M2322 duplicate, and the direct DSMZ/KOMODO Medium 371 family.

The hydrates on `CoCl2 . 6H2O`, `NiCl2 . 6H2O`, and `Na2MoO4 .H2O` are grounded more broadly or to the wrong hydration state: cobalt is grounded to anhydrous cobalt dichloride, nickel is grounded to nickel dichloride, and sodium molybdate monohydrate is grounded to anhydrous sodium molybdate.

## Evidence

The ATCC source lists 1.0 g KH2PO4, 1.0 g KCl, 1.0 g NH4Cl, 0.24 g MgSO4 . 7H2O, 0.17 g CaSO4 . 2H2O, 1.0 ml Trace Elements Solution SL-6, 200.0 g NaCl, 1.0 g sodium glutamate, 5.0 g yeast extract, 5.0 g Casamino acids, 5.0 g Na2CO3 sterilized as a separate solution, 20.0 g agar, and distilled water to 1.0 L.

The source instructs autoclaving the basal medium at 121C for 15 minutes, adding Na2CO3 solution after autoclaving, and adjusting the final pH to 9.0 if necessary.

The source defines Trace Elements Solution SL-6 as a separate 1.0 L stock containing 0.10 g ZnSO4 . 7H2O, 0.03 g MnCl2 . 4H2O, 0.3 g H3BO3, 0.2 g CoCl2 . 6H2O, 0.01 g CuCl2 . 2H2O, 0.02 g NiCl2 . 6H2O, and 0.03 g Na2MoO4 .H2O, adjusted to pH 3.4.

The generated record includes the basal solids and correctly types the record as `SOLID_AGAR`.

## Completeness

The final 1.0 ml SL-6 addition has been reduced to an empty solution wrapper with `1 G_PER_L`, and every SL-6 stock component has been flattened into the final medium at its stock concentration.

The sodium carbonate post-autoclave addition has been reduced to an empty solution wrapper named `Unknown solution`.

The record lacks the final pH 9.0 value, the basal autoclave and post-autoclave Na2CO3 addition steps, and the SL-6 stock pH 3.4 adjustment.

## Findings

- Major: The SL-6 stock has been flattened across the preparation boundary. The stock components are represented as final-medium ingredients, while the 1.0 ml stock addition is represented as `1 G_PER_L`.
- Major: `Na2CO3 (sterilized as a separate solution)` is an empty solution wrapper, so the record does not retain a resolved sodium carbonate post-autoclave addition.
- Major: The source water rows for the 1.0 L final medium and 1.0 L SL-6 stock are both represented as `G_PER_L` amounts.
- Major: The ATCC pH 9.0 adjustment, basal autoclave step, post-autoclave Na2CO3 addition, and SL-6 pH 3.4 adjustment are absent.
- Major: TOGO M2378 is unlinked from the active TOGO M2322 and direct DSMZ/KOMODO Medium 371 Natronobacteria records, even though they use the same DSMZ-family basal recipe.
- Major: Several hydrated salts in SL-6 have incomplete or incorrect ontology grounding.

## Recommended Edits

- In `data/normalized_yaml/bacterial/TOGO_M2378_Natronobacteria_medium.yaml`, restore Trace Elements Solution SL-6 as a nested stock solution with a 1.0 ml final-medium addition.
- Represent `Na2CO3 (sterilized as a separate solution)` as a sodium carbonate post-autoclave addition, or add a structured stock solution whose composition is explicit.
- Correct both water quantities to 1.0 L preparation volumes instead of gram-per-liter concentrations.
- Add preparation metadata for the 121C, 15 minute basal-medium autoclave, the post-autoclave Na2CO3 addition, final pH 9.0, and SL-6 pH 3.4.
- Link or collapse the active TOGO M2378, TOGO M2322, direct DSMZ, and KOMODO Natronobacteria records according to their source-level relationship.
- Re-ground the hydrated SL-6 salts to exact CHEBI terms where available, and leave unsupported hydrate-specific groundings explicit if no exact term exists.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natronobacteria_medium__8fc54f89.yaml` and verify the final recipe has a 1.0 ml SL-6 addition, not direct final-medium rows for the SL-6 salts.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored and hidden files for `TOGO:M2378`, `TOGO:M2322`, `mediadive.medium:371`, `CultureMech:008962`, and `CultureMech:008910` to verify the duplicate family is either linked or collapsed.

## Additional Notes

None found.

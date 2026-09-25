# YAML Record Review: MICROCELLA ALKALIPHILA MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/microcella_alkaliphila_medium__b71dfbd6.yaml`
- Started UTC: 2026-09-24T06:20:31Z
- Finished UTC: 2026-09-24T06:20:31Z
- Verdict: needs curation

## Target

- Reviewed merged record `data/merge_yaml/merged/microcella_alkaliphila_medium__b71dfbd6.yaml`.
- Editable normalized source: `data/normalized_yaml/bacterial/microcella_alkaliphila_medium.yaml`.
- MediaDive medium: `mediadive.medium:1063`, MICROCELLA ALKALIPHILA MEDIUM.
- DSMZ source: DSMZ Medium 1063 PDF.

## Validation

- LinkML open-schema validation: passed; `No issues found`.
- Strict validation: passed with 0 errors; `validate_strict.py` scanned 1 file and produced only the TSV header.
- Reference validation: passed; 1 file, 0 checks.
- Term validation: passed.
- Embedded history: Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The MediaDive and DSMZ identities are coherent: DSMZ Medium 1063 and MediaDive medium 1063 both identify MICROCELLA ALKALIPHILA MEDIUM at pH 9.5.
- The generated record expands `Trypticase soy broth` into researched TSB/TSA constituents from Wikipedia, then includes `Agar` even though DSMZ calls for Trypticase soy broth and the CultureMech record is `LIQUID`.
- `NiCl2 x 6 H2O` is grounded only to generic nickel dichloride.

## Evidence

- DSMZ Medium 1063 lists 30 g Trypticase soy broth, 3 g yeast extract, 944 ml distilled water, 50 ml mineral salt solution, 5 ml vitamin solution, and 1 ml trace element solution SL-10.
- The DSMZ instruction says to add sterile 1 M Na-sesquicarbonate after sterilization to reach pH 9.5.
- MediaDive expands `Mineral solution` as a 1 L stock containing KH2PO4, MgCl2 x 6 H2O, NaCl, NH4Cl, CaCl2 x 2 H2O, and water.
- MediaDive expands `Trace element solution SL-10` as a 1 L stock containing 10 ml 25% HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and water.
- MediaDive expands `Seven vitamins solution` as a 1 L stock with Vitamin B12, p-Aminobenzoic acid, D-(+)-biotin, Nicotinic acid, Calcium pantothenate, Pyridoxine hydrochloride, Thiamine-HCl x 2 H2O, and water.
- MediaDive expands 1 M Na-sesquicarbonate solution as a 100 ml stock with NaHCO3 4.2 g and anhydrous Na2CO3 5.3 g.

## Completeness

- The final 944 ml water row is missing.
- The 50 ml mineral solution, 5 ml vitamin solution, 1 ml SL-10 solution, and post-sterilization 1 M Na-sesquicarbonate adjustment are not fully represented as stock additions.
- The normalized source contains an August 2026 partial repair that moved four vitamin rows and FeCl2 into nested stocks, but several stock-strength components remain top-level.

## Findings

- The source 30 g/L Trypticase soy broth was replaced by five TSB constituent rows and a 15 g/L Agar row from Trypticase Soy Agar. This introduces a solidifying agent that is not present in the liquid DSMZ 1063 recipe.
- The final 944 ml distilled water was dropped from the top-level recipe.
- Mineral solution is completely flattened: KH2PO4, MgCl2 x 6 H2O, NaCl, NH4Cl, and CaCl2 x 2 H2O are top-level final ingredients at stock concentrations rather than children of a 50 ml/L stock.
- The generated record is stale relative to the normalized source's August stock-nesting repair for Seven vitamins and SL-10, so it still publishes all vitamin and trace-element rows as top-level ingredients.
- The normalized repair is incomplete: p-Aminobenzoic acid, D-(+)-biotin, and Calcium pantothenate are still top-level rows from Seven vitamins, and HCl plus the Zn, Mn, B, Co, Cu, Ni, and Mo salts are still top-level rows from SL-10.
- The Na-sesquicarbonate stock components are listed as final 42 g/L NaHCO3 and 53 g/L anhydrous Na2CO3 even though the source uses sterile 1 M stock after sterilization only as needed to reach pH 9.5.
- The generated and normalized records keep the SL-10 preparation note as a top-level step even though it belongs to Trace element solution SL-10.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/microcella_alkaliphila_medium.yaml`.
- Restore `Trypticase soy broth` as the DSMZ 30 g/L ingredient or, if product expansion is retained, remove the TSA-only agar constituent and keep provenance to a supplier specification rather than Wikipedia.
- Restore 944 ml distilled water to the final medium.
- Nest Mineral solution at 50 ml/L, Seven vitamins solution at 5 ml/L, and Trace element solution SL-10 at 1 ml/L with all of their stock components.
- Represent sterile 1 M Na-sesquicarbonate as a pH-adjustment stock rather than two fixed final carbonate rows.
- Scope the SL-10 FeCl2/HCl preparation note to SL-10.
- Re-ground `NiCl2 x 6 H2O` to an exact hexahydrate term if one is available.
- Regenerate `data/merge_yaml/merged/microcella_alkaliphila_medium__b71dfbd6.yaml` after the normalized source is fixed.

## Follow-up Checks

- Re-run focused open-schema, strict, reference, and term validators for `data/merge_yaml/merged/microcella_alkaliphila_medium__b71dfbd6.yaml`.
- Verify there is no agar row in the liquid recipe.
- Verify the final medium has 50 ml mineral solution, 5 ml vitamin solution, and 1 ml SL-10 rather than stock-strength top-level salts and vitamins.
- Verify Na-sesquicarbonate is a post-sterilization pH adjustment to pH 9.5, not fixed final NaHCO3 and Na2CO3 ingredients.

## Additional Notes

- Empty optional fields were not treated as defects.

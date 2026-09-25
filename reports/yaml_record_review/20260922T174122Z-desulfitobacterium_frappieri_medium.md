# YAML Record Review: desulfitobacterium_frappieri_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfitobacterium_frappieri_medium.yaml`
- Started UTC: 2026-09-22T17:41:22Z
- Finished UTC: 2026-09-22T17:41:22Z
- Verdict: needs curation

## Target

Generated bacterial `desulfitobacterium_frappieri_medium` record for KOMODO Medium 836, enriched from DSMZ Medium 836.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to KOMODO Medium 836 and notes DSMZ Medium 836 as its resolved source. The current MediaDive REST record and DSMZ PDF both identify DSMZ 836 as `DESULFITOBACTERIUM PCP-1 MEDIUM`.

The complex/undefined classification is supported by yeast extract.

The imported `Aerobic: Yes` note conflicts with the DSMZ procedure, which sparges the medium with 100% N2, dispenses it under the same gas atmosphere, and adds carbonate from a sterile anoxic stock prepared under 80% N2 and 20% CO2.

## Evidence

DSMZ 836 adds 2.00 ml FeCl2 x 4 H2O stock, 1.00 ml Trace element solution SL-10, and 0.50 ml 0.1% sodium resazurin stock to the main 1000 ml water recipe. The generated record keeps the direct FeCl2 contribution as `0.002 G_PER_L`, but it also flattens the 1.5 g/L FeCl2 row from SL-10 and then merges both rows into `1.502 G_PER_L`.

Every other SL-10 component is emitted as a top-level final-medium ingredient at stock strength: 10 ml 25% HCl becomes `2.5 G_PER_L`; ZnCl2 is `0.07 G_PER_L`; MnCl2 x 4 H2O is `0.1 G_PER_L`; H3BO3 is `0.006 G_PER_L`; CoCl2 x 6 H2O is `0.19 G_PER_L`; CuCl2 x 2 H2O is `0.002 G_PER_L`; NiCl2 x 6 H2O is `0.024 G_PER_L`; and Na2MoO4 x 2 H2O is `0.036 G_PER_L`.

The generated `NaHCO3` row is marked as a variable pH buffer extracted from notes, but DSMZ 836 contains fixed `Na2CO3` and no sodium bicarbonate ingredient.

DSMZ 836 instructs curators to dissolve all ingredients except carbonate, sulfite, and sulfide, adjust to pH 7.0, sparge with 100% N2 for 30-45 min, dispense anoxically into Hungate tubes or serum vials, autoclave, add sterile anoxic carbonate/sulfite/sulfide stocks before use, freshly prepare and filter-sterilize sulfite, then confirm pH 7.5 before use. None of those steps are represented.

DSMZ 836 also states that DSM 13498 cultures need a 3.00 g/L Na-formate supplement, which is absent.

## Completeness

The generated record has no `solutions` block for Trace element solution SL-10 or for the FeCl2, sodium resazurin, carbonate, sulfite, and sulfide stock additions described by DSMZ.

Distilled water is present in the source at 1000 ml but absent from the generated ingredient list.

The DSMZ anaerobic preparation workflow, stock-sterilization details, initial pH 7.0 adjustment, final pH 7.5 check, and strain-specific DSM 13498 formate supplementation note are not captured.

## Findings

- Needs curation: Trace element solution SL-10 was flattened into final-medium ingredient rows at stock concentrations.
- Needs curation: direct FeCl2 and SL-10 FeCl2 were summed across different recipe contexts into `1.502 G_PER_L`.
- Needs curation: the generated `NaHCO3` pH-buffer ingredient is unsupported by DSMZ 836.
- Needs curation: the `Aerobic: Yes` note contradicts DSMZ 836's explicitly anoxic N2 and N2/CO2 preparation.
- Needs curation: preparation steps are missing.
- Needs curation: stock additions and SL-10 lack structured solution records.
- Needs curation: distilled water and the DSM 13498 Na-formate supplement note are missing.

## Recommended Edits

- Refresh `data/normalized_yaml/bacterial/desulfitobacterium_frappieri_medium.yaml` from current DSMZ 836 or MediaDive medium 836.
- Model Trace element solution SL-10 as a nested 1 ml stock addition, not as top-level final-medium ingredients.
- Preserve the direct 2 ml 0.1% FeCl2 stock separately from the SL-10 FeCl2 stock.
- Remove the unsupported `NaHCO3` ingredient and the misleading `Aerobic: Yes` note.
- Add the DSMZ anaerobic preparation procedure, including the initial pH 7.0 adjustment and final pH 7.5 check.
- Add the DSM 13498-specific 3.00 g/L Na-formate supplementation note or variant.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regeneration.
- Confirm SL-10 components are nested under a Trace element solution SL-10 solution.
- Confirm the top-level FeCl2 row stays near the 2 ml 0.1% stock contribution and is not summed with the SL-10 stock formula.
- Confirm the generated record has no `NaHCO3` row unless a source explicitly adds bicarbonate.
- Confirm anaerobic preparation text and the DSM 13498 Na-formate supplement survive regeneration.

## Additional Notes

MediaDive REST medium 836 and the DSMZ Medium 836 PDF were reachable during review and agreed on the source composition.

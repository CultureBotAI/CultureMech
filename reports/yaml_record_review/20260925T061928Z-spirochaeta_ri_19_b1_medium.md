# YAML Record Review: spirochaeta_ri_19_b1_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/spirochaeta_ri_19_b1_medium.yaml
- Started UTC: 2026-09-25T06:17:29Z
- Finished UTC: 2026-09-25T06:19:29Z
- Verdict: needs curation

## Target

Generated merged YAML for TOGO M2768 / DSMZ 509a, SPIROCHAETA RI 19.B1 MEDIUM.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/spirochaeta_ri_19_b1_medium.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The record is grounded to the correct TOGO M2768 source and TOGO points to DSMZ Medium 509a.

The generated YAML does not preserve DSMZ 509a's solution hierarchy or pH 6.8-7.0 range; it flattens final additions and their referenced stocks into direct parent ingredients and empty `Unknown solution` stubs.

## Evidence

DSMZ 509a lists SPIROCHAETA RI 19.B1 MEDIUM as a solution assembly with 962 ml Solution A, 20 ml Solution B, 1 ml Solution C, 10 ml Solution D, and 10 ml Solution E. TOGO M2768 records the same medium with pH 6.8-7.0 and decomposes those named solutions into their components.

DSMZ Solution A contains 4.00 g NaCl, 0.80 g MgCl2 x 6 H2O, 0.50 g KCl, 0.30 g NH4Cl, 0.20 g KH2PO4, 0.03 g CaCl2 x 2 H2O, 1.00 ml trace element solution SL-10, 1.00 ml selenite-tungstate solution, 0.50 ml sodium resazurin, and 960.00 ml distilled water. Solution B contains 1.00 g Na2CO3 in 20.00 ml distilled water, Solution C is 1.00 ml Wolin's vitamin solution (10x), Solution D contains 1.00 g starch in 10.00 ml distilled water, and Solution E contains 0.30 g Na2S x 9 H2O in 10.00 ml distilled water.

DSMZ 509a defines trace element solution SL-10, selenite-tungstate solution, and Wolin's vitamin solution as separate stocks. The trace element stock contains gram, milligram, and 990.00 ml water rows and is brought to 1000.00 ml; the selenite-tungstate and Wolin vitamin stocks are each 1000.00 ml.

## Completeness

The generated record sums seven independent water rows into one `3980.0` `G_PER_L` distilled-water ingredient, converts DSMZ milliliter solution additions into grams per liter, converts multiple milligram stock rows into grams per liter, loses pH 6.8-7.0, and leaves all solution shells empty.

## Findings

- Major: DSMZ/TOGO solution hierarchy A through E is flattened into one parent ingredient list, with an extra empty `Solution F` stub generated from a source narrative typo.
- Major: final solution volumes such as 962 ml Solution A, 20 ml Solution B, 1 ml Solution C, 10 ml Solution D, and 10 ml Solution E are represented as `G_PER_L` concentrations.
- Major: distinct water rows from Solution A, Solution B, Solution D, Solution E, trace element solution SL-10, selenite-tungstate solution, and Wolin's vitamin solution are summed into a single impossible `3980.0` `G_PER_L` water row.
- Major: milligram stock rows are inflated to gram-per-liter scale; for example 100 mg MnCl2 x 4 H2O is imported as `100` `G_PER_L`, 190 mg CoCl2 x 6 H2O as `190` `G_PER_L`, 3 mg Na2SeO3 x 5 H2O as `3` `G_PER_L`, and 20 mg biotin from the Wolin 10x stock as `2` `G_PER_L`.
- Major: pH 6.8-7.0 from TOGO M2768 and DSMZ 509a's completion instructions is absent.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M2768_Spirochaeta_RI_19.B1_Medium.yaml` to model final additions as named Solution A through Solution E records with source milliliter volumes.
- Remove the extra Solution F artifact unless a primary source row for Solution F is found.
- Keep trace element solution SL-10, selenite-tungstate solution, and Wolin's vitamin solution as named nested stocks rather than parent ingredients.
- Restore source units for milligram stock rows and individual distilled-water rows.
- Add the pH range 6.8-7.0 and preserve the N2/CO2 and N2 sterilization instructions.
- Regenerate `data/merge_yaml/merged/spirochaeta_ri_19_b1_medium.yaml` from the repaired normalized record.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated record.
- Confirm the regenerated record has Solution A through Solution E with no Solution F stub.
- Confirm the parent ingredient list no longer contains stock rows from SL-10, selenite-tungstate, or Wolin vitamins.
- Confirm the pH range is 6.8-7.0.

## Additional Notes

None found.

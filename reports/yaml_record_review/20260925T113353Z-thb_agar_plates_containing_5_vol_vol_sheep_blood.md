# YAML Record Review: THB agar plates containing 5% (vol/vol) sheep blood

- Repository: CultureMech
- Record: data/merge_yaml/merged/thb_agar_plates_containing_5_vol_vol_sheep_blood.yaml
- Started UTC: 2026-09-25T11:29:01Z
- Finished UTC: 2026-09-25T11:33:53Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M2261, THB agar plates containing 5% (vol/vol) sheep blood.
- The record was merged from `thb_agar_plates_containing_5_vol_vol_sheep_blood`.
- The checked sources were the normalized TOGO M2261 record, the TOGO M2261 API payload, and the cited Todd Hewitt Broth product page.

## Validation

- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- TOGO M2261 cites the Todd Hewitt Broth product page and labels the record as THB agar plates containing 5% vol/vol sheep blood.
- The Todd Hewitt Broth product page supports the 20 g/L neopeptone, 3.1 g/L beef-heart infusion, 2 g/L dextrose, 2 g/L sodium chloride, 0.4 g/L disodium phosphate, 2.5 g/L sodium carbonate, and pH 7.8 +/- 0.2 values for the broth base.
- The cited product page does not provide a per-liter agar mass or a sheep-blood-agar plate formulation; those additions are present in TOGO M2261, with sheep blood specified as 5% vol/vol and agar lacking an amount.

## Evidence

- TOGO M2261 lists 1 L distilled water, 2 g sodium chloride, 2 g dextrose, 2.5 g sodium carbonate, 0.4 g disodium phosphate, 5% vol/vol sheep blood, 20 g neopeptone, 3.1 g heart infusion from 500 g, and agar with no amount.
- TOGO M2261 gives pH 7.8 +/- 0.2 and a free-text comment of growth at 37 C.
- The cited Todd Hewitt Broth product page gives the same approximate per-liter broth formula for heart infusion, neopeptone, dextrose, sodium chloride, disodium phosphate, and sodium carbonate.

## Completeness

- The Todd-Hewitt broth powder rows match the cited product page.
- The pH 7.8 +/- 0.2 value is missing.
- The TOGO 1 L water row is typed as 1 G_PER_L water.
- The TOGO 5% vol/vol sheep-blood row is typed as 5 G_PER_L.
- Agar remains variable because the TOGO payload names agar without an amount and the cited Todd-Hewitt broth page does not supply one.

## Findings

- Sheep blood has a unit error: TOGO specifies 5% vol/vol, but the merged YAML stores `5 G_PER_L`.
- Distilled water has a unit error: TOGO specifies 1 L, but the merged YAML stores `1 G_PER_L`.
- The record dropped TOGO's pH 7.8 +/- 0.2 metadata.
- The record is named and typed as solid agar, but the cited store page is for Todd Hewitt Broth and does not verify a specific agar amount for sheep-blood plates.

## Recommended Edits

- Preserve TOGO's 5% vol/vol sheep-blood unit instead of converting it to G_PER_L.
- Preserve the 1 L distilled-water row as a volume or omit it deliberately rather than encoding it as 1 G_PER_L.
- Add pH 7.8 +/- 0.2 from the TOGO payload.
- Keep Agar as variable or unresolved unless a plate-specific source supplies a defensible per-liter agar concentration.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Recheck the exact TOGO M2261 source if a future source import adds an agar mass so the record can be resolved without borrowing a generic agar-plate concentration.

## Additional Notes

- None found.

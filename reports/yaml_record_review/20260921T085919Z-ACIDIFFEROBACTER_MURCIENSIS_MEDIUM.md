# YAML Record Review: acidifferobacter_murciensis_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml`
- Started UTC: 2026-09-21T08:58:12Z
- Finished UTC: 2026-09-21T08:59:19Z
- Verdict: needs curation

## Target

Generated merge record `ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml` is a singleton merge from `data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml`. It represents TOGO M1020, whose original source is JCM Medium 970 / ACIDIFFEROBACTER MURCIENSIS MEDIUM.

## Validation

- PASS: open LinkML schema validation with `linkml-validate`.
- PASS: strict schema layer validation with `scripts/validate_strict.py`.
- PASS: linkml-reference-validator on this generated record.
- PASS: linkml-term-validator on this generated record.
- Not checked: embedded `MediaRecipe.curation_history` entries; no focused generated-record history validator is documented, and `just validate-history` targets standalone `history/` files.

## Identity and Grounding

TOGO M1020 and the direct MediaDive/JCM J970 import refer to the same JCM medium. The ignored-inclusive exact source-ID search found one normalized record for exact `TOGO:M1020`, one normalized record for exact `mediadive.medium:J970`, and two generated outputs: this TOGO singleton and `acidifferobacter_murciensis_medium__18078015.yaml` for the direct JCM import.

The live JCM `GRMD=970` page now returns `Nothing found`, so the current retrievable primary recipe for this source is TOGO's archived M1020 snapshot. That snapshot still names `JCM_M970`, points at `GRMD=970`, and preserves the old component units needed to audit the CultureMech conversion.

## Evidence

- TOGO M1020 API fetched during review: its basal block lists 900 ml distilled water; CaCl2.2H2O, KH2PO4, MgCl2.6H2O, and `(NH4)2SO4` in milligrams; Na2MoO4.2H2O, H3BO3, MnCl2.4H2O, CoCl2.6H2O, CuCl2.2H2O, and ZnCl2 in micrograms; a 100 ml Iron(II) sulfate solution; and a 10 N H2SO4 pH-adjustment component. Its separate Iron(II) sulfate solution block contains 100 ml distilled water, 20 g FeSO4.7H2O, and 2 ml concentrated H2SO4.
- TOGO comments: pH adjustment to 2.0 with 10 N H2SO4 and post-autoclave addition of the separately autoclaved iron sulfate solution are present in the API response.
- Direct JCM normalized record `data/normalized_yaml/bacterial/acidifferobacter_murciensis_medium.yaml`: carries `mediadive.medium:J970`, pH 2.0, and the preparation text but is generated separately from the TOGO snapshot.

## Completeness

The generated target keeps recognizable ingredient labels but loses the source's unit scales and stock boundary. It is not a usable representation of TOGO M1020 because most basal salts are orders of magnitude too concentrated, the 100 ml iron sulfate stock addition is represented as `100 G_PER_L`, and the FeSO4 / concentrated H2SO4 stock recipe was also flattened into final top-level rows.

The target also has no `ph_value` and no `preparation_steps`, even though TOGO records the pH 2.0 adjustment and the timing of the separately autoclaved iron stock addition.

## Findings

- CRITICAL: Milligram and microgram source rows were stored as unconverted `G_PER_L` values. Examples from TOGO M1020 include `CaCl2.2H2O 147 mg` becoming `147 G_PER_L`, `KH2PO4 27.2 mg` becoming `27.2 G_PER_L`, `Na2MoO4.2H2O 12.1 ug` becoming `12.1 G_PER_L`, and `ZnCl2 70 ug` becoming `70 G_PER_L`.
- CRITICAL: The Iron(II) sulfate stock was flattened into the final medium. TOGO calls for 100 ml of a separately prepared solution containing 20 g FeSO4.7H2O plus 2 ml concentrated H2SO4 in 100 ml water; the generated target keeps an empty `Iron(II) sulfate solution` at `100 G_PER_L` and lifts the 20 g / 2 ml stock recipe to final top-level ingredients.
- MAJOR: TOGO M1020 and the direct JCM J970 import are the same archived `GRMD=970` recipe but remain split into two generated records because their stock handling, pH handling, water handling, and unit conversions diverge.
- MAJOR: Water volumes were merged into a concentration. The 900 ml basal water and 100 ml stock water became a single `Distilled water` row at `1000.0 G_PER_L`; the 100 ml stock water should not be folded into the final basal volume row.
- MAJOR: The target drops pH 2.0 and the instruction that the iron sulfate solution is separately autoclaved and added only after the basal medium is autoclaved.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml` from the TOGO component units: convert mg and ug basal salts to the correct gram-scale concentrations, preserve 900 ml water as a volume row if retained at all, and represent 100 ml Iron(II) sulfate solution as a stock addition rather than flattening its formula.
- Move the 20 g FeSO4.7H2O, 2 ml concentrated H2SO4, and 100 ml water rows into the `Iron(II) sulfate solution` composition.
- Restore `ph_value: 2.0` and the autoclave / post-autoclave iron-stock `preparation_steps` from the TOGO comment.
- Correct the direct JCM J970 normalized source to the same representation and regenerate merged YAML so `TOGO_M1020_Acidifferobacter_Murciensis_Medium` and `acidifferobacter_murciensis_medium` merge.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the corrected TOGO and JCM normalized records.
- Re-run an ignored-inclusive exact search for `TOGO:M1020`, `mediadive.medium:J970`, and `GRMD=970` after regeneration to confirm there is one generated JCM 970 recipe.
- Verify the regenerated target has no microgram or milligram rows preserved numerically as gram-per-liter rows and no empty Iron(II) sulfate solution.

## Additional Notes

The direct JCM normalized record is not a trustworthy fallback for concentration arithmetic: it fixed some milligram-to-gram conversions but still has multiple old microgram-scale TOGO/JCM rows as `G_PER_L` and the same iron-stock flattening pattern.

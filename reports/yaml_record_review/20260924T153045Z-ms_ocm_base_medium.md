# YAML Record Review: ms_ocm_base_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ms_ocm_base_medium.yaml
- Started UTC: 2026-09-24T15:29:03Z
- Finished UTC: 2026-09-24T15:30:45Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:009199 |
| Name | ms_ocm_base_medium |
| Original name | MS-OCM Base Medium |
| Category | bacterial |
| Source identity | TOGO:M2642, imported from ATCC Medium 2467 |
| Reviewed artifact | Generated merge output |
| Maintained owner | data/normalized_yaml/bacterial/ms_ocm_base_medium.yaml |
| Merge status | One source recipe; `merged_from: ms_ocm_base_medium` |

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate` | Passed; `No issues found` |
| Strict validation with `scripts/validate_strict.py` | Passed with 0 errors |
| Reference validation with `linkml-reference-validator` | Passed; 0 reference checks |
| Term validation with `linkml-term-validator` | Passed |
| Embedded `curation_history` validation | Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML |

## Identity and Grounding

The source identity is correct. TOGO `M2642` is `MS-OCM Base Medium`, points to the ATCC Medium 2467 PDF, and the original ATCC URL still resolves to `ATCC Medium 2467.pdf`.

An exact gitignore-independent search for `CultureMech:009199`, `TOGO:M2642`, `https://togomedium.org/medium/M2642`, and the ATCC PDF hash under `data/normalized_yaml` and `data/merge_yaml` found only the maintained owner, this generated merge record, and generated indexes. No sibling TOGO M2642 record was found in those record corpora.

The imported record does not preserve ATCC's stock-solution structure. ATCC Medium 2467 starts with 8.4 g sodium bicarbonate in 976 ml DI water, then adds 10 ml of Solution A, 2 ml of Solution B, and later 2 ml of Solution C and 10 ml ATCC MD-TMS per liter. The YAML instead stores Solution A, B, C, and ATCC MD-TMS as `G_PER_L` rows and also flattens those stock-solution ingredients into the final recipe without volume scaling.

## Evidence

Supported source claims:

- TOGO M2642 and ATCC Medium 2467 support the `MS-OCM Base Medium` label and the ATCC PDF provenance.
- ATCC supports the initial 8.4 g sodium bicarbonate plus 976 ml DI water base, N2-CO2 gassing, 2 g yeast extract, 2 g Trypticase peptones, pH 7.0-7.3 before tube transfer, and 121 C autoclaving.
- ATCC supports Solution A as a 100x stock added at 10 ml/L, Solution B as a 500x stock added at 2 ml/L, Solution C as a 500x stock added at 2 ml/L, and Co-enzyme M, sodium sulfide, and cysteine as separate 100x reducing-agent stocks.

Unsupported or incorrectly flattened generated claims:

- The `DI Water` row is `4276.0 G_PER_L`, from merging 976 ml final water with three 1 L stock-water rows and three 100 ml stock-water rows.
- Solution A, Solution B, Solution C, ATCC MD-TMS, and Co-enzyme M stock additions are represented as `G_PER_L` solutes even though ATCC gives their additions in milliliters per liter or as standalone 100x stock recipes.
- The YAML stores Solution A stock concentrations as final concentrations: 100 g/L ammonium chloride, 100 g/L magnesium chloride hexahydrate, and 40 g/L calcium chloride dehydrate.
- The YAML stores Solution B's stock concentration, 200 g/L potassium dibasic phosphate trihydrate, as a final concentration.
- The pH 7.0-7.3 checkpoint and most preparation operations are missing from structured fields.

## Completeness

The ATCC ingredient names are mostly present, but their preparation boundaries are missing. MS-OCM Base Medium cannot be curated as one flat ingredient list without distinguishing the final base, 100x stocks, 500x stocks, ATCC MD-TMS, and optional reducing-agent stocks.

Consequential gaps:

- Seven water rows from final and stock recipes have been merged into one impossible final concentration.
- 100x and 500x stock contents are not scaled to their final-medium additions.
- The ATCC pH range and gassing/autoclaving/dispensing/storage instructions were left as source comments and are not represented in YAML.
- Legacy `mediaingredientmech_term` entries remain for Calcium chloride dehydrate, Mercaptoethanesulfonic acid, and Sodium sulfide nonahydrate.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Stock-solution water rows are merged into an impossible final water concentration. | ATCC lists 976 ml DI water for the base, up to 1000 ml for Solution A, up to 1000 ml for Solution B, up to 1000 ml for Solution C, and three reducing-agent stocks made in 100 ml DI water; the YAML adds those seven water rows to `4276.0 G_PER_L`. | data/normalized_yaml/bacterial/ms_ocm_base_medium.yaml |
| Major | Solution and supplement volumes are represented as grams per liter. | ATCC adds 10 ml Solution A, 2 ml Solution B, 2 ml Solution C, and 10 ml ATCC MD-TMS per liter; the YAML stores `Solution A` as `10 G_PER_L`, `Solution B` as `2 G_PER_L`, `Solution C` as `2 G_PER_L`, and `Trace Mineral Supplement, ATCC MD-TMS` as `10 G_PER_L`. | data/normalized_yaml/bacterial/ms_ocm_base_medium.yaml |
| Major | Stock concentrations are flattened without 100x or 500x dilution. | Solution A is a 100x stock and Solution B/C are 500x stocks, but the YAML stores 100 g/L NH4Cl, 100 g/L magnesium chloride hexahydrate, 40 g/L calcium chloride dehydrate, 200 g/L potassium dibasic phosphate trihydrate, and full-strength Solution C resazurin as final concentrations. | data/normalized_yaml/bacterial/ms_ocm_base_medium.yaml |
| Major | The source pH range and procedure are missing. | ATCC states the clear medium should be between pH 7 and pH 7.3 and describes N2-CO2 gassing, continuous gassing during dispensing, capped/crimped tubes, and autoclaving at 121 C; the YAML has no `ph_range` or `preparation_steps`. | data/normalized_yaml/bacterial/ms_ocm_base_medium.yaml |
| Minor | Three legacy MediaIngredientMech IDs survived the CHEBI-keyed migration. | The record still has `mediaingredientmech_term` entries for Calcium chloride dehydrate, Mercaptoethanesulfonic acid, and Sodium sulfide nonahydrate after a 2026-06-05 history event says legacy MediaIngredientMech IDs were replaced with CHEBI-keyed links. | data/normalized_yaml/bacterial/ms_ocm_base_medium.yaml |

## Recommended Edits

1. Reconstruct `data/normalized_yaml/bacterial/ms_ocm_base_medium.yaml` from ATCC Medium 2467 with explicit final-medium additions for Solution A, Solution B, Solution C, ATCC MD-TMS, Co-enzyme M, sodium sulfide, and cysteine instead of flat stock contents.
2. Keep Solution A, Solution B, Solution C, and each 100x reducing-agent recipe behind solution boundaries or scale their ingredients to final-medium units with the source dilution factors.
3. Replace the merged `DI Water` row with source-scoped water quantities or remove stock waters from the final ingredient list.
4. Add the pH 7.0-7.3 checkpoint and ATCC gassing, dispensing, autoclaving, and storage steps as `preparation_steps`.
5. Convert remaining `mediaingredientmech_term` entries to CHEBI-keyed links where an exact ChEBI grounding exists.
6. Rerun the merge generator so the generated `ms_ocm_base_medium.yaml` reflects the repaired owner.

## Follow-up Checks

1. Re-run open schema, strict, reference, and term validation on the regenerated merged record.
2. Diff the regenerated recipe against the ATCC Medium 2467 PDF and TOGO M2642, with explicit checks for the 10 ml/L, 2 ml/L, and 100x/500x dilution semantics.
3. Confirm the regenerated record has a pH range of 7.0-7.3 and no merged `4276.0 G_PER_L` water row.
4. Run the exact gitignore-independent `TOGO:M2642` and ATCC-PDF duplicate search again after regeneration to make sure no sibling source record was introduced.

## Additional Notes

- The ATCC source URL resolves through a case-normalizing redirect and returns `ATCC Medium 2467.pdf`.
- The exact duplicate search above included ignored files.

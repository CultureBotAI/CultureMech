# YAML Record Review: medium_1_liquid_with_20_horse_serum

- Repository: CultureMech
- Record: data/merge_yaml/merged/medium_1_liquid_with_20_horse_serum.yaml
- Started UTC: 2026-09-24T01:09:44Z
- Finished UTC: 2026-09-24T01:10:47Z
- Verdict: needs curation

## Target

Reviewed generated merged record `data/merge_yaml/merged/medium_1_liquid_with_20_horse_serum.yaml` for TOGO medium M2200. Exact `find` over `data/normalized_yaml` with ignored files included found one owner: `data/normalized_yaml/bacterial/medium_1_liquid_with_20_horse_serum.yaml`.

Exact `TOGO:M2200` scans over the generated record, the owner, and normalized indexes included ignored files and found only this record family and the matching bacterial/recipe index entries.

## Validation

- Open LinkML validation against `src/culturemech/schema/culturemech.yaml` as `MediaRecipe`: passed with `No issues found`.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows; the strict TSV had a header only.
- LinkML reference validation: passed; 0 reference checks were emitted for this file.
- LinkML term validation with labels and `conf/oak_config.yaml`: passed.
- Embedded `curation_history`: Not checked. The repository `just validate-history` target validates standalone `history/` files rather than embedded generated-record history blocks.

## Identity and Grounding

`media_term.term.id` is `TOGO:M2200`, matching the TOGO API response for `Medium 1 liquid, with 20 % horse serum`. M2200 uses DSMZ Medium 1 as its base and adds 20% horse serum. DSMZ Medium 1 and MediaDive medium 1 define Peptone 5 g/L, Meat extract 3 g/L, Agar 15 g/L if necessary, water to 1000 ml, and pH 7.0.

The normalized owner was repaired on 2026-09-12, after this generated record was last merged. The owner now carries a `RESOLVED_TOGO_M2200_SCORE15` event, structured references to TOGO M2200 and DSMZ Medium 1, `ph_value: 7.0`, an `ADJUST_PH` step, a supplemented-variant link to `nutrient_agar`, and corrected units for Horse serum and Distilled water.

## Evidence

The generated record is stale relative to the repaired normalized owner:

- `Horse serum` is still `20 PERCENT_W_V`; the owner corrected it to `20.0 PERCENT_V_V`, which better represents a serum liquid supplement.
- `Distilled water` is still `1000 G_PER_L`; the owner corrected the source `1000 ml` to `1.0 L`.
- pH 7.0 from TOGO/DSMZ is absent from the generated record.
- The generated record lacks the owner preparation step `Adjust pH to 7.0.`
- The generated record lacks the parent/variant relationship to DSMZ Medium 1 through `nutrient_agar`.
- The generated `Peptone` row remains ungrounded; the owner grounds it to `MICRO:0000178`.

## Completeness

All five TOGO M2200 component rows are present, but two use obsolete units in generated output and the pH/preparation evidence is incomplete. The source name contains `liquid` while TOGO retains the DSMZ Medium 1 agar row; the owner documents this ambiguity, but the generated record does not.

`Meat extract` and `Horse serum` remain intentionally unmapped in the normalized owner because they are generic complex materials.

## Findings

1. `needs curation` - The generated record is stale and predates the targeted 2026-09-12 repair of TOGO M2200.
2. `needs curation` - `Horse serum` is represented as weight/volume percent rather than volume/volume percent in generated output.
3. `needs curation` - `Distilled water` is represented as 1000 g/L instead of the source 1000 ml final volume.
4. `minor` - The generated record omits pH 7.0, its `ADJUST_PH` preparation step, the DSMZ Medium 1 supplemented-variant relationship, structured source references, and the repaired Peptone grounding.

## Recommended Edits

Regenerate the merged record from `data/normalized_yaml/bacterial/medium_1_liquid_with_20_horse_serum.yaml` so it inherits the M2200 repair event, pH 7.0, percent v/v serum unit, water unit, references, parent-media relationship, and Peptone grounding.

After regeneration, explicitly review whether the agar row and `SOLID_AGAR` state should remain on a source recipe named `Medium 1 liquid, with 20 % horse serum`; the source currently carries both the liquid name and the DSMZ Medium 1 agar row.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validators on the regenerated merged record.
- Confirm `Horse serum` uses `PERCENT_V_V`.
- Confirm `Distilled water` no longer uses `G_PER_L`.
- Confirm pH 7.0, source references, and the `nutrient_agar` parent relationship survive the merge.
- Re-check `TOGO:M2200` in normalized source indexes with ignored files included.

## Additional Notes

The TOGO M2200 API response, DSMZ Medium 1 PDF, and MediaDive medium 1 REST/rendered pages were inspected directly.

# YAML Record Review: diluted_marine_agar

- Repository: CultureMech
- Record: `data/merge_yaml/merged/diluted_marine_agar__46d2ab80.yaml`
- Started UTC: 2026-09-22T22:04:29Z
- Finished UTC: 2026-09-22T22:05:18Z
- Verdict: needs curation

## Target

`CultureMech:015411` represents JCM Medium J644, `DILUTED MARINE AGAR`, from MediaDive's JCM import. The generated record is a single-source merge from `data/normalized_yaml/specialized/diluted_marine_agar.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

JCM J644 and TOGO M658 both point to the same JCM Medium 644 page. A gitignore-independent `find` over `data/` found this specialized JCM generated record, a separate bacterial TOGO `Diluted_Marine_Agar` generated record, the repaired specialized normalized record, the unrepaired bacterial TOGO normalized record, and many other Marine Agar variants. This JCM import and the TOGO M658 import should converge after the TOGO-side volume units are repaired and the generated records are rebuilt.

## Evidence

- The live JCM 644 page lists 3.74 g Marine broth 2216 from BD-Difco, 15.0 g agar, 750.0 ml filtered seawater, and 250.0 ml distilled water.
- JCM states that, unless otherwise noted, media are autoclaved at 121 C for 15 min.
- The live MediaDive J644 REST payload preserves the same four-row 1000 ml recipe with filtered seawater as 750 ml and distilled water as 250 ml.
- The normalized specialized source was repaired in September 2026 to represent `Filtered seawater` and `Distilled water` as `750` and `250` `ML_PER_L`, to keep Marine broth 2216 with its BD-Difco attribution, and to add a JCM autoclave step.

## Completeness

The generated record is stale relative to the repaired normalized specialized source. Its Marine broth and agar rows match JCM, but the two source volume rows are not both represented correctly.

## Findings

- `Filtered seawater` was emitted as `Sea water` at `750 G_PER_L`, but the source row is 750 ml per liter.
- The 250 ml distilled-water row is absent from generated YAML.
- The JCM default autoclave instruction is absent from the generated record.
- TOGO M658 points to the same JCM 644 source but still has both water rows as `G_PER_L` in its bacterial normalized and generated records, preventing this specialized import from converging with it.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/diluted_marine_agar__46d2ab80.yaml` from the repaired specialized normalized record.
- Repair `data/normalized_yaml/bacterial/diluted_marine_agar.yaml` so its 750 ml filtered seawater and 250 ml distilled-water rows use `ML_PER_L`.
- Merge or otherwise link the JCM J644 and TOGO M658 records as source duplicates after both normalized sources carry equivalent ingredient units.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that filtered seawater and distilled water are both emitted as milliliter-per-liter values.
- Verify that the generated JCM and TOGO Diluted Marine Agar records converge or carry an explicit source-duplicate relationship.

## Additional Notes

None found.

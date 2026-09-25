# YAML Record Review: peptone_czapeks_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/peptone_czapeks_agar.yaml
- Started UTC: 2026-09-24T20:22:55Z
- Finished UTC: 2026-09-24T20:22:55Z
- Verdict: needs curation

## Target

Generated bacterial MediaRecipe `CultureMech:009965`, `peptone_czapeks_agar`, from the maintained TOGO owner `data/normalized_yaml/bacterial/peptone_czapeks_agar.yaml`.

The record represents TOGO M56, Peptone-Czapek's Agar, derived from JCM `JCM_M64` / GRMD 64. Its generated recipe contains distilled water, 0.5 g/L MgSO4 x 7 H2O, 1 g/L K2HPO4, 10 g/L FeSO4 x 7 H2O, 0.5 g/L KCl, 30 g/L sucrose, 15 g/L agar, and 5 g/L Bacto peptone.

## Validation

- Open LinkML validation: Passed with no issues.
- Strict validator: Passed; `/private/tmp/peptone_czapeks_agar.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The TOGO identity is internally consistent: `TOGO:M56`, the `JCM_M64` original media ID, and the JCM `GRMD=64` source URL all refer to Peptone-Czapek's Agar.

An exact ignored-inclusive search found a separate generated direct MediaDive/JCM record, `data/merge_yaml/merged/peptone_czapeks_agar__a8441710.yaml`, from `data/normalized_yaml/fungal/peptone_czapeks_agar.yaml`. That sibling uses `mediadive.medium:J64` and the same JCM `GRMD=64` source URL, and therefore appears to be the same source recipe rather than a distinct medium.

## Evidence

The TOGO M56 API payload supports the source identity and lists a 1 L distilled water row, 0.5 g MgSO4 x 7 H2O, 1 g K2HPO4, 10 mg FeSO4 x 7 H2O, 0.5 g KCl, 30 g sucrose, 15 g agar, and 5 g Bacto peptone in the main solution.

The JCM `GRMD=64` page currently returns "Nothing found"; the preserved TOGO payload and the direct MediaDive/JCM J64 CultureMech owner are therefore the available mirrors for this JCM recipe.

Most grounding choices are appropriate: K2HPO4, KCl, sucrose, agar, magnesium sulfate heptahydrate, and iron(2+) sulfate heptahydrate match their source strings, and the BD-Difco Bacto peptone is correctly left ungrounded as a commercial complex ingredient.

## Completeness

The generated record preserves each TOGO M56 row and carries the expected TOGO/JCM source notes, but the maintained owner has converted two TOGO quantities into the wrong normalized units.

The same JCM `GRMD=64` recipe is also split into the direct MediaDive/JCM generated sibling `peptone_czapeks_agar__a8441710`; that sibling has the correct 0.01 g/L FeSO4 x 7 H2O concentration but omits the source 1 L water row.

## Findings

1. Needs curation: `Distilled water` is encoded as `1 G_PER_L` even though TOGO M56 supplies `1 L`.
2. Needs curation: `FeSO4 x 7 H2O` is encoded as `10 G_PER_L` even though TOGO M56 supplies `10 mg`; the normalized concentration for the 1 L recipe should be 0.01 g/L.
3. Needs curation: JCM `GRMD=64` is represented twice in generated YAML. This TOGO M56 record and the direct MediaDive/JCM J64 sibling should collapse into one generated source-duplicate record after unit and water normalization.

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/peptone_czapeks_agar.yaml` so `Distilled water` keeps the source 1 L volume without grams-per-liter units.
2. Convert `FeSO4 x 7 H2O` to `0.01 G_PER_L` in the TOGO owner.
3. Add the missing 1 L water row to `data/normalized_yaml/fungal/peptone_czapeks_agar.yaml`.
4. Regenerate merged YAML and verify the TOGO M56 and MediaDive/JCM J64 owners merge as source duplicates.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owners and regenerated merged record.
2. Repeat an exact ignored-inclusive search for `TOGO:M56`, `mediadive.medium:J64`, and `GRMD=64` after regeneration to confirm the JCM 64 recipe is represented once in `data/merge_yaml/merged/`.

## Additional Notes

The exact ignored-inclusive duplicate search covered `data`, `src`, and `scripts` for `TOGO:M56`, `JCM_M64`, `GRMD=64`, `CultureMech:009965`, and `peptone_czapeks_agar`.

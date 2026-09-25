# YAML Record Review: HD-MEDIUM, 1:10 diluted, modified
- Repository: CultureMech
- Record: data/merge_yaml/merged/hd_medium_1_10_diluted_modified__33364d2d.yaml
- Started UTC: 2026-09-23T11:41:39Z
- Finished UTC: 2026-09-23T11:42:04Z
- Verdict: needs curation

## Target

Reviewed the direct DSMZ/MediaDive branch for DSMZ Medium 1135, `HD-MEDIUM, 1:10 diluted, modified`, at `data/merge_yaml/merged/hd_medium_1_10_diluted_modified__33364d2d.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hd_medium_1_10_diluted_modified__33364d2d.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `mediadive.medium:1135` and retains DSMZ Medium 1135's title and pH 5.5. It is a direct MediaDive import rather than the KOMODO-derived duplicate at `data/merge_yaml/merged/hd_medium_1_10_diluted_modified.yaml`.

## Evidence

MediaDive 1135 and the DSMZ PDF both describe Solution A with casein peptone 0.50 g, glucose 0.10 g, yeast extract 0.25 g, MES 1.95 g, water alternatives for liquid and solid medium, and Solution B as 1.5% washed agar with 500 ml double-distilled water. The source says to adjust to pH 5.5 with NaOH/HCl, sterilize separately, combine Solution A with Solution B at 50 C for solid medium, and incubate at 20 C for 4 days.

The generated record collapses the 1000 ml liquid-medium water, 500 ml solid-medium Solution A water, and 500 ml Solution B water into `Double distilled water` at `2000.0 G_PER_L` with a duplicate-merge note. It retains `Agar` at 15 g/L and three free-text preparation steps.

## Completeness

The core solutes, pH, medium term, and DSMZ preparation sentences are present. The structured recipe is incomplete because the liquid and solid branches are not represented, Solution B is not retained as a solid-only solution, and water volumes are no longer scoped to their respective branches.

## Findings

- Mutually exclusive water rows were summed into a nonsensical `2000.0 G_PER_L` water ingredient. The DSMZ liquid recipe contains 1000 ml water in Solution A; the solid recipe contains 500 ml water in Solution A plus 500 ml water in Solution B.
- `Agar` is unconditional, although DSMZ only uses the washed-agar Solution B when preparing solid medium.
- The source's Solution A/Solution B structure was flattened away, so downstream users cannot reconstruct the separate sterilization and 50 C combination workflow from structured slots.
- Preparation step 3 is typed as `HEAT`, but its text is the incubation note `Liquid and solid medium possible. Incubation at 20 C, 4 days.` rather than a sterilization or heating step.
- This direct DSMZ record remains separate from the KOMODO-derived DSMZ 1135 branch with the same source recipe.

## Recommended Edits

- Split DSMZ Medium 1135 into liquid and solid alternatives or preserve explicit solution/condition scopes so duplicate water normalization cannot add liquid and solid rows together.
- Keep agar scoped to the solid-medium preparation.
- Represent Solution A and Solution B as distinct recipe components or preparation-scoped additions.
- Reclassify the incubation note instead of importing it as a generic `HEAT` preparation step.
- Merge or alias this direct DSMZ branch with the KOMODO branch after both are regenerated from the same scoped DSMZ representation.

## Follow-up Checks

- Re-run merge generation and confirm only one DSMZ Medium 1135 record remains.
- Confirm the regenerated liquid branch sums to a 1 L Solution A and the solid branch combines 500 ml Solution A with 500 ml Solution B.

## Additional Notes

None.

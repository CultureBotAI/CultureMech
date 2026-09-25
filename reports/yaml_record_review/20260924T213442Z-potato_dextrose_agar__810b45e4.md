# YAML Record Review: potato_dextrose_agar__810b45e4

- Repository: CultureMech
- Record: data/merge_yaml/merged/potato_dextrose_agar__810b45e4.yaml
- Started UTC: 2026-09-24T21:34:42Z
- Finished UTC: 2026-09-24T21:34:42Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:008284
- Name: potato_dextrose_agar
- Source import: TOGO_M1721_Potato_Dextrose_Agar
- Primary external ID: TOGO:M1721
- Maintained input: data/normalized_yaml/bacterial/TOGO_M1721_Potato_Dextrose_Agar.yaml

This generated record represents TOGO Medium M1721 / NBRC Medium 930, Potato Dextrose Agar made from Nissui dehydrated PDA.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/potato_dextrose_agar__810b45e4.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct TOGO M1721 / NBRC 930 identity. TOGO M1721 imports NBRC_M930, and the NBRC Medium 930 page lists the same two-row commercial Potato Dextrose Agar recipe.

Exact ignored-file searches across `data` for `TOGO:M1721`, `medium/M1721`, `gm_id=M1721`, `NBRC_M930`, `NO=930`, `TOGO_M1721_Potato_Dextrose_Agar`, and `Nissui Potato Dextrose Agar` found one normalized YAML recipe, this merged YAML record, and generated index/tracking references to that same recipe; no second exact NBRC 930 / TOGO M1721 recipe was found.

The generated merge is stale. Its maintained `data/normalized_yaml/bacterial/TOGO_M1721_Potato_Dextrose_Agar.yaml` input has a later `RESOLVED_TOGO_COMMERCIAL_SCORE20_GRAPH` repair that corrected the 1 L water row to 1000 ML_PER_L, added source references, and added a preparation step to suspend 39 g Nissui Potato Dextrose Agar in 1 L distilled water.

## Evidence

- TOGO M1721 lists 1 L distilled water and 39 g Nissui Potato Dextrose Agar.
- NBRC 930 lists 39 g Nissui Potato Dextrose Agar and 1 L distilled water.
- Neither inspected source page lists a pH, temperature, or separate preparation note beyond the commercial formulation itself.

## Completeness

The generated record is incomplete against the already-corrected maintained input: it still imports source water as `1 G_PER_L`, omits source references, and lacks the maintained preparation step.

## Findings

1. Major: The generated merged record is stale relative to `data/normalized_yaml/bacterial/TOGO_M1721_Potato_Dextrose_Agar.yaml`; future repair belongs in regeneration from that maintained normalized recipe.
2. Major: The stale merge misrepresents the source 1 L distilled water row as 1 G_PER_L.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/potato_dextrose_agar__810b45e4.yaml` from the already-corrected TOGO M1721 normalized YAML so the 1000 ML_PER_L water row, NBRC 930 references, and commercial-PDA preparation step propagate into the generated record.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `TOGO:M1721`, `NBRC_M930`, and `NO=930` with ignored files included before adding any new NBRC 930 import.
- Spot-check the regenerated page to ensure it renders 39 g Nissui Potato Dextrose Agar in 1 L distilled water.

## Additional Notes

None found.

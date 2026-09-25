# YAML Record Review: kiritimatiella_tyg_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/kiritimatiella_tyg_medium.yaml
- Started UTC: 2026-09-23T17:44:40Z
- Finished UTC: 2026-09-23T17:45:23Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:000999`, the generated `kiritimatiella_tyg_medium` record merged from `data/normalized_yaml/bacterial/kiritimatiella_tyg_medium.yaml`. The record represents DSMZ `1526b`, "KIRITIMATIELLA (TYG) MEDIUM", as a bacterial, complex, undefined, liquid medium.

## Validation

- LinkML open schema validation passed for `data/merge_yaml/merged/kiritimatiella_tyg_medium.yaml`.
- Strict validation passed with 0 error rows in `/private/tmp/kiritimatiella_tyg_medium.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` entries were not checked: the available history validator validates standalone files under `history/`, not embedded generated YAML history.

## Identity and Grounding

An ignored-inclusive exact search for `CultureMech:000999`, `mediadive.medium:1526b`, and `DSMZ_Medium1526b` found the DSMZ owner, this generated record, and index/manifest metadata for the exact source. No exact local duplicate of DSMZ 1526b was found.

The record is grounded to the DSMZ PDF and MediaDive `1526b`. The generated YAML was produced on 2026-08-06 and is stale relative to the 2026-08-07 `apply_cocktail_nesting.py` repair on the normalized owner.

## Evidence

DSMZ Medium 1526b lists a 1002 ml final volume with 60 g Sea Salt, 1 ml Wolfe's mineral elixir, 1 g Trypticase peptone, 1 g yeast extract, 1 g glucose, 0.5 ml sodium resazurin 0.1% w/v, 1 g Na2CO3, 1 ml Wolin's vitamin solution (10x), 0.5 g L-Cysteine HCl x H2O, 0.5 g Na2S x 9 H2O, and 1000 ml distilled water. It separately provides a 1 L Wolfe's mineral elixir stock, a 1 L Wolin's vitamin stock, and an anoxic preparation sequence with 80% N2 / 20% CO2 and 100% N2 stock preparation.

## Completeness

The main ingredients, pH range, and principal anoxic preparation paragraph are present. The source stock structure is not represented in the generated file, the later partial stock nesting on the owner has not been regenerated into the merge output, and the 1000 ml distilled-water main-solvent row is absent.

## Findings

- The generated record has no `solutions`, despite DSMZ and MediaDive both representing Wolfe's mineral elixir and Wolin's vitamin solution as 1 ml stock additions.
- All Wolfe and Wolin stock components are flattened into top-level `ingredients` at stock strength. For example, the generated record stores `MgSO4 x 7 H2O` as `30 G_PER_L` and `Biotin` as `0.02 G_PER_L`, but those are 1 L stock concentrations added to the final recipe at only 1 ml/l.
- `data/normalized_yaml/bacterial/kiritimatiella_tyg_medium.yaml` already moved five stock-strength rows into two `solutions` after this generated record was produced, so the current generated output is stale.
- The normalized owner repair is still partial: several Wolfe minerals and most Wolin vitamins remain top-level ingredients even though the DSMZ PDF scopes them to the two stock solutions.
- The Wolfe mineral elixir pH step, "First adjust pH to 1.0 with diluted H2SO4, then add and dissolve the salts", is promoted as a top-level Kiritimatiella TYG preparation step instead of being scoped to the Wolfe stock.
- The DSMZ 1000 ml distilled-water row is absent.

## Recommended Edits

- Finish the normalized-owner repair so all Wolfe's mineral elixir and Wolin's vitamin solution components are nested under the two 1 ml/l stock additions.
- Scope the pH 1.0 mineral-elixir instruction to the Wolfe stock preparation, not the final TYG medium.
- Keep the main DSMZ anoxic preparation step at the final medium level.
- Regenerate `data/merge_yaml/merged/kiritimatiella_tyg_medium.yaml` after the owner repair so it no longer contains the stale fully flattened ingredient list.

## Follow-up Checks

- Re-run the open schema, strict, reference, and term validators against regenerated Kiritimatiella TYG.
- Confirm the regenerated record contains two `solutions`, each with `1 ML_PER_L`, rather than top-level stock components.
- Confirm no Wolin vitamin or Wolfe mineral stock-only row remains in top-level `ingredients`.

## Additional Notes

The exact search included ignored files and hidden files.

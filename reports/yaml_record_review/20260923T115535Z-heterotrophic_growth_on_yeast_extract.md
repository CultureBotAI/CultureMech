# YAML Record Review: Heterotrophic growth on Yeast extract
- Repository: CultureMech
- Record: data/merge_yaml/merged/heterotrophic_growth_on_yeast_extract.yaml
- Started UTC: 2026-09-23T11:54:56Z
- Finished UTC: 2026-09-23T11:55:35Z
- Verdict: needs curation

## Target

Reviewed the generated KOMODO/DSMZ 709 merge at `data/merge_yaml/merged/heterotrophic_growth_on_yeast_extract.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/heterotrophic_growth_on_yeast_extract.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The generated record keeps the `komodo.medium:709.1` identity for heterotrophic growth on yeast extract but also merges `komodo.medium:709` and `komodo.medium:709.2` into the same final record. KOMODO 709 and 709.1 map to the DSMZ Medium 709 base/heterotrophic formulation; KOMODO 709.2 is DSMZ Medium 709's autotrophic ferrous-sulfate variant and should not collapse into the yeast-extract branch.

## Evidence

DSMZ Medium 709 lists the pH 2.0 heterotrophic medium with 0.5 g/L magnesium sulfate heptahydrate, 0.4 g/L ammonium sulfate, 0.2 g/L K2HPO4, 0.1 g/L KCl, 0.01 g/L ferrous sulfate heptahydrate, 0.25 g/L yeast extract, and 1000 ml distilled water. Its preparation instructs curators to dissolve everything except yeast extract, adjust to pH 2.0 with H2SO4, autoclave, and add yeast extract from a sterile stock. The same DSMZ sheet separately states that autotrophic growth omits yeast extract, uses 13.90 g/L ferrous sulfate heptahydrate, and adjusts to pH 1.7 before autoclaving.

The generated merged record has the heterotrophic ingredient amounts and pH, omits 1000 ml distilled water, adds H2SO4 as a variable ingredient, has no preparation steps, and lists the autotrophic `autotrophic_growth_on_ferrous_sulfate` source as if it had the same recipe.

## Completeness

The heterotrophic branch has the mineral and yeast-extract amounts, but it lacks water and the late sterile yeast-extract addition. The autotrophic source record is currently represented with the wrong FeSO4 amount, the wrong pH, and an incorrect yeast-extract ingredient before it is merged away.

## Findings

- KOMODO 709.2's autotrophic pH 1.7, yeast-extract omission, and 13.90 g/L ferrous sulfate variant were overwritten by the pH 2.0 heterotrophic DSMZ base recipe.
- The merge folded the autotrophic and heterotrophic recipes together because their normalized parents now have identical signatures.
- The 1000 ml distilled-water row from DSMZ Medium 709 is missing.
- H2SO4 is represented as a variable ingredient even though DSMZ only uses it for pH adjustment.
- The generated record omits the autoclaving and post-autoclave sterile yeast-extract addition.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/autotrophic_growth_on_ferrous_sulfate.yaml` so it omits yeast extract, uses 13.90 g/L ferrous sulfate heptahydrate, and records pH 1.7.
- Keep the heterotrophic KOMODO 709.1 recipe separate from the autotrophic KOMODO 709.2 recipe during merge.
- Restore the distilled-water row and represent H2SO4 as pH-adjustment reagent text or a preparation-scoped reagent.
- Add preparation steps for dissolving the base, pH adjustment, autoclaving, and sterile yeast-extract addition.

## Follow-up Checks

- Re-run merge generation and verify only KOMODO 709 and KOMODO 709.1 collapse into this heterotrophic record.
- Confirm KOMODO 709.2 regenerates as a distinct pH 1.7 ferrous-sulfate record with no yeast extract.

## Additional Notes

None.

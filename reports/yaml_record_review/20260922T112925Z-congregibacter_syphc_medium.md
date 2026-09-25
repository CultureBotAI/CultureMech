# YAML Record Review: CONGREGIBACTER (SYPHC) MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/congregibacter_syphc_medium.yaml`
- Started UTC: 2026-09-22T11:27:00Z
- Finished UTC: 2026-09-22T11:29:25Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:000551`
- Normalized source: `data/normalized_yaml/bacterial/congregibacter_syphc_medium.yaml`
- Source identity: DSMZ Medium 1115, `CONGREGIBACTER (SYPHC) MEDIUM`
- Current generated merge: one source recipe, `congregibacter_syphc_medium`

## Validation

- Open schema validation: pass.
- Strict validation: pass.
- Reference validation: pass with 0 checks.
- Term validation: pass.
- Embedded `curation_history`: not checked by the standalone history validator.

## Identity and Grounding

- DSMZ Medium 1115 is a final marine broth with 35 g Sea Salt, 0.1 g ammonium chloride, 1 g yeast extract, 1.1 g sodium pyruvate, 2.5 g HEPES, 0.04 g L-histidine, 0.04 g L-cysteine HCl hydrate, 0.05 g KH2PO4, 1 ml Wolfe's mineral elixir, 0.5 ml Seven vitamins solution, and 1000 ml distilled water.
- Wolfe's mineral elixir and Seven vitamins solution are stock solutions printed below the final recipe.
- The generated record omits both stock-solution ingredients and flattens their stock-strength constituents into the final medium.
- A gitignore-independent search found a KOMODO Medium 1115 / DSMZ 1115 copy under `sypg_medium__0c1821a0.yaml`; this direct DSMZ output does not merge that related source.

## Evidence

- DSMZ source checked: `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1115.pdf`.
- Local normalized owner checked: `data/normalized_yaml/bacterial/congregibacter_syphc_medium.yaml`.
- Local KOMODO 1115 owner checked: `data/normalized_yaml/bacterial/sypg_medium.yaml`.

## Completeness

- The bacterial category, liquid state, 7.3-7.5 final pH range, and main bulk ingredients are appropriate.
- Final-medium ingredients are normalized to per-liter values from DSMZ's 1001 ml final volume.
- Stock-solution nesting is incomplete: the generated record has no `solutions`, while the normalized owner moved only 8 of the 21 stock constituents out of final-medium `ingredients`.

## Findings

1. All 14 Wolfe's mineral elixir constituents are generated as final-medium grams per liter even though DSMZ adds the stock at 1 ml/l. Those trace components are therefore roughly 1000x too concentrated.
2. All 7 Seven vitamins solution constituents are generated as final-medium grams per liter even though DSMZ adds that stock at 0.5 ml/l. Those vitamins are therefore roughly 2000x too concentrated.
3. The direct stock ingredients `Wolfe's mineral elixir` and `Seven vitamins solution` are missing from the generated final-medium ingredient list.
4. The normalized `apply_cocktail_nesting.py` repair is only partial for this record; several Wolfe and Seven vitamins stock constituents still remain as final-medium ingredients and need to move under their solutions.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/congregibacter_syphc_medium.yaml`, retain only DSMZ final-medium ingredients in `ingredients`.
2. Move the full Wolfe's mineral elixir and Seven vitamins solution stock compositions under `solutions`.
3. Add Wolfe's mineral elixir at `1 ML_PER_L` and Seven vitamins solution at `0.5 ML_PER_L` to the final recipe.
4. Reassess the KOMODO Medium 1115 / `sypg_medium` relationship after the complete nesting repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after repairing and regenerating this record.
- Confirm no Wolfe's mineral elixir or Seven vitamins stock-only constituents remain as final-medium ingredients.
- Confirm the regenerated record still preserves DSMZ 1115's final pH range and microaerophilic-growth note.

## Additional Notes

- No LinkML structural defect was found.
- The current generated record predates the August 2026 cocktail-nesting repair, and the normalized owner still needs a complete stock-solution pass.

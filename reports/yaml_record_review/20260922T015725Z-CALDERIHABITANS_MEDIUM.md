# YAML Record Review: calderihabitans_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDERIHABITANS_MEDIUM.yaml
- Started UTC: 2026-09-22T01:56:02Z
- Finished UTC: 2026-09-22T01:57:25Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:000978`, `calderihabitans_medium`, `CALDERIHABITANS MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `calderihabitans_medium` on fingerprint `8d5a0a0d310f592ba7f7224fa8364b532429187c9a9e20c74cf3c368b42b8def`.
- Authoritative owner: `data/normalized_yaml/bacterial/calderihabitans_medium.yaml`.
- Claimed source identity: DSMZ / MediaDive Medium `1508`, `CALDERIHABITANS MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium `1508` is `CALDERIHABITANS MEDIUM`; the live DSMZ PDF agrees with the record's pH range 7.3 to 7.5 and its preparation text.
- K2HPO4, NH4Cl, sodium nitrate, ferric citrate monohydrate, sodium carbonate, sodium pyruvate, sodium thiosulfate pentahydrate, sodium sulfide nonahydrate, disodium EDTA, iron(II) sulfate heptahydrate, zinc sulfate heptahydrate, manganese(II) chloride tetrahydrate, boric acid, cobalt chloride hexahydrate, copper(II) chloride dihydrate, sodium molybdate dihydrate, biotin, folic acid, pyridoxine hydrochloride, thiamine hydrochloride, riboflavin, nicotinic acid, vitamin B12, 4-aminobenzoic acid, and lipoic acid are grounded to source-compatible identities.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- `NaNO3` has a correct primary ChEBI grounding but still carries a legacy `mediaingredientmech_term` identifier instead of a `mediaingredientmech_chebi_term` link.
- Sea Salt and yeast extract are intentionally ungrounded.

## Evidence

- DSMZ Medium 1508 lists final pH 7.3 to 7.5, final volume 1002 ml, Sea Salt 21.00 g, K2HPO4 0.10 g, NH4Cl 0.10 g, NaNO3 0.05 g, yeast extract 0.05 g, ferric citrate monohydrate 0.01 g, Trace element solution SL-4 1.00 ml, 0.50 ml of 0.1% sodium resazurin, Na2CO3 1.50 g, Na-pyruvate 1.00 g, `Na2S2O3 x 5 H2O` 1.00 g, Wolin's vitamin solution (10x) 1.00 ml, `Na2S x 9 H2O` 0.25 g, and distilled water 1000.00 ml.
- DSMZ lists Trace element solution SL-4 and Wolin's vitamin solution (10x) as separate 1 L stock formulations, not direct final-medium ingredient rows.
- DSMZ instructs curators to leave carbonate, pyruvate, thiosulfate, vitamins, and sulfide out of the autoclaved base; sparge the base medium with 80% N2 / 20% CO2 for 30 to 45 min; add pyruvate, thiosulfate, vitamins, and sulfide from sterile anoxic stocks prepared under 100% N2; add carbonate from a sterile anoxic stock prepared under 80% N2 / 20% CO2; filter-sterilize pyruvate, thiosulfate, and vitamin stocks; and adjust the completed medium to pH 7.3 to 7.5 if necessary.

## Completeness

- The pH range and preparation prose are present.
- The 1 L distilled water row is absent.
- The 1 ml/L Trace element solution SL-4 and 1 ml/L Wolin's vitamin solution additions are absent as solution additions.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: Trace element solution SL-4 is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 1 ml of SL-4 per final liter.
- Major: Wolin's vitamin solution (10x) is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 1 ml of this stock per final liter.
- Major: the generated record omits the 1000 ml distilled-water row from the final medium.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.
- Minor: `NaNO3` still has a legacy `MediaIngredientMech:000171` link even though the primary `CHEBI:63005` term has already been repaired.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/calderihabitans_medium.yaml`, not the generated merge.
- Model Trace element solution SL-4 and Wolin's vitamin solution (10x) as solution additions at 1 ml/L each, and move the stock-only metals and vitamins into the corresponding stock recipes.
- Add the 1 L distilled water row from DSMZ 1508.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Replace the stale `NaNO3` `mediaingredientmech_term` with the equivalent `mediaingredientmech_chebi_term`.
- Regenerate merged YAML and verify that the generated record preserves the stock additions instead of flattening their recipes.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 1508, with special attention to the two 1 ml/L stock additions, the 1 L water row, the pH 7.3 to 7.5 range, the retained anoxic preparation steps, and the hydrate-specific nickel chloride grounding.

## Additional Notes

- `find . -iname '*calderihabitans*'` included ignored and hidden files and found only the reviewed generated merge plus `data/normalized_yaml/bacterial/calderihabitans_medium.yaml`.
- A gitignore-independent search for `CALDERIHABITANS_MEDIUM`, `Calderihabitans`, `CALDERIHABITANS`, and `calderihabitans` found the active normalized owner, generated merge, registry/catalog rows, the current content review manifest row, archived validation rows, and an obsolete label-plausibility finding for the pre-regrounding `NaNO3` ChEBI assignment.

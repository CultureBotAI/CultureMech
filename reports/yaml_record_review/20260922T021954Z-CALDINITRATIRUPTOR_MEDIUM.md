# YAML Record Review: caldinitratiruptor_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDINITRATIRUPTOR_MEDIUM.yaml
- Started UTC: 2026-09-22T02:18:00Z
- Finished UTC: 2026-09-22T02:19:54Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:004013`, `caldinitratiruptor_medium`, `CALDINITRATIRUPTOR medium`, class `MediaRecipe`.
- Merge lineage: generated two-source merge of `KOMODO_1251_CALDINITRATIRUPTOR_medium` and `caldinitratiruptor_medium` on fingerprint `bf5baf440133a71d71e342f7617daec68dcf3ebed077497f019b9cc6c0175124`.
- Authoritative owners: `data/normalized_yaml/bacterial/KOMODO_1251_CALDINITRATIRUPTOR_medium.yaml` for KOMODO 1251 and `data/normalized_yaml/bacterial/caldinitratiruptor_medium.yaml` for DSMZ / MediaDive Medium 1251.
- Claimed source identity: KOMODO Medium 1251, `CALDINITRATIRUPTOR medium`, merged with DSMZ / MediaDive Medium 1251, `CALDINITRATIRUPTOR MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium 1251 is `CALDINITRATIRUPTOR MEDIUM`; the live DSMZ PDF agrees with the pH 7.0 and with the DSMZ owner's anaerobic preparation text.
- KOMODO Medium 1251 cites DSMZ Medium 1251 and has the same ingredient signature as the active DSMZ owner, so the `SOURCE_DUPLICATE` relationship is source-compatible.
- The direct final-medium salts, nitrate, yeast extract, carbonate, and glucose rows are source-compatible identities.
- Modified Wolin's mineral rows are grounded to source-compatible identities but are modeled at the wrong formulation level.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- `NaNO3` has a correct current primary sodium nitrate term but still carries a legacy `mediaingredientmech_term` field instead of a `mediaingredientmech_chebi_term` field.
- Yeast extract is intentionally ungrounded as an undefined biological mixture.

## Evidence

- DSMZ Medium 1251 lists NH4Cl, KH2PO4, K2HPO4, KCl, NaCl, NaNO3, calcium chloride dihydrate, magnesium chloride hexahydrate, 10 ml Modified Wolin's mineral solution, yeast extract, sodium carbonate, D-glucose, and 1000 ml distilled water in the final medium.
- DSMZ lists Modified Wolin's mineral solution as a separate 1 L stock formulation, not as direct final-medium ingredient rows.
- The active normalized owners have already collapsed the old identical NaCl and CaCl2 duplicate sums to 1.0 g/L NaCl and 0.1 g/L CaCl2, but this generated merge still contains stale 2.0 g/L NaCl and 0.2 g/L CaCl2 values from before the September 2026 duplicate-repair pass.
- DSMZ instructs curators to leave carbonate and glucose out of the autoclaved base, sparge with 80% N2 / 20% CO2, dispense and autoclave under that gas phase, then add glucose from a sterile anoxic 100% N2 stock and carbonate from a sterile anoxic 80% N2 / 20% CO2 stock before setting final pH 7.0.

## Completeness

- The pH value is present.
- The DSMZ owner's preparation steps are absent from the generated merge because the merge chose the KOMODO owner.
- The 1000 ml distilled-water row is absent.
- The 10 ml/L Modified Wolin's mineral solution addition is absent as a solution ingredient.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: the generated merge is stale relative to the active normalized owners and still reports NaCl and `CaCl2 x 2 H2O` as summed duplicate values.
- Major: Modified Wolin's mineral solution is flattened into final-medium ingredient rows at stock strength; DSMZ Medium 1251 calls for 10 ml of this stock per final liter.
- Major: the generated merge chose the KOMODO owner and dropped the DSMZ owner's carbonate/glucose stock-addition and anaerobic autoclaving preparation step.
- Major: the generated record omits the 1000 ml distilled-water row from the final medium.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.
- Minor: `NaNO3` still uses a legacy `mediaingredientmech_term` object despite the CHEBI-keying migration recorded in `curation_history`.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/KOMODO_1251_CALDINITRATIRUPTOR_medium.yaml` and `data/normalized_yaml/bacterial/caldinitratiruptor_medium.yaml`, not the generated merge.
- Model Modified Wolin's mineral solution as a 10 ml/L solution addition and move the mineral-solution-only rows into the corresponding stock recipe.
- Preserve the DSMZ preparation steps in the generated duplicate merge, either by enriching the KOMODO owner or by making the DSMZ owner canonical when it has the same formulation plus richer preparation evidence.
- Add the 1 L distilled water row from DSMZ Medium 1251.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Migrate the `NaNO3` MediaIngredientMech link to the CHEBI-keyed field.
- Regenerate merged YAML and verify that the generated record reflects the repaired 1.0 g/L NaCl and 0.1 g/L CaCl2 values from the normalized owners.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against both normalized owners.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 1251, with special attention to the 10 ml/L Modified Wolin's mineral solution, the 1 L water row, the DSMZ anaerobic preparation steps, the repaired NaCl and CaCl2 rows, and the hydrate-specific nickel chloride grounding.

## Additional Notes

- `find . -iname '*caldinitratiruptor*'` included ignored and hidden files and found the base Caldinitratiruptor DSMZ/KOMODO pair plus the neighboring Caldinitratiruptor microaerophilus TOGO/JCM records.
- A gitignore-independent search for Caldinitratiruptor Medium labels, slugs, and DSMZ / KOMODO 1251 identifiers found the active DSMZ owner, the active KOMODO duplicate owner, the generated merge, registry/catalog rows, current content review manifest rows, label-plausibility rows for the now-repaired NaNO3 primary term, the archived DSMZ/KOMODO source-duplicate review row, and archived DSMZ 1251 validation rows.

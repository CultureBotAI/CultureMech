# YAML Record Review: caldisphaera_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/Caldisphaera_Medium.yaml
- Started UTC: 2026-09-22T02:26:24Z
- Finished UTC: 2026-09-22T02:29:25Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009235`, `caldisphaera_medium`, `Caldisphaera Medium`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `TOGO_M2680_Caldisphaera_Medium` on fingerprint `9379f472248a00a3c7c00f12e12aa5d105288a7842b7be77d13286fde28d19f4`.
- Authoritative owner: `data/normalized_yaml/archaea/TOGO_M2680_Caldisphaera_Medium.yaml`.
- Claimed source identity: TOGO Medium `M2680`, `Caldisphaera Medium`, with original source URL pointing to DSMZ Medium 991.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- TOGO `M2680` is a Caldisphaera record derived from DSMZ Medium 991; the fetched TOGO payload agrees with the DSMZ PDF on the medium name and the completed-medium pH range of 4.0 to 4.5.
- The ammonium sulfate, phosphate, sulfide, ferric chloride hexahydrate, sulfur, citrate, yeast extract, and hydrate-specific calcium chloride final rows are source-compatible identities.
- `MgSO4 x 7 H2O` has been repaired to the source-compatible magnesium sulfate heptahydrate primary term, but its stale `mediaingredientmech_chebi_term` still points to generic magnesium sulfate.
- Allen's trace element solution and Wolin's 10x vitamin solution rows are grounded to source-compatible individual chemicals but are modeled at the wrong formulation level.
- Sulfur powder and yeast extract are intentionally ungrounded as a mineral allotrope mixture and an undefined biological mixture.
- `10 N H2SO4`, `Carbon dioxide gas`, `Hydrogen gas`, `1 N HCl`, and `N2` are modeled as variable-concentration ingredients instead of pH-adjustment or gas-atmosphere preparation details.

## Evidence

- DSMZ Medium 991 lists ammonium sulfate 1.30 g, KH2PO4 0.28 g, magnesium sulfate heptahydrate 0.25 g, calcium chloride dihydrate 0.07 g, ferric chloride hexahydrate 0.02 g, 10 ml Allen's trace element solution, trisodium citrate dihydrate 2.94 g, 0.50 ml 0.1% sodium resazurin, 10 g powdered sulfur, 0.50 g Oxoid yeast extract, 1 ml Wolin's vitamin solution 10x, sodium sulfide nonahydrate 0.50 g, and 1000 ml distilled water in the final medium.
- The TOGO `M2680` payload preserves the DSMZ final masses and pH range but reports the Wolin vitamin addition as 10 ml rather than the DSMZ 1 ml.
- DSMZ defines Allen's trace element solution as a separate 1 L stock with milligram-scale `MnCl2 x 4 H2O`, borax, `ZnSO4 x 7 H2O`, `CuCl2 x 2 H2O`, `Na2MoO4 x 2 H2O`, `VOSO4 x 2 H2O`, and `CoSO4` rows; the generated record imports those stock milligram values as final-medium grams per liter.
- DSMZ defines Wolin's vitamin solution 10x as a separate 1 L stock with milligram-scale vitamins; the generated record imports those stock milligram values as final-medium grams per liter.
- DSMZ instructs curators to adjust the base to pH 3.5 with 10 N H2SO4, sparge with 80% H2 / 20% CO2, dispense into vessels containing sulfur, heat to 90-100 C for 1-2 h on three successive days, add yeast, filter-sterilized vitamins, and sulfide from sterile anoxic stocks under N2, and pressurize the inoculated medium to 1 bar overpressure with sterile 80% H2 / 20% CO2.

## Completeness

- The generated record carries the pH range 4.0 to 4.5 from TOGO / DSMZ.
- The generated merge omits all preparation steps despite rich DSMZ and TOGO instructions for acidification, sparging, sulfur sterilization, anaerobic stock additions, and post-inoculation pressurization.
- The 10 ml/L Allen's trace element solution and 1 ml/L Wolin's vitamin solution 10x additions are absent as solution ingredients.
- The 0.5 ml/L sodium resazurin addition is present only as an empty `Unknown solution` with `G_PER_L` units.
- Empty `target_organisms` and `source_references` are not inherently defects for this TOGO import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: the generated merge is stale relative to the maintained TOGO owner; duplicate cleanup has since changed `Distilled water` from `3000.0` to `1000.0`.
- Major: even the active owner models the source's 1000 ml final water row as `1000.0 G_PER_L`, which overstates water mass by 1000-fold.
- Major: Allen's trace element solution has been flattened into final-medium rows at stock strength, so stock milligram values such as 450 mg/L borax appear as unsupported final grams per liter.
- Major: Wolin's 10x vitamin solution has been flattened into final-medium rows at stock strength, so stock milligram values such as 20 mg/L biotin appear as unsupported final grams per liter.
- Major: TOGO `M2680` misimports the DSMZ 1 ml Wolin vitamin addition as 10 ml, and the migrated CultureMech record turns that source error into flattened vitamin rows.
- Major: the 0.5 ml sodium resazurin addition is migrated into an empty `Unknown solution` with mass-concentration units instead of a volume addition.
- Major: acid, acid-adjustment, and gas-atmosphere details are modeled as variable final ingredients, including `10 N H2SO4`, `1 N HCl`, `Carbon dioxide gas`, `Hydrogen gas`, and `N2`.
- Major: the generated record omits all DSMZ anaerobic and sulfur-handling preparation steps.
- Minor: hydrate-specific `MgSO4 x 7 H2O` and `VOSO4 x 2 H2O` primary terms were repaired, but their legacy MediaIngredientMech enrichments remain stale or absent.

## Recommended Edits

- Curate `data/normalized_yaml/archaea/TOGO_M2680_Caldisphaera_Medium.yaml`, not the generated merge.
- Preserve the final 1000 ml distilled-water row as final solvent, not `1000.0 G_PER_L`, and keep final water distinct from any stock water rows.
- Replace the flattened trace-element rows with a 10 ml/L Allen's trace element solution addition and preserve the Allen stock formula as a subrecipe.
- Replace the flattened vitamin rows with a 1 ml/L Wolin's vitamin solution 10x addition derived from DSMZ Medium 991 rather than the 10 ml value in the TOGO payload.
- Represent the 0.5 ml sodium resazurin solution as a volume addition with a composition or source-preserving label, not as an empty `Unknown solution`.
- Move 10 N H2SO4, 1 N HCl, H2, CO2, and N2 into pH-adjustment, trace-stock, sparging, pressurization, and anaerobic-transfer preparation steps as appropriate.
- Add the DSMZ preparation instructions for acidification, 80% H2 / 20% CO2 sparging, sulfur handling, repeated heating, sterile anoxic stock additions, and post-inoculation pressurization.
- Re-run term enrichment so repaired hydrate-specific primary terms and MediaIngredientMech grounding fields agree.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 991 and the TOGO `M2680` payload, with special attention to 1000 ml final water, 10 ml/L Allen's trace element solution, 1 ml/L Wolin's vitamin solution 10x, 0.5 ml/L sodium resazurin, pH 4.0 to 4.5, and absence of stock-water, stock-salt, acid, or gas-atmosphere rows from final `ingredients`.

## Additional Notes

- `find . -iname '*caldisphaera*'` included ignored and hidden files and found only the reviewed generated merge plus the active TOGO, active DSMZ, and active KOMODO normalized owners.
- A gitignore-independent search for `TOGO:M2680`, `TOGO_M2680_Caldisphaera`, DSMZ / MediaDive Medium 991 identifiers, `KOMODO_991_CALDISPHAERA`, and `CALDISPHAERA MEDIUM` found the active TOGO, direct DSMZ, and KOMODO owners, the generated TOGO merge, two generated DSMZ / KOMODO 991 peer records under `CALDIVIRGA_MEDIUM` labels, registry/catalog/index rows, validation archive rows, and an archived variant proposal that the KOMODO 991 owner may duplicate KOMODO 883.

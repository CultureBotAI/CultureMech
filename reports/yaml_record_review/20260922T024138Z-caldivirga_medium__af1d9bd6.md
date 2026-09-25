# YAML Record Review: caldivirga_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/caldivirga_medium__af1d9bd6.yaml
- Started UTC: 2026-09-22T02:40:11Z
- Finished UTC: 2026-09-22T02:41:38Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002043`, `caldivirga_medium`, `CALDIVIRGA MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated two-source merge of `caldisphaera_medium` and `caldivirga_medium` on fingerprint `af1d9bd6f229050a09f45a184f68c51aee146e47c662e22bf2635b54ab468c5a`.
- Authoritative owners: `data/normalized_yaml/archaea/caldivirga_medium.yaml` for DSMZ / MediaDive Medium 883 and `data/normalized_yaml/archaea/caldisphaera_medium.yaml` for DSMZ / MediaDive Medium 991.
- Claimed source identity: DSMZ / MediaDive Medium 883, `CALDIVIRGA MEDIUM`, merged with DSMZ / MediaDive Medium 991, `CALDISPHAERA MEDIUM`, as a source duplicate.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium 883 is `CALDIVIRGA MEDIUM`; the live DSMZ 883 PDF agrees with the record's pH 4.0 and with the retained anoxic preparation text.
- The merged-in DSMZ 991 owner is `CALDISPHAERA MEDIUM`; it has pH 4.0 to 4.5 and different acidification, sparging, and sterilization instructions from DSMZ 883.
- DSMZ 883 and DSMZ 991 share the same final and stock formula signatures after normalization, but the source medium numbers, pH values, and preparation protocols differ; they should not be collapsed as a source duplicate without preserving those differences as distinct variants or records.
- The direct final-medium ammonium, phosphate, magnesium, calcium, ferric chloride, citrate, sulfur, yeast, sulfide, and resazurin identities are source-compatible but are slightly underconcentrated.
- Allen's trace element solution and Wolin's vitamin solution rows are grounded to source-compatible individual chemicals but are modeled at the wrong formulation level.
- Yeast extract is intentionally ungrounded as an undefined biological mixture.

## Evidence

- DSMZ Medium 883 lists 2.94 g trisodium citrate dihydrate, 1.30 g ammonium sulfate, 0.28 g KH2PO4, 0.25 g magnesium sulfate heptahydrate, 0.07 g calcium chloride dihydrate, 0.02 g ferric chloride hexahydrate, 10 ml Allen's trace element solution, 0.50 ml 0.1% sodium resazurin, 10 g powdered sulfur, 0.50 g Oxoid yeast extract, 1 ml Wolin's vitamin solution 10x, 0.50 g sodium sulfide nonahydrate, and 1000 ml distilled water in the final medium.
- Both maintained DSMZ owners carry the final-medium mass rows at approximately `source_value / 1.011`; for example, 2.94 g trisodium citrate appears as 2.90801 g/L, 1.30 g ammonium sulfate appears as 1.28586 g/L, and 10 g sulfur appears as 9.8912 g/L.
- The 1.011 divisor matches the 10 ml Allen trace and 1 ml Wolin vitamin additions, so final-medium masses appear to have been renormalized after treating those milliliters as final-volume expansion.
- DSMZ defines Allen's trace element solution and Wolin's vitamin solution 10x as separate 1 L stock formulations, not direct final-medium ingredient rows.
- DSMZ 883 instructs curators to adjust the basal medium to pH 3.5 with 4 N H2SO4, sparge with 100% N2, autoclave sulfur-containing vessels at 105 C for 20 min, and pressurize inoculated vessels with 80% H2 / 20% CO2; DSMZ 991 instead calls for 10 N H2SO4, 80% H2 / 20% CO2 sparging, and repeated 90-100 C heat treatments.

## Completeness

- The pH 4.0 from DSMZ 883 is present.
- The pH 4.0 to 4.5 from DSMZ 991 is absent after the source-duplicate merge.
- The DSMZ 883 preparation steps are present, but the DSMZ 991 preparation steps are absent after the source-duplicate merge.
- The 1000 ml distilled-water row is absent.
- The 10 ml/L Allen's trace element solution and 1 ml/L Wolin's vitamin solution 10x additions are absent as solution ingredients.
- Empty `target_organisms` and `source_references` are not inherently defects for these DSMZ imports; the DSMZ PDFs support the formulations but do not make a strain-specific growth claim.

## Findings

- Major: two different DSMZ source media, Medium 883 and Medium 991, are merged as a source duplicate solely because flattened stock rows produced the same ingredient signature.
- Major: final-medium mass rows are lower than the inspected DSMZ formulas by a constant 1000/1011 factor, apparently from renormalizing around 11 ml of stock additions.
- Major: Allen's trace element solution is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 10 ml of this stock per final liter.
- Major: Wolin's vitamin solution 10x is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 1 ml of this stock per final liter.
- Major: the generated record omits the 1000 ml distilled-water row from the final medium.
- Major: the generated record omits the explicit 10 ml Allen and 1 ml Wolin stock additions.
- Major: the generated merge kept DSMZ 883's pH 4.0 and preparation steps and dropped DSMZ 991's pH 4.0 to 4.5 and Caldisphaera-specific preparation steps.
- Minor: generated `variant_children` still point at `data/normalized_yaml/bacterial/caldisphaera_medium.yaml`; `find` included ignored files and found no such bacterial path, only the active `data/normalized_yaml/archaea/caldisphaera_medium.yaml`.

## Recommended Edits

- Curate `data/normalized_yaml/archaea/caldivirga_medium.yaml` and `data/normalized_yaml/archaea/caldisphaera_medium.yaml`, not the generated merge.
- Restore exact DSMZ final-medium concentrations before the 1000/1011 renormalization.
- Add the 1 L distilled-water row from DSMZ.
- Model Allen's trace element solution and Wolin's vitamin solution 10x as 10 ml/L and 1 ml/L stock additions, and move their internal ingredients into the corresponding stock recipes.
- Do not let identical flattened stock signatures collapse DSMZ 883 and DSMZ 991 into a lossy source duplicate; either preserve them as distinct media or as variants that retain pH and preparation differences.
- Preserve DSMZ 883 and DSMZ 991 preparation steps in any regenerated merge or variant relationship.
- Refresh variant child/parent paths so they point at the active `data/normalized_yaml/archaea/*.yaml` owner paths.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against both normalized owners.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare regenerated direct DSMZ records against DSMZ Medium 883 and DSMZ Medium 991, with special attention to pH, acid strength, gas atmosphere, sulfur sterilization, 10 ml/L Allen's trace element solution, 1 ml/L Wolin's vitamin solution, 1000 ml water, and absence of stock rows from final `ingredients`.
- Re-run a gitignore-independent search for stale `data/normalized_yaml/bacterial/caldisphaera_medium.yaml` and `data/normalized_yaml/bacterial/caldivirga_medium.yaml` paths after regeneration.

## Additional Notes

- `find . -iname '*caldivirga*'` included ignored and hidden files and found three generated Caldivirga records plus the active KOMODO 883, TOGO `M2386`, and direct DSMZ 883 normalized owners.
- A gitignore-independent structured-data search for Caldivirga labels, KOMODO 883, KOMODO 991, TOGO `M2386`, and DSMZ / MediaDive 883 identifiers found the Caldivirga owners, the KOMODO 991 Caldisphaera owner, direct DSMZ 991 Caldisphaera rows, registry/catalog rows, current content review manifest rows, concentration-plausibility rows for vitamin-scale rows, and variant-link proposals that had already flagged KOMODO 883 and KOMODO 991 as a low-confidence possible source duplicate.

# YAML Record Review: caldicellulosiruptor_medium_with_2_5_nacl

- Repository: CultureMech
- Record: data/merge_yaml/merged/caldicellulosiruptor_medium_with_2_5_nacl.yaml
- Started UTC: 2026-09-22T02:04:38Z
- Finished UTC: 2026-09-22T02:05:49Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:010422`, `caldicellulosiruptor_medium_with_2_5_nacl`, `Caldicellulosiruptor Medium With 2.5% NaCl`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `TOGO_M994_Caldicellulosiruptor_Medium_With_2.5_NaCl` on fingerprint `18cd27846f9267249dd5b9b7a2f6ba4d57876d7481947e78eea766798b1b9927`.
- Authoritative owner: `data/normalized_yaml/bacterial/TOGO_M994_Caldicellulosiruptor_Medium_With_2.5_NaCl.yaml`.
- Claimed source identity: TOGO Medium `M994`, `Caldicellulosiruptor Medium With 2.5% NaCl`, derived from JCM `JCM_M947`.
- Related unmerged duplicate: `data/normalized_yaml/bacterial/caldicellulosiruptor_medium_with_2_5_nacl.yaml` claims MediaDive / JCM Medium `J947`, `CALDICELLULOSIRUPTOR MEDIUM WITH 2.5% NaCl`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- TOGO `M994` is the Caldicellulosiruptor Medium With 2.5% NaCl recipe imported from JCM M947.
- NaCl, KH2PO4, NH4Cl, K2HPO4, magnesium chloride hexahydrate, ferric chloride hexahydrate, cellobiose, glucose, and L-cysteine hydrochloride hydrate are grounded to source-compatible identities.
- Distilled water and `Trace element solution SL--10 (see Medium [M433])` are present but mis-modeled by amount or unit.
- Yeast extract and Trypticase peptone are intentionally ungrounded as undefined biological mixtures.
- The `N2` source gas is modeled as a variable-concentration final ingredient instead of as an anoxic gas-atmosphere preparation condition.

## Evidence

- The TOGO API payload lists 1 L distilled water, 1 g yeast extract, 25 g NaCl, 0.75 g KH2PO4, 0.9 g NH4Cl, 1.5 g K2HPO4, 0.5 mg resazurin, 0.4 g `MgCl2.6H2O`, 2.5 mg `FeCl3.6H2O`, 1 g cellobiose, 1 g glucose, 2 g Trypticase peptone, 0.75 g `L-Cysteine.HCl.H2O`, 1 ml Trace element solution SL-10 from Medium M433, and N2 in the main solution.
- TOGO preserves two preparation comments: adjust pH to 7.5, and prepare the medium anaerobically under 100% N2 with filter-sterilized cellobiose added after autoclaving from an anoxic N2 stock.
- The live JCM `GRMD=947` page returned `Nothing found`, so the original JCM page could not be independently checked.

## Completeness

- The pH 7.5 is absent.
- The TOGO preparation comments are absent from `preparation_steps`.
- The 1 ml Trace element solution SL-10 addition is present only as an empty `Unknown solution` stub with `G_PER_L` units instead of a volume unit and a link to the M433 composition.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the TOGO payload supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: 1 L distilled water was imported as 1 g/L water, so the record is short by three orders of magnitude.
- Major: 0.5 mg resazurin was imported as 0.5 g/L and 2.5 mg `FeCl3.6H2O` was imported as 2.5 g/L.
- Major: the 1 ml Trace element solution SL-10 addition was migrated into an empty `Unknown solution` record with a `G_PER_L` concentration.
- Major: the generated record omits the pH 7.5 and all anaerobic preparation instructions from TOGO.
- Minor: the 100% N2 atmosphere is present as a variable final ingredient instead of a preparation condition.
- Minor: TOGO M994 and MediaDive / JCM J947 are duplicate source records but currently generate two separate `caldicellulosiruptor_medium_with_2_5_nacl` pages with complementary defects.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/TOGO_M994_Caldicellulosiruptor_Medium_With_2.5_NaCl.yaml`, not the generated merge.
- Convert 1 L distilled water to 1000 ml or 1000 g/L rather than 1 g/L.
- Convert 0.5 mg resazurin and 2.5 mg ferric chloride hexahydrate to 0.0005 g/L and 0.0025 g/L.
- Model `Trace element solution SL--10 (see Medium [M433])` as a 1 ml/L solution reference and resolve the M433 stock composition instead of keeping an empty `Unknown solution`.
- Add pH 7.5 and the two TOGO preparation comments as structured preparation steps.
- Reconcile this TOGO record with `data/normalized_yaml/bacterial/caldicellulosiruptor_medium_with_2_5_nacl.yaml` as a JCM source duplicate after both records agree on water, resazurin, ferric chloride, SL-10, pH, and anoxic preparation.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against TOGO M994, with special attention to 1 L water, the two milligram-scale additions, the 1 ml M433 SL-10 addition, pH 7.5, the 100% N2 preparation condition, and the cellobiose-after-autoclaving instruction.

## Additional Notes

- `find . -iname '*caldicellulosiruptor*2*5*nacl*'` included ignored and hidden files and found both generated duplicate records plus their active TOGO and MediaDive / JCM normalized owners.
- A gitignore-independent search for `TOGO:M994`, `M994`, `Caldicellulosiruptor Medium With 2.5% NaCl`, and `caldicellulosiruptor_medium_with_2_5_nacl` found the active TOGO owner, the active MediaDive / JCM owner, both generated merges, registry/catalog rows, current content review manifest rows, archived validation rows, and unrelated NBRC/JCM M994 text in other records.

# YAML Record Review: caldicellulosiruptor_medium_for_dsm_10319

- Repository: CultureMech
- Record: data/merge_yaml/merged/caldicellulosiruptor_medium_for_dsm_10319.yaml
- Started UTC: 2026-09-22T02:01:26Z
- Finished UTC: 2026-09-22T02:04:04Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009111`, `caldicellulosiruptor_medium_for_dsm_10319`, `Caldicellulosiruptor Medium (For DSM 10319)`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `caldicellulosiruptor_medium_for_dsm_10319` on fingerprint `8c95e8f97e6be203eb1316cf1bc33a03a062da680c0ba10c776b38ac223e2d37`.
- Authoritative owner: `data/normalized_yaml/bacterial/caldicellulosiruptor_medium_for_dsm_10319.yaml`.
- Claimed source identity: TOGO Medium `M2542`, `Caldicellulosiruptor Medium (For DSM 10319)`, with original source URL pointing to DSMZ Medium 640.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation completed with 11 errors across `target_organisms[*].evidence[0].snippet` and `variants[*].evidence[0].snippet`.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- TOGO `M2542` is the DSMZ Medium 640 DSM 10319 substitution that replaces cellobiose with 5.00 g/L D-glucose.
- NaCl, KH2PO4, NH4Cl, K2HPO4, D-glucose, magnesium chloride hexahydrate, L-cysteine hydrochloride hydrate, sodium molybdate dihydrate, boric acid, manganese(II) chloride tetrahydrate, cobalt chloride hexahydrate, copper(II) chloride dihydrate, zinc chloride, and iron dichloride tetrahydrate are grounded to source-compatible identities.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- Trypticase peptone and yeast extract are intentionally ungrounded as undefined biological mixtures.
- The `N2` source gas is modeled as a variable-concentration final ingredient instead of as an anoxic gas-atmosphere preparation condition.

## Evidence

- The TOGO API payload lists 0.5 ml Na-resazurin solution, 1000 ml distilled water, 0.9 g NaCl, 0.75 g KH2PO4, 0.9 g NH4Cl, 1.5 g K2HPO4, 5 g D-glucose, 0.4 g `MgCl2 x 6 H2O`, 2.5 ml `FeCl3 x 6H2O` solution, 2 g Trypticase peptone, 0.75 g `L-Cysteine-HCl x H2O`, 1 g yeast extract, 1 ml Trace element solution SL-10, and 100% N2 in the final-medium paragraph.
- The TOGO API payload lists Trace element solution SL-10 as a separate subcomponent with 990 ml distilled water, 10 ml 25% HCl, 1.5 g `FeCl2 x 4 H2O`, and milligram-scale ZnCl2, `MnCl2 x 4 H2O`, H3BO3, `CoCl2 x 6 H2O`, `CuCl2 x 2 H2O`, `NiCl2 x 6 H2O`, and `Na2MoO4 x 2 H2O` rows.
- TOGO preserves the DSMZ instructions to keep cysteine and cellobiose out of the initial base, sparge with 100% N2 for 30 to 45 min, add cysteine before pH adjustment, autoclave under the same gas, add the carbohydrate after autoclaving from a filter-sterilized anoxic stock, and prepare SL-10 by dissolving FeCl2 in HCl before adding the other salts.

## Completeness

- The pH 7.2 is present in the fetched TOGO metadata but is absent from the generated record.
- The TOGO preparation comments are absent from `preparation_steps`.
- The 0.5 ml resazurin, 2.5 ml ferric chloride, and 1 ml SL-10 solution additions are present only as empty `solutions` stubs named `Unknown solution`, with `G_PER_L` units instead of volume units.
- The enriched target organisms and variants are about two modified DSMZ 640 media from Blumer-Schuette 2010 and Shang 2013, not the exact TOGO M2542 medium for DSM 10319.

## Findings

- Major: SL-10 stock water was merged with final water into one 1990 g/L final `Distilled water` row.
- Major: every milligram-scale SL-10 component was imported as grams per liter; for example 36 mg `Na2MoO4 x 2 H2O` became 36 g/L and 190 mg `CoCl2 x 6 H2O` became 190 g/L.
- Major: the SL-10 HCl and trace metals were flattened into the final medium even though TOGO models SL-10 as a 1 ml/L subcomponent.
- Major: three solution additions were migrated into empty `Unknown solution` records with mass-concentration units where TOGO supplies 0.5 ml, 2.5 ml, and 1 ml additions.
- Major: the generated record omits the pH 7.2 and all anoxic preparation steps from TOGO / DSMZ.
- Major: the nine `target_organisms` and two `variants` carry reference snippets that fail exact reference validation and describe other modified DSMZ 640 formulations instead of TOGO M2542.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caldicellulosiruptor_medium_for_dsm_10319.yaml`, not the generated merge.
- Keep the final 1000 ml distilled-water row separate from the 990 ml SL-10 stock water row.
- Replace the flattened SL-10 rows with a 1 ml/L `Trace element solution SL-10` addition and preserve the SL-10 subrecipe with milligram units.
- Represent Na-resazurin solution and the acidified `FeCl3 x 6H2O` solution as volume additions with compositions or source-preserving labels, not empty `Unknown solution` records with `G_PER_L` units.
- Add pH 7.2 and preparation steps from the TOGO / DSMZ comments.
- Move the Blumer-Schuette 2010 and Shang 2013 organism/variant evidence to records that model those exact modified DSMZ 640 formulations, and keep this record focused on the DSM 10319 D-glucose substitution.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against TOGO M2542 and DSMZ Medium 640, with special attention to the 5 g/L D-glucose substitution, retained pH 7.2, the 0.5 ml resazurin addition, 2.5 ml ferric chloride stock addition, 1 ml SL-10 addition, and absence of stock-water or stock-metal rows from final `ingredients`.
- Re-run reference validation after moving or replacing the two paper-backed enrichment blocks; the expected result is zero exact-snippet errors.

## Additional Notes

- `find . -iname '*caldicellulosiruptor*10319*'` included ignored and hidden files and found only the reviewed generated merge plus `data/normalized_yaml/bacterial/caldicellulosiruptor_medium_for_dsm_10319.yaml`.
- A gitignore-independent search for `caldicellulosiruptor_medium_for_dsm_10319`, `TOGO:M2542`, `M2542`, `Caldicellulosiruptor Medium (For DSM 10319)`, and `DSM 10319` found the active normalized owner, generated merge, registry/catalog rows, current content review rows for this TOGO record and the KOMODO DSM 10319 variant, and archived validation rows.

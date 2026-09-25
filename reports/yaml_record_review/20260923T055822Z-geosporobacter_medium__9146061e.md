# YAML Record Review: geosporobacter_medium__9146061e

- Repository: CultureMech
- Record: data/merge_yaml/merged/geosporobacter_medium__9146061e.yaml
- Started UTC: 2026-09-23T05:54:53Z
- Finished UTC: 2026-09-23T05:58:22Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:002244` is the direct MediaDive/JCM import for JCM 1064, `GEOSPOROBACTER MEDIUM`.

The generated row derives from `data/normalized_yaml/bacterial/geosporobacter_medium.yaml`; future formula fixes belong in that maintained normalized input or in the MediaDive import path that produced it. An ignored-file-inclusive exact source-ID search also found the equivalent Togo import in `data/normalized_yaml/bacterial/TOGO_M1133_Geosporobacter_Medium.yaml` and `data/merge_yaml/merged/GEOSPOROBACTER_MEDIUM.yaml`.

## Validation

`linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/geosporobacter_medium__9146061e.yaml` passed.

`scripts/validate_strict.py data/merge_yaml/merged/geosporobacter_medium__9146061e.yaml --workers 1 --quiet` passed with 0 error rows.

`linkml-reference-validator validate data data/merge_yaml/merged/geosporobacter_medium__9146061e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` passed with 0 checks.

`linkml-term-validator validate-data data/merge_yaml/merged/geosporobacter_medium__9146061e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` passed.

Embedded `curation_history` entries were not checked: the repository's `validate-history` recipe targets standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `mediadive.medium:J1064` identity and JCM source URL match the live JCM 1064 `GEOSPOROBACTER MEDIUM` page and the MediaDive REST payload for `J1064`.

The record is split from the equivalent Togo import for the same JCM source. The normalized Togo row carries `TOGO:M1133` with `original_media_id: JCM_M1064` and the same JCM 1064 source URL, but it remains a separate generated record because the two importers represented the stock additions differently.

Most grounded salts agree with the source formula. `NiCl2 x 6 H2O` is grounded to `CHEBI:34887`, `nickel dichloride`, which does not preserve the source's hexahydrate form.

## Evidence

The live JCM 1064 source lists a main formula with KCl 0.5 g, KH2PO4 0.2 g, NaCl 1.0 g, NH4Cl 0.05 g, CaCl2 x 2H2O 0.1 g, MgCl2 x 6H2O 0.4 g, yeast extract 1.0 g, glucose 0.36 g, Trace vitamins from JCM 197 at 1.0 ml, Trace element solution from JCM 231 at 1.0 ml, NaHCO3 0.84 g, Na2S x 9H2O 0.5 g, resazurin 1.0 mg, and distilled water 1.0 L.

MediaDive preserves that hierarchy as `Main sol. J1064` plus two referenced solutions: `Trace vitamins` and `Trace element solution`, each added to the main medium at 1 ml.

JCM 197 confirms that `Trace vitamins` is a 1 L stock with milligram quantities of biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid.

JCM 231 confirms that `Trace element solution` is a stock whose internal salts are made up to 1000 ml, starting with Na2-EDTA in 500 ml of distilled water. It includes stock-strength NaCl and CaCl2 x 2H2O rows, but those are not additional 1 g/L and 0.13 g/L final-medium rows.

The generated record preserves the anaerobic autoclaving, filtration, stock-addition, and pH adjustment instructions from JCM 1064 as free text.

## Completeness

The main distilled-water row from JCM 1064 is absent.

The 1 ml `Trace vitamins` and 1 ml `Trace element solution` additions are absent as solution references. Their stock internals were flattened into final-medium ingredients at stock strength.

The final `ph_value` is `7.8`; JCM states a preparation range of pH 7.5 to 8.0, and the exact midpoint is not the same source claim.

Empty growth-evidence, variant, discussion, and publication slots are acceptable for this imported source recipe.

## Findings

- Major: The 1 ml `Trace vitamins` addition from JCM 197 was flattened into ten direct ingredient rows at 1 L stock strength. The normalized owner is `data/normalized_yaml/bacterial/geosporobacter_medium.yaml`.
- Major: The 1 ml `Trace element solution` addition from JCM 231 was flattened into thirteen direct ingredient rows at stock strength. The generated record therefore asserts final 6.2 g/L MgSO4 x 7H2O, 0.55 g/L MnSO4 x n H2O, 0.17 g/L CoCl2 x 6H2O, and other trace-salt values that are about 1000-fold higher than the 1 ml stock addition supports.
- Major: Duplicate cleanup summed stock-internal NaCl and CaCl2 x 2H2O into the basal salts, yielding final `NaCl` 1.998004 g/L and `CaCl2 x 2 H2O` 0.22980040000000002 g/L instead of keeping the trace-stock rows scoped to the 1 ml `Trace element solution`.
- Major: The direct MediaDive/JCM record remains split from the equivalent Togo `JCM_M1064` import in `data/normalized_yaml/bacterial/TOGO_M1133_Geosporobacter_Medium.yaml`.
- Minor: `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride.
- Minor: The scalar `ph_value` stores an exact 7.8 even though JCM only says to adjust pH to the 7.5 to 8.0 range.

## Recommended Edits

- Preserve `Trace vitamins` and `Trace element solution` in `data/normalized_yaml/bacterial/geosporobacter_medium.yaml` as 1 ml stock additions to JCM 1064 instead of direct final-medium ingredients.
- Keep the JCM 197 and JCM 231 stock recipes as separate subrecipes, or compute pre-diluted final values from a documented 1 ml addition and keep the stock boundary visible.
- Remove the duplicate-merge sums that add stock-strength NaCl and CaCl2 x 2H2O to the basal final-medium rows.
- Preserve the JCM 1064 1 L distilled-water row as formulation context.
- Align the MediaDive J1064 and Togo M1133 normalized inputs so the regenerated merge either combines them or records an explicit equivalence instead of publishing two same-source Geosporobacter records.
- Replace the `NiCl2 x 6 H2O` grounding with a hydrate-specific term if one is available; otherwise leave the exact source string unresolved instead of using the anhydrous salt.
- Replace the exact `ph_value: 7.8` with a range-capable representation when supported, or keep the pH range only in preparation text.

## Follow-up Checks

- Regenerate the merge and confirm this record no longer has direct `Biotin`, `Folic acid`, `Na2-EDTA`, `MgSO4 x 7 H2O`, or trace-metal rows at stock strength.
- Confirm the regenerated final medium has only basal NaCl and CaCl2 x 2H2O final rows plus a scoped 1 ml `Trace element solution` addition.
- Re-run LinkML, strict, reference, and term validation on the regenerated generated YAML.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:J1064` and `TOGO:M1133` to confirm the same JCM source is no longer published as two unrelated generated records.

## Additional Notes

The source-ID search used `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`, so ignored generated records and indexes were included.

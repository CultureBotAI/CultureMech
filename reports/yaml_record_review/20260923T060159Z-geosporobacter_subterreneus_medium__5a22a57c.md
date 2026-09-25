# YAML Record Review: geosporobacter_subterreneus_medium__5a22a57c

- Repository: CultureMech
- Record: data/merge_yaml/merged/geosporobacter_subterreneus_medium__5a22a57c.yaml
- Started UTC: 2026-09-23T05:59:58Z
- Finished UTC: 2026-09-23T06:01:59Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:002895` is the direct MediaDive/JCM import for JCM 548, `GEOSPOROBACTER SUBTERRENEUS MEDIUM`.

The generated row derives from `data/normalized_yaml/bacterial/geosporobacter_subterreneus_medium.yaml`; future formula fixes belong in that normalized input or in the importer that flattened MediaDive J548. An ignored-file-inclusive exact search for the JCM 548 URL, `mediadive.medium:J548`, and `JCM_M548` also found `data/normalized_yaml/bacterial/TOGO_M550_Geosporobacter_Subterreneus_Medium.yaml` and `data/merge_yaml/merged/GEOSPOROBACTER_SUBTERRENEUS_MEDIUM.yaml` as an equivalent Togo branch.

## Validation

`linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/geosporobacter_subterreneus_medium__5a22a57c.yaml` passed.

`scripts/validate_strict.py data/merge_yaml/merged/geosporobacter_subterreneus_medium__5a22a57c.yaml --workers 1 --quiet` passed with 0 error rows.

`linkml-reference-validator validate data data/merge_yaml/merged/geosporobacter_subterreneus_medium__5a22a57c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` passed with 0 checks.

`linkml-term-validator validate-data data/merge_yaml/merged/geosporobacter_subterreneus_medium__5a22a57c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `mediadive.medium:J548` identity, label, category, liquid state, and pH 7.2 agree with the live JCM 548 source and the MediaDive REST payload.

The same JCM recipe is imported separately through Togo M550. The normalized Togo row cites `JCM_M548` and the same `GRMD=548` URL, but it remains a separate generated record because its `Solution A` and stock-addition structure does not fingerprint-match the flattened MediaDive record.

The small-molecule groundings on ammonium chloride, glucose, sodium hydrogencarbonate, sodium sulfide nonahydrate, and resazurin are plausible for those source strings. `Sea Salt` is still ungrounded, which is acceptable for this branded complex sea-salts mixture unless a precise product term is available.

## Evidence

JCM 548 defines `Solution A` as 10 g Sea salts (Sigma), 1 g NH4Cl, 1 mg resazurin, and 920 ml distilled water. It then instructs curators to distribute 0.92 volume, with 4.6 ml in a Hungate tube as the example, before autoclaving under a N2-CO2 4:1 gas mixture.

JCM 548 completes the medium by adding 0.05 ml 10% yeast extract solution, 0.1 ml 1 M glucose, 0.2 ml 5% NaHCO3 solution, and 0.05 ml 2% Na2S x 9H2O solution per 4.6 ml of autoclaved medium.

MediaDive preserves `Solution A` as a 920 ml solution and keeps the four post-autoclave additions as milliliter stock additions with 10%, 1 M, 5%, and 2% attributes.

The generated record keeps the two preparation sentences, but the second one ends at the colon introducing the stock table while the four table rows have been recoded as direct ingredients.

## Completeness

`Solution A` is absent as a named 920 ml subrecipe in the generated record, and the 920 ml distilled-water row is absent entirely.

The four stock additions after autoclaving are absent as solution additions with milliliter units and stock strengths.

The N2-CO2 4:1 atmosphere, Hungate-tube example, NaHCO3 filter sterilization, and anaerobic storage context are retained only in free text, which is enough for review but should remain attached to the solution workflow if the recipe is normalized.

Empty growth-evidence, variant, discussion, and publication slots are acceptable for this imported source recipe.

## Findings

- Major: The generated formula uses the 920 ml `Solution A` stock concentrations directly: Sea Salt 10.8696 g/L, NH4Cl 1.08696 g/L, and resazurin 0.00108696 g/L. JCM uses 0.92 volume of this stock and 0.08 volume of other additions, so the final medium should not publish those undiluted values.
- Major: The four completion stocks were converted from ml additions with explicit strengths to direct `G_PER_L` ingredients. The generated `Yeast extract` 0.05 g/L, `Glucose` 0.1 g/L, `NaHCO3` 0.2 g/L, and `Na2S x 9 H2O` 0.05 g/L rows are the source's ml volumes, not final mass concentrations.
- Major: The JCM 548 `Solution A` boundary and its 920 ml distilled-water row are missing, which makes the retained instruction to add stock solutions "per 4.6 ml" impossible to follow from structured data.
- Major: The direct MediaDive/JCM record is split from the equivalent Togo M550 import for `JCM_M548`.

## Recommended Edits

- In `data/normalized_yaml/bacterial/geosporobacter_subterreneus_medium.yaml`, represent `Solution A` as its own 920 ml subrecipe and use it at 4.6 ml per 5 ml final medium, matching the JCM 548 example.
- Preserve 10% yeast extract solution, 1 M glucose, 5% NaHCO3 solution, and 2% Na2S x 9H2O solution as milliliter stock additions instead of direct final `G_PER_L` ingredients.
- Keep the JCM post-autoclave sterilization and anaerobic storage instructions attached to the relevant stock additions.
- Align the MediaDive J548 and Togo M550 normalized inputs so the regenerated merge combines or explicitly cross-links the equivalent source records.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/geosporobacter_subterreneus_medium__5a22a57c.yaml` and confirm it no longer contains direct 0.05 g/L yeast extract, 0.1 g/L glucose, 0.2 g/L NaHCO3, or 0.05 g/L Na2S x 9H2O rows.
- Confirm the regenerated recipe retains `Solution A` with 920 ml water and a 4.6 ml addition amount.
- Re-run LinkML, strict, reference, and term validation on the regenerated generated YAML.
- Re-run an ignored-file-inclusive exact search for `JCM_M548`, `mediadive.medium:J548`, and `GRMD=548` to confirm the MediaDive and Togo branches no longer publish the same JCM recipe as unrelated generated records.

## Additional Notes

The exact local source search used `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`, so ignored generated records and indexes were included.

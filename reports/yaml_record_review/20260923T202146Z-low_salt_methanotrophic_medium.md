# YAML Record Review: Low-Salt Methanotrophic Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/low_salt_methanotrophic_medium.yaml`
- Started UTC: `2026-09-23T20:20:21Z`
- Finished UTC: `2026-09-23T20:21:46Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:010268`
- `name`: `low_salt_methanotrophic_medium`
- `original_name`: `Low-Salt Methanotrophic Medium`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `TOGO:M852`
- `merge_fingerprint`: `b6a1c86414c571771229312aee7d91d10e40bf558c6ec1f72038547a3bffca8a`
- `merged_from`: `TOGO_M852_Low-Salt_Methanotrophic_Medium`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/low_salt_methanotrophic_medium.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:010268`, `TOGO:M852`, `Source: JCM, ID: M852`, `low_salt_methanotrophic_medium`, the owner filename, and the merge fingerprint found the maintained owner `data/normalized_yaml/bacterial/TOGO_M852_Low-Salt_Methanotrophic_Medium.yaml` plus this generated record.
- The same search also found a separate maintained record, `data/normalized_yaml/bacterial/low_salt_methanotrophic_medium.yaml`, and generated record, `data/merge_yaml/merged/low_salt_methanotrophic_medium__082cce68.yaml`, with the same normalized `name` for `CultureMech:003161` / `mediadive.medium:J817`.
- The TOGO M852 metadata identifies this medium as `Low-Salt Methanotrophic Medium`, original media ID `JCM_M817`, source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=817`, and pH 6.8.
- The live JCM URL for formula 817 returned a `Nothing found` page during this review, but MediaDive REST still resolved JCM `J817` to `LOW-SALT METHANOTROPHIC MEDIUM` with pH 6.8 and stock solutions that align with the TOGO M852 stock structure.

## Evidence

- TOGO M852 has `main solution 1` with 1 L distilled water, 0.1 g `MgSO4 x 7 H2O`, 0.02 g `CaCl2 x 2 H2O`, 0.1 g `KNO3`, 0.1 g `KBr`, 0.1 ml `Trace element solution (see Medium [M850])`, and 0.1 ml `Iron stock solution (see Medium [M850])`.
- TOGO M852 has `main solution 2` with 0.1 ml `Vitamin solution`, 1 ml `Phosphate buffer stock solution (see Medium [M850])`, and 0.1 ml `Selenite--tungstate solution (see Medium [M431])`.
- TOGO M852 has a separate `Vitamin solution` made in 1 L distilled water with 1 mg biotin, 10 mg `p--Aminobenzoic acid`, 10 mg `Thiamine HCl`, 10 mg `Pyridoxine HCl`, 5 mg vitamin B12, 20 mg riboflavin, and 20 mg nicotinic acid.
- TOGO M852 instructs curators to mix components and autoclave, add the autoclaved or filter-sterilized solutions after cooling, adjust to pH 6.8, distribute 20 ml aliquots into 120 ml serum bottles, seal with butyl rubber stoppers, and add 100 ml filter-sterilized methane gas to the headspace.
- MediaDive J817 resolves the same JCM formula as one main solution and separate vitamin, trace-element, iron, phosphate-buffer, and selenite-tungstate stock solutions.
- The generated record flattens the vitamin stock ingredients into top-level ingredients with their mg amounts preserved as `G_PER_L`, collapses the two distinct 1 L distilled-water rows into one top-level 2.0 `G_PER_L` water row, and stores the five stock-solution additions as 0.1 or 1 `G_PER_L` instead of milliliter additions.

## Completeness

- The generated record preserves the TOGO medium accession and the top-level mineral rows.
- The generated stock-solution model is incomplete: the five `solutions` entries have empty `composition` arrays, lose the stock medium IDs as typed references, and use mass-concentration units for milliliter stock additions.
- The generated ingredient list is over-flattened: vitamin-stock constituents are represented as final-medium grams per liter rather than as components of a 1 L vitamin stock added at 0.1 ml.
- The generated preparation section is absent despite detailed source preparation, pH adjustment, bottle, stopper, filter-sterilization, and methane-headspace instructions.
- The generated corpus contains a same-name sibling for JCM J817 / `CultureMech:003161` that should be reconciled against TOGO M852 before either record is treated as a unique medium.

## Findings

1. Stock solution boundaries and units were flattened into wrong top-level concentrations.
   - Evidence: TOGO M852 keeps vitamin ingredients inside `Vitamin solution` and adds only 0.1 ml of that stock to the main medium; the generated record instead stores `Biotin` as 1 `G_PER_L`, `p--Aminobenzoic acid` as 10 `G_PER_L`, and similar top-level gram-per-liter rows.
   - Impact: final-medium consumers see stock concentrate ingredients at biologically impossible amounts and cannot reconstruct the actual medium.

2. Stock additions are typed as grams per liter instead of milliliter additions.
   - Evidence: TOGO M852 adds 0.1 ml trace elements, 0.1 ml iron stock, 0.1 ml vitamin stock, 1 ml phosphate buffer, and 0.1 ml selenite--tungstate solution; the generated `solutions` entries store the same numeric values with `unit: G_PER_L`.
   - Impact: each stock addition has the wrong dimension and cannot be interpreted as the TOGO or JCM recipe intended.

3. Distinct water rows from separate solution scopes were merged.
   - Evidence: TOGO M852 has one 1 L water row in `main solution 1` and a second 1 L water row in `Vitamin solution`; the generated record collapses them into a single 2.0 `G_PER_L` top-level `Distilled water` row.
   - Impact: the generated record erases the vitamin-stock preparation boundary and creates a solvent amount that is neither source row.

4. Source preparation instructions are missing.
   - Evidence: TOGO M852 states when to autoclave, when to add sterilized stocks, the target pH of 6.8, the 20 ml fill volume, 120 ml serum bottle, butyl rubber stopper, and 100 ml methane headspace; the generated YAML has no `preparation_steps`.
   - Impact: following the generated record would omit required post-autoclave additions and methane headspace setup.

5. The corpus has two same-name records for the same JCM formula lineage.
   - Evidence: TOGO M852 reports original media ID `JCM_M817`; MediaDive resolves JCM `J817` to `LOW-SALT METHANOTROPHIC MEDIUM`; `data/normalized_yaml/bacterial/low_salt_methanotrophic_medium.yaml` owns a second `low_salt_methanotrophic_medium` record for `CultureMech:003161`.
   - Impact: search and merge outputs expose duplicate generated records for the same formulation under the same normalized name.

## Recommended Edits

1. Rework `data/normalized_yaml/bacterial/TOGO_M852_Low-Salt_Methanotrophic_Medium.yaml` or the TOGO importer so M852 preserves main-solution and stock-solution boundaries, milliliter stock additions, water rows, and pH 6.8.
2. Represent the M852 `Vitamin solution` composition as a stock solution, not as final-medium top-level ingredients.
3. Add source-backed preparation steps for autoclaving, post-cooling additions, pH adjustment, 20 ml / 120 ml bottle dispensing, butyl-rubber sealing, and 100 ml methane headspace.
4. Reconcile `CultureMech:010268` with the JCM/MediaDive `CultureMech:003161` sibling before regenerating to avoid keeping duplicate generated `low_salt_methanotrophic_medium` pages.
5. Replace the legacy `KNO3` `mediaingredientmech_term` with the CHEBI-keyed enrichment shape when the owner is corrected.

## Follow-up Checks

- Re-fetch TOGO M852 and MediaDive J817, then verify that the corrected owner preserves all main and stock solution rows with source units and scope.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Run an ignored-inclusive exact search for `low_salt_methanotrophic_medium`, `J817`, `JCM_M817`, and `TOGO:M852` after de-duplication to confirm the target is no longer represented by two active CultureMech records.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.
- The JCM formula URL cited by TOGO M852 was checked and returned `Nothing found`; MediaDive's J817 REST record was used as the JCM fallback for formula details.

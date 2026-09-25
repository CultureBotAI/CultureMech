# YAML Record Review: LOW-SALT METHANOTROPHIC MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/low_salt_methanotrophic_medium__082cce68.yaml`
- Started UTC: `2026-09-23T20:21:55Z`
- Finished UTC: `2026-09-23T20:22:57Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:003161`
- `name`: `low_salt_methanotrophic_medium`
- `original_name`: `LOW-SALT METHANOTROPHIC MEDIUM`
- `category`: `bacterial`
- `medium_type`: `DEFINED`
- `composition_type`: `DEFINED`
- `physical_state`: `LIQUID`
- `ph_value`: `6.8`
- `media_term`: `mediadive.medium:J817`
- `merge_fingerprint`: `082cce68dd221327fd9017cdcf26a0007339ea8a881bf60c83072e7138089114`
- `merged_from`: `low_salt_methanotrophic_medium`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/low_salt_methanotrophic_medium__082cce68.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:003161`, `mediadive.medium:J817`, `Source: JCM, ID: J817`, `low_salt_methanotrophic_medium`, and the merge fingerprint found one maintained owner, `data/normalized_yaml/bacterial/low_salt_methanotrophic_medium.yaml`, plus this generated record.
- The same search also found `data/normalized_yaml/bacterial/TOGO_M852_Low-Salt_Methanotrophic_Medium.yaml` and `data/merge_yaml/merged/low_salt_methanotrophic_medium.yaml`, a separate `CultureMech:010268` / `TOGO:M852` record with the same normalized name for the same JCM 817 formula lineage.
- The generated record merges exactly one owner on the recorded fingerprint and preserves the MediaDive JCM medium ID.
- MediaDive REST resolves `J817` as JCM `LOW-SALT METHANOTROPHIC MEDIUM`, pH 6.8, and `complex_medium: no`.
- The live JCM URL saved in the record notes returned a `Nothing found` page during this review; the same formula is still available through MediaDive's J817 REST record.

## Evidence

- MediaDive J817 has a `Main sol. J817` with 0.1 g KNO3, 0.1 g `MgSO4 x 7 H2O`, 0.02 g `CaCl2 x 2 H2O`, 0.1 g KBr, 0.1 ml trace element stock, 0.1 ml iron stock, 1000 ml distilled water, 0.1 ml vitamin stock, 1 ml phosphate buffer stock, and 0.1 ml selenite-tungstate stock.
- MediaDive J817 has separate `Vitamin solution`, `Trace element solution`, `Iron stock solution 4.5 g/L`, `Phosphate buffer stock solution`, and `Selenite-tungstate solution` records with their own component rows.
- MediaDive J817 keeps the pH 6.8 and preparation steps: autoclave main components, add autoclaved or filter-sterilized solutions after cooling, adjust pH to 6.8, dispense 20 ml into 120 ml serum bottles, seal with butyl rubber stoppers, and add 100 ml filter-sterilized methane to the headspace.
- The generated record has a flat list of main-medium salts plus all vitamin, trace-element, iron, phosphate-buffer, and selenite-tungstate stock ingredients as top-level ingredients; it has no `solutions` array.

## Completeness

- The generated record preserves the MediaDive/JCM identity, pH 6.8, most stock ingredient identities, and the two source preparation steps.
- The generated record loses the main/stock solution boundaries and the stock-addition volumes, so the ingredient list does not distinguish final-medium 0.1 ml additions from 1 L stock recipes.
- The generated record omits every `Distilled water` row from the main and stock solutions.
- The live JCM source link in `notes` was not retrievable during this review; MediaDive was retrievable and should be recorded as recoverable source provenance.
- The generated corpus contains a TOGO M852 same-name sibling for the same JCM 817 lineage.

## Findings

1. Stock solutions were flattened into final-medium ingredient rows.
   - Evidence: MediaDive J817 adds 0.1 ml vitamin stock and 0.1 ml trace-element stock to the main solution; the generated record has no `solutions` array and stores vitamin and trace-element stock components as top-level `G_PER_L` ingredient rows.
   - Impact: downstream consumers cannot tell whether 20 mg/L riboflavin is a vitamin-stock concentration or a final-medium concentration after 0.1 ml stock addition.

2. Main-medium stock additions were omitted.
   - Evidence: MediaDive `Main sol. J817` includes 0.1 ml trace element stock, 0.1 ml iron stock, 0.1 ml vitamin stock, 1 ml phosphate buffer stock, and 0.1 ml selenite-tungstate stock; the generated record has no ingredient or solution rows for those additions.
   - Impact: following only the generated record gives no way to reproduce the actual stock-addition recipe.

3. Main and stock water rows were dropped.
   - Evidence: MediaDive J817 includes 1000 ml distilled water in the main solution and 1000 ml distilled water in each stock solution; the generated YAML contains no `Distilled water` ingredient or stock component.
   - Impact: the final volume and stock volumes are implicit and cannot be validated from the generated record.

4. The corpus has two same-name records for the same JCM formula lineage.
   - Evidence: TOGO M852 reports original media ID `JCM_M817`; MediaDive resolves JCM `J817` to `LOW-SALT METHANOTROPHIC MEDIUM`; `data/normalized_yaml/bacterial/TOGO_M852_Low-Salt_Methanotrophic_Medium.yaml` owns a second `low_salt_methanotrophic_medium` record for `CultureMech:010268`.
   - Impact: search and merge outputs expose duplicate generated records for the same formulation under the same normalized name.

5. The only direct JCM link in the record is stale.
   - Evidence: `notes` points to the JCM GRMD 817 URL, but that page returned `Nothing found` during this review; MediaDive REST for `J817` still returns the formulation.
   - Impact: users cannot recover the formulation from the cited JCM URL without knowing to query MediaDive.

6. `KNO3` still carries a deprecated `mediaingredientmech_term` link.
   - Evidence: the generated and maintained `KNO3` ingredient rows have `term: CHEBI:63043` but retain `mediaingredientmech_term: MediaIngredientMech:000170`; the June 2026 curation event notes that the legacy `MediaIngredientMech:NNNNNN` ID scheme was deprecated.
   - Impact: this row missed the CHEBI-keyed enrichment shape used by the other migrated rows.

## Recommended Edits

1. Rework `data/normalized_yaml/bacterial/low_salt_methanotrophic_medium.yaml` or the MediaDive importer so J817 preserves the main solution, stock solutions, stock-addition volumes, stock water rows, and stock component rows in their original scopes.
2. Reconcile this JCM/MediaDive `CultureMech:003161` record with the TOGO M852 `CultureMech:010268` sibling before regenerating so the same JCM 817 formulation is not published twice.
3. Add MediaDive J817 as a retrievable source reference and keep the current JCM URL only as a dead or archival upstream pointer.
4. Replace the legacy `KNO3` `mediaingredientmech_term` object with the CHEBI-keyed enrichment shape used by the other CHEBI-grounded rows.

## Follow-up Checks

- Re-fetch MediaDive J817 and verify that all corrected main-medium and stock rows match the REST solution scopes.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Run an ignored-inclusive exact search for `low_salt_methanotrophic_medium`, `J817`, `JCM_M817`, and `TOGO:M852` after de-duplication to confirm the target is no longer represented by two active CultureMech records.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.
- The JCM formula URL in the generated record's `notes` was checked and returned `Nothing found`; MediaDive's J817 REST record was used as the live JCM fallback for formula details.

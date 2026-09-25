# YAML Record Review: capnocytophaga_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml
- Started UTC: 2026-09-22T03:28:51Z
- Finished UTC: 2026-09-22T03:28:51Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002808`, `capnocytophaga_medium`, class `MediaRecipe`.
- Merge lineage: one source recipe, `JCM_J459_CAPNOCYTOPHAGA_MEDIUM`, on fingerprint `ea2957598874d72d1d2638a79dac442eb99d1d80e5d90eba1827bb5c6256bfcd`.
- Maintained owner: `data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml`.
- Claimed source identity: JCM Medium 459, cross-listed in MediaDive as `mediadive.medium:J459`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The generated merge and normalized owner are materially identical: the merge only appends its `MERGED_RECIPES` event, `merge_fingerprint`, and `merged_from`.
- The record denotes JCM Medium 459, `CAPNOCYTOPHAGA MEDIUM`. The JCM page, the MediaDive J459 page, and the MediaDive J459 JSON all agree on the label, liquid complex classification, final pH 7.0, and six non-water ingredients imported into this record.
- A gitignore-independent exact search found this active owner and generated merge for `CultureMech:002808` / `mediadive.medium:J459`. It also found other same-name active Capnocytophaga records, but those resolve to DSMZ 340, KOMODO 340, and TOGO M459/M2175 rather than to JCM 459.
- `Trypticase peptone` and `Yeast extract` are complex source ingredients and are reasonably left without CHEBI groundings; the packaged MediaIngredientMech index does, however, provide an exact `MICRO:0000175` mapping for the Trypticase peptone label.

## Evidence

- JCM Medium 459 lists Trypticase peptone 17 g, Yeast extract 3 g, Glucose 3 g, NaCl 3 g, KNO3 3 g, Hemin 3 mg, and Distilled water 1 L; MediaDive's J459 JSON preserves the same `Main sol. J459` recipe as `mediadive.solution:4206` with the same converted g/L values.
- JCM's Medium 459 page says to adjust pH to 7.0, separately autoclave glucose, and incubate under an oxygen-free atmosphere containing 5-10% CO2. It also states the JCM default that, unless otherwise stated, media are sterilized by autoclaving at 121 deg C for 15 min.
- The normalized owner captured the medium-specific pH, separate-glucose, and incubation instructions, but did not preserve the source water row or the default autoclave condition for the non-glucose base.
- The active solution import `data/normalized_yaml/bacterial/mediadive_4206_Main_sol_J459.yaml` represents the same `mediadive.solution:4206` main solution, but the generated medium does not link to it, and the solution stores `Distilled water` as `1000 PERCENT_V_V` instead of `1000 ML_PER_L`.

## Completeness

- The generated record is missing the source `Distilled water` row.
- The generated record tells curators to autoclave glucose separately but omits the JCM default autoclaving rule that applies to the rest of the medium.
- KNO3 has a correct CHEBI primary `term`, but its `mediaingredientmech_term` is still a legacy `MediaIngredientMech:000170` object rather than the CHEBI-keyed mirror used on Glucose, NaCl, and Hemin.
- Target organisms, variants, and references are empty. The inspected formula source is sufficient for composition and preparation, but this record has not tried to curate strain-specific growth claims.

## Findings

- Major: the generated record omits the required 1 L distilled-water component. JCM, MediaDive J459, and the active `mediadive.solution:4206` import all include it.
- Major: the preparation is incomplete. The record preserves the source instruction to autoclave glucose separately, but does not preserve JCM's default 121 deg C, 15 min autoclave condition for the rest of the medium.
- Minor: `Trypticase peptone` is ungrounded despite a unique packaged MediaIngredientMech mapping to `MICRO:0000175`.
- Minor: KNO3 still carries a legacy `mediaingredientmech_term` even though its primary CHEBI grounding is correct.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml`, not the generated merge.
- Add `Distilled water` at `1000 ML_PER_L` to the maintained medium owner, and repair `data/normalized_yaml/bacterial/mediadive_4206_Main_sol_J459.yaml` so the standalone solution uses `ML_PER_L` rather than `PERCENT_V_V` for the same water row.
- Add a main-medium autoclave step preserving JCM's default 121 deg C for 15 min sterilization, keeping glucose's separate autoclave instruction explicit.
- Ground `Trypticase peptone` to `MICRO:0000175` if MICRO terms are accepted in ingredient rows; otherwise document why this exact packaged mapping should remain unused.
- Replace KNO3's legacy `mediaingredientmech_term` with the CHEBI-keyed `mediaingredientmech_chebi_term` mirror.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the maintained owner and `data/normalized_yaml/bacterial/mediadive_4206_Main_sol_J459.yaml`.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml`.
- Inspect the regenerated merge to confirm it contains `Distilled water`, a main-medium autoclave step, no legacy KNO3 MIM field, and the intended Trypticase peptone grounding state.
- Re-check the JCM Medium 459 page and MediaDive J459 JSON export to confirm the formula and the default autoclaving rule still match.

## Additional Notes

- `find . -iname '*capnocytophaga*'` included ignored and hidden files and found expected active siblings for JCM 459, DSMZ/MediaDive 340, KOMODO 340, TOGO M459, and TOGO M2175, plus their generated merges; no hidden or ignored second owner for JCM 459 was present under this checkout.
- `CAPNOCYTOPHAGA_II_MEDIUM.yaml` is the preceding casefold record but denotes DSMZ/MediaDive Medium 779, not JCM 459.

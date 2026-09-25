# YAML Record Review: capnocytophaga_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/capnocytophaga_medium__a7f2b87e.yaml
- Started UTC: 2026-09-22T03:32:42Z
- Finished UTC: 2026-09-22T03:32:42Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:005049`, `capnocytophaga_medium`, class `MediaRecipe`.
- Merge lineage: three source recipes, `KOMODO_340_CAPNOCYTOPHAGA_medium`, `capnocytophaga_medium`, and `medium_340_modified_for_dsm_7271`, on fingerprint `a7f2b87ec5cc7c7aa2630804b8e1bc258ba29c6ced4b3844f184e30ddc74d48c`.
- Maintained owners: `data/normalized_yaml/bacterial/KOMODO_340_CAPNOCYTOPHAGA_medium.yaml`, `data/normalized_yaml/bacterial/capnocytophaga_medium.yaml`, and `data/normalized_yaml/bacterial/medium_340_modified_for_dsm_7271.yaml`.
- Claimed source identities: KOMODO medium 340 mirrored from DSMZ/MediaDive medium 340, direct DSMZ/MediaDive medium 340, and KOMODO medium 340_7271 mirrored from the same DSMZ/MediaDive medium 340 formula.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation exited successfully for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The generated record denotes DSMZ/MediaDive Medium 340, `CAPNOCYTOPHAGA MEDIUM`. The DSMZ PDF and MediaDive JSON agree on the label, complex liquid classification, final pH 7.0, six non-water components, 1000 ml distilled water, and two preparation instructions.
- The duplicate link among the KOMODO 340 mirror, direct DSMZ/MediaDive owner, and KOMODO 340_7271 mirror is structurally plausible: all three active normalized records have identical imported solute names and concentrations, and both KOMODO records explicitly cite DSMZ Medium 340 in their notes.
- The generated merge chose the KOMODO 340 mirror as the canonical body, so `media_term` is `komodo.medium:340` and `notes` say `Aerobic: Yes` even though the direct DSMZ owner cites `mediadive.medium:340` and stores the pH adjustment plus the oxygen-free, 5-10% CO2 incubation instruction.
- `Trypticase` is incorrectly grounded to `CHEBI:78018` dodecylphosphocholine; the packaged ingredient occurrence output shows that the legacy `MediaIngredientMech:000263` label has a unique exact mapping to `MICRO:0000175`.
- `Yeast extract` is a complex source ingredient and is reasonably left without a CHEBI grounding. The other simple ingredients use source-compatible CHEBI primary terms.

## Evidence

- DSMZ Medium 340 lists Trypticase 17 g, Yeast extract 3 g, Glucose 3 g, NaCl 3 g, KNO3 3 g, Haemin 3 mg, and Distilled water 1000 ml.
- MediaDive's Medium 340 JSON preserves the same `Main sol. 340` recipe as `mediadive.solution:653` with the same formula, the same 1000 ml solution volume, and a structured `Distilled water` row.
- DSMZ and MediaDive both require pH adjustment to 7.0, separate sterilization of glucose, and incubation in an oxygen-free atmosphere containing 5-10% CO2.
- The active solution import `data/normalized_yaml/bacterial/mediadive_653_Main_sol_340.yaml` represents the same `mediadive.solution:653` main solution, but the generated medium does not link to it, and the solution stores `Distilled water` as `1000 PERCENT_V_V` instead of `1000 ML_PER_L`.

## Completeness

- The generated record is missing the source `Distilled water` row.
- The generated record is missing both preparation instructions from the direct DSMZ owner.
- KNO3 has a correct CHEBI primary `term`, but its `mediaingredientmech_term` is still a legacy `MediaIngredientMech:000170` object rather than the CHEBI-keyed mirror used on Glucose, NaCl, and Haemin.
- The KOMODO 340 owner says `Aerobic: Yes`; DSMZ instead specifies an oxygen-free CO2-containing atmosphere, and the KOMODO 340_7271 sibling says `Aerobic: No`.
- Target organisms, evidence, variants other than source-duplicate relationships, and references are empty. The inspected DSMZ/MediaDive source is sufficient for composition and preparation, but this record has not tried to curate strain-specific growth claims.

## Findings

- Major: the source-duplicate merge discarded DSMZ/MediaDive preparation instructions. `data/normalized_yaml/bacterial/capnocytophaga_medium.yaml` stores the pH adjustment and separate-glucose/oxygen-free incubation text, but the generated `CultureMech:005049` body is inherited from the KOMODO mirror and has no `preparation_steps`.
- Major: the generated record omits the required 1000 ml distilled-water component. DSMZ, MediaDive Medium 340, and the active `mediadive.solution:653` import all include it.
- Major: `Trypticase` is grounded to an unrelated surfactant, `CHEBI:78018` dodecylphosphocholine, rather than to the exact packaged `MICRO:0000175` mapping.
- Minor: KNO3 still carries a legacy `mediaingredientmech_term` even though its primary CHEBI grounding is correct.
- Minor: the KOMODO `Aerobic: Yes` note is incompatible with the inspected DSMZ/MediaDive instruction to incubate under an oxygen-free, CO2-containing atmosphere.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/KOMODO_340_CAPNOCYTOPHAGA_medium.yaml`, `data/normalized_yaml/bacterial/capnocytophaga_medium.yaml`, and `data/normalized_yaml/bacterial/medium_340_modified_for_dsm_7271.yaml`, not the generated merge.
- Copy the DSMZ pH adjustment and separate-glucose/oxygen-free incubation instructions into the KOMODO mirrors, or make the merge prefer the direct DSMZ/MediaDive owner when an exact `SOURCE_DUPLICATE` exists, then regenerate the merged record.
- Add `Distilled water` at `1000 ML_PER_L` to the maintained medium owners, and repair `data/normalized_yaml/bacterial/mediadive_653_Main_sol_340.yaml` so the standalone solution uses `ML_PER_L` rather than `PERCENT_V_V` for the same water row.
- Reground `Trypticase` to `MICRO:0000175` if MICRO terms are accepted in ingredient rows; otherwise remove the unrelated `CHEBI:78018` primary term and document why this exact packaged mapping should remain unused.
- Replace KNO3's legacy `mediaingredientmech_term` with the CHEBI-keyed `mediaingredientmech_chebi_term` mirror.
- Replace the KOMODO `Aerobic: Yes` note with source-backed oxygen-free CO2 incubation text, or drop it once the structured preparation steps carry the atmosphere instruction.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against all three maintained medium owners and `data/normalized_yaml/bacterial/mediadive_653_Main_sol_340.yaml`.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/capnocytophaga_medium__a7f2b87e.yaml`.
- Inspect the regenerated merge to confirm it contains `Distilled water`, the DSMZ preparation instructions, no legacy KNO3 MIM field, a repaired Trypticase grounding state, and no unsupported aerobic-only note.
- Re-check the MediaDive Medium 340 JSON export and DSMZ PDF to confirm the maintained medium and solution still match all source rows and instructions.

## Additional Notes

- `rg --no-ignore --hidden -l` for the exact record IDs and source identifiers included ignored and hidden files; it found the three active normalized owners, the generated merge, generated indexes/catalogs, archived validation reports, the growth review page, and ingredient occurrence output, but no fourth active normalized owner for these exact DSMZ/KOMODO 340 records.
- `find . -iname '*capnocytophaga*'` also included ignored and hidden files and found expected active siblings for DSMZ/MediaDive 340, KOMODO 340, KOMODO 340_7271, JCM 459, DSMZ/MediaDive 779, KOMODO 779, TOGO M459, and TOGO M2175, plus their generated merges and existing review reports.

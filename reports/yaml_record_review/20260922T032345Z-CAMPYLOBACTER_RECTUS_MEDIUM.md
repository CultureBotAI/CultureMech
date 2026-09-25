# YAML Record Review: campylobacter_rectus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CAMPYLOBACTER_RECTUS_MEDIUM.yaml
- Started UTC: 2026-09-22T03:23:45Z
- Finished UTC: 2026-09-22T03:23:45Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:005035`, `campylobacter_rectus_medium`, class `MediaRecipe`.
- Merge lineage: two source recipes, `KOMODO_338_CAMPYLOBACTER_RECTUS_medium` and `campylobacter_rectus_medium`, on fingerprint `38474ba3b3f6acfd01dcaf01226a0bf41620c089cf8342538d2326e8fda43554`.
- Maintained owners: `data/normalized_yaml/bacterial/KOMODO_338_CAMPYLOBACTER_RECTUS_medium.yaml` and `data/normalized_yaml/bacterial/campylobacter_rectus_medium.yaml`.
- Claimed source identities: KOMODO medium 338 mirrored from DSMZ/MediaDive medium 338, and direct DSMZ/MediaDive medium 338.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The generated record denotes DSMZ/MediaDive Medium 338, `CAMPYLOBACTER RECTUS MEDIUM`. The DSMZ PDF, MediaDive HTML, and MediaDive JSON all agree on the label, complex liquid classification, pH 7.5, and the ten non-water ingredients at the concentrations imported into the generated record.
- The duplicate link between the KOMODO import and direct MediaDive/DSMZ import is valid: the active registry/catalog keeps both normalized owners as `ACTIVE`, a gitignore-independent exact search found only those two maintained owners plus the generated merge for `CultureMech:005035`, `CultureMech:001438`, `komodo.medium:338`, and `mediadive.medium:338`, and `find . -iname '*campylobacter*rectus*'` found no hidden or ignored sibling raw capture.
- The generated merge chose the KOMODO mirror as the canonical body, so `media_term` is `komodo.medium:338` and `notes` say `Aerobic: Yes` even though the direct DSMZ owner cites `mediadive.medium:338` and stores the anaerobic preparation steps.
- The `Trypticase` row is grounded to `CHEBI:78018` / `dodecylphosphocholine`, which is unrelated to the DSMZ `Trypticase (BBL)` ingredient. The packaged MediaIngredientMech label index maps exact `Trypticase` and the BBL trypticase-peptone synonyms to `MICRO:0000175`.

## Evidence

- DSMZ Medium 338 lists Beef extract 3 g, Trypticase 9 g, Yeast extract 11 g, NaCl 2 g, Na2HPO4 0.4 g, Na2CO3 0.25 g, Haemin 5 mg, Na-formate 2 g, Na-fumarate 3 g, Resazurin 1 mg, and Distilled water 1000 ml; MediaDive's Medium 338 JSON preserves the same one-solution recipe, compound order, source attributes `Difco` and `BBL`, and converted g/L values.
- DSMZ and MediaDive both require pH adjustment to 7.5, anaerobic preparation under 100% N2, and separate nitrogen autoclaving for haemin, formate, and fumarate solutions.
- No inspected DSMZ or MediaDive source supports the KOMODO-imported `Aerobic: Yes` note.
- The active solution import `data/normalized_yaml/bacterial/mediadive_650_Main_sol_338.yaml` represents the same `mediadive.solution:650` main solution, but the generated medium does not link to it, and the solution stores `Distilled water` as `1000 PERCENT_V_V` instead of `1000 ML_PER_L`.

## Completeness

- The generated record is missing the source `Distilled water` row. Because Medium 338 is a one-liter main solution and the MediaDive solution import includes that row, this is a representational omission rather than an intentionally empty optional field.
- The generated record is missing both anaerobic preparation steps from the direct DSMZ owner, including the special haemin stock made in 0.1 ml 1N NaOH and diluted to 10 ml before neutralization.
- Target organisms, variants other than the source-duplicate relationship, incubation conditions, and references are empty. DSMZ Medium 338 does list strain associations on MediaDive, but this generated record has not yet tried to curate target-organism growth claims, so those empty slots should stay empty until a growth-evidence pass.

## Findings

- Major: the source-duplicate merge discarded DSMZ/MediaDive preparation instructions. `data/normalized_yaml/bacterial/campylobacter_rectus_medium.yaml` stores the two DSMZ steps, but the generated `CultureMech:005035` body is inherited from the KOMODO mirror and has no `preparation_steps`.
- Major: the generated record omits the required 1000 ml distilled-water component. DSMZ, MediaDive Medium 338, and the active `mediadive.solution:650` import all include it.
- Major: the generated notes contradict the DSMZ procedure by saying `Aerobic: Yes`. DSMZ and MediaDive both say the medium is prepared anaerobically under 100% N2 and that haemin, formate, and fumarate solutions are autoclaved separately under nitrogen.
- Major: `Trypticase` has the wrong CHEBI grounding. Both normalized owners map the DSMZ `Trypticase (BBL)` row to `CHEBI:78018` / `dodecylphosphocholine`, while the packaged label index supplies `MICRO:0000175` for exact `Trypticase`.
- Minor: both normalized medium owners still carry a legacy `mediaingredientmech_term` on `Trypticase`, while all supported simple-chemical rows have already been migrated to `mediaingredientmech_chebi_term`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/KOMODO_338_CAMPYLOBACTER_RECTUS_medium.yaml` and `data/normalized_yaml/bacterial/campylobacter_rectus_medium.yaml`, not the generated merge.
- Copy the DSMZ anaerobic `preparation_steps` into the KOMODO mirror or make the merge prefer the direct DSMZ/MediaDive owner when an exact `SOURCE_DUPLICATE` exists, then regenerate the merged record.
- Add `Distilled water` at `1000 ML_PER_L` to both maintained medium owners, and repair `data/normalized_yaml/bacterial/mediadive_650_Main_sol_338.yaml` so its solution composition uses `ML_PER_L` rather than `PERCENT_V_V` for the same water row.
- Remove the `Aerobic: Yes` note from the KOMODO owner or replace it with source-backed anaerobic preparation text.
- Replace the `CHEBI:78018` dodecylphosphocholine grounding on `Trypticase` with the exact packaged `MICRO:0000175` mapping, preserving the DSMZ source text.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against both maintained medium owners and `data/normalized_yaml/bacterial/mediadive_650_Main_sol_338.yaml`.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/CAMPYLOBACTER_RECTUS_MEDIUM.yaml`.
- Inspect the regenerated merge to confirm it contains `Distilled water`, both anaerobic DSMZ steps, no aerobic note, and no `CHEBI:78018` grounding on `Trypticase`.
- Re-check the MediaDive Medium 338 JSON export and DSMZ PDF to confirm the maintained medium and solution still match all source rows and instructions.

## Additional Notes

- MediaDive exposes the same source formula as `mediadive.solution:650` / `Main sol. 338`, not only as flattened Medium 338 rows.
- The historical import-tracking report `data/import_tracking/reports/kg_fallback_consensus_changes.tsv` includes `mediadive_650_Main_sol_338` in the batch that replaced Trypticase's earlier fallback with `CHEBI:78018`; the wrong grounding was an automated corpus-consensus artifact, not a DSMZ claim.

# YAML Record Review: BEGGIATOA medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BEGGIATOA_MEDIUM.yaml
- Started UTC: 2026-09-21T19:36:47Z
- Finished UTC: 2026-09-21T19:39:07Z
- Verdict: needs curation

## Target

- Reviewed `data/merge_yaml/merged/BEGGIATOA_MEDIUM.yaml`.
- Class: `MediaRecipe`.
- ID: `CultureMech:004177`.
- Name: `beggiatoa_medium`.
- Original name: `BEGGIATOA medium`.
- Source identity: `komodo.medium:155`, label `BEGGIATOA medium`; the KOMODO owner cites DSMZ Medium 155.
- Generated status: derived merge output under `data/merge_yaml/merged/`; future curation belongs in both normalized duplicate owners followed by merge regeneration.
- Maintained owners:
  - `data/normalized_yaml/bacterial/KOMODO_155_BEGGIATOA_medium.yaml`, `CultureMech:004177`, `komodo.medium:155`.
  - `data/normalized_yaml/bacterial/beggiatoa_medium.yaml`, `CultureMech:001036`, `mediadive.medium:155`.
- Merge metadata: `SOURCE_DUPLICATE` merge of `KOMODO_155_BEGGIATOA_medium` and `beggiatoa_medium` on fingerprint `46875cbc6812cf0da16eded1674d637e24bbc87a459e4148add22170a5b4d524`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BEGGIATOA_MEDIUM.yaml` via the no-project Python 3.11 workaround | Passed |
| Closed-schema strict validation, `scripts/validate_strict.py data/merge_yaml/merged/BEGGIATOA_MEDIUM.yaml --out /private/tmp/BEGGIATOA_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/BEGGIATOA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were applicable |
| `linkml-term-validator validate-data data/merge_yaml/merged/BEGGIATOA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `MediaRecipe.curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not a focused embedded-history validator for one merged record |

The documented `just` commands were not run directly because the project runtime currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` before target-specific validation.

## Identity and Grounding

- `CultureMech:004177` resolves in `data/culturemech_id_registry.tsv` to `data/normalized_yaml/bacterial/KOMODO_155_BEGGIATOA_medium.yaml`; the merged DSMZ duplicate `CultureMech:001036` resolves to `data/normalized_yaml/bacterial/beggiatoa_medium.yaml`.
- MediaDive JSON, the rendered MediaDive page, and the linked DSMZ PDF all identify DSMZ Medium 155 as `BEGGIATOA MEDIUM`, source DSMZ, pH 7.4.
- The KOMODO record explicitly cites DSMZ Medium 155 and has the same pH, ingredient names, and concentration signatures as the DSMZ owner, so the source-duplicate merge is plausible.
- Several ingredient groundings are exact for the flattened chemical salts, but the current rows conflate complete solution additions with neat chemical additions. `CaSO4` is a 20 ml saturated calcium sulfate solution in the source, the trace elements are a separate 1000 ml stock added at 5 ml/L, and catalase is an activity-unit addition, not a mass concentration.

## Evidence

- DSMZ/MediaDive Medium 155 supports pH 7.4 and the five direct low-concentration salts or organics now represented as final g/L values: 0.45 mg NH4Cl, 0.1 mg K2HPO4, 0.2 mg magnesium sulfate heptahydrate, 0.5 g sodium acetate, and 0.5 g Difco nutrient broth per 1000 ml.
- DSMZ/MediaDive supports optional agar at 10 g per 1000 ml; the current `Agar` row preserves that quantity and has a note marking it as optional in practice.
- DSMZ/MediaDive says the first main-solution row is 20 ml saturated calcium sulfate solution. The current record instead says `20` `G_PER_L` of `CaSO4`.
- DSMZ/MediaDive says the main solution receives 5 ml `Trace element solution`, whose own 1000 ml stock contains EDTA, ferrous sulfate heptahydrate, zinc sulfate heptahydrate, manganese sulfate tetrahydrate, copper sulfate pentahydrate, boric acid, cobalt nitrate, sodium molybdate dihydrate, and distilled water. The current record flattens the stock recipe into final-medium ingredient rows and omits the 5 ml dilution.
- DSMZ/MediaDive says catalase is filter-sterilized and supplied as 15000 to 35000 units per 1000 ml. The current record says `35000` `G_PER_L`.
- DSMZ/MediaDive says distilled water is used to bring both the final medium and the trace element solution to 1000 ml. Neither water row is represented in the generated record.
- A gitignore-independent search over `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` for the exact CultureMech IDs, digit-bounded KOMODO/MediaDive 155 source IDs, digit-bounded `DSMZ Medium 155`, and both owner slugs found the two normalized owners, the generated merge, generated indexes, and import-priority reports. It did not find a repository-owned raw KOMODO or MediaDive capture for the reviewed Medium 155 records.

## Completeness

- Consequentially incomplete: the 5 ml trace stock boundary and its 1000 ml stock composition are not modeled, so the record overstates every trace element as though its stock g/L value were present directly in the final medium.
- Consequentially incomplete: the calcium sulfate saturated solution and catalase activity-unit additions are modeled with mass-concentration units that the source does not support.
- Consequentially incomplete in the generated KOMODO-canonical merge: the DSMZ preparation step about adjusting pH before autoclaving and adding catalase just before inoculation is absent, even though the DSMZ duplicate owner carries it.
- Empty target-organism and growth-evidence slots are acceptable here; DSMZ Medium 155 gives no strain-specific growth claim in the inspected source.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `CaSO4` is the wrong material and unit. The source requires 20 ml saturated calcium sulfate solution; both normalized owners record 20 g/L calcium sulfate. | `data/normalized_yaml/bacterial/KOMODO_155_BEGGIATOA_medium.yaml` and `data/normalized_yaml/bacterial/beggiatoa_medium.yaml` |
| Major | The 5 ml `Trace element solution` addition is flattened into undiluted final-medium ingredients. This loses the stock-solution boundary, omits the stock water row, and changes all downstream trace concentrations by the 5 ml into 1000 ml dilution factor. | `data/normalized_yaml/bacterial/KOMODO_155_BEGGIATOA_medium.yaml` and `data/normalized_yaml/bacterial/beggiatoa_medium.yaml` |
| Major | `Catalase` is expressed as `35000` `G_PER_L`; the source specifies filter-sterilized catalase activity, 15000 to 35000 units per 1000 ml, added just before inoculation. | `data/normalized_yaml/bacterial/KOMODO_155_BEGGIATOA_medium.yaml` and `data/normalized_yaml/bacterial/beggiatoa_medium.yaml` |
| Major | The generated KOMODO-canonical record lacks the preparation step that the DSMZ source and duplicate owner already contain, so it drops the timing of pH adjustment, autoclaving, and catalase addition. | `data/normalized_yaml/bacterial/KOMODO_155_BEGGIATOA_medium.yaml`, then merge regeneration |
| Minor | `Nutrient broth` omits the source attribute `Difco`, leaving a complex commercial ingredient less specific than DSMZ Medium 155. | `data/normalized_yaml/bacterial/KOMODO_155_BEGGIATOA_medium.yaml` and `data/normalized_yaml/bacterial/beggiatoa_medium.yaml` |

## Recommended Edits

1. In both normalized duplicate owners, replace the mass `CaSO4` row with a source-faithful 20 ml saturated calcium sulfate solution representation.
2. Represent `Trace element solution` as a 5 ml addition to the main medium and preserve its EDTA, ferrous sulfate, zinc sulfate, manganese sulfate, copper sulfate, boric acid, cobalt nitrate, sodium molybdate, and 1000 ml distilled-water stock recipe under the appropriate solution field or standalone solution record.
3. Replace the `Catalase` mass concentration with an activity-unit representation, keep the 15000 to 35000 units per 1000 ml range in structured fields or notes, and preserve its filter-sterilized post-autoclave addition.
4. Restore the DSMZ preparation instruction to the KOMODO owner so pH adjustment with indicator paper before autoclaving and just-before-inoculation catalase addition survive merge generation.
5. Preserve `Nutrient broth` as the Difco product rather than a fully generic nutrient-broth row if the schema has a source attribute or notes slot for that detail.
6. Regenerate `data/merge_yaml/merged/BEGGIATOA_MEDIUM.yaml` after both owners are corrected.

## Follow-up Checks

- Rerun the open schema validator, `scripts/validate_strict.py`, `linkml-term-validator`, and `linkml-reference-validator` on both normalized owners and the regenerated merged record.
- Rerun the repository merge verifier documented for duplicate-owner changes to prove `data/merge_yaml/merged/BEGGIATOA_MEDIUM.yaml` reflects the corrected owners.
- Manually compare the regenerated record against the DSMZ Medium 155 PDF or MediaDive 155 JSON and verify the 20 ml calcium sulfate solution, 5 ml trace solution addition, catalase activity units, two 1000 ml water rows, and pH/catalase timing.

## Additional Notes

- MediaDive JSON, the MediaDive rendered page, and the DSMZ PDF agreed for every inspected ingredient, amount, solution boundary, and preparation instruction.
- The initial repository search was corrected to digit-bound `mediadive.medium:155` and `DSMZ Medium 155`, so the final negative raw-source statement is not based on broader matches to DSMZ 1550-series media.
- Reports are read-only review artifacts; no normalized recipe, generated merge, page, history entry, or GitHub issue was edited for this review.

# YAML Record Review: flexibacter_canadensis_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/flexibacter_canadensis_medium__71301e54.yaml
- Started UTC: 2026-09-23T03:32:29Z
- Finished UTC: 2026-09-23T03:33:04Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:005074` / `flexibacter_canadensis_medium`, the KOMODO Medium 357 record that explicitly cites DSMZ Medium 357.
- Confirmed that this generated record merged `data/normalized_yaml/bacterial/KOMODO_357_FLEXIBACTER_CANADENSIS_medium.yaml` with the DSMZ 357 parent source.
- Cross-checked the generated record against the DSMZ 357 PDF and the MediaDive REST payload for DSMZ medium 357.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; 0 total ERROR rows in `/private/tmp/flexibacter_canadensis_medium_71301e54.strict.tsv`.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The KOMODO identity is coherent: `komodo.medium:357` and the record notes both say this is DSMZ Medium 357.
- The generated file is stale relative to the DSMZ parent's normalized topology: `data/normalized_yaml/bacterial/flexibacter_canadensis_medium.yaml` now lists the KOMODO source as a `variant_children` source duplicate.
- KNO3 still has a legacy `mediaingredientmech_term` identifier rather than an id-safe CHEBI mirror.
- Sodium glycerophosphate is ungrounded.
- Casamino acids is an ungrounded undefined complex ingredient; that is acceptable.

## Evidence

- DSMZ 357 and MediaDive 357 both assert pH 7.5 and a solid agar main recipe containing MgSO4 x 7 H2O, KNO3, CaCl2 x 2 H2O, Sodium glycerophosphate, a 1 ml/L Trace element solution SL-10 addition, Tris, Thiamine-HCl x 2 H2O, Casamino acids, Glucose, Vitamin B12, Agar, and Distilled water.
- The generated record correctly carries `SOLID_AGAR`, `ph_value: 7.5`, the DSMZ-resolved main-recipe vitamins, and the agar row.
- The generated record has no `solutions` array, so the 1 ml/L Trace element solution SL-10 addition is absent.
- DSMZ SL-10 stock rows are present as top-level final ingredients instead: HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O.

## Completeness

- Ingredient rows from the main DSMZ recipe are complete and numerically correct.
- The main pH value is present, but the source pH-adjustment preparation instruction is absent.
- The SL-10 stock addition is not represented; instead, its stock formula is flattened.

## Findings

- Needs curation: the 1 ml/L Trace element solution SL-10 addition from DSMZ 357 is absent.
- Needs curation: SL-10 stock components are incorrectly exposed as final-medium top-level ingredients at stock strength.
- Needs curation: the generated merge predates the current normalized source-duplicate topology and still carries the older two-source merge metadata.
- Needs curation: KNO3 still uses a legacy MediaIngredientMech ID, and Sodium glycerophosphate needs a small-molecule grounding pass.
- Minor issue: the KOMODO import's first embedded curation-history timestamp is malformed as `2026-01-27T01:15:02.fZ`.

## Recommended Edits

- Repair the DSMZ 357 source and KOMODO 357 duplicate by restoring a 1 `ML_PER_L` Trace element solution SL-10 addition and removing the SL-10 stock contents from final top-level `ingredients`.
- Add a preparation step that preserves the DSMZ pH-adjustment instruction.
- Regenerate `data/merge_yaml/merged/flexibacter_canadensis_medium__71301e54.yaml` from the current normalized topology so the KOMODO exact duplicate remains attached through the DSMZ parent's `variant_children` relationship.
- Replace the legacy KNO3 MediaIngredientMech mirror with an id-safe CHEBI mirror and ground Sodium glycerophosphate if a precise local mapping exists.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated KOMODO 357 YAML.
- Confirm the regenerated record has a 1 `ML_PER_L` SL-10 solution and no top-level SL-10-only HCl or trace-metal ingredient rows.
- Confirm `ph_value: 7.5`, `physical_state: SOLID_AGAR`, Thiamine-HCl x 2 H2O at 0.001 `G_PER_L`, Vitamin B12 at 0.000001 `G_PER_L`, and Agar at 10 `G_PER_L` are preserved.
- Confirm embedded curation-history timestamps are parseable after regeneration.

## Additional Notes

- This record has the same DSMZ 357 stock-boundary defect as the DSMZ parent, but not the microgram/milligram unit inflation found in the TOGO M2591 split.

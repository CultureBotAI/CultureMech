# YAML Record Review: fervidobacterium_tf_a_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/fervidobacterium_tf_a_medium.yaml
- Started UTC: 2026-09-23T03:19:32Z
- Finished UTC: 2026-09-23T03:20:34Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:001876` / `fervidobacterium_tf_a_medium`, the DSMZ 740 import for FERVIDOBACTERIUM TF(A) MEDIUM.
- Cross-checked the generated record against the DSMZ Medium 740 PDF and the MediaDive REST payload for medium 740.
- Compared the generated merge with its normalized source at `data/normalized_yaml/bacterial/fervidobacterium_tf_a_medium.yaml`.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; 0 total ERROR rows in `/private/tmp/fervidobacterium_tf_a_medium.strict.tsv`.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The core DSMZ 740 identity is coherent: the medium term is `mediadive.medium:740`, the label matches DSMZ/MediaDive, and the source note links to DSMZ Medium 740.
- The generated file is stale relative to the normalized source's 2026-09-13 `RESOLVED_KOMODO_740_FERVIDOBACTERIUM_TOPOLOGY` repair. The normalized file now lists `tf_a_medium.yaml` and `for_dsm_17883.yaml` as `variant_children`; the generated merge still carries the older 2026-08-06 three-source merge metadata and synonym list.
- Most defined direct ingredients have appropriate CHEBI groundings.
- Yeast extract and Trypticase peptone are ungrounded complex ingredients; that is acceptable. `Calcium D-(+)-pantothenate` has a primary CHEBI term but lacks a mirrored `mediaingredientmech_chebi_term`.

## Evidence

- DSMZ 740 and MediaDive both define a main solution containing a 10 ml/L addition of Modified Wolin's mineral solution and a 1 ml/L addition of Wolin's vitamin solution (10x).
- DSMZ 740 and MediaDive both provide nested formulas for Modified Wolin's mineral solution and Wolin's vitamin solution.
- The generated file has no `solutions` array, and all Modified Wolin's mineral and Wolin's vitamin subingredients are instead present as direct top-level `ingredients`.
- The duplicate notes on MgSO4 x 7 H2O and CaCl2 x 2 H2O show that stock concentrations have been numerically added to direct final-medium concentrations.
- DSMZ 740 also defines DSM 17883 and DSM 21710 strain-specific sulfur/pH variants; those variant instructions are absent from this canonical generated recipe and should remain in dedicated variant records rather than be collapsed into the DSMZ 740 parent.

## Completeness

- The main DSMZ/MediaDive preparation instruction is present and captures anoxic sparging, autoclaving, post-autoclave addition of calcium chloride, glucose, vitamins, cysteine, and sulfide, vitamin filtration, and complete-medium pH 6.8-7.0.
- The Modified Wolin's mineral solution preparation instruction is present.
- The stock addition structure is missing, so final-medium reconstruction is incomplete despite the presence of both stock recipes.

## Findings

- Needs curation: the 10 ml/L Modified Wolin's mineral solution and 1 ml/L Wolin's vitamin solution additions are absent as solution additions.
- Needs curation: Modified Wolin's mineral components are overrepresented as final-medium ingredients at stock strength; MgSO4 x 7 H2O and CaCl2 x 2 H2O are also incorrectly merged with the direct main-recipe rows.
- Needs curation: Wolin's vitamin solution components are overrepresented as final-medium ingredients at 10x stock strength.
- Needs curation: the generated merge should be regenerated from the post-2026-09-13 normalized topology so exact KOMODO 740/740.1 entries remain under the DSMZ parent as variants instead of as old merged synonyms.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/fervidobacterium_tf_a_medium.yaml` by restoring Modified Wolin's mineral solution at 10 `ML_PER_L` and Wolin's vitamin solution (10x) at 1 `ML_PER_L`.
- Remove Modified Wolin's mineral and Wolin's vitamin subingredients from top-level final `ingredients` unless the model gains a nested stock-composition representation.
- Preserve the direct main-recipe MgSO4 x 7 H2O and CaCl2 x 2 H2O rows at their MediaDive-normalized final concentrations, without adding the stock formula amounts.
- Regenerate `data/merge_yaml/merged/fervidobacterium_tf_a_medium.yaml` so the September KOMODO topology repair and the stock-boundary correction both reach the derived record.

## Follow-up Checks

- After repair and regeneration, rerun open-schema, strict, reference, and term validation on the generated DSMZ 740 YAML.
- Confirm the regenerated record includes two solution additions and no top-level Biotin, Folic acid, trace-metal stock, or stock-only mineral rows from the nested solutions.
- Confirm MgSO4 x 7 H2O and CaCl2 x 2 H2O no longer carry duplicate-merge notes.
- Confirm `tf_a_medium` and `for_dsm_17883` are represented through `variant_children`, not by the old generated synonym merge.

## Additional Notes

- The generated file is derived data. Apply the stock restoration to `data/normalized_yaml/bacterial/fervidobacterium_tf_a_medium.yaml` or to the MediaDive import logic, then regenerate the merge output.

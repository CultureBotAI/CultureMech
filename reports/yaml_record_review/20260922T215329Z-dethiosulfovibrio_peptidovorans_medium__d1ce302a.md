# YAML Record Review: dethiosulfovibrio_peptidovorans_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dethiosulfovibrio_peptidovorans_medium__d1ce302a.yaml`
- Started UTC: 2026-09-22T21:51:52Z
- Finished UTC: 2026-09-22T21:53:29Z
- Verdict: needs curation

## Target

`CultureMech:006487` represents KOMODO Medium 786 merged with the DSMZ Medium 786 MediaDive import for `DETHIOSULFOVIBRIO PEPTIDOVORANS MEDIUM`. The generated record merged `data/normalized_yaml/bacterial/KOMODO_786_DETHIOSULFOVIBRIO_PEPTIDOVORANS_medium.yaml` and `data/normalized_yaml/bacterial/dethiosulfovibrio_peptidovorans_medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

DSMZ Medium 786 is different from TOGO M784/JCM 759 even though both normalize to `dethiosulfovibrio_peptidovorans_medium`. A gitignore-independent, case-insensitive `find` over `data/` found both generated fingerprints and the TOGO, KOMODO, JCM, and DSMZ normalized views, so this DSMZ/KOMODO merge should be repaired as its own variant.

## Evidence

- MediaDive DSMZ 786 defines `Main sol. 786` as a 1010 ml recipe with base salts, yeast extract, Trypticase peptone, NaCl, 10 ml Modified Wolin's mineral solution, resazurin, Na2CO3, Na2S2O3, L-cysteine, Na2S, and 1000 ml distilled water.
- Modified Wolin's mineral solution is a 1000 ml stock containing nitrilotriacetic acid, MgSO4, MnSO4, NaCl, FeSO4, CoSO4, CaCl2, ZnSO4, CuSO4, AlK(SO4)2, H3BO3, Na2MoO4, NiCl2, Na2SeO3, Na2WO4, and distilled water.
- The MediaDive main preparation keeps carbonate, thiosulfate, cysteine, and sulfide out of the autoclaved base and adds those from sterile anoxic stocks after the 80% N2 / 20% CO2 sparging step.
- The sibling TOGO M784 record points to JCM 759, lists pH 7.3, and uses 900 ml water plus four different milliliter additions; it is not the same formula as DSMZ 786.

## Completeness

The record is incomplete because Modified Wolin's mineral solution was flattened into the top-level ingredient list and its water row was dropped. The main 1000 ml water row is also missing.

## Findings

- Fifteen Modified Wolin's mineral solution child ingredients were promoted to top-level final-medium ingredients even though the source adds only 10 ml of that stock to 1010 ml main medium.
- `NaCl` from the main medium and Modified Wolin's mineral solution were merged into `31.0 G_PER_L`.
- `CaCl2 x 2 H2O` from the main medium and Modified Wolin's mineral solution were merged into `0.2 G_PER_L` in the generated record.
- The 1000 ml main water and 1000 ml mineral-stock water rows are absent.
- The Modified Wolin's mineral solution pH 6.5/7.0 preparation instructions are not represented on the stock.
- The normalized MediaDive source has a September duplicate-collapse repair for CaCl2, but it still needs full stock nesting to avoid losing the mineral-solution CaCl2 row.

## Recommended Edits

- Restore Modified Wolin's mineral solution as a 1000 ml stock added at 10 ml to the DSMZ 786 main recipe.
- Move all stock-strength Wolin minerals, including NaCl, CaCl2, and stock water, under Modified Wolin's mineral solution.
- Keep main-medium NaCl and CaCl2 separate from their same-named Modified Wolin stock rows.
- Preserve the main anaerobic preparation and the Wolin pH-adjustment preparation in their proper scopes.
- Maintain the DSMZ 786/KOMODO 786 duplicate-source merge separately from the TOGO M784/JCM 759 formulation.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no Modified Wolin's mineral solution child remains as a top-level ingredient.
- Verify that no duplicate merge crosses the main-medium and mineral-stock boundary.
- Verify that DSMZ 786 and TOGO M784 still emit as distinct variants unless a source-backed relationship is added.

## Additional Notes

None found.

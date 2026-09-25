# YAML Record Review: caproiciproducens_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/caproiciproducens_medium__2ae702e9.yaml
- Started UTC: 2026-09-22T03:41:21Z
- Finished UTC: 2026-09-22T03:41:21Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002434`, `caproiciproducens_medium`, class `MediaRecipe`.
- Merge lineage: one source recipe, `caproiciproducens_medium`, on fingerprint `2ae702e9f0f8e496c9bef1356588b32b18e62d2e9f17379d30f6fda21eb72f38`.
- Maintained owner: `data/normalized_yaml/bacterial/caproiciproducens_medium.yaml`.
- Claimed source identity: JCM Medium 1268, cross-listed in MediaDive as `mediadive.medium:J1268`.

## Validation

- Open LinkML schema validation exited successfully for the generated merge.
- Strict CultureMech validation exited successfully for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The generated merge and normalized owner are materially identical: the merge only appends its `MERGED_RECIPES` event, `merge_fingerprint`, and `merged_from`.
- The record denotes MediaDive/JCM Medium J1268. The JCM 1268 live page currently labels the same recipe `CAPROICIBACTERIUM MEDIUM`, while MediaDive labels it `CAPROICIPRODUCENS MEDIUM`; the inspected formula and JCM numeric identifier still match.
- The nine dissolved base salts in the generated `ingredients` list agree with the JCM and MediaDive amounts after the 2 mg ZnSO4 x 7 H2O and 2 mg CoCl2 x 6 H2O rows are normalized to `0.002 G_PER_L`.
- All nine base salts have source-compatible primary groundings. `Yeast extract` and `Tryptone` are complex stock ingredients and are reasonably left without CHEBI groundings; the packaged ingredient output has an exact `MICRO:0000182` mapping for `Tryptone` if MICRO terms are accepted in ingredient rows.

## Evidence

- JCM Medium 1268 lists a 645 ml base solution with ammonium sulfate 2 g, K2HPO4 1 g, KH2PO4 0.5 g, FeSO4 x 7 H2O 0.015 g, MgSO4 x 7 H2O 0.1 g, variable-hydrate MnSO4 0.01 g, CaCl2 x 2 H2O 0.01 g, ZnSO4 x 7 H2O 0.002 g, and CoCl2 x 6 H2O 0.002 g.
- JCM then says to mix the base components, adjust pH to 6.5, autoclave under an N2 atmosphere, and after cooling aseptically and anaerobically add autoclaved stock solutions: 100 ml 10% Yeast extract, 100 ml 10% Tryptone, 100 ml 1.0 M Glucose, 20 ml 1.0 M Sodium acetate, and 35 ml 1.0 M sodium butyrate.
- MediaDive's J1268 JSON preserves those same rows in `Main sol. J1268` as `mediadive.solution:5409`, including `Distilled water` as 645 ml, a 1000 ml final solution volume, and the pH 6.5/N2 autoclave/post-cooling addition step.
- The JCM page also has a source comment to preheat the medium to 37 C for subculturing.

## Completeness

- The generated record is missing the source `Distilled water` row.
- The five post-cooling stock additions are encoded as ordinary `G_PER_L` ingredients. Their source values are milliliter addition volumes of 10% or 1.0 M stock solutions, not 100, 20, 100, 35, and 100 g/L mass concentrations.
- The generated preparation step keeps the source pH 6.5, N2 autoclave, and post-cooling anaerobic addition text, but it does not explicitly tie each stock addition to that post-cooling step.
- The generated record is missing JCM's 37 C preheat note for subculturing.
- Target organisms, evidence, variants, and references are empty. The inspected JCM/MediaDive source is sufficient for composition and preparation, but this record has not tried to curate strain-specific growth claims.

## Findings

- Major: the generated record omits the required 645 ml distilled-water component. JCM, MediaDive J1268, and the same-source TOGO M1364 import all include it.
- Major: the five stock solution additions have the wrong concentration semantics. The record stores their source milliliter additions as `G_PER_L` values, losing that they are 10% Yeast extract, 10% Tryptone, 1.0 M Glucose, 1.0 M Sodium acetate, and 1.0 M sodium butyrate stocks added after the base cools.
- Minor: the 37 C subculture preheat note from JCM is missing.
- Minor: `Tryptone` is ungrounded despite a unique packaged MediaIngredientMech mapping to `MICRO:0000182`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/caproiciproducens_medium.yaml`, not the generated merge.
- Add `Distilled water` as a volume-based 645 ml base-water addition.
- Remodel the five stock solution rows so their 100 ml, 100 ml, 100 ml, 20 ml, and 35 ml values are represented as post-cooling source-volume additions of 10% or 1.0 M autoclaved stocks, not as direct `G_PER_L` ingredients.
- Split or enrich the preparation steps so curators can tell which components are autoclaved in the base under N2 and which stock solutions are added aseptically and anaerobically after cooling.
- Add the JCM 37 C preheat note as structured preparation text or an explicit source note.
- Ground `Tryptone` to `MICRO:0000182` if MICRO terms are accepted in ingredient rows.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against `data/normalized_yaml/bacterial/caproiciproducens_medium.yaml`.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/caproiciproducens_medium__2ae702e9.yaml`.
- Inspect the regenerated merge to confirm it has volume-based 645 ml water, semantically correct stock-solution additions, the 37 C note, and the intended Tryptone grounding state.
- Re-check the JCM Medium 1268 page and MediaDive J1268 JSON export to confirm the maintained owner still matches the source formula and comments.

## Additional Notes

- `rg --no-ignore --hidden -l` for `CultureMech:002434`, `mediadive.medium:J1268`, `caproiciproducens_medium__2ae702e9`, and `CAPROICIPRODUCENS MEDIUM` included ignored and hidden files; it found one active normalized owner, one generated merge, generated indexes/catalogs, archived validation reports, ingredient audit output, and unrelated downstream app/report artifacts, but no second active normalized owner for `mediadive.medium:J1268`.
- This record and `TOGO_M1364_Caproiciproducens_Medium` both resolve to JCM Medium 1268, but they are not duplicates until the MediaDive and Togo representations preserve water and the five stock solution additions in the same shape.

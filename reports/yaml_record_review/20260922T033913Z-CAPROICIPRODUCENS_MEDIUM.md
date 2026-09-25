# YAML Record Review: caproiciproducens_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml
- Started UTC: 2026-09-22T03:39:13Z
- Finished UTC: 2026-09-22T03:39:13Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:007902`, `caproiciproducens_medium`, class `MediaRecipe`.
- Merge lineage: one source recipe, `TOGO_M1364_Caproiciproducens_Medium`, on fingerprint `18e87c62c4614283e3a1dc83c5fedba8b91fa60f3502c50b4c7d5bcc8908d96b`.
- Maintained owner: `data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml`.
- Claimed source identity: Togo Medium `M1364`, imported from JCM Medium 1268.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation exited successfully for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The generated merge and normalized owner are materially identical: the merge only appends its `MERGED_RECIPES` event, `merge_fingerprint`, and `merged_from`.
- The record denotes Togo Medium M1364, which the Togo API identifies as an extraction from JCM Medium 1268.
- The JCM 1268 live page currently labels the same recipe `CAPROICIBACTERIUM MEDIUM`, while Togo and MediaDive J1268 label it as Caproiciproducens/CAPROICIPRODUCENS medium; the inspected formula and JCM numeric identifier still match.
- The nine dissolved base salts in the generated `ingredients` list agree with the JCM, Togo, and MediaDive amounts after 2 mg ZnSO4 x 7 H2O and 2 mg CoCl2 x 6 H2O are normalized to `0.002 G_PER_L`.
- `MnSO4 x H2O` is reasonably ungrounded because the source deliberately leaves the hydration state variable. The other grounded base salts are source-compatible except `CoCl2 x 6 H2O`, whose primary term is generic/anhydrous cobalt dichloride rather than the explicitly labelled hexahydrate.

## Evidence

- JCM Medium 1268 lists a 645 ml base solution with ammonium sulfate 2 g, K2HPO4 1 g, KH2PO4 0.5 g, FeSO4 x 7 H2O 0.015 g, MgSO4 x 7 H2O 0.1 g, variable-hydrate MnSO4 0.01 g, CaCl2 x 2 H2O 0.01 g, ZnSO4 x 7 H2O 0.002 g, and CoCl2 x 6 H2O 0.002 g.
- JCM then says to mix the base components, adjust pH to 6.5, autoclave under an N2 atmosphere, and after cooling aseptically and anaerobically add autoclaved stock solutions: 100 ml 10% Yeast extract, 100 ml 10% Tryptone, 100 ml 1.0 M Glucose, 20 ml 1.0 M Sodium acetate, and 35 ml 1.0 M sodium butyrate.
- The JCM addition volumes sum with 645 ml base water to 1000 ml final volume, which is also the final volume in the MediaDive J1268 JSON `Main sol. J1268`.
- The Togo M1364 API preserves the same two subcomponents and comments, including the pH 6.5 anaerobic autoclave instruction and the 37 C preheat note for subculturing.

## Completeness

- The generated record is missing `ph_value: 6.5` even though the JCM and Togo source comments declare the pH and MediaDive models it in structured metadata.
- The generated record is missing the source instruction to autoclave the base medium under N2, add the five autoclaved stock solutions aseptically and anaerobically after cooling, and preheat subculture medium to 37 C.
- `Distilled water` is encoded as `645 G_PER_L`, which is a solid mass concentration, not the source 645 ml base-solution volume.
- `N2` is encoded as a variable ingredient, but the source mentions it only as the autoclave atmosphere for the base solution.
- The five stock solution additions are empty `solutions` entries named `Unknown solution`; their `concentration` values conflate source addition volumes with stock concentrations and do not preserve that 100 ml, 20 ml, 100 ml, 35 ml, and 100 ml are the volumes to add after cooling.
- `FeSO4 x 7 H2O` and `CoCl2 x 6 H2O` have correct source amounts but no CHEBI-keyed MediaIngredientMech mirror, and the latter also needs a primary term for cobalt dichloride hexahydrate.

## Findings

- Major: all five post-autoclave stock solution additions lost their composition and volume semantics. The generated `solutions` array contains empty `composition: []` entries and stores `100`, `20`, `100`, `35`, and `100` as `G_PER_L` concentrations rather than as milliliter additions of 10% or 1.0 M stock solutions.
- Major: the source preparation procedure is absent. The generated record has no pH 6.5 value, no base-medium autoclaving under N2, no aseptic anaerobic addition of the five autoclaved stock solutions after cooling, and no 37 C preheat note.
- Major: the base water row uses the wrong unit. JCM, Togo, and MediaDive give 645 ml distilled water, while the normalized owner and generated merge store `645 G_PER_L`.
- Minor: `N2` should be represented as an autoclave-atmosphere condition, not as a variable recipe ingredient.
- Minor: `CoCl2 x 6 H2O` is grounded to a generic/anhydrous cobalt dichloride primary term even though Togo labels the source component as cobalt dichloride hexahydrate.
- Minor: `FeSO4 x 7 H2O` and `CoCl2 x 6 H2O` are missing CHEBI-keyed `mediaingredientmech_chebi_term` mirrors.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml`, not the generated merge.
- Change `Distilled water` from `645 G_PER_L` to a volume-based 645 ml base-water addition.
- Move `N2` out of `ingredients` and into a preparation step that preserves the source autoclave atmosphere.
- Add `ph_value: 6.5` and structured preparation steps for the JCM pH adjustment, N2 autoclave, post-cooling aseptic anaerobic stock additions, and 37 C preheat note.
- Preserve the five stock solution additions as source-volume additions, not empty solution shells with `Unknown solution` names.
- Ground `CoCl2 x 6 H2O` to a cobalt dichloride hexahydrate primary term while keeping the 0.002 g/L amount, and add CHEBI-keyed MIM mirrors for both `FeSO4 x 7 H2O` and `CoCl2 x 6 H2O` if those mirrors are accepted for these source labels.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against `data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml`.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml`.
- Inspect the regenerated merge to confirm it has volume-based 645 ml water, pH 6.5, no recipe-row `N2`, non-empty/semantically correct stock-solution additions, and the expected anaerobic autoclave and post-cooling preparation steps.
- Re-check the Togo M1364 API, JCM Medium 1268 page, and MediaDive J1268 JSON export to confirm the maintained owner still matches the source formula and comments.

## Additional Notes

- `rg --no-ignore --hidden -l` for `CultureMech:007902`, `TOGO:M1364`, `TOGO_M1364_Caproiciproducens_Medium`, `CAPROICIPRODUCENS_MEDIUM`, and `Caproiciproducens` included ignored and hidden files; it found one active normalized owner, one generated merge, generated indexes/catalogs, archived validation reports, ingredient audit output, and unrelated downstream app/report artifacts, but no second active normalized owner for Togo M1364.
- The source water and stock-addition volumes intentionally total 1000 ml, so the 645 ml water row is not a missing final-volume water row; it is the base solution volume before the five autoclaved stock solutions are added.

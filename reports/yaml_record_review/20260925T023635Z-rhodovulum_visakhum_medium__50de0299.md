# YAML Record Review: rhodovulum_visakhum_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/rhodovulum_visakhum_medium__50de0299.yaml
- Started UTC: 2026-09-25T02:34:00Z
- Finished UTC: 2026-09-25T02:36:34Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record:

- Path: `data/merge_yaml/merged/rhodovulum_visakhum_medium__50de0299.yaml`
- ID: `CultureMech:003832`
- Label: `rhodovulum_visakhum_medium`
- Source identity: KOMODO Medium 1128 / DSMZ Medium 1128
- Source CURIEs: `komodo.medium:1128`, `mediadive.medium:1128`
- Generated from:
  - `data/normalized_yaml/bacterial/KOMODO_1128_RHODOVULUM_VISAKHUM_medium.yaml`
  - `data/normalized_yaml/bacterial/rhodovulum_visakhum_medium.yaml`

The target is a generated duplicate merge. Future fixes belong in normalized
source records or in merge/import logic, followed by regeneration of
`data/merge_yaml/merged/`.

## Validation

| Check | Result |
| --- | --- |
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/rhodovulum_visakhum_medium__50de0299.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/rhodovulum_visakhum_medium__50de0299.yaml --out /private/tmp/rhodovulum_visakhum_medium__50de0299.strict.tsv --workers 1 --quiet` | Passed; 0 error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/rhodovulum_visakhum_medium__50de0299.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were present. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/rhodovulum_visakhum_medium__50de0299.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: `just validate-history` validates standalone `history/` records, not embedded `MediaRecipe.curation_history` entries. |

## Identity and Grounding

- The record ID, normalized label, bacterial category, liquid physical state,
  pH 6.8, KOMODO 1128 source identity, and DSMZ 1128 cross-reference are
  internally aligned.
- DSMZ Medium 1128 resolves through both the MediaDive REST API and the DSMZ
  PDF as `RHODOVULUM VISAKHUM MEDIUM`.
- The target's `SOURCE_DUPLICATE` link to
  `data/normalized_yaml/bacterial/rhodovulum_visakhum_medium.yaml` is
  conceptually valid: the KOMODO owner says it copied DSMZ Medium 1128 and
  uses the same medium number.
- The `MgCl2 x 7 H2O` ingredient is not safely grounded. The target maps this
  hydrated source label to `CHEBI:6636` / magnesium dichloride, which does not
  preserve the source hydration.
- The JCM J515 / TOGO M516 same-name siblings are not exact source duplicates
  of this DSMZ/KOMODO target: JCM adds sorbitol, uses MgCl2 x 6 H2O instead
  of DSMZ's MgCl2 x 7 H2O, and refers to a Trace element solution SL8 stock
  by a JCM medium number.
- The exact ignored-inclusive source search covered `data` and `src` YAML and
  Python files for `komodo.medium:1128`, `mediadive.medium:1128`,
  `KOMODO_1128_RHODOVULUM_VISAKHUM_medium`, `DSMZ Medium: 1128`,
  `JCM_J515_RHODOVULUM_VISAKHUM_MEDIUM`,
  `TOGO_M516_Rhodovulum_Visakhum_Medium`, `TOGO:M516`,
  `mediadive.medium:J515`, and `JCM_M515`. It found the four normalized
  source owners, three generated same-name records, and
  `data/metal_ree_analysis.yaml`.

## Evidence

- DSMZ Medium 1128 supports KH2PO4 0.50 g/L, MgCl2 x 7 H2O 1.00 g/L, NaCl
  20.00 g/L, NH4Cl 0.60 g/L, CaCl2 x 2 H2O 0.15 g/L, and yeast extract
  0.40 g/L as pre-autoclave main-medium ingredients.
- DSMZ Medium 1128 supports `Micronutrient solution SL8` at 1.00 ml/L, not
  direct final-medium rows of Na2-EDTA, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O,
  H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and
  Na2MoO4 x 2 H2O at their stock concentrations.
- DSMZ Medium 1128 supports `Distilled water` at 1000.00 ml in the final
  medium and at 1000.0 ml in the SL8 stock. The target omits both water
  boundaries.
- DSMZ Medium 1128 supports adding sodium pyruvate at 3.0 g/L after
  autoclaving from a sterile stock. The target preserves the amount but loses
  the post-autoclave scope.
- DSMZ Medium 1128 supports adding Vitamin B12 as 1.0 ml/L of a 2 mg/L
  filter-sterilized stock after autoclaving. The target instead encodes
  `Vitamin B12` as `1 G_PER_L`.
- DSMZ Medium 1128 supports main-medium pH adjustment to 6.8, nitrogen
  bubbling and N2-filled rubber-septum tubes, and SL8 stock adjustment to
  pH 6.5. None of these steps survive in the generated target.

## Completeness

- The generated target is missing two solution boundaries: SL8 at 1 ml/L and
  Vitamin B12 stock at 1 ml/L.
- The generated target is missing final-water and stock-water rows.
- The generated target is missing all DSMZ preparation context, including N2
  handling and the post-autoclave addition boundary.
- The generated target has no target-organism, growth-metric, reference, or
  evidence blocks. These are optional in the schema and the DSMZ/KOMODO source
  recipe does not by itself establish a specific growth outcome.

## Findings

### Major

1. **The SL8 micronutrient stock is flattened into the final medium.**
   DSMZ 1128 adds `Micronutrient solution SL8` at 1 ml/L and defines the
   listed metal salts inside a separate 1000 ml stock. The target lists those
   stock ingredients directly in the final medium at stock `G_PER_L` values,
   multiplying their final concentrations by 1000 and erasing the stock
   boundary. Future fixes belong in
   `data/normalized_yaml/bacterial/rhodovulum_visakhum_medium.yaml` and
   `data/normalized_yaml/bacterial/KOMODO_1128_RHODOVULUM_VISAKHUM_medium.yaml`,
   or in the DSMZ resolver that copied flattened DSMZ rows into the KOMODO
   owner.

2. **The post-autoclave Vitamin B12 stock was converted to 1 g/L Vitamin B12.**
   The DSMZ source adds 1 ml/L of a 2 mg/L Vitamin B12 stock after autoclaving,
   while the target says `Vitamin B12` concentration is `1 G_PER_L`. That is
   a stock-volume row imported as a mass concentration and it materially
   changes the formulation.

3. **Source water rows are omitted.**
   The target has neither the 1000 ml final-medium water nor the 1000 ml SL8
   stock water from DSMZ 1128, making both final volume and stock volume
   unrecoverable.

4. **The generated merge drops DSMZ preparation instructions.**
   The direct DSMZ owner records the source pH, N2 bubbling / N2-filled
   septum tubes, post-autoclave addition cue, and SL8 pH 6.5 text, but the
   generated merge inherits the KOMODO owner, which lacks
   `preparation_steps`. If the two normalized owners remain in the same
   `SOURCE_DUPLICATE` group, the KOMODO owner needs the DSMZ preparation
   context or `src/culturemech/merge/merger.py` needs a tie-break or field
   merge that preserves source preparation when exact duplicate owners merge.

5. **The DSMZ magnesium chloride hydrate is over-grounded to anhydrous
   magnesium chloride.**
   The DSMZ source and target ingredient string are `MgCl2 x 7 H2O`, but the
   target grounds it to `CHEBI:6636`, magnesium dichloride. Hydration is
   identity-significant in this corpus; if no exact seven-hydrate term exists,
   the source label should remain explicitly unresolved rather than mapped to
   the anhydrous salt.

## Recommended Edits

1. Repair the DSMZ owner,
   `data/normalized_yaml/bacterial/rhodovulum_visakhum_medium.yaml`, so the
   main medium, `Micronutrient solution SL8`, Vitamin B12 stock, final water,
   stock water, and preparation steps match DSMZ Medium 1128 without stock
   flattening.
2. Repair the KOMODO duplicate owner,
   `data/normalized_yaml/bacterial/KOMODO_1128_RHODOVULUM_VISAKHUM_medium.yaml`,
   or the DSMZ resolver that populated it, so copied DSMZ Medium 1128 content
   preserves nested solutions and preparation context.
3. De-ground or exactly resolve `MgCl2 x 7 H2O`; do not keep the anhydrous
   `CHEBI:6636` link on a hydrated source label.
4. Rerun the merge generation and verify that the regenerated DSMZ/KOMODO
   generated target has seven pre-autoclave final ingredients, two solution
   additions, explicit water rows, pH 6.8, pH 6.5 for the SL8 stock, and the
   N2 handling instructions.
5. Keep the JCM J515 / TOGO M516 generated siblings separate from this
   DSMZ/KOMODO record unless a later review proves their 6-hydrate, sorbitol,
   and stock-source differences are source artifacts.

## Follow-up Checks

- `just validate data/normalized_yaml/bacterial/rhodovulum_visakhum_medium.yaml`
- `just validate data/normalized_yaml/bacterial/KOMODO_1128_RHODOVULUM_VISAKHUM_medium.yaml`
- `just validate-terms data/normalized_yaml/bacterial/rhodovulum_visakhum_medium.yaml`
- The focused open-schema, strict, reference, and term validators used in this
  review against the regenerated generated target.
- A manual diff of the regenerated target against the DSMZ Medium 1128 PDF or
  REST payload, specifically checking that SL8 and Vitamin B12 remain stock
  additions and are not flattened into final grams per liter.
- An exact ignored-inclusive source search for DSMZ 1128, KOMODO 1128, JCM
  J515, and TOGO M516 before adding or rejecting cross-source duplicate links.

## Additional Notes

- A slug ignored-inclusive search over `data/normalized_yaml` and
  `data/merge_yaml/merged` found three generated same-name records:
  this DSMZ/KOMODO target, `RHODOVULUM_VISAKHUM_MEDIUM.yaml`, and
  `rhodovulum_visakhum_medium__69bd8d39.yaml`. It also found the four
  normalized owners for KOMODO 1128, DSMZ 1128, JCM J515, and TOGO M516.
- The live JCM `GRMD=515` page was available at review time and confirmed that
  the JCM sibling is a distinct same-name formula with MgCl2 x 6 H2O,
  sorbitol, 1 ml Vitamin B12 stock, and a 1 ml Trace element solution SL8
  stock referencing JCM Medium 190.

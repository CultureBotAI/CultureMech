# YAML Record Review: roseibaca_calidilacus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/roseibaca_calidilacus_medium__a1a63bdc.yaml
- Started UTC: 2026-09-25T02:38:06Z
- Finished UTC: 2026-09-25T02:40:18Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record:

- Path: `data/merge_yaml/merged/roseibaca_calidilacus_medium__a1a63bdc.yaml`
- ID: `CultureMech:002310`
- Label: `roseibaca_calidilacus_medium`
- Source identity: JCM Medium J1137 / MediaDive `J1137`
- Source CURIE: `mediadive.medium:J1137`
- Generated from:
  - `data/normalized_yaml/bacterial/roseibaca_calidilacus_medium.yaml`

The target is a generated singleton merge. Future fixes belong in the
normalized MediaDive/JCM owner or in MediaDive nested-solution import logic,
followed by regeneration of `data/merge_yaml/merged/`.

## Validation

| Check | Result |
| --- | --- |
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/roseibaca_calidilacus_medium__a1a63bdc.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/roseibaca_calidilacus_medium__a1a63bdc.yaml --out /private/tmp/roseibaca_calidilacus_medium__a1a63bdc.strict.tsv --workers 1 --quiet` | Passed; 0 error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/roseibaca_calidilacus_medium__a1a63bdc.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were present. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/roseibaca_calidilacus_medium__a1a63bdc.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: `just validate-history` validates standalone `history/` records, not embedded `MediaRecipe.curation_history` entries. |

## Identity and Grounding

- The record ID, normalized label, bacterial category, defined-medium
  classification, and JCM J1137 / MediaDive source identity are internally
  aligned.
- MediaDive J1137 resolves to `ROSEIBACA CALIDILACUS MEDIUM`, source JCM.
  The live JCM `GRMD=1137` page was inspected on 2026-09-25 and returned
  `Nothing found`, so MediaDive J1137 and TOGO M1217 are the usable
  secondary captures of the JCM recipe.
- TOGO M1217 records original source `JCM_M1137` and the same JCM URL. It is
  a same-source duplicate imported through a different parser, but it
  generated separately as `ROSEIBACA_CALIDILACUS_MEDIUM.yaml`.
- The exact source-ID ignored-inclusive search covered `data` and `src` YAML
  and Python files for `mediadive.medium:J1137`, `TOGO:M1217`,
  `JCM_J1137_ROSEIBACA_CALIDILACUS_MEDIUM`,
  `TOGO_M1217_Roseibaca_Calidilacus_Medium`, `JCM_M1137`, and `GRMD=1137`.
  It found the MediaDive/JCM owner and target, the TOGO owner and target, and
  `data/metal_ree_analysis.yaml`.

## Evidence

- MediaDive J1137 supports a final liter that contains 200 ml `5 x Salts
  solution`, 0.84 g NaHCO3, 0.46 g glycerol, 0.03 g KH2PO4, 0.02 g Na2CO3,
  1.42 mg ammonium ferric citrate, 10 ml `100 x BG-FPC solution`, 10 ml of
  1 M TES pH 8.0, 10 ml `Trace vitamins`, and 770 ml distilled water.
- MediaDive J1137 supports `5 x Salts solution` as its own stock: 493 g
  MgSO4 x 7 H2O, 57 g Na2SO4, and 7.5 g KCl brought to 1 L.
- MediaDive J1137 supports `100 x BG-FPC solution` as its own stock: NaNO3,
  MgSO4 x 7 H2O, CaCl2 x 2 H2O, Na2-EDTA, 100 ml of `Trace element
  solution`, and 900 ml distilled water.
- MediaDive J1137 supports `Trace element solution` and `Trace vitamins` as
  separate 1 L stocks. The generated target instead lists all trace metals
  and vitamins directly in the final medium at stock concentrations.
- The generated target sums MgSO4 x 7 H2O from the 5x salts stock and the
  100x BG-FPC stock into one `500.49 G_PER_L` row. The source has 493 g/L in
  5x salts and 7.49 g/L in BG-FPC; they are not duplicate final rows.
- The two MediaDive preparation steps are scoped to different solution
  boundaries: the final mixture is filter-sterilized, while the `5 x Salts
  solution` is brought to 1 L with distilled water. The target keeps both as
  top-level `preparation_steps`, detached from their stock context.

## Completeness

- The generated target lacks all five solution boundaries: 5x salts, 100x
  BG-FPC, Trace element solution, Trace vitamins, and 1 M TES buffer.
- The generated target lacks final-medium and stock water rows.
- The generated target lacks duplicate metadata linking the same JCM source as
  TOGO M1217.
- The generated target has no target-organism, growth-metric, reference, or
  evidence blocks. These are optional in the schema and the JCM/MediaDive
  source recipe does not by itself establish a specific growth outcome.

## Findings

### Major

1. **Nested JCM stock recipes were flattened into one final ingredient list.**
   The source final liter contains 200 ml of 5x salts, 10 ml of 100x BG-FPC,
   10 ml of 1 M TES pH 8.0, 10 ml of trace vitamins, and 770 ml water. The
   target has no `solutions` entries and instead emits the stock salts,
   trace metals, and vitamins as if each were a final-medium ingredient.
   Future fixes belong in
   `data/normalized_yaml/bacterial/roseibaca_calidilacus_medium.yaml` or in
   `src/culturemech/import/mediadive_importer.py`.

2. **MgSO4 x 7 H2O from two different stocks was summed into one row.**
   The target records `500.49 G_PER_L` with a note that 493.0 and 7.49 were
   merged. Those values are from two separate source stocks with different
   dilution factors, not duplicate rows in the same solution, so summing them
   creates an unsupported formulation.

3. **Water rows from three source boundaries were dropped.**
   MediaDive J1137 has 770 ml distilled water in the final medium, 900 ml in
   100x BG-FPC, and 1000 ml in the Trace element and Trace vitamins stocks.
   The target omits every water row and therefore loses the volume context
   that defines each stock.

4. **Stock-level preparation steps are attached to the parent medium.**
   `Add components to distilled water and bring volume to 1.0 L` belongs to
   the 5x salts stock, not to the final JCM medium. Flattening stock steps
   into top-level `preparation_steps` leaves a misleading protocol.

5. **The TOGO/Mediadive duplicate set is split.**
   TOGO M1217 and MediaDive J1137 capture the same JCM `GRMD=1137` recipe,
   but TOGO generated a separate record because it kept five empty
   `Unknown solution` placeholders while MediaDive flattened the same stocks
   into direct ingredients. Both owners need to be repaired to the same
   nested source structure and then linked as `SOURCE_DUPLICATE`.

### Minor

1. **`NaNO3` still carries a legacy MediaIngredientMech identifier.**
   The row already has `term: CHEBI:63005`, but the ingredient-specific
   mapping uses `mediaingredientmech_term: MediaIngredientMech:000171`
   instead of `mediaingredientmech_chebi_term`.

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/roseibaca_calidilacus_medium.yaml`
   so the final medium and four nested reusable stocks match MediaDive J1137
   instead of one flat ingredient list.
2. Preserve `5 x Salts solution`, `100 x BG-FPC solution`, `Trace element
   solution`, `Trace vitamins`, 1 M TES pH 8.0, and all water volumes as
   solution rows or linked solution records with the source ml/L dilutions.
3. Remove the summed `MgSO4 x 7 H2O` row and keep the 493 g/L and 7.49 g/L
   rows scoped to their respective stocks.
4. Keep stock preparation steps attached to their stocks instead of emitting
   every nested step at top level.
5. Repair `data/normalized_yaml/bacterial/TOGO_M1217_Roseibaca_Calidilacus_Medium.yaml`
   to the same JCM structure, then add reciprocal `SOURCE_DUPLICATE` metadata
   between the TOGO and MediaDive owners.

## Follow-up Checks

- `just validate data/normalized_yaml/bacterial/roseibaca_calidilacus_medium.yaml`
- `just validate data/normalized_yaml/bacterial/TOGO_M1217_Roseibaca_Calidilacus_Medium.yaml`
- The focused open-schema, strict, reference, and term validators used in this
  review against the regenerated generated target.
- A manual comparison of the repaired JCM owner against the inspected MediaDive
  J1137 payload, specifically checking that MgSO4 remains split by solution
  and that five stock additions remain nested.
- An exact ignored-inclusive search for `mediadive.medium:J1137`,
  `TOGO:M1217`, `JCM_M1137`, and both owner stems before adding duplicate
  links.

## Additional Notes

- The TOGO M1217 owner shows the same source structure from another import
  route: 770 ml final water, 200 ml 5x salts, 10 ml 100x BG-FPC, 10 ml TES,
  10 ml Trace vitamins, and a 100 ml nested Trace element solution inside
  BG-FPC. Its current normalized record has already merged four water rows
  into `1672.0 G_PER_L` and should not be copied into the MediaDive owner.

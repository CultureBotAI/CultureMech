# YAML Record Review: rhodovulum_kholense_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/rhodovulum_kholense_medium__b03507f6.yaml
- Started UTC: 2026-09-25T02:31:06Z
- Finished UTC: 2026-09-25T02:31:51Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record:

- Path: `data/merge_yaml/merged/rhodovulum_kholense_medium__b03507f6.yaml`
- ID: `CultureMech:003845`
- Label: `rhodovulum_kholense_medium`
- Source identity: KOMODO Medium 1136 / DSMZ Medium 1136
- Source CURIEs: `komodo.medium:1136`, `mediadive.medium:1136`
- Generated from:
  - `data/normalized_yaml/bacterial/KOMODO_1136_RHODOVULUM_KHOLENSE_medium.yaml`
  - `data/normalized_yaml/bacterial/rhodovulum_kholense_medium.yaml`

The target is a generated duplicate merge. Future fixes belong in normalized
source records or in merge/import logic, followed by regeneration of
`data/merge_yaml/merged/`.

## Validation

| Check | Result |
| --- | --- |
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/rhodovulum_kholense_medium__b03507f6.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/rhodovulum_kholense_medium__b03507f6.yaml --out /private/tmp/rhodovulum_kholense_medium__b03507f6.strict.tsv --workers 1 --quiet` | Passed; 0 error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/rhodovulum_kholense_medium__b03507f6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were present. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/rhodovulum_kholense_medium__b03507f6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: `just validate-history` validates standalone `history/` records, not embedded `MediaRecipe.curation_history` entries. |

## Identity and Grounding

- The record ID, normalized label, bacterial category, liquid physical state,
  complex/undefined medium classification, KOMODO 1136 source identity, and
  DSMZ 1136 cross-reference are internally aligned.
- DSMZ Medium 1136 resolves through both the MediaDive REST API and the DSMZ
  PDF as `RHODOVULUM KHOLENSE MEDIUM`.
- The target's `SOURCE_DUPLICATE` link to
  `data/normalized_yaml/bacterial/rhodovulum_kholense_medium.yaml` is
  conceptually valid: the KOMODO owner says it copied DSMZ Medium 1136 and
  uses the same medium number.
- The exact source-ID ignored-inclusive search covered `data` and `src` YAML
  and Python files for `komodo.medium:1136`, `mediadive.medium:1136`,
  `KOMODO_1136_RHODOVULUM_KHOLENSE_medium`, and `DSMZ Medium: 1136`. It found
  the KOMODO owner, the DSMZ owner, this generated target, and
  `data/metal_ree_analysis.yaml`.
- The exact JCM/TOGO ignored-inclusive search covered `data` and `src` YAML
  and Python files for `JCM_J649_RHODOVULUM_KHOLENSE_MEDIUM`,
  `TOGO_M664_Rhodovulum_Kholense_Medium`, `JCM_M649`,
  `togomedium:664`, and `jcm.medium:649`. It found separate JCM and TOGO
  normalized owners plus separate generated siblings; no exact JCM/TOGO
  duplicate is linked to this DSMZ/KOMODO generated target.

## Evidence

- DSMZ Medium 1136 supports the seven base final-medium ingredients in the
  target: KH2PO4 0.50 g/L, CaCl2 x 2 H2O 0.12 g/L, MgSO4 x 7 H2O 2.00 g/L,
  NH4Cl 0.64 g/L, NaCl 20.00 g/L, yeast extract 0.50 g/L, and sodium pyruvate
  3.00 g/L.
- DSMZ Medium 1136 does not support adding Na2-EDTA, FeSO4 x 7 H2O, ZnCl2,
  MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and
  Na2MoO4 x 2 H2O directly to the final liter at their stock concentrations.
  The DSMZ PDF and MediaDive REST payload both put these rows under
  `Trace element solution SL-12`, a separate 1000 ml stock, and the final
  medium receives 1 ml of that stock.
- DSMZ Medium 1136 supports a final-medium `Distilled water` row of
  1000.00 ml and the target omits it.
- DSMZ Medium 1136 supports two preparation instructions that the generated
  target omits: adjust to pH 7.0, then bubble the medium with N2 and fill
  10 ml portions in 15 ml rubber-septum tubes under N2.
- The pH 7.0 claim is supported by DSMZ Medium 1136.
- The inspected TOGO M664 payload points to JCM `GRMD=649` and represents a
  JCM sibling with 1000 ml distilled water plus a cross-reference to
  `Trace element solution SL--12 (see Medium [M497])`; MediaDive's JCM J649
  REST payload represents that stock as 1 ml `micronutrient solution` with
  the attribute `SL12) (see Medium No. 497`. That source boundary differs
  from the self-contained DSMZ 1136 stock, so the JCM/TOGO siblings need their
  own review before any cross-source duplicate relation can be asserted.
- The live JCM `GRMD=649` page was inspected on 2026-09-25 and returned
  `Nothing found`; MediaDive J649 and TOGO M664 remained usable secondary
  captures of the JCM formulation.

## Completeness

- The generated target is missing the explicit `Trace element solution SL-12`
  stock reference at 1 ml/L.
- The generated target is missing the final `Distilled water` ingredient.
- The generated target is missing DSMZ 1136 preparation context for nitrogen
  bubbling and N2-filled septum tubes.
- The generated target has no target-organism, growth-metric, reference, or
  evidence blocks. These are optional in the schema and the DSMZ/KOMODO source
  recipe does not by itself establish a specific growth outcome.
- No search for publication growth evidence was needed to decide the source
  recipe defects above.

## Findings

### Major

1. **The trace-element stock is flattened into the final medium at stock
   concentrations.**
   DSMZ 1136 adds `Trace element solution SL-12` at 1 ml/L and defines the
   listed trace salts inside that stock. The generated target instead lists
   the nine SL-12 salts as final-medium `G_PER_L` ingredients at their stock
   values, omits the 1 ml/L stock row, and omits the stock/final-medium
   boundary. Future fixes belong in
   `data/normalized_yaml/bacterial/rhodovulum_kholense_medium.yaml` and
   `data/normalized_yaml/bacterial/KOMODO_1136_RHODOVULUM_KHOLENSE_medium.yaml`,
   or in the DSMZ resolver that copied these rows into the KOMODO owner.

2. **The generated target omits source water rows.**
   DSMZ 1136 has 1000 ml distilled water in the final medium and another
   1000 ml distilled water in the SL-12 stock. Neither boundary is represented
   in the target: the final water row is absent and the stock water row is
   lost with the rest of the stock structure. Future fixes share the normalized
   DSMZ/KOMODO ownership in finding 1; if `mediadive_2280_Trace_element_solution_SL-12.yaml`
   is reused for the stock, its water entry also needs unit review because it
   is currently `1000 PERCENT_V_V`.

3. **The generated merge drops DSMZ preparation instructions.**
   The direct DSMZ normalized owner already records pH adjustment and N2
   bubbling / N2-filled septum tubes from the DSMZ source, but the generated
   merge inherits the KOMODO owner, which lacks `preparation_steps`. If the
   two normalized owners remain in the same `SOURCE_DUPLICATE` group, the
   KOMODO owner needs the DSMZ preparation context or
   `src/culturemech/merge/merger.py` needs a tie-break or field merge that
   preserves source preparation when two exact duplicate owners are merged.

## Recommended Edits

1. Repair the DSMZ owner,
   `data/normalized_yaml/bacterial/rhodovulum_kholense_medium.yaml`, so its
   final medium contains only the seven DSMZ final salts/extract/carbon rows,
   `Trace element solution SL-12` at 1 ml/L, and `Distilled water` at
   1000 ml/L, with the inspected DSMZ preparation steps intact.
2. Repair the KOMODO duplicate owner,
   `data/normalized_yaml/bacterial/KOMODO_1136_RHODOVULUM_KHOLENSE_medium.yaml`,
   so its copied DSMZ composition keeps the same final-stock boundary and
   preparation context as DSMZ Medium 1136, or adjust the DSMZ resolver so a
   regenerated KOMODO owner cannot flatten nested DSMZ solutions.
3. Review `data/normalized_yaml/bacterial/mediadive_2280_Trace_element_solution_SL-12.yaml`
   before reusing it as the authoritative stock record because its component
   salts match DSMZ SL-12, but its water row is represented as
   `1000 PERCENT_V_V`.
4. Rerun the merge generation after normalized-owner repair and verify that
   `data/merge_yaml/merged/rhodovulum_kholense_medium__b03507f6.yaml` or its
   successor keeps the stock row, final water row, and DSMZ preparation steps.
5. Keep the JCM J649 / TOGO M664 records as separate generated targets until a
   curator resolves the JCM `M497` stock cross-reference and can compare it
   chemically with DSMZ SL-12.

## Follow-up Checks

- `just validate data/normalized_yaml/bacterial/rhodovulum_kholense_medium.yaml`
- `just validate data/normalized_yaml/bacterial/KOMODO_1136_RHODOVULUM_KHOLENSE_medium.yaml`
- `just validate data/normalized_yaml/bacterial/mediadive_2280_Trace_element_solution_SL-12.yaml`
- `just validate-strict data/normalized_yaml/bacterial/rhodovulum_kholense_medium.yaml data/normalized_yaml/bacterial/KOMODO_1136_RHODOVULUM_KHOLENSE_medium.yaml`
- The focused open-schema, strict, reference, and term validators used in this
  review against the regenerated merged target.
- A manual diff of the regenerated target against the DSMZ Medium 1136 PDF or
  REST payload, specifically checking that SL-12 remains a 1 ml/L stock and is
  not flattened into final grams per liter.
- An exact ignored-inclusive search for the JCM `GRMD=649`, TOGO `M664`, and
  DSMZ `1136` source IDs before adding or rejecting cross-source
  `SOURCE_DUPLICATE` or variant links.

## Additional Notes

- A slug ignored-inclusive search over `data/normalized_yaml` and
  `data/merge_yaml/merged` found three generated same-name records:
  this DSMZ/KOMODO target, `RHODOVULUM_KHOLENSE_MEDIUM.yaml`, and
  `rhodovulum_kholense_medium__ea7c96fd.yaml`. It also found the four
  normalized owners for KOMODO 1136, DSMZ 1136, JCM J649, and TOGO M664.
- `src/culturemech/merge/merge_recipes.py` groups normalized records by
  ingredient fingerprint and documents that concentration, pH, temperature,
  and preparation differences are ignored. The separate JCM/TOGO generated
  siblings arise here because their imported stock reference changes the
  ingredient identity enough to put them in separate fingerprint groups, not
  because this target proved a curated non-duplicate relation.

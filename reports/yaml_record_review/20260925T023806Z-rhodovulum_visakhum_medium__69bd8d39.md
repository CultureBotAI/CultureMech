# YAML Record Review: rhodovulum_visakhum_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/rhodovulum_visakhum_medium__69bd8d39.yaml
- Started UTC: 2026-09-25T02:36:35Z
- Finished UTC: 2026-09-25T02:38:05Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record:

- Path: `data/merge_yaml/merged/rhodovulum_visakhum_medium__69bd8d39.yaml`
- ID: `CultureMech:009907`
- Label: `rhodovulum_visakhum_medium`
- Source identity: TOGO Medium M516, original source JCM `JCM_M515`
- Source CURIE: `TOGO:M516`
- Generated from:
  - `data/normalized_yaml/bacterial/TOGO_M516_Rhodovulum_Visakhum_Medium.yaml`

The target is a generated singleton merge. Future fixes belong in the
normalized TOGO owner or in TOGO importer logic, followed by regeneration of
`data/merge_yaml/merged/`.

## Validation

| Check | Result |
| --- | --- |
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/rhodovulum_visakhum_medium__69bd8d39.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/rhodovulum_visakhum_medium__69bd8d39.yaml --out /private/tmp/rhodovulum_visakhum_medium__69bd8d39.strict.tsv --workers 1 --quiet` | Passed; 0 error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/rhodovulum_visakhum_medium__69bd8d39.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were present. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/rhodovulum_visakhum_medium__69bd8d39.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: `just validate-history` validates standalone `history/` records, not embedded `MediaRecipe.curation_history` entries. |

## Identity and Grounding

- The record ID, normalized label, bacterial category, liquid physical state,
  and TOGO M516 source identity are internally aligned.
- TOGO M516 resolves to `Rhodovulum Visakhum Medium`, carries source pH 6.8,
  and records original source `JCM_M515` with the JCM `GRMD=515` URL.
- The live JCM `GRMD=515` page was available and confirmed the same JCM
  formulation with the same pH, 1 ml Vitamin B12 stock, and 1 ml Trace
  element solution SL8 stock. JCM points to Medium 190 for the SL8 stock;
  TOGO points to M183, which is its JCM M190 import.
- MediaDive JCM J515 is a third capture of the same JCM source, but the
  generated MediaDive JCM sibling is not linked to this TOGO target because
  the two importers damaged the stock representation in different ways.
- The first exact `M183` search also matched neighboring IDs such as
  `TOGO:M1830`; that output was discarded. The rerun ignored-inclusive search
  used a numeric boundary on `TOGO:M183` and exact terms for
  `TOGO_M183_LYS_Medium`, `Trace element solution SL8 (see Medium [M183])`,
  `JCM_M515`, `TOGO:M516`, and `mediadive.medium:J515` under
  `data/normalized_yaml` and `data/merge_yaml/merged`. It found the M516 owner
  and target, the JCM J515 owner and sibling, the M183 LYS owner and target,
  and several other exact M183 stock references.

## Evidence

- TOGO M516 supports the base ingredients captured by the target: 1 L
  distilled water, yeast extract 0.4 g, NaCl 20 g, CaCl2 x 2 H2O 0.15 g,
  KH2PO4 0.5 g, NH4Cl 0.6 g, MgCl2 x 6 H2O 1 g, sodium pyruvate 3 g, and
  sorbitol 3 g.
- TOGO M516 supports adding `Vitamin B12 (20 ug/ml) (filter--sterilized)` at
  1 ml, not a direct final `Vitamin B12` row at `1 G_PER_L`.
- TOGO M516 supports a 1 ml `Trace element solution SL8 (see Medium [M183])`
  stock addition, not a `G_PER_L` placeholder.
- The inspected TOGO M183 payload resolves the M516 stock cross-reference:
  M183 is LYS Medium / JCM M190 and contains a `Trace element solution SL8`
  subcomponent with 1 L distilled water, molybdate, borate, manganese,
  cobalt, nickel, copper, zinc, FeCl2, and EDTA.
- TOGO M516 supports pH 6.8, and the generated target omits `ph_value`.

## Completeness

- The generated target imports `Distilled water` 1 L as `1 G_PER_L`.
- The generated target imports both post-autoclave additions as data that a
  reader cannot execute: Vitamin B12 is a final ingredient at `1 G_PER_L`,
  and SL8 is an empty `Unknown solution` at `1 G_PER_L`.
- The generated target lacks the source pH 6.8.
- The generated target lacks the TOGO M516 / JCM J515 duplicate relationship.
- The generated target has no target-organism, growth-metric, reference, or
  evidence blocks. These are optional in the schema and TOGO M516 does not by
  itself establish a specific growth outcome.

## Findings

### Major

1. **The source volumes were imported as grams per liter.**
   TOGO M516 gives 1 L final water, 1 ml Vitamin B12 stock, and 1 ml SL8
   stock. The generated target encodes each as `G_PER_L`, turning water and
   solution additions into nonsensical mass concentrations. Future fixes
   belong in
   `data/normalized_yaml/bacterial/TOGO_M516_Rhodovulum_Visakhum_Medium.yaml`
   or in `src/culturemech/import/togo_importer.py`.

2. **The M183 SL8 stock cross-reference was not resolved.**
   The source points to `Medium [M183]`, and the inspected TOGO M183 payload
   contains the referenced `Trace element solution SL8` composition. The
   target keeps an `Unknown solution` with `composition: []`, so the required
   trace metals are absent.

3. **The Vitamin B12 stock is represented as pure Vitamin B12.**
   TOGO M516 says to add 1 ml of a 20 ug/ml filter-sterilized Vitamin B12
   solution, but the target's final ingredient row says `Vitamin B12` at
   `1 G_PER_L`. The stock concentration and solution boundary must be
   preserved.

4. **The source pH and post-autoclave addition context are missing.**
   TOGO M516 carries pH 6.8 and separates Vitamin B12 plus SL8 into a second
   post-autoclave block. The target has no `ph_value` and no
   `preparation_steps`, so it loses the condition and preparation boundary
   needed to follow the JCM/TOGO recipe.

5. **The JCM/TOGO duplicate set remains split.**
   TOGO M516, live JCM `GRMD=515`, and MediaDive J515 all describe the same
   JCM formulation, but the TOGO and MediaDive owners generate as separate
   records because TOGO keeps an unresolved M183 stock reference while
   MediaDive flattens the SL8 stock into direct ingredient rows. Future
   curation should repair both stock representations and then add a
   `SOURCE_DUPLICATE` relationship between the TOGO M516 and JCM J515 owners.

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/TOGO_M516_Rhodovulum_Visakhum_Medium.yaml`
   so final water remains a volume row, Vitamin B12 remains a 1 ml
   filter-sterilized stock addition, and SL8 remains a 1 ml stock reference.
2. Teach `src/culturemech/import/togo_importer.py` to preserve source `ml`
   and `L` units and to resolve `reference_media_id: M183` to the reusable
   SL8 stock instead of emitting `composition: []`.
3. Add pH 6.8 and the post-autoclave addition boundary from TOGO M516.
4. Review `data/normalized_yaml/bacterial/JCM_J515_RHODOVULUM_VISAKHUM_MEDIUM.yaml`
   so its MediaDive J515 import keeps the Vitamin B12 and SL8 stock additions
   instead of flattening SL8; then add reciprocal `SOURCE_DUPLICATE` metadata
   between the repaired TOGO and JCM owners.
5. Regenerate `data/merge_yaml/merged/` and confirm this generated record or
   its successor merges with the JCM J515 generated record rather than
   remaining a singleton.

## Follow-up Checks

- `just validate data/normalized_yaml/bacterial/TOGO_M516_Rhodovulum_Visakhum_Medium.yaml`
- `just validate data/normalized_yaml/bacterial/JCM_J515_RHODOVULUM_VISAKHUM_MEDIUM.yaml`
- The focused open-schema, strict, reference, and term validators used in this
  review against the regenerated generated target.
- A manual comparison of repaired TOGO M516 against the inspected TOGO M516
  and M183 payloads, specifically checking 1 L water, 1 ml Vitamin B12, 1 ml
  SL8, M183 stock resolution, pH 6.8, and post-autoclave scoping.
- An exact ignored-inclusive search with numeric boundaries for `TOGO:M183`,
  `TOGO:M516`, and `mediadive.medium:J515` before adding duplicate links.

## Additional Notes

- The normalized TOGO M183 owner,
  `data/normalized_yaml/bacterial/TOGO_M183_LYS_Medium.yaml`, is not a ready
  stock-solution record. It flattens the M183 main medium and embedded SL8
  stock into a single ingredient list with the same unit errors, so a repair
  should use the inspected M183 stock subcomponent rather than copying the
  current normalized LYS record wholesale.

# YAML Record Review: Methanosaeta Thermophila Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanosaeta_thermophila_medium__c680f26f.yaml`
- Started UTC: 2026-09-24T04:39:47Z
- Finished UTC: 2026-09-24T04:41:50Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:009347`, the generated one-source merge for TOGO medium
`M279`, `Methanosaeta Thermophila Medium`, derived from
`data/normalized_yaml/archaea/TOGO_M279_Methanosaeta_Thermophila_Medium.yaml`.

The generated merge was produced on fingerprint
`c680f26f491e29c826c479c8be2110cb4a655f9c50b23e3ffa8a608d2f404e14` from
`TOGO_M279_Methanosaeta_Thermophila_Medium`.

## Validation

- LinkML open validation: passed with `No issues found`.
- Strict schema validation: passed with 0 error rows; the TSV contained the
  header only.
- Reference validation: passed; 1 file validated, 0 total checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked. The available history validator
  targets standalone files under `history/`, not `MediaRecipe.curation_history`
  blocks embedded in generated YAML.

## Identity and Grounding

The top-level TOGO identity is correct: `TOGO:M279` corresponds to JCM medium
285, `METHANOSAETA THERMOPHILA MEDIUM`, at final pH 6.5.

The generated file is stale relative to its normalized owner. The owner carries
a September 10, 2026 `RESOLVED_TOGO_JCM_ARCHAEA_SCORE15` curation that restores
defined typing, pH 6.5, nested Trace minerals and Trace vitamins compositions,
percent-stock additions, preparation steps, and references to TOGO `M279`, JCM
285, JCM 151, and JCM 197. The generated merge still reflects the pre-repair
empty-stub state from August 6, 2026.

Grounding is also stale in the generated file: `MgCl2 x 6H2O` lacks a
`mediaingredientmech_chebi_term`, `CO2` is present twice as gas rows, and
seven actual post-autoclave solution additions remain detached as empty
`solutions` stubs.

## Evidence

### Supported by inspected sources

- TOGO `M279` supports 1 L distilled water, 0.5 g NH4Cl, 0.4 g K2HPO4,
  0.1 g MgCl2 x 6H2O, 1 mg resazurin, 10 ml Trace minerals, and N2/CO2
  gassing in the main recipe.
- TOGO `M279` supports post-autoclave additions of 20 ml 5 percent NaHCO3,
  10 ml 1 percent CaCl2 x 2H2O, 10 ml 33 percent sodium acetate, 10 ml
  1.42 percent Coenzyme M, 5 ml 5 percent Na2S x 9H2O, 10 ml Trace vitamins,
  and a 30 percent CO2 gas phase.
- JCM 285 is the original source for TOGO `M279`; it supports the same base rows
  and post-autoclave stock-addition list.
- JCM 151 supports the trace-minerals stock now nested in the repaired
  normalized owner, including nitrilotriacetic acid, MgSO4 x 7H2O,
  MnSO4 x H2O, NaCl, FeSO4 x 7H2O, CoSO4 x 7H2O, CaCl2 x 2H2O,
  ZnSO4 x 7H2O, CuSO4 x 5H2O, AlK(SO4)2, H3BO3, Na2MoO4 x 2H2O, and
  distilled water.
- JCM 197 supports the trace-vitamin stock now nested in the repaired
  normalized owner.
- The repaired owner preserves source preparation steps for N2/CO2 cooling,
  dispensing and autoclaving under N2/CO2, adding anaerobic sterile stocks after
  autoclaving, and bringing the headspace to 30 percent CO2.

### Unsupported or over-scoped in the YAML

- The generated record still marks the medium as `COMPLEX` and `UNDEFINED`
  even though the immediate source is a fully defined JCM formulation and the
  normalized owner is now `DEFINED`.
- `Distilled water` is `1 G_PER_L` and resazurin is `1 G_PER_L`; the source and
  repaired owner record those rows as 1 L water and 1 mg resazurin.
- Trace minerals, Trace vitamins, 5 percent NaHCO3, 1 percent CaCl2 x 2H2O,
  33 percent sodium acetate, 1.42 percent Coenzyme M, and 5 percent Na2S x
  9H2O are empty top-level `solutions` with `G_PER_L` units instead of
  `ML_PER_L` addition volumes and nested stock compositions.
- The generated file has no `preparation_steps`, so every JCM preparation
  instruction is absent from the generated output.
- Schema-defaulted gas rows remain in the generated top-level ingredient list,
  including duplicated carbon dioxide rows, instead of the curated `N2`/`CO2`
  representation in the owner.

## Completeness

The generated file is not complete as a record of TOGO `M279` or JCM 285. It
has only the main direct ingredients and seven empty stock stubs. The repaired
owner already supplies the missing trace-mineral, trace-vitamin, percent-stock,
and preparation detail, but those improvements have not been propagated into
`data/merge_yaml/merged`.

Empty optional fields were not treated as defects.

## Findings

- `needs curation`: the generated merge is stale relative to the September 10,
  2026 repair in its normalized owner.
- `needs curation`: `Distilled water` and `Resazurin` have incorrect
  `G_PER_L` units in the generated file.
- `needs curation`: seven stock additions have empty compositions and wrong
  `G_PER_L` units in the generated `solutions` array.
- `needs curation`: trace-mineral and trace-vitamin formulas restored in the
  owner are absent from the generated record.
- `needs curation`: all JCM preparation steps restored in the owner are absent
  from the generated record.
- `needs curation`: medium typing remains `COMPLEX`/`UNDEFINED` in the
  generated file despite the repaired `DEFINED` owner.
- `needs curation`: generated gas rows and ingredient grounding predate the
  owner repair.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/methanosaeta_thermophila_medium__c680f26f.yaml`
  from `data/normalized_yaml/archaea/TOGO_M279_Methanosaeta_Thermophila_Medium.yaml`.
- Verify that the regenerated merge keeps `ML_PER_L` on the seven solution
  additions and preserves nested `composition` rows for Trace minerals and
  Trace vitamins.
- Preserve owner preparation steps and pH 6.5 in the generated output.
- Drop duplicate/default gas artifacts that are not present in the repaired
  owner.
- Refresh ingredient grounding after regeneration so the generated merge has
  the same CHEBI-keyed fields as the owner.

## Follow-up Checks

- Re-run the focused LinkML, strict, reference, and term validators after
  regeneration.
- Diff the regenerated merge against the repaired owner and verify that no
  empty `composition: []` stock remains.
- Spot-check the regenerated Trace minerals and Trace vitamins blocks against
  JCM 151 and JCM 197.

## Additional Notes

The direct MediaDive/JCM rendering of JCM 285 is reviewed separately in
`data/merge_yaml/merged/methanosaeta_thermophila_medium__8ffe3304.yaml`.

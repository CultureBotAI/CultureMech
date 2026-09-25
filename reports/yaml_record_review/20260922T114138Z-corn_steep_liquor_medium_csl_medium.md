# YAML Record Review: Corn steep liquor medium (CSL medium)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/corn_steep_liquor_medium_csl_medium.yaml`
- Started UTC: 2026-09-22T11:39:20Z
- Finished UTC: 2026-09-22T11:41:38Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009439`
- Normalized source: `data/normalized_yaml/bacterial/corn_steep_liquor_medium_csl_medium.yaml`
- Source identity: TOGO M2901, `Corn steep liquor medium (CSL medium)`
- Current generated merge: one source recipe, `corn_steep_liquor_medium_csl_medium`

## Validation

- Open schema validation: pass.
- Strict validation: pass.
- Reference validation: pass with 0 checks.
- Term validation: pass.
- Embedded `curation_history`: not checked by the standalone history validator.

## Identity and Grounding

- TOGO M2901 is a one-liter CSL medium with KH2PO4, K2HPO4, magnesium chloride hexahydrate, ammonium sulfate, ferric chloride hexahydrate, xylose, and corn steep liquor.
- TOGO encodes `FeCl3.6H2O` as 20 mg, not 20 g.
- A gitignore-independent search over `data` found no additional M2901 or `CultureMech:009439` YAML records.

## Evidence

- TOGO API checked: `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2901`.
- Local normalized owner checked: `data/normalized_yaml/bacterial/corn_steep_liquor_medium_csl_medium.yaml`.
- The CultureMech concentration enum was checked and includes `MG_PER_L`.

## Completeness

- The bacterial category, liquid state, complex undefined type, and seven non-water source ingredients are present.
- Most gram quantities match TOGO's one-liter recipe exactly.
- No source-catalogue duplicate or variant relationship was found.

## Findings

1. `FeCl3.6H2O` is overstated by 1000x: TOGO lists 20 mg, but the YAML stores `20 G_PER_L`.
2. `Distilled water` is stored as `1 G_PER_L`; TOGO encodes one liter of water.
3. The source URL is present only in `notes`, with no `references` entry.

## Recommended Edits

1. Change `FeCl3.6H2O` to `20 MG_PER_L` or the equivalent `0.02 G_PER_L`.
2. Change `Distilled water` from `1 G_PER_L` to a source-preserving one-liter water ingredient.
3. Add the TOGO M2901 URL to `references`.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after repairing and regenerating.
- Re-query TOGO M2901 and confirm all seven non-water ingredients retain the source quantities and units.

## Additional Notes

- No schema-level defect was found.
- The ferric chloride unit conversion is the only large concentration error in the checked source payload.

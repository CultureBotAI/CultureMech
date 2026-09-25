# YAML Record Review: Microlunatus Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/microlunatus_medium__d418d8ae.yaml`
- Started UTC: 2026-09-24T06:24:11Z
- Finished UTC: 2026-09-24T06:24:11Z
- Verdict: pass with minor issues

## Target

- Reviewed merged record `data/merge_yaml/merged/microlunatus_medium__d418d8ae.yaml`.
- Editable normalized sources: `data/normalized_yaml/bacterial/TOGO_M1703_Microlunatus_Medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M204_Microlunatus_Medium.yaml`.
- TOGO media: `TOGO:M1703` from NBRC 909 and `TOGO:M204` from JCM 211.

## Validation

- LinkML open-schema validation: passed; `No issues found`.
- Strict validation: passed with 0 errors; `validate_strict.py` scanned 1 file and produced only the TSV header.
- Reference validation: passed; 1 file, 0 checks.
- Term validation: passed.
- Embedded history: Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The duplicate merge is appropriate: JCM Medium 211 and NBRC Medium 909 have the same solid Microlunatus formula.
- This is a distinct solid-agar formula, not a duplicate of the liquid 0.5 g/L KH2PO4 Microlunatus records reviewed immediately before it.
- The simple salts, glucose, monosodium glutamate, magnesium sulfate heptahydrate, and agar are grounded correctly.
- Peptone and yeast extract are acceptable ungrounded undefined components.

## Evidence

- TOGO M1703 and TOGO M204 both list 1 L distilled water, MgSO4 x 7 H2O 0.1 g, Yeast extract 0.5 g, KH2PO4 0.44 g, ammonium sulfate 0.1 g, Monosodium glutamate 0.5 g, Glucose 0.5 g, Agar 15 g, Peptone 0.5 g, and pH 7.0.
- JCM Medium 211 lists the same rows and says to adjust pH to 7.0.
- The generated YAML carries all nine ingredient rows with the correct non-water concentrations and `physical_state: SOLID_AGAR`.

## Completeness

- The core ingredient recipe is complete.
- The source water row is present but has the wrong unit.
- The source pH 7.0 was not retained as `ph_value`.

## Findings

- The source `Distilled water 1 L` row was imported as `1 G_PER_L`; both normalized TOGO sources have the same unit defect.
- The generated merge omits the pH 7.0 carried by both TOGO payloads and the JCM/NBRC provider pages.

## Recommended Edits

- Correct distilled-water concentration in both normalized TOGO sources from `1 G_PER_L` to a volume unit that preserves the source `1 L`.
- Restore pH 7.0 in both normalized TOGO sources.
- Regenerate `data/merge_yaml/merged/microlunatus_medium__d418d8ae.yaml`.

## Follow-up Checks

- Re-run focused open-schema, strict, reference, and term validators for `data/merge_yaml/merged/microlunatus_medium__d418d8ae.yaml`.
- Verify the regenerated record still has `physical_state: SOLID_AGAR` and 15 g/L Agar.
- Verify KH2PO4 remains 0.44 g/L, not 0.5 g/L.
- Verify the water row is no longer `1 G_PER_L` and `ph_value` is 7.0.

## Additional Notes

- Empty optional fields were not treated as defects.

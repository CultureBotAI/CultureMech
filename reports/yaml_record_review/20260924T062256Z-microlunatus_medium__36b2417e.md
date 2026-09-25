# YAML Record Review: Microlunatus Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/microlunatus_medium__36b2417e.yaml`
- Started UTC: 2026-09-24T06:22:56Z
- Finished UTC: 2026-09-24T06:22:56Z
- Verdict: pass with minor issues

## Target

- Reviewed merged record `data/merge_yaml/merged/microlunatus_medium__36b2417e.yaml`.
- Editable normalized source: `data/normalized_yaml/bacterial/TOGO_M1622_Microlunatus_Medium.yaml`.
- TOGO medium: `TOGO:M1622`, Microlunatus Medium.
- Original source: NBRC medium 822.

## Validation

- LinkML open-schema validation: passed; `No issues found`.
- Strict validation: passed with 0 errors; `validate_strict.py` scanned 1 file and produced only the TSV header.
- Reference validation: passed; 1 file, 0 checks.
- Term validation: passed.
- Embedded history: Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The recipe identity is coherent: TOGO `M1622`, NBRC `NO=822`, and the YAML all point to Microlunatus Medium.
- The generated ingredient names and amounts match NBRC's seven solutes.
- Magnesium sulfate is correctly grounded to the heptahydrate term, and the simple salts plus glucose and sodium glutamate are grounded.
- Peptone and yeast extract are acceptable ungrounded undefined components.

## Evidence

- NBRC Medium 822 lists Glucose 0.5 g, Peptone 0.5 g, Yeast extract 0.5 g, Sodium glutamate 0.5 g, KH2PO4 0.5 g, ammonium sulfate 0.1 g, MgSO4 x 7 H2O 0.1 g, Distilled water 1 L, and pH 7.0.
- TOGO M1622 carries the same composition and pH.
- The generated YAML carries the seven solutes with matching g/L values and has `ph_value: 7.0`.

## Completeness

- The core seven-solute recipe is complete.
- The final pH is represented as `ph_value`.
- The source water row is present but has the wrong unit.

## Findings

- The source `Distilled water 1 L` row was imported as `1 G_PER_L`; it should be represented as 1 L or 1000 ml per liter.
- The normalized source has the same water-unit defect, so this should be fixed in `data/normalized_yaml/bacterial/TOGO_M1622_Microlunatus_Medium.yaml` and then regenerated.

## Recommended Edits

- Correct the distilled-water concentration in `data/normalized_yaml/bacterial/TOGO_M1622_Microlunatus_Medium.yaml` from `1 G_PER_L` to a volume unit that preserves the source `1 L`.
- Regenerate `data/merge_yaml/merged/microlunatus_medium__36b2417e.yaml`.

## Follow-up Checks

- Re-run focused open-schema, strict, reference, and term validators for `data/merge_yaml/merged/microlunatus_medium__36b2417e.yaml`.
- Verify the seven solute concentrations remain unchanged.
- Verify the solvent row is no longer `1 G_PER_L`.

## Additional Notes

- Empty optional fields were not treated as defects.

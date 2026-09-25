# YAML Record Review: modified_desulfovibrio_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_desulfovibrio_medium__a639c769.yaml
- Started UTC: 2026-09-24T10:49:14Z
- Finished UTC: 2026-09-24T10:50:07Z
- Verdict: needs curation

## Target

Generated record `CultureMech:010288` for TOGO medium `M870`, `Modified Desulfovibrio Medium`, which mirrors JCM medium 834.

The generated record merges `TOGO_M870_Modified_Desulfovibrio_Medium` from `data/normalized_yaml/bacterial/TOGO_M870_Modified_Desulfovibrio_Medium.yaml`. The generated YAML was compared with that maintained owner, TOGO `M870`, JCM 834, and JCM 389.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed with no error rows.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct TOGO `M870` identity and preserves the JCM 834 beef-extract supplement.

The generated artifact is stale relative to a 2026-09-06 `RESOLVED_JCM_MORE_SCORE40_GRAPH` repair in `data/normalized_yaml/bacterial/TOGO_M870_Modified_Desulfovibrio_Medium.yaml`. The maintained owner now resolves JCM 834 to JCM 389 plus 3.0 g/L `Beef extract (BD-Difco)`, adds the base-medium rows, captures the JCM 389 pH range and preparation steps, and grounds yeast extract and beef extract to FOODON.

## Evidence

TOGO `M870` points to JCM 834 and records 3 g/L `Beef extract (BD-Difco)` plus a reference to the Desulfovibrio base medium. The TOGO comment and JCM 834 page specify that the actual formula is JCM Medium 389 supplemented with 3 g/L BD-Difco beef extract.

JCM 389 lists K2HPO4, NH4Cl, Na2SO4, MgSO4 x 7 H2O, CaCl2 x 2 H2O, sodium lactate, yeast extract, FeSO4 x 7 H2O, sodium thioglycolate, ascorbic acid, resazurin, and 1 L distilled water, with N2 handling, pH adjustment, and autoclaving instructions.

The generated record still contains only `Beef extract (BD-Difco)` plus an empty `DESULFOVIBRIO MEDIUM (see Medium [M384])` solution. The repaired maintained owner contains the JCM 389 base rows, the beef-extract supplement, `ph_range: 6.8-7.0`, the JCM 389 preparation sequence, and a water row.

## Completeness

The generated record preserves the TOGO/JCM wrapper identity and the 3 g/L beef-extract supplement.

It is incomplete for the entire referenced base medium, pH, preparation, solvent, and FOODON enrichment that already exist in the maintained owner.

## Findings

- High: The generated YAML is stale relative to the 2026-09-06 repair of `TOGO_M870_Modified_Desulfovibrio_Medium.yaml`.
- High: Twelve JCM 389 base-medium rows are absent from the generated artifact, leaving only the JCM 834 beef-extract supplement.
- High: The generated `DESULFOVIBRIO MEDIUM (see Medium [M384])` solution is empty, so it does not represent the referenced JCM 389 formula.
- Medium: JCM 389 pH and preparation details, including N2 handling and autoclaving, are absent.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/modified_desulfovibrio_medium__a639c769.yaml` from the repaired 2026-09-06 maintained owner.
- Confirm that the regenerated artifact keeps the 3.0 g/L `Beef extract (BD-Difco)` supplement, all JCM 389 base ingredients, the 1 L distilled-water row, `ph_range: 6.8-7.0`, and the explicit preparation steps.
- Preserve the FOODON grounding for yeast extract and beef extract during regeneration.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated record against JCM 834 and JCM 389 to verify the base-medium rows, the beef-extract supplement, the water row, and the pH and N2 handling instructions.

## Additional Notes

None found.

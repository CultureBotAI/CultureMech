# YAML Record Review: desulfobotulus_par22n_medium__bd3fccf7

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfobotulus_par22n_medium__bd3fccf7.yaml`
- Started UTC: 2026-09-22T18:21:36Z
- Finished UTC: 2026-09-22T18:21:36Z
- Verdict: needs curation

## Target

Generated bacterial `desulfobotulus_par22n_medium` record for MediaDive/JCM Medium J1193.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is correctly grounded to MediaDive medium J1193 / JCM Medium J1193, `DESULFOBOTULUS PAR22N MEDIUM`.

An exact ignored-file search found one separate TOGO M1278 same-name import. This generated record has a single `merged_from` source and is the MediaDive/JCM import.

The complex, semi-defined, liquid classification is supported by the 0.2 g/L yeast-extract ingredient in the live JCM recipe.

## Evidence

The generated basal rows match MediaDive's J1193 normalization against a 1017 ml main solution: NaCl, KH2PO4, Na2SO4, Na2CO3, NH4Cl, MgCl2 x 6 H2O, KCl, and yeast extract are scaled from the JCM table.

The source then adds 1 ml each of FeCl2 solution, Trace element solution, and Fe-Ni-WO-Se solution before 1 L water; after autoclaving it adds 1 ml Vitamin solution, 5 ml 1 M Sodium octanoate solution, and 8 ml 5% Na2S x 9H2O solution per liter.

The generated record has no FeCl2, Trace element, or Fe-Ni-WO-Se stock solution records. Their contents are flattened into the top-level final medium at stock concentrations: HCl, FeCl2 x 4 H2O, JCM 187 trace metals, FeSO4, NiSO4, Na2WO4, and Na2SeO3 are all final rows.

The post-cooling additions are also mis-modeled. Sodium octanoate is `5` G_PER_L from a 5 ml stock addition, Na2S x 9 H2O is `8` G_PER_L from an 8 ml stock addition, and the only `solutions` entry is a Vitamin solution stub with concentration `1` G_PER_L and no composition.

The 1 L source water row is absent.

## Completeness

The pH 9.0 target and the anaerobic boil, N2 cooling, Hungate-tube dispensing, autoclaving, and aseptic post-cooling addition instructions survived.

The post-cooling table rows did not survive as structured milliliter additions, and the link from the Vitamin solution row to JCM 1157 is represented only as a local MediaDive solution identifier in an empty stub.

## Findings

- Major issue: FeCl2, Trace element, and Fe-Ni-WO-Se solutions are not nested under `solutions`.
- Major issue: FeCl2, JCM 187 trace elements, and Fe-Ni-WO-Se metals are flattened as top-level ingredients at stock concentrations.
- Major issue: 1 M Sodium octanoate solution and 5% Na2S x 9 H2O solution use raw source milliliter volumes as G_PER_L final concentrations.
- Major issue: the JCM 1157 Vitamin solution is an empty G_PER_L stub rather than a 1 ml stock addition with composition.
- Major issue: the 1 L source water component is missing.
- Minor issue: the post-cooling source table was reduced to prose ending in a colon.

## Recommended Edits

- Rebuild the normalized source record from JCM 1193, MediaDive J1193, or TOGO M1278 with explicit stock solutions and milliliter additions.
- Keep FeCl2 solution, Trace element solution, Fe-Ni-WO-Se solution, Vitamin solution, 1 M Sodium octanoate, and 5% Na2S x 9H2O as stock additions rather than top-level final ingredients.
- Move the JCM 187 and JCM 1121 stock contents into nested stock records.
- Resolve the JCM 1157 Vitamin solution and attach its formula to the 1 ml Vitamin solution addition.
- Restore the 1 L distilled-water row or an equivalent main-solution total-volume representation.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after restructuring the record.
- Confirm sodium octanoate and sulfide final concentrations are derived from stock strength and addition volume.
- Confirm FeSO4, NiSO4, Na2WO4, and Na2SeO3 remain local to Fe-Ni-WO-Se solution scope.
- Compare the direct MediaDive/JCM record against TOGO M1278 before any later same-name merge.

## Additional Notes

JCM GRMD 1193, MediaDive REST medium J1193, and TOGO M1278 were reachable during review.

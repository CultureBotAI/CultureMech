# YAML Record Review: desulfobacterium_cetonicum_medium__33e412bb

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfobacterium_cetonicum_medium__33e412bb.yaml`
- Started UTC: 2026-09-22T18:08:36Z
- Finished UTC: 2026-09-22T18:08:36Z
- Verdict: needs curation

## Target

Generated bacterial `desulfobacterium_cetonicum_medium` record for MediaDive/JCM Medium J395.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is correctly grounded to MediaDive medium J395 / JCM Medium J395, `DESULFOBACTERIUM CETONICUM MEDIUM`.

An exact ignored-file search found KOMODO 612 and TOGO M391 records for the same named medium, plus a KOMODO 612 merge into `DESULFOSARCINA_CETONICA_MEDIUM`, but this fingerprinted generated record has a single `merged_from` source and is the MediaDive/JCM import.

The defined, bacterial, liquid classification is supported by the live JCM and MediaDive sources.

## Evidence

The generated final-medium macronutrient rows match MediaDive's J395 normalization against a 1002 ml main solution: Na2SO4, KH2PO4, NH4Cl, NaCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, sodium butyrate, NaHCO3, resazurin, and Na2S x 9 H2O are scaled from the JCM table.

The JCM table also adds 1 ml FeCl2 solution and 1 ml Trace element solution, both referencing JCM 187.

MediaDive preserves those as two solution additions, but the generated YAML has no `solutions` block. Instead, FeCl2-stock HCl, FeCl2 x 4 H2O, and the Trace element solution's ZnCl2, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, and Na2MoO4 rows were flattened into top-level final-medium ingredients at their stock-solution concentrations.

The 1 L source water row is absent from the generated ingredient list.

## Completeness

The JCM preparation paragraph survived, including the N2-CO2 autoclave atmosphere, separate sodium butyrate sterilization in 10 ml water under N2, filter-sterilized 5% NaHCO3 handling, anaerobically autoclaved 5% Na2S x 9H2O addition prior to inoculation, and final pH check.

The stock additives and the source water volume did not survive structurally, so the record cannot distinguish final-medium rows from FeCl2 and trace-element stock-bottle rows.

The top-level `ph_value` is `7.3`, which is consistent with MediaDive's scalar pH but loses the live JCM instruction to check that the final pH is 7.2-7.4.

## Findings

- Major issue: JCM 187 FeCl2 solution and Trace element solution are not represented as 1 ml stock additions under `solutions`.
- Major issue: FeCl2-stock HCl, FeCl2 x 4 H2O, and all trace metals are flattened as final-medium ingredients at full stock concentration.
- Major issue: the 1 L source water component is missing.
- Minor issue: source pH 7.2-7.4 is reduced to `ph_value: 7.3`.

## Recommended Edits

- Rebuild the normalized source record from JCM 395 or MediaDive REST J395 with explicit JCM 187 FeCl2 and Trace element stock solution additions.
- Move FeCl2 x 4 H2O, HCl, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O under their respective `solutions` records.
- Restore the 1 L distilled-water row or an equivalent total-volume representation for the main solution.
- Store the final pH instruction as a 7.2-7.4 range instead of a single value.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after restructuring the record.
- Confirm the corrected top-level ingredient list contains no full-strength JCM 187 stock ingredients.
- Confirm sodium butyrate, NaHCO3, and Na2S x 9 H2O remain represented at their final source amounts while preserving their separate sterilization and addition instructions.
- Confirm the KOMODO and TOGO records remain separate unless their sources agree at the ingredient and preparation level.

## Additional Notes

JCM GRMD 395 and MediaDive REST medium J395 were reachable during review.

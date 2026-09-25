# YAML Record Review: NAUTILIA ABYSSI MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/nautilia_abyssi_medium__0d5af3f0.yaml
- Started UTC: 2026-09-24T16:57:46Z
- Finished UTC: 2026-09-24T16:57:47Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:003040` for direct MediaDive/JCM J695, `NAUTILIA ABYSSI MEDIUM`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to MediaDive/JCM J695.

An exact repository search including ignored and hidden files for `CultureMech:003040`, `GRMD=695`, `mediadive.medium:J695`, `nautilia_abyssi_medium`, and `NAUTILIA ABYSSI` found this direct JCM generated record plus its normalized owner and an active TOGO M715 import of the same JCM Medium 695 source.

`Sulfur` is grounded to sulfur atom rather than elemental sulfur, and `NaNO3` still has a legacy `mediaingredientmech_term` link.

## Evidence

JCM Medium 695 lists 25.0 g NaCl, 1.0 g NaNO3, 0.33 g NH4Cl, 0.33 g KCl, 0.33 g CaCl2 . 2H2O, 0.33 g MgCl2 . 6H2O, 1.95 g MES, 1.0 mg resazurin, 10.0 ml Trace minerals, 12.0 g sulfur powder, and 1.0 L distilled water.

The source instructs mixing components except sulfur, adjusting pH to 6.0, autoclaving under an N2 atmosphere, distributing medium into culture vessels containing sulfur under an H2-CO2 4:1 gas mixture, sealing with butyl rubber stoppers, aseptically and anaerobically adding 10.0 ml Trace vitamins, 20.0 ml 2% KH2PO4, and 10.0 ml 5% Na2S . 9H2O per liter, then pressurizing inoculated culture vessels to 200 kPa H2-CO2 4:1.

The MediaDive record models the 10.0 ml Trace minerals row as a stock solution and carries the final post-autoclave additions as milliliter rows.

## Completeness

The generated record has no solution entries, omits the 1.0 L distilled-water row, flattens Trace minerals into the final recipe, and flattens the post-autoclave vitamins, phosphate, and sulfide additions into direct gram-per-liter ingredients.

The generated preparation text preserves the main procedure and gas regime.

## Findings

- Major: The main JCM rows were normalized against MediaDive's 1050 ml final volume, so source rows such as 25.0 g NaCl and 12.0 g sulfur powder became `23.8095 G_PER_L` and `11.4286 G_PER_L`.
- Major: Trace minerals was flattened into direct ingredients and its internal NaCl and CaCl2 rows were merged with base-medium rows, yielding unsupported summed concentrations.
- Major: The 10.0 ml Trace vitamins, 20.0 ml 2% KH2PO4, and 10.0 ml 5% Na2S x 9 H2O post-autoclave additions are represented as 10, 20, and 10 `G_PER_L`.
- Major: The source 1.0 L distilled-water row is missing.
- Major: The direct JCM/MediaDive J695 owner is unlinked from the active TOGO M715 import of the same source.
- Minor: Sulfur and the NaNO3 MediaIngredientMech link need grounding cleanup.

## Recommended Edits

- In `data/normalized_yaml/bacterial/nautilia_abyssi_medium.yaml`, keep JCM source masses as 1 L recipe amounts instead of concentrations normalized to MediaDive's 1050 ml internal volume.
- Restore Trace minerals as a 10.0 ml stock addition and preserve its internal composition separately.
- Restore Trace vitamins, 2% KH2PO4, and 5% Na2S x 9 H2O as post-autoclave milliliter additions.
- Restore distilled water as the 1.0 L preparation volume.
- Link or collapse the direct JCM/MediaDive J695 owner with TOGO M715.
- Ground sulfur powder to elemental sulfur and refresh the NaNO3 MediaIngredientMech CHEBI link.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/nautilia_abyssi_medium__0d5af3f0.yaml` and verify no top-level ingredient is normalized to 1050 ml.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored and hidden files for `TOGO:M715`, `mediadive.medium:J695`, and `GRMD=695` to verify the duplicate source records are linked or collapsed.

## Additional Notes

None found.

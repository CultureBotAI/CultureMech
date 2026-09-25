# YAML Record Review: thermoplasma_kamchatkensis_medium__57d65c1c

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoplasma_kamchatkensis_medium__57d65c1c.yaml
- Started UTC: 2026-09-25T12:00:30Z
- Finished UTC: 2026-09-25T12:00:30Z
- Verdict: pass with minor issues

## Target

Reviewed `CultureMech:002405`, `thermoplasma_kamchatkensis_medium`, generated from JCM Medium J1239 / MediaDive `mediadive.medium:J1239`.

## Validation

- LinkML schema: Passed with `linkml-validate`; no issues found.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermoplasma_kamchatkensis_medium__57d65c1c.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The record is grounded to the correct JCM source, J1239, "THERMOPLASMA KAMCHATKENSIS MEDIUM", and the generated scalar concentrations and pH match MediaDive and the direct JCM page.

## Evidence

- JCM J1239 lists 3.0 g KH2PO4, 1.0 g MgSO4 x 7 H2O, 0.25 g CaCl2 x 2 H2O, 0.2 g (NH4)2SO4, 0.1 g yeast extract, 5.0 g sucrose, 4.0 g sulfur powder, and 1 L distilled water.
- JCM J1239 adjusts pH to 2.5 with 10 N H2SO4, separately autoclaves yeast extract and sucrose, steams sulfur for 3 hr on each of 3 successive days, distributes medium into vessels containing sulfur, replaces the gas phase with N2-CO2 at 4:1, and seals with butyl rubber stoppers.

## Completeness

The source ingredient masses, pH value, and full preparation text are present. The only direct source ingredient missing from the generated record is the 1 L distilled-water row.

## Findings

- The 1 L `Distilled water` row from JCM J1239 is absent.
- `Sulfur` loses the source "powder" attribute and is grounded to CHEBI:26833, `sulfur atom`, which is less specific than elemental sulfur powder.
- The N2-CO2 gas phase is preserved in prose but is not structured as a gas-ratio condition.

## Recommended Edits

- Add the 1 L distilled-water row.
- Preserve the sulfur powder attribute, and consider a more specific sulfur grounding if one is available.
- Keep the source N2-CO2 4:1 gas instruction if gas-ratio fields are later added.

## Follow-up Checks

- Verify that `Sulfur` should not be modeled as a solid phase or vessel additive distinct from dissolved ingredients.
- Keep the pH-adjustment H2SO4 in preparation text unless the schema gains a dedicated pH reagent field.

## Additional Notes

No target-organism evidence was reviewed. The exact source search included ignored and hidden files and found only the expected JCM J1239 normalized source for this record.

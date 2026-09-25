# YAML Record Review: thermoplasma_acidophilum_medium__bb19d61f

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoplasma_acidophilum_medium__bb19d61f.yaml
- Started UTC: 2026-09-25T12:00:28Z
- Finished UTC: 2026-09-25T12:00:28Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:010388`, `thermoplasma_acidophilum_medium`, generated from TOGO Medium M963 and ultimately sourced from JCM Medium J917.

## Validation

- LinkML schema: Passed; the command exited 0 with no diagnostics.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermoplasma_acidophilum_medium__bb19d61f.strict.tsv` contained only the header.
- Reference validation: Passed; the command exited 0 with no diagnostics.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The TOGO source and the underlying JCM page both identify the target as JCM Medium 917, "THERMOPLASMA ACIDOPHILUM MEDIUM", at pH 2.0.

## Evidence

- JCM J917 lists 1.0 g BD-Difco yeast extract, 1.0 g BD-Difco casamino acids, 1.3 g (NH4)2SO4, 0.3 g KH2PO4, 0.25 g MgSO4 x 7 H2O, 0.2 g NaCl, 0.05 g CaCl2 x 2 H2O, and 1 L distilled water.
- JCM J917 instructs pH adjustment to 2.0 with 10 N H2SO4.
- MediaDive J917 reports the same scalar ingredient set and pH 2.0.

## Completeness

The scalar non-water ingredients match JCM J917. The water row is unit-corrupted as 1 G_PER_L, the pH 2.0 instruction is only implicit through a variable H2SO4 ingredient, and there are no `preparation_steps` for the acid adjustment.

## Findings

- `Distilled water` 1 G_PER_L copies the source `1 L` volume as a mass concentration.
- The source pH 2.0 is absent from `ph_value`.
- `H2SO4` is present as a variable top-level ingredient with no 10 N concentration, rather than as a pH-adjustment reagent in preparation.
- The record uses TOGO/JCM M963 as a separate generated medium even though the exact source search also found a direct MediaDive J917 import in `THERMOPLASMA_ACIDOPHILUM_MEDIUM.yaml`.

## Recommended Edits

- Replace the water row with a 1 L distilled-water ingredient or merge with the direct JCM J917 representation after checking which import is more complete.
- Add `ph_value: 2.0` and a preparation step for adjustment with 10 N H2SO4.
- Move or scope H2SO4 so it is not read as a direct medium solute.
- Normalize the hydrate spelling in preferred terms to the repository's ASCII style while preserving source labels in provenance if needed.

## Follow-up Checks

- Decide whether the TOGO M963 and direct JCM J917 recipes should merge into one record with both provenance edges.
- Check whether supplier names for BD-Difco yeast extract and casamino acids should be structured or retained only in preferred labels.

## Additional Notes

No target-organism evidence was reviewed. The exact source search included ignored and hidden files and found TOGO M963 plus a direct JCM J917 generated record for the same source.

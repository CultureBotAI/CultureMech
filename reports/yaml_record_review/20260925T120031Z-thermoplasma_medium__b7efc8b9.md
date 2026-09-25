# YAML Record Review: thermoplasma_medium__b7efc8b9

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoplasma_medium__b7efc8b9.yaml
- Started UTC: 2026-09-25T12:00:31Z
- Finished UTC: 2026-09-25T12:00:31Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:002541`, `thermoplasma_medium`, generated from JCM Medium J180 and merged with Picrophilus Medium J233 and DSMZ/MediaDive 1141 provenance.

## Validation

- LinkML schema: Passed with `linkml-validate`; no issues found.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermoplasma_medium__b7efc8b9.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The top-level identity points to JCM J180, "THERMOPLASMA MEDIUM". Its `merged_from` cluster also folds in JCM J233, "PICROPHILUS MEDIUM", and DSMZ 1141, "THERMOGYMNOMONAS MEDIUM"; those sources share a small ingredient signature but differ in pH, yeast-extract amount, or organism context.

## Evidence

- JCM J180 lists 0.2 g (NH4)2SO4, 3.0 g KH2PO4, 0.5 g MgSO4 x 7 H2O, 0.25 g CaCl2 x 2 H2O, 1.0 g BD-Difco yeast extract, 10.0 g glucose, and 1 L distilled water.
- JCM J180 adjusts pH to 2.0 with 10 N H2SO4, separately autoclaves yeast extract and glucose as 10% solutions, and adds them aseptically.
- JCM J233 says to use Medium No. 180 with 2.0 g/L final yeast extract and pH 1.0.
- DSMZ 1141 uses the same six non-water main ingredients as J180 but adjusts to pH 3.0 with 10 N H2SO4 and is a Thermogymnomonas medium, not a Thermoplasma variant.

## Completeness

The JCM J180 scalar ingredients and main pH/preparation sentence are mostly present, but the water row is absent, the BD-Difco yeast-extract supplier is absent, and the JCM 13583 pH 3.0 comment from J180 is missing. More importantly, the merge collapsed J233 and DSMZ 1141 into source duplicates instead of retaining their pH and formulation differences.

## Findings

- The JCM J180 1 L distilled-water row is absent.
- JCM J233 is not a source duplicate of J180 because it changes the final yeast extract from 1.0 g/L to 2.0 g/L and adjusts pH to 1.0.
- DSMZ 1141 / Thermogymnomonas is not a source duplicate of J180 because it adjusts pH to 3.0 and belongs to a different source medium.
- The JCM J180 comment for JCM 13583 pH 3.0 is absent.
- Yeast extract loses the BD-Difco source attribute.

## Recommended Edits

- Split JCM J180, JCM J233, and DSMZ 1141 into separate source records or represent J233 as a true pH/yeast-extract variant of J180, not a `SOURCE_DUPLICATE`.
- Add the JCM J180 water row and restore the JCM 13583 pH 3.0 comment.
- Preserve the BD-Difco yeast-extract attribute where possible.
- Ensure the already-reviewed `thermogymnomonas_medium.yaml` DSMZ 1141 record is the only owner of DSMZ 1141 provenance.

## Follow-up Checks

- Recompute fingerprints after including pH, water, and supplier attributes so acidophilic media with the same core salts no longer collapse.
- Check whether J233's pH 1.0 and yeast-extract 2.0 g/L should be modeled as a variant of J180 or as an independent Picrophilus parent medium.

## Additional Notes

No target-organism evidence was reviewed. The exact source search included ignored and hidden files and found JCM J180, JCM J233, DSMZ 1141, and the already-reviewed generated Thermogymnomonas record that also uses DSMZ 1141.

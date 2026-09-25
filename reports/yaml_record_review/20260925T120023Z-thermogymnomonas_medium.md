# YAML Record Review: thermogymnomonas_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermogymnomonas_medium.yaml
- Started UTC: 2026-09-25T12:00:23Z
- Finished UTC: 2026-09-25T12:00:23Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:003851`, `thermogymnomonas_medium`, generated from KOMODO Medium 1141 with a DSMZ Medium 1141 / MediaDive `mediadive.medium:1141` cross-reference.

## Validation

- LinkML schema: Passed with `linkml-validate`; no issues found.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermogymnomonas_medium.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The identity is consistent across the generated KOMODO record, MediaDive record 1141, and the DSMZ 1141 PDF: all point to "THERMOGYMNOMONAS MEDIUM" with pH 3.0.

## Evidence

- DSMZ Medium 1141 and MediaDive 1141 list 0.20 g (NH4)2SO4, 3.00 g KH2PO4, 0.50 g MgSO4 x 7 H2O, 0.25 g CaCl2 x 2 H2O, 1.00 g yeast extract, 10.00 g glucose, and 1000 ml distilled water.
- The DSMZ preparation adjusts pH to 3.0 with 10 N H2SO4.
- The DSMZ preparation separately autoclaves yeast extract and glucose as 10% solutions, then adds them aseptically to the medium.

## Completeness

The scalar salt, yeast extract, glucose, and pH rows match DSMZ 1141. The generated record omits the 1000 ml distilled-water row and has no `preparation_steps`, so the 10 N acid adjustment, separate 10% yeast extract and glucose solutions, autoclaving, and aseptic additions are not represented as preparation.

## Findings

- `Distilled water` 1000 ml is present in DSMZ 1141 and MediaDive 1141 but missing from the generated ingredient list.
- The record has no preparation steps, dropping the DSMZ instructions to adjust pH with 10 N H2SO4 and separately autoclave yeast extract and glucose as 10% solutions before aseptic addition.
- `H2SO4` is present as a variable top-level ingredient extracted from notes; this is source-backed as a pH adjustment, but its concentration of 10 N belongs in the pH-adjustment instruction rather than as an unqualified medium ingredient.
- The `Yeast extract` row loses the DSMZ "Difco" supplier attribute.

## Recommended Edits

- Add the 1000 ml distilled-water row from DSMZ 1141.
- Add preparation steps for pH adjustment with 10 N H2SO4 and separate 10% yeast extract and glucose autoclaving with aseptic addition.
- Move or scope the variable H2SO4 entry so it is clearly a pH adjustment reagent.
- Preserve the DSMZ "Difco" attribute on yeast extract if the schema can carry supplier notes.

## Follow-up Checks

- Check the separate merged `thermoplasma_medium__b7efc8b9.yaml` record that also lists `mediadive.medium:1141` as a source ID before deduplicating DSMZ 1141-derived content.
- Verify whether the KOMODO `Aerobic: No` note has any direct DSMZ 1141 support; DSMZ 1141 itself does not state anaerobic handling.

## Additional Notes

No target-organism evidence was reviewed. The exact local source search included ignored and hidden files and found KOMODO 1141, MediaDive 1141, and one separate merged Thermoplasma record that also records `mediadive.medium:1141` as a source ID; the DSMZ 1141 PDF was fetched and rendered to text for this review.

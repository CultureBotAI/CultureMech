# YAML Record Review: modified_eggerth_gagnon_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_eggerth_gagnon_medium.yaml
- Started UTC: 2026-09-24T10:52:57Z
- Finished UTC: 2026-09-24T10:53:48Z
- Verdict: needs curation

## Target

Generated record `CultureMech:001055` for DSMZ/MediaDive medium `1580`, `MODIFIED EGGERTH-GAGNON MEDIUM`.

The generated record merges `modified_eggerth_gagnon_medium` from `data/normalized_yaml/bacterial/modified_eggerth_gagnon_medium.yaml`. The generated YAML was compared with that maintained owner, MediaDive medium `1580`, and the DSMZ Medium 1580 PDF.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed with no error rows.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct DSMZ/MediaDive medium identity.

Its ingredient list is corrupted by a commercial MacConkey Agar decomposition that does not belong to DSMZ 1580. Those MacConkey-only rows are intermixed with DSMZ rows, producing duplicate peptone and agar rows and adding lactose, bile salts, sodium chloride, neutral red, and crystal violet that are absent from the DSMZ source.

## Evidence

The DSMZ Medium 1580 PDF lists 10 g peptone, 4 g Na2HPO4 x 2H2O, 2 g mucin from porcine stomach Type III, 15 g BactoAgar, and 950 ml distilled water; after autoclaving at 121 C, the medium is cooled to 50 C and 50 ml sheep blood is added aseptically.

MediaDive `1580` encodes the same six recipe rows: peptone, Na2HPO4 x 2 H2O, mucin from porcine stomach Type III, Bacto agar, 950 ml distilled water, and 50 ml sheep blood.

The generated YAML omits mucin and distilled water entirely, stores 50 ml sheep blood as `50` `G_PER_L`, and adds eight MacConkey Agar constituent rows with MicrobeNotes catalog metadata that are not supported by DSMZ 1580.

## Completeness

The generated record preserves the DSMZ identity, peptone row, phosphate row, agar row, and preparation prose.

It is incomplete for two required source rows and incorrect for the sheep-blood unit. It also contains multiple extraneous MacConkey Agar rows that should not be present in this medium.

## Findings

- High: MacConkey Agar constituent rows were injected into Modified Eggerth-Gagnon Medium even though DSMZ 1580 does not include MacConkey Agar.
- High: The 2 g/L `Mucin from porcine stomach Type III` source row is absent.
- High: The 950 ml distilled-water source row is absent.
- Medium: The source 50 ml sheep-blood addition is represented as 50 g/L.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/modified_eggerth_gagnon_medium.yaml` directly against DSMZ Medium 1580 or MediaDive `1580`.
- Remove the MacConkey Agar-derived peptone, proteose peptone, lactose monohydrate, bile salts, sodium chloride, neutral red, crystal violet, and 13.5 g/L agar rows.
- Restore 2 g/L `Mucin from porcine stomach Type III` and 950 ml/L distilled water.
- Change sheep blood from `50` `G_PER_L` to a 50 ml/L volume addition.
- Regenerate `data/merge_yaml/merged/modified_eggerth_gagnon_medium.yaml` after the maintained owner is repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated record against the DSMZ Medium 1580 PDF and MediaDive `1580` to verify peptone, Na2HPO4 x 2 H2O, mucin, BactoAgar, distilled water, sheep blood, and the 121 C and 50 C preparation instructions.

## Additional Notes

None found.

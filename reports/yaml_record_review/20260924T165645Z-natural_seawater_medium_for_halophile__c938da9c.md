# YAML Record Review: Natural Seawater Medium For Halophile

- Repository: CultureMech
- Record: data/merge_yaml/merged/natural_seawater_medium_for_halophile__c938da9c.yaml
- Started UTC: 2026-09-24T16:56:44Z
- Finished UTC: 2026-09-24T16:56:45Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:009537` for TOGO M3026, the liquid JCM M1377-1 import of `Natural Seawater Medium For Halophile`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to TOGO M3026 and original JCM M1377-1.

An exact repository search including ignored and hidden files for `TOGO:M3026`, `CultureMech:009537`, `GRMD=1377`, `JCM_M1377`, `natural_seawater_medium_for_halophile`, and `Natural_Seawater_Medium` found this liquid M3026 record plus an active TOGO M3027 solid-agar import of the same JCM 1377 page.

No incorrect CHEBI grounding was found on grounded rows. `Natural seawater`, `Yeast extract`, `Proteose peptone No. 3`, and `Casamino acids` are undefined or mixture components and are appropriately ungrounded to CHEBI.

## Evidence

JCM Medium 1377 lists 1.0 g Casamino acids, 1.0 g yeast extract, 3.0 g Proteose peptone No. 3, 1.0 g glucose, 0.05 g sodium pyruvate, 132.0 g NaCl, 0.6 g K2HPO4, and 1.0 L natural seawater.

JCM instructs adjusting pH to 7.0-7.2 and adding 20.0 g/L agar only for solid medium.

The generated record correctly omits agar from this liquid M1377-1 import.

## Completeness

The pH 7.0-7.2 adjustment is absent.

The source's 1.0 L Natural seawater volume is represented as `1 G_PER_L`.

## Findings

- Major: `Natural seawater` is mis-unitized as `1 G_PER_L` instead of the source 1.0 L volume.
- Major: The source pH 7.0-7.2 adjustment is absent.
- Major: TOGO M3026 is unlinked from TOGO M3027, the 20.0 g/L agar variant imported from the same JCM 1377 source page.

## Recommended Edits

- In `data/normalized_yaml/bacterial/natural_seawater_medium_for_halophile.yaml`, correct Natural seawater to 1.0 L.
- Add the JCM pH 7.0-7.2 adjustment.
- Link the M3026 liquid recipe with `data/normalized_yaml/bacterial/TOGO_M3027_Natural_Seawater_Medium_For_Halophile.yaml` as its solid-agar variant.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natural_seawater_medium_for_halophile__c938da9c.yaml` and verify Natural seawater is no longer `1 G_PER_L`.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored and hidden files for `TOGO:M3026`, `TOGO:M3027`, and `GRMD=1377` to verify the liquid and agar variants are linked.

## Additional Notes

None found.

# YAML Record Review: halophilic_medium__8e91af80

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halophilic_medium__8e91af80.yaml`
- Started UTC: 2026-09-23T10:58:59Z
- Finished UTC: 2026-09-23T10:59:59Z
- Verdict: needs curation

## Target

Generated merged YAML for MediaDive/DSMZ medium 1125, `HALOPHILIC MEDIUM`, merged with the KOMODO 1125 copy.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches MediaDive `mediadive.medium:1125` and the DSMZ 1125 PDF.
- An ignored-file-inclusive exact search for `mediadive.medium:1125`, `DSMZ_Medium1125.pdf`, and `halophilic_medium` found the direct DSMZ import, a KOMODO 1125 copy resolved to the same DSMZ medium, and their merged output.
- The KOMODO copy carries the same DSMZ ingredient set and is an appropriate duplicate to merge after water and preparation are reconciled.
- The MgCl2 x 6 H2O, CaCl2 x 2 H2O, salts, sucrose, and HEPES groundings are appropriate.

## Evidence

- DSMZ 1125 lists 20 g MgCl2 x 6 H2O, 5 g K2SO4, 0.1 g CaCl2 x 2 H2O, 0.1 g yeast extract, 0.5 g NH4Cl, 0.05 g KH2PO4, 0.5 g sucrose, 180 g NaCl, 6 g HEPES, and 1000 ml distilled water.
- DSMZ 1125 instructs adjustment to pH 6.5.
- MediaDive 1125 preserves the same 1000 ml distilled-water row and pH step.
- The generated merge keeps the non-water ingredient amounts and `ph_value: 6.5` but omits the water row.

## Completeness

- Missing ingredient: the explicit 1000 ml distilled-water row was dropped.
- Underspecified preparation: `Adjust to pH 6.5` is modeled as generic `MIX` instead of `ADJUST_PH`.

## Findings

1. The generated DSMZ 1125 merge omits the 1000 ml distilled-water row.
2. The pH adjustment step uses a generic `MIX` action.

## Recommended Edits

- Add distilled water with the correct 1000 ml final-volume representation.
- Change the pH preparation step to `ADJUST_PH`.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:1125`, `komodo.medium:1125`, and `DSMZ_Medium1125.pdf` after regeneration.
- Verify that the direct DSMZ 1125 import and the KOMODO 1125 copy still merge to one record after the water row is restored.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.

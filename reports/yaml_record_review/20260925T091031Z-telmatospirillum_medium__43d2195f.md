# YAML Record Review: telmatospirillum_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/telmatospirillum_medium__43d2195f.yaml`
- Started UTC: 2026-09-25T09:09:20Z
- Finished UTC: 2026-09-25T09:10:31Z
- Verdict: pass with minor issues

## Target

Reviewed generated record `CultureMech:000563` for `telmatospirillum_medium`, the DSMZ/MediaDive Medium 1126 TELMATOSPIRILLUM MEDIUM import merged from `telmatospirillum_medium.yaml` with fingerprint `43d2195fc1962f427c299ca9a2f43664b1ae83e3560e31295510d94654860a38`.

## Validation

- LinkML schema validation: Passed with `No issues found`.
- Strict validation: Passed; 1 file scanned and 0 error rows written to `/private/tmp/telmatospirillum_medium__43d2195f.strict.tsv`.
- Reference validation: Passed; 1 file validated, 0 external checks.
- Term validation: Passed.
- Embedded `curation_history`: Not checked; `just validate-history` validates standalone `history/`, not merged `MediaRecipe.curation_history`.

## Identity and Grounding

The generated `mediadive.medium:1126` grounding matches DSMZ Medium 1126, TELMATOSPIRILLUM MEDIUM. MediaDive 1126 points to the same DSMZ PDF and reports the same defined liquid formulation with a pH range of 5.5 to 6.5.

The target is a source duplicate of `data/merge_yaml/merged/TELMATOSPIRILLUM_MEDIUM.yaml`, which is KOMODO Medium 1126 copied from DSMZ Medium 1126.

## Evidence

The DSMZ Medium 1126 PDF lists K2HPO4, KH2PO4, ammonium sulfate, CaCl2, MgSO4, Na-EDTA, FeCl3 x 6 H2O, KI, CoCl2 x 6 H2O, MnCl2 x 4 H2O, ZnSO4, H3BO2, Na2MoO4 x 2 H2O, CuCl2, NiCl2 x 6 H2O, sodium citrate, and 1000 mL distilled water. The generated record preserves the 16 non-water ingredients at the correct grams-per-liter values, including the milligram trace components.

The DSMZ PDF says to prepare the medium anaerobically under nitrogen, adjust to pH 5.5 - 6.5 with 1M H3PO4, and dispense under nitrogen into sealable serum bottles or Hungate tubes. The generated preparation step preserves that instruction.

## Completeness

The target has all defined solute ingredients from DSMZ 1126. The omitted 1000 mL distilled-water carrier is not a practical curation defect for this generated record because all DSMZ solutes are already represented per liter.

No target organism evidence is present in the DSMZ recipe PDF or MediaDive recipe payload, so an empty `target_organisms` slot is not a defect here.

## Findings

- `KI` still has a legacy `mediaingredientmech_term` instead of a `mediaingredientmech_chebi_term`, even though it is already grounded to `CHEBI:8346`.
- Duplicate merging missed the KOMODO 1126 import. `data/merge_yaml/merged/TELMATOSPIRILLUM_MEDIUM.yaml` is copied from the same DSMZ 1126 formulation but is emitted separately after adding variable `H3PO4` from the pH note and collapsing the pH range to `ph_value: 6.5`.

## Recommended Edits

- Refresh the `KI` MediaIngredientMech migration in `data/normalized_yaml/bacterial/telmatospirillum_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_1126_TELMATOSPIRILLUM_MEDIUM.yaml`, then regenerate merged YAML; do not hand-edit generated merge files.
- Teach duplicate merging that the KOMODO DSMZ-1126 import remains a source duplicate when the only substantive differences are a variable pH-adjuster row extracted from a note and a single pH value derived from the same source pH range.

## Follow-up Checks

- Revalidate regenerated Telmatospirillum records with schema, strict, reference, and term validators.
- Search exact `mediadive.medium:1126`, `komodo.medium:1126`, and `mediaingredientmech_term:`, including ignored files, to confirm the DSMZ/KOMODO pair no longer splits and no legacy KI link remains.

## Additional Notes

Exact identity and legacy-link searches used `rg --no-ignore --hidden`, so ignored files were included.

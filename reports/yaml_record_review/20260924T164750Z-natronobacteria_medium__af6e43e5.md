# YAML Record Review: Natronobacteria Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/natronobacteria_medium__af6e43e5.yaml
- Started UTC: 2026-09-24T16:47:49Z
- Finished UTC: 2026-09-24T16:47:50Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:008910` for TOGO M2322, a DSMZ Medium 371 solid-agar `Natronobacteria Medium` import.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to TOGO M2322 and its original DSMZ Medium 371 PDF for `NATRONOBACTERIA MEDIUM`.

An exact repository search including ignored and hidden files for `TOGO:M2322`, `TOGO:M2378`, `mediadive.medium:371`, `komodo.medium:371`, `CultureMech:008910`, `CultureMech:008962`, `DSMZ_Medium371`, and `natronobacteria_medium` found this TOGO M2322 owner, the active ATCC-derived TOGO M2378 sibling, and a direct DSMZ/KOMODO Medium 371 generated record that has already merged the local `mediadive.medium:371` and `komodo.medium:371` owners as source duplicates.

The primary `MgSO4 x 7 H2O` term is correctly grounded to magnesium sulfate heptahydrate, but its `mediaingredientmech_chebi_term` still points at generic magnesium sulfate. `NiCl2 x 6 H2O` is grounded to generic nickel dichloride.

## Evidence

The DSMZ source lists 1.00 g KH2PO4, 1.00 g KCl, 1.00 g NH4Cl, 0.24 g MgSO4 x 7 H2O, 0.17 g CaSO4 x 2 H2O, 1.00 ml Trace element solution SL-10, 20.00 g agar if necessary, 200.00 g NaCl, 1.00 g Na2-glutamate, 5.00 g yeast extract, 5.00 g Casamino acids, and 5.00 g Na2CO3 per 1000 ml.

The source instructs curators to adjust pH to 6.5 before autoclaving, sterilize Na2CO3 separately from the medium and add it after cooling, check final pH to 9.0 - 9.5, and heat and dissolve agar before adding sodium chloride when agar medium is prepared.

The generated record includes the DSMZ basal solids and correctly types the record as `SOLID_AGAR`.

## Completeness

The generated record has flattened the DSMZ Medium 320 SL-10 stock recipe into final-medium ingredients and left only a `1 G_PER_L` `Unknown solution` wrapper for the 1.00 ml SL-10 addition.

The final 1000 ml water and the 990 ml water from the SL-10 stock were merged into a single `1990.0 G_PER_L` row.

The pH range, Na2CO3 separate sterilization step, and agar-specific preparation instruction are absent.

## Findings

- Major: The 1.00 ml Trace element solution SL-10 addition is represented as a `1 G_PER_L` unknown solution, while SL-10 stock salts were flattened into direct ingredients of the final medium.
- Major: Source milligram SL-10 rows were promoted to gram-per-liter values after flattening; for example, 70 mg ZnCl2, 100 mg MnCl2 x 4 H2O, 6 mg H3BO3, 190 mg CoCl2 x 6 H2O, 2 mg CuCl2 x 2 H2O, 24 mg NiCl2 x 6 H2O, and 36 mg Na2MoO4 x 2 H2O became 70, 100, 6, 190, 2, 24, and 36 `G_PER_L`.
- Major: Final-medium and SL-10 stock water quantities have been summed into `1990.0 G_PER_L`, which is neither the DSMZ final 1000 ml volume nor a valid stock representation.
- Major: The pH 6.5 before autoclaving, final pH 9.0 - 9.5, separate Na2CO3 sterilization, post-cooling Na2CO3 addition, and agar-before-NaCl preparation instruction are absent.
- Major: TOGO M2322 is unlinked from the direct DSMZ/KOMODO Medium 371 source-duplicate family.
- Minor: One stale MediaIngredientMech CHEBI link and one broad nickel chloride grounding remain on hydrate-specific ingredients.

## Recommended Edits

- In `data/normalized_yaml/bacterial/TOGO_M2322_Natronobacteria_Medium.yaml`, restore Trace element solution SL-10 as a 1.00 ml stock addition referencing a structured DSMZ Medium 320 stock recipe instead of flattening it into final-medium ingredients.
- Remove direct final-medium SL-10 salt rows from the TOGO owner after the stock solution is represented.
- Correct water so the final medium is brought to 1000 ml and SL-10 keeps its own 990 ml stock water.
- Add the DSMZ pH and preparation instructions for pH 6.5 before autoclaving, separately sterilized Na2CO3, final pH 9.0 - 9.5, and agar preparation.
- Link or collapse the TOGO M2322 import with the existing direct DSMZ/KOMODO Medium 371 source-duplicate family.
- Refresh hydrate-specific CHEBI and MediaIngredientMech grounding on MgSO4 x 7 H2O and NiCl2 x 6 H2O.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natronobacteria_medium__af6e43e5.yaml` and verify only the 1.00 ml SL-10 stock addition remains in the final recipe.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored and hidden files for `TOGO:M2322`, `mediadive.medium:371`, and `komodo.medium:371` to verify the source duplicates are linked or collapsed.

## Additional Notes

None found.

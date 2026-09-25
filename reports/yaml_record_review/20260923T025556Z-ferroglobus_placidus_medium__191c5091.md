# YAML Record Review: ferroglobus_placidus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ferroglobus_placidus_medium__191c5091.yaml
- Started UTC: 2026-09-23T02:54:24Z
- Finished UTC: 2026-09-23T02:55:56Z
- Verdict: needs curation

## Target

CultureMech:009221 is the generated merged record for TOGO Medium M2666, `Ferroglobus Placidus Medium`, whose original URL is DSMZ Medium 730.

DSMZ 730 defines a liquid medium made by combining Solution A, Solution B, Solution C, Solution D, and Solution E, then adjusting the complete medium to pH 7.2. Solution A contains seawater salts, KNO3, 10 ml Modified Wolin's mineral solution, and water. Solution B contains Na2CO3 in 30 ml water. Solution C is 1 ml Wolin's vitamin solution. Solution D is Na-pyruvate in 10 ml water. Solution E is Na2S x 9 H2O in 10 ml water.

## Validation

- LinkML open-schema validation: pass; `linkml-validate` reported `No issues found`.
- Strict schema validation: pass; `scripts/validate_strict.py` reported 0 files with errors and 0 total error rows.
- Reference validation: pass; the reference validator scanned the file and reported 0 checks.
- Term validation: pass; `linkml-term-validator` exited 0 and reported `Validation passed`.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded history entries in generated MediaRecipe YAML.

## Identity and Grounding

The CultureMech identifier, normalized name, and `TOGO:M2666` medium term point to the intended TogoMedium import.

The generated record carries plausible CHEBI grounding for most specific salts and vitamins, but `N2 gas` is ungrounded even though adjacent `Nitrogen gas` is grounded to `CHEBI:17997`.

`MgSO4 x 7 H2O` has the correct primary `term` as `CHEBI:31795`, but its `mediaingredientmech_chebi_term` still points at generic `CHEBI:32599`; the source history records a 2026-06-10 primary-term fix that did not update the MediaIngredientMech CHEBI link.

## Evidence

The generated record has flattened all Togo M2666 subcomponents into top-level ingredients and then kept separate `solutions` stubs with empty or externalized compositions. That loses the fact that Modified Wolin's mineral solution is a 10 ml addition to Solution A, Solution C is a vitamin stock, Solution D is a pyruvate stock, and Solution E is a sulfide stock.

Stock and solvent rows are consequently nonsensical in the generated ingredients. Distilled water from Solution A, Modified Wolin's mineral solution, Solution B, Wolin's vitamin solution, Solution D, and Solution E is merged to `2980.0` g/L. NaCl and CaCl2 x 2 H2O from Solution A are merged with the full-strength Modified Wolin's mineral stock rows. Trace selenium and tungsten rows that are milligram quantities in DSMZ and MediaDive appear as `0.3` and `0.4` g/L in the Togo-derived generated record, and vitamin stock quantities such as 2 mg biotin and 10 mg pyridoxine-HCl appear as `2` and `10` g/L.

The Togo payload diverges from the DSMZ 730 PDF and the MediaDive DSMZ 730 REST payload before CultureMech import: Togo M2666 uses 940 ml Solution A plus 10 ml Solution C, while DSMZ and MediaDive use 950 ml Solution A plus 1 ml Solution C. The generated record inherits the Togo values.

## Completeness

The generated record is not composition-complete for DSMZ 730 because it does not preserve the five-solution medium recipe and it overstates stock contents as if they were final gram-per-liter values.

It also omits the explicit pH 7.2 value present in DSMZ and in the parallel MediaDive DSMZ 730 import.

## Findings

1. The Togo import flattens Solution A through Solution E and Modified Wolin's mineral solution into one ingredient list, which destroys the source solution hierarchy.
2. Multiple source milliliter or milligram quantities are represented as `G_PER_L` ingredient concentrations without the required stock-volume and mg-to-g scaling.
3. Togo M2666 itself disagrees with DSMZ 730 on the Solution A and Solution C volumes, so this record should be reconciled against the DSMZ source PDF or the MediaDive DSMZ 730 payload.
4. `N2 gas` is ungrounded despite duplicating the grounded `Nitrogen gas` ingredient.
5. `MgSO4 x 7 H2O` has mismatched primary and MediaIngredientMech CHEBI terms after the heptahydrate regrounding.

## Recommended Edits

1. Prefer the native DSMZ 730 import or recurate the Togo record against DSMZ 730, preserving Solution A, B, C, D, E, and Modified Wolin's mineral solution as nested stocks.
2. Correct all stock-volume and milligram conversions before flattening any stock constituents.
3. Restore pH 7.2 if this TOGO-derived record remains.
4. Ground `N2 gas` to `CHEBI:17997` or merge it with the existing `Nitrogen gas` entry.
5. Update the `MgSO4 x 7 H2O` MediaIngredientMech CHEBI link to match `CHEBI:31795`.

## Follow-up Checks

- Re-run open-schema, strict-schema, reference, and term validation after recurating the record.
- Confirm the corrected record does not contain `Distilled water` as `2980.0` g/L or vitamin mg quantities as multi-gram-per-liter ingredients.
- Confirm the final record preserves DSMZ pH 7.2 and the intended Solution A through E volumes.

## Additional Notes

The Togo M2666 API fetch initially failed inside the sandbox with DNS resolution error `Could not resolve host: togomedium.org`; the fetch succeeded after rerunning `curl -L` with escalated network access.

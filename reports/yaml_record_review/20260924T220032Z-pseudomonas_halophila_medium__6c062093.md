# YAML Record Review: pseudomonas_halophila_medium__6c062093

- Repository: CultureMech
- Record: data/merge_yaml/merged/pseudomonas_halophila_medium__6c062093.yaml
- Started UTC: 2026-09-24T22:00:32Z
- Finished UTC: 2026-09-24T22:00:32Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:005583`, the generated bacterial liquid `PSEUDOMONAS HALOPHILA MEDIUM` record merged from `data/normalized_yaml/bacterial/pseudomonas_halophila_medium.yaml`, a KOMODO Medium 470 import enriched from DSMZ/MediaDive Medium 470.

## Validation

- LinkML validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `scripts/validate_strict.py` scanned one file and reported zero `ERROR` rows.
- Reference validation: Passed; `linkml-reference-validator` validated one file and reported zero reference checks.
- Term validation: Passed; `linkml-term-validator` exited 0.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The intended identity is DSMZ/MediaDive Medium 470, `PSEUDOMONAS HALOPHILA MEDIUM`. An exact ignored YAML search for `mediadive.medium:470`, `DSMZ_Medium470`, `DSMZ Medium: 470`, and `pseudomonas_halophila_medium` found this KOMODO branch, a direct DSMZ 470 branch, a direct JCM `J433` branch, a TOGO `M433` branch, and an ignored generated test output for the same name.

## Evidence

MediaDive 470 models the final 1 L recipe as 900 ml Solution A plus 100 ml Solution B. Solution A contains 46.8 g NaCl, 39.4 g MgSO4 x 7 H2O, 1 g NH4Cl, 5 g glycerol, 1 ml Trace element solution SL-10, 10 ml Vitamin solution, and 890 ml distilled water. Solution B contains 1 g KH2PO4 and 100 ml distilled water. SL-10 is a separate 1 L stock containing 10 ml 25% HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 990 ml water; the Vitamin solution is another 1 L stock.

## Completeness

The generated KOMODO record loses every solution boundary. It stores Solution A's stock-strength salt values, Solution B's stock-strength KH2PO4 value, SL-10's stock-strength minerals, and the Vitamin solution's stock-strength vitamins all as if they were final-medium g/L concentrations.

## Findings

- Solution A values are not diluted into the final 1 L recipe: NaCl is 51.9423 g/L instead of 46.8 g/L, MgSO4 x 7 H2O is 43.7292 g/L instead of 39.4 g/L, NH4Cl is 1.10988 g/L instead of 1 g/L, and glycerol is 5.54939 g/L instead of 5 g/L.
- Solution B is missing as a 100 ml/L component, and KH2PO4 is represented as the 10 g/L Solution B stock concentration instead of 1 g/L in the final medium.
- The 1 ml SL-10 addition and 10 ml Vitamin solution addition are absent; their internal HCl, trace salts, and vitamins are listed as final top-level ingredients.
- The 890 ml Solution A water, 100 ml Solution B water, 990 ml SL-10 water, and 1000 ml vitamin-stock water rows are all absent.
- The DSMZ, JCM, TOGO, and KOMODO source branches for this same recipe remain split across multiple generated records.

## Recommended Edits

- Repair the KOMODO, direct DSMZ, direct JCM, and TOGO normalized records so DSMZ/MediaDive 470 keeps Solution A and Solution B as 900 ml/L and 100 ml/L solution components.
- Nest SL-10 and Vitamin solution under Solution A at 1 ml per 900 ml and 10 ml per 900 ml, or otherwise preserve enough solution structure that their components are not interpreted as final-medium concentrations.
- Preserve each water row inside the solution where it belongs instead of omitting it or merging all solution waters into one top-level ingredient.
- Regenerate `data/merge_yaml/merged` and verify that `mediadive.medium:470`, JCM `J433`, TOGO `M433`, and KOMODO 470 coalesce into one canonical record.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merged record.
- Repeat exact ignored YAML searches for `mediadive.medium:470`, `DSMZ_Medium470`, and `pseudomonas_halophila_medium` to verify that no stale duplicate branch remains.

## Additional Notes

None.

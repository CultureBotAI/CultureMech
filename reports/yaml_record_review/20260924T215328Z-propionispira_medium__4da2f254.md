# YAML Record Review: propionispira_medium__4da2f254

- Repository: CultureMech
- Record: data/merge_yaml/merged/propionispira_medium__4da2f254.yaml
- Started UTC: 2026-09-24T21:53:28Z
- Finished UTC: 2026-09-24T21:53:28Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:001306`, the generated bacterial liquid `PROPIONISPIRA MEDIUM` record merged from one direct MediaDive/DSMZ normalized input, `data/normalized_yaml/bacterial/propionispira_medium.yaml`.

## Validation

- LinkML validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `scripts/validate_strict.py` scanned one file and reported zero `ERROR` rows.
- Reference validation: Passed; `linkml-reference-validator` validated one file and reported zero reference checks.
- Term validation: Passed; `linkml-term-validator` exited 0.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The direct DSMZ identity is clear: MediaDive Medium 207 is `PROPIONISPIRA MEDIUM`, pH 7.2. An exact ignored YAML search for `mediadive.medium:207`, `DSMZ_Medium207`, `DSMZ, ID: 207`, and `propionispira_medium` found this direct branch and a second generated `PROPIONISPIRA_MEDIUM.yaml` branch from `KOMODO_207_PROPIONISPIRA_medium.yaml`; both point to DSMZ/MediaDive 207 and should be reconciled.

## Evidence

MediaDive REST for medium 207 reports a 1000 ml main solution with KH2PO4, Na2HPO4 x 12 H2O, NH4Cl, MgCl2 x 6 H2O, 10 ml Trace element solution, 1.5 mg FeSO4 x 7 H2O, 5 ml Wolin's vitamin solution, 1 mg resazurin, NaHCO3, yeast extract, Na-lactate, Na2S x 9 H2O, and 1000 ml distilled water.

The same payload defines `Trace element solution` as a separate 1000 ml stock containing NTA, FeCl2 x 4 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnCl2, CuCl2, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, NaCl, Na2SeO3 x 5 H2O, and 1000 ml water. It defines `Wolin's vitamin solution` as a separate 1000 ml stock with biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium D-(+)-pantothenate, vitamin B12, p-Aminobenzoic acid, (DL)-alpha-Lipoic acid, and 1000 ml water.

## Completeness

The record has the main dry-salt and complex additions at the expected values, but it omits the main water and both stock additions. It flattens every trace-element and Wolin vitamin stock component into the final medium at stock strength, so several ingredients are present at concentrations 100x to 200x higher than intended for the final 10 ml/L and 5 ml/L stock additions.

## Findings

- The generated recipe lacks the 10 ml/L `Trace element solution` addition and the 5 ml/L `Wolin's vitamin solution` addition even though both are explicit in the MediaDive 207 main recipe.
- NTA, FeCl2 x 4 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnCl2, CuCl2, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, NaCl, and Na2SeO3 x 5 H2O belong inside the 10 ml/L trace-element stock but are modeled as final-medium g/L ingredients.
- Biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium D-(+)-pantothenate, vitamin B12, p-Aminobenzoic acid, and (DL)-alpha-Lipoic acid belong inside the 5 ml/L Wolin stock but are modeled as final-medium g/L ingredients.
- The main 1000 ml distilled water, trace-element stock water, and Wolin stock water are all absent.
- The direct DSMZ record is split from the generated KOMODO 207 `PROPIONISPIRA_MEDIUM.yaml` output for the same DSMZ medium.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/propionispira_medium.yaml` by adding the main water, moving the MediaDive `Trace element solution` and `Wolin's vitamin solution` recipes into nested `solutions`, and keeping only the 10 ml/L and 5 ml/L solution additions in the final medium.
- Repair the KOMODO 207 sibling or replace it with an alias of the repaired direct DSMZ record so `mediadive.medium:207` emits one merged output.
- Regenerate `data/merge_yaml/merged` and confirm that the final concentrations of trace salts and vitamins reflect dilution from 10 ml/L and 5 ml/L stocks rather than stock-strength values.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merged record.
- Repeat the exact ignored YAML search for `mediadive.medium:207` and `propionispira_medium` to verify that the direct DSMZ and KOMODO representations were deduplicated.

## Additional Notes

None.

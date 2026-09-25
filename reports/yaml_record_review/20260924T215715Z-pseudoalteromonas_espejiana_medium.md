# YAML Record Review: pseudoalteromonas_espejiana_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/pseudoalteromonas_espejiana_medium.yaml
- Started UTC: 2026-09-24T21:57:15Z
- Finished UTC: 2026-09-24T21:57:15Z
- Verdict: pass with minor issues

## Target

Reviewed `CultureMech:001247`, the generated bacterial `PSEUDOALTEROMONAS ESPEJIANA  MEDIUM` record merged from one direct MediaDive/DSMZ normalized input, `data/normalized_yaml/bacterial/pseudoalteromonas_espejiana_medium.yaml`.

## Validation

- LinkML validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `scripts/validate_strict.py` scanned one file and reported zero `ERROR` rows.
- Reference validation: Passed; `linkml-reference-validator` validated one file and reported zero reference checks.
- Term validation: Passed; `linkml-term-validator` exited 0.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The DSMZ/MediaDive identity is clean: MediaDive Medium 1810 is `PSEUDOALTEROMONAS ESPEJIANA  MEDIUM`, and the generated record is grounded to `mediadive.medium:1810`. An exact ignored YAML search for `mediadive.medium:1810`, `DSMZ, ID: 1810`, and `pseudoalteromonas_espejiana_medium` found only this generated output and its direct normalized source.

## Evidence

MediaDive 1810 reports one 1000 ml main solution with 8 g Nutrient broth, 0.7 g KCl, 1.5 g CaCl2 x 2 H2O, 12 g MgSO4 x 7 H2O, 26 g NaCl, optional 15 g agar, 1000 ml distilled water, pH 7.0, and autoclaving at 121 C for 15 min.

The generated record preserves the required solute amounts, pH, agar amount, and autoclave instruction.

## Completeness

The generated record is usable for the main DSMZ 1810 salt and nutrient recipe, but it omits the 1000 ml distilled water row. It also drops MediaDive's `Difco 234000` attribute on Nutrient broth and reduces the optional agar flag to a free-text `Optional ingredient` note while making the overall record `SOLID_AGAR`.

## Findings

- Minor: the DSMZ/MediaDive 1000 ml distilled water row is missing.
- Minor: the Nutrient broth row loses the source attribute `Difco 234000`.
- Minor: agar is marked optional by MediaDive, but the generated recipe encodes a single `SOLID_AGAR` physical state with no parallel liquid variant.

## Recommended Edits

- Add a 1000 ml distilled water row and retain the `Difco 234000` nutrient-broth attribute as ingredient evidence if this direct record is revisited.
- Consider splitting the optional agar branch from the liquid recipe, or clarify that `SOLID_AGAR` is the agar-containing form of a recipe whose source marks agar optional.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation if the normalized source is edited and `data/merge_yaml/merged` is regenerated.
- Repeat the exact ignored YAML search for `mediadive.medium:1810` and `pseudoalteromonas_espejiana_medium` to confirm that no duplicate DSMZ 1810 branch is introduced.

## Additional Notes

None.

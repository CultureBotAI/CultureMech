# YAML Record Review: rhizomonas_medium__1bd5219e

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rhizomonas_medium__1bd5219e.yaml`
- Started UTC: 2026-09-25T02:06:44Z
- Finished UTC: 2026-09-25T02:07:54Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002584` for JCM Medium J222 / `mediadive.medium:J222`, generated from `data/normalized_yaml/bacterial/rhizomonas_medium.yaml`.

## Validation

- Open schema validation: passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

MediaDive J222 and the JCM GRMD 222 page both identify this target as `RHIZOMONAS MEDIUM`. An exact ignored-inclusive search for `mediadive.medium:J222` found the source ID in the direct normalized owner, this generated target, and the manifest row.

## Evidence

JCM 222 lists 5.0 g Polypepton (Nihon Pharm. Co.), 2.5 g glucose, 1.0 g K2HPO4, 0.5 g MgSO4 x 7H2O, 0.5 g KNO3, 60.0 mg Ca(NO3)2 x 4H2O, 11.0 g agar, and 1.0 L distilled water, with pH adjusted to 7.2. MediaDive J222 carries the same recipe as 5, 2.5, 1, 0.5, 0.5, 0.06, and 11 g/L plus 1000 ml distilled water and pH 7.2.

## Completeness

The generated target preserves the non-water amounts and pH but is missing one required source component.

## Findings

- `Distilled water` is missing from the owner and generated target, even though JCM 222 lists 1.0 L and MediaDive J222 lists 1000 ml.
- The source qualifier on `Polypepton (Nihon Pharm. Co.)` / MediaDive `Polypeptone` attribute `Nihon Pharm. Co.` is lost; the generated target only says `Polypeptone`.
- The `KNO3` row still carries a legacy `mediaingredientmech_term: MediaIngredientMech:000170` despite having a CHEBI primary term and a June history note claiming legacy links were replaced.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/rhizomonas_medium.yaml` by adding distilled water as 1000 ml/L and preserving the Polypepton/Polypeptone supplier qualifier.
- Replace the legacy `mediaingredientmech_term` on KNO3 with the CHEBI-keyed field used elsewhere.
- Add a direct JCM reference and repair history, then regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Confirm the regenerated target has the eight JCM components, including 1000 ml/L distilled water.
- Confirm the KNO3 row has no `mediaingredientmech_term` field.
- Re-run open schema, strict, reference, and term validation for the regenerated target.

## Additional Notes

The remaining source concentrations match JCM/MediaDive after the 60 mg calcium nitrate tetrahydrate row is normalized to 0.06 g/L.

# YAML Record Review: myca_medium__a0afdc6e

- Repository: CultureMech
- Record: data/merge_yaml/merged/myca_medium__a0afdc6e.yaml
- Started UTC: 2026-09-24T16:03:43Z
- Finished UTC: 2026-09-24T16:05:36Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/myca_medium__a0afdc6e.yaml`.

The generated record represents the direct MediaDive/JCM owner for JCM Medium
138:

- canonical `id`: `CultureMech:002497`
- canonical `media_term`: `mediadive.medium:J138`
- canonical `name`: `myca_medium`
- canonical `original_name`: `MYCA MEDIUM`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `ph_value`: `6.8`
- `ingredients`: 4
- `merged_from`: `myca_medium`

## Validation

- Open schema validation: Passed; exited 0 with no diagnostics.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The high-level JCM 138 identity is correct, but the duplicate TOGO import is
unlinked. An exact ignored-file-inclusive search for `CultureMech:002497`,
`mediadive.medium:J138`, `CultureMech:007833`, and `TOGO:M129` found two
active normalized owners for the same JCM 138 source:

- `CultureMech:002497`: `data/normalized_yaml/bacterial/myca_medium.yaml`
- `CultureMech:007833`:
  `data/normalized_yaml/bacterial/TOGO_M129_MYCA_Medium.yaml`

These owners generate two separate records, `myca_medium__a0afdc6e.yaml` and
`MYCA_MEDIUM.yaml`, despite both pointing to the current JCM Medium 138 page.

## Evidence

The current JCM 138 page lists MYCA Medium as 1.0 g Sodium DL-malate, 3.0 g
Yeast extract `(BD-Difco)`, 2.0 g Casamino acids `(BD-Difco)`, 0.5 g
ammonium sulfate, and 1.0 L Distilled water, followed by `Adjust pH to 6.8.`

The current TOGO M129 API points to `JCM_M138` and carries the same source
composition, including the 1 L distilled-water row and pH 6.8.

## Completeness

The generated direct JCM record has the four dry solutes and the pH 6.8
instruction, but it omits the 1 L distilled-water row entirely. Its active
TOGO duplicate has the complementary defect: it retains `Distilled water` but
represents the 1 L source amount as 1 g/L.

JCM's page also gives the default JCM sterilization instruction: unless
otherwise stated, sterilize media by autoclaving at 121 C for 15 min. Neither
the generated direct JCM record nor the TOGO duplicate preserves that
instruction.

## Findings

- The 1 L distilled-water ingredient is missing.
- The active TOGO M129 duplicate is unlinked and generates a separate MYCA
  record for the same JCM 138 page.
- The TOGO M129 owner preserves water with the wrong 1 g/L unit.
- The JCM default 121 C for 15 min autoclave instruction is missing.
- The TOGO M129 duplicate still has a legacy `MediaIngredientMech:000524`
  mapping for `Sodium DL--malate`.

## Recommended Edits

- Restore 1 L distilled water in `data/normalized_yaml/bacterial/myca_medium.yaml`.
- Repair `data/normalized_yaml/bacterial/TOGO_M129_MYCA_Medium.yaml` so
  distilled water is a volume, not 1 g/L.
- Link TOGO M129 to the direct JCM J138 owner as a `SOURCE_DUPLICATE`.
- Preserve JCM's default 121 C for 15 min autoclave instruction if no
  source-specific sterilization overrides it.
- Migrate the TOGO M129 `Sodium DL--malate` mapping to the CHEBI-keyed
  equivalent used by the direct JCM owner.
- Regenerate MYCA Medium after repairing the maintained owners.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the
  regenerated YAML.
- Confirm the regenerated record carries the JCM water volume.
- Confirm only one generated MYCA Medium source family remains for JCM 138.
- Confirm an ignored-file-inclusive exact search for `TOGO:M129` and
  `mediadive.medium:J138` shows the two owners linked as source duplicates.

## Additional Notes

The source composition itself is simple and stable across JCM and TOGO; the
defects are local import unit handling, missing water in the MediaDive path, and
unlinked duplicate ownership.

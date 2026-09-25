# YAML Record Review: reinforced_clostridial_medium__7bb126ee

- Repository: CultureMech
- Record: `data/merge_yaml/merged/reinforced_clostridial_medium__7bb126ee.yaml`
- Started UTC: 2026-09-25T01:49:05Z
- Finished UTC: 2026-09-25T01:50:14Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:010020` for TOGO Medium M620 / `TOGO:M620`, generated from `data/normalized_yaml/bacterial/TOGO_M620_Reinforced_Clostridial_Medium.yaml`.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

TOGO M620 cites original source `JCM_M612` and the JCM GRMD 612 URL. Exact ignored-inclusive searches for `TOGO:M620`, `JCM_M612`, and `GRMD=612` within the owner, generated target, and manifest confirmed that this generated file is the TOGO import of the same JCM Medium 612 source used by `mediadive.medium:J612`.

## Evidence

The TOGO API payload for M620 lists Distilled water at `1 L`, Agar at `15 g`, and Reinforced clostridial medium (BD-Difco) at `38 g`. The cited JCM GRMD 612 page lists the same recipe as 38.0 g Reinforced clostridial medium (BD-Difco), 15.0 g agar, and 1.0 L distilled water, and states that media should be autoclaved at 121 C for 15 min unless otherwise stated.

## Completeness

The generated record carries all three TOGO component labels, but the water amount is in the wrong unit and the record is emitted separately from the direct JCM 612 owner for the same original source.

## Findings

- The normalized TOGO owner and the generated target convert `1 L` distilled water into `1 G_PER_L` on lines 9-12. TOGO and JCM both state a volume, not a gram amount; the correct normalized concentration is 1000 `ML_PER_L`.
- The generated TOGO M620 target is an unmerged duplicate of JCM Medium J612 / `mediadive.medium:J612`. Its `notes` point to `JCM_M612` and the same GRMD 612 URL, but the merge emitted M620 under a different fingerprint because the water row was imported as `1 G_PER_L`.

## Recommended Edits

- Fix TOGO unit normalization for liter-valued water rows so `1 L` becomes 1000 `ML_PER_L`, then repair `data/normalized_yaml/bacterial/TOGO_M620_Reinforced_Clostridial_Medium.yaml`.
- Source-merge or explicitly source-link TOGO M620 with the corrected JCM Medium J612 owner.
- Regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Confirm the regenerated TOGO/JCM recipe has 38.0 g/L Reinforced clostridial medium (BD-Difco), 15.0 g/L agar, and 1000 ml/L distilled water.
- Confirm `TOGO:M620` no longer emits as a standalone generated target with a 1 g/L water row.
- Re-run open schema, strict, reference, and term validation for the regenerated target.

## Additional Notes

The current owner and generated target match for the inspected fields, so the unit fix belongs in normalized YAML or TOGO import logic before regeneration.

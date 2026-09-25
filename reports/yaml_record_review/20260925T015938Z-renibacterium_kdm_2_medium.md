# YAML Record Review: renibacterium_kdm_2_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/renibacterium_kdm_2_medium.yaml`
- Started UTC: 2026-09-25T01:57:35Z
- Finished UTC: 2026-09-25T01:59:38Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:008770` for TOGO Medium M2176 / `TOGO:M2176`, generated from `data/normalized_yaml/bacterial/TOGO_M2176_Renibacterium_KDM-2_medium.yaml`.

## Validation

- Open schema validation: passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

TOGO M2176 imports ATCC Medium 1108 as Renibacterium KDM-2 medium. Exact ignored-inclusive searches for `TOGO:M2176` and the ATCC PDF token within the owner, generated target, and manifest found the expected owner, generated target, and manifest row.

## Evidence

The ATCC 1108 PDF lists 1.0% w/v peptone, 0.05% w/v yeast extract, 0.1% w/v L-Cysteine . HCl, 1.5% w/v agar, and 20.0% w/v fetal bovine serum. It instructs curators to dissolve peptone, yeast extract, and cysteine in 80% final-volume distilled water; adjust to pH 6.5 with NaOH; add agar and heat; autoclave at 121 C for 15 minutes; cool to 45 C; and add serum at 45 C. The TOGO M2176 API carries the same component percentages, pH, and preparation comments.

## Completeness

The current generated target preserves the ATCC ingredient names but is stale relative to the repaired owner, with all percentage concentrations still under-scaled and with all pH/preparation evidence absent.

## Findings

- The generated target kept raw percent numbers as g/L: 1.0% peptone became 1 g/L instead of 10 g/L, 0.05% yeast extract became 0.05 g/L instead of 0.5 g/L, 0.1% L-Cysteine . HCl became 0.1 g/L instead of 1 g/L, and 1.5% agar became 1.5 g/L instead of 15 g/L.
- `Fetal bovine serum` is represented as `20 G_PER_L`, but ATCC lists 20.0% and directs adding serum after cooling to 45 C. The September owner repair converts this to 200 ml/L and keeps the serum as an opaque complex component.
- `Distilled water` is represented as `80 G_PER_L`, but ATCC uses 80% final-volume distilled water in the first preparation step. The repaired owner records 800 ml/L.
- The generated target lacks `ph_value: 6.5`, the ATCC preparation sequence, autoclave sterilization metadata, source notes, `data_quality_flags`, and TOGO/ATCC references already present in the maintained owner.

## Recommended Edits

- Regenerate `data/merge_yaml/merged` from `data/normalized_yaml/bacterial/TOGO_M2176_Renibacterium_KDM-2_medium.yaml` so the corrected September percent conversions and ATCC preparation metadata are emitted.
- Keep NaOH as a variable pH-adjuster because ATCC 1108 states the target pH but no final NaOH concentration.

## Follow-up Checks

- Confirm the regenerated target has peptone 10 g/L, yeast extract 0.5 g/L, L-Cysteine . HCl 1 g/L, agar 15 g/L, fetal bovine serum 200 ml/L, and distilled water 800 ml/L.
- Confirm the pH 6.5 and all six ATCC preparation steps appear in the regenerated target.
- Re-run open schema, strict, reference, and term validation for the regenerated target.

## Additional Notes

The manifest flags a variable concentration on the repaired normalized owner, but that variable amount belongs to NaOH and is source-faithful because the source only says to adjust to pH 6.5 with NaOH.

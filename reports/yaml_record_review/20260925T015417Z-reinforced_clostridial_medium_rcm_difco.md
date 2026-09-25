# YAML Record Review: reinforced_clostridial_medium_rcm_difco

- Repository: CultureMech
- Record: `data/merge_yaml/merged/reinforced_clostridial_medium_rcm_difco.yaml`
- Started UTC: 2026-09-25T01:53:15Z
- Finished UTC: 2026-09-25T01:54:17Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:009308` for TOGO Medium M2758 / `TOGO:M2758`, generated from `data/normalized_yaml/bacterial/reinforced_clostridial_medium_rcm_difco.yaml`.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

Exact ignored-inclusive searches for `TOGO:M2758` within the owner, generated target, and manifest found only `data/normalized_yaml/bacterial/reinforced_clostridial_medium_rcm_difco.yaml`, this generated target, and the manifest row. TOGO M2758 has no external `src_url` but records liquid 37 C anaerobic cultivation in Difco Reinforced Clostridial Medium.

## Evidence

The TOGO M2758 API payload lists 1 L distilled water, 3 g yeast extract, 5 g sodium chloride, 5 g dextrose, 3 g sodium acetate, 1 g soluble starch, 0.5 g agar, 0.5 g cysteine HCl, 10 g beef extract, and 10 g peptone. Its source comment describes `liquid cultures at 37 C in Reinforced Clostridial Medium (RCM) (Difco)`.

## Completeness

The Difco RCM expansion otherwise follows TOGO M2758, but the water unit and physical-state inference are wrong in the normalized owner and generated target.

## Findings

- The `Distilled water` ingredient records TOGO's `1 L` source amount as `1 G_PER_L`. This is the same liter-to-gram import error seen in nearby TOGO product records; the row should be a volume amount such as 1000 `ML_PER_L`.
- The record is marked `physical_state: SOLID_AGAR` because the formula contains 0.5 g/L agar. TOGO's comment identifies the medium as a liquid culture medium, and 0.5 g/L agar is too low to make a standard solid agar plate.
- The TOGO M2758 import lacks the source comment's 37 C temperature metadata and has no `references` block for `https://togomedium.org/medium/M2758`.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/reinforced_clostridial_medium_rcm_difco.yaml` so distilled water is volume-normalized, the record is `LIQUID`, and the 37 C TOGO comment is preserved as `temperature_value: 37.0`.
- Add `https://togomedium.org/medium/M2758` as a reference and add a curation-history entry documenting the repair.
- Regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Confirm the regenerated target still has the nine non-water Difco RCM constituents from TOGO M2758 at their original gram-per-liter amounts.
- Confirm the regenerated target has water as 1000 ml/L, not 1 g/L.
- Re-run open schema, strict, reference, and term validation for the regenerated target.

## Additional Notes

The owner and generated target match for the inspected fields, so this needs a normalized-YAML or TOGO-import correction before regeneration.

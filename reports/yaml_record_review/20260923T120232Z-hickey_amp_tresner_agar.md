# YAML Record Review: Hickey & Tresner Agar
- Repository: CultureMech
- Record: data/merge_yaml/merged/hickey_amp_tresner_agar.yaml
- Started UTC: 2026-09-23T12:01:57Z
- Finished UTC: 2026-09-23T12:02:32Z
- Verdict: needs curation

## Target

Reviewed the generated Togo M1487 / NBRC M270 record for `Hickey & Tresner Agar` at `data/merge_yaml/merged/hickey_amp_tresner_agar.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hickey_amp_tresner_agar.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `TOGO:M1487`, which imports `NBRC_M270`. Togo and the NBRC source page both identify NBRC Medium 270 as Hickey & Tresner Agar, so the media identity is correct.

## Evidence

Togo M1487 and NBRC M270 list a one-liter agar containing 1 g yeast extract, 1 g beef extract, 2 g N-Z-Amine A, 10 g dextrin, 0.02 g CoCl2 x 6 H2O, 20 g agar, and 1 L distilled water at pH 7.3.

The generated record correctly keeps the yeast extract, beef extract, N-Z-Amine A, dextrin, and agar masses. It serializes the 1 L distilled-water row as `1 G_PER_L`, omits `ph_value: 7.3`, and maps cobalt chloride hexahydrate to `CHEBI:35696` / `cobalt dichloride`, which loses the explicitly hydrated source form.

## Completeness

The recipe is otherwise concise; the source does not expose additional sterilization or stock-solution instructions. The normalized source has the same water, pH, and cobalt-term problems, so these need to be curated upstream rather than fixed only by regeneration.

## Findings

- `Distilled water` uses `1 G_PER_L` instead of preserving the 1 L solvent volume.
- The pH 7.3 condition from both Togo and NBRC is missing.
- `CoCl2 x 6 H2O` is grounded as anhydrous cobalt dichloride even though the source specifies cobalt chloride hexahydrate.
- No source reference entry is present for the NBRC URL.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/hickey_amp_tresner_agar.yaml` to represent 1 L distilled water as a solvent volume.
- Add `ph_value: 7.3`.
- Re-ground `CoCl2 x 6 H2O` to the cobalt chloride hexahydrate term and keep the hydrated source label.
- Add explicit Togo and NBRC references, then regenerate the merged artifact.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Confirm the regenerated record has no `G_PER_L` unit on `Distilled water` and no anhydrous cobalt chloride grounding for the hexahydrate row.

## Additional Notes

None.
